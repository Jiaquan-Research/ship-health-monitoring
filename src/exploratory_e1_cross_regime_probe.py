from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "ncmapss" / "data_set" / "N-CMAPSS_DS02-006.h5"
REPORT_PATH = ROOT / "outputs" / "exploratory_e1_cross_regime_probe.md"

UNITS = [5, 2, 16]
CONDITION_VARS = ["alt", "Mach", "TRA", "T2"]
TARGET = "T50"
GROUND_TRUTH = "HPT_eff_mod"
REGIME_ORDER = ["Early", "Middle", "Late"]


def decode(values: np.ndarray) -> list[str]:
    return [v.decode("utf-8", errors="replace") if isinstance(v, bytes) else str(v) for v in values]


def fmt(value: object, digits: int = 4) -> str:
    if pd.isna(value):
        return "N/A"
    return f"{float(value):.{digits}g}"


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


def load_unit(unit: int) -> pd.DataFrame:
    with h5py.File(DATA_PATH, "r") as f:
        a_var = decode(f["A_var"][()])
        w_var = decode(f["W_var"][()])
        xs_var = decode(f["X_s_var"][()])
        t_var = decode(f["T_var"][()])

        unit_idx = a_var.index("unit")
        cycle_idx = a_var.index("cycle")
        condition_idx = [w_var.index(name) for name in CONDITION_VARS]
        target_idx = xs_var.index(TARGET)
        gt_idx = t_var.index(GROUND_TRUTH)

        units = f["A_dev"][:, unit_idx].astype(int)
        mask = units == unit
        cycles = f["A_dev"][mask, cycle_idx].astype(int)
        w = f["W_dev"][mask, :][:, condition_idx]
        y = f["X_s_dev"][mask, target_idx]
        gt = f["T_dev"][mask, gt_idx]

    data = {
        "unit": np.full(len(cycles), unit, dtype=int),
        "cycle": cycles,
        TARGET: y,
        GROUND_TRUTH: gt,
    }
    for idx, name in enumerate(CONDITION_VARS):
        data[name] = w[:, idx]
    return pd.DataFrame(data).sort_values("cycle").reset_index(drop=True)


def regime_cycles(cycles: pd.Series) -> dict[str, np.ndarray]:
    unique = np.array(sorted(cycles.unique().astype(int)))
    n = len(unique)
    early_end = max(1, int(np.floor(n * 0.2)))
    middle_start = int(np.floor(n * 0.4))
    middle_end = max(middle_start + 1, int(np.floor(n * 0.6)))
    late_start = min(n - 1, int(np.floor(n * 0.8)))
    return {
        "Early": unique[:early_end],
        "Middle": unique[middle_start:middle_end],
        "Late": unique[late_start:],
    }


def assign_regimes(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
    cycles = regime_cycles(df["cycle"])
    out = df.copy()
    out["regime"] = "Other"
    for regime, values in cycles.items():
        out.loc[out["cycle"].isin(values), "regime"] = regime
    return out, cycles


def cycle_span(values: np.ndarray) -> str:
    return f"{int(values.min())}-{int(values.max())} ({len(values)} cycles)"


def run_probe() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rows = []
    regime_rows = []
    matrix_rows = []
    for unit in UNITS:
        df, cycles = assign_regimes(load_unit(unit))
        for regime in REGIME_ORDER:
            subset = df[df["regime"].eq(regime)]
            regime_rows.append(
                {
                    "Unit": unit,
                    "Regime": regime,
                    "CycleSpan": cycle_span(cycles[regime]),
                    "Rows": len(subset),
                    "MeanHPT_eff_mod": subset[GROUND_TRUTH].mean(),
                }
            )

        for train_regime in REGIME_ORDER:
            train = df[df["regime"].eq(train_regime)]
            reg = model()
            reg.fit(train[CONDITION_VARS], train[TARGET])
            for test_regime in REGIME_ORDER:
                test = df[df["regime"].eq(test_regime)]
                pred = reg.predict(test[CONDITION_VARS])
                residual = test[TARGET].to_numpy() - pred
                r2 = r2_score(test[TARGET], pred)
                mae = mean_absolute_error(test[TARGET], pred)
                rms = float(np.sqrt(np.mean(np.square(residual))))
                row = {
                    "Unit": unit,
                    "Train": train_regime,
                    "Test": test_regime,
                    "RowsTrain": len(train),
                    "RowsTest": len(test),
                    "R2": r2,
                    "MAE": mae,
                    "ResidualMean": float(np.mean(residual)),
                    "ResidualStd": float(np.std(residual, ddof=0)),
                    "ResidualRMS": rms,
                    "AbsResidualMean": float(np.mean(np.abs(residual))),
                }
                rows.append(row)
                matrix_rows.append(row)
    return pd.DataFrame(rows), pd.DataFrame(regime_rows), pd.DataFrame(matrix_rows)


def verdict(results: pd.DataFrame) -> str:
    same = results[results["Train"].eq(results["Test"])]["R2"].mean()
    cross = results[~results["Train"].eq(results["Test"])]["R2"].mean()
    if same - cross > 0.5:
        return "Cross-regime instability observed."
    return "No obvious instability observed."


def write_report(results: pd.DataFrame, regimes: pd.DataFrame) -> None:
    avg_matrix = results.groupby(["Train", "Test"], as_index=False)["R2"].mean()
    matrix = avg_matrix.pivot(index="Train", columns="Test", values="R2").loc[REGIME_ORDER, REGIME_ORDER]
    same = results[results["Train"].eq(results["Test"])]["R2"].mean()
    cross = results[~results["Train"].eq(results["Test"])]["R2"].mean()
    verdict_text = verdict(results)

    lines = []
    lines.append("# Exploratory E-1 Cross-Regime Probe")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("This is NOT a validation.")
    lines.append("")
    lines.append("This is NOT M-1A.")
    lines.append("")
    lines.append("No claims are upgraded.")
    lines.append("")
    lines.append("No conclusions about universality are made.")
    lines.append("")
    lines.append("Observation only.")
    lines.append("")
    lines.append("## Frozen C0.2 Selections")
    lines.append("")
    lines.append(f"* Dataset: `{DATA_PATH.relative_to(ROOT)}`")
    lines.append(f"* Units: `{', '.join(str(u) for u in UNITS)}`")
    lines.append(f"* Condition variables: `{', '.join(CONDITION_VARS)}`")
    lines.append(f"* Target: `{TARGET}`")
    lines.append(f"* Ground-truth label retained from C0.2: `{GROUND_TRUTH}`")
    lines.append("")
    lines.append("No C0.2 models were retrained or modified.")
    lines.append("")
    lines.append("## Regime Windows")
    lines.append("")
    lines.append("Regime windows are lifecycle partitions only.")
    lines.append("")
    lines.append("They are not interpreted as health states.")
    lines.append("")
    lines.append("| Unit | Regime | Cycle Span | Rows | Mean HPT_eff_mod |")
    lines.append("|---:|---|---|---:|---:|")
    for _, row in regimes.iterrows():
        lines.append(
            f"| {int(row['Unit'])} | {row['Regime']} | {row['CycleSpan']} | "
            f"{int(row['Rows']):,} | {fmt(row['MeanHPT_eff_mod'])} |"
        )
    lines.append("")
    lines.append("## Transfer Matrix")
    lines.append("")
    lines.append("Mean R2 across units.")
    lines.append("")
    lines.append("| Train \\\\ Test | Early | Middle | Late |")
    lines.append("|---|---:|---:|---:|")
    for train in REGIME_ORDER:
        lines.append(
            f"| {train} | {fmt(matrix.loc[train, 'Early'])} | "
            f"{fmt(matrix.loc[train, 'Middle'])} | {fmt(matrix.loc[train, 'Late'])} |"
        )
    lines.append("")
    lines.append("## Detailed Results")
    lines.append("")
    lines.append(
        "| Unit | Train | Test | R2 | MAE | Residual Mean | Residual Std | Residual RMS | Abs Residual Mean |"
    )
    lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|")
    for _, row in results.iterrows():
        lines.append(
            f"| {int(row['Unit'])} | {row['Train']} | {row['Test']} | "
            f"{fmt(row['R2'])} | {fmt(row['MAE'])} | {fmt(row['ResidualMean'])} | "
            f"{fmt(row['ResidualStd'])} | {fmt(row['ResidualRMS'])} | {fmt(row['AbsResidualMean'])} |"
        )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"* Mean same-window R2: `{fmt(same)}`")
    lines.append(f"* Mean cross-window R2: `{fmt(cross)}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("If same-window performance is approximately cross-window performance, cross-regime instability is weak.")
    lines.append("")
    lines.append("If cross-window performance collapses while same-window remains good, cross-regime instability exists.")
    lines.append("")
    lines.append("No speculation is provided.")
    lines.append("")
    lines.append("No comparison with HVAC is made.")
    lines.append("")
    lines.append("No universality claim is made.")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(verdict_text)
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    results, regimes, _ = run_probe()
    write_report(results, regimes)
    print(REPORT_PATH)
    print(verdict(results))


if __name__ == "__main__":
    main()
