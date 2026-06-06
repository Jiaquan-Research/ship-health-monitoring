from __future__ import annotations

from pathlib import Path

import h5py
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "ncmapss" / "data_set"
DS02 = DATA_DIR / "N-CMAPSS_DS02-006.h5"
DS01 = DATA_DIR / "N-CMAPSS_DS01-005.h5"
OUTPUT = ROOT / "outputs" / "ncmapss_c01_label_audit.md"


def decode(values: np.ndarray) -> list[str]:
    return [v.decode("utf-8", errors="replace") if isinstance(v, bytes) else str(v) for v in values]


def load_split(path: Path, split: str) -> tuple[pd.DataFrame, list[str]]:
    with h5py.File(path, "r") as f:
        t = f[f"T_{split}"][:]
        t_var = decode(f["T_var"][:])
        a = f[f"A_{split}"][:]
        a_var = decode(f["A_var"][:])
    t_df = pd.DataFrame(t, columns=t_var)
    a_df = pd.DataFrame(a, columns=a_var)
    t_df["unit"] = a_df["unit"].astype(int)
    t_df["cycle"] = a_df["cycle"].astype(int)
    return t_df, t_var


def global_stats(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    rows = []
    for col in cols:
        series = df[col]
        mean = float(series.mean())
        std = float(series.std(ddof=0))
        rows.append(
            {
                "Column": col,
                "Min": float(series.min()),
                "Max": float(series.max()),
                "Mean": mean,
                "Std": std,
                "All_Zero": bool(std == 0 and mean == 0),
            }
        )
    return pd.DataFrame(rows)


def per_unit_max_abs(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    rows = []
    for unit, part in df.groupby("unit", sort=True):
        row = {"Unit": int(unit)}
        for col in cols:
            max_abs = float(part[col].abs().max())
            row[col] = max_abs
        rows.append(row)
    return pd.DataFrame(rows)


def usable_summary(df: pd.DataFrame, cols: list[str]) -> tuple[pd.DataFrame, list[str], list[str]]:
    rows = []
    usable = []
    zero = []
    for col in cols:
        nonzero_units = []
        col_min = float(df[col].min())
        col_max = float(df[col].max())
        for unit, part in df.groupby("unit", sort=True):
            if float(part[col].std(ddof=0)) > 0.001 or float(part[col].abs().max()) > 0.001:
                nonzero_units.append(str(int(unit)))
        if nonzero_units:
            usable.append(col)
        else:
            zero.append(col)
        rows.append(
            {
                "Column": col,
                "Usable": bool(nonzero_units),
                "Nonzero Units": ", ".join(nonzero_units) if nonzero_units else "None",
                "Min": col_min,
                "Max": col_max,
            }
        )
    return pd.DataFrame(rows), usable, zero


def dev_test_compare(dev_stats: pd.DataFrame, test_stats: pd.DataFrame) -> pd.DataFrame:
    dev = dev_stats.set_index("Column")
    test = test_stats.set_index("Column")
    rows = []
    for col in dev.index:
        rows.append(
            {
                "Column": col,
                "Dev_Std": dev.loc[col, "Std"],
                "Test_Std": test.loc[col, "Std"],
                "Non-zero in Dev": bool(dev.loc[col, "Std"] > 0.001 or max(abs(dev.loc[col, "Min"]), abs(dev.loc[col, "Max"])) > 0.001),
                "Non-zero in Test": bool(test.loc[col, "Std"] > 0.001 or max(abs(test.loc[col, "Min"]), abs(test.loc[col, "Max"])) > 0.001),
            }
        )
    return pd.DataFrame(rows)


def fmt(value: object) -> str:
    if isinstance(value, (float, np.floating)):
        return f"{float(value):.6f}"
    if isinstance(value, bool):
        return "True" if value else "False"
    return str(value)


def markdown_table(df: pd.DataFrame, columns: list[str]) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(fmt(row[col]) for col in columns) + " |")
    return lines


def marked_per_unit_table(df: pd.DataFrame, cols: list[str]) -> list[str]:
    display = df.copy()
    for col in cols:
        display[col] = display[col].map(lambda v: f"{v:.6f}*" if v > 0.001 else f"{v:.6f}")
    return markdown_table(display, ["Unit"] + cols)


def nonzero_columns(stats: pd.DataFrame) -> list[str]:
    rows = []
    for _, row in stats.iterrows():
        if row["Std"] > 0.001 or max(abs(row["Min"]), abs(row["Max"])) > 0.001:
            rows.append(row["Column"])
    return rows


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    ds02_dev, cols = load_split(DS02, "dev")
    ds02_test, _ = load_split(DS02, "test")
    ds01_dev, _ = load_split(DS01, "dev")

    ds02_dev_stats = global_stats(ds02_dev, cols)
    ds02_test_stats = global_stats(ds02_test, cols)
    ds01_dev_stats = global_stats(ds01_dev, cols)
    unit_stats = per_unit_max_abs(ds02_dev, cols)
    usable_df, usable_cols, zero_cols = usable_summary(ds02_dev, cols)
    compare_df = dev_test_compare(ds02_dev_stats, ds02_test_stats)

    ds02_nonzero = nonzero_columns(ds02_dev_stats)
    ds01_nonzero = nonzero_columns(ds01_dev_stats)

    if "HPT_eff_mod" in usable_cols:
        best_col = "HPT_eff_mod"
    elif usable_cols:
        best_col = usable_cols[0]
    else:
        best_col = "None"

    if "HPC_eff_mod" in ds01_nonzero:
        best_file = "N-CMAPSS_DS01-005.h5"
    elif ds01_nonzero:
        best_file = "N-CMAPSS_DS01-005.h5 using " + ds01_nonzero[0]
    else:
        best_file = "No recommendation from DS01/DS02 spot check"

    lines: list[str] = []
    lines.append("# Validation C0.1 — T_dev Label Audit")
    lines.append("")
    lines.append("Read-only audit of N-CMAPSS degradation labels. No model retraining and no residual recomputation were performed.")
    lines.append("")
    lines.append("## 1. Global T_dev Statistics — DS02-006 Dev")
    lines.append("")
    lines.extend(markdown_table(ds02_dev_stats, ["Column", "Min", "Max", "Mean", "Std", "All_Zero"]))
    lines.append("")
    lines.append("## 2. Per-unit T_dev Max Absolute Values — DS02-006 Dev")
    lines.append("")
    lines.append("A `*` marks max_abs > 0.001.")
    lines.append("")
    lines.extend(marked_per_unit_table(unit_stats, cols))
    lines.append("")
    lines.append("## 3. Usable Ground Truth Summary")
    lines.append("")
    lines.append(f"- Usable ground truth columns: {', '.join(usable_cols) if usable_cols else 'None'}")
    lines.append(f"- Zero columns: {', '.join(zero_cols) if zero_cols else 'None'}")
    lines.append("")
    lines.extend(markdown_table(usable_df, ["Column", "Usable", "Nonzero Units", "Min", "Max"]))
    lines.append("")
    lines.append("## 4. Dev vs Test Comparison — DS02-006")
    lines.append("")
    lines.extend(markdown_table(compare_df, ["Column", "Dev_Std", "Test_Std", "Non-zero in Dev", "Non-zero in Test"]))
    lines.append("")
    lines.append("## 5. Cross-file Comparison — DS02-006 vs DS01-005 Dev")
    lines.append("")
    lines.append(f"- Non-zero DS02-006 dev columns: {', '.join(ds02_nonzero) if ds02_nonzero else 'None'}")
    lines.append(f"- Non-zero DS01-005 dev columns: {', '.join(ds01_nonzero) if ds01_nonzero else 'None'}")
    lines.append("")
    cross = pd.DataFrame(
        {
            "Column": cols,
            "DS02_dev_nonzero": [col in ds02_nonzero for col in cols],
            "DS01_dev_nonzero": [col in ds01_nonzero for col in cols],
        }
    )
    lines.extend(markdown_table(cross, ["Column", "DS02_dev_nonzero", "DS01_dev_nonzero"]))
    lines.append("")
    lines.append("## 6. Diagnosis")
    lines.append("")
    lines.append("**Q1: Is HPC_eff_mod the only zero column, or is the entire T_dev block zero?**")
    lines.append("")
    lines.append("HPC_eff_mod is zero, but the entire T_dev block is not empty. DS02-006 dev has non-zero HPT_eff_mod, LPT_eff_mod, and LPT_flow_mod.")
    lines.append("")
    lines.append("**Q2: Which units have non-zero degradation labels?**")
    lines.append("")
    lines.append("All DS02-006 dev units show non-trivial non-zero values for HPT_eff_mod. Units 16, 18, and 20 also show non-zero LPT_eff_mod and LPT_flow_mod. HPC_eff_mod remains zero for all units.")
    lines.append("")
    lines.append("**Q3: Which ground truth column should be used for Spearman correlation instead of HPC_eff_mod?**")
    lines.append("")
    lines.append(f"For DS02-006 dev, use `{best_col}`. It is non-zero across the selected units and is the clearest efficiency degradation label in this file.")
    lines.append("")
    lines.append("**Q4: Is DS02-006 dev split suitable for ground truth correlation validation? If not, which DS file is recommended?**")
    lines.append("")
    lines.append("DS02-006 dev is not suitable for HPC_eff_mod correlation validation because HPC_eff_mod is constant zero. It is suitable only if the C0 rerun switches the ground-truth label to a non-zero DS02 component such as HPT_eff_mod. For HPC-specific validation, the DS01 spot check should be used only if its HPC_eff_mod is non-zero; otherwise pick a file whose component degradation matches the target variable.")
    lines.append("")
    lines.append("## 7. Recommendation")
    lines.append("")
    lines.append(f"- Best ground truth column for a DS02 C0 Spearman rerun: `{best_col}`.")
    lines.append(f"- Best DS file from this spot check: `{best_file}`.")
    lines.append("- Recommended rerun rule: align the state target with the component that actually degrades in the selected DS file. Do not reuse HPC_eff_mod when it is constant zero.")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
