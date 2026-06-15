# Exploration Review — Week 1

Date: 2026-06-12
Status: Periodic Review (Exploration Line)
Scope: Summarizes exploration-line activity for the period
covering I-1 through Battery Dataset Context Audit (P0).

---

## Purpose

This document is a periodic audit of the exploration line
itself. Its purpose is not to produce new findings, but to:

- record what has been observed;
- record what questions currently exist;
- record what was deliberately NOT pursued;
- check whether open issues from any prior review have
  been resolved, absorbed, or remain outstanding.

This document follows the same discipline as the rest of
the exploration line: observation first, no theory, no
claim upgrades. It also applies that discipline reflexively
— the exploration line's own outputs are subject to review,
just as any other result would be.

This is the first review of this kind. There is no prior
review to carry over from.

---

## 1. Observations (Chronological)

| # | Item | Result | Type |
|---|------|--------|------|
| 1 | I-1 (Negative Control) | FAIL — healthy-period residual/HI correlates with OA_TEMP and CWL_SEC_LOAD | Validation (Review Layer) |
| 2 | M-1 (Condition Leakage Audit) | FAIL — strong condition dependence remains (RF R² up to 0.645 for HI_v0) | Validation (Review Layer) |
| 3 | M-1A (Type Separation) | Type C dominant; Type A not supported; Type B moderate; Type D not primary | Validation (Review Layer) |
| 4 | E-1 (N-CMAPSS Cross-Regime Probe) | No obvious instability observed (same-window R²≈0.999, cross-window R²≈0.916) | Exploratory |
| 5 | E-2 (Battery Cross-Regime Probe) | NASA Battery: collapse observed. Oxford Battery: no obvious collapse. | Exploratory |
| 6 | Battery Dataset Context Audit (P0) | Layer 1 (Acquisition): Different, high confidence. Layer 2 (Chemistry): Unknown. Layer 3 (E-2 Implementation): Inconsistent, high confidence. | Audit |

Items 1-3 are Review Layer validations (pre-registered,
formal pass/fail criteria). Items 4-6 are Exploration Line
activity (observation-only, no claim implications).

---

## 2. Questions Currently Open

### Q0 — Global Mapping vs Piecewise Mapping

Status: Exploratory question. Very low evidence.
Defined in: `docs/exploration/q0_global_vs_piecewise.md`

Current evidence inventory for Q0:

| Dataset | Observation | Counts toward Q0? |
|---------|-------------|---------------------|
| HVAC | Cross-season collapse (M-1A) | Yes — 1 observation |
| N-CMAPSS | No obvious instability (E-1) | Yes — 1 observation |
| Battery (NASA/Oxford) | E-2 results diverge, but audited as non-comparable | **Suspended** — see Section 4 |

Q0 evidence count after this review: HVAC ×1, N-CMAPSS ×1.
Battery's contribution is suspended pending E-2 redesign,
not removed. See Section 4 for the reasoning and the path
back in.

---

## 3. Trees

### Tree A — Mode Conditioned Structure (Q0)

Concerns: Condition → Expected State (external side).

Status: 2 observations (HVAC, N-CMAPSS). No theory.
No unification attempted.

This week's development: Battery was probed (E-2) but the
result could not be added to the Q0 evidence inventory —
see Section 3 (Battery Status) below.

### Tree B — Residual ≠ Health

Concerns: Residual → Health (internal side).
Defined in: `docs/exploration/residual_health_notes.md`

Status: 3 anecdotal patterns recorded (R1 ×1, R2 ×1,
R3 ×2). No new observations this week. Document was
tightened per review (wording on R2/R3 references,
added Frequency section, added scope boundary).

Trees A and B remain independent. No cross-tree
interaction occurred this week.

---

## 4. Battery Status — E-2 Divergence Audited, Not Resolved

This is the most significant single item from this review
period and is given its own section.

E-2 produced an apparent contradiction: NASA Battery showed
"collapse observed" while Oxford Battery showed "no obvious
collapse." Following the established discipline
(Observation → Pause → Context Audit → Comparability Check
→ Question Generation if justified), a Context Audit (P0)
was performed before any interpretation.

Result of the audit:

- **Layer 1 (Acquisition Protocol):** Different, high
  confidence. NASA's two compared conditions are disjoint
  cells under different temperature/load test protocols
  (24°C/4A square-wave vs 4°C/2A fixed load). Oxford's two
  compared conditions are the same cells under two different
  *measurement* protocols (1-C discharge vs pseudo-OCV
  characterization), not two *operating regimes* in the
  sense relevant to Q0.

- **Layer 2 (Chemistry/Degradation Mechanism):** Unknown,
  high confidence in the "unknown" assessment itself —
  documentation is insufficient to determine whether NASA
  and Oxford cells would be expected to behave similarly
  with respect to regime-dependent performance.

- **Layer 3 (E-2 Implementation Consistency):** Inconsistent,
  high confidence. Regime definitions, predictors,
  populations, observational units, row counts, and capping
  paths all differ between the NASA and Oxford runs of E-2.

**Conclusion of this review:** The E-2 "collapse vs no
collapse" outcome does not currently constitute a pair of
comparable observations about Type C. It is closer to two
differently-posed questions producing two different
answers, rather than one question producing two
contradictory answers. Per the established discipline, this
divergence is recorded as audited, not as a contradiction
requiring resolution via new theory or new questions.

**Disposition:**

Battery (NASA and Oxford)'s contribution to the Q0
evidence inventory is suspended pending redesign,
effective this review. It is marked:

> "E-2 needs redesign before Battery can contribute to Q0."

This is not a negative judgment of the datasets themselves.
It reflects that the current E-2 implementation did not ask
a question about Battery that is comparable to the
HVAC/N-CMAPSS questions about Q0 (i.e., "does the same
fitted relationship hold across different *operating
regimes* of the *same asset population*?").

A future E-2' would need to first establish what
constitutes "regime" for a battery dataset in a sense
analogous to "season" (HVAC) or "lifecycle stage"
(N-CMAPSS) — e.g., possibly: ambient temperature bands
during cycling, charge/discharge rate bands, or
depth-of-discharge bands, applied consistently within a
single population of cells. This redesign is not scheduled
as part of this review; it is recorded as a precondition
for Battery's re-entry into the Q0 inventory.

---

## 5. Dead Ends

None identified this period.

Note: "Battery contribution to Q0 suspended" (Section 4)
is NOT a dead end. The context-audit absorption of the
E-2 divergence is itself a successful outcome — it
resolved an apparent contradiction without requiring new
theory or new questions. The datasets remain in the
Dataset Zoo; only their current contribution to Q0 is
paused pending redesign.

---

## 6. Open Issues

The following issues remain open and unresolved as of this
review:

- **Condition normalization** — M-1/M-1A identified Type C
  (cross-regime instability) as the dominant leakage
  mechanism in HVAC. No remediation has been attempted.
  Engineering line (Validation D, HI_v1, C5) remains
  blocked pending resolution.

- **Baseline meaning** — `residual_health_notes.md` Section 5
  flags an open question about what "baseline" means for an
  asset with extensive operating history (factory-era
  behavior vs. current accumulated state). Not pursued.

- **E-2 redesign precondition** — see Section 4. Required
  before Battery can re-enter the Q0 inventory. Not
  scheduled.

---

## 7. Things Intentionally NOT Pursued

This section records impulses that were deliberately not
acted on, per the exploration discipline.

- **No new Q-numbers were generated.** The E-2 divergence
  did not produce "Q6/Q7/Q8" as initially flagged as a risk
  during E-2 itself. The Context Audit absorbed the
  divergence instead.

- **No unification of R1/R2/R3** (Tree B) was attempted.
  `residual_health_notes.md` Section 5 explicitly defers
  this question (currently R1 ×1, R2 ×1, R3 ×2 — judged
  insufficient).

- **No cross-tree interaction** between Tree A and Tree B
  was proposed or pursued, despite both trees being active
  in the same period.

- **No theory of Type C** was proposed. Type C remains
  described only as "dominant mechanism in HVAC, not
  observed in N-CMAPSS, currently inapplicable to Battery."

- **No generalization beyond industrial health monitoring**
  was attempted, per the scope boundary added to
  `residual_health_notes.md`.

- **E-3 was not executed.** Per prior discussion, the E-1/E-2
  divergence was judged higher-priority to resolve (via
  Context Audit) than acquiring a new observation. This
  review's Section 4 reflects the outcome of that
  prioritization.

---

## 7.5 Process Lessons

This period's most significant outcome may not be any
individual observation, but the fact that the exploration
discipline itself was exercised end-to-end for the first
time on a real divergence (E-2).

1. The sequence Observation → Pause → Context Audit →
   Comparability Check → Question Generation was exercised
   successfully during the E-2 divergence (Section 4).

2. An interesting or surprising result does not necessarily
   deserve a new question. The E-2 divergence initially
   looked like it might require new Q-numbers; a Context
   Audit resolved it without any.

3. A context audit can absorb an apparent contradiction
   without requiring a new theory. "Two differently-posed
   questions producing two different answers" is a complete
   explanation in itself.

4. Exploration line outputs themselves require periodic
   review — this document is an instance of that, and is
   itself subject to the same discipline (see Section 8).

---

## 8. Carryover for Next Review

Items to check at the next periodic review:

- Has the "E-2 redesign precondition" (Section 4) been
  addressed, or does it remain outstanding?
- Has "Condition normalization" (Section 6) seen any
  movement, or does it remain a pure blocker?
- Has "Baseline meaning" (Section 6) accumulated any new
  observations, or does it remain a single flagged question?
- Does the Q0 evidence inventory (Section 2) still stand at
  HVAC ×1, N-CMAPSS ×1, or have new datasets been added
  (Dataset Zoo: ZEMA, C-MAPSS, Bearing datasets are
  downloaded but not yet probed)?
- Have any new items appeared in "Things Intentionally NOT
  Pursued" — and if an item disappears from that list
  without becoming a tracked question, that itself should
  be noted (it would mean the discipline was not followed).
- Has this Exploration Review itself remained useful, or
  has it become unnecessary overhead? (The review process
  is itself subject to audit, per Process Lesson 4.)

---

## 9. Engineering Line Status (Reference Only)

For reference, not modified by this review:

- Validation D: blocked (per attack_review_summary_v1.md
  Section 9 and Section 10)
- HI_v1: blocked
- C5: blocked
- Claim Registry: unchanged this period

This review does not propose any change to the above.

---

## Version History

v1 — 2026-06-12 — First periodic exploration review.
Covers I-1 through Battery Dataset Context Audit (P0).
No prior review to carry over from.

v1.1 — 2026-06-12 — Changed Battery disposition from
"removed" to "suspended pending redesign" throughout;
clarified Dead Ends section; added Process Lessons
section (7.5); added self-review carryover item.
