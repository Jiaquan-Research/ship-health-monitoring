from __future__ import annotations

import io
import math
import zipfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


ROOT = Path(__file__).resolve().parents[1]
NASA_ZIP = ROOT / "data" / "battery" / "nasa_li_ion" / "5_Battery_Data_Set.zip"
OXFORD_MAT = ROOT / "data" / "battery" / "oxford" / "Oxford_Battery_Degradation_Dataset_1.mat"
OUT = ROOT / "outputs" / "exploratory_e2_battery_cross_regime_probe.md"


@dataclass(frozen=True)
class Regime:
    dataset: str
    name: str
    frame: pd.DataFrame
    feature_cols: tuple[str, ...]
    target_col: str = "voltage"


def as_1d(value) -> np.ndarray:
    arr = np.asarray(value).astype(float).reshape(-1)
    return arr


def finite_frame(data: dict[str, np.ndarray]) -> pd.DataFrame:
    n = min(len(v) for v in data.values())
    trimmed = {k: np.asarray(v[:n], dtype=float) for k, v in data.items()}
    df = pd.DataFrame(trimmed)
    return df.replace([np.inf, -np.inf], np.nan).dropna()


def cap_rows(df: pd.DataFrame, max_rows: int = 50_000) -> pd.DataFrame:
    if len(df) <= max_rows:
        return df.reset_index(drop=True)
    idx = np.linspace(0, len(df) - 1, max_rows).astype(int)
    return df.iloc[idx].reset_index(drop=True)


def load_nasa_regimes() -> list[Regime]:
    selected = {
        "NASA_room_24C_square_4A": (
            "5. Battery Data Set/2. BatteryAgingARC_25_26_27_28_P1.zip",
            ["B0025.mat", "B0026.mat", "B0027.mat", "B0028.mat"],
        ),
        "NASA_cold_4C_fixed_2A": (
            "5. Battery Data Set/5. BatteryAgingARC_49_50_51_52.zip",
            ["B0049.mat", "B0050.mat", "B0051.mat", "B0052.mat"],
        ),
    }
    regimes: list[Regime] = []
    with zipfile.ZipFile(NASA_ZIP) as outer:
        for regime_name, (inner_name, mats) in selected.items():
            rows = []
            with zipfile.ZipFile(io.BytesIO(outer.read(inner_name))) as inner:
                for mat_name in mats:
                    mat = sio.loadmat(io.BytesIO(inner.read(mat_name)), squeeze_me=True, struct_as_record=False)
                    battery_key = next(k for k in mat if not k.startswith("__"))
                    battery = mat[battery_key]
                    cycles = np.atleast_1d(battery.cycle)
                    for cycle in cycles:
                        if str(cycle.type) != "discharge":
                            continue
                        data = cycle.data
                        rows.append(
                            finite_frame(
                                {
                                    "time": as_1d(data.Time),
                                    "current": as_1d(data.Current_measured),
                                    "temperature": as_1d(data.Temperature_measured),
                                    "voltage": as_1d(data.Voltage_measured),
                                }
                            )
                        )
            frame = cap_rows(pd.concat(rows, ignore_index=True))
            regimes.append(Regime("NASA Battery", regime_name, frame, ("time", "current", "temperature")))
    return regimes


def load_oxford_regimes() -> list[Regime]:
    mat = sio.loadmat(OXFORD_MAT, squeeze_me=True, struct_as_record=False)
    branch_map = {
        "Oxford_C1_discharge": "C1dc",
        "Oxford_OCV_discharge": "OCVdc",
    }
    by_branch: dict[str, list[pd.DataFrame]] = {name: [] for name in branch_map}
    for cell_name in sorted(k for k in mat if k.startswith("Cell")):
        cell = mat[cell_name]
        cycle_names = sorted(a for a in dir(cell) if a.startswith("cyc"))
        for cycle_name in cycle_names:
            cycle = getattr(cell, cycle_name)
            for regime_name, branch_name in branch_map.items():
                branch = getattr(cycle, branch_name)
                by_branch[regime_name].append(
                    finite_frame(
                        {
                            "time": as_1d(branch.t),
                            "charge": as_1d(branch.q),
                            "temperature": as_1d(branch.T),
                            "voltage": as_1d(branch.v),
                        }
                    )
                )
    regimes: list[Regime] = []
    for regime_name, frames in by_branch.items():
        frame = cap_rows(pd.concat(frames, ignore_index=True))
        regimes.append(Regime("Oxford Battery", regime_name, frame, ("time", "charge", "temperature")))
    return regimes


def evaluate(train: Regime, test: Regime) -> dict[str, object]:
    train_df = train.frame
    test_df = test.frame
    feature_cols = list(train.feature_cols)
    model = LinearRegression()
    model.fit(train_df[feature_cols], train_df[train.target_col])
    pred = model.predict(test_df[feature_cols])
    y = test_df[test.target_col].to_numpy()
    rho = spearmanr(y, pred).statistic
    if math.isnan(rho):
        rho = float("nan")
    return {
        "Dataset": train.dataset,
        "Train_Regime": train.name,
        "Test_Regime": test.name,
        "Comparison": "same-window" if train.name == test.name else "cross-window",
        "Train_Rows": len(train_df),
        "Test_Rows": len(test_df),
        "R2": r2_score(y, pred),
        "RMSE": math.sqrt(mean_squared_error(y, pred)),
        "Spearman": rho,
    }


def format_float(x: float) -> str:
    if isinstance(x, float) and math.isnan(x):
        return "nan"
    return f"{x:.4f}"


def markdown_table(df: pd.DataFrame) -> str:
    shown = df.copy()
    for col in ["R2", "RMSE", "Spearman"]:
        shown[col] = shown[col].map(format_float)
    cols = list(shown.columns)
    rows = [[str(row[col]) for col in cols] for _, row in shown.iterrows()]
    widths = [len(col) for col in cols]
    for row in rows:
        widths = [max(w, len(cell)) for w, cell in zip(widths, row)]
    header = "| " + " | ".join(col.ljust(widths[i]) for i, col in enumerate(cols)) + " |"
    sep = "| " + " | ".join("-" * widths[i] for i in range(len(cols))) + " |"
    body = ["| " + " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)) + " |" for row in rows]
    return "\n".join([header, sep] + body)


def verdict(metrics: pd.DataFrame) -> str:
    cross = metrics[metrics["Comparison"] == "cross-window"]
    if cross.empty:
        return "Inconclusive."
    if (cross["R2"] < 0).any():
        return "Collapse observed."
    if (cross["R2"] < 0.5).any():
        return "Mild degradation observed."
    return "No obvious instability observed."


def main() -> None:
    regimes = load_nasa_regimes() + load_oxford_regimes()
    rows = []
    for dataset in sorted(set(r.dataset for r in regimes)):
        subset = [r for r in regimes if r.dataset == dataset]
        for train in subset:
            for test in subset:
                rows.append(evaluate(train, test))
    metrics = pd.DataFrame(rows)
    final_verdict = verdict(metrics)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Exploratory E-2 Battery Cross-Regime Probe",
        "",
        "Status: Observation only.",
        "",
        "This is NOT validation.",
        "",
        "This is NOT evidence generation.",
        "",
        "This does NOT support Q0.",
        "",
        "---",
        "",
        "## Protocol Reference",
        "",
        "`docs/exploration/e2_battery_cross_regime_probe_v0.1.md`",
        "",
        "---",
        "",
        "## Datasets",
        "",
        "- NASA Battery Dataset",
        "- Oxford Battery Dataset",
        "",
        "Only already-downloaded files were used.",
        "",
        "---",
        "",
        "## Method",
        "",
        "Simple same-window and cross-window evaluation.",
        "",
        "Model:",
        "",
        "Linear regression.",
        "",
        "NASA raw inputs:",
        "",
        "- time",
        "- measured current",
        "- measured temperature",
        "",
        "Oxford raw inputs:",
        "",
        "- time",
        "- charge",
        "- temperature",
        "",
        "Target:",
        "",
        "Voltage.",
        "",
        "No PCA, clustering, UMAP, HDBSCAN, Koopman, SINDy, MoE, Transformer, Autoencoder, or deep learning was used.",
        "",
        "---",
        "",
        "## Regime Windows",
        "",
        "| Dataset | Regime | Rows Used |",
        "|---|---|---:|",
    ]
    for r in regimes:
        lines.append(f"| {r.dataset} | {r.name} | {len(r.frame)} |")
    lines += [
        "",
        "---",
        "",
        "## Key Metrics",
        "",
        markdown_table(metrics),
        "",
        "---",
        "",
        "## Verdict",
        "",
        final_verdict,
        "",
        "---",
        "",
        "## Output Restrictions",
        "",
        "No conclusion is implied.",
        "",
        "No support for Q0 is implied.",
        "",
        "No claim upgrade is implied.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("Key Metrics")
    print(markdown_table(metrics))
    print()
    print("Verdict")
    print(final_verdict)


if __name__ == "__main__":
    main()
