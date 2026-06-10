from pathlib import Path
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.metrics import r2_score


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "data" / "lbnl" / "ChillerPlant.csv"
RESIDUAL_PATH = ROOT / "outputs" / "residuals_normal.csv"
REPORT_PATH = ROOT / "outputs" / "validation_m1a_type_separation.md"

FIG_CAPACITY = ROOT / "outputs" / "validation_m1a_model_capacity.png"
FIG_TRANSFER = ROOT / "outputs" / "validation_m1a_cross_season_transfer.png"
FIG_SEASONAL = ROOT / "outputs" / "validation_m1a_seasonal_summary.png"
FIG_INVENTORY = ROOT / "outputs" / "validation_m1a_missing_variable_inventory.png"

CONDITIONS = [
    "CWL_SEC_LOAD",
    "OA_TEMP",
    "OA_TEMP_WB",
    "CWL_PRI_SW_TEMPSPT",
    "CT_SW_TEMPSPT",
    "CWL_SEC_DPSPT",
]

TARGETS = [
    "CHL_POW_1",
    "CHL_SW_TEMP_1",
    "CT_SW_TEMP_1",
    "CHL_RWCD_TEMP_1",
]

HI_TARGET = "CT_SW_TEMP_1"
HI_WINDOW_ROWS = 360


def fmt(value, digits=4):
    if pd.isna(value):
        return "N/A"
    return f"{float(value):.{digits}g}"


def residual_rms(frame: pd.DataFrame, cols: list[str]) -> pd.Series:
    return np.sqrt(np.square(frame[cols]).mean(axis=1))


def make_hi(series: pd.Series) -> pd.Series:
    return np.sqrt(series.pow(2).rolling(HI_WINDOW_ROWS, min_periods=HI_WINDOW_ROWS // 2).mean())


def condition_corrs(data: pd.DataFrame, signal: str) -> pd.DataFrame:
    rows = []
    for condition in CONDITIONS:
        pair = data[[signal, condition]].dropna()
        rows.append(
            {
                "Signal": signal,
                "Condition": condition,
                "Spearman": pair[signal].corr(pair[condition], method="spearman"),
                "Pearson": pair[signal].corr(pair[condition], method="pearson"),
            }
        )
    out = pd.DataFrame(rows)
    out["AbsSpearman"] = out["Spearman"].abs()
    return out.sort_values("AbsSpearman", ascending=False).reset_index(drop=True)


def condition_explain_r2(data: pd.DataFrame, signal: str) -> float:
    frame = data[[signal] + CONDITIONS].dropna()
    model = RandomForestRegressor(n_estimators=80, max_depth=8, random_state=42, n_jobs=-1)
    model.fit(frame[CONDITIONS], frame[signal])
    return r2_score(frame[signal], model.predict(frame[CONDITIONS]))


def residual_signals_from_predictions(
    data: pd.DataFrame,
    predictions: np.ndarray,
    train_mask: np.ndarray,
    model_name: str,
) -> pd.DataFrame:
    out = pd.DataFrame(index=data.index)
    norm_cols = []
    for idx, target in enumerate(TARGETS):
        residual = data[target].to_numpy() - predictions[:, idx]
        train_std = data.loc[train_mask, target].std()
        col = f"{target}_residual_norm"
        out[col] = residual / train_std
        norm_cols.append(col)
    out["Residual_RMS"] = residual_rms(out, norm_cols)
    out["HI_v0"] = make_hi(out[f"{HI_TARGET}_residual_norm"])
    out["Model"] = model_name
    for condition in CONDITIONS:
        out[condition] = data[condition]
    return out.dropna(subset=["Residual_RMS", "HI_v0"] + CONDITIONS)


def load_data() -> pd.DataFrame:
    residuals = pd.read_csv(RESIDUAL_PATH, parse_dates=["Datetime"]).set_index("Datetime").sort_index()
    baseline_cols = ["Datetime"] + CONDITIONS + TARGETS
    baseline = pd.read_csv(BASELINE_PATH, usecols=baseline_cols, parse_dates=["Datetime"])
    baseline = baseline.set_index("Datetime").sort_index()
    return baseline.join(residuals, how="inner").dropna(subset=CONDITIONS + TARGETS)


def frozen_hvac_signals(data: pd.DataFrame) -> pd.DataFrame:
    out = pd.DataFrame(index=data.index)
    norm_cols = [f"{target}_residual_norm" for target in TARGETS]
    for col in norm_cols:
        out[col] = data[col]
    out["Residual_RMS"] = residual_rms(out, norm_cols)
    out["HI_v0"] = make_hi(out[f"{HI_TARGET}_residual_norm"])
    out["Model"] = "HVAC-v1 Frozen XGBoost"
    for condition in CONDITIONS:
        out[condition] = data[condition]
    return out.dropna(subset=["Residual_RMS", "HI_v0"] + CONDITIONS)


def model_capacity_probe(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_cut = int(len(data) * 0.8)
    train_mask = np.zeros(len(data), dtype=bool)
    train_mask[:train_cut] = True

    x_train = data.iloc[:train_cut][CONDITIONS]
    y_train = data.iloc[:train_cut][TARGETS]
    x_all = data[CONDITIONS]

    model_specs = [
        ("Random Forest diagnostic", RandomForestRegressor(n_estimators=80, max_depth=12, random_state=42, n_jobs=-1)),
        ("Extra Trees diagnostic", ExtraTreesRegressor(n_estimators=80, max_depth=12, random_state=42, n_jobs=-1)),
    ]

    signals = [frozen_hvac_signals(data)]
    for name, model in model_specs:
        model.fit(x_train, y_train)
        preds = model.predict(x_all)
        signals.append(residual_signals_from_predictions(data, preds, train_mask, name))

    rows = []
    corr_tables = []
    for signal_data in signals:
        model_name = signal_data["Model"].iloc[0]
        for signal in ["Residual_RMS", "HI_v0"]:
            corrs = condition_corrs(signal_data, signal)
            corr_tables.append(corrs.assign(Model=model_name))
            rows.append(
                {
                    "Model": model_name,
                    "Signal": signal,
                    "MaxAbsSpearman": corrs["AbsSpearman"].max(),
                    "TopCondition": corrs.iloc[0]["Condition"],
                    "ConditionR2": condition_explain_r2(signal_data, signal),
                }
            )
    return pd.DataFrame(rows), pd.concat(corr_tables, ignore_index=True)


def season_masks(data: pd.DataFrame) -> dict[str, pd.Series]:
    month = data.index.month
    return {
        "Winter": month.isin([1, 2, 12]),
        "Summer": month.isin([6, 7, 8]),
    }


def xgb_model():
    from xgboost import XGBRegressor

    return XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=-1,
    )


def transfer_probe(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    masks = season_masks(data)
    combos = [
        ("Winter", "Winter"),
        ("Summer", "Summer"),
        ("Winter", "Summer"),
        ("Summer", "Winter"),
    ]
    rows = []
    corr_rows = []
    for train_name, test_name in combos:
        train = data.loc[masks[train_name]].copy()
        test = data.loc[masks[test_name]].copy()
        model = xgb_model()
        model.fit(train[CONDITIONS], train[HI_TARGET])
        pred = model.predict(test[CONDITIONS])
        residual = test[HI_TARGET].to_numpy() - pred
        train_std = train[HI_TARGET].std()
        result = test[CONDITIONS].copy()
        result["residual_norm"] = residual / train_std
        result["abs_residual"] = np.abs(result["residual_norm"])
        r2 = r2_score(test[HI_TARGET], pred)
        rows.append(
            {
                "Train": train_name,
                "Test": test_name,
                "RowsTrain": len(train),
                "RowsTest": len(test),
                "R2": r2,
                "ResidualMean": result["residual_norm"].mean(),
                "ResidualStd": result["residual_norm"].std(),
                "ResidualRMS": np.sqrt(np.square(result["residual_norm"]).mean()),
                "AbsResidualMean": result["abs_residual"].mean(),
            }
        )
        corrs = condition_corrs(result.rename(columns={"abs_residual": "AbsResidual"}), "AbsResidual")
        for _, row in corrs.iterrows():
            corr_rows.append(
                {
                    "Train": train_name,
                    "Test": test_name,
                    "Condition": row["Condition"],
                    "Spearman": row["Spearman"],
                    "Pearson": row["Pearson"],
                }
            )
    return pd.DataFrame(rows), pd.DataFrame(corr_rows)


def missing_variable_inventory(data: pd.DataFrame) -> pd.DataFrame:
    columns = pd.read_csv(BASELINE_PATH, nrows=1).columns.tolist()
    lowered = {col.lower(): col for col in columns}
    checks = [
        ("humidity", ["humid", "rh", "relative_humidity"]),
        ("wet-bulb temperature", ["wb", "wet"]),
        ("solar radiation", ["solar", "rad", "irradiance"]),
        ("time features", ["hour", "month", "dayofyear", "season"]),
        ("other outdoor air variables", ["oa_"]),
        ("load variables", ["load"]),
        ("setpoint variables", ["spt", "setpoint"]),
    ]
    rows = []
    for category, tokens in checks:
        matches = [col for col in columns if any(token in col.lower() for token in tokens)]
        rows.append(
            {
                "CandidateCategory": category,
                "PresentInRawData": bool(matches),
                "MatchingColumns": ", ".join(matches[:20]) if matches else "None found",
                "InHVACv1": ", ".join([col for col in matches if col in CONDITIONS]) or "None",
            }
        )
    return pd.DataFrame(rows)


def evidence_ranking(capacity: pd.DataFrame, transfer: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    reductions = []
    for signal in ["Residual_RMS", "HI_v0"]:
        hvac_r2 = capacity[
            capacity["Model"].eq("HVAC-v1 Frozen XGBoost") & capacity["Signal"].eq(signal)
        ]["ConditionR2"].iloc[0]
        diagnostic_r2 = capacity[
            ~capacity["Model"].eq("HVAC-v1 Frozen XGBoost") & capacity["Signal"].eq(signal)
        ]["ConditionR2"].min()
        reductions.append((signal, hvac_r2 - diagnostic_r2, hvac_r2, diagnostic_r2))
    best_reduction = max(item[1] for item in reductions)
    reduction_text = "; ".join(
        f"{signal}: HVAC-v1 R2={fmt(hvac_r2)}, best diagnostic R2={fmt(diag_r2)}, reduction={fmt(reduction)}"
        for signal, reduction, hvac_r2, diag_r2 in reductions
    )

    same = transfer[transfer["Train"].eq(transfer["Test"])]["R2"].mean()
    cross = transfer[~transfer["Train"].eq(transfer["Test"])]["R2"].mean()
    transfer_gap = same - cross

    missing_major = inventory[
        inventory["CandidateCategory"].isin(["humidity", "solar radiation", "time features"])
        & inventory["InHVACv1"].eq("None")
    ]

    rows = []
    rows.append(
        {
            "Type": "Type A",
            "EvidenceStrength": "Weak" if best_reduction > 0.1 else "Not supported",
            "Basis": (
                f"Signal-wise diagnostic condition R2 comparison: {reduction_text}. "
                "Higher capacity does not substantially reduce leakage if this value is small."
            ),
        }
    )
    rows.append(
        {
            "Type": "Type C",
            "EvidenceStrength": "Strong" if transfer_gap > 0.5 else ("Moderate" if transfer_gap > 0.2 else "Weak"),
            "Basis": f"Mean same-season R2={fmt(same)}, mean cross-season R2={fmt(cross)}, gap={fmt(transfer_gap)}.",
        }
    )
    rows.append(
        {
            "Type": "Type B",
            "EvidenceStrength": "Moderate" if len(missing_major) else "Weak",
            "Basis": (
                "Potentially relevant categories absent from HVAC-v1: "
                + ", ".join(missing_major["CandidateCategory"].tolist())
                if len(missing_major)
                else "No major missing category was clearly identified by name inventory."
            ),
        }
    )
    return pd.DataFrame(rows)


def save_figures(capacity: pd.DataFrame, transfer: pd.DataFrame, inventory: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = capacity["Model"] + "\n" + capacity["Signal"]
    x = np.arange(len(capacity))
    ax.bar(x, capacity["ConditionR2"], color="#4c78a8")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right")
    ax.set_ylabel("Condition explanatory R2")
    ax.set_title("M-1A.1 Model-Capacity Leakage Comparison")
    fig.tight_layout()
    fig.savefig(FIG_CAPACITY, dpi=160)
    plt.close(fig)

    matrix = transfer.pivot(index="Train", columns="Test", values="R2").loc[["Winter", "Summer"], ["Winter", "Summer"]]
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(matrix.values, cmap="viridis", vmin=min(0, np.nanmin(matrix.values)), vmax=max(1, np.nanmax(matrix.values)))
    ax.set_xticks(np.arange(matrix.shape[1]))
    ax.set_xticklabels(matrix.columns)
    ax.set_yticks(np.arange(matrix.shape[0]))
    ax.set_yticklabels(matrix.index)
    ax.set_xlabel("Test season")
    ax.set_ylabel("Train season")
    ax.set_title("M-1A.2 Cross-Season Transfer R2")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, f"{matrix.values[i, j]:.2f}", ha="center", va="center", color="white")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(FIG_TRANSFER, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4))
    transfer.plot(x="Train", y=["ResidualRMS", "AbsResidualMean"], kind="bar", ax=ax)
    ax.set_title("M-1A.2 Seasonal Residual Summary")
    ax.set_ylabel("Residual statistic")
    fig.tight_layout()
    fig.savefig(FIG_SEASONAL, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4))
    table_data = inventory[["CandidateCategory", "PresentInRawData", "InHVACv1"]].values.tolist()
    ax.axis("off")
    table = ax.table(
        cellText=table_data,
        colLabels=["Category", "Present", "In HVAC-v1"],
        loc="center",
        cellLoc="left",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.5)
    ax.set_title("M-1A.3 Missing Variable Inventory")
    fig.tight_layout()
    fig.savefig(FIG_INVENTORY, dpi=160)
    plt.close(fig)


def main() -> None:
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    data = load_data()
    capacity, capacity_corrs = model_capacity_probe(data)
    transfer, transfer_corrs = transfer_probe(data)
    inventory = missing_variable_inventory(data)
    ranking = evidence_ranking(capacity, transfer, inventory)
    save_figures(capacity, transfer, inventory)

    lines = []
    lines.append("# Validation M-1A Type Separation")
    lines.append("")
    lines.append("## 1. Protocol Reference")
    lines.append("")
    lines.append("Protocol: `docs/review/m1a_type_separation_protocol_v0.1.md`")
    lines.append("")
    lines.append("Diagnosis only.")
    lines.append("")
    lines.append("No remediation was performed.")
    lines.append("")
    lines.append("No new datasets were introduced.")
    lines.append("")
    lines.append("No algorithm replacement is implied.")
    lines.append("")
    lines.append("## 2. M-1A.1 Results")
    lines.append("")
    lines.append("Model Capacity Probe targeting Type A.")
    lines.append("")
    lines.append("| Model | Signal | Max Abs Spearman | Top Condition | Condition R2 |")
    lines.append("|---|---|---:|---|---:|")
    for _, row in capacity.iterrows():
        lines.append(
            f"| {row['Model']} | {row['Signal']} | {fmt(row['MaxAbsSpearman'])} | "
            f"{row['TopCondition']} | {fmt(row['ConditionR2'])} |"
        )
    lines.append("")
    lines.append("Detailed condition correlations:")
    lines.append("")
    lines.append("| Model | Signal | Condition | Spearman | Pearson |")
    lines.append("|---|---|---|---:|---:|")
    for _, row in capacity_corrs.iterrows():
        lines.append(
            f"| {row['Model']} | {row['Signal']} | {row['Condition']} | "
            f"{fmt(row['Spearman'])} | {fmt(row['Pearson'])} |"
        )
    lines.append("")
    lines.append("## 3. M-1A.2 Results")
    lines.append("")
    lines.append("Cross-season Transfer Probe targeting Type C.")
    lines.append("")
    lines.append("| Train | Test | Train Rows | Test Rows | R2 | Residual Mean | Residual Std | Residual RMS | Abs Residual Mean |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for _, row in transfer.iterrows():
        lines.append(
            f"| {row['Train']} | {row['Test']} | {int(row['RowsTrain']):,} | {int(row['RowsTest']):,} | "
            f"{fmt(row['R2'])} | {fmt(row['ResidualMean'])} | {fmt(row['ResidualStd'])} | "
            f"{fmt(row['ResidualRMS'])} | {fmt(row['AbsResidualMean'])} |"
        )
    lines.append("")
    lines.append("Correlation structure for cross-season residual magnitude:")
    lines.append("")
    lines.append("| Train | Test | Condition | Spearman | Pearson |")
    lines.append("|---|---|---|---:|---:|")
    for _, row in transfer_corrs.iterrows():
        lines.append(
            f"| {row['Train']} | {row['Test']} | {row['Condition']} | "
            f"{fmt(row['Spearman'])} | {fmt(row['Pearson'])} |"
        )
    lines.append("")
    lines.append("## 4. M-1A.3 Inventory")
    lines.append("")
    lines.append("Missing Variable Inventory targeting Type B.")
    lines.append("")
    lines.append("| Candidate Category | Present In Raw Data | Matching Columns | In HVAC-v1 |")
    lines.append("|---|---|---|---|")
    for _, row in inventory.iterrows():
        lines.append(
            f"| {row['CandidateCategory']} | {row['PresentInRawData']} | "
            f"{row['MatchingColumns']} | {row['InHVACv1']} |"
        )
    lines.append("")
    lines.append("## 5. Evidence Ranking")
    lines.append("")
    lines.append("| Type | Evidence Strength | Basis |")
    lines.append("|---|---|---|")
    for _, row in ranking.iterrows():
        lines.append(f"| {row['Type']} | {row['EvidenceStrength']} | {row['Basis']} |")
    lines.append("")
    lines.append("## 6. Dominance Assessment")
    lines.append("")
    strength_order = {"Strong": 4, "Moderate": 3, "Weak": 2, "Not supported": 1}
    ranking["Score"] = ranking["EvidenceStrength"].map(strength_order)
    best_score = ranking["Score"].max()
    dominant = ranking[ranking["Score"].eq(best_score)]
    if len(dominant) == 1:
        lines.append(f"Dominant mechanism: {dominant.iloc[0]['Type']}.")
    else:
        lines.append("No single dominant mechanism was forced.")
        lines.append("")
        lines.append("Highest-ranked mechanisms:")
        lines.append("")
        for _, row in dominant.iterrows():
            lines.append(f"* {row['Type']}: {row['EvidenceStrength']}")
    lines.append("")
    lines.append("Multiple mechanisms may coexist.")
    lines.append("")
    lines.append("## 7. Verdict")
    lines.append("")
    lines.append("Diagnosis complete.")
    lines.append("")
    if (ranking["EvidenceStrength"] == "Strong").any() or (ranking["EvidenceStrength"] == "Moderate").any():
        lines.append("Dominant or high-priority leakage mechanisms became clearer.")
    else:
        lines.append("Type A, Type B, and Type C remain inseparable.")
    lines.append("")
    lines.append("## 8. Implications")
    lines.append("")
    lines.append("No remediation path is assumed.")
    lines.append("")
    lines.append("No algorithm changes are implied.")
    lines.append("")
    lines.append("No evidence levels are upgraded.")
    lines.append("")
    lines.append("M-1A is diagnostic only.")
    lines.append("")
    lines.append("## 9. Visualizations")
    lines.append("")
    lines.append(f"* `{FIG_CAPACITY.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_TRANSFER.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_SEASONAL.relative_to(ROOT)}`")
    lines.append(f"* `{FIG_INVENTORY.relative_to(ROOT)}`")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
