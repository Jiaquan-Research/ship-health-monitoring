from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "lbnl"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_PATH = OUTPUT_DIR / "b3a_temporal_resolution.md"

DATASETS = {
    "Baseline": DATA_DIR / "ChillerPlant.csv",
    "095": DATA_DIR / "ChillerPlant_coolingtower_fouling_095.csv",
    "080": DATA_DIR / "ChillerPlant_coolingtower_fouling_080.csv",
    "065": DATA_DIR / "ChillerPlant_coolingtower_fouling_065.csv",
}
DATASET_ORDER = ["Baseline", "095", "080", "065"]

SAMPLING = {
    "1min": None,
    "15min": "15min",
    "1h": "1h",
    "2h": "2h",
}

CONDITION_VARIABLES = [
    "CWL_SEC_LOAD",
    "OA_TEMP",
    "OA_TEMP_WB",
    "CWL_PRI_SW_TEMPSPT",
    "CT_SW_TEMPSPT",
    "CWL_SEC_DPSPT",
]

STATE_VARIABLES = [
    "CHL_POW_1",
    "CT_SW_TEMP_1",
    "CHL_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
]

READ_COLUMNS = ["Datetime", "CHL_STA_1"] + CONDITION_VARIABLES + STATE_VARIABLES


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


def make_model() -> XGBRegressor:
    return XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=-1,
        tree_method="hist",
    )


def rmse(y_true: pd.Series, y_pred: pd.Series) -> float:
    return mean_squared_error(y_true, y_pred) ** 0.5


def strict_monotonic(values: list[float]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def load_base_datasets() -> dict[str, pd.DataFrame]:
    datasets = {}
    for name, path in DATASETS.items():
        print(f"Loading {name}: {path.name}")
        df = pd.read_csv(path, usecols=READ_COLUMNS, parse_dates=["Datetime"])
        df = df.set_index("Datetime").sort_index()
        df = df[df["CHL_STA_1"] != 0].drop(columns=["CHL_STA_1"])
        datasets[name] = df
    return datasets


def resample_dataset(df: pd.DataFrame, rule: str | None) -> pd.DataFrame:
    if rule is None:
        return df.copy()
    return df.resample(rule).mean().dropna()


def train_models(baseline: pd.DataFrame) -> tuple[dict[str, XGBRegressor], list[dict[str, object]]]:
    split_idx = int(len(baseline) * 0.8)
    train = baseline.iloc[:split_idx]
    test = baseline.iloc[split_idx:]
    models = {}
    rows = []
    for target in STATE_VARIABLES:
        model = make_model()
        model.fit(train[CONDITION_VARIABLES], train[target])
        train_pred = pd.Series(model.predict(train[CONDITION_VARIABLES]), index=train.index)
        test_pred = pd.Series(model.predict(test[CONDITION_VARIABLES]), index=test.index)
        rows.append(
            {
                "Target": target,
                "Train Rows": len(train),
                "Test Rows": len(test),
                "Train R2": r2_score(train[target], train_pred),
                "Test R2": r2_score(test[target], test_pred),
                "RMSE": rmse(test[target], test_pred),
            }
        )
        models[target] = model
    return models, rows


def compute_residual_stats(
    datasets: dict[str, pd.DataFrame],
    models: dict[str, XGBRegressor],
) -> list[dict[str, object]]:
    rows = []
    for target, model in models.items():
        for dataset_name in DATASET_ORDER:
            df = datasets[dataset_name]
            pred = pd.Series(model.predict(df[CONDITION_VARIABLES]), index=df.index)
            residual = df[target] - pred
            rows.append(
                {
                    "Target": target,
                    "Dataset": dataset_name,
                    "Residual Mean": residual.mean(),
                    "Residual RMS": (residual.pow(2).mean()) ** 0.5,
                    "Residual P95": residual.quantile(0.95),
                }
            )
    return rows


def expected_state_pass(row: pd.Series) -> bool:
    threshold = 0.90 if row["Target"] == "CHL_POW_1" else 0.70
    return bool(row["Test R2"] > threshold)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_datasets = load_base_datasets()

    sample_count_rows = []
    b1_rows = []
    residual_rows = []
    b21_rows = []
    sensitivity_rows = []

    for sampling_label, rule in SAMPLING.items():
        print(f"Processing sampling level: {sampling_label}")
        sampled = {
            name: resample_dataset(df, rule)
            for name, df in raw_datasets.items()
        }
        for dataset_name in DATASET_ORDER:
            sample_count_rows.append(
                {
                    "Sampling": sampling_label,
                    "Dataset": dataset_name,
                    "Rows": len(sampled[dataset_name]),
                }
            )

        models, model_rows = train_models(sampled["Baseline"])
        for row in model_rows:
            row["Sampling"] = sampling_label
            b1_rows.append(row)

        stats = compute_residual_stats(sampled, models)
        for row in stats:
            row["Sampling"] = sampling_label
            residual_rows.append(row)

        stats_df = pd.DataFrame(stats)
        for target in STATE_VARIABLES:
            target_stats = stats_df[stats_df["Target"] == target].set_index("Dataset").loc[DATASET_ORDER]
            rms_values = target_stats["Residual RMS"].tolist()
            mean_values = target_stats["Residual Mean"].tolist()
            p95_values = target_stats["Residual P95"].tolist()
            baseline_rms = target_stats.loc["Baseline", "Residual RMS"]
            strongest_rms = target_stats.loc["065", "Residual RMS"]
            sensitivity = (strongest_rms - baseline_rms) / baseline_rms if baseline_rms else float("inf")
            b21_rows.append(
                {
                    "Sampling": sampling_label,
                    "Target": target,
                    "RMS_065/RMS_baseline": strongest_rms / baseline_rms if baseline_rms else float("inf"),
                    "Strict RMS Monotonic": strict_monotonic(rms_values),
                    "Strict Mean Monotonic": strict_monotonic(mean_values),
                    "Strict P95 Monotonic": strict_monotonic(p95_values),
                }
            )
            sensitivity_rows.append(
                {
                    "Sampling": sampling_label,
                    "Target": target,
                    "Sensitivity": sensitivity,
                }
            )

    sample_counts = pd.DataFrame(sample_count_rows)
    b1_results = pd.DataFrame(b1_rows)[
        ["Sampling", "Target", "Train Rows", "Test Rows", "Train R2", "Test R2", "RMSE"]
    ]
    residual_stats = pd.DataFrame(residual_rows)[
        ["Sampling", "Target", "Dataset", "Residual Mean", "Residual RMS", "Residual P95"]
    ]
    b21_results = pd.DataFrame(b21_rows)
    sensitivity = pd.DataFrame(sensitivity_rows)

    baseline_sensitivity = sensitivity[sensitivity["Sampling"] == "1min"].set_index("Target")["Sensitivity"]
    retention_rows = []
    for _, row in sensitivity.iterrows():
        retention_rows.append(
            {
                "Sampling": row["Sampling"],
                "Target": row["Target"],
                "Sensitivity": row["Sensitivity"],
                "Retention Ratio": row["Sensitivity"] / baseline_sensitivity[row["Target"]],
            }
        )
    retention = pd.DataFrame(retention_rows)

    b1_results["B1 Pass"] = b1_results.apply(expected_state_pass, axis=1)
    sampling_summary_rows = []
    for sampling_label in SAMPLING:
        b1_pass = bool(b1_results[b1_results["Sampling"] == sampling_label]["B1 Pass"].all())
        b21_pass = bool(b21_results[b21_results["Sampling"] == sampling_label]["Strict RMS Monotonic"].all())
        min_retention = float(retention[retention["Sampling"] == sampling_label]["Retention Ratio"].min())
        sampling_summary_rows.append(
            {
                "Sampling": sampling_label,
                "B1 Pass": b1_pass,
                "B2.1 RMS Monotonic Pass": b21_pass,
                "Min Retention Ratio": min_retention,
                "Overall Pass": b1_pass and b21_pass and min_retention >= 0.80,
            }
        )
    sampling_summary = pd.DataFrame(sampling_summary_rows)

    sample_counts.to_csv(OUTPUT_DIR / "b3a_sample_counts.csv", index=False)
    b1_results.to_csv(OUTPUT_DIR / "b3a_b1_results.csv", index=False)
    residual_stats.to_csv(OUTPUT_DIR / "b3a_residual_stats.csv", index=False)
    b21_results.to_csv(OUTPUT_DIR / "b3a_b21_results.csv", index=False)
    retention.to_csv(OUTPUT_DIR / "b3a_sensitivity_retention.csv", index=False)
    sampling_summary.to_csv(OUTPUT_DIR / "b3a_sampling_summary.csv", index=False)

    if bool(sampling_summary[sampling_summary["Sampling"] == "2h"]["Overall Pass"].iloc[0]):
        verdict = "Strong Evidence"
        minimum_interval = "2h"
    elif bool(sampling_summary[sampling_summary["Sampling"] == "1h"]["Overall Pass"].iloc[0]):
        verdict = "Moderate Evidence"
        minimum_interval = "1h"
    elif bool(sampling_summary[sampling_summary["Sampling"] == "15min"]["Overall Pass"].iloc[0]):
        verdict = "Weak Evidence"
        minimum_interval = "15min"
    else:
        verdict = "Failure"
        minimum_interval = "1min only / unresolved"

    report = [
        "# Validation B3A: Temporal Resolution Feasibility Audit",
        "",
        f"- Verdict: {verdict}",
        f"- Minimum viable sampling interval under conservative criteria: {minimum_interval}",
        "- Scope: Expected State and raw residual severity replication only.",
        "- Excluded: HI_v0, CUSUM, EWMA, VIB, Autoencoder, Transformer, mapping changes.",
        "",
        "## Section 1: Sample Count Audit",
        "",
        markdown_table(sample_counts),
        "",
        "## Section 2: B1 Results",
        "",
        markdown_table(b1_results),
        "",
        "## Section 3: B2.1 Results",
        "",
        markdown_table(b21_results),
        "",
        "### Residual Statistics",
        "",
        markdown_table(residual_stats),
        "",
        "## Section 4: Sensitivity Retention Audit",
        "",
        markdown_table(retention),
        "",
        "### Sampling Summary",
        "",
        markdown_table(sampling_summary),
        "",
        "## Section 5: Conclusion",
        "",
        "### Q1: How far can sampling frequency be reduced before Expected State performance degrades?",
        "",
    ]

    b1_all_pass = [
        row["Sampling"]
        for _, row in sampling_summary.iterrows()
        if row["B1 Pass"]
    ]
    report.extend(
        [
            (
                f"Expected State performance passes through: {', '.join(b1_all_pass)}."
                if b1_all_pass
                else "Expected State performance does not pass even at the audited reduced sampling levels."
            ),
            "",
            "### Q2: How far can sampling frequency be reduced before degradation detection fails?",
            "",
        ]
    )

    b21_pass_levels = [
        row["Sampling"]
        for _, row in sampling_summary.iterrows()
        if row["B2.1 RMS Monotonic Pass"]
    ]
    report.extend(
        [
            (
                f"Residual RMS monotonicity passes through: {', '.join(b21_pass_levels)}."
                if b21_pass_levels
                else "Residual RMS monotonicity does not pass under the audited sampling levels."
            ),
            "",
            "### Q3: What is the minimum viable sampling interval?",
            "",
            minimum_interval,
            "",
            "### Q4: Do results support future Marine deployment?",
            "",
            (
                "Yes, preliminarily. The conservative audit supports lower-frequency monitoring and suggests marine hourly/logbook-scale data may be usable, subject to marine-domain validation."
                if verdict in {"Strong Evidence", "Moderate Evidence"}
                else "Only weakly or not yet. Marine deployment still likely requires higher-frequency exports or further validation."
            ),
        ]
    )

    REPORT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
