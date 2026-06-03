from __future__ import annotations

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "lbnl"
MODEL_DIR = PROJECT_ROOT / "src" / "expected_state_model"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

DATASETS = {
    "Baseline": DATA_DIR / "ChillerPlant.csv",
    "065": DATA_DIR / "ChillerPlant_coolingtower_fouling_065.csv",
    "080": DATA_DIR / "ChillerPlant_coolingtower_fouling_080.csv",
    "095": DATA_DIR / "ChillerPlant_coolingtower_fouling_095.csv",
}

DATASET_ORDER = ["Baseline", "065", "080", "095"]
STATE_VARIABLES = [
    "CHL_POW_1",
    "CHL_SW_TEMP_1",
    "CT_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
]

MODEL_FILES = {
    target: MODEL_DIR / f"esm_{target}.joblib"
    for target in STATE_VARIABLES
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


def load_models() -> dict[str, dict]:
    models = {}
    for target, path in MODEL_FILES.items():
        payload = joblib.load(path)
        if payload["target"] != target:
            raise ValueError(f"Model target mismatch for {path}: {payload['target']} != {target}")
        models[target] = payload
    return models


def load_dataset(path: Path) -> tuple[pd.DataFrame, dict[str, float | int]]:
    df = pd.read_csv(path, parse_dates=["Datetime"])
    df = df.set_index("Datetime").sort_index()
    rows_before = len(df)
    df = df[df["CHL_STA_1"] != 0].copy()
    rows_after = len(df)
    return df, {
        "Rows Before": rows_before,
        "Rows After": rows_after,
        "Retention %": rows_after / rows_before * 100 if rows_before else 0.0,
    }


def residual_rms(residual: pd.Series) -> float:
    return float((residual.pow(2).mean()) ** 0.5)


def strict_monotonic(values: list[float]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def relaxed_monotonic(values: list[float]) -> bool:
    baseline, v065, v080, v095 = values
    return (v095 > baseline) and ((v095 > v080 > baseline) or (v095 > v065 > baseline))


def save_target_plot(target: str, severity: pd.DataFrame) -> None:
    values = severity.set_index("Dataset").loc[DATASET_ORDER, "RMS"]
    plt.figure(figsize=(7, 5))
    plt.plot(DATASET_ORDER, values.values, marker="o", linewidth=2)
    plt.title(f"Validation B2 Residual RMS: {target}")
    plt.xlabel("Dataset")
    plt.ylabel("Residual RMS")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"b2_rms_{target}.png", dpi=160)
    plt.close()


def save_all_targets_plot(severity_stats: pd.DataFrame) -> None:
    plt.figure(figsize=(9, 6))
    for target in STATE_VARIABLES:
        subset = severity_stats[severity_stats["Target"] == target].set_index("Dataset").loc[DATASET_ORDER]
        plt.plot(DATASET_ORDER, subset["RMS"].values, marker="o", linewidth=2, label=target)
    plt.title("Validation B2 Residual RMS by Fault Severity")
    plt.xlabel("Dataset")
    plt.ylabel("Residual RMS")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "b2_all_targets_comparison.png", dpi=160)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    models = load_models()
    condition_variables = models[STATE_VARIABLES[0]]["condition_variables"]
    for target, payload in models.items():
        if payload["condition_variables"] != condition_variables:
            raise ValueError(f"Condition variable mismatch for {target}")

    train_std_table = pd.read_csv(OUTPUT_DIR / "residual_statistics.csv")
    train_std = dict(zip(train_std_table["Target"], train_std_table["Train Target Std"]))

    filtering_rows = []
    severity_rows = []
    normalized_residual_frames = []

    for dataset_name in DATASET_ORDER:
        path = DATASETS[dataset_name]
        print(f"Evaluating {dataset_name}: {path.name}")
        df, filter_summary = load_dataset(path)
        filtering_rows.append({"Dataset": dataset_name, **filter_summary})

        residual_frame = pd.DataFrame(index=df.index)
        residual_frame.index.name = "Datetime"
        residual_frame["Dataset"] = dataset_name

        for target in STATE_VARIABLES:
            payload = models[target]
            model = payload["model"]
            predicted = pd.Series(model.predict(df[condition_variables]), index=df.index)
            residual = df[target] - predicted
            residual_norm = residual / train_std[target]

            residual_frame[f"{target}_residual"] = residual
            residual_frame[f"{target}_residual_norm"] = residual_norm

            severity_rows.append(
                {
                    "Target": target,
                    "Dataset": dataset_name,
                    "Mean": float(residual.mean()),
                    "Std": float(residual.std()),
                    "RMS": residual_rms(residual),
                    "AbsMean": float(residual.abs().mean()),
                    "P95": float(residual.quantile(0.95)),
                }
            )

        normalized_residual_frames.append(residual_frame.reset_index())

    filtering = pd.DataFrame(filtering_rows)
    severity_stats = pd.DataFrame(severity_rows)
    severity_stats.to_csv(OUTPUT_DIR / "validation_b2_residual_statistics.csv", index=False)
    filtering.to_csv(OUTPUT_DIR / "validation_b2_filtering.csv", index=False)
    pd.concat(normalized_residual_frames, ignore_index=True).to_csv(
        OUTPUT_DIR / "validation_b2_residuals.csv",
        index=False,
    )

    monotonic_rows = []
    sensitivity_rows = []
    for target in STATE_VARIABLES:
        target_stats = severity_stats[severity_stats["Target"] == target].set_index("Dataset").loc[DATASET_ORDER]
        save_target_plot(target, target_stats.reset_index())
        metric_values = {
            metric: target_stats[metric].tolist()
            for metric in ["AbsMean", "RMS", "P95"]
        }
        monotonic_rows.append(
            {
                "Target": target,
                "Strict AbsMean": strict_monotonic(metric_values["AbsMean"]),
                "Relaxed AbsMean": relaxed_monotonic(metric_values["AbsMean"]),
                "Strict RMS": strict_monotonic(metric_values["RMS"]),
                "Relaxed RMS": relaxed_monotonic(metric_values["RMS"]),
                "Strict P95": strict_monotonic(metric_values["P95"]),
                "Relaxed P95": relaxed_monotonic(metric_values["P95"]),
            }
        )
        rms_baseline = metric_values["RMS"][0]
        rms_095 = metric_values["RMS"][-1]
        sensitivity_rows.append(
            {
                "Target": target,
                "Sensitivity Score": (rms_095 - rms_baseline) / rms_baseline if rms_baseline else float("inf"),
                "RMS Baseline": rms_baseline,
                "RMS 095": rms_095,
            }
        )

    save_all_targets_plot(severity_stats)
    monotonic = pd.DataFrame(monotonic_rows)
    monotonic.to_csv(OUTPUT_DIR / "validation_b2_monotonicity.csv", index=False)
    sensitivity = (
        pd.DataFrame(sensitivity_rows)
        .sort_values("Sensitivity Score", ascending=False)
        .reset_index(drop=True)
    )
    sensitivity.insert(0, "Rank", sensitivity.index + 1)
    sensitivity.to_csv(OUTPUT_DIR / "validation_b2_sensitivity.csv", index=False)

    relaxed_counts = int(monotonic["Relaxed RMS"].sum())
    strong_targets = severity_stats.pivot(index="Target", columns="Dataset", values="RMS")
    exceeds = (strong_targets["095"] > 1.5 * strong_targets["Baseline"]).to_dict()
    significant_exceeds = sum(bool(value) for value in exceeds.values())
    moderate_pass = bool(monotonic.loc[monotonic["Target"] == "CHL_SW_TEMP_1", "Relaxed RMS"].iloc[0])
    strong_pass = relaxed_counts >= 3 and significant_exceeds >= 3

    if strong_pass:
        verdict = "Strong PASS"
        verdict_reason = (
            "At least 3 of 4 targets show relaxed RMS monotonicity and RMS_095 substantially exceeds RMS_baseline."
        )
    elif moderate_pass or relaxed_counts >= 1:
        verdict = "Moderate PASS"
        verdict_reason = "At least one target shows a clear relaxed monotonic residual response."
    else:
        verdict = "Fail"
        verdict_reason = "Residual metrics do not separate severity levels reliably."

    strict_any = bool(
        monotonic[["Strict AbsMean", "Strict RMS", "Strict P95"]].any(axis=1).any()
    )
    relaxed_any = bool(
        monotonic[["Relaxed AbsMean", "Relaxed RMS", "Relaxed P95"]].any(axis=1).any()
    )
    most_sensitive = sensitivity.iloc[0]["Target"]

    report_lines = [
        "# Validation B2: Residual Severity Analysis",
        "",
        f"- Verdict: {verdict}",
        f"- Basis: {verdict_reason}",
        "- Models: frozen Validation B1 Expected State Models. No retraining performed.",
        f"- Condition Variables: {', '.join(condition_variables)}",
        f"- State Variables: {', '.join(STATE_VARIABLES)}",
        "",
        "## Section 1: Dataset Filtering Summary",
        "",
        markdown_table(filtering),
        "",
        "## Section 2: Residual Statistics",
        "",
        markdown_table(severity_stats),
        "",
        "## Section 3: Monotonic Severity Test",
        "",
        markdown_table(monotonic),
        "",
        "## Section 4: Sensitivity Ranking",
        "",
        markdown_table(sensitivity[["Rank", "Target", "Sensitivity Score"]]),
        "",
        "## Section 5: Interpretation",
        "",
        "### Q1: Do residuals increase when fouling severity increases?",
        "",
        (
            "Yes. Residual RMS increases with higher fouling severity for at least one target, and the strongest responses are visible in the sensitivity ranking."
            if relaxed_counts >= 1
            else "No. Residual RMS does not increase consistently enough to indicate severity separation."
        ),
        "",
        "### Q2: Does strict monotonicity hold?",
        "",
        (
            "Yes, strict monotonicity holds for at least one target/metric combination."
            if strict_any
            else "No. Baseline < 065 < 080 < 095 does not hold strictly across the tested residual metrics."
        ),
        "",
        "### Q3: Does relaxed monotonicity hold?",
        "",
        (
            f"Yes. Relaxed RMS monotonicity holds for {relaxed_counts} of 4 targets."
            if relaxed_any
            else "No. Relaxed monotonicity does not hold for the evaluated metrics."
        ),
        "",
        "### Q4: Which target is most sensitive?",
        "",
        f"`{most_sensitive}` has the highest sensitivity score.",
        "",
        "### Q5: Does this support Expected State -> Residual -> Degradation as a valid monitoring route?",
        "",
        (
            "Yes, with scope limits. The frozen Expected State residuals contain degradation information for cooling-tower fouling, but this validates severity response only for the LBNL HVAC domain."
            if verdict != "Fail"
            else "No. The tested residual metrics are insufficient to support the degradation route for this fault family."
        ),
        "",
        "### Q6: Can a simple HI_v0 be justified?",
        "",
        (
            "Yes. A simple HI_v0 based on normalized residual magnitude or residual RMS is justified as a first degradation indicator, because B2 shows residual separation by fouling severity."
            if verdict != "Fail"
            else "No. A simple HI_v0 is not justified until residual severity separation is demonstrated."
        ),
        "",
        "## Generated Outputs",
        "",
        "- `outputs/validation_b2_residual_statistics.csv`",
        "- `outputs/validation_b2_filtering.csv`",
        "- `outputs/validation_b2_monotonicity.csv`",
        "- `outputs/validation_b2_sensitivity.csv`",
        "- `outputs/validation_b2_residuals.csv`",
        "- `outputs/b2_all_targets_comparison.png`",
    ]
    for target in STATE_VARIABLES:
        report_lines.append(f"- `outputs/b2_rms_{target}.png`")

    (OUTPUT_DIR / "validation_b2.md").write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'validation_b2.md'}")


if __name__ == "__main__":
    main()
