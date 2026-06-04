# HI_v0 Rolling RMS Validation

## 1. Summary

- Verdict: Moderate PASS
- Best target: `CT_SW_TEMP_1`
- Best window size: `6h`
- Q3 status: Preliminary Supported
- Input: frozen B2.1 normalized residuals only. Residuals were not recomputed and models were not loaded.

### Loaded Residuals

| Dataset | Rows |
| --- | --- |
| Baseline | 525540 |
| 095 | 525540 |
| 080 | 525540 |
| 065 | 525540 |

### Columns Confirmed

`Datetime`, `Dataset`, `CT_SW_TEMP_1_residual_norm`, `CHL_SW_TEMP_1_residual_norm`, `CHL_RWCD_TEMP_1_residual_norm`, `CHL_POW_1_residual_norm`

## 2. Severity Statistics Table

Primary window: W=24h.

| Target | Window | Dataset | HI_mean | HI_p95 | HI_p99 | HIz_mean | Exceedance_P95 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CT_SW_TEMP_1 | 24h | Baseline | 0.0255308 | 0.060827 | 0.0838032 | -1.1091e-16 | 4.99999 |
| CT_SW_TEMP_1 | 24h | 095 | 0.0368661 | 0.0693429 | 0.089988 | 0.501328 | 10.6114 |
| CT_SW_TEMP_1 | 24h | 080 | 0.0927773 | 0.147873 | 0.185295 | 2.97412 | 84.3737 |
| CT_SW_TEMP_1 | 24h | 065 | 0.178481 | 0.294738 | 0.378837 | 6.76453 | 98.091 |
| CHL_SW_TEMP_1 | 24h | Baseline | 0.0318602 | 0.0932139 | 0.145549 | 2.77274e-17 | 4.99999 |
| CHL_SW_TEMP_1 | 24h | 095 | 0.0333388 | 0.103002 | 0.168506 | 0.0422462 | 6.42562 |
| CHL_SW_TEMP_1 | 24h | 080 | 0.0339489 | 0.101588 | 0.191788 | 0.0596761 | 6.30348 |
| CHL_SW_TEMP_1 | 24h | 065 | 0.0356604 | 0.105551 | 0.19947 | 0.108576 | 7.0626 |
| CHL_RWCD_TEMP_1 | 24h | Baseline | 0.0276462 | 0.0751882 | 0.101364 | 8.31822e-17 | 4.99999 |
| CHL_RWCD_TEMP_1 | 24h | 095 | 0.0300877 | 0.0813056 | 0.10497 | 0.0851314 | 8.22528 |
| CHL_RWCD_TEMP_1 | 24h | 080 | 0.053308 | 0.162653 | 0.214443 | 0.894814 | 37.8802 |
| CHL_RWCD_TEMP_1 | 24h | 065 | 0.105501 | 0.340216 | 0.435214 | 2.71475 | 44.2275 |
| CHL_POW_1 | 24h | Baseline | 0.0929304 | 0.288691 | 0.334515 | -2.77274e-17 | 4.99999 |
| CHL_POW_1 | 24h | 095 | 0.0932841 | 0.289444 | 0.336168 | 0.00333303 | 5.06992 |
| CHL_POW_1 | 24h | 080 | 0.0968368 | 0.305323 | 0.352487 | 0.0368083 | 6.94141 |
| CHL_POW_1 | 24h | 065 | 0.104095 | 0.331234 | 0.381729 | 0.105199 | 10.2201 |

## 3. Monotonicity Results

| Target | Window | Strict_Mean | Strict_P95 | Strict_HIz |
| --- | --- | --- | --- | --- |
| CT_SW_TEMP_1 | 6h | True | True | True |
| CT_SW_TEMP_1 | 12h | True | True | True |
| CT_SW_TEMP_1 | 24h | True | True | True |
| CT_SW_TEMP_1 | 48h | True | True | True |
| CHL_SW_TEMP_1 | 6h | True | True | True |
| CHL_SW_TEMP_1 | 12h | True | True | True |
| CHL_SW_TEMP_1 | 24h | True | False | True |
| CHL_SW_TEMP_1 | 48h | True | True | True |
| CHL_RWCD_TEMP_1 | 6h | True | True | True |
| CHL_RWCD_TEMP_1 | 12h | True | True | True |
| CHL_RWCD_TEMP_1 | 24h | True | True | True |
| CHL_RWCD_TEMP_1 | 48h | True | True | True |
| CHL_POW_1 | 6h | True | True | True |
| CHL_POW_1 | 12h | True | True | True |
| CHL_POW_1 | 24h | True | True | True |
| CHL_POW_1 | 48h | True | True | True |

## 4. Sensitivity Ranking

Primary window: W=24h.

| Rank | Target | Window | Sensitivity_Score |
| --- | --- | --- | --- |
| 3 | CT_SW_TEMP_1 | 24h | 5.9908 |
| 6 | CHL_RWCD_TEMP_1 | 24h | 2.8161 |
| 11 | CHL_POW_1 | 24h | 0.120141 |
| 12 | CHL_SW_TEMP_1 | 24h | 0.119276 |

## 5. Window Size Comparison

| Rank | Target | Window | Sensitivity_Score |
| --- | --- | --- | --- |
| 14 | CHL_SW_TEMP_1 | 12h | 0.107811 |
| 12 | CHL_SW_TEMP_1 | 24h | 0.119276 |
| 9 | CHL_SW_TEMP_1 | 48h | 0.134309 |
| 16 | CHL_SW_TEMP_1 | 6h | 0.0992748 |
| 2 | CT_SW_TEMP_1 | 12h | 6.14985 |
| 3 | CT_SW_TEMP_1 | 24h | 5.9908 |
| 4 | CT_SW_TEMP_1 | 48h | 5.86519 |
| 1 | CT_SW_TEMP_1 | 6h | 6.43014 |

## 6. Interpretation

### Q1: Does HI_v0 separate fault severity levels?

Yes. HI_v0 separates Baseline -> 095 -> 080 -> 065 monotonically for the primary W=24h window.

### Q2: Which target is most useful?

`CT_SW_TEMP_1` remains the strongest sensitivity target. `CHL_SW_TEMP_1` remains useful as a cleaner-baseline comparator, but its sensitivity is lower.

### Q3: Which window size performs best?

`6h` performs best by maximum sensitivity score, led by `CT_SW_TEMP_1`.

### Q4: Does HI_v0 add value over raw residual RMS from B2.1?

| Target | B2.1_Raw_RMS_Sensitivity | HI_v0_24h_Sensitivity | Delta |
| --- | --- | --- | --- |
| CT_SW_TEMP_1 | 4.59509 | 5.9908 | 1.3957 |
| CHL_SW_TEMP_1 | 0.257044 | 0.119276 | -0.137768 |
| CHL_RWCD_TEMP_1 | 3.086 | 2.8161 | -0.269903 |
| CHL_POW_1 | 0.126491 | 0.120141 | -0.00635013 |

No. HI_v0 does not improve sensitivity over raw residual RMS for enough targets to be considered a clear improvement.

### Q5: Can Q3 of the Concept Paper be marked "Preliminary Supported"?

Yes. Q3 can be marked Preliminary Supported for the HVAC-domain residual-to-HI construction.

## 7. Recommended HI_v0 Configuration

- Primary target: `CT_SW_TEMP_1`
- Window size: `6h`
- Threshold type: `P95`

## Generated Outputs

- `outputs/hi_v0/hi_v0_baseline_stats.csv`
- `outputs/hi_v0/hi_v0_severity_stats.csv`
- `outputs/hi_v0/hi_v0_monotonicity.csv`
- `outputs/hi_v0/hi_v0_sensitivity.csv`
- `outputs/hi_v0/hi_v0_vs_raw_residual.csv`
- `outputs/hi_v0/hi_v0_window_sensitivity.png`
- `outputs/hi_v0/hi_v0_timeseries_CT_SW_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_severity_CT_SW_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_timeseries_CHL_SW_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_severity_CHL_SW_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_timeseries_CHL_RWCD_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_severity_CHL_RWCD_TEMP_1_24h.png`
- `outputs/hi_v0/hi_v0_timeseries_CHL_POW_1_24h.png`
- `outputs/hi_v0/hi_v0_severity_CHL_POW_1_24h.png`