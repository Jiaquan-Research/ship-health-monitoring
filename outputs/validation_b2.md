# Validation B2: Residual Severity Analysis

- Verdict: Fail
- Basis: Residual metrics do not separate severity levels reliably.
- Models: frozen Validation B1 Expected State Models. No retraining performed.
- Condition Variables: CWL_SEC_LOAD, OA_TEMP, OA_TEMP_WB, CWL_PRI_SW_TEMPSPT, CT_SW_TEMPSPT, CWL_SEC_DPSPT
- State Variables: CHL_POW_1, CHL_SW_TEMP_1, CT_SW_TEMP_1, CHL_RWCD_TEMP_1

## Section 1: Dataset Filtering Summary

| Dataset | Rows Before | Rows After | Retention % |
| --- | --- | --- | --- |
| Baseline | 525540 | 525540 | 100 |
| 065 | 525540 | 525540 | 100 |
| 080 | 525540 | 525540 | 100 |
| 095 | 525540 | 525540 | 100 |

## Section 2: Residual Statistics

| Target | Dataset | Mean | Std | RMS | AbsMean | P95 |
| --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | Baseline | 0.0682649 | 7.79236 | 7.79265 | 2.5835 | 6.68148 |
| CHL_SW_TEMP_1 | Baseline | 0.00166448 | 0.169244 | 0.169252 | 0.063705 | 0.185307 |
| CT_SW_TEMP_1 | Baseline | 0.00183445 | 0.278185 | 0.27819 | 0.12531 | 0.35067 |
| CHL_RWCD_TEMP_1 | Baseline | 0.00264073 | 0.27877 | 0.278782 | 0.115802 | 0.344879 |
| CHL_POW_1 | 065 | 0.770306 | 8.74449 | 8.77835 | 2.97231 | 10.4982 |
| CHL_SW_TEMP_1 | 065 | 0.000458823 | 0.212757 | 0.212758 | 0.0706663 | 0.20176 |
| CT_SW_TEMP_1 | 065 | 1.2557 | 0.919739 | 1.5565 | 1.2729 | 2.75886 |
| CHL_RWCD_TEMP_1 | 065 | 0.499622 | 1.02369 | 1.1391 | 0.527207 | 2.47653 |
| CHL_POW_1 | 080 | 0.309786 | 8.13003 | 8.13592 | 2.72002 | 7.93277 |
| CHL_SW_TEMP_1 | 080 | 0.00100041 | 0.186972 | 0.186975 | 0.0672935 | 0.195576 |
| CT_SW_TEMP_1 | 080 | 0.604068 | 0.522526 | 0.798706 | 0.642253 | 1.3665 |
| CHL_RWCD_TEMP_1 | 080 | 0.197557 | 0.524382 | 0.560362 | 0.246714 | 1.24893 |
| CHL_POW_1 | 095 | 0.104879 | 7.82767 | 7.82836 | 2.60177 | 6.85937 |
| CHL_SW_TEMP_1 | 095 | 0.00136223 | 0.181678 | 0.181683 | 0.0665075 | 0.194897 |
| CT_SW_TEMP_1 | 095 | 0.13199 | 0.306501 | 0.333712 | 0.221194 | 0.510948 |
| CHL_RWCD_TEMP_1 | 095 | 0.0341374 | 0.300297 | 0.302231 | 0.128619 | 0.498721 |

## Section 3: Monotonic Severity Test

| Target | Strict AbsMean | Relaxed AbsMean | Strict RMS | Relaxed RMS | Strict P95 | Relaxed P95 |
| --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | False | False | False | False | False | False |
| CHL_SW_TEMP_1 | False | False | False | False | False | False |
| CT_SW_TEMP_1 | False | False | False | False | False | False |
| CHL_RWCD_TEMP_1 | False | False | False | False | False | False |

## Section 4: Sensitivity Ranking

| Rank | Target | Sensitivity Score |
| --- | --- | --- |
| 1 | CT_SW_TEMP_1 | 0.199583 |
| 2 | CHL_RWCD_TEMP_1 | 0.0841134 |
| 3 | CHL_SW_TEMP_1 | 0.0734446 |
| 4 | CHL_POW_1 | 0.00458283 |

## Section 5: Interpretation

### Q1: Do residuals increase when fouling severity increases?

No. Residual RMS does not increase consistently enough to indicate severity separation.

### Q2: Does strict monotonicity hold?

No. Baseline < 065 < 080 < 095 does not hold strictly across the tested residual metrics.

### Q3: Does relaxed monotonicity hold?

No. Relaxed monotonicity does not hold for the evaluated metrics.

### Q4: Which target is most sensitive?

`CT_SW_TEMP_1` has the highest sensitivity score.

### Q5: Does this support Expected State -> Residual -> Degradation as a valid monitoring route?

No. The tested residual metrics are insufficient to support the degradation route for this fault family.

### Q6: Can a simple HI_v0 be justified?

No. A simple HI_v0 is not justified until residual severity separation is demonstrated.

## Generated Outputs

- `outputs/validation_b2_residual_statistics.csv`
- `outputs/validation_b2_filtering.csv`
- `outputs/validation_b2_monotonicity.csv`
- `outputs/validation_b2_sensitivity.csv`
- `outputs/validation_b2_residuals.csv`
- `outputs/b2_all_targets_comparison.png`
- `outputs/b2_rms_CHL_POW_1.png`
- `outputs/b2_rms_CHL_SW_TEMP_1.png`
- `outputs/b2_rms_CT_SW_TEMP_1.png`
- `outputs/b2_rms_CHL_RWCD_TEMP_1.png`