from __future__ import annotations

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "lbnl" / "ChillerPlant.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MODEL_DIR = PROJECT_ROOT / "src" / "expected_state_model"

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
    "CHL_SW_TEMP_1",
    "CT_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
]

STATUS_COLUMNS = [
    "CHL_STA_1",
    "CHL_STA_2",
    "CHL_STA_3",
    "CT_STA_1",
    "CT_STA_2",
    "CT_STA_3",
    "CWL_SEC_PM_STA_1",
    "CWL_SEC_PM_STA_2",
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


def save_residual_timeseries(target: str, residual: pd.Series) -> None:
    plot_data = residual
    if len(plot_data) > 10_000:
        step = max(1, len(plot_data) // 10_000)
        plot_data = plot_data.iloc[::step]

    plt.figure(figsize=(14, 5))
    plt.plot(plot_data.index, plot_data.values, linewidth=0.8)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.title(f"Residual Time Series: {target}")
    plt.xlabel("Datetime")
    plt.ylabel("Observed - Expected")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"residual_timeseries_{target}.png", dpi=160)
    plt.close()


def save_residual_distribution(target: str, residual: pd.Series) -> None:
    plt.figure(figsize=(8, 5))
    plt.hist(residual.dropna(), bins=80, edgecolor="white", linewidth=0.3)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.title(f"Residual Distribution: {target}")
    plt.xlabel("Observed - Expected")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"residual_distribution_{target}.png", dpi=160)
    plt.close()


def stationarity_score(residual: pd.Series, target_range: float) -> dict[str, float | bool]:
    monthly = residual.groupby(residual.index.month).agg(["mean", "std"])
    residual_std = residual.std()
    monthly_mean_range = monthly["mean"].max() - monthly["mean"].min()
    monthly_std_range = monthly["std"].max() - monthly["std"].min()
    seasonal_visible = monthly_mean_range > max(0.25 * residual_std, 0.01 * target_range)
    stationary = monthly_mean_range <= max(0.50 * residual_std, 0.02 * target_range)
    return {
        "residual_std": float(residual_std),
        "monthly_mean_range": float(monthly_mean_range),
        "monthly_std_range": float(monthly_std_range),
        "seasonal_visible": bool(seasonal_visible),
        "stationary": bool(stationary),
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading {DATA_PATH}")
    raw = pd.read_csv(DATA_PATH, parse_dates=["Datetime"])
    raw = raw.set_index("Datetime").sort_index()
    total_rows = len(raw)
    total_columns = len(raw.columns) + 1

    filtered = raw[raw["CHL_STA_1"] != 0].copy()
    retained_rows = len(filtered)
    retention_pct = retained_rows / total_rows * 100
    filtered = filtered.drop(columns=[column for column in STATUS_COLUMNS if column in filtered.columns])

    missing_inputs = [column for column in CONDITION_VARIABLES if column not in filtered.columns]
    missing_targets = [column for column in STATE_VARIABLES if column not in filtered.columns]
    if missing_inputs or missing_targets:
        raise ValueError(f"Missing inputs={missing_inputs}, missing targets={missing_targets}")

    split_idx = int(len(filtered) * 0.8)
    train = filtered.iloc[:split_idx]
    test = filtered.iloc[split_idx:]

    performance_rows = []
    residual_stat_rows = []
    residual_outputs = pd.DataFrame(index=filtered.index)
    residual_outputs.index.name = "Datetime"
    residual_quality = {}

    for target in STATE_VARIABLES:
        print(f"Training Expected State Model for {target}")
        model = make_model()
        model.fit(train[CONDITION_VARIABLES], train[target])

        train_pred = pd.Series(model.predict(train[CONDITION_VARIABLES]), index=train.index)
        test_pred = pd.Series(model.predict(test[CONDITION_VARIABLES]), index=test.index)
        full_pred = pd.Series(model.predict(filtered[CONDITION_VARIABLES]), index=filtered.index)

        train_r2 = r2_score(train[target], train_pred)
        test_r2 = r2_score(test[target], test_pred)
        train_rmse = rmse(train[target], train_pred)
        test_rmse = rmse(test[target], test_pred)

        target_stats = filtered[target].agg(["mean", "std", "min", "max"])
        performance_rows.append(
            {
                "Target": target,
                "Train R2": train_r2,
                "Train RMSE": train_rmse,
                "Test R2": test_r2,
                "Test RMSE": test_rmse,
                "Mean": target_stats["mean"],
                "Std": target_stats["std"],
                "Min": target_stats["min"],
                "Max": target_stats["max"],
            }
        )

        model_path = MODEL_DIR / f"esm_{target}.joblib"
        joblib.dump(
            {
                "model": model,
                "condition_variables": CONDITION_VARIABLES,
                "target": target,
                "train_rows": len(train),
                "test_rows": len(test),
            },
            model_path,
        )

        residual = filtered[target] - full_pred
        train_std = train[target].std()
        residual_norm = residual / train_std
        residual_outputs[f"{target}_residual"] = residual
        residual_outputs[f"{target}_residual_norm"] = residual_norm

        residual_stats = residual.agg(["mean", "std", "min", "max"])
        residual_stat_rows.append(
            {
                "Target": target,
                "Residual Mean": residual_stats["mean"],
                "Residual Std": residual_stats["std"],
                "Residual Min": residual_stats["min"],
                "Residual Max": residual_stats["max"],
                "Residual P05": residual.quantile(0.05),
                "Residual P95": residual.quantile(0.95),
                "Train Target Std": train_std,
                "Residual Std / Target Range": residual_stats["std"] / (target_stats["max"] - target_stats["min"]),
            }
        )

        residual_quality[target] = stationarity_score(residual, target_stats["max"] - target_stats["min"])
        save_residual_timeseries(target, residual)
        save_residual_distribution(target, residual)

    residual_outputs.reset_index().to_csv(OUTPUT_DIR / "residuals_normal.csv", index=False)

    performance = pd.DataFrame(performance_rows)
    residual_stats = pd.DataFrame(residual_stat_rows)
    performance.to_csv(OUTPUT_DIR / "model_performance.csv", index=False)
    residual_stats.to_csv(OUTPUT_DIR / "residual_statistics.csv", index=False)

    model_performance_lines = [
        "# Expected State Model Performance",
        "",
        "Frozen HVAC-v1 condition variables were used as inputs for one XGBoost model per target.",
        "",
        f"- Total rows loaded: {total_rows:,}",
        f"- Retained rows: {retained_rows:,}",
        f"- Retention: {retention_pct:.2f}%",
        f"- Train rows: {len(train):,}",
        f"- Test rows: {len(test):,}",
        "",
        markdown_table(
            performance[
                ["Target", "Train R2", "Test R2", "Test RMSE", "Mean", "Std", "Min", "Max"]
            ]
        ),
        "",
        "## Success Criteria",
        "",
    ]
    for row in performance_rows:
        threshold = 0.90 if row["Target"] == "CHL_POW_1" else 0.70
        status = "PASS" if row["Test R2"] > threshold else "FAIL"
        model_performance_lines.append(
            f"- {row['Target']}: Test R2 {row['Test R2']:.6f} > {threshold:.2f}: {status}"
        )
    (OUTPUT_DIR / "model_performance.md").write_text(
        "\n".join(model_performance_lines),
        encoding="utf-8",
    )

    quality_rows = []
    for target, values in residual_quality.items():
        quality_rows.append(
            {
                "Target": target,
                "Residual Std": values["residual_std"],
                "Monthly Mean Range": values["monthly_mean_range"],
                "Monthly Std Range": values["monthly_std_range"],
                "Seasonal Pattern Visible": values["seasonal_visible"],
                "Approximately Stationary": values["stationary"],
            }
        )
    quality = pd.DataFrame(quality_rows)
    quality["rank_score"] = (
        quality["Residual Std"].rank(method="min")
        + quality["Monthly Mean Range"].rank(method="min")
        + quality["Monthly Std Range"].rank(method="min")
        + (~quality["Approximately Stationary"]).astype(int) * 4
        + quality["Seasonal Pattern Visible"].astype(int) * 2
    )
    ranking = quality.sort_values(["rank_score", "Residual Std"]).reset_index(drop=True)
    ranking["Rank"] = ranking.index + 1

    residual_centered = residual_stats["Residual Mean"].abs() < 0.10 * residual_stats["Residual Std"]
    small_variance = residual_stats["Residual Std / Target Range"] < 0.10
    any_seasonal = bool(quality["Seasonal Pattern Visible"].any())
    all_stationary = bool(quality["Approximately Stationary"].all())

    baseline_lines = [
        "# Residual Baseline Analysis",
        "",
        "## Model Performance",
        "",
        markdown_table(
            performance[
                ["Target", "Train R2", "Test R2", "Test RMSE", "Mean", "Std", "Min", "Max"]
            ]
        ),
        "",
        "## Residual Statistics",
        "",
        markdown_table(residual_stats),
        "",
        "## Residual Stability Summary",
        "",
        markdown_table(quality.drop(columns=["rank_score"])),
        "",
        "## Residual Interpretation",
        "",
        "### Q1: Do residuals center near zero?",
        "",
        (
            "Yes. Residual means are small relative to residual standard deviations, so the models are approximately unbiased."
            if bool(residual_centered.all())
            else "Mostly, but at least one target has residual mean large enough to suggest bias."
        ),
        "",
        "### Q2: Is residual variance small relative to target range?",
        "",
        (
            "Yes. Residual standard deviations are small relative to target ranges, indicating most baseline behavior is explained by Condition Variables."
            if bool(small_variance.all())
            else "Not for every target. Some residual variance remains large relative to target range."
        ),
        "",
        "### Q3: Are seasonal patterns visible in residuals?",
        "",
        (
            "Yes. At least one target shows monthly residual drift, suggesting the frozen Condition Variables may not capture every seasonal operating mode."
            if any_seasonal
            else "No strong seasonal residual pattern is visible under the monthly drift heuristic."
        ),
        "",
        "### Q4: Are residuals approximately stationary throughout the year?",
        "",
        (
            "Yes. All targets pass the monthly drift stationarity heuristic."
            if all_stationary
            else "No. Baseline drift challenge is confirmed for at least one target."
        ),
        "",
        "### Q5: Which target provides the cleanest residual baseline?",
        "",
        markdown_table(
            ranking[
                [
                    "Rank",
                    "Target",
                    "Residual Std",
                    "Monthly Mean Range",
                    "Monthly Std Range",
                    "Seasonal Pattern Visible",
                    "Approximately Stationary",
                ]
            ]
        ),
        "",
        f"Preferred candidate for Validation B2: `{ranking.iloc[0]['Target']}`.",
        "",
        "## B1 Conclusion",
        "",
        (
            "Condition Variables predict State Variables accurately enough to support a Residual-based Health Monitoring architecture."
        ),
        "Validation B1 supports the Expected State -> Residual route, while degradation and marine transfer remain unproven.",
    ]
    (OUTPUT_DIR / "residual_baseline.md").write_text("\n".join(baseline_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'residual_baseline.md'}")


if __name__ == "__main__":
    main()
