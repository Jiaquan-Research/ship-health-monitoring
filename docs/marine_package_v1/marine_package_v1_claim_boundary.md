# Marine Package v1.0 Claim Boundary

Document status: Frozen  
Version: v1.0  
Phase: Framework Freeze  
Marine validity: Not claimed  
Marine data request status: Planned, not started

## 1. Purpose

This document freezes the claim taxonomy, evidence categories, supported wording, prohibited wording, and amendment rules for Marine Package v1.0 before detailed evidence mapping begins.

No Marine validity claimed. Marine data request remains planned but not started. External Validation of Project Results remains planned and incomplete.

## 2. Claim ID Namespace

| Namespace | Meaning |
|---|---|
| `C-xxx` | CODLAG claims |
| `PR-xxx` | PRONOSTIA claims |
| `R-xxx` | Residual-route claims |
| `N-xxx` | Nonresidual-route claims |
| `F-xxx` | Framework claims |
| `P-xxx` | Product-boundary claims |
| `M-xxx` | Marine-interface and Marine-process claims |
| `G-xxx` | Gap IDs |
| `T-xxx` | Candidate tool IDs |

Reserved ranges:

- `001-099`: core Package v1.0 claims
- `100-199`: future Marine validation claims
- `200-299`: future deployment and operational claims

Existing IDs must not be renumbered. Gap IDs and Tool IDs must not be reused as claim IDs.

## 3. Independent Classification Axes

| Axis | Allowed values | Definition |
|---|---|---|
| `support_status` | `SUPPORTED`, `SUPPORTED_WITH_LIMITATIONS`, `PILOT_EVIDENCE_ONLY`, `DEVELOPMENT_EVIDENCE_ONLY`, `DESIGN_ONLY`, `UNRESOLVED`, `UNSUPPORTED`, `NOT_TESTED`, `NOT_STARTED`, `OUT_OF_SCOPE` | How strongly is this claim supported within its stated scope? |
| `claim_type` | `EMPIRICAL_RESULT`, `EMPIRICAL_PILOT_RESULT`, `DEVELOPMENT_RESULT`, `BOUNDARY_CLAIM`, `ARCHITECTURAL_CONCEPTUAL`, `STRUCTURAL_INFERENCE`, `PROCESS_STATE`, `PLANNED_PROCESS_RULE`, `PRODUCT_HYPOTHESIS`, `NON_CLAIM` | What kind of statement is this? |
| `support_basis` | `REVIEWED_NUMERICAL_EVIDENCE`, `FROZEN_CLOSURE_RECORD`, `DEVELOPMENT_REVIEW_RECORD`, `PILOT_ARTIFACTS_AND_REVIEW`, `METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS`, `ARCHITECTURAL_REASONING`, `USER_CONFIRMED_REAL_WORLD_STATUS`, `USER_CONFIRMED_PROJECT_DECISION`, `CANONICAL_TEMPLATE_EXISTENCE`, `DOCUMENTED_SCOPE_BOUNDARY`, `NONE` | What evidence or authority supports the claim? |
| `marine_transfer_status` | `NO_MARINE_CLAIM`, `STRUCTURAL_RELEVANCE_ONLY`, `MARINE_HYPOTHESIS`, `MARINE_VALIDATION_REQUIRED`, `MARINE_SUPPORTED` | What, if anything, can this claim imply for Marine use? |

`MARINE_SUPPORTED` must not be used in Marine Package v1.0 Phase 1 or Phase 2 unless direct reviewed Marine evidence exists.

Evidence strength is separate:

| evidence_strength | Definition |
|---|---|
| `STRONG` | Reviewed numerical evidence with clear lineage plus held-out or cross-model support. |
| `MODERATE` | Reviewed numerical evidence with documented limitations. |
| `LIMITED` | Development-only, pilot-only, incomplete-review, or lineage-limited evidence. |
| `DESIGN` | Architecture, interface, planned method, or planned process only. |
| `NONE` | No supporting evidence. |

Documented source-specific `support_basis` values:

| support_basis | Meaning |
|---|---|
| `NCMAPSS_DS02_RESIDUAL_PILOT_ARTIFACTS_AND_REVIEW` | N-CMAPSS DS02 residual pilot artifacts and review records support the pilot claim. |
| `NCMAPSS_DS02_PILOT_CLOSURE_BOUNDARY` | N-CMAPSS DS02 pilot closure boundary records support the non-Marine boundary claim. |
| `PILOT_RESULT_AND_METHOD_STRUCTURE` | The pilot result and method structure support a bounded structural inference. |

## 4. Claim Register

| ID | Claim | support_status | claim_type | support_basis | marine_transfer_status | evidence_strength |
|---|---|---|---|---|---|---|
| C-001 | Single-variable condition normalization may be insufficient to separate healthy and degraded states. | SUPPORTED_WITH_LIMITATIONS | BOUNDARY_CLAIM | REVIEWED_NUMERICAL_EVIDENCE | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| C-002 | Residual evidence may remain hidden when operating-condition representation is under-specified. | SUPPORTED_WITH_LIMITATIONS | BOUNDARY_CLAIM | REVIEWED_NUMERICAL_EVIDENCE | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| C-003 | Stratified residual analysis can recover degradation structure that is not visible in globally pooled residuals. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | REVIEWED_NUMERICAL_EVIDENCE | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| C-004 | Residual-route feasibility depends on condition-variable sufficiency, not only model capacity. | SUPPORTED_WITH_LIMITATIONS | STRUCTURAL_INFERENCE | REVIEWED_NUMERICAL_EVIDENCE | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| PR-001 | Fixed-condition datasets may not support or require a meaningful Expected State residual model. | SUPPORTED_WITH_LIMITATIONS | BOUNDARY_CLAIM | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| PR-002 | When operating-condition variation is minimal, direct progression or nonresidual analysis may be more appropriate than condition-normalized residual modelling. | SUPPORTED_WITH_LIMITATIONS | STRUCTURAL_INFERENCE | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| PR-003 | Method selection must depend on the operating-condition structure of the dataset and equipment. | SUPPORTED_WITH_LIMITATIONS | STRUCTURAL_INFERENCE | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| PR-004 | Non-application of an Expected State model in a fixed-condition case is a method boundary, not necessarily an experimental failure. | SUPPORTED_WITH_LIMITATIONS | BOUNDARY_CLAIM | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| R-001 | Expected State modelling can remove part of operating-condition variation. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-002 | Residuals can carry progression-related information. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-003 | Residual evidence remained similar under BL150 and BL175. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-004 | A small primary channel set can be selected from residual evidence. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-005 | A scalar HI can be constructed from selected residual evidence. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-006 | The canonical FD002 HI showed positive unit-level progression association. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-007 | poly3 and ridge provided cross-model support. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-008 | poly1 acted as an underfit negative control. | SUPPORTED_WITH_LIMITATIONS | EMPIRICAL_RESULT | FROZEN_CLOSURE_RECORD | STRUCTURAL_RELEVANCE_ONLY | MODERATE |
| R-009 | N-CMAPSS DS02 produced a development-stage residual pilot signal under continuous and interacting operating conditions. | PILOT_EVIDENCE_ONLY | EMPIRICAL_PILOT_RESULT | NCMAPSS_DS02_RESIDUAL_PILOT_ARTIFACTS_AND_REVIEW | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| R-010 | The N-CMAPSS DS02 residual result is pilot evidence only and does not establish Marine validity, general residual-route validation, or deployment readiness. | SUPPORTED | BOUNDARY_CLAIM | NCMAPSS_DS02_PILOT_CLOSURE_BOUNDARY | NO_MARINE_CLAIM | LIMITED |
| R-011 | The N-CMAPSS DS02 residual pilot suggests that nonlinear condition modelling may be necessary when operating conditions are continuous and interacting. | SUPPORTED_WITH_LIMITATIONS | STRUCTURAL_INFERENCE | PILOT_RESULT_AND_METHOD_STRUCTURE | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| N-001 | RAW trend can provide development-stage progression evidence. | DEVELOPMENT_EVIDENCE_ONLY | DEVELOPMENT_RESULT | DEVELOPMENT_REVIEW_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| N-002 | DELTA from reference can provide development-stage progression evidence. | DEVELOPMENT_EVIDENCE_ONLY | DEVELOPMENT_RESULT | DEVELOPMENT_REVIEW_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| N-003 | EWMA can provide development-stage smoothed progression evidence. | DEVELOPMENT_EVIDENCE_ONLY | DEVELOPMENT_RESULT | DEVELOPMENT_REVIEW_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| N-004 | CUSUM showed strong sensitivity to temporally ordered deviations. | DEVELOPMENT_EVIDENCE_ONLY | DEVELOPMENT_RESULT | DEVELOPMENT_REVIEW_RECORD | STRUCTURAL_RELEVANCE_ONLY | LIMITED |
| N-005 | CUSUM specificity and reference-period interpretation remain unresolved. | UNRESOLVED | BOUNDARY_CLAIM | DEVELOPMENT_REVIEW_RECORD | NO_MARINE_CLAIM | LIMITED |
| N-006 | The DS02 nonresidual test gate was not opened. | SUPPORTED | BOUNDARY_CLAIM | FROZEN_CLOSURE_RECORD | NO_MARINE_CLAIM | LIMITED |
| N-007 | Nonresidual methods are candidate approaches for low-data self-baseline trend monitoring. | DESIGN_ONLY | PRODUCT_HYPOTHESIS | ARCHITECTURAL_REASONING | STRUCTURAL_RELEVANCE_ONLY | DESIGN |
| F-001 | Residual and nonresidual routes address different operational questions. | SUPPORTED_WITH_LIMITATIONS | ARCHITECTURAL_CONCEPTUAL | METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS | STRUCTURAL_RELEVANCE_ONLY | DESIGN |
| F-002 | Residual routes require stronger condition coverage and Expected State support. | SUPPORTED_WITH_LIMITATIONS | ARCHITECTURAL_CONCEPTUAL | METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS | STRUCTURAL_RELEVANCE_ONLY | DESIGN |
| F-003 | Nonresidual routes can operate under weaker data conditions but provide weaker causal attribution. | SUPPORTED_WITH_LIMITATIONS | ARCHITECTURAL_CONCEPTUAL | METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS | STRUCTURAL_RELEVANCE_ONLY | DESIGN |
| F-004 | Maintenance reset is necessary for lifecycle interpretation. | DESIGN_ONLY | ARCHITECTURAL_CONCEPTUAL | METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS | MARINE_VALIDATION_REQUIRED | DESIGN |
| F-005 | Public-data evidence does not establish Marine validity. | SUPPORTED | BOUNDARY_CLAIM | DOCUMENTED_SCOPE_BOUNDARY | NO_MARINE_CLAIM | MODERATE |
| F-006 | Health Assessment has not been completed. | SUPPORTED | BOUNDARY_CLAIM | DOCUMENTED_SCOPE_BOUNDARY | NO_MARINE_CLAIM | MODERATE |
| F-007 | Deployment readiness has not been demonstrated. | SUPPORTED | BOUNDARY_CLAIM | DOCUMENTED_SCOPE_BOUNDARY | NO_MARINE_CLAIM | MODERATE |
| F-008 | Decision-support tools may exist below the full Health Assessment layer. | DESIGN_ONLY | ARCHITECTURAL_CONCEPTUAL | ARCHITECTURAL_REASONING | MARINE_VALIDATION_REQUIRED | DESIGN |
| M-001 | Canonical Marine request, intake, sensor inventory, and variable-role mapping templates exist. | SUPPORTED | PROCESS_STATE | CANONICAL_TEMPLATE_EXISTENCE | NO_MARINE_CLAIM | DESIGN |
| M-002 | Existence of the templates does not mean that the Marine data request has started. | SUPPORTED | BOUNDARY_CLAIM | DOCUMENTED_SCOPE_BOUNDARY | NO_MARINE_CLAIM | DESIGN |
| M-003 | The Marine data request process is currently planned but not started. | SUPPORTED | PROCESS_STATE | USER_CONFIRMED_REAL_WORLD_STATUS | NO_MARINE_CLAIM | DESIGN |
| M-004 | Marine Package v1.0 and the External Validation of Project Results document are the planned prerequisites for initiating the first formal Marine data request. | DESIGN_ONLY | PLANNED_PROCESS_RULE | USER_CONFIRMED_PROJECT_DECISION | MARINE_VALIDATION_REQUIRED | DESIGN |
| M-005 | No Marine dataset has been received or qualified. | SUPPORTED | PROCESS_STATE | USER_CONFIRMED_REAL_WORLD_STATUS | NO_MARINE_CLAIM | DESIGN |
| M-006 | Direct Marine validation has not started. | SUPPORTED | BOUNDARY_CLAIM | DOCUMENTED_SCOPE_BOUNDARY | NO_MARINE_CLAIM | DESIGN |

R-011 is an inference supported by the pilot and method structure. It must not be represented as proof that nonlinear models are always required.

## 5. Permitted Package Wording

Permitted Package Wording includes claims from different support levels, including supported, supported-with-limitations, development-only, pilot-only, boundary, and process-state statements.

Permission to use wording does not mean that all listed statements have the same evidence strength.

Permitted wording:

- Public-data evidence supports the technical feasibility of the residual-to-Evidence-to-HI route.
- Development evidence supports RAW, DELTA, and EWMA as candidate nonresidual trend methods.
- CODLAG and PRONOSTIA expose method-selection and condition-representation boundaries.
- CUSUM remains unresolved because sensitivity was not matched by sufficient specificity and reference-period interpretability.
- Residual and nonresidual routes serve different conceptual and operational roles.
- The Marine data request process is planned but has not started.
- Completion of Marine Package v1.0 and the External Validation of Project Results document is the planned prerequisite for initiating the request.

## 6. Supported Claims

Supported claims are the rows with `support_status = SUPPORTED`. They include boundary claims and process-state claims. They do not imply uniform evidence strength.

## 7. Supported-With-Limitations Claims

Supported-with-limitations claims include CODLAG, PRONOSTIA, FD002 residual-route claims, R-011, and architecture claims F-001 to F-003. Their limitations must travel with any reuse.

## 8. Pilot-Only Claims

R-009 is pilot-only. It must not be upgraded into general residual-route validation or Marine validation.

## 9. Development-Only Claims

N-001 through N-004 are development-only. RAW, DELTA, and EWMA produced accepted development-stage evidence. CUSUM sensitivity did not establish operational specificity.

## 10. Unresolved Claims

N-005 is unresolved. CUSUM remains unresolved and must not be described as an operationally validated alarm method.

## 11. Marine Process Claims

| Field | Value |
|---|---|
| request_package_status | NOT_STARTED |
| request_sent_status | NOT_SENT |
| response_status | NOT_APPLICABLE |
| data_received_status | NO |
| intake_status | NOT_STARTED |
| qualification_status | NOT_STARTED |
| process_status | PLANNED_NOT_STARTED |
| status_source | USER_CONFIRMED_REAL_WORLD_STATUS |
| last_confirmed_date | 2026-07-12 |

Marine request start condition:

```text
Marine Package v1.0 completed
AND
External Validation of Project Results completed
```

## 12. Marine and Product Non-Claims

No current package claim may state or imply direct Marine validation has started, Marine data have been received, Marine data have been qualified, Marine evidence exists, Marine feasibility is established, Marine validity is established, deployment readiness is established, Health Assessment is complete, or RUL prediction for shipboard equipment is available.

## 13. Residual/Nonresidual Conceptual Boundary

The residual-versus-nonresidual distinction is an architectural and operational boundary inferred from method design and separate public-data experiments. It is not a formal same-dataset head-to-head comparison.

## 14. Gap ID Authority

The Phase 1 definitions of G-001 through G-006 are authoritative.

Any earlier planning document that used these IDs for different meanings is superseded for Marine Package v1.0.

Phase 2 must preserve G-001 through G-006 and continue new gap numbering from G-007.

Existing gap IDs must not be renumbered.

| Gap ID | Definition |
|---|---|
| G-001 | Same-dataset residual/nonresidual head-to-head comparison absent. |
| G-002 | FD002 historical dataset-hash and source-script lineage incomplete. |
| G-003 | DS02 nonresidual CUSUM unresolved and test gate unopened. |
| G-004 | Marine request status may be confused with template readiness. |
| G-005 | External Validation of Project Results is planned but not yet defined. |
| G-006 | Candidate-tool readiness remains conceptual or implementation-planning only. |

## 15. Tool-Readiness Terminology Boundary

Allowed readiness values:

- `CONCEPT_ONLY`
- `READY_FOR_PROTOTYPING`
- `PROTOTYPE_EXISTS_UNREVIEWED`
- `PROTOTYPE_REVIEWED`
- `REQUIRES_MARINE_DATA`
- `REQUIRES_METHOD_VALIDATION`
- `NOT_READY`

`READY_FOR_PROTOTYPING` means that current evidence is sufficient to begin implementation planning. It does not mean that a prototype already exists.

Phase 1 readiness labels are implementation-planning labels, not product validation decisions.

## 16. Prohibited Wording

Prohibited wording:

- Marine validity has been demonstrated.
- The framework predicts shipboard equipment failure.
- The HI represents true physical degradation.
- The system estimates remaining useful life for shipboard equipment.
- The framework is deployment ready.
- CUSUM is validated for operational alarm use.
- FD002 proves shipboard applicability.
- Residual methods are universally superior to nonresidual methods.
- Nonresidual methods are empirically proven to be better for low-data Marine systems.
- The Marine data request is underway.
- Marine data are pending delivery.
- External validation has been completed.

## 17. Claim Retirement and Amendment Rules

Existing IDs must never be renumbered after freeze. Retired claims retain their ID and are marked `RETIRED`. Reworded claims retain their ID only if their meaning is unchanged. Meaningfully changed claims receive a new ID. New claims append using the next unused number. Future Marine validation claims must use the reserved `100-199` range. Future deployment and operational claims must use the reserved `200-299` range.

## 18. Final Framework State

Readiness decision:

`MARINE_PACKAGE_V1_FRAMEWORK_READY_FOR_EVIDENCE_MAPPING`

Framework state:

`MARINE_PACKAGE_V1_FRAMEWORK_FROZEN`

## 19. Phase 2 Reconciliation Findings

Evidence map: `docs/marine_package_v1/marine_package_v1_evidence_map.csv`

Artifact index: `docs/marine_package_v1/marine_package_v1_artifact_index.md`

Gap register: `docs/marine_package_v1/marine_package_v1_gap_register.md`

Phase 2 reconciliation completed:

- primary evidence mapping corrected
- artifact hash linkage verified
- artifact roles recalibrated
- gap severity and blockers recalibrated
- all 40 frozen claims mapped
- no claim text changes
- no claim classification changes
- no framework conflicts
- G-001 through G-027 preserved

Phase 2 readiness decision:

`MARINE_PACKAGE_V1_READY_FOR_DRAFTING_WITH_DOCUMENTED_GAPS`

Document status remains Frozen v1.0. This section records Phase 2 references only and does not amend the frozen claim register.
