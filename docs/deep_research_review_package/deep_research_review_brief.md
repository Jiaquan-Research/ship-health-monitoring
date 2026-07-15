# Deep Research Review Brief

Document status: Temporary Review Input
Package ID: DEEP_RESEARCH_REVIEW_PACKAGE_001
Package version: v1.1
Purpose: Independent pre-external-communication red-team review of the current Marine project evidence, scientific boundaries, communication risks, and governance/process design.

## 1. Review Context

This brief governs a blind Deep Research review of the supplied locked package. The review is advisory. It is not External Validation execution. The Deep Research system is not acting as the External Reviewer. Findings do not modify frozen claims, frozen gaps, or process state. Findings are advisory review inputs that require later reconciliation and human judgment.

External web research is permitted. Repository evidence and external evidence must be kept separately identifiable in every finding.

## 2. Input Package Lock

Use only the files supplied in this review package and external sources that you identify during your own research. The package manifest is the hash authority for the supplied inputs.

The Review Package and this Research Brief must not be changed between the two independent reviews. Both reviews must reference the same package manifest and use files whose hashes match the locked manifest.

## 3. Independent Blind Review Rules

This package is intended for two independent blind reviews:

- ChatGPT 5.6 SOL Deep Research
- Fable 5 Deep Research

The two review systems must run in separate conversations or sessions. Neither model may receive the other model's findings. No finding from Review A may be copied into the prompt for Review B. No adaptive prompting based on the first completed review is allowed. Do not select or encode a preferred review order; SOL-first and Fable-first are both permitted.

Each Deep Research system must inspect the supplied package independently, conduct external research independently, produce its own findings, avoid predicting the other model's findings, avoid assuming consensus, and avoid optimizing for agreement.

A finding identified by only one review system must not automatically be treated as low-confidence or low-value. A single-model finding means only: not independently reproduced by the second review system. Later reconciliation may classify such a finding as valid blind spot, false positive, interpretation difference, evidence-access difference, or unresolved.

## 4. Required Review Areas

### Q1 - Claim-Evidence-Gap Integrity

Identify broken claim-to-evidence links, claims stronger than their mapped evidence, gaps inconsistent with current evidence, missing limitations, and classification inconsistencies.

### Q2 - Process and State Consistency

Identify contradictions involving Draft, Complete, Reviewed, Approved, Frozen, Started, Not Started, Planned, Qualified, and Validated. Pay particular attention to cases where definition work is confused with execution or completion.

### Q3 - Public-Data / Marine Boundary

Identify any explicit or implicit movement from public-data evidence to Marine feasibility, Marine validity, shipboard applicability, deployment readiness, operational prediction, or RUL capability without sufficient evidence.

### Q4 - External Scientific and Engineering Challenge

Using external literature, standards, engineering practice, or relevant technical sources, challenge Expected State model assumptions, residual construction, Evidence construction, Health Indicator construction and aggregation, cross-model validation logic, sample-size limitations, dataset transfer assumptions, CUSUM treatment, residual versus nonresidual route selection, and claimed engineering relevance.

Do not treat disagreement with common practice as automatic proof that the project is wrong. Report it as an external scientific or engineering challenge requiring reconciliation.

### Q5 - Historical Verification Trace

Inspect historical completion and review records actually present in the supplied package. Do not infer missing historical reports.

Identify any current completed, verified, reviewed, approved, or frozen state that cannot be traced to an independently inspectable supplied record. Use the finding description `HISTORICAL_VERIFICATION_TRACE_NOT_ESTABLISHED` where appropriate.

This means only that the verification chain cannot currently be independently reconstructed from supplied materials. It does not mean that the historical claim was false.

### Q6 - Translation and Marine-Engineer Communication Risk

For important claims and boundaries, ask: If the precise technical classification labels and software/data-science terminology are removed, would a plain-language explanation to a marine engineer sound stronger than the frozen classification actually permits?

Pay particular attention to labels such as `PILOT_EVIDENCE_ONLY`, `STRUCTURAL_RELEVANCE_ONLY`, `PUBLIC_DATA_ONLY`, `UNRESOLVED`, `NOT_VALIDATED`, and `NOT_STARTED`.

Identify claims likely to become unintentionally stronger during Chinese or marine-engineer-oriented translation.

### Q7 - Governance and Process Overhead

Identify duplicated governance mechanisms, processes whose complexity materially exceeds the current evidence scale, manual checks that should plausibly be automated, process rules that conflict with each other, review mechanisms vulnerable to self-approval or rubber-stamping, and verification claims that depend excessively on manually transcribed counts or statuses.

Do not redesign the entire governance system. Do not propose a large new governance framework unless a specific identified failure cannot reasonably be addressed otherwise.

### Q8 - Pre-External-Communication Readiness

Assess whether any issue should be corrected before preparing the Marine colleague project brief, reviewer invitation material, marine-engineer support translations, or external scientific-positioning material.

Do not assess whether Marine validity has been established. Do not assess deployment readiness as achieved.

## 5. Finding Categories

Each finding may receive one or more category labels:

- A - INTERNAL_CONSISTENCY_FINDING
- B - EXTERNAL_SCIENTIFIC_ENGINEERING_CHALLENGE
- C - TRANSLATION_COMMUNICATION_RISK
- D - GOVERNANCE_PROCESS_OVERHEAD

Do not force a finding into exactly one category. Multi-label classification is allowed. Category overlap or classification disagreement may itself be useful during later reconciliation.

## 6. Finding Severity

Each finding must receive one advisory severity label:

- CRITICAL
- HIGH
- MEDIUM
- LOW
- BOUNDARY_ONLY

Severity in this Deep Research review is advisory only. It does not modify the Marine Package Gap Register. It does not automatically inherit the formal status or severity of any existing gap. It does not authorize creation, closure, downgrade, or upgrade of a formal gap. Formal repository changes require a separately authorized task.

## 7. Required Finding Schema

Each finding should contain:

```text
finding_id
title
category_labels
severity
affected_files
affected_claims
affected_gaps
finding_description
evidence_from_repository
external_sources_if_any
reasoning
potential_impact
translation_risk
recommended_action
confidence
```

Repository evidence and external evidence must remain separately identifiable.

If no external source is used, state:

```text
external_sources_if_any: None
```

If no claim or gap is directly affected, state:

```text
affected_claims: None
affected_gaps: None
```

Do not invent claim IDs or gap IDs.

## 8. Prohibited Review Behavior

Do not rewrite the Marine Package, silently correct repository artifacts, create new frozen claims, create new formal gaps, modify formal gap severity, claim Marine validity, claim Marine feasibility, claim deployment readiness, claim shipboard RUL capability, treat External Validation as started, treat Deep Research as External Validation, treat the AI system as the External Reviewer, redesign the project from scratch, expand into unrelated algorithm research, or recommend governance expansion merely because current governance is imperfect.

## 9. Required Final Report Structure

Return the review using this structure:

```text
1. Executive Assessment

2. Review Scope and Input Package Identification

3. Highest-Priority Findings

4. Detailed Findings
   - finding schema required

5. Internal Consistency Assessment

6. External Scientific and Engineering Challenges

7. Translation and Marine-Engineer Communication Risks

8. Governance and Process Overhead

9. Pre-External-Communication Readiness

10. Findings That May Be False Positives or Require Human Judgment

11. Recommended Actions Before External Communication

12. What Should Explicitly Not Be Changed

13. Final Review Position
```

Clearly distinguish verified repository contradiction, external challenge, interpretive concern, translation risk, process overhead, and uncertain finding.

## 10. Non-Authority Statement

This Deep Research review does not start External Validation, does not select or replace the human External Reviewer, does not open the Marine Request Gate, does not authorize Marine data request execution, and does not change any frozen package or definition artifact. Any recommended correction requires a separate authorized repository task.
