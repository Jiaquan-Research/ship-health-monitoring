# Attack Review Summary v1

Date:

2026-06-10

Status:

Review Layer Convergence

---

## 1. Scope

This document summarizes three independent
adversarial reviews.

Goal:

Identify:

* which attacks are valid;
* which claims survive;
* what remains unresolved.

This document preserves criticism.

It is not a defense.

---

## 2. Round 1 Summary

Focus:

Experimental design.

Main findings:

### Valid attacks

* B2 initially failed.
* Severity ordering was corrected post-hoc.
* HI_v0 improvement was concentrated on
  CT_SW_TEMP_1.
* Internal evidence strength was overstated.

### Impact

C1:

Strong → Moderate

C2:

Strong → Moderate

C3:

Moderate → Initial

---

## 3. Round 2 Summary

Focus:

Methodology.

Main findings:

### Valid attacks

Pseudo degradation ordering

≠

Temporal degradation.

Maintenance effects are:

* partial;
* overlapping;
* ambiguous.

Trend interpretation is indirect.

Baseline reset semantics remain unresolved.

### Impact

C4:

Removed from Claim Registry.

Trend becomes an Open Question.

C5:

Downgraded to Open Problem.

---

## 4. Fable5 Review Summary

Focus:

Validation framework itself.

Main findings:

### Valid attacks

Current PASS results originate from tests
with limited falsification power.

4-point monotonicity and Spearman rho=1.0
are structurally easy to satisfy.

Negative controls are missing.

Healthy-data false-positive behavior
remains unknown.

Residual construct validity remains unproven.

### Impact

Current evidence should be interpreted as:

Pipeline mechanics demonstrated on
two simulation domains.

Not:

Strong cross-domain evidence.

---

## 5. Internal Validation Sequence

Timeline:

I-1

↓

M-1

↓

M-1A

↓

E-1

---

## I-1 Negative Control

Result:

FAIL

Main finding:

Healthy trajectories exhibited apparent trends.

Strong correlation with:

OA_TEMP

CWL_SEC_LOAD

Interpretation:

Likely condition leakage rather than genuine degradation trend.

No claim upgrades.

---

## M-1 Condition Leakage Audit

Result:

FAIL

Main finding:

Strong condition dependence remains.

Random Forest:

Residual RMS ~ Conditions

R² ≈ 0.379

HI_v0 ~ Conditions

R² ≈ 0.645

Interpretation:

Residual and HI still contain condition information.

Type D not considered primary.

---

## M-1A Type Separation

Result:

Type C dominant.

Type B moderate.

Type A not supported.

Type D not primary.

Interpretation:

Cross-regime instability appears to be the major source of leakage.

No remediation performed.

No conclusions upgraded.

---

## Exploratory E-1

Status:

Exploratory only.

Not a validation.

Not evidence.

Result:

No obvious instability observed.

N-CMAPSS same-window:

R² ≈ 0.9988

Cross-window:

R² ≈ 0.9161

Interpretation:

Performance degradation exists but HVAC-style collapse was not observed.

No universality implied.

---

## Emergence of Q0

A new exploratory question appeared:

Global Mapping ?

vs

Piecewise Mapping ?

Q0 is not part of the Claim Registry.

Q0 is not supported by evidence.

Q0 should remain speculative.

---

## Overall Status

Current understanding:

The original engineering pipeline remains alive.

However,

Expected State stability became the dominant unresolved problem.

Current priority:

Understand Type C.

Validation D remains blocked.

No claim upgrades are justified.

---

## 6. Surviving Structure

Current structure surviving all reviews:

Condition

↓

Expected State

↓

Residual

↓

HI

Evidence level:

C1

Moderate Evidence

C2

Moderate Evidence

C3

Initial Evidence

These remain provisional.

Note: C1 and C2 evidence comes entirely from
simulation data (LBNL EnergyPlus-Modelica co-simulation
and N-CMAPSS NASA simulation). Neither dataset
represents a real machine under real operating conditions.
"Moderate Evidence" in this context means:
pipeline mechanics behave as expected on two simulators.
It does not imply that real-world transfer is likely
or that the evidence level would survive on real machinery.

Marine validation has not yet occurred.

---

## 7. Open Problems

### OP-1

Residual construct validity.

Main question:

Does residual contain health information,
or condition leakage?

---

### OP-2

Trend interpretation.

Main question:

Does ordering information imply
temporal degradation?

---

### OP-3

Baseline Management.

Main question:

How should maintenance resets be handled?

---

### OP-4

Marine transfer.

Main question:

Will the pipeline survive real machinery?

---

## 8. Current Project Status

Current understanding:

"In two industrial simulation datasets,
the pipeline behaves as expected under
known degradation scenarios.

This is a necessary prerequisite.

It is not sufficient evidence for
real-world deployment."

Current status is NOT:

"Strong cross-domain evidence established."

---

## 9. Current Highest-Priority Question

I-1 (Negative Control) and M-1 (Condition Leakage Audit)
have both been executed and returned FAIL.
M-1A (Type Separation) identified Type C
(cross-regime instability) as the dominant mechanism.

Executed sequence:

I-1 FAIL -> M-1 FAIL -> M-1A: Type C dominant -> E-1: no collapse on N-CMAPSS

Current unresolved question:

Q0:

Is the Expected State model fundamentally
a Global Mapping or a Piecewise Mapping?

This question emerged from M-1A findings.
It remains exploratory with very low evidence.
It is NOT part of the Claim Registry.
It is NOT a validated claim.
It is an observation-driven research question only.

Current priority:

Understand Type C through Dataset Zoo observation.

Validation D remains blocked until
Expected State stability is resolved.

No claim upgrades are justified at this stage.

---

## 10. Philosophy

Every PASS should correspond to
a test that could genuinely FAIL.

Unknown remains a valid outcome.

Deletion is acceptable.

Open Problems are preferable to
overstated conclusions.

---

## Version History

v1

2026-06-10

Initial convergence summary.

v1.1

2026-06-11

Section 9 updated to reflect I-1/M-1/M-1A/E-1
execution results. Q0 documented as exploratory
question. Current priority updated to Dataset Zoo
observation for Type C understanding.
