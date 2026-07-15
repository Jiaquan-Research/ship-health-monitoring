# External Validation of Project Results Specification

Document status: Frozen
Version: v1.0
Phase: External Validation Definition
External Validation execution: Not started
External reviewer: Not selected
Marine data request: Planned, not started
Marine validity: Not claimed

## 1. Purpose

External Validation of Project Results provides an independent review of the project's public-data findings, framework claims, documented limitations, Marine boundaries, reproducibility records, and process-state assertions. Its purpose is to determine whether the Marine Package accurately represents the available evidence and its limits.

External Validation does not prove Marine applicability, Marine validity, deployment readiness, shipboard RUL, or Health Assessment completion.

The External Reviewer must be a human individual. An artificial-intelligence system, large language model, autonomous agent, software review system, or other non-human system is not eligible to serve as the External Reviewer. AI systems may assist with clerical work, search, formatting, consistency checks, or reviewer support only when their use is disclosed and the human reviewer independently evaluates and owns the final judgment.

The human-reviewer requirement exists because the current project workflow has already used multiple AI systems for drafting, execution, review, correction, and governance. External Validation is intended to introduce an independent human judgment outside that AI-assisted workflow. A review conducted only by another AI system would be an additional internal or automated review, not External Validation of Project Results.

Permitted distinctions:

- AI-assisted internal review: permitted
- AI-assisted human external review: permitted with disclosure and human ownership
- AI-only external review: prohibited
- project-participating AI acting as reviewer: prohibited

## 2. Scope

The review scope includes the Marine Package v1.0 narrative, 40 frozen claims, 27 active gaps, Evidence Map, Artifact Index, Gap Register, Completion Review, Freeze Manifest, primary public-data closure and review artifacts, canonical numerical artifacts, candidate-tool definitions, Marine process-state claims, and permitted and prohibited wording.

The reviewer assesses accuracy, traceability, support strength, boundary preservation, internal consistency, reproducibility disclosure, process-state accuracy, and absence of unsupported Marine implications.

## 3. Non-Scope

External Validation definition excludes new model execution, metric recomputation unless separately authorized, opening blocked test data, Marine dataset evaluation, shipboard feasibility validation, deployment approval, product safety approval, RUL validation, operator-workflow validation, alarm-threshold validation, commercial due diligence, and source-code security audit.

The reviewer may identify missing work but may not silently perform or claim it.

## 4. Validation Object

The validation object is the integrity of the project's representation of its existing evidence. It is not the truth of all future Marine hypotheses, the operational value of an undeployed tool, or the physical degradation meaning of the current HI.

External Validation validates the evidence package and its claim discipline. It does not validate Marine performance.

## 5. Reviewer Eligibility

A reviewer is eligible only if all mandatory conditions are satisfied:

1. The reviewer is a human individual.
2. The reviewer satisfies at least one technical-competence route.
3. The reviewer satisfies the independence requirements.
4. The reviewer completes the conflict-of-interest declaration.
5. The reviewer accepts personal responsibility for the final review.
6. The reviewer has sufficient access and time to complete the required scope.

Failure of Condition 1 results in `REVIEWER_INELIGIBLE`. It cannot result in `REVIEWER_ELIGIBLE_WITH_MANAGED_CONFLICT` because non-human reviewer status is not a manageable conflict.

Technical-competence routes:

- Route A: relevant research experience in prognostics, health monitoring, reliability, condition monitoring, industrial data analysis, or adjacent fields.
- Route B: relevant engineering experience in machinery maintenance, marine engineering, industrial operations, reliability, or technical assurance.
- Route C: relevant audit, verification, validation, safety, quality, or evidence-review experience for technical systems.

The reviewer must be able to read technical English, inspect repository artifacts, follow claim-to-evidence mappings, distinguish evidence levels, identify unsupported generalization, and document findings.

Academic credentials are not the only eligibility route.

## 6. Reviewer Independence

The reviewer must be independent from both the formal repository authors and experiment executors and the AI-assisted governance workflow that designed, reviewed, and corrected Marine Package v1.0.

Minimum requirements:

- The reviewer did not author the reviewed Package.
- The reviewer did not execute the experiments being reviewed.
- The reviewer is not responsible for obtaining a favorable result.
- The reviewer has no undisclosed financial, employment, academic, or personal interest that would materially bias the review.
- The reviewer may ask questions and request clarification but may not rewrite the evidence record on behalf of the project owner.

Acceptable conditions include prior familiarity with the project, technical discussion with the project owner, reviewer compensation disclosed in advance, and domain collaboration without authorship of the reviewed evidence.

Potentially disqualifying conditions include co-authorship of primary evidence, direct responsibility for disputed results, undisclosed commercial interest, review outcome linked to payment, personal conflict affecting impartiality, substantial prior contribution to Package design, claim wording, experiment interpretation, task-card design, or responsibility for defending the Package outcome.

Independence decisions:

- `INDEPENDENCE_CONFIRMED`
- `INDEPENDENCE_CONFIRMED_WITH_DISCLOSED_LIMITATION`
- `INDEPENDENCE_NOT_ESTABLISHED`

`INDEPENDENCE_CONFIRMED_WITH_DISCLOSED_LIMITATION` may be used only for a human reviewer.

Any AI system that participated in designing, drafting, reviewing, executing, auditing, correcting, or governing Marine Package v1.0 or its task-card workflow is ineligible to act as the External Reviewer. This includes ChatGPT, Claude, Codex, Gemini, any model, agent, or automated workflow derived from or operating through those systems, and any successor instance using the same project conversation, repository context, task history, or governance memory. The exclusion applies regardless of whether the AI system directly wrote repository files, only reviewed outputs, only proposed corrections, only generated task cards, only checked hashes, only summarized evidence, or acted in a separate conversation or interface.

The human reviewer must personally inspect the required evidence package, make claim-level and gap-level decisions, assess Marine and process-state boundaries, decide whether findings are blocking, approve the final External Validation decision, approve the Marine Request Gate decision, and accept responsibility for the review record. The reviewer may not merely sign an AI-generated conclusion without conducting their own review.

## 7. Conflict-of-Interest Rules

The reviewer must sign a declaration covering authorship, experiment involvement, financial interest, employment relationship, academic collaboration, personal relationship, competitive interest, prior public position on the project, prior participation in AI-assisted project workflow, prior access to private project discussions, prior contribution to task-card design, prior contribution to Package wording, prior contribution to review findings, use of project-specific AI context or memory, AI tools intended for use during the review, and other material conflicts.

Required question: Has the reviewer, directly or through an AI system under their control, previously participated in drafting, reviewing, correcting, or governing Marine Package v1.0? Response: Yes / No. If Yes, explanation and independence assessment are required.

Conflict decision labels:

- `NO_MATERIAL_CONFLICT`
- `DISCLOSED_MANAGEABLE_CONFLICT`
- `REVIEWER_INELIGIBLE`

A manageable conflict must include mitigation.

## 8. Reviewer Appointment Process

The appointment sequence is:

1. Identify reviewer candidate.
2. Obtain reviewer declaration.
3. Check technical eligibility.
4. Check independence.
5. Record conflicts and mitigation.
6. Approve or reject reviewer.
7. Freeze the review scope.
8. Deliver the evidence package.
9. Start External Validation execution.

Reviewer appointment must be recorded separately. This definition task does not appoint anyone.

## 9. Evidence Package

The evidence package is defined in `docs/external_validation/external_validation_evidence_package_manifest.md`. It includes controlled groups for frozen Package governance, frozen claim and gap controls, public-data residual evidence, public-data nonresidual evidence, framework and architecture, Marine request and intake templates, reproducibility and lineage records, and review instructions and forms.

## 10. Evidence Access Rules

Default access is read-only. The reviewer may not modify repository evidence, execute code, open blocked test data, access credentials or unrelated personal files, redistribute files externally without permission, or substitute files outside the manifest.

Reviewer questions must be recorded. Clarifications from the project owner must be added as review correspondence, not silently inserted into frozen artifacts.

## 11. Review Questions

Claim integrity questions:

- Are all 40 claims represented accurately?
- Does each claim retain its frozen support level?
- Is any development, pilot, design, or process evidence written as stronger evidence?
- Are unsupported generalizations present?

Gap integrity questions:

- Are all 27 gaps visible?
- Are blocker classifications accurate?
- Does Package completion improperly imply gap closure?
- Are any limitations hidden or minimized?

Numerical integrity questions:

- Do reported numerical values match authoritative artifacts?
- Are cross-dataset comparisons appropriately bounded?
- Were any values presented without source or status?

Reproducibility questions:

- Are incomplete dataset hashes disclosed?
- Are source-script limitations disclosed?
- Does the Artifact Index accurately describe lineage?

Marine boundary questions:

- Is Marine validity avoided?
- Is Marine feasibility avoided?
- Is data receipt or qualification falsely implied?
- Is External Validation completion falsely implied?

Candidate-tool questions:

- Do tool definitions match the frozen Structure?
- Are readiness labels interpreted correctly?
- Are unsupported decisions and safety boundaries visible?

Process-state questions:

- Is the Marine request still planned and not started?
- Is External Validation accurately described?
- Are future workstreams separated from completed work?

## 12. Claim-Level Review Method

The reviewer must evaluate every frozen claim with fields for claim_id, claim_text, classification, mapping_status, primary evidence, support-strength assessment, Package wording assessment, boundary assessment, review decision, finding ID, and reviewer note.

Claim-level decisions:

- `CONFIRMED`
- `CONFIRMED_WITH_LIMITATION`
- `WORDING_REVISION_REQUIRED`
- `SUPPORT_DOWNGRADE_REQUIRED`
- `EVIDENCE_LINK_CORRECTION_REQUIRED`
- `UNRESOLVED`
- `NOT_REVIEWABLE`

The reviewer may recommend a downgrade. The reviewer may not upgrade a frozen claim without a separate amendment and new supporting evidence.

## 13. Gap-Level Review Method

The reviewer must evaluate each gap with fields for gap_id, severity, status, blocker fields, Package representation, recommended action, closure condition, review decision, finding ID, and reviewer note.

Gap-level decisions:

- `CONFIRMED_OPEN`
- `CONFIRMED_ACCEPTED_LIMITATION`
- `WORDING_CORRECTION_REQUIRED`
- `SEVERITY_REVIEW_REQUIRED`
- `BLOCKER_REVIEW_REQUIRED`
- `CLOSURE_EVIDENCE_REQUIRED`
- `UNRESOLVED`

No gap may be closed solely because the reviewer agrees with the Package.

## 14. Numerical Review Method

The default External Validation is document and evidence-trace review. The reviewer must compare Package numbers to indexed authoritative artifacts, verify signs, units, labels, and dataset context, verify pilot/development/test terminology, and verify no value is presented as a common benchmark without justification.

The reviewer is not required to recompute metrics. If recomputation is requested, it requires a separate task with frozen protocol, authorized inputs, source scripts, environment record, output path, hashes, and review decision.

## 15. Reproducibility and Lineage Review

The reviewer must inspect the Artifact Index, dataset hash status, source-script lineage status, historical document status, hash sources, broken-path status, authority level, and known limitations.

The reviewer must distinguish result correctness, result traceability, and result reproducibility. Incomplete reproducibility does not automatically invalidate a result, but it must constrain claim strength.

## 16. Marine Boundary Review

Marine boundary decisions:

- `NO_UNSUPPORTED_MARINE_CLAIMS`
- `MARINE_WORDING_CORRECTION_REQUIRED`
- `MARINE_IMPLICATION_UNRESOLVED`

The reviewer must explicitly confirm whether the Package avoids Marine validity, Marine feasibility, Marine deployment, shipboard failure prediction, shipboard RUL, validated shipboard alarms, Marine data receipt, and Marine data qualification.

## 17. Process-State Review

The reviewer must confirm:

- Marine Package: Complete and Frozen
- External Validation: Under review only after execution begins
- Marine request: Planned, not started
- Marine data received: No
- Marine intake: Not started
- Marine qualification: Not started
- Marine validation: Not started

Any discrepancy is a blocking review finding.

## 18. Candidate-Tool Review

The reviewer must compare all T-001 through T-009 fields with the frozen Structure: tool ID, conceptual purpose, method route, supported decision, unsupported decision, readiness, Marine validation requirement, minimum data assumption, and main safety boundary.

Any mismatch requires correction or formal amendment.

## 19. Review Decision Labels

The final External Validation decision must use exactly one label:

- `EXTERNAL_VALIDATION_ACCEPTED`
- `EXTERNAL_VALIDATION_ACCEPTED_WITH_NONBLOCKING_FINDINGS`
- `EXTERNAL_VALIDATION_REVISION_REQUIRED`
- `EXTERNAL_VALIDATION_RECONCILIATION_REQUIRED`
- `EXTERNAL_VALIDATION_REJECTED`
- `EXTERNAL_VALIDATION_INCOMPLETE`
- `EXTERNAL_VALIDATION_NOT_REVIEWABLE`

`EXTERNAL_VALIDATION_ACCEPTED` means no blocking findings and no unresolved claim, gap, numerical, Marine-boundary, or process-state contradictions. `EXTERNAL_VALIDATION_ACCEPTED_WITH_NONBLOCKING_FINDINGS` means only nonblocking editorial, navigation, or minor lineage findings remain. `EXTERNAL_VALIDATION_REVISION_REQUIRED` means correctable Package or documentation issues exist and frozen evidence does not require reconciliation. `EXTERNAL_VALIDATION_RECONCILIATION_REQUIRED` means a material contradiction exists among claims, evidence, gaps, hashes, classifications, or process states. `EXTERNAL_VALIDATION_REJECTED` means the Package materially misrepresents evidence or boundaries and cannot be accepted without major reconstruction. `EXTERNAL_VALIDATION_INCOMPLETE` means required review scope was not completed. `EXTERNAL_VALIDATION_NOT_REVIEWABLE` means evidence access, reviewer independence, or artifact integrity is insufficient for a valid review.

## 20. Finding Severity

Finding severity labels:

- `CRITICAL`: invalidates the review or Package integrity.
- `HIGH`: blocks acceptance or Marine request readiness.
- `MEDIUM`: requires correction before final acceptance unless explicitly waived with documented rationale.
- `LOW`: nonblocking correction.
- `INFORMATIONAL`: observation with no required correction.

Blocking categories include unsupported Marine validity implication, false Marine data receipt or qualification, false External Validation completion, claim support upgrade without evidence, missing frozen claim, missing active gap, incorrect blocker classification affecting the Marine request, canonical numerical contradiction, candidate-tool semantic drift, broken authoritative evidence path, material hash mismatch, reviewer independence failure, incomplete required review scope, non-human reviewer identity, AI-only review, materially undisclosed AI assistance, and absent human accountability.

## 21. Required Corrections

Every correction must include finding_id, affected file, affected section, problem statement, required change, evidence basis, severity, blocking status, responsible party, verification method, and resolution state.

Correction states:

- `OPEN`
- `IN_PROGRESS`
- `RESOLVED_PENDING_REVIEW`
- `VERIFIED_CLOSED`
- `ACCEPTED_NONBLOCKING`
- `REJECTED`

## 22. Disagreement and Appeal Handling

Disagreement sequence:

1. Reviewer records the finding.
2. Project owner may provide a written response.
3. Reviewer may confirm, revise, or withdraw the finding.
4. Unresolved disagreements remain visible.
5. A second reviewer may be appointed for material disputes.
6. The project owner may not unilaterally mark a reviewer finding closed.

Dispute outcomes:

- `REVIEWER_POSITION_CONFIRMED`
- `PROJECT_RESPONSE_ACCEPTED`
- `WORDING_COMPROMISE_ACCEPTED`
- `SECOND_REVIEW_REQUIRED`
- `UNRESOLVED_DISAGREEMENT`

## 23. Review Iteration Rules

Allowed iterations are initial review, correction round, verification review, and final decision. Endless silent editing is not allowed.

Every iteration must have iteration ID, input hashes, findings opened, findings resolved, files changed, final hashes, and reviewer decision.

## 24. Completion Criteria

External Validation is complete only when an eligible human reviewer is formally appointed, independence and conflicts are recorded, the required evidence package is delivered, all required review sections are completed, all 40 claims are reviewed, all 27 gaps are reviewed, all 9 candidate tools are checked, Marine and process-state boundaries are reviewed, all blocking findings are resolved or the review is formally rejected, a final decision record is signed or explicitly approved, and final reviewed hashes are recorded.

Creating this specification alone does not complete External Validation.

## 25. Failure and Abstention Criteria

The reviewer must abstain or issue `NOT_REVIEWABLE` when required evidence is missing, hash integrity cannot be established, reviewer independence is compromised, review scope is materially restricted, the reviewer lacks competence for the required scope, or blocked data or unauthorized execution is required to answer a mandatory question.

Additional not-reviewable or reconciliation conditions are: a non-human system is presented as the External Reviewer, the reviewer identity is an AI system or autonomous agent, a human reviewer merely adopts an AI-generated result without independent review, a project-participating AI system controls the final decision, AI assistance is used but materially undisclosed, or human accountability for the final decision cannot be established.

## 26. External Validation Record

The final record must include reviewer identity, eligibility and independence result, evidence package hash, review scope completion, claim and gap review results, numerical and lineage review, Marine boundary review, process-state review, candidate-tool review, findings, corrections, unresolved disagreements, final decision, Marine Request Gate decision, final hashes, signature or approval record, and date.

If AI tools are used by the human reviewer, the review record must disclose the AI system used, purpose of use, artifacts or sections affected, whether the AI generated findings, how the human reviewer verified those findings, and whether any reviewer decision was changed after human inspection. Required fields are `AI assistance used: Yes / No`, and if Yes, `AI assistance disclosure: Complete` and `Human independent verification: Confirmed`.

AI assistance does not transfer reviewer authority to the AI system.

## 27. Marine Request Gate

The Marine request gate may open only if Marine Package v1.0 remains complete and frozen, the External Validation final decision is `EXTERNAL_VALIDATION_ACCEPTED` or `EXTERNAL_VALIDATION_ACCEPTED_WITH_NONBLOCKING_FINDINGS`, all blocking findings are closed, G-005 closure criteria are satisfied, G-021 closure criteria are satisfied, and the final decision record explicitly states `MARINE_REQUEST_GATE_OPEN`.

The External Reviewer is a verified human individual.

Reviewer independence has been established.

Any AI assistance has been disclosed.

The final decision is personally approved by the human reviewer.

The gate remains blocked for `EXTERNAL_VALIDATION_REVISION_REQUIRED`, `EXTERNAL_VALIDATION_RECONCILIATION_REQUIRED`, `EXTERNAL_VALIDATION_REJECTED`, `EXTERNAL_VALIDATION_INCOMPLETE`, and `EXTERNAL_VALIDATION_NOT_REVIEWABLE`. The gate also remains blocked if the reviewer is non-human, reviewer identity is unclear, human ownership of the decision is absent, AI-only review was performed, or AI assistance was materially undisclosed.

This definition task leaves the gate `MARINE_REQUEST_GATE_NOT_EVALUATED`.

Opening the Marine Request Gate authorizes a separate Marine data request
preparation and initiation workstream.

It does not itself create, approve, send, or start the Marine data request.

After a gate-open decision, the Marine data request remains planned and not
started until a separately authorized execution task records request package
preparation, approval, transmission, and process-state change.

Next authorized workstream after gate opening:
`MARINE_DATA_REQUEST_INITIATION_TASK_REQUIRED`

Required distinctions:

- `MARINE_REQUEST_GATE_OPEN`: authorization to prepare/initiate a later task
- Marine data request started: No
- Request sent: No
- Data received: No

## 28. Change Control

Once frozen, substantive changes to the specification require version increment, change record, hash refresh, review, Documentation Map update, Artifact Index update, and Gap Register status review where applicable.

Substantive changes include reviewer eligibility, independence criteria, decision labels, completion criteria, Marine request gate conditions, blocking finding definitions, and required evidence scope. Editorial corrections may use a controlled metadata correction.

## 29. Security and Confidentiality

The reviewer receives only authorized artifacts. Credentials are excluded. Personal files are excluded. Unrelated private data are excluded. Redistribution requires permission. Review correspondence is retained. Sensitive future Marine data require a separate access protocol.

Current public-data artifacts are not assumed confidential unless marked.

## 30. Final Definition State

Definition state: `EXTERNAL_VALIDATION_DEFINITION_APPROVED_AND_FROZEN`

External Validation execution state: `NOT_STARTED`

External reviewer: Not selected

Marine request gate state: `MARINE_REQUEST_GATE_NOT_EVALUATED`

Next authorized phase: `EXTERNAL_VALIDATION_REVIEWER_SELECTION_AND_APPOINTMENT_001`
