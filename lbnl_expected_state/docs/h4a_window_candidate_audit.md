# H4A Semantic Window Candidate Audit

## Objective

Generate quantitative evidence to support the Reviewer's decision on Semantic Window definition.

This task does not freeze the window.

This task does not run H4B experiments.

The Reviewer freezes the window after reviewing this audit.

## Inputs

```text
outputs/csv/residual_v1.csv
outputs/csv/hi_candidates_v1.csv
```

Condition columns required for this audit were read from the raw LBNL dataset by timestamp alignment.

Train split only.

No Test split was evaluated.

No model retraining was performed.

No figures were generated.

## Audit 1 - Load Threshold Candidates

Output CSV:

```text
outputs/csv/h4a_load_threshold_audit.csv
```

| Threshold              | Description             |   Train rows retained |   Train retention ratio (%) |   HI_C median |   HI_C IQR |   HI_C 95th percentile |   Residual Dispersion (IQR) |   Spearman(Residual, CWL_SEC_LOAD) within window |
|:-----------------------|:------------------------|----------------------:|----------------------------:|--------------:|-----------:|-----------------------:|----------------------------:|-------------------------------------------------:|
| CWL_SEC_LOAD > 0       | Exclude exact zero only |                324589 |                      82.351 |       1.1015  |    3.58275 |                9.71498 |                     1.45949 |                                         0.043679 |
| CWL_SEC_LOAD >= 50000  | Moderate exclusion      |                123625 |                      31.365 |       4.34564 |    4.76781 |               13.1472  |                     5.8453  |                                        -0.017994 |
| CWL_SEC_LOAD >= 100000 | Aggressive exclusion    |                113446 |                      28.782 |       4.67787 |    4.8243  |               13.4777  |                     6.29678 |                                        -0.009442 |

## Audit 2 - Flow Boundary Investigation

No fixed upper boundary for CWL_SEC_CW_FLOW is assumed in this audit.

The high-density cluster end is reported as a descriptive histogram-based estimate only. It is not a selected boundary.

### Flow Boundary Descriptive Statistics

| Statistic                                          |            Value |
|:---------------------------------------------------|-----------------:|
| Unique value count                                 | 189392           |
| p1                                                 |      8.37975e-06 |
| p5                                                 |      8.37975e-06 |
| p25                                                |      8.37975e-06 |
| p50                                                |    343.036       |
| p75                                                |    743.099       |
| p95                                                |    837.847       |
| p99                                                |    837.847       |
| High-density cluster end estimate                  |      8.37929     |
| Rows where CWL_SEC_CW_FLOW = 0                     |      0           |
| Rows where CWL_SEC_CW_FLOW < p1                    |    506           |
| Rows where CWL_SEC_CW_FLOW = 0 or near-zero (< p1) |    506           |
| Rows where CWL_SEC_CW_FLOW >= p99                  |  63713           |

### Candidate Flow Exclusion Rules

Output CSV:

```text
outputs/csv/h4a_flow_boundary_audit.csv
```

| Rule   | Definition                                     |   p1 value |   p99 value |   Train rows retained |   Train retention ratio (%) |   Residual Dispersion (IQR) within window |   Spearman(Residual, CWL_SEC_CW_FLOW) within window |
|:-------|:-----------------------------------------------|-----------:|------------:|----------------------:|----------------------------:|------------------------------------------:|----------------------------------------------------:|
| F1     | CWL_SEC_CW_FLOW > p1                           |      8e-06 |     837.847 |                265871 |                      67.453 |                                  1.03858  |                                           -0.046441 |
| F2     | CWL_SEC_CW_FLOW > p1 AND CWL_SEC_CW_FLOW < p99 |      8e-06 |     837.847 |                202158 |                      51.289 |                                  0.113147 |                                           -0.075946 |

## Audit 3 - Combined Window Candidates

Output CSV:

```text
outputs/csv/h4a_combined_window_audit.csv
```

| Window   | Definition                                                |   Train rows retained |   Train retention ratio (%) |   HI_C median |   HI_C IQR |   HI_C 95th percentile |   Residual Dispersion (IQR) |   Spearman(Residual, CWL_SEC_LOAD) within window |   Spearman(Residual, OA_TEMP) within window |
|:---------|:----------------------------------------------------------|----------------------:|----------------------------:|--------------:|-----------:|-----------------------:|----------------------------:|-------------------------------------------------:|--------------------------------------------:|
| W1       | CWL_SEC_LOAD >= 50000 AND CWL_SEC_CW_FLOW > p1 AND < p99  |                 73079 |                      18.541 |       4.07781 |    4.58822 |                12.3201 |                     5.62903 |                                        -0.018465 |                                   -0.017797 |
| W2       | CWL_SEC_LOAD >= 100000 AND CWL_SEC_CW_FLOW > p1 AND < p99 |                 71042 |                      18.024 |       4.14932 |    4.5948  |                12.4141 |                     5.64895 |                                        -0.020379 |                                   -0.01757  |
| W3       | CWL_SEC_LOAD >= 50000 only                                |                123625 |                      31.365 |       4.34564 |    4.76781 |                13.1472 |                     5.8453  |                                        -0.017994 |                                   -0.01225  |

## Reviewer Window Decision

Reviewer fills after reviewing all three audits.

```text
Selected Window Definition

Exclusion rule 1: [Reviewer fills]

Exclusion rule 2: [Reviewer fills, if any]

Train rows retained: [from audit]

Train retention ratio: [from audit]

Evidence basis: [Reviewer fills - reference specific audit observations]

Reviewer Decision: PASS / REVISE
```

## Boundary

This audit reports numbers only.

It does not select a window.

It does not compare Baseline vs Window.

It does not compute H1 metrics.

It does not run H4B.
