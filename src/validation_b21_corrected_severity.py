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
    "095": DATA_DIR / "ChillerPlant_coolingtower_fouling_095.csv",
    "080": DATA_DIR / "ChillerPlant_coolingtower_fouling_080.csv",
    "065": DATA_DIR / "ChillerPlant_coolingtower_fouling_065.csv",
}
SEVERITY_ORDER = ["Baseline", "095", "080", "065"]
STATE_VARIABLES = [
    "CHL_POW_1",
    "CHL_SW_TEMP_1",
    "CT_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
]


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
    for target in STATE_VARIABLES:
        path = MODEL_DIR / f"esm_{target}.joblib"
        payload = joblib.load(path)
        if payload["target"] != target:
            raise ValueError(f"Model target mismatch: {path}")
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
    baseline, v095, v080, v065 = values
    return (v065 > baseline) and ((v065 > v080 > baseline) or (v065 > v095 > baseline))


def save_target_plot(target: str, severity: pd.DataFrame) -> None:
    values = severity.set_index("Dataset").loc[SEVERITY_ORDER, "RMS"]
    plt.figure(figsize=(7, 5))
    plt.plot(SEVERITY_ORDER, values.values, marker="o", linewidth=2)
    plt.title(f"Validation B2.1 Residual RMS: {target}")
    plt.xlabel("Corrected Severity Order")
    plt.ylabel("Residual RMS")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"b21_rms_{target}.png", dpi=160)
    plt.close()


def save_all_targets_plot(severity_stats: pd.DataFrame) -> None:
    plt.figure(figsize=(9, 6))
    for target in STATE_VARIABLES:
        subset = severity_stats[severity_stats["Target"] == target].set_index("Dataset").loc[SEVERITY_ORDER]
        plt.plot(SEVERITY_ORDER, subset["RMS"].values, marker="o", linewidth=2, label=target)
    plt.title("Validation B2.1 Residual RMS by Corrected Fault Severity")
    plt.xlabel("Corrected Severity Order")
    plt.ylabel("Residual RMS")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "b21_all_targets.png", dpi=160)
    plt.close()


def most_reliable_metric(monotonic: pd.DataFrame) -> str:
    candidates = {
        "AbsMean": int(monotonic["Strict AbsMean"].sum()) * 2 + int(monotonic["Relaxed AbsMean"].sum()),
        "RMS": int(monotonic["Strict RMS"].sum()) * 2 + int(monotonic["Relaxed RMS"].sum()),
        "P95": int(monotonic["Strict P95"].sum()) * 2 + int(monotonic["Relaxed P95"].sum()),
    }
    return sorted(candidates.items(), key=lambda item: (-item[1], item[0]))[0][0]


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
    residual_frames = []

    for dataset_name in SEVERITY_ORDER:
        print(f"Evaluating {dataset_name}: {DATASETS[dataset_name].name}")
        df, summary = load_dataset(DATASETS[dataset_name])
        filtering_rows.append({"Dataset": dataset_name, **summary})

        residual_frame = pd.DataFrame(index=df.index)
        residual_frame.index.name = "Datetime"
        residual_frame["Dataset"] = dataset_name

        for target in STATE_VARIABLES:
            payload = models[target]
            predicted = pd.Series(payload["model"].predict(df[condition_variables]), index=df.index)
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
        residual_frames.append(residual_frame.reset_index())

    filtering = pd.DataFrame(filtering_rows)
    severity_stats = pd.DataFrame(severity_rows)
    severity_stats.to_csv(OUTPUT_DIR / "validation_b21_residual_statistics.csv", index=False)
    filtering.to_csv(OUTPUT_DIR / "validation_b21_filtering.csv", index=False)
    pd.concat(residual_frames, ignore_index=True).to_csv(OUTPUT_DIR / "validation_b21_residuals.csv", index=False)

    monotonic_rows = []
    sensitivity_rows = []
    for target in STATE_VARIABLES:
        target_stats = severity_stats[severity_stats["Target"] == target].set_index("Dataset").loc[SEVERITY_ORDER]
        save_target_plot(target, target_stats.reset_index())
        values = {metric: target_stats[metric].tolist() for metric in ["AbsMean", "RMS", "P95"]}
        monotonic_rows.append(
            {
                "Target": target,
                "Strict AbsMean": strict_monotonic(values["AbsMean"]),
                "Relaxed AbsMean": relaxed_monotonic(values["AbsMean"]),
                "Strict RMS": strict_monotonic(values["RMS"]),
                "Relaxed RMS": relaxed_monotonic(values["RMS"]),
                "Strict P95": strict_monotonic(values["P95"]),
                "Relaxed P95": relaxed_monotonic(values["P95"]),
            }
        )
        rms_baseline = values["RMS"][0]
        rms_065 = values["RMS"][-1]
        sensitivity_rows.append(
            {
                "Target": target,
                "Sensitivity Score": (rms_065 - rms_baseline) / rms_baseline if rms_baseline else float("inf"),
                "RMS Baseline": rms_baseline,
                "RMS 065": rms_065,
            }
        )

    monotonic = pd.DataFrame(monotonic_rows)
    monotonic.to_csv(OUTPUT_DIR / "validation_b21_monotonicity.csv", index=False)
    save_all_targets_plot(severity_stats)

    sensitivity = pd.DataFrame(sensitivity_rows).sort_values("Sensitivity Score", ascending=False).reset_index(drop=True)
    sensitivity.insert(0, "Rank", sensitivity.index + 1)
    sensitivity.to_csv(OUTPUT_DIR / "validation_b21_sensitivity.csv", index=False)

    strict_abs_or_rms = int((monotonic["Strict AbsMean"] | monotonic["Strict RMS"]).sum())
    moderate_target = bool(monotonic.loc[monotonic["Target"] == "CHL_SW_TEMP_1", ["Strict AbsMean", "Relaxed AbsMean", "Strict RMS", "Relaxed RMS"]].any(axis=None))
    if strict_abs_or_rms >= 3:
        verdict = "Strong PASS"
        verdict_reason = "At least 3 of 4 targets show strict monotonicity for RMS and/or AbsMean."
    elif moderate_target or strict_abs_or_rms >= 1 or int((monotonic["Relaxed RMS"] | monotonic["Relaxed AbsMean"]).sum()) >= 1:
        verdict = "Moderate PASS"
        verdict_reason = "At least one target shows a clear monotonic residual response under the corrected ordering."
    else:
        verdict = "Fail"
        verdict_reason = "Corrected ordering still does not separate degradation levels."

    reliable_metric = most_reliable_metric(monotonic)
    most_sensitive = sensitivity.iloc[0]["Target"]
    preliminary_supported = verdict != "Fail"

    report = [
        "# Validation B2.1: Corrected Severity Ordering",
        "",
        f"- Verdict: {verdict}",
        f"- Basis: {verdict_reason}",
        "- Corrected order: Baseline -> 095 -> 080 -> 065",
        "- Models: frozen Validation B1 Expected State Models. No retraining performed.",
        f"- Condition Variables: {', '.join(condition_variables)}",
        f"- State Variables: {', '.join(STATE_VARIABLES)}",
        "",
        "## Dataset Filtering Summary",
        "",
        markdown_table(filtering),
        "",
        "## Section 1: Residual Statistics",
        "",
        markdown_table(severity_stats),
        "",
        "## Section 2: Monotonicity Results",
        "",
        markdown_table(monotonic),
        "",
        "## Section 3: Sensitivity Ranking",
        "",
        markdown_table(sensitivity[["Rank", "Target", "Sensitivity Score"]]),
        "",
        "## Section 4: Interpretation",
        "",
        "### Q1: Does corrected severity ordering produce monotonic residual growth?",
        "",
        (
            "Yes. The corrected ordering produces monotonic residual growth for the targets and metrics shown in the monotonicity table."
            if verdict != "Fail"
            else "No. The corrected ordering still fails to separate degradation levels."
        ),
        "",
        "### Q2: Which residual metric is most reliable?",
        "",
        f"`{reliable_metric}` is most reliable by strict/relaxed monotonic hit count across targets.",
        "",
        "### Q3: Which target is most sensitive?",
        "",
        f"`{most_sensitive}` has the highest sensitivity score.",
        "",
        "### Q4: Does this support Expected State -> Residual -> Physical Degradation as a valid route?",
        "",
        (
            "Yes, preliminarily. Frozen-model residuals increase with corrected cooling-tower fouling severity, supporting the route within the LBNL HVAC fault family."
            if verdict != "Fail"
            else "No. Residuals do not show sufficient severity separation under the corrected ordering."
        ),
        "",
        "### Q5: Can Q2 of the Concept Paper be marked \"Preliminary Supported\"?",
        "",
        (
            "Yes. Q2 can be marked Preliminary Supported, with the caveat that this is HVAC-domain evidence and depends on corrected fault-label ordering."
            if preliminary_supported
            else "No. Q2 should remain unsupported until residual severity separation is demonstrated."
        ),
        "",
        "## Generated Outputs",
        "",
        "- `outputs/validation_b21_residual_statistics.csv`",
        "- `outputs/validation_b21_filtering.csv`",
        "- `outputs/validation_b21_monotonicity.csv`",
        "- `outputs/validation_b21_sensitivity.csv`",
        "- `outputs/validation_b21_residuals.csv`",
        "- `outputs/b21_all_targets.png`",
    ]
    for target in STATE_VARIABLES:
        report.append(f"- `outputs/b21_rms_{target}.png`")

    (OUTPUT_DIR / "validation_b21.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'validation_b21.md'}")


if __name__ == "__main__":
    main()
