# Review Guide and Pack Index

Package ID: DEEP_RESEARCH_REVIEW_PACKAGE_001
Package version: v1.1
Transport ID: DEEP_RESEARCH_REVIEW_PACKAGE_TRANSPORT_V2_001
Document status: Transport v2 build artifact

## How to Use This Package

Read the Research Brief first. Use Reading Packs as the default review corpus. Use Evidence Packs and lookup files for targeted claim, gap, numerical, and artifact checks. Integrity metadata is separated from reading content.

## Reading Pack Inventory

| Pack | Path | Documents | Lines | Bytes |
| --- | --- | ---: | ---: | ---: |
| RP-01 | `docs/deep_research_review_package_transport_v2/reading/RP-01_marine_package_narrative_and_boundaries.md` | 1 | 428 | 36771 |
| RP-02 | `docs/deep_research_review_package_transport_v2/reading/RP-02_marine_claims_gaps_and_completion_controls.md` | 4 | 963 | 76065 |
| RP-03 | `docs/deep_research_review_package_transport_v2/reading/RP-03_external_validation_definition_and_governance.md` | 6 | 1059 | 53861 |
| RP-04 | `docs/deep_research_review_package_transport_v2/reading/RP-04_repository_state_and_documentation_navigation.md` | 1 | 295 | 13311 |
| RP-05 | `docs/deep_research_review_package_transport_v2/reading/RP-05_codlag_and_pronostia_evidence.md` | 4 | 733 | 36733 |
| RP-06 | `docs/deep_research_review_package_transport_v2/reading/RP-06_fd002_residual_evidence_and_hi.md` | 3 | 715 | 33373 |
| RP-07 | `docs/deep_research_review_package_transport_v2/reading/RP-07_ncmapss_residual_pilot.md` | 2 | 619 | 24608 |
| RP-08 | `docs/deep_research_review_package_transport_v2/reading/RP-08_ncmapss_nonresidual_development.md` | 2 | 229 | 6143 |
| RP-09 | `docs/deep_research_review_package_transport_v2/reading/RP-09_framework_architecture_and_decision_documents_part_01.md` | 2 | 922 | 16147 |
| RP-09 | `docs/deep_research_review_package_transport_v2/reading/RP-09_framework_architecture_and_decision_documents_part_02.md` | 3 | 595 | 15376 |

## Evidence Pack Inventory

| Pack | Path | Documents | Lines | Bytes |
| --- | --- | ---: | ---: | ---: |
| EP-01 | `docs/deep_research_review_package_transport_v2/evidence/EP-01_marine_evidence_map_doc-004.md` | 1 | 60 | 60314 |
| EP-02 | `docs/deep_research_review_package_transport_v2/evidence/EP-02_marine_artifact_index_doc-005.md` | 1 | 115 | 28673 |
| EP-05 | `docs/deep_research_review_package_transport_v2/evidence/EP-05_machine_oriented_numerical_artifacts_doc-008.md` | 1 | 97 | 3481 |
| EP-05 | `docs/deep_research_review_package_transport_v2/evidence/EP-05_machine_oriented_numerical_artifacts_doc-015.md` | 1 | 59 | 2426 |
| EP-05 | `docs/deep_research_review_package_transport_v2/evidence/EP-05_machine_oriented_numerical_artifacts_doc-023.md` | 1 | 145 | 5940 |
| EP-05 | `docs/deep_research_review_package_transport_v2/evidence/EP-05_machine_oriented_numerical_artifacts_doc-028.md` | 1 | 88 | 19262 |
| EP-04 | `docs/deep_research_review_package_transport_v2/evidence/EP-04_fd002_cross_model_summary_doc-025.md` | 1 | 26 | 1757 |
| EP-03 | `docs/deep_research_review_package_transport_v2/evidence/EP-03_cusum_diagnostic_doc-031_part_01.md` | 1 | 779 | 24220 |
| EP-03 | `docs/deep_research_review_package_transport_v2/evidence/EP-03_cusum_diagnostic_doc-031_part_02.md` | 1 | 779 | 25714 |
| EP-03 | `docs/deep_research_review_package_transport_v2/evidence/EP-03_cusum_diagnostic_doc-031_part_03.md` | 1 | 779 | 25615 |
| EP-03 | `docs/deep_research_review_package_transport_v2/evidence/EP-03_cusum_diagnostic_doc-031_part_04.md` | 1 | 665 | 21872 |

## Q1-Q8 Routing Table

| Review question | Primary packs | Secondary lookup |
| --- | --- | --- |
| Q1 Claim-Evidence-Gap Integrity | RP-01, RP-02 | EP-01, claim index, gap index |
| Q2 Process and State Consistency | RP-02, RP-03, RP-04 | document index |
| Q3 Public-Data / Marine Boundary | RP-01, RP-03 | claim index |
| Q4 Scientific and Engineering Challenge | RP-05, RP-06, RP-07, RP-08, RP-09 | Evidence Packs |
| Q5 Historical Verification Trace | RP-02, RP-04, RP-06, RP-07, RP-08 | artifact lookup |
| Q6 Translation Risk | RP-01, RP-02, RP-03 | claim index |
| Q7 Governance Overhead | RP-02, RP-03, RP-04, RP-09 | document index |
| Q8 Communication Readiness | all Reading Packs | all lookup indexes |

## Document Coverage Table

| Document ID | Source path | Role | Default reading required |
| --- | --- | --- | --- |
| DOC-001 | `docs/marine_package_v1/marine_package_v1.md` | Marine Package v1.0 main document | Yes |
| DOC-002 | `docs/marine_package_v1/marine_package_v1_structure.md` | Marine Package v1.0 Structure | Yes |
| DOC-003 | `docs/marine_package_v1/marine_package_v1_claim_boundary.md` | Marine Package v1.0 Claim Boundary | Yes |
| DOC-004 | `docs/marine_package_v1/marine_package_v1_evidence_map.csv` | Marine Package v1.0 Evidence Map | No |
| DOC-005 | `docs/marine_package_v1/marine_package_v1_artifact_index.md` | Marine Package v1.0 Artifact Index | No |
| DOC-006 | `docs/marine_package_v1/marine_package_v1_gap_register.md` | Marine Package v1.0 Gap Register | Yes |
| DOC-007 | `docs/marine_package_v1/marine_package_v1_completion_review.md` | Marine Package v1.0 Completion Review | Yes |
| DOC-008 | `docs/marine_package_v1/marine_package_v1_freeze_manifest.json` | Marine Package v1.0 Freeze Manifest | No |
| DOC-009 | `docs/external_validation/external_validation_of_project_results_specification.md` | External Validation Specification | Yes |
| DOC-010 | `docs/external_validation/external_validation_evidence_package_manifest.md` | External Validation Evidence Package Manifest | Yes |
| DOC-011 | `docs/external_validation/external_reviewer_declaration_template.md` | External Reviewer Declaration Template | Yes |
| DOC-012 | `docs/external_validation/external_validation_review_form.md` | External Validation Review Form | Yes |
| DOC-013 | `docs/external_validation/external_validation_decision_record_template.md` | External Validation Decision Record Template | Yes |
| DOC-014 | `docs/external_validation/external_validation_definition_approval_and_freeze_record.md` | External Validation Definition Approval and Freeze Record | Yes |
| DOC-015 | `docs/external_validation/external_validation_definition_freeze_manifest.json` | External Validation Definition Freeze Manifest | No |
| DOC-016 | `docs/documentation_map.md` | Documentation Map | Yes |
| DOC-017 | `outputs/codlag_expected_state/stratified_residual_diagnostic/CODLAG_stratified_residual_diagnostic_summary.md` | CODLAG residual boundary evidence | Yes |
| DOC-018 | `docs/validation/framework_validation/CODLAG_expected_state_baseline_execution_record.md` | CODLAG Expected State execution record | Yes |
| DOC-019 | `docs/validation/framework_validation/PRONOSTIA-BD-001_closure_review.md` | PRONOSTIA fixed-condition closure review | Yes |
| DOC-020 | `docs/validation/framework_validation/PRONOSTIA-BD-001_execution_summary.md` | PRONOSTIA fixed-condition execution summary | Yes |
| DOC-021 | `docs/validation/framework_validation/FD002_consolidated_closure_report.md` | FD002 residual evidence closure report | Yes |
| DOC-022 | `docs/validation/framework_validation/FD002_existing_state_audit.md` | FD002 existing-state audit | Yes |
| DOC-023 | `docs/validation/framework_validation/FD002_health_evidence_v0_execution_summary.md` | FD002 Health Evidence numerical support | No |
| DOC-024 | `docs/validation/framework_validation/FD002_HI_v0_closure_review.md` | FD002 HI closure review | Yes |
| DOC-025 | `outputs/cmapss_fd002/phase_b/B1_fixed_channel/CMAPSS_FD002_B1_cross_model_comparison_summary.csv` | FD002 cross-model numerical support | No |
| DOC-026 | `docs/validation/ncmapss_prevalidation/NCMAPSS_prevalidation_completion_summary.md` | N-CMAPSS DS02 residual pilot completion summary | Yes |
| DOC-027 | `docs/validation/ncmapss_prevalidation/NCMAPSS_DS02_residual_prevalidation_diagnostic_review.md` | N-CMAPSS DS02 residual pilot review evidence | Yes |
| DOC-028 | `outputs/ncmapss/prevalidation/ds02_residual_001/NCMAPSS_DS02_HI_summary.csv` | N-CMAPSS DS02 residual pilot numerical support | No |
| DOC-029 | `docs/validation/public_data_nonresidual/ncmapss_ds02_nonresidual_development_closure_report.md` | N-CMAPSS DS02 nonresidual development closure evidence | Yes |
| DOC-030 | `docs/validation/public_data_nonresidual/ncmapss_ds02_nonresidual_archive_summary.md` | N-CMAPSS DS02 nonresidual archive evidence | Yes |
| DOC-031 | `outputs/public_data_nonresidual/ncmapss_ds02/dev_004/cusum_reference_diagnostic_summary.json` | CUSUM unresolved diagnostic numerical support | No |
| DOC-032 | `lbnl_expected_state/docs/architecture/health_evidence_framework.md` | Health Evidence architecture authority | Yes |
| DOC-033 | `lbnl_expected_state/docs/decisions/DD-002_residual_evidence_hierarchy.md` | Residual evidence hierarchy authority | Yes |
| DOC-034 | `lbnl_expected_state/docs/decisions/DD-003_project_terminology_standard.md` | Project terminology authority | Yes |
| DOC-035 | `lbnl_expected_state/docs/decisions/DD-005_stateful_health_indicator_lifecycle.md` | Stateful HI lifecycle architecture authority | Yes |
| DOC-036 | `lbnl_expected_state/docs/decisions/DD-006_evidence_diversity_principle.md` | Evidence diversity principle authority | Yes |

## Pack Access Declaration Template

For every Reading Pack, report READ / PARTIALLY_READ / NOT_ACCESSED / PARSER_FAILURE.
For every Evidence Pack, report LOOKUP_ONLY / READ / NOT_ACCESSED / PARSER_FAILURE.

All required Reading Packs accessible: Yes / No
All required source documents represented: Yes / No / Not verified
Parser or attachment failure observed: Yes / No
Review completeness affected: Yes / No

## Parser Failure Protocol

If a pack appears truncated, inaccessible, unreadable, or partially parsed, record PARSER_FAILURE and do not state that the full package was reviewed.

## Non-Authority Statement

Transport v2 changes delivery architecture only. It does not modify Marine Package v1.0, External Validation definitions, frozen claims, active gaps, evidence strength, process state, Marine validity, or Marine feasibility.
