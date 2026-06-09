# Falsification Protocol v0.1

Date: 2026-06-09

Status:

Open

Source:

* claim_registry_v0.1.md
* deep_research_attack_protocol_v0.1.md
* attack_review_round1.md

Purpose:

Describe how each claim may fail.

Agreement is unnecessary.

---

## Evidence Strength Interpretation

Strong Evidence ≠ truth

Moderate Evidence ≠ truth

Initial Evidence ≠ truth

Hypothesis ≠ truth

All claims remain falsifiable.

---

# F1 — C1

Condition → Expected State

Current Strength:

Moderate Evidence

Current Confidence:

Medium

Reason:

Cross-domain support exists,
but controller-policy explanations have not been excluded.

---

Specific attack from Round 1 review:

High R² may arise from controller policy learning
rather than transferable physics.

HVAC:

* CWL_SEC_DPSPT nearly constant
* CHL_STA_1 always = 1
* single chronological 80/20 split on autocorrelated series

N-CMAPSS:

* per-unit training
* no cross-unit transfer test

---

Potential weakness:

High R² may depend on:

* control-dominated systems
* low-dimensional manifolds
* limited operating regimes

---

Falsification criterion:

Marine generator data:

Held-out R² < 0.5

or

No stable Condition Variables exist.

or

Cross-unit transfer fails systematically.

---

Interpretation:

Marine transfer of C1 fails.

Non-Marine evidence remains valid.

---

Required action:

Downgrade C1.

---

# F2 — C2

Expected State → Residual

Current Strength:

Moderate Evidence

Current Confidence:

Low-Medium

Reason:

B2.1 contains post-hoc ordering risk.

---

Specific attack from Round 1 review:

B2 initially FAIL.

B2.1 PASS only after severity ordering changed.

Order:

095 → 080 → 065

was inferred from observed data patterns,
not pre-registered from simulator metadata.

---

Potential weakness:

Residual separation may depend on
post-hoc label interpretation.

---

Falsification criterion:

Residual cannot separate healthy and degraded states
when external severity semantics are independently known.

or

Residual separation disappears on independent datasets.

---

Interpretation:

C2 weakened or rejected.

---

Required action:

Downgrade or reject C2.

---

# F3 — C3

Residual → HI

Current Strength:

Initial Evidence

Current Confidence:

Low

Reason:

Comparator family not explored.

---

Specific attack from Round 1 review:

Internal contradiction:

Only 1 of 4 targets showed clear HI improvement.

Project's own 3/4 criterion was not satisfied.

Baseline P95 threshold was computed from
the same series used for evaluation,
creating a potentially tautological false-positive check.

---

Potential weakness:

Rolling RMS may simply smooth noise.

---

Missing comparators:

* EWMA
* CUSUM
* Trend slope

---

Falsification criterion:

HI correlation ≤ residual correlation

or

Alternative HI forms consistently outperform Rolling RMS.

---

Interpretation:

HI_v0 rejected as preferred HI.

Residual route remains possible.

---

Required action:

Replace HI_v0.

---

# F4 — C4

Residual → Trend

Current Strength:

Initial Evidence

Current Confidence:

Low

Reason:

Pseudo-degradation only.

---

Potential weakness:

Pseudo-degradation trend

≠

Temporal degradation trend.

---

Falsification criterion:

Long-term Marine data shows:

* no trend
* unstable trend direction

---

Interpretation:

C4 downgraded.

---

Required action:

Restrict trend interpretation.

---

# F5 — C5

Baseline Management

Current Strength:

Hypothesis

Current Confidence:

Very Low

Reason:

No maintenance-event evidence exists.

---

Potential weakness:

Maintenance effects may be:

* partial
* overlapping
* gradual

Re-stationarization may never occur.

---

Falsification criterion:

After maintenance:

Residual fails to re-stationarize.

or

Segment logic becomes inconsistent.

---

Interpretation:

Current framework rejected.

---

Required action:

Redesign Baseline Management.

---

# Failure Propagation

C1 failure

↓

Re-evaluate C2–C5

---

C2 failure

↓

Re-evaluate C3–C5

---

C3 failure

↓

Replace HI

---

C4 failure

↓

Restrict trend interpretation

---

C5 failure

↓

Redesign Baseline Management

Q1–Q4a remain independent

---

# Philosophy

The purpose of this document is not to protect claims.

The purpose is to make claims easier to disprove.
