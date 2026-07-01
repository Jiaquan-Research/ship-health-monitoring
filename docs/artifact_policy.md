# Artifact Policy

This document provides repository artifact guidance before Gate M3 Framework Audit.

It is a policy recommendation document only. It does not change repository behaviour, `.gitignore`, experiment outputs, or version-control state.

## Purpose

Repository artifacts provide evidence, reproducibility, and reviewability for the Health Evidence framework.

Artifacts should be retained when they support one of the following purposes:

- reproduce a scientific object;
- document a completed audit;
- support reviewer inspection;
- preserve a frozen manifest;
- provide traceability between framework stages.

## Artifact Categories

### Version-Controlled Outputs

Recommended for version control:

- Markdown reports required for framework review;
- small CSV summaries that define scientific objects or evaluation tables;
- JSON manifests;
- small configuration files;
- final review documents;
- canonical architecture, decision, gate, taxonomy, and specification documents.

Examples:

- `lbnl_expected_state/outputs/reports/*.md`
- `lbnl_expected_state/outputs/manifests/*.json`
- `lbnl_expected_state/outputs/csv/h5b_prototype_summary.csv`
- `lbnl_expected_state/outputs/csv/h5b_evaluation_matrix.csv`

### Temporary Outputs

Temporary outputs include intermediate diagnostics, scratch reports, exploratory figures, and one-off generated artifacts that are not required for framework traceability.

Recommendation:

Temporary outputs should either be ignored, moved to a separate archive, or regenerated when needed.

No current files are moved by this policy.

### Large Files

Large generated files should not enter ordinary Git history without an explicit decision.

Recommended handling options:

- Git LFS;
- external artifact storage;
- release package;
- regenerate-from-manifest policy;
- local-only archive.

Examples requiring explicit policy:

- large residual datasets;
- generated candidate Health Indicator timelines;
- full group-membership audit CSVs;
- large model exports;
- large binary datasets.

## Figures

Figures are review artifacts.

Recommended version-control policy:

- retain final figures that are referenced by frozen reports;
- archive exploratory or superseded figures;
- avoid storing repeated regenerated variants unless needed for audit.

Figures should remain grouped by experiment or framework stage.

Current preferred location for LBNL framework figures:

```text
lbnl_expected_state/outputs/figures/
```

## CSV Files

CSV files fall into two categories.

### Canonical CSVs

Canonical CSVs define or summarize scientific objects.

Examples:

- condition variable definitions;
- evaluation matrix summaries;
- group metrics;
- leakage audit summaries.

These are candidates for version control when small enough.

### Large Generated CSVs

Large generated CSVs contain full timelines or row-level outputs.

Examples:

- residual timelines;
- Health Indicator candidate timelines;
- group membership tables.

These require explicit artifact policy before commit.

## Reports

Reports are primary review artifacts and should generally be version-controlled when they document completed tasks, gates, or scientific reviews.

Recommended report categories:

- experiment reports;
- gate reviews;
- scientific reviews;
- framework summaries;
- reviewer decision records.

Current preferred location for LBNL framework reports:

```text
lbnl_expected_state/outputs/reports/
```

## Models

Model artifacts support reproducibility but can become large or environment-specific.

Recommended policy:

- retain lightweight frozen model files when they are required for reproducibility;
- pair every retained model with a manifest;
- use external storage or Git LFS for large model artifacts.

Current LBNL model artifact:

```text
lbnl_expected_state/outputs/models/expected_state_v1_xgb.json
```

## Root Outputs

Root-level `outputs/` currently contains historical and exploratory artifacts.

Recommendation:

Treat root `outputs/` as historical unless a file is explicitly referenced by current framework documentation.

Future cleanup may separate it into:

```text
archive/
  legacy_outputs/
  exploratory_outputs/
  superseded_outputs/
```

No files are moved by this policy.

## Retention Recommendation

Before Gate M3, each artifact should be assigned one of the following statuses:

- Retain in Git
- Retain via Git LFS
- Archive outside Git
- Regenerate when needed
- Personal/local reference only

This assignment should be performed before committing the framework freeze package.
