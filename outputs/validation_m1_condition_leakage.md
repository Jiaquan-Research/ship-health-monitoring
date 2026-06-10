# Validation M-1 Condition Leakage Audit

## 1. Protocol Reference

Protocol: `docs/review/m1_condition_leakage_protocol_v0.1.md`

No retraining was performed.

No new datasets were introduced.

No fault data was loaded.

No remediation was performed.

## 2. Frozen Artifact Sources

* Residual source: `outputs\residuals_normal.csv`
* HI aggregate source: `outputs\hi_v0\hi_v0_severity_stats.csv`
* Baseline condition source: `data\lbnl\ChillerPlant.csv`

HVAC-v1 condition variables used:

* `CWL_SEC_LOAD`
* `OA_TEMP`
* `OA_TEMP_WB`
* `CWL_PRI_SW_TEMPSPT`
* `CT_SW_TEMPSPT`
* `CWL_SEC_DPSPT`

HI_v0 was derived from frozen normalized residuals using the existing HI_v0 Rolling RMS definition for `CT_SW_TEMP_1`, window `6h`. This did not recompute residuals or retrain models.

Baseline HI stats reference row: HI_mean=0.02265, HI_p95=0.07093, HI_p99=0.1022.

Aligned rows analyzed: 525,361

## 3. Full-Period Correlations

### Residual_RMS

| Rank | Condition | Spearman | Pearson |
|---:|---|---:|---:|
| 1 | OA_TEMP_WB | 0.7756 | 0.4449 |
| 2 | OA_TEMP | 0.7633 | 0.4309 |
| 3 | CT_SW_TEMPSPT | 0.7573 | 0.4278 |
| 4 | CWL_PRI_SW_TEMPSPT | -0.7318 | -0.4399 |
| 5 | CWL_SEC_LOAD | 0.666 | 0.4159 |
| 6 | CWL_SEC_DPSPT | N/A | N/A |

### HI_v0

| Rank | Condition | Spearman | Pearson |
|---:|---|---:|---:|
| 1 | CT_SW_TEMPSPT | 0.7148 | 0.4995 |
| 2 | OA_TEMP | 0.6991 | 0.613 |
| 3 | OA_TEMP_WB | 0.6942 | 0.595 |
| 4 | CWL_PRI_SW_TEMPSPT | -0.6587 | -0.429 |
| 5 | CWL_SEC_LOAD | 0.5398 | 0.2609 |
| 6 | CWL_SEC_DPSPT | N/A | N/A |

## 4. Variance Explanation Results

| Target | Linear R2 | Random Forest R2 |
|---|---:|---:|
| Residual_RMS | 0.2323 | 0.3788 |
| HI_v0 | 0.4084 | 0.6453 |

### Feature Importance

| Target | Model | Rank | Condition | Importance |
|---|---|---:|---|---:|
| Residual_RMS | LinearRegression | 1 | CWL_SEC_LOAD | 0.01206 |
| Residual_RMS | LinearRegression | 2 | CWL_PRI_SW_TEMPSPT | 0.01029 |
| Residual_RMS | LinearRegression | 3 | OA_TEMP | 0.009237 |
| Residual_RMS | LinearRegression | 4 | OA_TEMP_WB | 0.007938 |
| Residual_RMS | LinearRegression | 5 | CT_SW_TEMPSPT | 0.001172 |
| Residual_RMS | LinearRegression | 6 | CWL_SEC_DPSPT | 0 |
| Residual_RMS | RandomForestRegressor | 1 | OA_TEMP_WB | 0.7234 |
| Residual_RMS | RandomForestRegressor | 2 | CWL_SEC_LOAD | 0.226 |
| Residual_RMS | RandomForestRegressor | 3 | CT_SW_TEMPSPT | 0.03102 |
| Residual_RMS | RandomForestRegressor | 4 | OA_TEMP | 0.01874 |
| Residual_RMS | RandomForestRegressor | 5 | CWL_PRI_SW_TEMPSPT | 0.0009051 |
| Residual_RMS | RandomForestRegressor | 6 | CWL_SEC_DPSPT | 0 |
| HI_v0 | LinearRegression | 1 | OA_TEMP_WB | 0.012 |
| HI_v0 | LinearRegression | 2 | CT_SW_TEMPSPT | 0.009905 |
| HI_v0 | LinearRegression | 3 | CWL_SEC_LOAD | 0.006707 |
| HI_v0 | LinearRegression | 4 | CWL_PRI_SW_TEMPSPT | 0.004532 |
| HI_v0 | LinearRegression | 5 | OA_TEMP | 0.00328 |
| HI_v0 | LinearRegression | 6 | CWL_SEC_DPSPT | 0 |
| HI_v0 | RandomForestRegressor | 1 | OA_TEMP | 0.7848 |
| HI_v0 | RandomForestRegressor | 2 | CWL_SEC_LOAD | 0.1079 |
| HI_v0 | RandomForestRegressor | 3 | CT_SW_TEMPSPT | 0.074 |
| HI_v0 | RandomForestRegressor | 4 | OA_TEMP_WB | 0.01827 |
| HI_v0 | RandomForestRegressor | 5 | CWL_PRI_SW_TEMPSPT | 0.01503 |
| HI_v0 | RandomForestRegressor | 6 | CWL_SEC_DPSPT | 0 |

## 5. Seasonal Stability Results

| Target | Condition | Window 1 | Window 2 | Window 3 | Sign Reversal | Magnitude Range |
|---|---|---:|---:|---:|---|---:|
| Residual_RMS | OA_TEMP_WB | 0.2726 | 0.3383 | 0.7423 | False | 0.4697 |
| Residual_RMS | OA_TEMP | 0.266 | 0.3 | 0.7253 | False | 0.4593 |
| Residual_RMS | CT_SW_TEMPSPT | 0.4406 | 0.2874 | 0.7335 | False | 0.4461 |
| Residual_RMS | CWL_SEC_LOAD | 0.2739 | 0.3658 | 0.6332 | False | 0.3592 |
| Residual_RMS | CWL_PRI_SW_TEMPSPT | -0.4381 | -0.3216 | -0.6487 | False | 0.3271 |
| Residual_RMS | CWL_SEC_DPSPT | N/A | N/A | N/A | False | N/A |
| HI_v0 | OA_TEMP | 0.03019 | 0.1089 | 0.6662 | False | 0.636 |
| HI_v0 | OA_TEMP_WB | 0.04507 | 0.05505 | 0.6638 | False | 0.6187 |
| HI_v0 | CT_SW_TEMPSPT | 0.4336 | 0.09113 | 0.7045 | False | 0.6134 |
| HI_v0 | CWL_PRI_SW_TEMPSPT | -0.4316 | -0.04006 | -0.5738 | False | 0.5338 |
| HI_v0 | CWL_SEC_LOAD | 0.217 | -0.1205 | 0.5233 | True | 0.4028 |
| HI_v0 | CWL_SEC_DPSPT | N/A | N/A | N/A | False | N/A |

Seasonal asymmetry is present when correlations differ strongly between windows.

## 6. Leakage Taxonomy Assessment

### Type A

Supported. Condition variables are already present, yet condition variables explain substantial variance (max RF R2=0.6453) and residual/HI correlations remain.

### Type B

Plausible. Existing HVAC-v1 condition variables do not fully remove seasonal residual structure, suggesting important seasonal drivers may be missing or insufficiently represented.

### Type C

Supported. Correlations differ strongly between seasonal windows, including sign reversals or large magnitude shifts.

### Type D

Not primary. Condition variables explain meaningful variance, so the observed issue is more directly condition dependence than a residual definition problem alone.

Multiple leakage types may coexist. No single label was forced.

## 7. Verdict

FAIL

Strong condition dependence remains.

Leakage type can be identified.

Residual construct validity requires revision.

## 8. Implications

Failure does NOT invalidate the project.

Failure indicates:

Expected State → Residual

requires further study.

Forward validation remains suspended.

Validation D remains blocked.

No specific remediation path is assumed.

Leakage taxonomy should guide future investigation.

## 9. Visualizations

* `outputs\validation_m1_residual_condition_corr.png`
* `outputs\validation_m1_hi_condition_corr.png`
* `outputs\validation_m1_seasonal_comparison.png`
* `outputs\validation_m1_r2_summary.png`
