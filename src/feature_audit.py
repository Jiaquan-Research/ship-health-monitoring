from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "lbnl" / "ChillerPlant.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
TARGET = "CHL_POW_1"
POWER_LEAKAGE = ["CHL_POW_1", "CHL_POW_2", "CHL_POW_3"]
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
ENGINEERING_CONDITION_FEATURES = [
    "CWL_SEC_LOAD",
    "OA_TEMP",
    "OA_TEMP_WB",
    "CWL_PRI_SW_TEMPSPT",
    "CT_SW_TEMPSPT",
    "CWL_SEC_DPSPT",
]
MI_MAX_ROWS = 100_000
RANDOM_STATE = 42


def make_model() -> XGBRegressor:
    return XGBRegressor(
        n_estimators=350,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        objective="reg:squarederror",
        random_state=RANDOM_STATE,
        n_jobs=-1,
        tree_method="hist",
    )


def markdown_table(df: pd.DataFrame, index: bool = False, floatfmt: str = ".6g") -> str:
    rendered = df.reset_index() if index else df.copy()
    headers = [str(column) for column in rendered.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for _, row in rendered.iterrows():
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


def save_prediction_plot(
    actual: pd.Series,
    predicted: pd.Series,
    title: str,
    output_path: Path,
    max_points: int = 5_000,
) -> None:
    plot_df = pd.DataFrame({"Actual": actual, "Predicted": predicted}, index=actual.index)
    if len(plot_df) > max_points:
        plot_df = plot_df.iloc[:: math.ceil(len(plot_df) / max_points)]

    plt.figure(figsize=(13, 5))
    plt.plot(plot_df.index, plot_df["Actual"], label="Actual", linewidth=1.2)
    plt.plot(plot_df.index, plot_df["Predicted"], label="Predicted", linewidth=1.0, alpha=0.85)
    plt.title(title)
    plt.xlabel("Datetime")
    plt.ylabel(TARGET)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()


def train_model(
    df: pd.DataFrame,
    features: list[str],
    model_name: str,
    plot_path: Path,
) -> tuple[dict[str, float], pd.DataFrame]:
    data = df[features + [TARGET]].dropna()
    split_idx = int(len(data) * 0.8)
    train = data.iloc[:split_idx]
    test = data.iloc[split_idx:]

    model = make_model()
    model.fit(train[features], train[TARGET])
    predicted = pd.Series(model.predict(test[features]), index=test.index, name="Predicted")

    rmse = mean_squared_error(test[TARGET], predicted) ** 0.5
    metrics = {
        "rows_used": float(len(data)),
        "train_rows": float(len(train)),
        "test_rows": float(len(test)),
        "r2": float(r2_score(test[TARGET], predicted)),
        "rmse": float(rmse),
    }

    importance = (
        pd.DataFrame(
            {
                "feature": features,
                "importance": model.feature_importances_,
            }
        )
        .sort_values("importance", ascending=False)
        .reset_index(drop=True)
    )

    save_prediction_plot(test[TARGET], predicted, model_name, plot_path)
    return metrics, importance


def classify_feature(column: str, pearson_abs: float | None = None, mi_rank: int | None = None) -> str:
    name = column.upper()
    if column in STATUS_COLUMNS:
        return "Control Candidates"
    if column == "Datetime":
        return "Condition Candidates"
    if any(token in name for token in ("SPT", "SETPOINT", "DPSPT", "TEMPSPT")):
        return "Condition Candidates"
    if name in {"OA_TEMP", "OA_TEMP_WB", "CWL_SEC_LOAD"} or "LOAD" in name:
        return "Condition Candidates"
    if "CTRL" in name or "SPD_CTRL" in name or "TWV" in name:
        return "Control Candidates"
    if pearson_abs is not None and pearson_abs >= 0.85 and column != TARGET:
        return "Leakage Risk Features"
    if mi_rank is not None and mi_rank <= 10 and column not in ENGINEERING_CONDITION_FEATURES:
        if any(token in name for token in ("TEMP", "FLOW", "POW", "DP", "SPD")):
            return "Leakage Risk Features"
    if any(token in name for token in ("TEMP", "FLOW", "POW", "DP", "SPD")):
        return "State Candidates"
    return "State Candidates"


def write_feature_groups(
    columns: list[str],
    pearson: pd.DataFrame,
    mi: pd.DataFrame,
    output_path: Path,
) -> tuple[pd.DataFrame, dict[str, int]]:
    pearson_lookup = dict(zip(pearson["feature"], pearson["abs_correlation"]))
    mi_rank_lookup = {feature: rank + 1 for rank, feature in enumerate(mi["feature"].tolist())}
    rows = []
    for column in columns:
        group = classify_feature(column, pearson_lookup.get(column), mi_rank_lookup.get(column))
        rows.append(
            {
                "feature": column,
                "group": group,
                "abs_correlation_to_CHL_POW_1": pearson_lookup.get(column),
                "mi_rank": mi_rank_lookup.get(column),
            }
        )
    groups = pd.DataFrame(rows)
    summary = groups["group"].value_counts().sort_index().to_dict()

    lines = [
        "# Feature Groups",
        "",
        "Heuristic classification for all baseline columns after status-column removal.",
        "",
        "## Summary",
        "",
        markdown_table(pd.DataFrame({"group": summary.keys(), "count": summary.values()})),
        "",
    ]
    for group_name in [
        "Condition Candidates",
        "State Candidates",
        "Control Candidates",
        "Leakage Risk Features",
    ]:
        subset = groups[groups["group"] == group_name].copy()
        lines.extend([f"## {group_name}", ""])
        if subset.empty:
            lines.append("None.")
        else:
            lines.append(markdown_table(subset.fillna("")))
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return groups, summary


def stability_audit(df: pd.DataFrame, output_path: Path) -> tuple[dict[str, list[str]], set[str], dict[str, list[str]]]:
    seasonal_rankings: dict[str, list[str]] = {}
    lines = ["# Feature Stability Audit", ""]
    for month, name in [(1, "January"), (6, "June"), (12, "December")]:
        sample = df[df.index.month == month]
        correlations = (
            sample.select_dtypes(include="number")
            .corrwith(sample[TARGET])
            .drop(labels=[TARGET], errors="ignore")
            .dropna()
            .rename("correlation")
            .to_frame()
        )
        correlations["abs_correlation"] = correlations["correlation"].abs()
        top = correlations.sort_values("abs_correlation", ascending=False).head(10).reset_index()
        top = top.rename(columns={"index": "feature"})
        seasonal_rankings[name] = top["feature"].tolist()
        lines.extend([f"## {name}", "", markdown_table(top), ""])

    ranking_sets = {name: set(values) for name, values in seasonal_rankings.items()}
    common = set.intersection(*ranking_sets.values())
    all_ranked = set.union(*ranking_sets.values())
    drift = {name: sorted(values - common) for name, values in ranking_sets.items()}

    lines.extend(
        [
            "## Overlap Summary",
            "",
            f"- Common variables across January, June, and December: {len(common)}",
            f"- Common variables: {', '.join(sorted(common)) if common else 'None'}",
            f"- Variables appearing in at least one seasonal top 10: {len(all_ranked)}",
            "",
            "## Drift",
            "",
        ]
    )
    for name, variables in drift.items():
        lines.append(f"- {name}: {', '.join(variables) if variables else 'No drift from common set'}")

    stable = len(common) >= 5
    lines.extend(
        [
            "",
            "## Answer",
            "",
            (
                "Dominant predictors are reasonably stable across the year."
                if stable
                else "Dominant predictors drift substantially across the year."
            ),
        ]
    )
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return seasonal_rankings, common, drift


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading {DATA_PATH}")
    df = pd.read_csv(DATA_PATH, parse_dates=["Datetime"])
    df = df.set_index("Datetime").sort_index()
    total_rows = len(df)
    total_columns = len(df.columns) + 1
    rows_before = len(df)

    df = df[df["CHL_STA_1"] != 0].copy()
    rows_after = len(df)
    retained_pct = rows_after / rows_before * 100
    df = df.drop(columns=[col for col in STATUS_COLUMNS if col in df.columns])
    numeric_df = df.select_dtypes(include="number")

    print("Computing Pearson correlations")
    pearson = (
        numeric_df.corrwith(numeric_df[TARGET])
        .drop(labels=[TARGET], errors="ignore")
        .dropna()
        .rename("correlation")
        .to_frame()
    )
    pearson["abs_correlation"] = pearson["correlation"].abs()
    pearson = pearson.sort_values("abs_correlation", ascending=False).reset_index()
    pearson = pearson.rename(columns={"index": "feature"})
    pearson_top20 = pearson.head(20)
    pearson_top20.to_csv(OUTPUT_DIR / "feature_audit_pearson_top20.csv", index=False)

    print("Computing mutual information")
    mi_features = [col for col in numeric_df.columns if col != TARGET]
    mi_data = numeric_df[mi_features + [TARGET]].dropna()
    if len(mi_data) > MI_MAX_ROWS:
        mi_data = mi_data.iloc[:MI_MAX_ROWS]
        mi_note = f"MI computed on first {MI_MAX_ROWS:,} filtered rows."
    else:
        mi_note = f"MI computed on all {len(mi_data):,} filtered rows."
    mi_values = mutual_info_regression(
        mi_data[mi_features],
        mi_data[TARGET],
        random_state=RANDOM_STATE,
        n_neighbors=5,
    )
    mi = (
        pd.DataFrame({"feature": mi_features, "mutual_information": mi_values})
        .sort_values("mutual_information", ascending=False)
        .reset_index(drop=True)
    )
    mi_top20 = mi.head(20)
    mi_top20.to_csv(OUTPUT_DIR / "feature_audit_mi_top20.csv", index=False)

    print("Training Model A")
    model_a_features = [col for col in numeric_df.columns if col not in POWER_LEAKAGE]
    model_a_metrics, model_a_importance = train_model(
        numeric_df,
        model_a_features,
        "Model A: All Features Baseline",
        OUTPUT_DIR / "model_a_prediction.png",
    )
    model_a_importance.head(20).to_csv(OUTPUT_DIR / "model_a_feature_importance_top20.csv", index=False)

    print("Training Model B")
    model_b_features = [col for col in ENGINEERING_CONDITION_FEATURES if col in numeric_df.columns]
    model_b_metrics, model_b_importance = train_model(
        numeric_df,
        model_b_features,
        "Model B: Engineering Condition Variables",
        OUTPUT_DIR / "model_b_prediction.png",
    )
    model_b_importance.to_csv(OUTPUT_DIR / "model_b_feature_importance.csv", index=False)

    print("Training Model C")
    model_c_features = []
    for feature in mi["feature"].tolist():
        if feature in POWER_LEAKAGE or feature == TARGET:
            continue
        if feature not in model_c_features:
            model_c_features.append(feature)
        if len(model_c_features) == 10:
            break
    model_c_metrics, model_c_importance = train_model(
        numeric_df,
        model_c_features,
        "Model C: Data-Driven Condition Variables",
        OUTPUT_DIR / "model_c_prediction.png",
    )
    model_c_importance.to_csv(OUTPUT_DIR / "model_c_feature_importance.csv", index=False)

    print("Writing feature groups and stability audit")
    feature_groups, group_summary = write_feature_groups(
        ["Datetime"] + df.columns.tolist(),
        pearson,
        mi,
        OUTPUT_DIR / "feature_groups.md",
    )
    seasonal_rankings, common_stability, drift = stability_audit(
        numeric_df,
        OUTPUT_DIR / "feature_stability.md",
    )

    print("Writing correlation heatmap")
    heatmap_features = pearson_top20["feature"].tolist()
    corr_matrix = numeric_df[heatmap_features + [TARGET]].corr()
    plt.figure(figsize=(14, 12))
    sns.heatmap(corr_matrix, cmap="vlag", center=0, square=False)
    plt.title("Top 20 Correlated Variables to CHL_POW_1")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "feature_audit_correlation_plot.png", dpi=160)
    plt.close()

    performance_loss = model_a_metrics["r2"] - model_b_metrics["r2"]
    relative_rmse = model_b_metrics["rmse"] / model_a_metrics["rmse"] if model_a_metrics["rmse"] else float("inf")
    model_b_r2 = model_b_metrics["r2"]
    if model_b_r2 > 0.70:
        condition_answer = "Strong evidence that Condition Variables are sufficient."
    elif model_b_r2 >= 0.50:
        condition_answer = "Route appears viable, but Condition Variables require refinement."
    elif model_b_r2 < 0.30:
        condition_answer = "Current Condition Variable definition is likely incorrect."
    else:
        condition_answer = "Evidence is weak-to-moderate; Condition Variables likely need refinement."

    model_c_delta = model_c_metrics["r2"] - model_b_metrics["r2"]
    if model_c_delta > 0.05:
        discovery_answer = "Model C materially outperforms Model B, so important Condition Variables may be missing."
    else:
        discovery_answer = "Model C is close to Model B, so engineering variable selection is broadly aligned."

    stable_answer = (
        "Dominant predictors are reasonably stable across the year."
        if len(common_stability) >= 5
        else "Dominant predictors drift substantially across the year."
    )
    viable_answer = (
        "The Expected State -> Residual route is viable for CHL_POW_1."
        if model_b_r2 >= 0.50
        else "The Expected State -> Residual route is not yet supported by the current Condition Variable set."
    )

    report_lines = [
        "# Feature Audit: Expected State Route",
        "",
        "## 1. Dataset Summary",
        "",
        f"- Source file: `{DATA_PATH.relative_to(PROJECT_ROOT)}`",
        f"- Total rows loaded: {total_rows:,}",
        f"- Total columns loaded, including Datetime: {total_columns:,}",
        f"- Target: `{TARGET}`",
        "",
        "## 2. Filtering Summary",
        "",
        f"- Rows before filtering: {rows_before:,}",
        f"- Rows after `CHL_STA_1 != 0`: {rows_after:,}",
        f"- Percentage retained: {retained_pct:.2f}%",
        f"- Dropped status/control-state columns: {', '.join(STATUS_COLUMNS)}",
        "",
        "## 3. Pearson Top 20",
        "",
        markdown_table(pearson_top20),
        "",
        "## 4. Mutual Information Top 20",
        "",
        f"- {mi_note}",
        "",
        markdown_table(mi_top20),
        "",
        "## 5. Model A Results",
        "",
        "- Purpose: maximum achievable predictive performance using all non-target numeric features except chiller peer power leakage.",
        f"- Features used: {len(model_a_features)}",
        f"- R2: {model_a_metrics['r2']:.6f}",
        f"- RMSE: {model_a_metrics['rmse']:.6f}",
        "- Top 20 feature importances:",
        "",
        markdown_table(model_a_importance.head(20)),
        f"- Prediction plot: `outputs/model_a_prediction.png`",
        "",
        "## 6. Model B Results",
        "",
        "- Purpose: test manually selected engineering Condition Variables.",
        f"- Features used: {', '.join(model_b_features)}",
        f"- R2: {model_b_metrics['r2']:.6f}",
        f"- RMSE: {model_b_metrics['rmse']:.6f}",
        "- Feature importances:",
        "",
        markdown_table(model_b_importance),
        f"- Prediction plot: `outputs/model_b_prediction.png`",
        "",
        "## 7. Model C Results",
        "",
        "- Purpose: compare engineering intuition against data-discovered predictors.",
        f"- Features used: {', '.join(model_c_features)}",
        f"- R2: {model_c_metrics['r2']:.6f}",
        f"- RMSE: {model_c_metrics['rmse']:.6f}",
        "- Feature importances:",
        "",
        markdown_table(model_c_importance),
        f"- Prediction plot: `outputs/model_c_prediction.png`",
        "",
        "## 8. Feature Stability Results",
        "",
        f"- Common seasonal top-10 variables: {len(common_stability)}",
        f"- Common variables: {', '.join(sorted(common_stability)) if common_stability else 'None'}",
        f"- Stability answer: {stable_answer}",
        "- Seasonal drift:",
    ]
    for name, variables in drift.items():
        report_lines.append(f"  - {name}: {', '.join(variables) if variables else 'No drift from common set'}")

    report_lines.extend(
        [
            "",
            "## 9. Feature Classification Summary",
            "",
            markdown_table(pd.DataFrame({"group": group_summary.keys(), "count": group_summary.values()})),
            "",
            f"- Full classification: `outputs/feature_groups.md`",
            f"- Stability detail: `outputs/feature_stability.md`",
            f"- Correlation heatmap: `outputs/feature_audit_correlation_plot.png`",
            "",
            "## 10. Interpretation",
            "",
            f"**Q1: Can Condition Variables alone predict `{TARGET}`?**",
            "",
            f"Model B R2 is {model_b_metrics['r2']:.6f}. {condition_answer}",
            "",
            "**Q2: How much performance is lost compared to All Features?**",
            "",
            (
                f"Model A R2 is {model_a_metrics['r2']:.6f}; Model B R2 is "
                f"{model_b_metrics['r2']:.6f}. Absolute R2 loss is {performance_loss:.6f}. "
                f"Model B RMSE is {relative_rmse:.2f}x Model A RMSE."
            ),
            "",
            "**Q3: Does engineering intuition agree with data-driven discovery?**",
            "",
            (
                f"Model C R2 is {model_c_metrics['r2']:.6f}, compared with Model B R2 "
                f"{model_b_metrics['r2']:.6f}. {discovery_answer}"
            ),
            "",
            "**Q4: Are discovered relationships stable throughout the year?**",
            "",
            stable_answer,
            "",
            "**Q5: Is the Expected State -> Residual route viable?**",
            "",
            viable_answer,
        ]
    )

    (OUTPUT_DIR / "feature_audit.md").write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'feature_audit.md'}")


if __name__ == "__main__":
    main()
