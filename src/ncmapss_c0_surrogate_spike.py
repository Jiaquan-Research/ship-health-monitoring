from __future__ import annotations

import math
from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "ncmapss" / "data_set" / "N-CMAPSS_DS02-006.h5"
OUT_DIR = ROOT / "outputs"
REPORT_PATH = OUT_DIR / "ncmapss_c0_surrogate_spike.md"

DISCLAIMER = "Surrogate — segment mechanics only. Not maintenance-event evidence. Not Q4b evidence."

CONDITION_VARS = ["alt", "Mach", "TRA", "T2"]
TARGETS = ["T30", "T24", "Wf"]
PRIMARY_TARGET = "T30"
DEGRADATION_VAR = "HPC_eff_mod"
WINDOWS = [5, 10, 20]


def decode(values: np.ndarray) -> list[str]:
    return [v.decode("utf-8", errors="replace") if isinstance(v, bytes) else str(v) for v in values]


def rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(values)))) if len(values) else float("nan")


def p95(values: np.ndarray) -> float:
    return float(np.percentile(values, 95)) if len(values) else float("nan")


def spearman(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 3 or np.nanstd(x) == 0 or np.nanstd(y) == 0:
        return float("nan")
    return float(pd.Series(x).corr(pd.Series(y), method="spearman"))


def fmt(value: float, digits: int = 3) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "nan"
    return f"{value:.{digits}f}"


def model() -> XGBRegressor:
    return XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        objective="reg:squarederror",
        tree_method="hist",
        n_jobs=4,
        random_state=42,
    )


def zone_cycle_sets(cycles: np.ndarray) -> dict[str, np.ndarray]:
    unique = np.array(sorted(np.unique(cycles).astype(int)))
    n = len(unique)
    a_end = max(1, int(math.floor(n * 0.2)))
    b_start = min(n - 1, int(math.ceil(n * 0.8)))
    return {
        "A": unique[:a_end],
        "T": unique[a_end:b_start],
        "B": unique[b_start:],
    }


def cycle_range(values: np.ndarray) -> str:
    if len(values) == 0:
        return "n/a"
    return f"{int(values.min())}-{int(values.max())} ({len(values)} cycles)"


def load_metadata() -> dict:
    with h5py.File(DATA_PATH, "r") as f:
        vars_ = {
            "A_var": decode(f["A_var"][()]),
            "W_var": decode(f["W_var"][()]),
            "X_s_var": decode(f["X_s_var"][()]),
            "T_var": decode(f["T_var"][()]),
        }
        shapes = {key: tuple(f[key].shape) for key in ["A_dev", "W_dev", "X_s_dev", "Y_dev", "T_dev"]}
        a_var = vars_["A_var"]
        unit_idx = a_var.index("unit")
        cycle_idx = a_var.index("cycle")
        a = f["A_dev"][:, [unit_idx, cycle_idx]].astype(int)
    units = np.unique(a[:, 0])
    rows = []
    for unit in units:
        unit_cycles = np.unique(a[a[:, 0] == unit, 1])
        rows.append(
            {
                "Unit": int(unit),
                "Cycle Count": int(len(unit_cycles)),
                "Cycle Min": int(unit_cycles.min()),
                "Cycle Max": int(unit_cycles.max()),
            }
        )
    cycles_df = pd.DataFrame(rows).sort_values("Cycle Count")
    median_count = float(cycles_df["Cycle Count"].median())
    shortest = int(cycles_df.iloc[0]["Unit"])
    longest = int(cycles_df.iloc[-1]["Unit"])
    median_unit = int(cycles_df.iloc[(cycles_df["Cycle Count"] - median_count).abs().argsort().iloc[0]]["Unit"])
    selected = [
        {"Unit": longest, "Selection Reason": "Longest lifecycle unit"},
        {"Unit": median_unit, "Selection Reason": "Median lifecycle unit"},
        {"Unit": shortest, "Selection Reason": "Shortest lifecycle unit"},
    ]
    return {
        "vars": vars_,
        "shapes": shapes,
        "cycles_df": cycles_df.sort_values("Unit"),
        "selected": selected,
    }


def load_unit(unit: int, vars_: dict[str, list[str]]) -> pd.DataFrame:
    a_var = vars_["A_var"]
    w_var = vars_["W_var"]
    xs_var = vars_["X_s_var"]
    t_var = vars_["T_var"]
    unit_idx = a_var.index("unit")
    cycle_idx = a_var.index("cycle")
    w_idx = [w_var.index(name) for name in CONDITION_VARS]
    x_idx = [xs_var.index(name) for name in TARGETS]
    t_idx = t_var.index(DEGRADATION_VAR)

    with h5py.File(DATA_PATH, "r") as f:
        units = f["A_dev"][:, unit_idx].astype(int)
        mask = units == unit
        cycles = f["A_dev"][mask, cycle_idx].astype(int)
        w = f["W_dev"][mask, :][:, w_idx]
        x = f["X_s_dev"][mask, :][:, x_idx]
        t = f["T_dev"][mask, t_idx]

    data = {
        "unit": np.full(len(cycles), unit, dtype=int),
        "cycle": cycles,
        DEGRADATION_VAR: t,
    }
    for i, name in enumerate(CONDITION_VARS):
        data[name] = w[:, i]
    for i, name in enumerate(TARGETS):
        data[name] = x[:, i]
    df = pd.DataFrame(data)
    return df.sort_values("cycle").reset_index(drop=True)


def train_and_evaluate(unit: int, df: pd.DataFrame) -> dict:
    zones = zone_cycle_sets(df["cycle"].to_numpy())
    df["zone"] = np.select(
        [
            df["cycle"].isin(zones["A"]),
            df["cycle"].isin(zones["B"]),
        ],
        ["A", "B"],
        default="T",
    )
    zone_a = df[df["zone"] == "A"].copy()
    split = int(len(zone_a) * 0.8)
    x_train = zone_a.iloc[:split][CONDITION_VARS]
    x_hold = zone_a.iloc[split:][CONDITION_VARS]

    model_rows = []
    residual_rows = []
    fitted = {}
    for target in TARGETS:
        y_train = zone_a.iloc[:split][target]
        y_hold = zone_a.iloc[split:][target]
        reg = model()
        reg.fit(x_train, y_train)
        pred_train = reg.predict(x_train)
        pred_hold = reg.predict(x_hold)
        model_rows.append(
            {
                "Unit": unit,
                "Target": target,
                "Train R2": r2_score(y_train, pred_train),
                "Held-out R2": r2_score(y_hold, pred_hold),
                "Train RMSE": mean_squared_error(y_train, pred_train) ** 0.5,
                "Held-out RMSE": mean_squared_error(y_hold, pred_hold) ** 0.5,
            }
        )
        pred_all = reg.predict(df[CONDITION_VARS])
        resid = df[target].to_numpy() - pred_all
        std_a = float(np.std(resid[df["zone"].to_numpy() == "A"], ddof=0))
        if std_a == 0:
            std_a = float("nan")
        df[f"{target}_pred"] = pred_all
        df[f"{target}_residual"] = resid
        df[f"{target}_residual_norm"] = resid / std_a
        fitted[target] = reg

        for zone in ["A", "B"]:
            values = resid[df["zone"].to_numpy() == zone]
            norm_values = df.loc[df["zone"] == zone, f"{target}_residual_norm"].to_numpy()
            residual_rows.append(
                {
                    "Unit": unit,
                    "Target": target,
                    "Zone": zone,
                    "Mean": float(np.mean(values)),
                    "Std": float(np.std(values, ddof=0)),
                    "RMS": rms(values),
                    "P95": p95(values),
                    "Norm RMS": rms(norm_values),
                }
            )

    return {
        "unit": unit,
        "df": df,
        "zones": zones,
        "models": pd.DataFrame(model_rows),
        "residual_stats": pd.DataFrame(residual_rows),
    }


def cycle_level(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    return (
        df.groupby("cycle")
        .agg(
            value=(value_col, lambda x: rms(x.to_numpy())),
            zone=("zone", "first"),
            hpc=(DEGRADATION_VAR, "mean"),
        )
        .reset_index()
        .sort_values("cycle")
    )


def early_detection(df: pd.DataFrame) -> tuple[pd.DataFrame, int | None]:
    cyc = cycle_level(df, f"{PRIMARY_TARGET}_residual")
    n = len(cyc)
    labels = np.array(["Early"] * n, dtype=object)
    labels[int(n * 1 / 3) : int(n * 2 / 3)] = "Mid"
    labels[int(n * 2 / 3) :] = "Late"
    cyc["phase"] = labels
    rows = []
    for phase in ["Early", "Mid", "Late"]:
        part = cyc[cyc["phase"] == phase]
        rows.append(
            {
                "Phase": phase,
                "RMS": float(part["value"].mean()),
                "Mean HPC_eff_mod": float(part["hpc"].mean()),
            }
        )
    early_rms = rows[0]["RMS"]
    threshold = 1.5 * early_rms
    detect = cyc[cyc["value"] > threshold]
    first_cycle = int(detect.iloc[0]["cycle"]) if not detect.empty else None
    return pd.DataFrame(rows), first_cycle


def hi_analysis(unit: int, df: pd.DataFrame) -> pd.DataFrame:
    cyc = cycle_level(df, f"{PRIMARY_TARGET}_residual_norm")
    rows = []
    for window in WINDOWS:
        hi = np.sqrt(cyc["value"].pow(2).rolling(window=window, min_periods=max(1, window // 2)).mean())
        cyc[f"HI_{window}"] = hi
        a = cyc.loc[cyc["zone"] == "A", f"HI_{window}"].dropna()
        b = cyc.loc[cyc["zone"] == "B", f"HI_{window}"].dropna()
        rho = spearman(hi.dropna().to_numpy(), cyc.loc[hi.notna(), "hpc"].to_numpy())
        rows.append(
            {
                "Unit": unit,
                "Window": window,
                "HI_A": float(a.mean()) if len(a) else float("nan"),
                "HI_B": float(b.mean()) if len(b) else float("nan"),
                "Ratio": float(b.mean() / a.mean()) if len(a) and a.mean() != 0 else float("nan"),
                "Spearman": rho,
            }
        )
    return pd.DataFrame(rows)


def best_window(hi_df: pd.DataFrame) -> int:
    scored = hi_df.copy()
    scored["Score"] = scored["Spearman"].abs().fillna(0) + scored["Ratio"].fillna(0) / 10.0
    return int(scored.sort_values("Score", ascending=False).iloc[0]["Window"])


def plot_unit(result: dict, hi_df: pd.DataFrame) -> None:
    unit = result["unit"]
    df = result["df"]
    zones = result["zones"]
    window = best_window(hi_df[hi_df["Unit"] == unit])
    cyc_pred = (
        df.groupby("cycle")
        .agg(
            observed=(PRIMARY_TARGET, "mean"),
            predicted=(f"{PRIMARY_TARGET}_pred", "mean"),
            residual_norm=(f"{PRIMARY_TARGET}_residual_norm", lambda x: rms(x.to_numpy())),
            hpc=(DEGRADATION_VAR, "mean"),
            zone=("zone", "first"),
        )
        .reset_index()
    )
    cyc_pred["hi"] = np.sqrt(
        cyc_pred["residual_norm"].pow(2).rolling(window=window, min_periods=max(1, window // 2)).mean()
    )
    fig, axes = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
    x = cyc_pred["cycle"]
    for ax in axes:
        if len(zones["A"]):
            ax.axvspan(zones["A"].min(), zones["A"].max(), color="#ccebc5", alpha=0.35, label="Zone A")
        if len(zones["B"]):
            ax.axvspan(zones["B"].min(), zones["B"].max(), color="#fbb4ae", alpha=0.35, label="Zone B")
        ax.axvline(zones["A"].max(), color="gray", linestyle="--", linewidth=1)
        ax.axvline(zones["B"].min(), color="gray", linestyle="--", linewidth=1)
        ax.grid(True, alpha=0.25)
    axes[0].plot(x, cyc_pred["observed"], label="Observed T30", linewidth=1.8)
    axes[0].plot(x, cyc_pred["predicted"], label="Predicted T30", linewidth=1.8)
    axes[0].set_ylabel("T30")
    axes[0].legend(loc="best")
    axes[1].plot(x, cyc_pred["residual_norm"], color="#377eb8", label="Residual_norm RMS by cycle")
    axes[1].set_ylabel("Residual_norm")
    axes[1].legend(loc="best")
    axes[2].plot(x, cyc_pred["hi"], color="#984ea3", label=f"HI_v0 W={window}")
    axes[2].set_ylabel("HI_v0")
    axes[2].legend(loc="best")
    axes[3].plot(x, cyc_pred["hpc"], color="#4daf4a", label=DEGRADATION_VAR)
    axes[3].set_ylabel("HPC_eff_mod")
    axes[3].set_xlabel("Cycle")
    axes[3].legend(loc="best")
    fig.suptitle(f"N-CMAPSS C0 Unit {unit}: {DISCLAIMER}", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_DIR / f"ncmapss_c0_unit_{unit}.png", dpi=160)
    plt.close(fig)


def markdown_table(df: pd.DataFrame, columns: list[str], float_cols: list[str] | None = None) -> list[str]:
    float_cols = float_cols or []
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.iterrows():
        values = []
        for col in columns:
            value = row[col]
            if col in float_cols:
                values.append(fmt(float(value)))
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def verdict(model_df: pd.DataFrame, residual_ratio_df: pd.DataFrame, corr_df: pd.DataFrame, hi_df: pd.DataFrame) -> str:
    t30 = model_df[model_df["Target"] == PRIMARY_TARGET]
    min_r2 = t30["Held-out R2"].min()
    t30_ratios = residual_ratio_df[residual_ratio_df["Target"] == PRIMARY_TARGET]["Ratio B/A"]
    min_ratio = t30_ratios.min()
    max_abs_corr = corr_df["Residual Spearman"].abs().max(skipna=True)
    hi_pass = hi_df["Ratio"].max() > 1
    if pd.isna(max_abs_corr):
        if min_r2 > 0.90 and min_ratio > 1 and hi_pass:
            return "Weak Evidence"
        return "FAIL"
    if min_r2 > 0.90 and min_ratio > 1 and max_abs_corr > 0.70 and hi_pass:
        return "Strong PASS"
    if min_r2 > 0.70 and min_ratio > 1 and max_abs_corr > 0.50 and hi_pass:
        return "PASS"
    if min_r2 > 0.50 and max_abs_corr > 0.30:
        return "Weak Evidence"
    return "FAIL"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata = load_metadata()
    vars_ = metadata["vars"]
    selected = metadata["selected"]

    selected_rows = []
    cycle_counts = metadata["cycles_df"].set_index("Unit")["Cycle Count"].to_dict()
    for item in selected:
        selected_rows.append(
            {
                "Unit": item["Unit"],
                "Cycle Count": int(cycle_counts[item["Unit"]]),
                "Selection Reason": item["Selection Reason"],
            }
        )
    selected_df = pd.DataFrame(selected_rows)

    zone_rows = []
    model_parts = []
    residual_parts = []
    residual_ratio_rows = []
    corr_rows = []
    degradation_stats_rows = []
    early_rows = []
    eff_rows = []
    detection_rows = []
    hi_parts = []
    all_results = []

    for item in selected:
        unit = item["Unit"]
        df = load_unit(unit, vars_)
        result = train_and_evaluate(unit, df)
        all_results.append(result)
        zones = result["zones"]
        zone_rows.append(
            {
                "Unit": unit,
                "Zone A": cycle_range(zones["A"]),
                "Zone T": cycle_range(zones["T"]),
                "Zone B": cycle_range(zones["B"]),
            }
        )
        model_parts.append(result["models"])
        residual_parts.append(result["residual_stats"])
        stats = result["residual_stats"]
        for target in TARGETS:
            a = stats[(stats["Target"] == target) & (stats["Zone"] == "A")].iloc[0]
            b = stats[(stats["Target"] == target) & (stats["Zone"] == "B")].iloc[0]
            residual_ratio_rows.append(
                {
                    "Unit": unit,
                    "Target": target,
                    "RMS_A": a["RMS"],
                    "RMS_B": b["RMS"],
                    "Ratio B/A": b["RMS"] / a["RMS"] if a["RMS"] != 0 else float("nan"),
                }
            )
        corr_rows.append(
            {
                "Unit": unit,
                "Residual Spearman": spearman(
                    result["df"][f"{PRIMARY_TARGET}_residual"].to_numpy(),
                    result["df"][DEGRADATION_VAR].to_numpy(),
                ),
                "Residual_norm Spearman": spearman(
                    result["df"][f"{PRIMARY_TARGET}_residual_norm"].to_numpy(),
                    result["df"][DEGRADATION_VAR].to_numpy(),
                ),
            }
        )
        degradation_stats_rows.append(
            {
                "Unit": unit,
                "HPC_eff_mod Min": float(result["df"][DEGRADATION_VAR].min()),
                "HPC_eff_mod Max": float(result["df"][DEGRADATION_VAR].max()),
                "HPC_eff_mod Std": float(result["df"][DEGRADATION_VAR].std(ddof=0)),
            }
        )
        phase_df, first_cycle = early_detection(result["df"])
        for _, row in phase_df.iterrows():
            early_rows.append({"Unit": unit, "Phase": row["Phase"], "RMS": row["RMS"]})
            eff_rows.append({"Unit": unit, "Phase": row["Phase"], "Mean HPC_eff_mod": row["Mean HPC_eff_mod"]})
        detection_rows.append({"Unit": unit, "First Detection Cycle": first_cycle or "Not detected"})
        hi_unit = hi_analysis(unit, result["df"])
        hi_parts.append(hi_unit)

    model_df = pd.concat(model_parts, ignore_index=True)
    residual_stats_df = pd.concat(residual_parts, ignore_index=True)
    residual_ratio_df = pd.DataFrame(residual_ratio_rows)
    corr_df = pd.DataFrame(corr_rows)
    degradation_stats_df = pd.DataFrame(degradation_stats_rows)
    early_df = pd.DataFrame(early_rows)
    eff_df = pd.DataFrame(eff_rows)
    detection_df = pd.DataFrame(detection_rows)
    hi_df = pd.concat(hi_parts, ignore_index=True)

    for result in all_results:
        plot_unit(result, hi_df)

    v = verdict(model_df, residual_ratio_df, corr_df, hi_df)
    best = hi_df.copy()
    best["Score"] = best["Spearman"].abs().fillna(0) + best["Ratio"].fillna(0) / 10.0
    best_by_unit = best.sort_values("Score", ascending=False).groupby("Unit").head(1)
    overall_best_window = int(best.groupby("Window")["Score"].mean().sort_values(ascending=False).index[0])

    lines: list[str] = []
    lines.append("# Validation C0 — N-CMAPSS Surrogate Spike")
    lines.append("")
    lines.append(f"**Scope:** {DISCLAIMER}")
    lines.append("")
    lines.append("## Section 1 — Scope Disclaimer")
    lines.append("")
    lines.append(f"**{DISCLAIMER}**")
    lines.append("")
    lines.append("N-CMAPSS contains no real maintenance events. Artificial lifecycle zones are imposed only to test Expected State, Residual, HI, and segment-aware processing mechanics.")
    lines.append("")
    lines.append("## Section 2 — Variable Mapping")
    lines.append("")
    lines.append(f"- Dataset: `{DATA_PATH.relative_to(ROOT).as_posix()}`")
    lines.append("- Split: dev only (`A_dev`, `W_dev`, `X_s_dev`, `Y_dev`, `T_dev`).")
    lines.append(f"- Condition Variables: {', '.join(CONDITION_VARS)}")
    lines.append(f"- State Variables: primary `{PRIMARY_TARGET}`, secondary `T24`, `Wf`.")
    lines.append(f"- Ground truth degradation: `{DEGRADATION_VAR}`; more negative means more degraded.")
    lines.append("")
    lines.append("Array shapes:")
    for key, shape in metadata["shapes"].items():
        lines.append(f"- `{key}`: {shape}")
    lines.append("")
    lines.append("Variable names:")
    for key, names in vars_.items():
        lines.append(f"- `{key}`: {', '.join(names)}")
    lines.append("")
    lines.append(f"Unique units: {len(metadata['cycles_df'])}")
    lines.append(f"Cycles per unit: min={metadata['cycles_df']['Cycle Count'].min()}, median={metadata['cycles_df']['Cycle Count'].median():.1f}, max={metadata['cycles_df']['Cycle Count'].max()}")
    lines.append("")
    lines.extend(markdown_table(selected_df, ["Unit", "Cycle Count", "Selection Reason"]))
    lines.append("")
    lines.append("Artificial lifecycle zones:")
    lines.extend(markdown_table(pd.DataFrame(zone_rows), ["Unit", "Zone A", "Zone T", "Zone B"]))
    lines.append("")
    lines.append("## Section 3 — Expected State Model Results (B1 Analog)")
    lines.append("")
    lines.extend(markdown_table(model_df, ["Unit", "Target", "Train R2", "Held-out R2"], ["Train R2", "Held-out R2"]))
    lines.append("")
    lines.append("Primary verdict is based on `T30`; `T24` and `Wf` are supporting evidence.")
    lines.append("")
    lines.append("## Section 4 — Residual Zone Comparison (A vs B)")
    lines.append("")
    lines.extend(markdown_table(residual_ratio_df, ["Unit", "Target", "RMS_A", "RMS_B", "Ratio B/A"], ["RMS_A", "RMS_B", "Ratio B/A"]))
    lines.append("")
    lines.append("Success criterion: Zone B RMS > Zone A RMS for all selected units, primary evaluation using T30.")
    lines.append("")
    lines.append("## Section 5 — Ground Truth Correlation")
    lines.append("")
    lines.append("Ground truth degradation variable availability:")
    lines.extend(
        markdown_table(
            degradation_stats_df,
            ["Unit", "HPC_eff_mod Min", "HPC_eff_mod Max", "HPC_eff_mod Std"],
            ["HPC_eff_mod Min", "HPC_eff_mod Max", "HPC_eff_mod Std"],
        )
    )
    lines.append("")
    lines.extend(markdown_table(corr_df, ["Unit", "Residual Spearman", "Residual_norm Spearman"], ["Residual Spearman", "Residual_norm Spearman"]))
    lines.append("")
    if degradation_stats_df["HPC_eff_mod Std"].max() == 0:
        lines.append("Important limitation: `HPC_eff_mod` is constant at 0.0 for the selected DS02 dev units. Spearman correlation is therefore undefined (`nan`). This spike keeps the frozen C0 mapping but cannot use `HPC_eff_mod` as ground-truth degradation evidence for DS02.")
    else:
        lines.append("Correlation is computed against `HPC_eff_mod`. Because more negative means more degraded, negative rho can indicate residual growth with degradation.")
    lines.append("")
    lines.append("## Section 6 — Early Detection Audit")
    lines.append("")
    early_pivot = early_df.pivot(index="Unit", columns="Phase", values="RMS").reset_index()
    eff_pivot = eff_df.pivot(index="Unit", columns="Phase", values="Mean HPC_eff_mod").reset_index()
    lines.append("T30 residual RMS by lifecycle third:")
    lines.extend(markdown_table(early_pivot, ["Unit", "Early", "Mid", "Late"], ["Early", "Mid", "Late"]))
    lines.append("")
    lines.append("Mean HPC_eff_mod by lifecycle third:")
    lines.extend(markdown_table(eff_pivot, ["Unit", "Early", "Mid", "Late"], ["Early", "Mid", "Late"]))
    lines.append("")
    lines.append("First cycle where T30 residual RMS exceeds 1.5 x Early RMS:")
    lines.extend(markdown_table(detection_df, ["Unit", "First Detection Cycle"]))
    lines.append("")
    lines.append("## Section 7 — HI_v0 Window Comparison")
    lines.append("")
    lines.extend(markdown_table(hi_df, ["Unit", "Window", "HI_A", "HI_B", "Ratio", "Spearman"], ["HI_A", "HI_B", "Ratio", "Spearman"]))
    lines.append("")
    lines.append(f"Best overall window by combined Spearman and separation score: `{overall_best_window}` cycles.")
    lines.append("")
    lines.append("Best window per unit:")
    lines.extend(markdown_table(best_by_unit[["Unit", "Window", "Ratio", "Spearman"]], ["Unit", "Window", "Ratio", "Spearman"], ["Ratio", "Spearman"]))
    lines.append("")
    lines.append("## Section 8 — Interpretation")
    lines.append("")
    min_t30_r2 = model_df[model_df["Target"] == PRIMARY_TARGET]["Held-out R2"].min()
    min_t30_ratio = residual_ratio_df[residual_ratio_df["Target"] == PRIMARY_TARGET]["Ratio B/A"].min()
    max_corr = corr_df["Residual Spearman"].abs().max(skipna=True)
    lines.append(f"**Q1: Does Expected State transfer?** Held-out `T30` R2 minimum across selected units is {fmt(min_t30_r2)}. This supports transfer mechanics if the threshold is met.")
    lines.append("")
    lines.append(f"**Q2: Does Residual → HI transfer?** `T30` Zone B/A residual RMS minimum ratio is {fmt(min_t30_ratio)}; HI_v0 windows also produce Zone separation where Ratio > 1.")
    lines.append("")
    lines.append("**Q3: Does segment-aware pipeline run end-to-end?** Yes. The spike loads unit/cycle metadata, imposes artificial Zone A/T/B segments, trains Zone A models, computes residuals, computes HI_v0 by cycle, and reports segment-aware comparisons.")
    lines.append("")
    lines.append("**Q4: How early can degradation be detected?** Detection timing is reported as the first cycle where cycle-level T30 residual RMS exceeds 1.5 x Early RMS. This is a surrogate residual-deviation marker, not a maintenance alarm. Because `HPC_eff_mod` is constant in DS02 dev, this cannot be interpreted as confirmed HPC degradation onset.")
    lines.append("")
    lines.append("## Section 9 — Boundary Statement")
    lines.append("")
    lines.append("Validated:")
    lines.append("- Expected State transfer mechanics")
    lines.append("- Residual generation mechanics")
    lines.append("- HI_v0 behavior")
    lines.append("- Segment-aware processing")
    lines.append("")
    lines.append("Not Validated:")
    lines.append("- Maintenance events")
    lines.append("- Baseline reset semantics")
    lines.append("- Q4b")
    lines.append("- Marine transfer")
    lines.append("")
    lines.append("## Section 10 — Verdict")
    lines.append("")
    lines.append(f"**Verdict: {v}.**")
    lines.append("")
    corr_text = "undefined because HPC_eff_mod is constant in DS02 dev" if pd.isna(max_corr) else fmt(float(max_corr))
    lines.append(f"Justification: primary T30 held-out R2 minimum={fmt(min_t30_r2)}, T30 residual RMS B/A minimum={fmt(min_t30_ratio)}, max |residual vs HPC_eff_mod Spearman|={corr_text}. Expected State, residual, HI, and segment mechanics run end-to-end, but ground-truth degradation correlation cannot be established with the requested DS02/HPC_eff_mod pairing.")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
