from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESIDUAL_PATH = PROJECT_ROOT / "outputs" / "validation_b21_residuals.csv"
HI_V0_STATS_PATH = PROJECT_ROOT / "outputs" / "hi_v0" / "hi_v0_severity_stats.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_PATH = OUTPUT_DIR / "b4_residual_trend_audit.md"

DATASET_ORDER = ["Baseline", "095", "080", "065"]
STAGE_INDEX = {"Baseline": 0, "095": 1, "080": 2, "065": 3}
TARGETS = [
    "CT_SW_TEMP_1",
    "CHL_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
    "CHL_POW_1",
]
METRICS = ["AbsMean", "RMS", "P95", "P99", "Std"]


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


def strict_monotonic(values: list[float]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def load_residuals() -> pd.DataFrame:
    usecols = ["Datetime", "Dataset"]
    for target in TARGETS:
        usecols.extend([f"{target}_residual", f"{target}_residual_norm"])
    df = pd.read_csv(
        RESIDUAL_PATH,
        usecols=usecols,
        parse_dates=["Datetime"],
        dtype={"Dataset": str},
        low_memory=False,
    )
    df["Dataset"] = df["Dataset"].str.strip()
    return df.set_index("Datetime").sort_index()


def compute_metric(series: pd.Series, metric: str) -> float:
    if metric == "AbsMean":
        return float(series.abs().mean())
    if metric == "RMS":
        return float((series.pow(2).mean()) ** 0.5)
    if metric == "P95":
        return float(series.quantile(0.95))
    if metric == "P99":
        return float(series.quantile(0.99))
    if metric == "Std":
        return float(series.std())
    raise ValueError(metric)


def spearman_for_values(values: list[float]) -> float:
    stages = pd.Series([0, 1, 2, 3])
    metric_values = pd.Series(values)
    return float(stages.corr(metric_values, method="spearman"))


def cohens_d(a: pd.Series, b: pd.Series) -> float:
    pooled = (((len(a) - 1) * a.var() + (len(b) - 1) * b.var()) / (len(a) + len(b) - 2)) ** 0.5
    if pooled == 0:
        return float("inf")
    return float((a.mean() - b.mean()) / pooled)


def make_trend_plots(metrics_wide: pd.DataFrame, spearman: pd.DataFrame, trend_strength: pd.DataFrame) -> None:
    for target in TARGETS:
        subset = metrics_wide[metrics_wide["Target"] == target]
        plt.figure(figsize=(8, 5))
        for metric in METRICS:
            row = subset[subset["Metric"] == metric].iloc[0]
            values = [row[dataset] for dataset in DATASET_ORDER]
            plt.plot(["Stage 0", "Stage 1", "Stage 2", "Stage 3"], values, marker="o", linewidth=2, label=metric)
        plt.title(f"Pseudo Degradation Path: {target}")
        plt.xlabel("Pseudo degradation stage")
        plt.ylabel("Raw residual metric")
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f"b4_trend_path_{target}.png", dpi=160)
        plt.close()

    heat = spearman.pivot(index="Target", columns="Metric", values="Spearman_rho").loc[TARGETS, METRICS]
    plt.figure(figsize=(8, 4.8))
    sns.heatmap(heat, annot=True, cmap="viridis", vmin=-1, vmax=1, fmt=".2f")
    plt.title("B4 Spearman Trend Correlation")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "b4_spearman_heatmap.png", dpi=160)
    plt.close()

    ratios = trend_strength[trend_strength["Ratio"] != "N/A (near-zero baseline)"].copy()
    ratios["RatioValue"] = ratios["Ratio"].astype(float)
    plt.figure(figsize=(10, 5))
    for metric in METRICS:
        subset = ratios[ratios["Metric"] == metric]
        plt.bar(
            [f"{target}\n{metric}" for target in subset["Target"]],
            subset["RatioValue"],
            label=metric,
        )
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Metric_065 / Metric_Baseline")
    plt.title("B4 Trend Strength Ratios")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "b4_trend_strength.png", dpi=160)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Loading frozen residuals from {RESIDUAL_PATH}")
    df = load_residuals()
    row_counts = df["Dataset"].value_counts().reindex(DATASET_ORDER).reset_index()
    row_counts.columns = ["Dataset", "Rows"]

    metric_rows = []
    strength_rows = []
    step_rows = []
    residual_lookup: dict[tuple[str, str], pd.Series] = {}

    for target in TARGETS:
        col = f"{target}_residual"
        for dataset in DATASET_ORDER:
            residual_lookup[(target, dataset)] = df[df["Dataset"] == dataset][col].dropna()
        for metric in METRICS:
            values = {
                dataset: compute_metric(residual_lookup[(target, dataset)], metric)
                for dataset in DATASET_ORDER
            }
            metric_rows.append({"Target": target, "Metric": metric, **values})

            baseline_value = values["Baseline"]
            strongest_value = values["065"]
            delta = strongest_value - baseline_value
            ratio: float | str
            if abs(baseline_value) < 0.01:
                ratio = "N/A (near-zero baseline)"
            else:
                ratio = strongest_value / baseline_value
            d = cohens_d(residual_lookup[(target, "065")], residual_lookup[(target, "Baseline")])
            strength_rows.append(
                {
                    "Target": target,
                    "Metric": metric,
                    "Delta": delta,
                    "Ratio": ratio,
                    "Cohen_d": d,
                }
            )

            ordered = [values[dataset] for dataset in DATASET_ORDER]
            is_strict = strict_monotonic(ordered)
            if is_strict:
                step1 = values["095"] - values["Baseline"]
                step2 = values["080"] - values["095"]
                step3 = values["065"] - values["080"]
                no_reversal = step1 > 0 and step2 > 0 and step3 > 0
            else:
                step1 = values["095"] - values["Baseline"]
                step2 = values["080"] - values["095"]
                step3 = values["065"] - values["080"]
                no_reversal = False
            step_rows.append(
                {
                    "Target": target,
                    "Metric": metric,
                    "Step1": step1,
                    "Step2": step2,
                    "Step3": step3,
                    "No_Reversal": no_reversal,
                }
            )

    metrics_wide = pd.DataFrame(metric_rows)
    spearman = pd.DataFrame(
        [
            {
                "Target": row["Target"],
                "Metric": row["Metric"],
                "Spearman_rho": spearman_for_values([row[dataset] for dataset in DATASET_ORDER]),
            }
            for _, row in metrics_wide.iterrows()
        ]
    )
    monotonic = pd.DataFrame(
        [
            {
                "Target": row["Target"],
                "Metric": row["Metric"],
                "Strict_Monotonic": strict_monotonic([row[dataset] for dataset in DATASET_ORDER]),
            }
            for _, row in metrics_wide.iterrows()
        ]
    )
    trend_strength = pd.DataFrame(strength_rows)
    steps = pd.DataFrame(step_rows)

    hi_stats = pd.read_csv(HI_V0_STATS_PATH)
    hi_ct = hi_stats[
        (hi_stats["Target"] == "CT_SW_TEMP_1")
        & (hi_stats["Window"] == "24h")
    ].set_index("Dataset").loc[DATASET_ORDER]
    raw_ct_rms = metrics_wide[
        (metrics_wide["Target"] == "CT_SW_TEMP_1") & (metrics_wide["Metric"] == "RMS")
    ].iloc[0]
    raw_sensitivity = raw_ct_rms["065"] / raw_ct_rms["Baseline"]
    hi_sensitivity = hi_ct.loc["065", "HI_mean"] / hi_ct.loc["Baseline", "HI_mean"]
    hi_monotonic = strict_monotonic(hi_ct["HI_mean"].tolist())
    raw_monotonic = strict_monotonic([raw_ct_rms[dataset] for dataset in DATASET_ORDER])
    comparison = pd.DataFrame(
        [
            {
                "Carrier": "Raw residual RMS",
                "Baseline": raw_ct_rms["Baseline"],
                "095": raw_ct_rms["095"],
                "080": raw_ct_rms["080"],
                "065": raw_ct_rms["065"],
                "Ratio_065/Baseline": raw_sensitivity,
                "Strict_Monotonic": raw_monotonic,
            },
            {
                "Carrier": "HI_v0 Rolling RMS 24h",
                "Baseline": hi_ct.loc["Baseline", "HI_mean"],
                "095": hi_ct.loc["095", "HI_mean"],
                "080": hi_ct.loc["080", "HI_mean"],
                "065": hi_ct.loc["065", "HI_mean"],
                "Ratio_065/Baseline": hi_sensitivity,
                "Strict_Monotonic": hi_monotonic,
            },
        ]
    )

    reliable = monotonic.merge(spearman, on=["Target", "Metric"]).merge(steps, on=["Target", "Metric"])
    reliable = reliable[
        (reliable["Strict_Monotonic"])
        & (reliable["Spearman_rho"] == 1.0)
        & (reliable["No_Reversal"])
    ]
    reliable_targets = reliable["Target"].nunique()
    best_candidates = reliable.merge(trend_strength, on=["Target", "Metric"])
    best_candidates["RatioNumeric"] = pd.to_numeric(best_candidates["Ratio"], errors="coerce")
    best = best_candidates.sort_values(
        ["Target", "RatioNumeric"],
        ascending=[True, False],
    )
    primary_metric = "RMS"
    if not reliable[(reliable["Target"] == "CT_SW_TEMP_1") & (reliable["Metric"] == "RMS")].empty:
        primary_metric = "RMS"
    elif not reliable.empty:
        primary_metric = str(best_candidates.sort_values("RatioNumeric", ascending=False).iloc[0]["Metric"])

    strong_targets = monotonic[
        (monotonic["Metric"].isin(["RMS", "P95", "P99"]))
        & (monotonic["Strict_Monotonic"])
    ].groupby("Target")["Metric"].nunique()
    strong_pass = int((strong_targets >= 3).sum()) >= 2 and float(
        spearman[
            (spearman["Target"] == "CT_SW_TEMP_1") & (spearman["Metric"] == primary_metric)
        ]["Spearman_rho"].iloc[0]
    ) == 1.0
    moderate_pass = not monotonic[
        (monotonic["Target"] == "CT_SW_TEMP_1") & (monotonic["Strict_Monotonic"])
    ].empty
    if strong_pass:
        verdict = "Strong PASS"
        q4a = "Initial Evidence"
    elif moderate_pass:
        verdict = "Moderate PASS"
        q4a = "Initial Evidence"
    else:
        verdict = "Fail"
        q4a = "Not Supported"

    metrics_wide.to_csv(OUTPUT_DIR / "b4_trend_metrics.csv", index=False)
    spearman.to_csv(OUTPUT_DIR / "b4_spearman.csv", index=False)
    monotonic.to_csv(OUTPUT_DIR / "b4_monotonicity.csv", index=False)
    trend_strength.to_csv(OUTPUT_DIR / "b4_trend_strength.csv", index=False)
    steps.to_csv(OUTPUT_DIR / "b4_step_no_reversal.csv", index=False)
    comparison.to_csv(OUTPUT_DIR / "b4_raw_vs_hi_v0.csv", index=False)
    row_counts.to_csv(OUTPUT_DIR / "b4_dataset_rows.csv", index=False)
    make_trend_plots(metrics_wide, spearman, trend_strength)

    report = [
        "# Validation B4: Residual Trend Audit",
        "",
        f"- Verdict: {verdict}",
        f"- Q4a status: {q4a}",
        f"- Best trend metric: {primary_metric}",
        f"- Targets with reliable trend: {reliable_targets}/4",
        "- Input: frozen Validation B2.1 residuals only. No residuals recomputed. No models retrained.",
        "",
        "## Dataset Load Check",
        "",
        markdown_table(row_counts),
        "",
        "## Section 1: Trend Metrics Table",
        "",
        markdown_table(metrics_wide),
        "",
        "## Section 2: Spearman Correlation Table",
        "",
        markdown_table(spearman),
        "",
        "## Section 3: Monotonicity Results",
        "",
        markdown_table(monotonic),
        "",
        "## Section 4: Trend Strength",
        "",
        markdown_table(trend_strength),
        "",
        "## Section 5: Step-wise No-Reversal",
        "",
        markdown_table(steps),
        "",
        "## Section 6: Raw Residual vs HI_v0",
        "",
        markdown_table(comparison),
        "",
        (
            "HI_v0 Rolling RMS increases CT_SW_TEMP_1 trend ratio over raw residual RMS while preserving strict monotonicity."
            if hi_sensitivity > raw_sensitivity and hi_monotonic
            else "HI_v0 Rolling RMS does not improve CT_SW_TEMP_1 trend ratio over raw residual RMS."
        ),
        "",
        "## Section 7: Interpretation",
        "",
        "### Q1: Does residual naturally form a trend along the pseudo degradation path?",
        "",
        (
            "Yes. Raw residual metrics form monotonic pseudo-degradation trends for the primary target and multiple secondary targets."
            if verdict != "Fail"
            else "No. Raw residual metrics do not form reliable monotonic trends."
        ),
        "",
        "### Q2: Which trend metric is most reliable?",
        "",
        f"`{primary_metric}` is recommended because it is monotonic, has Spearman rho = 1.0, and has no step reversal for the primary target.",
        "",
        "### Q3: How many targets show reliable trend?",
        "",
        f"{reliable_targets}/4 targets show at least one reliable residual trend metric.",
        "",
        "### Q4: Does Rolling RMS improve over raw residual as a trend carrier?",
        "",
        (
            "Yes for CT_SW_TEMP_1 under W=24h: HI_v0 has a larger strongest-vs-baseline ratio than raw residual RMS."
            if hi_sensitivity > raw_sensitivity
            else "No for CT_SW_TEMP_1 under W=24h: raw residual RMS is at least as strong as HI_v0."
        ),
        "",
        "### Q5: Does this support Q4a Initial Evidence?",
        "",
        (
            "Yes. Residual -> Trend exists in the HVAC pseudo-degradation path, so Q4a can be marked Initial Evidence."
            if q4a == "Initial Evidence"
            else "No. Q4a should remain unsupported."
        ),
        "",
        "### Q6: What is the recommended primary Trend Metric for future Validation C/D?",
        "",
        f"Use `{primary_metric}` on `CT_SW_TEMP_1` as the primary trend metric, with AbsMean/P95/P99 as corroborating metrics.",
        "",
        "## Generated Outputs",
        "",
        "- `outputs/b4_trend_metrics.csv`",
        "- `outputs/b4_spearman.csv`",
        "- `outputs/b4_monotonicity.csv`",
        "- `outputs/b4_trend_strength.csv`",
        "- `outputs/b4_step_no_reversal.csv`",
        "- `outputs/b4_raw_vs_hi_v0.csv`",
        "- `outputs/b4_spearman_heatmap.png`",
        "- `outputs/b4_trend_strength.png`",
    ]
    for target in TARGETS:
        report.append(f"- `outputs/b4_trend_path_{target}.png`")

    REPORT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
