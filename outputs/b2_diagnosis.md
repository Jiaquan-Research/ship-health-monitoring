# Validation B2 Diagnosis

## Section 1: Filtering Summary

| Dataset | Rows Before | Rows After | Retention % |
| --- | --- | --- | --- |
| Baseline | 525540 | 525540 | 100 |
| 065 | 525540 | 525540 | 100 |
| 080 | 525540 | 525540 | 100 |
| 095 | 525540 | 525540 | 100 |

## Section 2: Raw State Variable Means

| Variable | Baseline | 065 | 080 | 095 |
| --- | --- | --- | --- | --- |
| CHL_POW_1 | 28.1798 | 28.8878 | 28.4248 | 28.2163 |
| CHL_SW_TEMP_1 | 51.8873 | 51.8902 | 51.8879 | 51.8873 |
| CT_SW_TEMP_1 | 62.1848 | 63.4408 | 62.7914 | 62.32 |
| CHL_RWCD_TEMP_1 | 64.2308 | 64.7302 | 64.4298 | 64.2669 |
| CT_RW_TEMP_1 | 65.8038 | 66.3055 | 66.0034 | 65.84 |
| CT_POW_1 | 1.40169 | 2.16147 | 1.88048 | 1.51057 |
| CT_FAN_SPD_1 | 0.205347 | 0.249364 | 0.232051 | 0.211381 |

## Section 3: Time Range Audit

### Time Coverage

| Dataset | Start | End | Duration |
| --- | --- | --- | --- |
| Baseline | 2018-01-01 01:00:00 | 2018-12-31 23:59:00 | 364 days 22:59:00 |
| 065 | 2018-01-01 01:00:00 | 2018-12-31 23:59:00 | 364 days 22:59:00 |
| 080 | 2018-01-01 01:00:00 | 2018-12-31 23:59:00 | 364 days 22:59:00 |
| 095 | 2018-01-01 01:00:00 | 2018-12-31 23:59:00 | 364 days 22:59:00 |

### Month Distribution

| Dataset | Jan% | Feb% | Mar% | Apr% | May% | Jun% | Jul% | Aug% | Sep% | Oct% | Nov% | Dec% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | 8.4827 | 7.67211 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 |
| 065 | 8.4827 | 7.67211 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 |
| 080 | 8.4827 | 7.67211 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 |
| 095 | 8.4827 | 7.67211 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 | 8.49412 | 8.22012 | 8.49412 | 8.22012 | 8.49412 |

## Section 4: Condition Variable Audit

| Variable | Baseline | 065 | 080 | 095 |
| --- | --- | --- | --- | --- |
| CWL_SEC_LOAD | 96029.3 | 96020.6 | 96025.8 | 96028.7 |
| OA_TEMP | 44.9141 | 44.914 | 44.914 | 44.9141 |
| OA_TEMP_WB | 49.9823 | 49.9823 | 49.9823 | 49.9823 |
| CWL_PRI_SW_TEMPSPT | 51.9325 | 51.9325 | 51.9326 | 51.9324 |
| CT_SW_TEMPSPT | 64.5362 | 64.5363 | 64.5362 | 64.5361 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 | 960.961 |

## Section 5: Load Distribution Audit

| Dataset | P5 | P50 | P95 |
| --- | --- | --- | --- |
| Baseline | 0 | 0.0041473 | 547322 |
| 065 | 0 | 0.00423303 | 547328 |
| 080 | 0 | 0.00414775 | 547314 |
| 095 | 0 | 0.00414744 | 547323 |

## Section 6: Delta From Baseline

| Variable | Delta_065 | Delta_080 | Delta_095 |
| --- | --- | --- | --- |
| CHL_POW_1 | 0.708002 | 0.245 | 0.0365746 |
| CHL_SW_TEMP_1 | 0.00297619 | 0.000671525 | 4.89823e-05 |
| CT_SW_TEMP_1 | 1.25597 | 0.606572 | 0.135232 |
| CHL_RWCD_TEMP_1 | 0.499455 | 0.198995 | 0.0361138 |
| CT_RW_TEMP_1 | 0.501699 | 0.19962 | 0.0361704 |
| CT_POW_1 | 0.75978 | 0.478792 | 0.108877 |
| CT_FAN_SPD_1 | 0.0440165 | 0.0267036 | 0.00603379 |

### Raw Trend Direction

| Variable | Direction |
| --- | --- |
| CHL_POW_1 | decreases 065->080->095 |
| CHL_SW_TEMP_1 | decreases 065->080->095 |
| CT_SW_TEMP_1 | decreases 065->080->095 |
| CHL_RWCD_TEMP_1 | decreases 065->080->095 |
| CT_RW_TEMP_1 | decreases 065->080->095 |
| CT_POW_1 | decreases 065->080->095 |
| CT_FAN_SPD_1 | decreases 065->080->095 |

## Section 7: Documentation Findings

### Non-CSV Files

| File | Size |
| --- | --- |
| LBNL_FDD_Data_Sets_Chiller_Plant.zip | 1570938957 |

No relevant text matches were found for fouling/severity/065/080/095/0.65/0.80/0.95.

Interpretation: no local documentation was available to directly define the label semantics, so diagnosis relies on raw process trends and identical operating-condition coverage.

## Section 8: Severity Semantics Audit

| Hypothesis | Confidence |
| --- | --- |
| A: 065 = most severe fault, 095 = least severe fault | 100 |
| C: Labels represent another physical quantity | 25.0828 |
| B: 095 = most severe fault, 065 = least severe fault | 20 |

## Section 9: Final Diagnosis

### Q1: Do raw State Variables change monotonically with severity label?

They mostly change monotonically in the inverse direction: raw fault effects are largest at 065, smaller at 080, and smallest at 095.

### Q2: Are Condition Variables comparable across datasets?

Yes. Condition-variable means, load distribution, time range, and month distribution are effectively identical across the four datasets.

### Q3: What do labels most likely mean?

065 most likely represents the strongest fouling case and 095 the weakest among these three files.

### Q4: Rank explanations for B2 FAIL

1. A. Severity labels inverted
2. C. Fault effect is inherently non-monotonic
3. D. Expected State Model does not generalize

Explanation B, Condition Variables differ substantially, is least likely because audited condition variables and calendar coverage match across datasets.

### Q5: What should Validation B2.1 do next?

Rerun the monotonic residual test using the severity order Baseline -> 095 -> 080 -> 065, while keeping the frozen B1 models and residual definitions unchanged.