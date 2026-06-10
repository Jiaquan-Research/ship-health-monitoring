# Validation M-1 Postmortem

Date:

2026-06-10

Status:

FAIL

---

## 1. Purpose

Validation M-1 was designed as a
Condition Leakage Audit.

Question:

Why do residual and HI remain
correlated with condition variables
despite those variables already being
included in the Expected State model?

The experiment followed:

docs/review/m1_condition_leakage_protocol_v0.1.md

No retraining was performed.

No new datasets were introduced.

No remediation was attempted.

---

## 2. Verdict

FAIL

Reason:

Strong condition dependence remains.

Leakage type can be identified.

Residual construct validity requires
further study.

---

## 3. Main Findings

Strong full-period correlations remain.

Examples:

Residual RMS vs OA_TEMP_WB

≈ 0.776

Residual RMS vs OA_TEMP

≈ 0.763

HI_v0 vs OA_TEMP

≈ 0.699

HI_v0 vs CT_SW_TEMPSPT

≈ 0.715

These values indicate that
condition information remains
inside residual and HI.

---

## 4. Variance Explanation

Random Forest explanatory models show:

Residual RMS

R² ≈ 0.379

HI_v0

R² ≈ 0.645

Therefore:

Condition variables explain
substantial variance.

Condition leakage is real.

---

## 5. Seasonal Effects

Correlations are not stationary.

Example:

HI_v0 vs OA_TEMP

Window 1

≈ 0.03

Window 2

≈ 0.11

Window 3

≈ 0.67

Seasonal asymmetry is present.

This supports the existence of
season-dependent behavior.

---

## 6. Leakage Taxonomy Assessment

### Type A

Supported.

Condition variables are already present.

Yet residual and HI remain strongly
correlated with them.

---

### Type B

Plausible.

Additional seasonal drivers may exist.

Current variables may be incomplete.

---

### Type C

Supported.

Correlation structure changes
between seasonal windows.

Evidence suggests
distribution shift or extrapolation effects.

---

### Type D

Not primary.

Condition variables explain
meaningful variance.

Observed failure appears more related
to condition dependence than to
Residual definition itself.

---

Multiple leakage types may coexist.

No single label was forced.

---

## 7. Relationship to Validation I-1

Validation I-1 showed:

Healthy trajectories exhibit trend.

M-1 identifies the likely source:

Condition leakage.

Therefore:

I-1 and M-1 are consistent.

---

## 8. Relationship to Fable5 Review

Fable5 proposed:

Residual may contain condition
information rather than pure
health information.

Validation M-1 partially confirms
this concern.

However:

Type D is not the dominant explanation.

Evidence currently supports:

Health information

*

Condition leakage

rather than:

Condition information only.

---

## 9. Project Impact

Forward validation remains suspended.

Validation D remains blocked.

Expected State → Residual becomes
the highest-priority layer.

Further diagnosis is required.

No remediation path is assumed.

---

## 10. What M-1 Does NOT Show

M-1 does NOT prove:

that the pipeline is invalid.

M-1 does NOT prove:

that HI has no value.

M-1 does NOT prove:

that Expected State formulation
is fundamentally wrong.

M-1 only demonstrates:

Condition information remains
inside residual and HI.

---

## 11. Next Question

M-1A

Type Separation Audit

Question:

Among:

Type A

Type B

Type C

which mechanism dominates?

Current evidence:

Type A

supported

Type C

supported

Type B

plausible

Type D

not primary

---

## 12. Lessons Learned

Validation M-1 became the second
pre-registered experiment to fail.

No thresholds were changed.

No variables were removed.

No post-hoc reinterpretation occurred.

Failure was accepted.

Understanding increased.

---

Version History

v1

2026-06-10

Initial postmortem.
