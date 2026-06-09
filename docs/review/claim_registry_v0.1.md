# Claim Registry v0.1

Date: 2026-06-09
Status: Open to independent review

No claim in this document is considered
established truth.

Evidence strength represents current confidence,
not certainty.

The purpose of this document is to facilitate
independent falsification attempts.

---

## Claim Priority for Independent Review

Critical

C1

C2

Important

C3

Exploratory

C4

Future

C5

Purpose:

Guide future attacks.

---

## C1 — Condition → Expected State

Strength:

Moderate Evidence

Claim:

Condition Variables can support Expected State modeling
in the validated non-Marine domains.

Current evidence:

- HVAC Validation B1
- N-CMAPSS Validation C0.2

Alternative Explanation:

High R² may depend on controller structure
and limited operating manifolds.

Marine transfer remains unvalidated.

Scope boundary:

Marine diesel generators may have variable multi-cylinder
behavior, load transients, and operating regimes not covered
by HVAC or aero-engine simulation data.

Status:

Open to independent review.

---

## C2 — Expected State → Residual

Strength:

Initial Evidence

Claim:

Residual can contain degradation information
when Expected State modeling is valid and label semantics
are correctly interpreted.

Current evidence:

- HVAC Validation B2.1
- N-CMAPSS Validation C0.2

Known Weakness:

B2.1 required corrected severity ordering.

Potential post-hoc ordering risk exists.

External severity semantics should be verified.

Scope boundary:

Marine residual behavior remains unvalidated.

Status:

Open to independent review.

---

## C3 — Residual → HI

Strength:

Initial Evidence

Claim:

Rolling RMS HI_v0 can summarize residual behavior
into a degradation-sensitive indicator in the tested domains.

Current evidence:

- HVAC HI_v0 validation
- N-CMAPSS C0.2

Known Weakness:

HI_v0 has not been benchmarked against:

* EWMA
* CUSUM
* Trend slope

Observed benefit may arise from smoothing
rather than additional information.

Scope boundary:

The optimal HI form remains open.

Status:

Open to independent review.

---

## C4 — Residual → Trend

Strength:

Initial Evidence

Claim:

Residual metrics can form a trend candidate
along pseudo-degradation paths.

Current evidence:

- HVAC Validation B4

Scope boundary:

Evidence is based on pseudo-degradation paths
and fault severity levels, not long-duration real
temporal degradation histories.

Status:

Open to independent review.

---

## C5 — Baseline Management

Strength:

Hypothesis

Claim:

Baseline Management may allow residual and HI trends
to remain interpretable across maintenance events.

Current evidence:

- Framework design
- Cross-industry literature support

Scope boundary:

No direct project evidence exists yet.
Validation requires real Marine maintenance records.

Status:

Awaiting Validation D.
