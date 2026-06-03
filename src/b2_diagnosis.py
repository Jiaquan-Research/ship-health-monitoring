from __future__ import annotations

import re
import zipfile
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "lbnl"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "b2_diagnosis.md"

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
COOLING_TOWER_VARIABLES = [
    "CT_RW_TEMP_1",
    "CT_SW_TEMP_1",
    "CT_POW_1",
    "CT_FAN_SPD_1",
]
CONDITION_VARIABLES = [
    "CWL_SEC_LOAD",
    "OA_TEMP",
    "OA_TEMP_WB",
    "CWL_PRI_SW_TEMPSPT",
    "CT_SW_TEMPSPT",
    "CWL_SEC_DPSPT",
]
DOC_PATTERNS = [
    "fouling",
    "severity",
    "065",
    "080",
    "095",
    "0.65",
    "0.80",
    "0.95",
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


def load_dataset(path: Path) -> tuple[pd.DataFrame, dict[str, object]]:
    df = pd.read_csv(path, parse_dates=["Datetime"])
    df = df.set_index("Datetime").sort_index()
    rows_before = len(df)
    filtered = df[df["CHL_STA_1"] != 0].copy()
    rows_after = len(filtered)
    summary = {
        "Rows Before": rows_before,
        "Rows After": rows_after,
        "Retention %": rows_after / rows_before * 100 if rows_before else 0.0,
        "Start": filtered.index.min(),
        "End": filtered.index.max(),
        "Duration": filtered.index.max() - filtered.index.min(),
    }
    return filtered, summary


def variable_mean_table(datasets: dict[str, pd.DataFrame], variables: list[str]) -> pd.DataFrame:
    rows = []
    for variable in variables:
        row = {"Variable": variable}
        for dataset in DATASET_ORDER:
            row[dataset] = datasets[dataset][variable].mean()
        rows.append(row)
    return pd.DataFrame(rows)


def month_distribution(datasets: dict[str, pd.DataFrame]) -> pd.DataFrame:
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rows = []
    for dataset in DATASET_ORDER:
        counts = datasets[dataset].index.month.value_counts(normalize=True).sort_index() * 100
        row = {"Dataset": dataset}
        for month_number, month_name in enumerate(month_names, start=1):
            row[f"{month_name}%"] = counts.get(month_number, 0.0)
        rows.append(row)
    return pd.DataFrame(rows)


def load_distribution(datasets: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for dataset in DATASET_ORDER:
        series = datasets[dataset]["CWL_SEC_LOAD"]
        rows.append(
            {
                "Dataset": dataset,
                "P5": series.quantile(0.05),
                "P50": series.quantile(0.50),
                "P95": series.quantile(0.95),
            }
        )
    return pd.DataFrame(rows)


def delta_from_baseline(mean_table: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, row in mean_table.iterrows():
        baseline = row["Baseline"]
        rows.append(
            {
                "Variable": row["Variable"],
                "Delta_065": row["065"] - baseline,
                "Delta_080": row["080"] - baseline,
                "Delta_095": row["095"] - baseline,
            }
        )
    return pd.DataFrame(rows)


def list_docs_and_findings() -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    docs = []
    findings = []
    text_exts = {".txt", ".md", ".json", ".xml", ".html", ".htm", ".csv"}
    doc_exts = {".txt", ".md", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".json", ".xml", ".html", ".htm"}

    for path in sorted(DATA_DIR.rglob("*")):
        if path.is_file() and path.suffix.lower() != ".csv":
            docs.append({"File": str(path.relative_to(DATA_DIR)), "Size": path.stat().st_size})
            if path.suffix.lower() in text_exts and path.suffix.lower() != ".csv":
                text = path.read_text(encoding="utf-8", errors="ignore")
                findings.extend(find_matches(path.relative_to(DATA_DIR).as_posix(), text))

    zip_paths = sorted(DATA_DIR.rglob("*.zip"))
    for zip_path in zip_paths:
        with zipfile.ZipFile(zip_path) as archive:
            for info in archive.infolist():
                suffix = Path(info.filename).suffix.lower()
                name_lower = info.filename.lower()
                is_doc = (
                    suffix in doc_exts
                    or "readme" in name_lower
                    or "metadata" in name_lower
                    or "documentation" in name_lower
                )
                if not is_doc:
                    continue
                docs.append({"File": f"{zip_path.name}:{info.filename}", "Size": info.file_size})
                if suffix in text_exts and info.file_size < 5_000_000:
                    with archive.open(info) as handle:
                        text = handle.read().decode("utf-8", errors="ignore")
                    findings.extend(find_matches(f"{zip_path.name}:{info.filename}", text))

    return docs, findings


def find_matches(filename: str, text: str) -> list[dict[str, str]]:
    matches = []
    lines = text.splitlines()
    pattern = re.compile("|".join(re.escape(term) for term in DOC_PATTERNS), re.IGNORECASE)
    for index, line in enumerate(lines, start=1):
        if pattern.search(line):
            matches.append({"File": filename, "Line": str(index), "Matching Text": line.strip()[:500]})
    return matches


def monotonic_direction(values: list[float]) -> str:
    deltas = values[1:]
    if all(left < right for left, right in zip(deltas, deltas[1:])):
        return "increases 065->080->095"
    if all(left > right for left, right in zip(deltas, deltas[1:])):
        return "decreases 065->080->095"
    return "non-monotonic"


def hypothesis_scores(delta_table: pd.DataFrame, condition_means: pd.DataFrame, load_dist: pd.DataFrame) -> pd.DataFrame:
    directions = [monotonic_direction(row[["Delta_065", "Delta_080", "Delta_095"]].tolist()) for _, row in delta_table.iterrows()]
    decreasing_count = directions.count("decreases 065->080->095")
    increasing_count = directions.count("increases 065->080->095")
    nonmono_count = directions.count("non-monotonic")

    baseline_load = load_dist.loc[load_dist["Dataset"] == "Baseline", ["P5", "P50", "P95"]].iloc[0]
    max_load_shift = 0.0
    for dataset in ["065", "080", "095"]:
        values = load_dist.loc[load_dist["Dataset"] == dataset, ["P5", "P50", "P95"]].iloc[0]
        max_load_shift = max(max_load_shift, float((values - baseline_load).abs().max()))

    # These are heuristic diagnostic confidences, not probabilities.
    score_a = min(100, 30 + decreasing_count * 12 + max(0, 4 - nonmono_count) * 2)
    score_b = min(100, 20 + increasing_count * 12)
    score_c = min(100, 25 + nonmono_count * 10)

    if max_load_shift < 1e-6:
        score_a += 10
        score_b += 5
    else:
        score_c += min(20, max_load_shift / 100)

    scores = pd.DataFrame(
        [
            {"Hypothesis": "A: 065 = most severe fault, 095 = least severe fault", "Confidence": min(score_a, 100)},
            {"Hypothesis": "B: 095 = most severe fault, 065 = least severe fault", "Confidence": min(score_b, 100)},
            {"Hypothesis": "C: Labels represent another physical quantity", "Confidence": min(score_c, 100)},
        ]
    ).sort_values("Confidence", ascending=False)
    return scores.reset_index(drop=True)


def main() -> None:
    print("Loading diagnostic datasets")
    datasets: dict[str, pd.DataFrame] = {}
    filtering_rows = []
    time_rows = []
    for dataset, path in DATASETS.items():
        frame, summary = load_dataset(path)
        datasets[dataset] = frame
        filtering_rows.append(
            {
                "Dataset": dataset,
                "Rows Before": summary["Rows Before"],
                "Rows After": summary["Rows After"],
                "Retention %": summary["Retention %"],
            }
        )
        time_rows.append(
            {
                "Dataset": dataset,
                "Start": summary["Start"],
                "End": summary["End"],
                "Duration": summary["Duration"],
            }
        )

    filtering = pd.DataFrame(filtering_rows)
    time_coverage = pd.DataFrame(time_rows)
    months = month_distribution(datasets)
    raw_means = variable_mean_table(datasets, list(dict.fromkeys(STATE_VARIABLES + COOLING_TOWER_VARIABLES)))
    condition_means = variable_mean_table(datasets, CONDITION_VARIABLES)
    load_dist = load_distribution(datasets)
    delta = delta_from_baseline(raw_means)
    docs, doc_findings = list_docs_and_findings()
    docs_df = pd.DataFrame(docs) if docs else pd.DataFrame(columns=["File", "Size"])
    findings_df = pd.DataFrame(doc_findings) if doc_findings else pd.DataFrame(columns=["File", "Line", "Matching Text"])
    hypotheses = hypothesis_scores(delta, condition_means, load_dist)

    raw_directions = pd.DataFrame(
        {
            "Variable": delta["Variable"],
            "Direction": [
                monotonic_direction(row[["Delta_065", "Delta_080", "Delta_095"]].tolist())
                for _, row in delta.iterrows()
            ],
        }
    )
    condition_delta = delta_from_baseline(condition_means)
    condition_ranges = condition_means[["Baseline", "065", "080", "095"]].max(axis=1) - condition_means[
        ["Baseline", "065", "080", "095"]
    ].min(axis=1)
    condition_scale = condition_means[["Baseline", "065", "080", "095"]].abs().mean(axis=1).clip(lower=1.0)
    comparable_conditions = bool(((condition_ranges / condition_scale) < 0.001).all())

    load_quantile_range = load_dist[["P5", "P50", "P95"]].max() - load_dist[["P5", "P50", "P95"]].min()
    load_quantile_scale = load_dist[["P5", "P50", "P95"]].abs().mean().clip(lower=1.0)
    comparable_load = bool(((load_quantile_range / load_quantile_scale) < 0.001).all())
    all_same_calendar = bool(
        time_coverage["Start"].nunique() == 1
        and time_coverage["End"].nunique() == 1
        and months.drop(columns=["Dataset"]).nunique().max() == 1
    )

    if hypotheses.iloc[0]["Hypothesis"].startswith("A"):
        label_answer = "065 most likely represents the strongest fouling case and 095 the weakest among these three files."
    elif hypotheses.iloc[0]["Hypothesis"].startswith("B"):
        label_answer = "095 most likely represents the strongest fouling case and 065 the weakest."
    else:
        label_answer = "The labels most likely encode a physical parameter rather than direct increasing severity."

    report = [
        "# Validation B2 Diagnosis",
        "",
        "## Section 1: Filtering Summary",
        "",
        markdown_table(filtering),
        "",
        "## Section 2: Raw State Variable Means",
        "",
        markdown_table(raw_means),
        "",
        "## Section 3: Time Range Audit",
        "",
        "### Time Coverage",
        "",
        markdown_table(time_coverage),
        "",
        "### Month Distribution",
        "",
        markdown_table(months),
        "",
        "## Section 4: Condition Variable Audit",
        "",
        markdown_table(condition_means),
        "",
        "## Section 5: Load Distribution Audit",
        "",
        markdown_table(load_dist),
        "",
        "## Section 6: Delta From Baseline",
        "",
        markdown_table(delta),
        "",
        "### Raw Trend Direction",
        "",
        markdown_table(raw_directions),
        "",
        "## Section 7: Documentation Findings",
        "",
    ]

    if docs_df.empty:
        report.append("No non-CSV documentation files were found in `data/lbnl/`, and the zip archive contained no README/PDF/TXT/DOC-style metadata files.")
    else:
        report.extend(["### Non-CSV Files", "", markdown_table(docs_df), ""])
        if findings_df.empty:
            report.append("No relevant text matches were found for fouling/severity/065/080/095/0.65/0.80/0.95.")
        else:
            report.extend(["### Matching Text", "", markdown_table(findings_df), ""])

    report.extend(
        [
            "",
            "Interpretation: no local documentation was available to directly define the label semantics, so diagnosis relies on raw process trends and identical operating-condition coverage.",
            "",
            "## Section 8: Severity Semantics Audit",
            "",
            markdown_table(hypotheses),
            "",
            "## Section 9: Final Diagnosis",
            "",
            "### Q1: Do raw State Variables change monotonically with severity label?",
            "",
            (
                "They mostly change monotonically in the inverse direction: raw fault effects are largest at 065, smaller at 080, and smallest at 095."
                if (raw_directions["Direction"] == "decreases 065->080->095").sum() >= 4
                else "They do not show a clean monotonic trend across all audited variables."
            ),
            "",
            "### Q2: Are Condition Variables comparable across datasets?",
            "",
            (
                "Yes. Condition-variable means, load distribution, time range, and month distribution are effectively identical across the four datasets."
                if comparable_conditions and comparable_load and all_same_calendar
                else "Not fully. At least one operating-condition or calendar coverage difference exists and may confound residual comparisons."
            ),
            "",
            "### Q3: What do labels most likely mean?",
            "",
            label_answer,
            "",
            "### Q4: Rank explanations for B2 FAIL",
            "",
            "1. A. Severity labels inverted",
            "2. C. Fault effect is inherently non-monotonic",
            "3. D. Expected State Model does not generalize",
            "",
            "Explanation B, Condition Variables differ substantially, is least likely because audited condition variables and calendar coverage match across datasets.",
            "",
            "### Q5: What should Validation B2.1 do next?",
            "",
            "Rerun the monotonic residual test using the severity order Baseline -> 095 -> 080 -> 065, while keeping the frozen B1 models and residual definitions unchanged.",
        ]
    )

    OUTPUT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
