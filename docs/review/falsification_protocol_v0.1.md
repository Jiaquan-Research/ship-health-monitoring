# Falsification Protocol v0.1

Date: 2026-06-09

Status:

Open

Purpose:

Describe how each claim may fail.

Failure is acceptable.

Agreement is unnecessary.

---

## Evidence Strength Interpretation

Strong Evidence

≠ truth

Moderate Evidence

≠ truth

Initial Evidence

≠ truth

Hypothesis

≠ truth

All claims remain falsifiable.

---

# F1 — C1

Condition → Expected State

Current strength:

Moderate Evidence

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

---

Interpretation:

C1 Marine transfer fails.

Non-Marine evidence remains valid.

---

Required action:

Downgrade C1.

---

# F2 — C2

Expected State → Residual

Current strength:

Initial Evidence

---

Potential weakness:

Post-hoc severity ordering risk.

---

Falsification criterion:

Residual cannot separate:

healthy

vs

degraded

when external severity semantics are known.

or

Residual separation disappears under
independent datasets.

---

Interpretation:

C2 weakened.

---

Required action:

Downgrade or reject C2.

---

# F3 — C3

Residual → HI

Current strength:

Initial Evidence

---

Potential weakness:

HI_v0 may simply smooth noise.

---

Missing comparators:

* EWMA
* CUSUM
* Trend slope

---

Falsification criterion:

HI correlation

≤

Residual correlation

or

Alternative HI forms consistently outperform
Rolling RMS.

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

Current strength:

Initial Evidence

---

Potential weakness:

Pseudo-degradation trend

≠

Temporal degradation trend.

---

Falsification criterion:

Long-term Marine data shows:

No trend

or

Trend direction unstable.

---

Interpretation:

C4 downgraded.

---

Required action:

Restrict trend interpretation.

---

# F5 — C5

Baseline Management

Current strength:

Hypothesis

---

Potential weakness:

Maintenance effects are:

* partial
* overlapping
* gradual

No clear re-stationarization exists.

---

Falsification criterion:

After maintenance:

Residual does not re-stationarize.

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

Re-evaluate C2–C5.

---

C2 failure

↓

Re-evaluate C3–C5.

---

C3 failure

↓

Replace HI.

---

C4 failure

↓

Trend interpretation restricted.

---

C5 failure

↓

Baseline Management redesign.

Q1–Q4a remain independent.

---

# Philosophy

The purpose of this document is not to
protect the claims.

The purpose is to make the claims easier
to disprove.
