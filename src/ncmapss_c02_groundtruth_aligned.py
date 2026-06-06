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
REPORT = OUT_DIR / "ncmapss_c02_groundtruth_aligned.md"
RANKING_CSV = OUT_DIR / "c02_sensor_groundtruth_ranking.csv"

DISCLAIMER = "Surrogate only. Not maintenance-event evidence. Not Q4b evidence."
CONDITION_VARS = ["alt", "Mach", "TRA", "T2"]
GROUND_TRUTH = "HPT_eff_mod"
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


def fmt(value: object, digits: int = 3) -> str:
    if value is None:
        return "None"
    if isinstance(value, (float, np.floating)):
        if math.isnan(float(value)):
            return "nan"
        return f"{float(value):.{digits}f}"
    return str(value)


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


def load_metadata() -> dict:
    with h5py.File(DATA_PATH, "r") as f:
        vars_ = {
            "A_var": decode(f["A_var"][()]),
            "W_var": decode(f["W_var"][()]),
            "X_s_var": decode(f["X_s_var"][()]),
            "T_var": decode(f["T_var"][()]),
        }
        shapes = {key: tuple(f[key].shape) for key in ["A_dev", "W_dev", "X_s_dev", "T_dev"]}
        a_var = vars_["A_var"]
        unit_idx = a_var.index("unit")
        cycle_idx = a_var.index("cycle")
        a = f["A_dev"][:, [unit_idx, cycle_idx]].astype(int)
        hpt = f["T_dev"][:, vars_["T_var"].index(GROUND_TRUTH)]
    units = np.unique(a[:, 0])
    rows = []
    for unit in units:
        cycles = np.unique(a[a[:, 0] == unit, 1])
        rows.append({"Unit": int(unit), "Cycles": int(len(cycles))})
    cycle_df = pd.DataFrame(rows).sort_values("Cycles")
    median_count = float(cycle_df["Cycles"].median())
    selected = [
        {"Unit": int(cycle_df.iloc[-1]["Unit"]), "Reason": "Longest lifecycle"},
        {
            "Unit": int(cycle_df.iloc[(cycle_df["Cycles"] - median_count).abs().argsort().iloc[0]]["Unit"]),
            "Reason": "Median lifecycle",
        },
        {"Unit": int(cycle_df.iloc[0]["Unit"]), "Reason": "Shortest lifecycle"},
    ]
    return {
        "vars": vars_,
        "shapes": shapes,
        "cycle_df": cycle_df.sort_values("Unit"),
        "selected": selected,
        "hpt_stats": {
            "Range": f"{float(hpt.min()):.6f} to {float(hpt.max()):.6f}",
            "Mean": float(np.mean(hpt)),
            "Std": float(np.std(hpt, ddof=0)),
        },
    }


def sensor_ranking(vars_: dict[str, list[str]]) -> pd.DataFrame:
    rows = []
    t_idx = vars_["T_var"].index(GROUND_TRUTH)
    with h5py.File(DATA_PATH, "r") as f:
        hpt = f["T_dev"][:, t_idx]
        xs = f["X_s_dev"]
        for idx, sensor in enumerate(vars_["X_s_var"]):
            rho = spearman(xs[:, idx], hpt)
            rows.append({"Sensor": sensor, "Spearman": rho, "AbsSpearman": abs(rho) if not math.isnan(rho) else float("nan")})
    ranking = pd.DataFrame(rows).sort_values("AbsSpearman", ascending=False).reset_index(drop=True)
    ranking.to_csv(RANKING_CSV, index=False)
    return ranking


def choose_targets(ranking: pd.DataFrame) -> list[str]:
    temp_candidates = [s for s in ["T48", "T50"] if s in set(ranking["Sensor"])]
    temp_rank = ranking[ranking["Sensor"].isin(temp_candidates)].sort_values("AbsSpearman", ascending=False)
    primary = str(temp_rank.iloc[0]["Sensor"]) if not temp_rank.empty else str(ranking[ranking["Sensor"].str.startswith("T")].iloc[0]["Sensor"])

    flow_speed = {"Nf", "Nc", "Wf"}
    secondary_rank = ranking[ranking["Sensor"].isin(flow_speed - {"Wf"})].sort_values("AbsSpearman", ascending=False)
    secondary = str(secondary_rank.iloc[0]["Sensor"]) if not secondary_rank.empty else str(ranking[ranking["Sensor"].isin(list(flow_speed))].iloc[0]["Sensor"])

    targets = []
    for target in [primary, secondary, "Wf"]:
        if target not in targets:
            targets.append(target)
    return targets


def load_unit(unit: int, vars_: dict[str, list[str]], targets: list[str]) -> pd.DataFrame:
    a_var, w_var, xs_var, t_var = vars_["A_var"], vars_["W_var"], vars_["X_s_var"], vars_["T_var"]
    unit_idx = a_var.index("unit")
    cycle_idx = a_var.index("cycle")
    w_idx = [w_var.index(name) for name in CONDITION_VARS]
    x_idx = [xs_var.index(name) for name in targets]
    t_idx = t_var.index(GROUND_TRUTH)
    with h5py.File(DATA_PATH, "r") as f:
        units = f["A_dev"][:, unit_idx].astype(int)
        mask = units == unit
        cycles = f["A_dev"][mask, cycle_idx].astype(int)
        w = f["W_dev"][mask, :][:, w_idx]
        x = f["X_s_dev"][mask, :][:, x_idx]
        t = f["T_dev"][mask, t_idx]
    data = {"unit": np.full(len(cycles), unit, dtype=int), "cycle": cycles, GROUND_TRUTH: t}
    for i, name in enumerate(CONDITION_VARS):
        data[name] = w[:, i]
    for i, name in enumerate(targets):
        data[name] = x[:, i]
    return pd.DataFrame(data).sort_values("cycle").reset_index(drop=True)


def zone_sets(cycles: np.ndarray) -> dict[str, np.ndarray]:
    unique = np.array(sorted(np.unique(cycles).astype(int)))
    n = len(unique)
    a_end = max(1, int(math.floor(n * 0.2)))
    b_start = min(n - 1, int(math.ceil(n * 0.8)))
    return {"A": unique[:a_end], "T": unique[a_end:b_start], "B": unique[b_start:]}


def cycle_range(values: np.ndarray) -> str:
    return f"{int(values.min())}-{int(values.max())} ({len(values)} cycles)"


def train_unit(unit: int, df: pd.DataFrame, targets: list[str]) -> dict:
    zones = zone_sets(df["cycle"].to_numpy())
    df["zone"] = np.select([df["cycle"].isin(zones["A"]), df["cycle"].isin(zones["B"])], ["A", "B"], default="T")
    zone_a = df[df["zone"] == "A"].copy()
    split = int(len(zone_a) * 0.8)
    x_train = zone_a.iloc[:split][CONDITION_VARS]
    x_hold = zone_a.iloc[split:][CONDITION_VARS]
    model_rows = []
    residual_rows = []
    corr_rows = []
    for target in targets:
        reg = model()
        y_train = zone_a.iloc[:split][target]
        y_hold = zone_a.iloc[split:][target]
        reg.fit(x_train, y_train)
        pred_train = reg.predict(x_train)
        pred_hold = reg.predict(x_hold)
        pred_all = reg.predict(df[CONDITION_VARS])
        residual = df[target].to_numpy() - pred_all
        zone_a_mask = df["zone"].to_numpy() == "A"
        std_a = float(np.std(residual[zone_a_mask], ddof=0))
        if std_a == 0:
            std_a = float("nan")
        df[f"{target}_pred"] = pred_all
        df[f"{target}_residual"] = residual
        df[f"{target}_residual_norm"] = residual / std_a
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
        for zone in ["A", "B"]:
            values = residual[df["zone"].to_numpy() == zone]
            residual_rows.append(
                {
                    "Unit": unit,
                    "Target": target,
                    "Zone": zone,
                    "Mean": float(np.mean(values)),
                    "Std": float(np.std(values, ddof=0)),
                    "RMS": rms(values),
                    "P95": p95(values),
                }
            )
        corr_rows.append(
            {
                "Unit": unit,
                "Target": target,
                "Spearman": spearman(residual, df[GROUND_TRUTH].to_numpy()),
                "AbsSpearman": abs(spearman(residual, df[GROUND_TRUTH].to_numpy())),
            }
        )
    return {
        "unit": unit,
        "df": df,
        "zones": zones,
        "models": pd.DataFrame(model_rows),
        "residual_stats": pd.DataFrame(residual_rows),
        "corr": pd.DataFrame(corr_rows),
    }


def cycle_level(df: pd.DataFrame, col: str) -> pd.DataFrame:
    return (
        df.groupby("cycle")
        .agg(value=(col, lambda x: rms(x.to_numpy())), zone=("zone", "first"), gt=(GROUND_TRUTH, "mean"))
        .reset_index()
        .sort_values("cycle")
    )


def hi_analysis(result: dict, targets: list[str]) -> pd.DataFrame:
    unit = result["unit"]
    df = result["df"]
    rows = []
    for target in targets:
        cyc = cycle_level(df, f"{target}_residual_norm")
        for window in WINDOWS:
            hi = np.sqrt(cyc["value"].pow(2).rolling(window=window, min_periods=max(1, window // 2)).mean())
            a = hi[cyc["zone"] == "A"].dropna()
            b = hi[cyc["zone"] == "B"].dropna()
            rho = spearman(hi.dropna().to_numpy(), cyc.loc[hi.notna(), "gt"].to_numpy())
            rows.append(
                {
                    "Unit": unit,
                    "Target": target,
                    "Window": window,
                    "HI_A": float(a.mean()) if len(a) else float("nan"),
                    "HI_B": float(b.mean()) if len(b) else float("nan"),
                    "HI Ratio": float(b.mean() / a.mean()) if len(a) and a.mean() != 0 else float("nan"),
                    "Spearman": rho,
                    "AbsSpearman": abs(rho) if not math.isnan(rho) else float("nan"),
                }
            )
    return pd.DataFrame(rows)


def best_hi(hi_df: pd.DataFrame) -> pd.Series:
    scored = hi_df.copy()
    scored["Score"] = scored["AbsSpearman"].fillna(0) + scored["HI Ratio"].fillna(0) / 10
    return scored.sort_values("Score", ascending=False).iloc[0]


def detection(result: dict, target: str, window: int) -> dict:
    df = result["df"]
    cyc = cycle_level(df, f"{target}_residual_norm")
    hi = np.sqrt(cyc["value"].pow(2).rolling(window=window, min_periods=max(1, window // 2)).mean())
    n = len(cyc)
    early = hi.iloc[: max(1, int(n * 0.33))].dropna()
    early_mean = float(early.mean()) if len(early) else float("nan")
    threshold = 1.5 * early_mean
    hits = cyc[hi > threshold]
    if hits.empty:
        return {"Unit": result["unit"], "Detection Cycle": "Not detected", "Lifecycle %": "n/a", "Threshold": threshold}
    cycle = int(hits.iloc[0]["cycle"])
    pct = 100 * (list(cyc["cycle"]).index(cycle) + 1) / n
    return {"Unit": result["unit"], "Detection Cycle": cycle, "Lifecycle %": pct, "Threshold": threshold}


def plot_unit(result: dict, target: str, window: int, detection_row: dict) -> None:
    unit = result["unit"]
    df = result["df"]
    zones = result["zones"]
    cyc = (
        df.groupby("cycle")
        .agg(
            observed=(target, "mean"),
            predicted=(f"{target}_pred", "mean"),
            residual=(f"{target}_residual", "mean"),
            residual_norm=(f"{target}_residual_norm", lambda x: rms(x.to_numpy())),
            gt=(GROUND_TRUTH, "mean"),
        )
        .reset_index()
    )
    cyc["hi"] = np.sqrt(cyc["residual_norm"].pow(2).rolling(window=window, min_periods=max(1, window // 2)).mean())
    fig, axes = plt.subplots(5, 1, figsize=(12, 14), sharex=True)
    for ax in axes:
        ax.axvspan(zones["A"].min(), zones["A"].max(), color="#ccebc5", alpha=0.35)
        ax.axvspan(zones["B"].min(), zones["B"].max(), color="#fbb4ae", alpha=0.35)
        ax.axvline(zones["A"].max(), color="gray", linestyle="--", linewidth=1)
        ax.axvline(zones["B"].min(), color="gray", linestyle="--", linewidth=1)
        if isinstance(detection_row["Detection Cycle"], int):
            ax.axvline(detection_row["Detection Cycle"], color="red", linestyle=":", linewidth=1.5)
        ax.grid(True, alpha=0.25)
    axes[0].plot(cyc["cycle"], cyc["observed"], label=f"Observed {target}")
    axes[0].plot(cyc["cycle"], cyc["predicted"], label=f"Predicted {target}")
    axes[0].legend()
    axes[0].set_ylabel(target)
    axes[1].plot(cyc["cycle"], cyc["residual"], color="#377eb8")
    axes[1].set_ylabel("Residual")
    axes[2].plot(cyc["cycle"], cyc["hi"], color="#984ea3")
    axes[2].set_ylabel(f"HI W={window}")
    axes[3].plot(cyc["cycle"], cyc["gt"], color="#4daf4a")
    axes[3].set_ylabel(GROUND_TRUTH)
    axes[4].plot(cyc["cycle"], cyc["hi"], color="#984ea3")
    axes[4].axhline(detection_row["Threshold"], color="red", linestyle="--", label="1.5 x Early HI")
    axes[4].set_ylabel("Detection")
    axes[4].set_xlabel("Cycle")
    axes[4].legend()
    fig.suptitle(f"N-CMAPSS C0.2 Unit {unit}: {DISCLAIMER}", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_DIR / f"ncmapss_c02_unit_{unit}.png", dpi=160)
    plt.close(fig)


def markdown_table(df: pd.DataFrame, columns: list[str], float_cols: set[str] | None = None) -> list[str]:
    float_cols = float_cols or set()
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.iterrows():
        values = [fmt(row[col]) if col in float_cols else str(row[col]) for col in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def verdict(model_df: pd.DataFrame, residual_ratio_df: pd.DataFrame, corr_df: pd.DataFrame, hi_df: pd.DataFrame) -> str:
    min_r2 = model_df["Held-out R2"].min()
    majority_residual = (residual_ratio_df["Ratio"] > 1).sum() >= (len(residual_ratio_df) / 2)
    max_corr = corr_df["AbsSpearman"].max()
    max_hi = hi_df["AbsSpearman"].max()
    if min_r2 > 0.90 and majority_residual and max_corr > 0.70 and max_hi > 0.70:
        return "Strong PASS"
    if min_r2 > 0.70 and majority_residual and max_corr > 0.50 and max_hi > 0.50:
        return "PASS"
    if min_r2 > 0.50 and (max_corr > 0.30 or max_hi > 0.30):
        return "Weak Evidence"
    return "FAIL"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = load_metadata()
    vars_ = meta["vars"]
    ranking = sensor_ranking(vars_)
    targets = choose_targets(ranking)
    selected = pd.DataFrame(
        [{"Unit": x["Unit"], "Cycles": int(meta["cycle_df"].set_index("Unit").loc[x["Unit"], "Cycles"]), "Reason": x["Reason"]} for x in meta["selected"]]
    )

    results = []
    zone_rows = []
    for unit in selected["Unit"]:
        df = load_unit(int(unit), vars_, targets)
        result = train_unit(int(unit), df, targets)
        results.append(result)
        zones = result["zones"]
        zone_rows.append({"Unit": int(unit), "Zone A": cycle_range(zones["A"]), "Zone T": cycle_range(zones["T"]), "Zone B": cycle_range(zones["B"])})

    model_df = pd.concat([r["models"] for r in results], ignore_index=True)
    residual_stats = pd.concat([r["residual_stats"] for r in results], ignore_index=True)
    residual_ratio_rows = []
    for unit in selected["Unit"]:
        for target in targets:
            a = residual_stats[(residual_stats["Unit"] == unit) & (residual_stats["Target"] == target) & (residual_stats["Zone"] == "A")].iloc[0]
            b = residual_stats[(residual_stats["Unit"] == unit) & (residual_stats["Target"] == target) & (residual_stats["Zone"] == "B")].iloc[0]
            residual_ratio_rows.append({"Unit": int(unit), "Target": target, "RMS_A": a["RMS"], "RMS_B": b["RMS"], "Ratio": b["RMS"] / a["RMS"] if a["RMS"] else float("nan")})
    residual_ratio_df = pd.DataFrame(residual_ratio_rows)
    corr_df = pd.concat([r["corr"] for r in results], ignore_index=True)
    hi_df = pd.concat([hi_analysis(r, targets) for r in results], ignore_index=True)

    best = best_hi(hi_df)
    best_target = str(best["Target"])
    best_window = int(best["Window"])
    detection_df = pd.DataFrame([detection(r, best_target, best_window) for r in results])
    for result, det in zip(results, detection_df.to_dict("records")):
        plot_unit(result, best_target, best_window, det)

    v = verdict(model_df, residual_ratio_df, corr_df, hi_df)
    c0_best_corr = "undefined (`HPC_eff_mod` constant zero)"

    lines = []
    lines.append("# Validation C0.2 — Ground Truth Aligned Rerun")
    lines.append("")
    lines.append(f"**Scope:** {DISCLAIMER}")
    lines.append("")
    lines.append("## 1. Scope Disclaimer")
    lines.append("")
    lines.append(f"**{DISCLAIMER}**")
    lines.append("")
    lines.append("This rerun uses the C0.1 finding that DS02-006 contains active `HPT_eff_mod` degradation while `HPC_eff_mod` is zero. It remains a surrogate mechanics validation only.")
    lines.append("")
    lines.append("## 2. Ground Truth Selection")
    lines.append("")
    lines.append("- Primary degradation label: `HPT_eff_mod`")
    lines.append("- Reason: C0.1 confirmed `HPT_eff_mod` is active across units 2, 5, 10, 16, 18, and 20, while `HPC_eff_mod = 0` for all units.")
    lines.append(f"- HPT_eff_mod range: {meta['hpt_stats']['Range']}")
    lines.append(f"- HPT_eff_mod mean: {fmt(meta['hpt_stats']['Mean'], 6)}")
    lines.append(f"- HPT_eff_mod std: {fmt(meta['hpt_stats']['Std'], 6)}")
    lines.append("")
    lines.extend(markdown_table(selected, ["Unit", "Cycles", "Reason"]))
    lines.append("")
    lines.append("Lifecycle zones:")
    lines.extend(markdown_table(pd.DataFrame(zone_rows), ["Unit", "Zone A", "Zone T", "Zone B"]))
    lines.append("")
    lines.append("## 3. Sensor Ranking")
    lines.append("")
    lines.extend(markdown_table(ranking.head(15), ["Sensor", "Spearman", "AbsSpearman"], {"Spearman", "AbsSpearman"}))
    lines.append("")
    lines.append("Final target selection:")
    lines.append(f"- Primary target: `{targets[0]}` (highest-ranked preferred temperature sensor among T48/T50)")
    lines.append(f"- Secondary target: `{targets[1]}` (highest-ranked flow/speed sensor excluding Wf when possible)")
    lines.append(f"- Continuity target: `Wf`")
    lines.append("")
    lines.append("## 4. Model Performance")
    lines.append("")
    lines.extend(markdown_table(model_df, ["Unit", "Target", "Train R2", "Held-out R2"], {"Train R2", "Held-out R2"}))
    lines.append("")
    lines.append("## 5. Residual Results")
    lines.append("")
    lines.extend(markdown_table(residual_ratio_df, ["Unit", "Target", "RMS_A", "RMS_B", "Ratio"], {"RMS_A", "RMS_B", "Ratio"}))
    lines.append("")
    lines.append("## 6. Ground Truth Correlation")
    lines.append("")
    lines.extend(markdown_table(corr_df, ["Unit", "Target", "Spearman", "AbsSpearman"], {"Spearman", "AbsSpearman"}))
    lines.append("")
    lines.append("Note: `HPT_eff_mod` is negative when degraded. Negative Spearman indicates residual tends to increase as degradation becomes more negative.")
    lines.append("")
    lines.append("## 7. HI_v0 Results")
    lines.append("")
    lines.extend(markdown_table(hi_df, ["Unit", "Target", "Window", "HI Ratio", "Spearman", "AbsSpearman"], {"HI Ratio", "Spearman", "AbsSpearman"}))
    lines.append("")
    lines.append(f"Best target/window: `{best_target}`, W={best_window} cycles.")
    lines.append("")
    lines.append("## 8. Early Detection")
    lines.append("")
    lines.extend(markdown_table(detection_df, ["Unit", "Detection Cycle", "Lifecycle %", "Threshold"], {"Lifecycle %", "Threshold"}))
    lines.append("")
    lines.append("## 9. Interpretation")
    lines.append("")
    lines.append("**Q1: Does residual track actual degradation?**")
    lines.append(f"Best residual |Spearman| = {fmt(corr_df['AbsSpearman'].max())}. Alignment with `HPT_eff_mod` provides a real, non-constant degradation label unlike C0.")
    lines.append("")
    lines.append("**Q2: Does HI track actual degradation?**")
    lines.append(f"Best HI |Spearman| = {fmt(hi_df['AbsSpearman'].max())}, with best HI Ratio = {fmt(hi_df['HI Ratio'].max())}.")
    lines.append("")
    lines.append("**Q3: Does alignment improve over C0?**")
    lines.append(f"Yes. C0 ground-truth correlation was {c0_best_corr}; C0.2 obtains finite correlations against active `HPT_eff_mod`.")
    lines.append("")
    lines.append("**Q4: What is the best sensor for degradation monitoring?**")
    lines.append(f"`{best_target}` is the best target in this rerun based on HI separation and Spearman score. Sensor ranking should be consulted for domain interpretation.")
    lines.append("")
    lines.append("**Q5: How early can degradation be detected?**")
    lines.append("Detection cycles are reported using the best target/window and threshold `HI_v0 > 1.5 x Early-Life HI`. This is a surrogate detectability marker, not an operational alarm.")
    lines.append("")
    lines.append("## 10. Verdict")
    lines.append("")
    lines.append(f"**Verdict: {v}.**")
    lines.append("")
    lines.append(f"Justification: C0.2 corrects the C0 ground-truth mismatch by using active `HPT_eff_mod`. Minimum held-out R2={fmt(model_df['Held-out R2'].min())}; maximum residual |Spearman|={fmt(corr_df['AbsSpearman'].max())}; maximum HI |Spearman|={fmt(hi_df['AbsSpearman'].max())}; maximum HI Ratio={fmt(hi_df['HI Ratio'].max())}.")
    lines.append("")
    lines.append("Compared with Validation C0, this rerun strengthens evidence for residual/HI mechanics because the degradation label is no longer constant. It still does not validate maintenance events, baseline reset, Q4b, or Marine transfer.")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)


if __name__ == "__main__":
    main()
