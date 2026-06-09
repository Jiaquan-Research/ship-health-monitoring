# Independent Review Checklist v0.1

Date: 2026-06-09

Status:

Open

Purpose:

Facilitate independent review.

Agreement is unnecessary.

Criticism is encouraged.

---

# Section 1 — Overall Assessment

Do you believe the project currently provides:

[ ] Strong support

[ ] Moderate support

[ ] Weak support

[ ] No support

Comments:

---

---

# Section 2 — Claim-by-Claim Review

## C1

Condition → Expected State

Current project assessment:

Moderate Evidence

Reviewer opinion:

[ ] Maintain

[ ] Downgrade

[ ] Reject

Main concerns:

* Hidden leakage
* Limited operating regimes
* Controller-dominated dynamics
* Other

### Evidence Source

HVAC Validation B1

R²≈0.97

N-CMAPSS C0.2

R²≈0.99

Scope:

HVAC and Aero-engine simulation only.

Marine transfer remains unvalidated.

Comments:

---

---

## C2

Expected State → Residual

Current project assessment:

Moderate Evidence

Reviewer opinion:

[ ] Maintain

[ ] Downgrade

[ ] Reject

Main concerns:

* Post-hoc severity ordering
* Label semantics
* Sensor selection bias
* Other

### Evidence Source

HVAC B2.1

Residual severity ordering

N-CMAPSS C0.2

Residual vs HPT_eff_mod

Scope:

Dependent on label semantics.

Marine evidence unavailable.

Comments:

---

---

## C3

Residual → HI

Current project assessment:

Initial Evidence

Reviewer opinion:

[ ] Maintain

[ ] Downgrade

[ ] Reject

Main concerns:

* HI comparator missing
* Rolling RMS merely smooths noise
* Internal inconsistency
* Other

### Evidence Source

HI_v0

HVAC

N-CMAPSS C0.2

Current status:

Initial Evidence

Comparator family not yet explored.

Comments:

---

---

## C4

Residual → Trend

Current project assessment:

Initial Evidence

Reviewer opinion:

[ ] Maintain

[ ] Downgrade

[ ] Reject

Main concerns:

* Pseudo-degradation
* Lack of real temporal evidence
* Other

### Evidence Source

HVAC B4

Pseudo-degradation path

Current status:

Initial Evidence

No real temporal degradation evidence.

Comments:

---

---

## C5

Baseline Management

Current project assessment:

Hypothesis

Reviewer opinion:

[ ] Maintain

[ ] Downgrade

[ ] Reject

Main concerns:

* Segment logic
* Re-stationarization assumptions
* Maintenance semantics
* Other

### Evidence Source

baseline_management_v0.2

Cross-industry literature review

Current status:

Hypothesis

No maintenance-event evidence.

Comments:

---

---

# Section 3 — Alternative Explanations

Can the observations be explained by:

[ ] Hidden leakage

[ ] Control policy effects

[ ] Dataset bias

[ ] Low-dimensional manifolds

[ ] Selection bias

[ ] Overfitting

[ ] Other

Comments:

---

---

# Section 4 — Most Vulnerable Claim

Which claim appears weakest?

[ ] C1

[ ] C2

[ ] C3

[ ] C4

[ ] C5

Reason:

---

---

# Section 5 — Suggested Experiments

What experiment would you run first to challenge the project?

Example directions

Possible review experiments:

* Test Expected State model on Marine generator data.

* Verify B2 severity ordering using external metadata.

* Compare HI_v0 with:

  EWMA

  CUSUM

  Trend slope

* Examine maintenance events and re-stationarization.

These examples are suggestions only.

Reviewers are free to propose different experiments.

---

---

# Section 6 — Missing Evidence

What evidence is currently missing?

---

---

# Section 7 — Final Recommendation

Overall recommendation:

[ ] Maintain current assessment

[ ] Downgrade some claims

[ ] Reject major claims

[ ] Insufficient evidence

Comments:

---

---

# Review Philosophy

Agreement is not required.

The project benefits from criticism.

Disconfirmation attempts are encouraged.
