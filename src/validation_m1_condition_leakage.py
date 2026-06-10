from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESIDUAL_PATH = ROOT / "outputs" / "residuals_normal.csv"
HI_STATS_PATH = ROOT / "outputs" / "hi_v0" / "hi_v0_severity_stats.csv"
BASELINE_PATH = ROOT / "data" / "lbnl" / "ChillerPlant.csv"
REPORT_PATH = ROOT / "outputs" / "validation_m1_condition_leakage.md"

FIG_RESIDUAL_CORR = ROOT / "outputs" / "validation_m1_residual_condition_corr.png"
FIG_HI_CORR = ROOT / "outputs" / "validation_m1_hi_condition_corr.png"
FIG_SEASONAL = ROOT / "outputs" / "validation_m1_seasonal_comparison.png"
FIG_R2 = ROOT / "outputs" / "validation_m1_r2_summary.png"

CONDITION_VARIABLES = [
    "CWL_SEC_LOAD",
    "OA_TEMP",
    "OA_TEMP_WB",
    "CWL_PRI_SW_TEMPSPT",
    "CT_SW_TEMPSPT",
    "CWL_SEC_DPSPT",
]

HI_TARGET = "CT_SW_TEMP_1"
HI_WINDOW = "6h"
HI_WINDOW_ROWS = 360


def residual_rms(frame: pd.DataFrame) -> pd.Series:
    cols = [c for c in frame.columns if c.endswith("_residual_norm")]
    return np.sqrt(np.square(frame[cols]).mean(axis=1))


def fmt(value: object, digits: int = 4) -> str:
    if pd.isna(value):
        return "N/A"
    return f"{float(value):.{digits}g}"


def corr_table(data: pd.DataFrame, target: str, variables: list[str], window: str) -> pd.DataFrame:
    rows = []
    for var in variables:
        pair = data[[target, var]].dropna()
        rows.append(
            {
                "Window": window,
                "Target": target,
                "Condition": var,
                "Spearman": pair[target].corr(pair[var], method="spearman"),
                "Pearson": pair[target].corr(pair[var], method="pearson"),
            }
        )
    out = pd.DataFrame(rows)
    out["AbsSpearman"] = out["Spearman"].abs()
    return out.sort_values("AbsSpearman", ascending=False).reset_index(drop=True)


def fit_explanatory_model(data: pd.DataFrame, target: str, variables: list[str]) -> tuple[dict[str, float], pd.DataFrame]:
    frame = data[[target] + variables].dropna()
    x = frame[variables]
    y = frame[target]

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    linear = LinearRegression()
    linear.fit(x_scaled, y)
    y_pred_linear = linear.predict(x_scaled)
    linear_r2 = r2_score(y, y_pred_linear)
    linear_importance = pd.DataFrame(
        {
            "Target": target,
            "Model": "LinearRegression",
            "Condition": variables,
            "Importance": np.abs(linear.coef_),
        }
    ).sort_values("Importance", ascending=False)

    rf = RandomForestRegressor(
        n_estimators=100,
        max_depth=6,
        random_state=42,
        n_jobs=-1,
    )
    rf.fit(x, y)
    y_pred_rf = rf.predict(x)
    rf_r2 = r2_score(y, y_pred_rf)
    rf_importance = pd.DataFrame(
        {
            "Target": target,
            "Model": "RandomForestRegressor",
            "Condition": variables,
            "Importance": rf.feature_importances_,
        }
    ).sort_values("Importance", ascending=False)

    r2 = {
        "LinearRegression": linear_r2,
        "RandomForestRegressor": rf_r2,
    }
    importance = pd.concat([linear_importance, rf_importance], ignore_index=True)
    return r2, importance


def split_windows(data: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    bounds = np.linspace(0, len(data), 4, dtype=int)
    return [
        (f"Window {idx + 1}", data.iloc[bounds[idx] : bounds[idx + 1]].copy())
        for idx in range(3)
    ]


def seasonal_stability(corrs: pd.DataFrame, target: str) -> pd.DataFrame:
    target_corrs = corrs[corrs["Target"].eq(target)].copy()
    pivot = target_corrs.pivot(index="Condition", columns="Window", values="Spearman")
    rows = []
    for condition, row in pivot.iterrows():
        values = row.dropna()
        signs = np.sign(values)
        sign_reversal = len(set(signs)) > 1
        magnitude_range = values.abs().max() - values.abs().min()
        rows.append(
            {
                "Target": target,
                "Condition": condition,
                "Window1": row.get("Window 1", np.nan),
                "Window2": row.get("Window 2", np.nan),
                "Window3": row.get("Window 3", np.nan),
                "SignReversal": sign_reversal,
                "MagnitudeRange": magnitude_range,
            }
        )
    return pd.DataFrame(rows).sort_values("MagnitudeRange", ascending=False)


def taxonomy_assessment(corr_full: pd.DataFrame, seasonal: pd.DataFrame, r2_summary: pd.DataFrame) -> dict[str, str]:
    max_spearman = corr_full["AbsSpearman"].max()
    max_rf_r2 = r2_summary["RandomForestRegressor"].max()
    sign_reversals = seasonal["SignReversal"].any()
    large_seasonal_shift = (seasonal["MagnitudeRange"] > 0.4).any()

    return {
        "Type A": (
            "Supported. Condition variables are already present, yet condition variables explain "
            f"substantial variance (max RF R2={fmt(max_rf_r2)}) and residual/HI correlations remain."
            if max_spearman >= 0.5 or max_rf_r2 >= 0.3
            else "Not strongly supported by this audit."
        ),
        "Type B": (
            "Plausible. Existing HVAC-v1 condition variables do not fully remove seasonal residual structure, "
            "suggesting important seasonal drivers may be missing or insufficiently represented."
            if large_seasonal_shift
            else "Not strongly supported by this audit."
        ),
        "Type C": (
            "Supported. Correlations differ strongly between seasonal windows, including sign reversals or large magnitude shifts."
            if sign_reversals or large_seasonal_shift
            else "Not strongly supported by this audit."
        ),
        "Type D": (
            "Not primary. Condition variables explain meaningful variance, so the observed issue is more directly condition dependence than a residual definition problem alone."
            if max_rf_r2 >= 0.3
            else "Plausible. Condition variables explain little variance while residual/HI structure remains."
        ),
    }


def save_figures(full_corr: pd.DataFrame, seasonal: pd.DataFrame, r2_summary: pd.DataFrame) -> None:
    def heatmap_for(target: str, path: Path, title: str) -> None:
        frame = full_corr[full_corr["Target"].eq(target)].set_index("Condition")[["Spearman", "Pearson"]]
        fig, ax = plt.subplots(figsize=(7, 4))
        im = ax.imshow(frame.values, vmin=-1, vmax=1, cmap="coolwarm", aspect="auto")
        ax.set_xticks(np.arange(frame.shape[1]))
        ax.set_xticklabels(frame.columns)
        ax.set_yticks(np.arange(frame.shape[0]))
        ax.set_yticklabels(frame.index)
        ax.set_title(title)
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                ax.text(j, i, f"{frame.values[i, j]:.2f}", ha="center", va="center", color="black")
        fig.colorbar(im, ax=ax, label="Correlation")
        fig.tight_layout()
        fig.savefig(path, dpi=160)
        plt.close(fig)

    heatmap_for("Residual_RMS", FIG_RESIDUAL_CORR, "Residual RMS vs HVAC-v1 Conditions")
    heatmap_for("HI_v0", FIG_HI_CORR, "HI_v0 vs HVAC-v1 Conditions")

    fig, ax = plt.subplots(figsize=(10, 5))
    for target in ["Residual_RMS", "HI_v0"]:
        sub = seasonal[seasonal["Target"].eq(target)]
        top_conditions = sub.sort_values("MagnitudeRange", ascending=False).head(3)["Condition"]
        for condition in top_conditions:
            row = sub[sub["Condition"].eq(condition)].iloc[0]
            ax.plot(
                ["Window 1", "Window 2", "Window 3"],
                [row["Window1"], row["Window2"], row["Window3"]],
                marker="o",
                label=f"{target}: {condition}",
            )
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel("Spearman correlation")
    ax.set_title("Seasonal Window Correlation Comparison")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG_SEASONAL, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(len(r2_summary))
    width = 0.35
    ax.bar(x - width / 2, r2_summary["LinearRegression"], width, label="Linear")
    ax.bar(x + width / 2, r2_summary["RandomForestRegressor"], width, label="Random Forest")
    ax.set_xticks(x)
    ax.set_xticklabels(r2_summary["Target"])
    ax.set_ylabel("R2")
    ax.set_title("Condition Variables Explain Residual/HI Variance")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_R2, dpi=160)
    plt.close(fig)


def main() -> None:
    residuals = pd.read_csv(RESIDUAL_PATH, parse_dates=["Datetime"]).set_index("Datetime").sort_index()
    hi_stats = pd.read_csv(HI_STATS_PATH)
    baseline_hi_stats = hi_stats[hi_stats["Dataset"].eq("Baseline")]

    conditions = pd.read_csv(
        BASELINE_PATH,
        usecols=["Datetime"] + CONDITION_VARIABLES,
        parse_dates=["Datetime"],
    ).set_index("Datetime").sort_index()

    data = residuals.join(conditions, how="inner")
    data["Residual_RMS"] = residual_rms(data)
    data["HI_v0"] = np.sqrt(
        data[f"{HI_TARGET}_residual_norm"].pow(2).rolling(HI_WINDOW_ROWS, min_periods=HI_WINDOW_ROWS // 2).mean()
    )
    data = data.dropna(subset=["Residual_RMS", "HI_v0"] + CONDITION_VARIABLES)

    full_corr = pd.concat(
        [
            corr_table(data, "Residual_RMS", CONDITION_VARIABLES, "Full"),
            corr_table(data, "HI_v0", CONDITION_VARIABLES, "Full"),
        ],
        ignore_index=True,
    )

    window_corrs = []
    for name, window in split_windows(data):
        window_corrs.append(corr_table(window, "Residual_RMS", CONDITION_VARIABLES, name))
        window_corrs.append(corr_table(window, "HI_v0", CONDITION_VARIABLES, name))
    window_corr = pd.concat(window_corrs, ignore_index=True)

    r2_rows = []
    importances = []
    for target in ["Residual_RMS", "HI_v0"]:
        r2, importance = fit_explanatory_model(data, target, CONDITION_VARIABLES)
        r2_rows.append({"Target": target, **r2})
        importances.append(importance)
    r2_summary = pd.DataFrame(r2_rows)
    importance_table = pd.concat(importances, ignore_index=True)

    seasonal = pd.concat(
        [
            seasonal_stability(window_corr, "Residual_RMS"),
            seasonal_stability(window_corr, "HI_v0"),
        ],
        ignore_index=True,
    )

    taxonomy = taxonomy_assessment(full_corr, seasonal, r2_summary)
    save_figures(full_corr, seasonal, r2_summary)

    verdict = "FAIL" if (full_corr["AbsSpearman"].max() >= 0.5 or r2_summary["RandomForestRegressor"].max() >= 0.3) else "PASS"

    lines = []
    lines.append("# Validation M-1 Condition Leakage Audit")
    lines.append("")
    lines.append("## 1. Protocol Reference")
    lines.append("")
    lines.append("Protocol: `docs/review/m1_condition_leakage_protocol_v0.1.md`")
    lines.append("")
    lines.append("No retraining was performed.")
    lines.append("")
    lines.append("No new datasets were introduced.")
    lines.append("")
    lines.append("No fault data was loaded.")
    lines.append("")
    lines.append("No remediation was performed.")
    lines.append("")
    lines.append("## 2. Frozen Artifact Sources")
    lines.append("")
    lines.append(f"* Residual source: `{RESIDUAL_PATH.relative_to(ROOT)}`")
    lines.append(f"* HI aggregate source: `{HI_STATS_PATH.relative_to(ROOT)}`")
    lines.append(f"* Baseline condition source: `{BASELINE_PATH.relative_to(ROOT)}`")
    lines.append("")
    lines.append("HVAC-v1 condition variables used:")
    lines.append("")
    for var in CONDITION_VARIABLES:
        lines.append(f"* `{var}`")
    lines.append("")
    lines.append(
        "HI_v0 was derived from frozen normalized residuals using the existing HI_v0 Rolling RMS definition "
        f"for `{HI_TARGET}`, window `{HI_WINDOW}`. This did not recompute residuals or retrain models."
    )
    selected = baseline_hi_stats[
        baseline_hi_stats["Target"].eq(HI_TARGET) & baseline_hi_stats["Window"].eq(HI_WINDOW)
    ]
    if not selected.empty:
        row = selected.iloc[0]
        lines.append("")
        lines.append(
            f"Baseline HI stats reference row: HI_mean={fmt(row['HI_mean'])}, "
            f"HI_p95={fmt(row['HI_p95'])}, HI_p99={fmt(row['HI_p99'])}."
        )
    lines.append("")
    lines.append(f"Aligned rows analyzed: {len(data):,}")
    lines.append("")
    lines.append("## 3. Full-Period Correlations")
    lines.append("")
    for target in ["Residual_RMS", "HI_v0"]:
        lines.append(f"### {target}")
        lines.append("")
        lines.append("| Rank | Condition | Spearman | Pearson |")
        lines.append("|---:|---|---:|---:|")
        sub = full_corr[full_corr["Target"].eq(target)].reset_index(drop=True)
        for idx, row in sub.iterrows():
            lines.append(
                f"| {idx + 1} | {row['Condition']} | {fmt(row['Spearman'])} | {fmt(row['Pearson'])} |"
            )
        lines.append("")
    lines.append("## 4. Variance Explanation Results")
    lines.append("")
    lines.append("| Target | Linear R2 | Random Forest R2 |")
    lines.append("|---|---:|---:|")
    for _, row in r2_summary.iterrows():
        lines.append(
            f"| {row['Target']} | {fmt(row['LinearRegression'])} | {fmt(row['RandomForestRegressor'])} |"
        )
    lines.append("")
    lines.append("### Feature Importance")
    lines.append("")
    lines.append("| Target | Model | Rank | Condition | Importance |")
    lines.append("|---|---|---:|---|---:|")
    for (target, model), group in importance_table.groupby(["Target", "Model"], sort=False):
        for idx, row in group.reset_index(drop=True).iterrows():
            lines.append(
                f"| {target} | {model} | {idx + 1} | {row['Condition']} | {fmt(row['Importance'])} |"
            )
    lines.append("")
    lines.append("## 5. Seasonal Stability Results")
    lines.append("")
    lines.append("| Target | Condition | Window 1 | Window 2 | Window 3 | Sign Reversal | Magnitude Range |")
    lines.append("|---|---|---:|---:|---:|---|---:|")
    for _, row in seasonal.iterrows():
        lines.append(
            f"| {row['Target']} | {row['Condition']} | {fmt(row['Window1'])} | "
            f"{fmt(row['Window2'])} | {fmt(row['Window3'])} | {row['SignReversal']} | "
            f"{fmt(row['MagnitudeRange'])} |"
        )
    lines.append("")
    lines.append("Seasonal asymmetry is present when correlations differ strongly between windows.")
    lines.append("")
    lines.append("## 6. Leakage Taxonomy Assessment")
    lines.append("")
    for label in ["Type A", "Type B", "Type C", "Type D"]:
        lines.append(f"### {label}")
        lines.append("")
        lines.append(taxonomy[label])
        lines.append("")
    lines.append("Multiple leakage types may coexist. No single label was forced.")
    lines.append("")
    lines.append("## 7. Verdict")
    lines.append("")
    lines.append(verdict)
    lines.append("")
    if verdict == "FAIL":
        lines.append("Strong condition dependence remains.")
        lines.append("")
        lines.append("Leakage type can be identified.")
        lines.append("")
        lines.append("Residual construct validity requires revision.")
    else:
        lines.append("Residual and HI show weak dependence on condition variables.")
        lines.append("")
        lines.append("Condition information explains little variance.")
    lines.append("")
    lines.append("## 8. Implications")
    lines.append("")
    if verdict == "FAIL":
        lines.append("Failure does NOT invalidate the project.")
        lines.append("")
        lines.append("Failure indicates:")
        lines.append("")
        lines.append("Expected State → Residual")
        lines.append("")
        lines.append("requires further study.")
        lines.append("")
        lines.append("Forward validation remains suspended.")
        lines.append("")
        lines.append("Validation D remains blocked.")
        lines.append("")
        lines.append("No specific remediation path is assumed.")
        lines.append("")
        lines.append("Leakage taxonomy should guide future investigation.")
    else:
        lines.append("Residual construct validity survives this audit.")
    lines.append("")
    lines.append("## 9. Visualizations")
    lines.append("")
    lines.append(f"* `{FIG_RESIDUAL_CORR.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_HI_CORR.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_SEASONAL.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_R2.relative_to(ROOT)}`")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT_PATH)
    print(f"Verdict: {verdict}")


if __name__ == "__main__":
    main()
