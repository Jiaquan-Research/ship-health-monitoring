---

# HI_v0 Design Document

**Status:** Design only. No implementation yet.

**Date:** 2026-06-04

**Based on:** Validation B1 and B2.1 results (LBNL Chiller Plant)

---

## 1. Research Question

Q3: Can a Health Indicator be constructed from Residual?

This document defines the design of HI_v0,

the first candidate Health Indicator for the

Ship Health Monitoring pipeline.

---

## 2. Evidence Basis

HI_v0 is designed directly from validated experimental results.

No assumptions are made beyond what the data supports.

| Finding | Source | Status |

|---------|--------|--------|

| Condition Variables predict State Variables (R²=0.970~0.993) | Validation B1 | Confirmed |

| Residual increases monotonically with fault severity | Validation B2.1 | Confirmed |

| CT_SW_TEMP_1 has highest fault sensitivity (Score=4.60) | Validation B2.1 | Confirmed |

| CHL_SW_TEMP_1 has cleanest baseline (Residual Std=0.169) | Validation B1 | Confirmed |

These two variables have different properties and serve

different roles:

- CT_SW_TEMP_1: high sensitivity, strong fault response

- CHL_SW_TEMP_1: clean baseline, low false positive risk

Both are included in HI_v0.

---

## 3. HI_v0 Definition

### Core Formula

```

HI_v0 = Rolling RMS of normalized residual

```

Step by step:

```

Step 1: residual = observed - predicted

        (from frozen B1 Expected State Models)



Step 2: residual_norm = residual / TrainStd(target)

        (same normalization used in B2.1)



Step 3: HI_v0(t) = RMS of residual_norm

        over rolling window W

```

### Candidate Targets

| Name | Target Variable | Primary Property |

|------|----------------|-----------------|

| HI_v0A | CT_SW_TEMP_1 | Highest fault sensitivity |

| HI_v0B | CHL_SW_TEMP_1 | Cleanest baseline |

| HI_v0C | CHL_RWCD_TEMP_1 | Second highest sensitivity |

| HI_v0D | CHL_POW_1 | Reference (lowest sensitivity) |

All four targets will be computed for comparison.

Primary focus: HI_v0A and HI_v0B.

### Rolling Window

Primary window: W = 24 hours (1440 rows at 1-min sampling)

Sensitivity comparison windows:

- W = 6 hours

- W = 12 hours

- W = 24 hours

- W = 48 hours

Rationale: window size controls the trade-off between

noise suppression and response speed. The optimal window

is determined by data, not by assumption.

---

## 4. HI_z: Baseline-Referenced Score

After computing HI_v0, a baseline-referenced score

is derived to enable threshold-based detection:

```

HI_z(t) = (HI_v0(t) - baseline_mean) / baseline_std

```

Where baseline_mean and baseline_std are computed

from the normal operating period (Baseline dataset).

Note: HI_z is a z-score, NOT a 0-1 normalized value.

A HealthScore (0-100 scale) is deferred to a later design stage.

---

## 5. Threshold Candidates

Thresholds are NOT frozen in this version.

The following candidates will be evaluated empirically

after HI_v0 is computed on the fault datasets:

| Threshold | Definition | Type |

|-----------|-----------|------|

| P95 | 95th percentile of baseline HI_v0 | Quantile |

| P99 | 99th percentile of baseline HI_v0 | Quantile |

| mean + 2std | Baseline mean + 2 standard deviations | Parametric |

| mean + 4std | Baseline mean + 4 standard deviations | Parametric |

Baseline residual distribution may not be Gaussian.

Rolling RMS distribution is likely not Gaussian.

Therefore quantile thresholds (P95, P99) are preferred

over parametric thresholds.

Final threshold selection requires visual inspection

of baseline HI_v0 distribution after implementation.

---

## 6. Validation Plan

HI_v0 will be validated using the same fault severity

ordering established in Validation B2.1:

```

Baseline → 095 → 080 → 065

(weakest fouling → strongest fouling)

```

### Metrics

For each target and each dataset:

| Metric | Definition |

|--------|-----------|

| HI mean | Mean of HI_v0 over full dataset |

| HI P95 | 95th percentile of HI_v0 |

| HI P99 | 99th percentile of HI_v0 |

| HI_z mean | Mean of HI_z over full dataset |

| Monotonicity | Strict: Baseline < 095 < 080 < 065 |

| Baseline exceedance rate | % of baseline points exceeding P95 threshold |

### Success Criteria

Strong PASS:

- At least 3 of 4 targets show strict monotonicity

  for HI mean and/or HI P95

- Baseline exceedance rate < 5% at P95 threshold

Moderate PASS:

- HI_v0A (CT_SW_TEMP_1) shows clear monotonic response

- Baseline exceedance rate < 10%

Fail:

- HI_v0 does not separate severity levels

  more clearly than raw residual

Note: if HI_v0 performs no better than raw residual RMS

from B2.1, the Rolling RMS formulation should be reconsidered.

HI_v0 must add value over the B2.1 baseline.

The validation must explicitly compare raw residual RMS

against HI_v0 Rolling RMS.

If HI_v0 does not provide more stable monotonicity

and lower baseline exceedance, it cannot be treated

as an improvement over raw residual metrics.

---

## 7. What HI_v0 Is NOT

- Not a final health score (no 0-100 scale in this version)

- Not a multivariate system-level indicator

- Not a long-term trend tracker (that is Q4, not Q3)

- Not validated for Marine systems (HVAC domain only)

- Not validated against natural degradation

  (fault injection data only)

---

## 8. Multivariate HI (Deferred)

Multivariate HI is deferred until single-variable

HI_v0 is validated.

When implemented, candidate weighting approaches:

- Sensitivity score from B2.1 (data-driven)

- Baseline noise level (inverse of Residual Std)

- Domain criticality (engineering judgment)

No weights are defined at this stage.

---

## 9. Open Questions

These questions are NOT answered by HI_v0 design.

They require implementation and validation.

| Question | How to answer |

|----------|--------------|

| What window size W is optimal? | Compare W=6/12/24/48h on fault data |

| Which threshold is most reliable? | Compare P95/P99/2std/4std on baseline |

| Does HI_v0 add value over raw residual? | Compare monotonicity scores |

| Is HI_v0A or HI_v0B more useful? | Compare sensitivity vs false positive rate |

| How does sampling frequency affect HI_v0? | Validation B3 (Temporal Resolution Audit) |

---

## 10. Implementation Notes (for Codex)

When implementing HI_v0:

1. Load frozen B2.1 residual_norm from:

   outputs/validation_b21_residuals.csv

2. Do NOT recompute residuals.

   Use the frozen B2.1 outputs directly.

3. Compute Rolling RMS for each target and each window.

4. Save outputs to:

   outputs/hi_v0/

5. Create validation report:

   outputs/hi_v0_validation.md

6. Do NOT implement HealthScore (0-100 scale).

   Do NOT implement multivariate aggregation.

   Do NOT implement CUSUM in this version.

---

## Version History

| Version | Date | Change |

|---------|------|--------|

| v0.1 | 2026-06-04 | Initial design. Based on B1/B2.1 results. |
