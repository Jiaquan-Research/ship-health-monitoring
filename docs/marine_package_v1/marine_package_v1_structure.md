# Marine Package v1.0 Structure

Document status: Frozen  
Version: v1.0  
Package: Marine Package v1.0  
Phase: Framework Freeze  
Marine validity: Not claimed  
Marine data request status: Planned, not started

## 1. Executive Summary

Marine Package v1.0 will organize the public-data validation evidence, framework boundaries, Marine intake interface, supported claims, unsupported claims, and next validation requirements needed before a formal Marine data request begins.

This framework freeze defines the package structure and claim-language foundation only. It does not create the complete evidence map, artifact inventory, final gap severity assessment, Marine Package narrative, or External Validation of Project Results document.

Readiness decision:

`MARINE_PACKAGE_V1_FRAMEWORK_READY_FOR_EVIDENCE_MAPPING`

## 2. Claim ID Namespace Rules

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

Each namespace starts at 001. Existing IDs must never be renumbered after freeze. New claims append using the next unused number. Retired claims retain their ID and are marked `RETIRED`. Reworded claims retain their ID only if their meaning is unchanged. Meaningfully changed claims receive a new ID. The same ID must refer to the same claim across all Package files.

Reserved ranges:

| Range | Use |
|---|---|
| `001-099` | core Package v1.0 claims |
| `100-199` | future Marine validation claims |
| `200-299` | future deployment and operational claims |

Positive Marine validation or deployment claims must not be assigned into the core range.

## 3. Independent Classification Axes

The framework uses four independent claim-classification axes plus a separate evidence-strength field.

| Axis | Allowed values | Definition |
|---|---|---|
| `support_status` | `SUPPORTED`, `SUPPORTED_WITH_LIMITATIONS`, `PILOT_EVIDENCE_ONLY`, `DEVELOPMENT_EVIDENCE_ONLY`, `DESIGN_ONLY`, `UNRESOLVED`, `UNSUPPORTED`, `NOT_TESTED`, `NOT_STARTED`, `OUT_OF_SCOPE` | How strongly is this claim supported within its stated scope? |
| `claim_type` | `EMPIRICAL_RESULT`, `EMPIRICAL_PILOT_RESULT`, `DEVELOPMENT_RESULT`, `BOUNDARY_CLAIM`, `ARCHITECTURAL_CONCEPTUAL`, `STRUCTURAL_INFERENCE`, `PROCESS_STATE`, `PLANNED_PROCESS_RULE`, `PRODUCT_HYPOTHESIS`, `NON_CLAIM` | What kind of statement is this? |
| `support_basis` | `REVIEWED_NUMERICAL_EVIDENCE`, `FROZEN_CLOSURE_RECORD`, `DEVELOPMENT_REVIEW_RECORD`, `PILOT_ARTIFACTS_AND_REVIEW`, `METHOD_DESIGN_AND_SEPARATE_EXPERIMENTS`, `ARCHITECTURAL_REASONING`, `USER_CONFIRMED_REAL_WORLD_STATUS`, `USER_CONFIRMED_PROJECT_DECISION`, `CANONICAL_TEMPLATE_EXISTENCE`, `DOCUMENTED_SCOPE_BOUNDARY`, `NONE` | What evidence or authority supports the claim? |
| `marine_transfer_status` | `NO_MARINE_CLAIM`, `STRUCTURAL_RELEVANCE_ONLY`, `MARINE_HYPOTHESIS`, `MARINE_VALIDATION_REQUIRED`, `MARINE_SUPPORTED` | What, if anything, can this claim imply for Marine use? |

`MARINE_SUPPORTED` must not be used anywhere in Marine Package v1.0 Phase 1 or Phase 2 unless direct reviewed Marine evidence exists.

Evidence strength is separate:

| evidence_strength | Definition |
|---|---|
| `STRONG` | Reviewed numerical evidence with clear lineage plus held-out or cross-model support. |
| `MODERATE` | Reviewed numerical evidence with documented limitations. |
| `LIMITED` | Development-only, pilot-only, incomplete-review, or lineage-limited evidence. |
| `DESIGN` | Architecture, interface, planned method, or planned process only. |
| `NONE` | No supporting evidence. |

`support_status` is not `evidence_strength`. `marine_transfer_status` is not `evidence_strength`. `claim_type` is not `evidence_strength`. `support_basis` is not `evidence_strength`.

Documented source-specific `support_basis` values:

| support_basis | Meaning |
|---|---|
| `NCMAPSS_DS02_RESIDUAL_PILOT_ARTIFACTS_AND_REVIEW` | N-CMAPSS DS02 residual pilot artifacts and review records support the pilot claim. |
| `NCMAPSS_DS02_PILOT_CLOSURE_BOUNDARY` | N-CMAPSS DS02 pilot closure boundary records support the non-Marine boundary claim. |
| `PILOT_RESULT_AND_METHOD_STRUCTURE` | The pilot result and method structure support a bounded structural inference. |

## 4. Package Structure Matrix

| Section | Section purpose | Claim namespaces involved | Required evidence type | Current evidence category | Known boundary | Missing input | Authoritative source category | Phase 2 mapping requirement |
|---|---|---|---|---|---|---|---|---|
| 1. Executive Summary | State package purpose and closure boundary | F, M, P | Reviewed source summaries | DESIGN_ONLY | not final package narrative | evidence map | package framework | map all claim summaries |
| 2. Engineering Problem Definition | Define shipboard monitoring problem | F, P | Framework architecture and public-data limits | STRUCTURAL_RELEVANCE_ONLY | no Marine dataset | Marine use case evidence | architecture docs | map problem claims to sources |
| 3. Intended User and Operational Context | Identify intended reader and operational setting | P, M | Product and Marine-process boundaries | DESIGN_ONLY | no deployment claim | Marine stakeholder input | process inputs | map user assumptions |
| 4. System Boundary | Separate framework, package, and future system | F, P | Boundary documents | SUPPORTED_WITH_LIMITATIONS | no deployment readiness | final product scope | decision docs | map supported/non-supported boundaries |
| 5. Framework Architecture | Define residual, Evidence, HI, Assessment layers | F, R, N | Architecture and closure evidence | SUPPORTED_WITH_LIMITATIONS | no Health Assessment completion | layer evidence map | framework docs | map layer-by-layer claims |
| 6. Dataset and Method Selection Logic | Explain dataset roles | C, PR, R, N | Dataset qualification and closures | SUPPORTED_WITH_LIMITATIONS | no direct Marine evidence | Phase 2 source expansion | dataset docs | expand dataset role table |
| 7. Data Qualification and Baseline Management | Define qualification and reset concerns | F, M, G | Qualification docs and templates | DESIGN_ONLY | no Marine data qualified | Marine delivery package | qualification docs | map qualification controls |
| 8. Expected State and Residual Route | Define residual-route evidence | R, C | FD002, CODLAG, DS02 residual evidence | SUPPORTED_WITH_LIMITATIONS | no Marine residual validity | evidence map | FD002/CODLAG/DS02 records | map R/C claims |
| 9. Nonresidual Route | Define RAW, DELTA, EWMA, CUSUM boundary | N | DS02 development closure | DEVELOPMENT_EVIDENCE_ONLY | test gate unopened | future execution decision | DS02 closure | map N claims and unresolved CUSUM |
| 10. Health Evidence Layer | Define channel evidence layer | R, F | FD002 Health Evidence outputs | SUPPORTED_WITH_LIMITATIONS | not Health Assessment | final evidence map | FD002 closure | map Evidence claims |
| 11. Health Indicator Layer | Define canonical HI evidence | R, F | FD002 HI closure | SUPPORTED_WITH_LIMITATIONS | not physical calibration | final evidence map | HI closure | map HI claims |
| 12. Health Assessment Boundary | State not completed | F, P | Closure boundaries | SUPPORTED | Assessment not performed | future Assessment design | closure docs | map non-claims |
| 13. Public-Data Validation Evidence | Summarize public-data evidence only | C, PR, R, N | Closed public-data records | SUPPORTED_WITH_LIMITATIONS | no Marine validity | complete artifact index | closures | build evidence map |
| 14. Dataset Boundary Cases | Use CODLAG/PRONOSTIA/DS02 as boundary cases | C, PR, N, R | Boundary audits | STRUCTURAL_RELEVANCE_ONLY | analogies only | source expansion | boundary docs | map each boundary claim |
| 15. Residual vs Nonresidual Conceptual Boundary | Define route distinction | F, R, N | Architecture and separate experiments | STRUCTURAL_RELEVANCE_ONLY | no same-dataset head-to-head | comparative study | framework docs | record open gap |
| 16. Maintenance Reset and Lifecycle Handling | Define reset need | F, P | Architecture/design docs | DESIGN_ONLY | no Marine maintenance record | Marine maintenance data | decision docs | map reset gaps |
| 17. Marine Data Request and Intake Interface | Index Marine templates | M | Frozen templates | SUPPORTED | templates are not execution | actual Marine request | Marine templates | map interface fields |
| 18. Marine Applicability Boundary | State transfer limits | F, M, P | Closure and boundary records | SUPPORTED | no direct Marine validation | Marine dataset | all closures | map transfer limitations |
| 19. Candidate Decision-Support Tools | Position conceptual tools | T, P, F | Conceptual route support | DESIGN_ONLY | no product readiness | Marine validation | package framework | map each tool assumption |
| 20. Known Limitations | Consolidate limitations | G, F, M | Reviewed limits | SUPPORTED_WITH_LIMITATIONS | no silent conflict resolution | gap severity audit | closures/audit | create gap register |
| 21. Open Gaps | Register framework-freeze issues | G | Audit evidence | UNRESOLVED | not final severity | Phase 2 gap audit | current docs | expand gap register |
| 22. Proposed Marine Validation Plan | Define future plan boundary | M, F | Planned process | NOT_STARTED | no Marine validation started | Marine data | process input | map plan prerequisites |
| 23. External Validation Requirement | Define future validation document | M, F | Planned process rule | DESIGN_ONLY | external validation not complete | later task | user-confirmed process | create future document |
| 24. Artifact and Reproducibility Index | Placeholder for artifact inventory | G, F | Existing closures/audits | DESIGN_ONLY | not created in this phase | full artifact index | audit outputs | create artifact index |
| 25. Permitted Package Wording | State allowed wording by support level | all claim namespaces | Evidence map | DESIGN_ONLY | not uniform evidence strength | full mapping | all sources | generate final supported claims |
| 26. Unsupported Claims | State non-claims | F, P, M | Boundary docs | SUPPORTED | must avoid overclaim | final review | closures | generate prohibited wording |
| 27. Final Package Boundary | Define final package scope | F, P, M | Package review | DESIGN_ONLY | not final report | final drafting | package framework | close Phase 2 before drafting |

## 5. Dataset Role Table

| Dataset | Package role | Main positive evidence | Main boundary evidence | Claim IDs | Marine transfer status |
|---|---|---|---|---|---|
| CODLAG | Residual feasibility boundary | Stratified residual analysis can recover degradation structure | Under-specified condition representation can hide degradation | `C-001-C-004` | STRUCTURAL_RELEVANCE_ONLY |
| C-MAPSS FD002 | Main residual-route evidence | Residual -> Evidence -> HI -> cross-model support | Historical lineage and deferred sensitivity limitations | `R-001-R-008` | STRUCTURAL_RELEVANCE_ONLY |
| PRONOSTIA | Fixed-condition boundary case | Direct progression analysis remains meaningful | Expected State residual modelling may be unnecessary or unidentifiable under fixed conditions | `PR-001-PR-004` | STRUCTURAL_RELEVANCE_ONLY |
| N-CMAPSS DS02 | Continuous-condition pilot and nonresidual development evidence | Residual pilot signal; RAW / DELTA / EWMA development evidence | No Marine validity; nonresidual test unopened; CUSUM unresolved | `R-009-R-011`; `N-001-N-007` | STRUCTURAL_RELEVANCE_ONLY |

No dataset is direct Marine evidence. Phase 2 evidence mapping must expand directly from these claim ranges.

## 6. Claim Register

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

## 7. Residual vs Nonresidual Boundary

The following residual-versus-nonresidual distinction is an architectural and operational boundary inferred from method design and separate public-data experiments.

It is not the result of a formal same-dataset head-to-head comparison.

The absence of a same-dataset comparison remains an open gap.

Residual route: conceptually best suited to separating operating-condition effects from state-related deviation when condition coverage, data quality, and model quality are sufficient.

Nonresidual route: conceptually best suited to self-baseline trend observation, maintenance-effect tracking, and low-data monitoring when causal attribution is not claimed.

Claim type: `ARCHITECTURAL_CONCEPTUAL`, not `EMPIRICAL_RESULT`.

## 8. Marine Execution Templates

| Template | Repository path | Authority level | Role | Boundary |
|---|---|---|---|---|
| Marine Data Request Template | `docs/validation/marine_execution_package/templates/marine_data_request_and_delivery_specification.md` | CANONICAL | Marine-facing data acquisition request interface | Template readiness yes; request started no. |
| Marine Data Intake Template | `docs/validation/marine_execution_package/templates/marine_data_intake_checklist.md` | CANONICAL | Intake and qualification entry interface | Marine data received no. |
| Sensor Inventory Template | `docs/validation/marine_execution_package/templates/sensor_inventory_template.md` | CANONICAL | Sensor inventory and metadata interface | Marine data qualified no. |
| Variable Role Mapping Template | `docs/validation/marine_execution_package/templates/variable_role_mapping_template.md` | CANONICAL | Variable-role mapping interface | Direct Marine validation not started. |

Role: `CANONICAL_MARINE_INTAKE_INTERFACE`

Template readiness: `YES`  
Marine request started: `NO`  
Marine data received: `NO`  
Marine data qualified: `NO`

## 9. Marine Request Status and Start Condition

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

Marine data request start condition:

```text
Marine Package v1.0 completed
AND
External Validation of Project Results completed
```

The Marine data request has not started because the planned evidence and communication package is not yet complete. This is a planned sequence, not a stalled or failed request process.

## 10. External Validation Requirement

Future document:

`External Validation of Project Results`

Role: an external-facing or independently reviewed assessment of the credibility, scope, limitations, and traceability of the project's completed public-data results.

Boundary:

- The document is planned.
- It is not created during this task.
- Its contents and reviewer mechanism remain to be defined in a later task.
- External validation has not occurred.

## 11. Candidate Decision-Support Tools

Candidate tools may support trend observation, comparison, data readiness, and maintenance-effect tracking. They must not be represented as validated fault diagnosis, remaining-life prediction, automated maintenance authorization, or deployment-ready Marine systems.

Readiness taxonomy:

| Readiness | Meaning |
|---|---|
| CONCEPT_ONLY | Conceptual tool only. |
| READY_FOR_PROTOTYPING | Evidence is sufficient to begin implementation planning; this does not mean a prototype exists. |
| PROTOTYPE_EXISTS_UNREVIEWED | An implementation exists but has not been reviewed. |
| PROTOTYPE_REVIEWED | An implementation exists and has been reviewed. |
| REQUIRES_MARINE_DATA | Marine data are required before meaningful implementation or validation. |
| REQUIRES_METHOD_VALIDATION | Method validation is required before tool positioning can advance. |
| NOT_READY | Not ready for planning or implementation. |

Phase 1 readiness labels are implementation-planning labels, not product validation decisions.

| Tool ID | Conceptual purpose | Method route | Supported decision | Unsupported decision | current_readiness_category | Marine validation requirement | Minimum data assumption | Main safety boundary |
|---|---|---|---|---|---|---|---|---|
| T-001 | Same-condition trend comparison | nonresidual / stratified | compare like-with-like trend | fault diagnosis | CONCEPT_ONLY | Marine same-condition data | stable condition labels | no causal claim |
| T-002 | Self-baseline DELTA dashboard | nonresidual | observe reference-relative change | RUL prediction | READY_FOR_PROTOTYPING | Marine reference review | early reference window | no alarm validation |
| T-003 | EWMA long-term drift monitor | nonresidual | smoothed trend observation | automated maintenance | READY_FOR_PROTOTYPING | Marine drift review | ordered time data | no deployment readiness |
| T-004 | Maintenance before/after comparison | nonresidual | compare pre/post maintenance | maintenance authorization | CONCEPT_ONLY | maintenance event records | timestamped events | reset confounding |
| T-005 | Voyage or watch-to-watch comparison | nonresidual | operational-period comparison | failure prediction | CONCEPT_ONLY | voyage/watch labels | segment metadata | no universal thresholds |
| T-006 | Equipment trend timeline with maintenance events | nonresidual / lifecycle | visualize trend with events | Health Assessment completion | CONCEPT_ONLY | Marine maintenance data | event log | no causal attribution |
| T-007 | Residual monitoring for data-rich equipment | residual | observe condition-normalized deviation | Marine residual validity | REQUIRES_MARINE_DATA | sufficient condition coverage | operating variables | Expected State quality gate |
| T-008 | Evidence and HI dashboard | residual / Evidence / HI | present public-data-derived indicators | physical degradation truth | REQUIRES_METHOD_VALIDATION | Marine Evidence review | selected channels | no Health Assessment |
| T-009 | Data-quality and baseline-readiness checker | intake / qualification | assess readiness | validation success | READY_FOR_PROTOTYPING | Marine intake data | manifest and metadata | readiness is not evidence |

## 12. Gap ID Authority

The Phase 1 definitions of G-001 through G-006 are authoritative.

Any earlier planning document that used these IDs for different meanings is superseded for Marine Package v1.0.

Phase 2 must preserve G-001 through G-006 and continue new gap numbering from G-007.

Existing gap IDs must not be renumbered.

| Gap ID | Definition | Classification |
|---|---|---|
| G-001 | Same-dataset residual/nonresidual head-to-head comparison absent. | PHASE_2_RECONCILIATION_ITEM |
| G-002 | FD002 historical dataset-hash and source-script lineage incomplete. | BOUNDARY_NOTE |
| G-003 | DS02 nonresidual CUSUM unresolved and test gate unopened. | PHASE_2_RECONCILIATION_ITEM |
| G-004 | Marine request status may be confused with template readiness. | BOUNDARY_NOTE |
| G-005 | External Validation of Project Results is planned but not yet defined. | DOCUMENTATION_GAP |
| G-006 | Candidate-tool readiness remains conceptual or implementation-planning only. | BOUNDARY_NOTE |

When Phase 2 needs earlier planning-card gap concepts, assign new IDs starting from `G-007`.

## 13. Permitted Package Wording

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

## 14. Unsupported Claims and Prohibited Wording

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

## 15. Final Framework State

Readiness decision:

`MARINE_PACKAGE_V1_FRAMEWORK_READY_FOR_EVIDENCE_MAPPING`

Framework state:

`MARINE_PACKAGE_V1_FRAMEWORK_FROZEN`

Next authorized phase:

`MARINE_PACKAGE_V1_EVIDENCE_MAPPING_AND_GAP_AUDIT_001`

## 16. Phase 2 Evidence Mapping Status

Phase 2 evidence mapping status: Complete

Phase 2 reconciliation status: Complete

Phase 2 outputs:

- `docs/marine_package_v1/marine_package_v1_evidence_map.csv`
- `docs/marine_package_v1/marine_package_v1_artifact_index.md`
- `docs/marine_package_v1/marine_package_v1_gap_register.md`

Claim coverage summary:

- total frozen claims: 40
- mapped claims: 40
- source-not-found claims: 0
- framework-conflict claims: 0

Artifact coverage summary:

- Artifact Index is the source of truth for artifact counts.
- artifacts indexed: 44
- artifacts without hashes: 0
- artifacts with Historical document status: 8
- artifacts with HISTORICAL or CONTEXT_ONLY authority: 0
- broken repository paths: 0
- authority conflicts: 0

Gap summary:

- G-001 through G-027 preserved
- Critical gaps: 0
- High gaps: 13
- Medium gaps: 10
- Low gaps: 2
- Boundary-only gaps: 2
- Marine request blockers: 2

Phase 2 readiness decision:

`MARINE_PACKAGE_V1_READY_FOR_DRAFTING_WITH_DOCUMENTED_GAPS`

Document status remains Frozen v1.0. This section records Phase 2 status references only and does not amend frozen claim text or classification.
