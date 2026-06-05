# Validation B3A: Temporal Resolution Feasibility Audit

Status: Design Only

Date: 2026-06-04

Depends On:

Validation B1 (PASS)

Validation B2.1 (STRONG PASS)

---

## 1. Research Question

Does the

Condition
-> Expected State
-> Residual
-> Physical Degradation

route remain valid when sampling frequency is reduced?

This directly addresses a critical marine deployment question:

Can lower-frequency ship data
(1h or 2h intervals)
support Health Monitoring?

---

## 2. Motivation

Current validations used:

LBNL Chiller Plant

1-minute sampling

Marine systems may provide:

* K-Chief export (1min-15min)
* Automated hourly reports
* Manual logbook records (~2h)

If the route fails below 1-minute data:

Marine deployment faces major constraints.

If the route remains valid at 1h or 2h:

Historical operational records may become usable.

---

## 3. Sampling Intervals

Apply identical resampling to ALL datasets:

Baseline

095

080

065

Resampling method:

resample().mean()

Sampling levels:

| Label | Interval | Approx Rows | Marine Analog          |
| ----- | -------- | ----------- | ---------------------- |
| 1min  | Original | 525,540     | High-frequency K-Chief |
| 15min | 15x      | ~35,036     | Typical export         |
| 1h    | 60x      | ~8,759      | Hourly report          |
| 2h    | 120x     | ~4,380      | Manual logbook         |

---

## 4. Validation Step A

Expected State Model Replication

For each sampling interval:

Train Expected State Models using:

Frozen HVAC-v1 Variable Mapping

Condition Variables:

* CWL_SEC_LOAD
* OA_TEMP
* OA_TEMP_WB
* CWL_PRI_SW_TEMPSPT
* CT_SW_TEMPSPT
* CWL_SEC_DPSPT

State Variables:

* CHL_POW_1
* CT_SW_TEMP_1
* CHL_SW_TEMP_1
* CHL_RWCD_TEMP_1

Training:

* XGBoost
* Same hyperparameters as B1
* First 80% train
* Last 20% test

Output:

| Sampling | Target | Train R2 | Test R2 | RMSE |

Important:

Models are retrained for each sampling interval.

This is intentional.

We are testing whether low-frequency data
can support Expected State Modeling.

---

## 5. Validation Step B

Residual vs Severity Replication

For each sampling interval:

Apply the corresponding Expected State Models.

Compute:

Residual

Observed - Predicted

For all datasets:

Baseline

095

080

065

Severity order:

Baseline
-> 095
-> 080
-> 065

Compute:

Residual RMS

Residual Mean

Residual P95

Check:

Strict Monotonicity

Baseline < 095 < 080 < 065

Output:

| Sampling | Target | RMS_065/RMS_baseline | Strict Monotonic |

---

## 6. Sample Count Audit

For each sampling level:

Report actual row counts.

Output:

| Sampling | Rows |

Purpose:

Differentiate:

* Temporal-resolution effects
* Sample-size effects

A reduction in performance may be caused by either.

This audit is mandatory.

---

## 7. Sensitivity Retention Audit

Define:

Retention Ratio

=

Sensitivity_sampling

/

Sensitivity_1min

For:

CT_SW_TEMP_1

CHL_SW_TEMP_1

CHL_RWCD_TEMP_1

CHL_POW_1

Output:

| Sampling | Target | Retention Ratio |

Interpretation:

1.00

No loss

0.80

20% loss

0.50

50% loss

---

## 8. Success Criteria

### Strong Evidence

2h passes:

* B1 (Expected State)
* B2.1 (Monotonicity)

AND

Retention Ratio >= 0.80

Interpretation:

Strong evidence that logbook-scale data
may be viable.

---

### Moderate Evidence

1h passes.

2h fails.

Interpretation:

Hourly monitoring likely feasible.

---

### Weak Evidence

15min passes.

1h fails.

Interpretation:

K-Chief export likely required.

---

### Failure

15min fails.

Interpretation:

Route appears dependent on high-frequency data.

---

## 9. Constraints

DO NOT:

* Introduce HI_v0
* Introduce CUSUM
* Introduce EWMA
* Introduce VIB
* Introduce Autoencoder
* Introduce Transformer
* Change HVAC-v1 variable mapping

ONLY:

* Resample data
* Retrain XGBoost
* Recompute residuals
* Repeat B1 and B2.1

---

## 10. Outputs

Create:

outputs/b3a_temporal_resolution.md

Include:

### Section 1

Sample Count Audit

### Section 2

B1 Results

R2 / RMSE

### Section 3

B2.1 Results

Monotonicity

### Section 4

Sensitivity Retention Audit

### Section 5

Conclusion

Answer:

Q1

How far can sampling frequency be reduced
before Expected State performance degrades?

Q2

How far can sampling frequency be reduced
before degradation detection fails?

Q3

What is the minimum viable sampling interval?

Q4

Do results support future Marine deployment?

---

## 11. Expected Outcome (Hypothesis)

Hypothesis:

1h will pass.

2h may pass.

Reasoning:

Performance degradation evolves slowly.

Controller noise is averaged out at lower frequency.

Temperature and efficiency trends should remain visible.

---

## 12. Deferred Work

Not part of B3A:

* HI_v0 validation under low-frequency sampling
* HealthScore construction
* Multivariate HI
* Trend prediction

These belong to:

Validation B3B

and later stages.

---

## Version History

v0.2

Added:

* Four-state-variable validation
* Sample count audit
* Sensitivity retention audit
* Conservative interpretation criteria
