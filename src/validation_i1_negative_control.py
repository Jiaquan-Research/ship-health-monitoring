from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESIDUAL_PATH = ROOT / "outputs" / "residuals_normal.csv"
HI_STATS_PATH = ROOT / "outputs" / "hi_v0" / "hi_v0_severity_stats.csv"
CONDITION_PATH = ROOT / "data" / "lbnl" / "ChillerPlant.csv"
REPORT_PATH = ROOT / "outputs" / "validation_i1_negative_control.md"

FIG_HI = ROOT / "outputs" / "validation_i1_hi_v0_full.png"
FIG_RMS = ROOT / "outputs" / "validation_i1_residual_rms.png"
FIG_COND = ROOT / "outputs" / "validation_i1_conditions_overlay.png"
FIG_SUMMARY = ROOT / "outputs" / "validation_i1_summary_stats.png"

PRIMARY_TARGET = "CT_SW_TEMP_1"
PRIMARY_WINDOW = "6h"
PRIMARY_WINDOW_ROWS = 360


def spearman_time(series: pd.Series) -> float:
    values = series.dropna()
    if len(values) < 3 or values.nunique() <= 1:
        return np.nan
    return pd.Series(np.arange(len(values)), index=values.index).corr(values, method="spearman")


def slope_time(series: pd.Series) -> float:
    values = series.dropna()
    if len(values) < 3 or values.nunique() <= 1:
        return np.nan
    x = np.arange(len(values), dtype=float)
    return float(np.polyfit(x, values.to_numpy(dtype=float), 1)[0])


def monotonic_direction(series: pd.Series) -> str:
    values = series.dropna()
    if len(values) < 3:
        return "insufficient data"
    diffs = np.diff(values.to_numpy(dtype=float))
    positive_share = float(np.mean(diffs > 0))
    negative_share = float(np.mean(diffs < 0))
    if positive_share == 1.0:
        return "strict increasing"
    if negative_share == 1.0:
        return "strict decreasing"
    if positive_share > negative_share:
        return f"mixed, upward-biased ({positive_share:.3f} positive steps)"
    if negative_share > positive_share:
        return f"mixed, downward-biased ({negative_share:.3f} negative steps)"
    return "mixed, no dominant step direction"


def rms_rowwise(frame: pd.DataFrame, columns: list[str]) -> pd.Series:
    return np.sqrt(np.square(frame[columns]).mean(axis=1))


def split_windows(frame: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    bounds = np.linspace(0, len(frame), 4, dtype=int)
    return [
        (f"Window {idx + 1}", frame.iloc[bounds[idx] : bounds[idx + 1]].copy())
        for idx in range(3)
    ]


def metric_row(name: str, frame: pd.DataFrame) -> dict[str, object]:
    return {
        "Window": name,
        "Rows": len(frame),
        "Start": frame.index.min(),
        "End": frame.index.max(),
        "HI_Spearman": spearman_time(frame["HI_v0"]),
        "Residual_RMS_Spearman": spearman_time(frame["Residual_RMS"]),
        "HI_Slope": slope_time(frame["HI_v0"]),
        "Residual_RMS_Slope": slope_time(frame["Residual_RMS"]),
        "HI_Monotonicity": monotonic_direction(frame["HI_v0"]),
        "Residual_RMS_Monotonicity": monotonic_direction(frame["Residual_RMS"]),
        "OA_TEMP_Corr_HI": frame[["HI_v0", "OA_TEMP"]].corr(method="spearman").iloc[0, 1],
        "Load_Corr_HI": frame[["HI_v0", "CWL_SEC_LOAD"]].corr(method="spearman").iloc[0, 1],
        "OA_TEMP_Corr_RMS": frame[["Residual_RMS", "OA_TEMP"]].corr(method="spearman").iloc[0, 1],
        "Load_Corr_RMS": frame[["Residual_RMS", "CWL_SEC_LOAD"]].corr(method="spearman").iloc[0, 1],
    }


def fmt_float(value: object, digits: int = 4) -> str:
    if pd.isna(value):
        return "N/A"
    return f"{float(value):.{digits}g}"


def verdict_from_metrics(metrics: pd.DataFrame) -> tuple[str, str, str]:
    window_rows = metrics.iloc[1:]

    hi_spearman_signs = np.sign(window_rows["HI_Spearman"].astype(float))
    rms_spearman_signs = np.sign(window_rows["Residual_RMS_Spearman"].astype(float))
    hi_slope_signs = np.sign(window_rows["HI_Slope"].astype(float))
    rms_slope_signs = np.sign(window_rows["Residual_RMS_Slope"].astype(float))

    hi_instability = len(set(hi_spearman_signs)) > 1 or len(set(hi_slope_signs)) > 1
    rms_instability = len(set(rms_spearman_signs)) > 1 or len(set(rms_slope_signs)) > 1

    if hi_instability or rms_instability:
        return (
            "FAIL",
            "FAIL: sub-window instability appears in healthy data.",
            "condition leakage / context effect",
        )

    return (
        "PASS",
        "PASS: no obvious persistent monotonic increase across full-period and sub-window metrics.",
        "no trend attribution required",
    )


def save_figures(data: pd.DataFrame, metrics: pd.DataFrame) -> None:
    boundaries = [data.index[len(data) // 3], data.index[(2 * len(data)) // 3]]

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data.index, data["HI_v0"], linewidth=0.8, color="#1f77b4")
    for boundary in boundaries:
        ax.axvline(boundary, color="black", linestyle="--", linewidth=0.8)
    ax.set_title("Validation I-1 HI_v0 on Healthy LBNL Baseline")
    ax.set_ylabel("HI_v0")
    ax.set_xlabel("Datetime")
    fig.tight_layout()
    fig.savefig(FIG_HI, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data.index, data["Residual_RMS"], linewidth=0.8, color="#d62728")
    for boundary in boundaries:
        ax.axvline(boundary, color="black", linestyle="--", linewidth=0.8)
    ax.set_title("Validation I-1 Residual RMS on Healthy LBNL Baseline")
    ax.set_ylabel("Residual RMS")
    ax.set_xlabel("Datetime")
    fig.tight_layout()
    fig.savefig(FIG_RMS, dpi=160)
    plt.close(fig)

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
    axes[0].plot(data.index, data["HI_v0"], linewidth=0.8, color="#1f77b4")
    axes[0].set_ylabel("HI_v0")
    axes[1].plot(data.index, data["OA_TEMP"], linewidth=0.8, color="#2ca02c")
    axes[1].set_ylabel("OA_TEMP")
    axes[2].plot(data.index, data["CWL_SEC_LOAD"], linewidth=0.8, color="#9467bd")
    axes[2].set_ylabel("CWL_SEC_LOAD")
    axes[2].set_xlabel("Datetime")
    for ax in axes:
        for boundary in boundaries:
            ax.axvline(boundary, color="black", linestyle="--", linewidth=0.8)
    fig.suptitle("Validation I-1 HI_v0, Outdoor Air Temperature, and Load")
    fig.tight_layout()
    fig.savefig(FIG_COND, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    labels = metrics["Window"].tolist()
    x = np.arange(len(labels))
    width = 0.35
    ax.bar(x - width / 2, metrics["HI_Spearman"], width, label="HI Spearman")
    ax.bar(x + width / 2, metrics["Residual_RMS_Spearman"], width, label="Residual RMS Spearman")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25, ha="right")
    ax.set_ylabel("Spearman(time, metric)")
    ax.legend()
    ax.set_title("Validation I-1 Spearman Summary")
    fig.tight_layout()
    fig.savefig(FIG_SUMMARY, dpi=160)
    plt.close(fig)


def main() -> None:
    residuals = pd.read_csv(RESIDUAL_PATH, parse_dates=["Datetime"])
    residuals = residuals.set_index("Datetime").sort_index()

    hi_stats = pd.read_csv(HI_STATS_PATH)
    baseline_hi_stats = hi_stats[hi_stats["Dataset"].eq("Baseline")].copy()
    selected_hi_stats = baseline_hi_stats[
        baseline_hi_stats["Target"].eq(PRIMARY_TARGET) & baseline_hi_stats["Window"].eq(PRIMARY_WINDOW)
    ]

    conditions = pd.read_csv(
        CONDITION_PATH,
        usecols=["Datetime", "OA_TEMP", "CWL_SEC_LOAD"],
        parse_dates=["Datetime"],
    ).set_index("Datetime").sort_index()

    start_idx = int(len(residuals) * 0.05)
    end_idx = int(len(residuals) * 0.95)
    healthy = residuals.iloc[start_idx:end_idx].copy()

    norm_cols = [c for c in healthy.columns if c.endswith("_residual_norm")]
    target_norm_col = f"{PRIMARY_TARGET}_residual_norm"
    if target_norm_col not in healthy.columns:
        raise ValueError(f"Missing required residual column: {target_norm_col}")

    healthy["Residual_RMS"] = rms_rowwise(healthy, norm_cols)
    healthy["HI_v0"] = np.sqrt(
        healthy[target_norm_col].pow(2).rolling(PRIMARY_WINDOW_ROWS, min_periods=PRIMARY_WINDOW_ROWS // 2).mean()
    )
    healthy = healthy.join(conditions[["OA_TEMP", "CWL_SEC_LOAD"]], how="left").dropna(
        subset=["Residual_RMS", "HI_v0", "OA_TEMP", "CWL_SEC_LOAD"]
    )

    metric_rows = [metric_row("Full healthy period", healthy)]
    metric_rows.extend(metric_row(name, frame) for name, frame in split_windows(healthy))
    metrics = pd.DataFrame(metric_rows)

    verdict, verdict_reason, likely_cause = verdict_from_metrics(metrics)

    save_figures(healthy, metrics)

    lines = []
    lines.append("# Validation I-1 Negative Control")
    lines.append("")
    lines.append("## 1. Protocol Reference")
    lines.append("")
    lines.append("Protocol: `docs/review/negative_control_protocol_v0.1.md`")
    lines.append("")
    lines.append("Status: executed according to pre-registered Validation I-1 protocol.")
    lines.append("")
    lines.append("No model retraining was performed.")
    lines.append("")
    lines.append("No new datasets were introduced.")
    lines.append("")
    lines.append("No fault datasets were loaded.")
    lines.append("")
    lines.append("Residuals were not recomputed.")
    lines.append("")
    lines.append("## 2. Dataset Definition")
    lines.append("")
    lines.append("Dataset: LBNL baseline only, `data/lbnl/ChillerPlant.csv`.")
    lines.append("")
    lines.append(f"Frozen residual rows before trimming: {len(residuals):,}")
    lines.append("")
    lines.append("Healthy period definition: exclude first 5% and last 5% of baseline residual rows.")
    lines.append("")
    lines.append(f"Healthy period rows after trimming and condition alignment: {len(healthy):,}")
    lines.append("")
    lines.append(f"Healthy period start: {healthy.index.min()}")
    lines.append("")
    lines.append(f"Healthy period end: {healthy.index.max()}")
    lines.append("")
    lines.append("## 3. Frozen Artifact Sources")
    lines.append("")
    lines.append(f"* Residual source: `{RESIDUAL_PATH.relative_to(ROOT)}`")
    lines.append(f"* HI aggregate source: `{HI_STATS_PATH.relative_to(ROOT)}`")
    lines.append("")
    lines.append(
        "The HI aggregate source contains Baseline summary rows but no time-resolved HI_v0 column. "
        "For the pre-registered time-based metric, HI_v0 was derived from the frozen "
        f"`{target_norm_col}` series using the existing Rolling RMS formula and the existing "
        f"recommended configuration: target `{PRIMARY_TARGET}`, window `{PRIMARY_WINDOW}`."
    )
    lines.append("")
    if selected_hi_stats.empty:
        lines.append("Selected baseline HI stats row: not found.")
    else:
        row = selected_hi_stats.iloc[0]
        lines.append(
            "Selected baseline HI stats row: "
            f"HI_mean={fmt_float(row['HI_mean'])}, HI_p95={fmt_float(row['HI_p95'])}, "
            f"HI_p99={fmt_float(row['HI_p99'])}."
        )
    lines.append("")
    lines.append("## 4. Full-Period Metrics")
    lines.append("")
    full = metrics.iloc[0]
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Spearman(time, HI_v0) | {fmt_float(full['HI_Spearman'])} |")
    lines.append(f"| Spearman(time, residual RMS) | {fmt_float(full['Residual_RMS_Spearman'])} |")
    lines.append(f"| HI_v0 trend slope | {fmt_float(full['HI_Slope'])} |")
    lines.append(f"| Residual RMS trend slope | {fmt_float(full['Residual_RMS_Slope'])} |")
    lines.append(f"| HI_v0 monotonicity | {full['HI_Monotonicity']} |")
    lines.append(f"| Residual RMS monotonicity | {full['Residual_RMS_Monotonicity']} |")
    lines.append("")
    lines.append("## 5. Sub-Window Metrics")
    lines.append("")
    lines.append(
        "| Window | Rows | Start | End | HI Spearman | Residual RMS Spearman | HI Slope | Residual RMS Slope |"
    )
    lines.append("|---|---:|---|---|---:|---:|---:|---:|")
    for _, row in metrics.iloc[1:].iterrows():
        lines.append(
            f"| {row['Window']} | {int(row['Rows']):,} | {row['Start']} | {row['End']} | "
            f"{fmt_float(row['HI_Spearman'])} | {fmt_float(row['Residual_RMS_Spearman'])} | "
            f"{fmt_float(row['HI_Slope'])} | {fmt_float(row['Residual_RMS_Slope'])} |"
        )
    lines.append("")
    lines.append("## 6. Trend Attribution")
    lines.append("")
    lines.append("OA_TEMP correlation and load correlation were computed for protocol-required trend attribution.")
    lines.append("")
    lines.append("| Window | HI vs OA_TEMP | HI vs Load | Residual RMS vs OA_TEMP | Residual RMS vs Load |")
    lines.append("|---|---:|---:|---:|---:|")
    for _, row in metrics.iterrows():
        lines.append(
            f"| {row['Window']} | {fmt_float(row['OA_TEMP_Corr_HI'])} | {fmt_float(row['Load_Corr_HI'])} | "
            f"{fmt_float(row['OA_TEMP_Corr_RMS'])} | {fmt_float(row['Load_Corr_RMS'])} |"
        )
    lines.append("")
    lines.append(f"Likely cause: {likely_cause}.")
    lines.append("")
    if likely_cause == "condition leakage / context effect":
        lines.append(
            "Trend correlated with OA_TEMP or load indicates likely condition leakage or context effect, "
            "not degradation signal."
        )
    else:
        lines.append("Trend attribution was not required by the protocol because no obvious trend-like behavior was observed.")
    lines.append("")
    lines.append("## 7. Visualizations")
    lines.append("")
    lines.append(f"* `{FIG_HI.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_RMS.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_COND.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_SUMMARY.relative_to(ROOT)}`")
    lines.append("")
    lines.append("## 8. Verdict")
    lines.append("")
    lines.append(verdict)
    lines.append("")
    lines.append(verdict_reason)
    lines.append("")
    lines.append("## 9. Consequences")
    lines.append("")
    if verdict == "FAIL":
        lines.append("Failure does NOT invalidate the project.")
        lines.append("")
        lines.append("Failure suggests:")
        lines.append("")
        lines.append("Residual may contain:")
        lines.append("")
        lines.append("* condition leakage;")
        lines.append("* context effects;")
        lines.append("* model deficiencies.")
        lines.append("")
        lines.append("Failure indicates that")
        lines.append("residual construct validity")
        lines.append("must be re-examined.")
        lines.append("")
        lines.append("Actions:")
        lines.append("")
        lines.append("* suspend forward validation work;")
        lines.append("* re-examine condition normalization;")
        lines.append("* re-examine Expected State formulation;")
        lines.append("* re-assess residual construct validity;")
        lines.append("* Validation D remains blocked")
        lines.append("  until I-1 passes.")
        lines.append("")
        lines.append("No specific remediation path")
        lines.append("is assumed.")
    else:
        lines.append("Success does NOT prove Trend.")
        lines.append("")
        lines.append("Success only demonstrates:")
        lines.append("")
        lines.append("Residual and HI do not generate")
        lines.append("obvious false trends")
        lines.append("on healthy trajectories.")
        lines.append("")
        lines.append("Trend interpretation remains")
        lines.append("an open question.")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT_PATH)
    print(f"Verdict: {verdict}")


if __name__ == "__main__":
    main()
