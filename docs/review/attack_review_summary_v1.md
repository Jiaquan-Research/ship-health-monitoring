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

## 5. Surviving Structure

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

## 6. Open Problems

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

## 7. Current Project Status

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

## 8. Highest-Priority Next Question

Q:

Can residual and HI remain stable
on healthy trajectories?

This question has not yet been tested.

A negative-control protocol is required.

Specifically: apply the frozen Expected State model
to healthy-only data with known operating-condition
variation and no fault injection.
If residual or HI shows an upward trend during
confirmed healthy periods, this indicates that
condition normalization is incomplete and that
operating-condition variation is leaking into
the residual signal.
If this test fails, the entire chain from
Residual → HI → Trend is contaminated at the source,
and no downstream validation (including Validation D)
will be interpretable until condition normalization
is fixed.
This is the single test that must be run
before any further validation work.

---

## 9. Philosophy

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
