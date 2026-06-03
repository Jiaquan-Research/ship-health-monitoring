# Validation B2.1: Corrected Severity Ordering

- Verdict: Strong PASS
- Basis: At least 3 of 4 targets show strict monotonicity for RMS and/or AbsMean.
- Corrected order: Baseline -> 095 -> 080 -> 065
- Models: frozen Validation B1 Expected State Models. No retraining performed.
- Condition Variables: CWL_SEC_LOAD, OA_TEMP, OA_TEMP_WB, CWL_PRI_SW_TEMPSPT, CT_SW_TEMPSPT, CWL_SEC_DPSPT
- State Variables: CHL_POW_1, CHL_SW_TEMP_1, CT_SW_TEMP_1, CHL_RWCD_TEMP_1

## Dataset Filtering Summary

| Dataset | Rows Before | Rows After | Retention % |
| --- | --- | --- | --- |
| Baseline | 525540 | 525540 | 100 |
| 095 | 525540 | 525540 | 100 |
| 080 | 525540 | 525540 | 100 |
| 065 | 525540 | 525540 | 100 |

## Section 1: Residual Statistics

| Target | Dataset | Mean | Std | RMS | AbsMean | P95 |
| --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | Baseline | 0.0682649 | 7.79236 | 7.79265 | 2.5835 | 6.68148 |
| CHL_SW_TEMP_1 | Baseline | 0.00166448 | 0.169244 | 0.169252 | 0.063705 | 0.185307 |
| CT_SW_TEMP_1 | Baseline | 0.00183445 | 0.278185 | 0.27819 | 0.12531 | 0.35067 |
| CHL_RWCD_TEMP_1 | Baseline | 0.00264073 | 0.27877 | 0.278782 | 0.115802 | 0.344879 |
| CHL_POW_1 | 095 | 0.104879 | 7.82767 | 7.82836 | 2.60177 | 6.85937 |
| CHL_SW_TEMP_1 | 095 | 0.00136223 | 0.181678 | 0.181683 | 0.0665075 | 0.194897 |
| CT_SW_TEMP_1 | 095 | 0.13199 | 0.306501 | 0.333712 | 0.221194 | 0.510948 |
| CHL_RWCD_TEMP_1 | 095 | 0.0341374 | 0.300297 | 0.302231 | 0.128619 | 0.498721 |
| CHL_POW_1 | 080 | 0.309786 | 8.13003 | 8.13592 | 2.72002 | 7.93277 |
| CHL_SW_TEMP_1 | 080 | 0.00100041 | 0.186972 | 0.186975 | 0.0672935 | 0.195576 |
| CT_SW_TEMP_1 | 080 | 0.604068 | 0.522526 | 0.798706 | 0.642253 | 1.3665 |
| CHL_RWCD_TEMP_1 | 080 | 0.197557 | 0.524382 | 0.560362 | 0.246714 | 1.24893 |
| CHL_POW_1 | 065 | 0.770306 | 8.74449 | 8.77835 | 2.97231 | 10.4982 |
| CHL_SW_TEMP_1 | 065 | 0.000458823 | 0.212757 | 0.212758 | 0.0706663 | 0.20176 |
| CT_SW_TEMP_1 | 065 | 1.2557 | 0.919739 | 1.5565 | 1.2729 | 2.75886 |
| CHL_RWCD_TEMP_1 | 065 | 0.499622 | 1.02369 | 1.1391 | 0.527207 | 2.47653 |

## Section 2: Monotonicity Results

| Target | Strict AbsMean | Relaxed AbsMean | Strict RMS | Relaxed RMS | Strict P95 | Relaxed P95 |
| --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | True | True | True | True | True | True |
| CHL_SW_TEMP_1 | True | True | True | True | True | True |
| CT_SW_TEMP_1 | True | True | True | True | True | True |
| CHL_RWCD_TEMP_1 | True | True | True | True | True | True |

## Section 3: Sensitivity Ranking

| Rank | Target | Sensitivity Score |
| --- | --- | --- |
| 1 | CT_SW_TEMP_1 | 4.59509 |
| 2 | CHL_RWCD_TEMP_1 | 3.086 |
| 3 | CHL_SW_TEMP_1 | 0.257044 |
| 4 | CHL_POW_1 | 0.126491 |

## Section 4: Interpretation

### Q1: Does corrected severity ordering produce monotonic residual growth?

Yes. The corrected ordering produces monotonic residual growth for the targets and metrics shown in the monotonicity table.

### Q2: Which residual metric is most reliable?

`AbsMean` is most reliable by strict/relaxed monotonic hit count across targets.

### Q3: Which target is most sensitive?

`CT_SW_TEMP_1` has the highest sensitivity score.

### Q4: Does this support Expected State -> Residual -> Physical Degradation as a valid route?

Yes, preliminarily. Frozen-model residuals increase with corrected cooling-tower fouling severity, supporting the route within the LBNL HVAC fault family.

### Q5: Can Q2 of the Concept Paper be marked "Preliminary Supported"?

Yes. Q2 can be marked Preliminary Supported, with the caveat that this is HVAC-domain evidence and depends on corrected fault-label ordering.

## Generated Outputs

- `outputs/validation_b21_residual_statistics.csv`
- `outputs/validation_b21_filtering.csv`
- `outputs/validation_b21_monotonicity.csv`
- `outputs/validation_b21_sensitivity.csv`
- `outputs/validation_b21_residuals.csv`
- `outputs/b21_all_targets.png`
- `outputs/b21_rms_CHL_POW_1.png`
- `outputs/b21_rms_CHL_SW_TEMP_1.png`
- `outputs/b21_rms_CT_SW_TEMP_1.png`
- `outputs/b21_rms_CHL_RWCD_TEMP_1.png`