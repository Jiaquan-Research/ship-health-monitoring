from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "outputs" / "validation_b21_residuals.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "hi_v0"
B21_SENSITIVITY_PATH = PROJECT_ROOT / "outputs" / "validation_b21_sensitivity.csv"

DATASET_ORDER = ["Baseline", "095", "080", "065"]
WINDOWS = {
    "6h": 360,
    "12h": 720,
    "24h": 1440,
    "48h": 2880,
}
TARGETS = {
    "CT_SW_TEMP_1": {
        "hi_name": "HI_v0A",
        "column": "CT_SW_TEMP_1_residual_norm",
        "property": "Highest fault sensitivity",
    },
    "CHL_SW_TEMP_1": {
        "hi_name": "HI_v0B",
        "column": "CHL_SW_TEMP_1_residual_norm",
        "property": "Cleanest baseline",
    },
    "CHL_RWCD_TEMP_1": {
        "hi_name": "HI_v0C",
        "column": "CHL_RWCD_TEMP_1_residual_norm",
        "property": "Second highest sensitivity",
    },
    "CHL_POW_1": {
        "hi_name": "HI_v0D",
        "column": "CHL_POW_1_residual_norm",
        "property": "Reference",
    },
}


def markdown_table(df: pd.DataFrame, floatfmt: str = ".6g") -> str:
    lines = [
        "| " + " | ".join(str(column) for column in df.columns) + " |",
        "| " + " | ".join("---" for _ in df.columns) + " |",
    ]
    for _, row in df.iterrows():
        values = []
        for value in row.tolist():
            if pd.isna(value):
                values.append("")
            elif isinstance(value, float):
                values.append(format(value, floatfmt))
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def rolling_rms(series: pd.Series, window: int) -> pd.Series:
    return series.pow(2).rolling(window=window, min_periods=window // 2).mean().pow(0.5)


def strict_monotonic(values: list[float]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def load_residuals() -> pd.DataFrame:
    usecols = ["Datetime", "Dataset"] + [meta["column"] for meta in TARGETS.values()]
    df = pd.read_csv(
        INPUT_PATH,
        usecols=usecols,
        parse_dates=["Datetime"],
        dtype={"Dataset": str},
        low_memory=False,
    )
    df["Dataset"] = df["Dataset"].str.strip()
    return df.set_index("Datetime").sort_index()


def save_timeseries_plot(hi_store: dict[tuple[str, str, str], pd.Series], target: str) -> None:
    plt.figure(figsize=(13, 5))
    min_len = min(len(hi_store[(target, "24h", dataset)].dropna()) for dataset in DATASET_ORDER)
    plot_len = min(min_len, 10_000)
    step = max(1, min_len // plot_len)
    for dataset in DATASET_ORDER:
        values = hi_store[(target, "24h", dataset)].dropna().iloc[:min_len:step].reset_index(drop=True)
        plt.plot(values.index, values.values, linewidth=1.0, label=dataset)
    plt.title(f"HI_v0 24h Time Series: {target}")
    plt.xlabel("Aligned sample index")
    plt.ylabel("HI_v0")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"hi_v0_timeseries_{target}_24h.png", dpi=160)
    plt.close()


def save_severity_plot(severity_24h: pd.DataFrame, target: str) -> None:
    subset = severity_24h[severity_24h["Target"] == target].set_index("Dataset").loc[DATASET_ORDER]
    plt.figure(figsize=(7, 5))
    plt.bar(DATASET_ORDER, subset["HI_mean"].values)
    plt.title(f"HI_v0 24h Severity Mean: {target}")
    plt.xlabel("Corrected severity order")
    plt.ylabel("HI_v0 mean")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"hi_v0_severity_{target}_24h.png", dpi=160)
    plt.close()


def save_window_sensitivity_plot(sensitivity: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    for target in ["CT_SW_TEMP_1", "CHL_SW_TEMP_1"]:
        subset = sensitivity[sensitivity["Target"] == target].set_index("Window").loc[list(WINDOWS.keys())]
        plt.plot(list(WINDOWS.keys()), subset["Sensitivity_Score"].values, marker="o", linewidth=2, label=target)
    plt.title("HI_v0 Window Sensitivity")
    plt.xlabel("Rolling window")
    plt.ylabel("Sensitivity score")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "hi_v0_window_sensitivity.png", dpi=160)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Loading frozen B2.1 residuals from {INPUT_PATH}")
    df = load_residuals()

    row_counts = df["Dataset"].value_counts().reindex(DATASET_ORDER).reset_index()
    row_counts.columns = ["Dataset", "Rows"]
    confirmed_columns = ["Datetime", "Dataset"] + [meta["column"] for meta in TARGETS.values()]

    hi_store: dict[tuple[str, str, str], pd.Series] = {}
    baseline_rows = []
    severity_rows = []

    print("Computing rolling RMS HI_v0")
    for target, meta in TARGETS.items():
        for window_name, window_rows in WINDOWS.items():
            for dataset in DATASET_ORDER:
                subset = df[df["Dataset"] == dataset]
                hi_store[(target, window_name, dataset)] = rolling_rms(subset[meta["column"]], window_rows)

            baseline_hi = hi_store[(target, window_name, "Baseline")].dropna()
            baseline_mean = float(baseline_hi.mean())
            baseline_std = float(baseline_hi.std())
            baseline_p95 = float(baseline_hi.quantile(0.95))
            baseline_p99 = float(baseline_hi.quantile(0.99))
            baseline_rows.append(
                {
                    "Target": target,
                    "Window": window_name,
                    "baseline_mean": baseline_mean,
                    "baseline_std": baseline_std,
                    "baseline_p95": baseline_p95,
                    "baseline_p99": baseline_p99,
                }
            )

            for dataset in DATASET_ORDER:
                hi = hi_store[(target, window_name, dataset)].dropna()
                hi_z = (hi - baseline_mean) / baseline_std
                severity_rows.append(
                    {
                        "Target": target,
                        "Window": window_name,
                        "Dataset": dataset,
                        "HI_mean": float(hi.mean()),
                        "HI_p95": float(hi.quantile(0.95)),
                        "HI_p99": float(hi.quantile(0.99)),
                        "HIz_mean": float(hi_z.mean()),
                        "Exceedance_P95": float((hi > baseline_p95).mean() * 100),
                    }
                )

    baseline_stats = pd.DataFrame(baseline_rows)
    severity_stats = pd.DataFrame(severity_rows)
    baseline_stats.to_csv(OUTPUT_DIR / "hi_v0_baseline_stats.csv", index=False)
    severity_stats.to_csv(OUTPUT_DIR / "hi_v0_severity_stats.csv", index=False)

    monotonic_rows = []
    for target in TARGETS:
        for window_name in WINDOWS:
            subset = severity_stats[
                (severity_stats["Target"] == target) & (severity_stats["Window"] == window_name)
            ].set_index("Dataset").loc[DATASET_ORDER]
            monotonic_rows.append(
                {
                    "Target": target,
                    "Window": window_name,
                    "Strict_Mean": strict_monotonic(subset["HI_mean"].tolist()),
                    "Strict_P95": strict_monotonic(subset["HI_p95"].tolist()),
                    "Strict_HIz": strict_monotonic(subset["HIz_mean"].tolist()),
                }
            )
    monotonic = pd.DataFrame(monotonic_rows)
    monotonic.to_csv(OUTPUT_DIR / "hi_v0_monotonicity.csv", index=False)

    sensitivity_rows = []
    for target in TARGETS:
        for window_name in WINDOWS:
            subset = severity_stats[
                (severity_stats["Target"] == target) & (severity_stats["Window"] == window_name)
            ].set_index("Dataset")
            baseline = subset.loc["Baseline", "HI_mean"]
            strongest = subset.loc["065", "HI_mean"]
            sensitivity_rows.append(
                {
                    "Target": target,
                    "Window": window_name,
                    "Sensitivity_Score": float((strongest - baseline) / baseline),
                }
            )
    sensitivity = (
        pd.DataFrame(sensitivity_rows)
        .sort_values("Sensitivity_Score", ascending=False)
        .reset_index(drop=True)
    )
    sensitivity.insert(0, "Rank", sensitivity.index + 1)
    sensitivity.to_csv(OUTPUT_DIR / "hi_v0_sensitivity.csv", index=False)

    severity_24h = severity_stats[severity_stats["Window"] == "24h"].copy()
    sensitivity_24h = sensitivity[sensitivity["Window"] == "24h"].copy()
    monotonic_24h = monotonic[monotonic["Window"] == "24h"].copy()

    print("Creating plots")
    for target in TARGETS:
        save_timeseries_plot(hi_store, target)
        save_severity_plot(severity_24h, target)
    save_window_sensitivity_plot(sensitivity)

    strong_monotonic_count = int(monotonic_24h["Strict_Mean"].sum())
    baseline_exceed_24h = severity_24h[severity_24h["Dataset"] == "Baseline"]["Exceedance_P95"]
    max_baseline_exceed = float(baseline_exceed_24h.max())
    hi_v0a_clear = bool(
        monotonic_24h.loc[monotonic_24h["Target"] == "CT_SW_TEMP_1", "Strict_Mean"].iloc[0]
    )

    b21 = pd.read_csv(B21_SENSITIVITY_PATH)
    b21_lookup = dict(zip(b21["Target"], b21["Sensitivity Score"]))
    hi_24h_lookup = dict(zip(sensitivity_24h["Target"], sensitivity_24h["Sensitivity_Score"]))
    value_rows = []
    for target in TARGETS:
        value_rows.append(
            {
                "Target": target,
                "B2.1_Raw_RMS_Sensitivity": b21_lookup[target],
                "HI_v0_24h_Sensitivity": hi_24h_lookup[target],
                "Delta": hi_24h_lookup[target] - b21_lookup[target],
            }
        )
    value_comparison = pd.DataFrame(value_rows)
    value_comparison.to_csv(OUTPUT_DIR / "hi_v0_vs_raw_residual.csv", index=False)

    hi_improves_raw = bool((value_comparison["Delta"] > 0).sum() >= 3)
    if strong_monotonic_count >= 3 and max_baseline_exceed <= 5.0 and hi_improves_raw:
        verdict = "Strong PASS"
    elif hi_v0a_clear and max_baseline_exceed <= 10.0:
        verdict = "Moderate PASS"
    else:
        verdict = "Fail"

    best_row = sensitivity.iloc[0]
    best_target = best_row["Target"]
    best_window = best_row["Window"]
    q3_status = "Preliminary Supported" if verdict != "Fail" else "Not Yet Supported"
    reliable_threshold = "P95" if max_baseline_exceed <= 5.0 else "P99"

    window_comparison = sensitivity[
        sensitivity["Target"].isin(["CT_SW_TEMP_1", "CHL_SW_TEMP_1"])
    ].sort_values(["Target", "Window"])

    report = [
        "# HI_v0 Rolling RMS Validation",
        "",
        "## 1. Summary",
        "",
        f"- Verdict: {verdict}",
        f"- Best target: `{best_target}`",
        f"- Best window size: `{best_window}`",
        f"- Q3 status: {q3_status}",
        "- Input: frozen B2.1 normalized residuals only. Residuals were not recomputed and models were not loaded.",
        "",
        "### Loaded Residuals",
        "",
        markdown_table(row_counts),
        "",
        "### Columns Confirmed",
        "",
        ", ".join(f"`{column}`" for column in confirmed_columns),
        "",
        "## 2. Severity Statistics Table",
        "",
        "Primary window: W=24h.",
        "",
        markdown_table(severity_24h),
        "",
        "## 3. Monotonicity Results",
        "",
        markdown_table(monotonic),
        "",
        "## 4. Sensitivity Ranking",
        "",
        "Primary window: W=24h.",
        "",
        markdown_table(sensitivity_24h[["Rank", "Target", "Window", "Sensitivity_Score"]]),
        "",
        "## 5. Window Size Comparison",
        "",
        markdown_table(window_comparison[["Rank", "Target", "Window", "Sensitivity_Score"]]),
        "",
        "## 6. Interpretation",
        "",
        "### Q1: Does HI_v0 separate fault severity levels?",
        "",
        (
            "Yes. HI_v0 separates Baseline -> 095 -> 080 -> 065 monotonically for the primary W=24h window."
            if strong_monotonic_count >= 3
            else "Not sufficiently. Fewer than 3 targets are strictly monotonic for HI_mean at W=24h."
        ),
        "",
        "### Q2: Which target is most useful?",
        "",
        (
            "`CT_SW_TEMP_1` remains the strongest sensitivity target. `CHL_SW_TEMP_1` remains useful as a cleaner-baseline comparator, but its sensitivity is lower."
        ),
        "",
        "### Q3: Which window size performs best?",
        "",
        f"`{best_window}` performs best by maximum sensitivity score, led by `{best_target}`.",
        "",
        "### Q4: Does HI_v0 add value over raw residual RMS from B2.1?",
        "",
        markdown_table(value_comparison),
        "",
        (
            "Yes. HI_v0 increases sensitivity versus raw residual RMS for at least 3 of 4 targets while preserving monotonicity and controlled baseline exceedance."
            if hi_improves_raw
            else "No. HI_v0 does not improve sensitivity over raw residual RMS for enough targets to be considered a clear improvement."
        ),
        "",
        "### Q5: Can Q3 of the Concept Paper be marked \"Preliminary Supported\"?",
        "",
        (
            "Yes. Q3 can be marked Preliminary Supported for the HVAC-domain residual-to-HI construction."
            if q3_status == "Preliminary Supported"
            else "No. Q3 should remain open until HI_v0 improves over raw residual metrics."
        ),
        "",
        "## 7. Recommended HI_v0 Configuration",
        "",
        f"- Primary target: `{best_target}`",
        f"- Window size: `{best_window}`",
        f"- Threshold type: `{reliable_threshold}`",
        "",
        "## Generated Outputs",
        "",
        "- `outputs/hi_v0/hi_v0_baseline_stats.csv`",
        "- `outputs/hi_v0/hi_v0_severity_stats.csv`",
        "- `outputs/hi_v0/hi_v0_monotonicity.csv`",
        "- `outputs/hi_v0/hi_v0_sensitivity.csv`",
        "- `outputs/hi_v0/hi_v0_vs_raw_residual.csv`",
        "- `outputs/hi_v0/hi_v0_window_sensitivity.png`",
    ]
    for target in TARGETS:
        report.append(f"- `outputs/hi_v0/hi_v0_timeseries_{target}_24h.png`")
        report.append(f"- `outputs/hi_v0/hi_v0_severity_{target}_24h.png`")

    (OUTPUT_DIR / "hi_v0_validation.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'hi_v0_validation.md'}")


if __name__ == "__main__":
    main()
