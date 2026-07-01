# Validation I-1 Negative Control

## 1. Protocol Reference

Protocol: `docs/review/negative_control_protocol_v0.1.md`

Status: executed according to pre-registered Validation I-1 protocol.

No model retraining was performed.

No new datasets were introduced.

No fault datasets were loaded.

Residuals were not recomputed.

## 2. Dataset Definition

Dataset: LBNL baseline only, `data/lbnl/ChillerPlant.csv`.

Frozen residual rows before trimming: 525,540

Healthy period definition: exclude first 5% and last 5% of baseline residual rows.

Healthy period rows after trimming and condition alignment: 472,807

Healthy period start: 2018-01-19 09:56:00

Healthy period end: 2018-12-13 18:02:00

## 3. Frozen Artifact Sources

* Residual source: `outputs\residuals_normal.csv`
* HI aggregate source: `outputs\hi_v0\hi_v0_severity_stats.csv`

The HI aggregate source contains Baseline summary rows but no time-resolved HI_v0 column. For the pre-registered time-based metric, HI_v0 was derived from the frozen `CT_SW_TEMP_1_residual_norm` series using the existing Rolling RMS formula and the existing recommended configuration: target `CT_SW_TEMP_1`, window `6h`.

Selected baseline HI stats row: HI_mean=0.02265, HI_p95=0.07093, HI_p99=0.1022.

## 4. Full-Period Metrics

| Metric | Value |
|---|---:|
| Spearman(time, HI_v0) | 0.2398 |
| Spearman(time, residual RMS) | 0.2283 |
| HI_v0 trend slope | 4.198e-08 |
| Residual RMS trend slope | 5.911e-08 |
| HI_v0 monotonicity | mixed, downward-biased (0.503 negative steps) |
| Residual RMS monotonicity | mixed, downward-biased (0.616 negative steps) |

## 5. Sub-Window Metrics

| Window | Rows | Start | End | HI Spearman | Residual RMS Spearman | HI Slope | Residual RMS Slope |
|---|---:|---|---|---:|---:|---:|---:|
| Window 1 | 157,602 | 2018-01-19 09:56:00 | 2018-05-08 20:37:00 | 0.1303 | 0.2917 | 1.132e-07 | 2.042e-07 |
| Window 2 | 157,602 | 2018-05-08 20:38:00 | 2018-08-26 07:19:00 | 0.1319 | 0.2194 | 6.826e-08 | 2.3e-07 |
| Window 3 | 157,603 | 2018-08-26 07:20:00 | 2018-12-13 18:02:00 | -0.5987 | -0.6146 | -2.631e-07 | -4.897e-07 |

## 6. Trend Attribution

OA_TEMP correlation and load correlation were computed for protocol-required trend attribution.

| Window | HI vs OA_TEMP | HI vs Load | Residual RMS vs OA_TEMP | Residual RMS vs Load |
|---|---:|---:|---:|---:|
| Full healthy period | 0.7237 | 0.5206 | 0.7811 | 0.6675 |
| Window 1 | 0.256 | 0.3595 | 0.4323 | 0.3757 |
| Window 2 | 0.07791 | -0.1596 | 0.2838 | 0.3346 |
| Window 3 | 0.7337 | 0.5285 | 0.7883 | 0.6814 |

Likely cause: condition leakage / context effect.

Trend correlated with OA_TEMP or load indicates likely condition leakage or context effect, not degradation signal.

## 7. Visualizations

* `outputs\validation_i1_hi_v0_full.png`
* `outputs\validation_i1_residual_rms.png`
* `outputs\validation_i1_conditions_overlay.png`
* `outputs\validation_i1_summary_stats.png`

## 8. Verdict

FAIL

FAIL: sub-window instability appears in healthy data.

## 9. Consequences

Failure does NOT invalidate the project.

Failure suggests:

Residual may contain:

* condition leakage;
* context effects;
* model deficiencies.

Failure indicates that
residual construct validity
must be re-examined.

Actions:

* suspend forward validation work;
* re-examine condition normalization;
* re-examine Expected State formulation;
* re-assess residual construct validity;
* Validation D remains blocked
  until I-1 passes.

No specific remediation path
is assumed.
