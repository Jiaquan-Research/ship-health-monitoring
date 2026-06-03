from __future__ import annotations

from collections import Counter
from pathlib import Path

import pandas as pd
from pandas.api.types import is_numeric_dtype


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "lbnl"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "lbnl_data_audit.md"

TIME_COLUMN_HINTS = ("time", "date", "datetime", "timestamp")
LABEL_COLUMN_HINTS = ("fault", "label", "class", "status", "state", "mode", "sta")
MAX_UNIQUE_VALUES = 30


def format_bytes(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} {unit}"
        value /= 1024
    return f"{size} B"


def find_time_column(df: pd.DataFrame) -> str | None:
    for column in df.columns:
        lowered = str(column).lower()
        if any(hint in lowered for hint in TIME_COLUMN_HINTS):
            parsed = pd.to_datetime(df[column], errors="coerce")
            if parsed.notna().mean() >= 0.8:
                return str(column)
    return None


def infer_sampling_interval(timestamps: pd.Series) -> dict[str, str]:
    values = timestamps.dropna().sort_values()
    diffs = values.diff().dropna()
    diffs = diffs[diffs > pd.Timedelta(0)]
    if diffs.empty:
        return {
            "median": "n/a",
            "mode": "n/a",
            "min": "n/a",
            "max": "n/a",
        }

    counts = Counter(diffs)
    mode_interval, mode_count = counts.most_common(1)[0]
    return {
        "median": str(diffs.median()),
        "mode": f"{mode_interval} ({mode_count} occurrences)",
        "min": str(diffs.min()),
        "max": str(diffs.max()),
    }


def markdown_table(rows: list[list[object]], headers: list[str]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        rendered = [str(value).replace("\n", " ") for value in row]
        lines.append("| " + " | ".join(rendered) + " |")
    return lines


def column_profile(df: pd.DataFrame) -> list[str]:
    missing = df.isna().sum()
    rows = []
    for column in df.columns:
        count = int(missing[column])
        pct = (count / len(df) * 100) if len(df) else 0.0
        rows.append([column, df[column].dtype, count, f"{pct:.3f}%"])
    return markdown_table(rows, ["Column", "Dtype", "Missing Count", "Missing %"])


def numeric_stats(df: pd.DataFrame) -> list[str]:
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        return ["No numeric columns found."]

    stats = numeric.agg(["min", "max", "mean"]).transpose()
    rows = []
    for column, values in stats.iterrows():
        rows.append(
            [
                column,
                f"{values['min']:.6g}",
                f"{values['max']:.6g}",
                f"{values['mean']:.6g}",
            ]
        )
    return markdown_table(rows, ["Column", "Min", "Max", "Mean"])


def is_categorical_or_label(column: str, series: pd.Series) -> bool:
    lowered = column.lower()
    if any(hint in lowered for hint in LABEL_COLUMN_HINTS):
        return True
    if not is_numeric_dtype(series):
        return True
    return series.nunique(dropna=True) <= MAX_UNIQUE_VALUES


def unique_value_summary(df: pd.DataFrame) -> list[str]:
    rows = []
    for column in df.columns:
        series = df[column]
        if not is_categorical_or_label(str(column), series):
            continue

        counts = series.value_counts(dropna=False).head(MAX_UNIQUE_VALUES)
        values = ", ".join(f"{repr(index)}: {count}" for index, count in counts.items())
        total_unique = int(series.nunique(dropna=True))
        rows.append([column, total_unique, values])

    if not rows:
        return ["No categorical or label-like columns found."]
    return markdown_table(rows, ["Column", "Unique Values", "Top Values"])


def audit_csv(path: Path) -> list[str]:
    lines = [f"## {path.name}", ""]
    lines.append(f"- Size: {format_bytes(path.stat().st_size)} ({path.stat().st_size:,} bytes)")

    df = pd.read_csv(path, low_memory=False)
    lines.append(f"- Rows: {len(df):,}")
    lines.append(f"- Columns: {len(df.columns):,}")

    time_column = find_time_column(df)
    if time_column:
        timestamps = pd.to_datetime(df[time_column], errors="coerce")
        intervals = infer_sampling_interval(timestamps)
        lines.extend(
            [
                f"- Time column: `{time_column}`",
                f"- Time range: {timestamps.min()} to {timestamps.max()}",
                "- Sampling interval:",
                f"  - Median: {intervals['median']}",
                f"  - Mode: {intervals['mode']}",
                f"  - Min: {intervals['min']}",
                f"  - Max: {intervals['max']}",
            ]
        )
    else:
        lines.append("- Time column: not detected")

    lines.extend(["", "### Columns, Data Types, and Missing Values", ""])
    lines.extend(column_profile(df))
    lines.extend(["", "### Numeric Basic Statistics", ""])
    lines.extend(numeric_stats(df))
    lines.extend(["", "### Categorical / Label-Like Unique Values", ""])
    lines.extend(unique_value_summary(df))
    lines.append("")
    return lines


def main() -> None:
    csv_files = sorted(DATA_DIR.rglob("*.csv"))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    report = [
        "# LBNL Chiller Plant Data Audit",
        "",
        f"- Data directory: `{DATA_DIR}`",
        f"- CSV files found: {len(csv_files)}",
        "",
    ]

    if not csv_files:
        report.append("No CSV files found.")
    else:
        for csv_file in csv_files:
            relative = csv_file.relative_to(PROJECT_ROOT)
            print(f"Auditing {relative}")
            report.extend(audit_csv(csv_file))

    OUTPUT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote audit report to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
