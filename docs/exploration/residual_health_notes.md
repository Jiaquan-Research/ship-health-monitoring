# Residual ≠ Health: Exploratory Notes

Status: Observation only. Not hypothesis. Not theory. Not evidence.
Very low confidence. Tree B of the exploration line (parallel to
Mode Conditioned Structure / Q0, which is Tree A).

This document does NOT:
- modify Claim Registry
- modify Concept Paper
- modify Baseline Management design
- support or block Validation D
- define a new theory

---

## 1. Background

Tree A (Mode Conditioned Structure / Q0) asks:

  Is Condition → Expected State a Global Mapping
  or a Piecewise Mapping?

This question concerns the EXTERNAL side of the pipeline:
the relationship between Condition Variables and the
Expected State function f.

Tree B asks a different question, concerning the INTERNAL
side:

  Even if f (Condition → Expected State) is well defined
  for a given regime, does Residual = Observed - f(Condition)
  faithfully represent Health?

These two trees are independent. Failure in one does not
imply failure in the other. They are recorded separately.

---

## 2. Core Reframing: PFD vs HI

A terminology distinction emerged during discussion that is
worth recording explicitly.

Performance Function Drift (PFD):

  PFD = Observed - f0(Condition)

  where f0 is some reference performance function
  (e.g., commissioning-time behavior, or a fitted
  Expected State model).

  PFD measures: how far has the system's input-output
  behavior moved from the reference, under the same
  external Condition.

Health Indicator (HI), as commonly used in this project
and in PHM literature generally, implicitly assumes:

  PFD direction ≈ Health direction

  i.e., "performance got worse" is treated as equivalent to
  "the machine is less healthy than before."

This document records observations where that equivalence
may not hold. The current pipeline (Residual → HI → Trend)
is, strictly speaking, a Performance Function Drift
Monitoring pipeline. Whether PFD ≈ Health is an additional,
separate, and currently unvalidated assumption.

This is not proposed as a renaming of the project. It is
recorded as a scope clarification: the pipeline measures
PFD; the mapping from PFD to Health is a further layer
that may be non-trivial.

---

## 3. Observed Patterns (Anecdotal, Engineering Experience)

The following patterns are recorded as anecdotal
observations from real marine engineering experience.
Each is currently a single (or a handful of) observation(s).
None should be treated as validated phenomena. They are
recorded because they illustrate concrete mechanisms by
which PFD and Health could diverge.

### Pattern R1 — Hidden State Drift (in-service, no event)

Observation:

A hydraulic system, while running (no maintenance event,
no logged intervention), can experience a sudden apparent
performance IMPROVEMENT. Mechanism: debris in the oil
circuit happens to plug an internal leakage path. Internal
leakage decreases, measured performance increases.

At the same time, normal wear may be increasing internal
leakage through a different path. The two effects can
partially or fully cancel, or even produce a net apparent
improvement, while underlying wear continues unabated —
or while a new degradation mode (the plugged debris itself)
has just been introduced.

Implication (observation only):

  Residual decreasing ⇏ Health improving.

  A hidden internal state variable (debris location/state)
  is neither a Condition Variable nor a Maintenance Event,
  yet it materially changes the observed input-output
  relationship.

Frequency: rare, but engineering-confirmed to occur
(not theoretical).

---

### Pattern R2 — Post-intervention Settling Transient

Observation:

After maintenance on a pump (e.g., reseating, reassembly),
performance can be temporarily WORSE immediately after
the work is completed, then recover — sometimes to a
level better than pre-maintenance — over a short running-in
period. Mechanism (one specific case): paper-based gaskets
require fluid absorption/swelling to reach their designed
sealing geometry; this takes some operating time after
reassembly.

In a minority of cases, the post-maintenance state does
NOT recover. In those cases the underlying cause is a
genuine workmanship issue (e.g., poor fastening, missing
seal, misalignment).

Implication (observation only):

  In the early part of the post-maintenance window,
  "normal settling" and "workmanship defect" can be
  observationally indistinguishable. They diverge only
  after the settling timescale has elapsed — one converges
  toward a good steady state, the other does not converge
  (or converges toward a bad state).

  This means: "residual unstable immediately after
  maintenance" is not itself informative about whether
  the maintenance was successful. Only the POST-SETTLING
  steady state is informative.

Relation to existing design:

baseline_management_v0.2.md Section 12 Step 5 already
requires a stability-confirmation window before treating
a post-maintenance state as a confirmed new baseline. This
pattern is compatible with that rule, and provides one
possible physical example consistent with the motivation behind
it. It adds a refinement: the settling transient ITSELF
may look like instability, and that is expected/normal —
the rule should not be interpreted as "instability = problem,"
but as "wait for convergence before judging."

---

### Pattern R3 — Historically Accumulated Compensation

Observation 1 ("the part that cannot be touched"):

On some vessels, certain components or fittings are known
among the crew as things that "must not be removed/changed,"
even when their original function is unclear or seems minor.
Engineering rationale (when known): the component has become
mechanically/thermally coupled into the system's current
equilibrium — affecting stress distribution, piping internal
leakage paths, thermal balance, or shaft alignment. Removing
it does not "restore the original design state"; it perturbs
a system that has re-equilibrated around its presence.

Observation 2 (setpoint-as-compensation):

Experienced engineers report cases where a vessel's fuel
viscosity setpoint, or cooling water temperature setpoint,
has been adjusted by a small fixed amount (e.g., "+3°C on
jacket water during standby") to eliminate a persistent
symptom (e.g., knocking at low main-engine speed) that
could not otherwise be diagnosed or resolved. The symptom
disappears. The underlying cause (possibly an injector
characteristic deviation, or a load-sharing imbalance on
one cylinder) is never identified or corrected — it is
compensated for via an external Condition adjustment.

Implication (observation only):

  For a vessel with significant operating history, the
  "reference" f0 learned from that vessel's data is not
  necessarily "f0 of a healthy generic generator" — whether such
  a generic reference even exists for a vessel with decades of
  history is itself an open question. It may be better described
  as:

    factory-era behavior
    + [sum of all uncorrected hidden-state deviations]
    + [sum of all undocumented compensating adjustments]

  If a future maintenance event removes one of these
  compensations (e.g., a setpoint is "corrected" back to
  a standard value during an overhaul), Residual may show
  a large step — but that step represents f0 itself
  shifting to a previously unobserved region, not a change
  in Health per se.

---

## 4. A Possible Future Identification Template (Not a Method)

The following is recorded purely as a "shape" that future
Dataset Zoo observations might be checked against. It is
NOT a detection algorithm, NOT a proposed feature, and
should not be implemented or tested at this stage. It is
written down only so that if something like it is observed
later, it can be recognized as potentially related to this
note.

Possible shapes to watch for (observation only):

  - An unexpected residual movement, in the direction
    OPPOSITE to the prevailing long-term trend, after which
    the trend resumes its prior direction. The movement may
    be abrupt or gradual; no specific shape is assumed.
    (Candidate shape for Pattern R1 — hidden state switch,
    no event logged.)

  - A short period of elevated residual VARIANCE (not
    necessarily elevated MEAN) immediately following a
    logged maintenance event, which then either converges
    to a new stable low-variance state, or fails to
    converge within an expected timescale. (Candidate shape
    for Pattern R2 — settling transient vs. workmanship
    defect; the two are distinguished only by long-run
    convergence, not by the transient itself.)

  - A large, durable step in residual that occurs at or
    near a maintenance event, where the new post-event
    baseline level is OUTSIDE the range of any previously
    observed operating history for that asset. (Candidate
    shape for Pattern R3 — f0 itself relocating, as opposed
    to a bounded health-state change within a previously
    seen f0.)

These shapes are speculative pattern descriptions only.
No claim is made that they are detectable, distinguishable
in practice, or that any current or future dataset will
exhibit them.

---

## 4.5 Frequency

The prevalence of R1, R2, and R3 is unknown.

Current observations are anecdotal (R1 ×1, R2 ×1, R3 ×2).

They may be:
- common;
- rare but important;
- edge cases;
- marine-specific phenomena.

No frequency estimate is implied. The primary risk
associated with these patterns is not that they are
wrong, but that a rare exception could be mistaken
for a dominant mechanism if frequency is assumed
without evidence.

---

## 5. Open Question (Recorded, Not Pursued)

The three patterns above (R1, R2, R3) may or may not be
manifestations of a single underlying phenomenon — e.g.,
"f0 contains slowly-evolving, unobserved internal state
variables, of which Condition Variables and logged
Maintenance Events capture only a partial view."

This unification question is explicitly NOT pursued at
this stage. Per the established exploration discipline
(Observation → Pause → Context Audit → Comparability
Check → Question Generation), a single anecdotal
observation per pattern (currently: R1 ×1, R2 ×1, R3 ×2)
is far too little evidence to justify generating a unified
hypothesis. This section exists only to flag that the
question exists, for possible future revisiting if and
when more observations accumulate.

A related, deeper question is also recorded without
pursuit: for a real vessel with years of operating history,
what does "baseline" even mean — "what a healthy generic
machine should do," or "what THIS machine, with its full
accumulated history, currently does"? This question is left
open deliberately.

---

## 6. Relationship to Other Exploration Documents

- Tree A (Q0, Mode Conditioned Structure): concerns
  Condition → Expected State (external side).
- Tree B (this document): concerns Residual → Health
  (internal side).
- These trees are independent. Evidence in one does not
  upgrade or downgrade the other.
- Both trees follow the same discipline: Observation first,
  no theory, no claim upgrades, failure acceptable.

---

## 7. Non-Goals

This document does NOT:
- propose a Performance Function Drift Indicator as a
  replacement for HI_v0 (mentioned only as a terminology
  clarification, not a design proposal)
- propose detection methods for R1/R2/R3
- claim these patterns are common, rare-but-negligible, or
  important — frequency is unknown
- claim these patterns apply outside marine diesel/hydraulic
  systems
- modify any evidence level in the Claim Registry

Scope boundary:

These notes are recorded within industrial health
monitoring contexts only (marine machinery, and by
extension other mechanical/hydraulic/thermal systems
discussed elsewhere in the exploration line). No
attempt is made to generalize them into a theory of
complex systems, attractors, hidden-state dynamics,
or any domain-independent framework. If future
observations suggest broader applicability, that
would itself require new evidence and a new,
separately-scoped document.

---

## Version History

v0.1 — 2026-06-12 — Initial notes. Three anecdotal patterns
(R1 Hidden State Drift, R2 Post-intervention Settling
Transient, R3 Historically Accumulated Compensation)
recorded. PFD vs HI terminology distinction recorded.
Unification question flagged but not pursued.

v0.1.1 — 2026-06-12 — Tightened R2/R3 wording to avoid
retroactive justification and unwarranted reference
assumptions; broadened R1 candidate shape; added
Frequency section; added explicit scope boundary.
