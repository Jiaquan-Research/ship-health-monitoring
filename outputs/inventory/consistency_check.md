# Document/Code Consistency Check

## Scope

Compared current stated project status in:

- `docs/review/claim_registry_v0.1.md`
- `docs/review/attack_review_summary_v1.md`
- `CLAUDE.md`
- `SYSTEM_STATE.md`
- `docs/exploration/exploration_review_week1.md`

against latest validation outputs:

- `outputs/validation_i1_negative_control.md`
- `outputs/validation_m1_condition_leakage.md`
- `outputs/validation_m1a_type_separation.md`
- plus relevant prior outputs for B4, HI_v0, and C0.2 where claims explicitly cite them.

## Claim Evidence-Level Check

| Claim | Evidence level stated in Claim Registry | Evidence level implied by latest validation output | Consistent? (Yes/No/Unclear) |
| --- | --- | --- | --- |
| C1 | Moderate Evidence | Moderate but qualified/unstable: B1/C0.2 support mechanics, but M-1A reports Type C dominant cross-regime instability and Validation D remains blocked. | Unclear |
| C2 | Initial Evidence | Unclear/weakened: C0.2 and B2.1 support residual mechanics, but I-1 and M-1 show residual/HI condition leakage and residual construct validity requires revision; attack summary also states C2 Moderate Evidence, which conflicts with registry. | No |
| C3 | Initial Evidence | Unclear/weakened: HI_v0 had prior Moderate PASS, but I-1/M-1 show HI_v0 trends and variance are condition-dependent in healthy data. | Unclear |
| C4 | Initial Evidence | Conflicted: B4 output says Q4a Initial Evidence, but attack review says C4 removed from Claim Registry and I-1 shows apparent trends in healthy data. | No |
| C5 | Hypothesis | Hypothesis / blocked: no direct project evidence; Validation D remains blocked and exploration review marks C5 blocked. | Yes |

## Findings

### Finding 1 - Claim Registry and Attack Review disagree on C2 evidence level

The current Claim Registry says C2 is Initial Evidence, while the attack review summary later says C2 is Moderate Evidence. This is a direct document-level inconsistency.

`docs/review/claim_registry_v0.1.md` lines 78-85:
```text
## C2 — Expected State → Residual

Strength:

Initial Evidence

Claim:

```

`docs/review/attack_review_summary_v1.md` lines 326-333:
```text
C2

Moderate Evidence

C3

Initial Evidence

```

Assessment: **Conflict found.** Use caution when summarizing C2 to a non-coding reviewer; the latest review-layer document and the registry do not use the same level.

### Finding 2 - Claim Registry still contains C4 although Attack Review Round 2 says C4 was removed

The Claim Registry includes C4 as Initial Evidence. Attack Review Summary says Round 2 removed C4 from the Claim Registry and made Trend an Open Question. B4 itself still reports Q4a Initial Evidence, so the project contains three distinguishable statements: B4 result, review judgment, and registry state.

`docs/review/claim_registry_v0.1.md` lines 150-157:
```text
## C4 — Residual → Trend

Strength:

Initial Evidence

Claim:

```

`docs/review/attack_review_summary_v1.md` lines 92-99:
```text
C4:

Removed from Claim Registry.

Trend becomes an Open Question.

C5:

```

`outputs/b4_residual_trend_audit.md` lines 4-11:
```text
- Q4a status: Initial Evidence
- Best trend metric: RMS
- Targets with reliable trend: 4/4
- Input: frozen Validation B2.1 residuals only. No residuals recomputed. No models retrained.

## Dataset Load Check

| Dataset | Rows |
```

Assessment: **Conflict found.** The registry appears stale or intentionally more permissive than Attack Review Round 2; this should be resolved before using C4 in a public-facing narrative.

### Finding 3 - CLAUDE.md contains stale strong-evidence language after later attack review downgrades

`CLAUDE.md` still reports cross-domain evidence as Strong/Moderate after C0.2. Attack Review Summary later says current evidence should be interpreted only as pipeline mechanics on two simulation domains and explicitly rejects strong cross-domain evidence.

`CLAUDE.md` lines 210-217:
```text
### Cross-Domain Evidence Status
Q1: Strong Evidence (HVAC + Aero Engine)
Q2: Strong Evidence (HVAC + Aero Engine)
Q3: Moderate Evidence (HVAC + Aero Engine)
Q4a: Initial Evidence
Q4b: Open — Architecture Defined, awaiting Marine data

### Explicitly NOT Current Priorities
```

`docs/review/attack_review_summary_v1.md` lines 129-136:
```text
Current evidence should be interpreted as:

Pipeline mechanics demonstrated on
two simulation domains.

Not:

Strong cross-domain evidence.
```

`docs/review/attack_review_summary_v1.md` lines 406-413:
```text
Current status is NOT:

"Strong cross-domain evidence established."

---

## 9. Current Highest-Priority Question

```

Assessment: **Conflict found.** `CLAUDE.md` is stale relative to the review layer. It should not be used as the authoritative current project status.

### Finding 4 - CLAUDE.md B4 Strong PASS wording is more positive than later review-layer status

`CLAUDE.md` records B4 as Strong PASS and says Q4a can be marked Initial Evidence. Later review documents keep Validation D blocked and identify Expected State stability / condition leakage as unresolved. This is not necessarily a contradiction about the B4 output itself, but it is a conflict in current project framing if read as current status.

`CLAUDE.md` lines 160-167:
```text
## Validation B4 Residual Trend Audit

Status:

PASS - Strong PASS

Q4a status:

```

`docs/review/attack_review_summary_v1.md` lines 296-303:
```text
Validation D remains blocked.

No claim upgrades are justified.

---

## 6. Surviving Structure

```

`outputs/validation_i1_negative_control.md` lines 85-92:
```text
FAIL: sub-window instability appears in healthy data.

## 9. Consequences

Failure does NOT invalidate the project.

Failure suggests:

```

Assessment: **Framing conflict found.** B4 remains a prior output, but later I-1/M-1/M-1A outputs constrain how much it can support trend claims.

### Finding 5 - SYSTEM_STATE.md is older than B2.1/HI/B4/C0/I-1/M-1 and is not current

`SYSTEM_STATE.md` reports only the early validation chain through B2.1 and preliminary supported status. It does not reflect later HI_v0, B4, C0.2, I-1, M-1, M-1A, or exploration outcomes.

`SYSTEM_STATE.md` lines 24-31:
```text
Current Evidence Chain

Condition Variables

↓

Expected State Model

```

`docs/exploration/exploration_review_week1.md` lines 291-298:
```text
## 9. Engineering Line Status (Reference Only)

For reference, not modified by this review:

- Validation D: blocked (per attack_review_summary_v1.md
  Section 9 and Section 10)
- HI_v1: blocked
- C5: blocked
```

Assessment: **Stale-status conflict.** `SYSTEM_STATE.md` should be treated as historical unless explicitly refreshed.

### Finding 6 - Latest review-layer outputs consistently block Validation D

I-1, M-1, Attack Review Summary, and Exploration Review agree that forward engineering validation / Validation D is blocked. This part is consistent.

`outputs/validation_i1_negative_control.md` lines 109-113:
```text
* Validation D remains blocked
  until I-1 passes.

No specific remediation path
is assumed.
```

`outputs/validation_m1_condition_leakage.md` lines 157-164:
```text
Validation D remains blocked.

No specific remediation path is assumed.

Leakage taxonomy should guide future investigation.

## 9. Visualizations

```

`docs/review/attack_review_summary_v1.md` lines 296-303:
```text
Validation D remains blocked.

No claim upgrades are justified.

---

## 6. Surviving Structure

```

`docs/exploration/exploration_review_week1.md` lines 295-302:
```text
- Validation D: blocked (per attack_review_summary_v1.md
  Section 9 and Section 10)
- HI_v1: blocked
- C5: blocked
- Claim Registry: unchanged this period

This review does not propose any change to the above.

```

Assessment: **Consistent.** This is the clearest current-status statement.

## Summary

- Authoritative current review-layer status should come from `attack_review_summary_v1.md`, `exploration_review_week1.md`, and the latest validation outputs, not from `CLAUDE.md` or `SYSTEM_STATE.md`.
- The most important unresolved registry issue is C4: present in Claim Registry but described as removed/open by Attack Review Summary.
- C2 also has an evidence-level mismatch: Initial in Claim Registry, Moderate in Attack Review Summary.
- Validation D blocked status is consistent across latest review-layer materials.
