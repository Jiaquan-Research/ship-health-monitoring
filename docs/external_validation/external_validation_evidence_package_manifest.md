# External Validation Evidence Package Manifest

Document status: Frozen
Version: v1.0
Evidence package status: Frozen definition, not issued
Reviewer: Not selected
External Validation execution: Not started

This manifest defines the controlled evidence package for External Validation of Project Results. It is not an issued review package and does not start External Validation execution.

Evidence groups:

- A. Frozen Package governance
- B. Frozen claim and gap controls
- C. Public-data residual evidence
- D. Public-data nonresidual evidence
- E. Framework and architecture
- F. Marine request and intake templates
- G. Reproducibility and lineage records
- H. Review instructions and forms

| group | artifact ID | repository path | role | status | review priority | required or optional | expected reviewer action | hash or hash source | known limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | MPV1-PACKAGE | `docs/marine_package_v1/marine_package_v1.md` | Frozen Package governance | Defined | High | Required | Confirm narrative accuracy and boundaries. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| A | MPV1-STRUCT | `docs/marine_package_v1/marine_package_v1_structure.md` | Frozen framework structure | Defined | High | Required | Check candidate tools and framework scope. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| B | MPV1-BOUND | `docs/marine_package_v1/marine_package_v1_claim_boundary.md` | Frozen claim and wording control | Defined | High | Required | Check claim text and prohibited wording. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| B | NOT_INDEXED_GOVERNANCE_FILE | `docs/marine_package_v1/marine_package_v1_evidence_map.csv` | Claim-to-evidence map | Defined | High | Required | Trace all claim support. | Current file hash after definition review | Frozen/reviewed Package control file referenced directly by repository path. |
| B | SELF_INDEX_NOT_APPLICABLE | `docs/marine_package_v1/marine_package_v1_artifact_index.md` | Artifact and hash index | Defined | High | Required | Check paths, hashes, lineage. | Current file hash after definition review | The Artifact Index does not maintain a conventional self-hash artifact record. It is referenced directly by path. |
| B | NOT_INDEXED_GOVERNANCE_FILE | `docs/marine_package_v1/marine_package_v1_gap_register.md` | Gap register | Defined | High | Required | Review all gaps and blockers. | Current file hash after definition review | Reviewed Package control file referenced directly by repository path. |
| A | MPV1-COMP-REVIEW | `docs/marine_package_v1/marine_package_v1_completion_review.md` | Completion review | Defined | High | Required | Confirm completion scope. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| A | MPV1-FREEZE-MANIFEST | `docs/marine_package_v1/marine_package_v1_freeze_manifest.json` | Freeze manifest | Defined | High | Required | Check freeze state. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| A | DOCMAP | `docs/documentation_map.md` | Repository navigation | Defined | High | Required | Check current process state. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | COD-001 | `outputs/codlag_expected_state/stratified_residual_diagnostic/CODLAG_stratified_residual_diagnostic_summary.md` | CODLAG primary support | Defined | High | Required | Check CODLAG boundary claims. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | PR-001A | `docs/validation/framework_validation/PRONOSTIA-BD-001_closure_review.md` | PRONOSTIA primary support | Defined | High | Required | Check fixed-condition boundary. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | FD2-001 | `docs/validation/framework_validation/FD002_consolidated_closure_report.md` | FD002 consolidated closure | Defined | High | Required | Check FD002 claim chain. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| G | FD2-004 | `docs/validation/framework_validation/FD002_existing_state_audit.md` | FD002 existing-state audit | Defined | High | Required | Check lineage limitations. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | FD2-009 | `docs/validation/framework_validation/FD002_health_evidence_v0_execution_summary.md` | FD002 Health Evidence record | Defined | High | Required | Check channel evidence. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | FD2-013 | `docs/validation/framework_validation/FD002_HI_v0_closure_review.md` | FD002 HI review | Defined | High | Required | Check HI boundaries. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | FD2-014 | `outputs/cmapss_fd002/phase_b/B1_fixed_channel/CMAPSS_FD002_B1_cross_model_comparison_summary.csv` | FD002 Phase B1 summary | Defined | High | Required | Check cross-model claims. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | NC-R-001 | `docs/validation/ncmapss_prevalidation/NCMAPSS_prevalidation_completion_summary.md` | N-CMAPSS residual completion | Defined | High | Required | Check pilot evidence. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| C | NC-R-002 | `docs/validation/ncmapss_prevalidation/NCMAPSS_DS02_residual_prevalidation_diagnostic_review.md` | N-CMAPSS residual review | Defined | High | Required | Check pilot limitations. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| D | NC-N-001 | `docs/validation/public_data_nonresidual/ncmapss_ds02_nonresidual_development_closure_report.md` | DS02 nonresidual closure | Defined | High | Required | Check nonresidual state. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| D | NC-N-002 | `docs/validation/public_data_nonresidual/ncmapss_ds02_nonresidual_archive_summary.md` | DS02 nonresidual archive | Defined | High | Required | Check archive state. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| D | NC-N-003 | `outputs/public_data_nonresidual/ncmapss_ds02/dev_004/cusum_reference_diagnostic_summary.json` | CUSUM diagnostic record | Defined | High | Required | Check unresolved CUSUM boundary. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| E | FW-002 | `lbnl_expected_state/docs/architecture/health_evidence_framework.md` | Health Evidence Framework | Defined | High | Required | Check architecture. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| E | DD-002 | `lbnl_expected_state/docs/decisions/DD-002_residual_evidence_hierarchy.md` | Decision document | Defined | High | Required | Check evidence hierarchy. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| E | DD-003 | `lbnl_expected_state/docs/decisions/DD-003_project_terminology_standard.md` | Decision document | Defined | High | Required | Check terminology. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| E | DD-005 | `lbnl_expected_state/docs/decisions/DD-005_stateful_health_indicator_lifecycle.md` | Decision document | Defined | High | Required | Check lifecycle logic. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| E | DD-006 | `lbnl_expected_state/docs/decisions/DD-006_evidence_diversity_principle.md` | Decision document | Defined | High | Required | Check evidence diversity. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| F | GOV-001 | `docs/dataset_qualification_specification.md` | Dataset Qualification Specification | Defined | High | Required | Check qualification boundary. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| G | GOV-003 | `docs/artifact_policy.md` | Artifact Policy | Defined | High | Required | Check artifact governance. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| F | M-ART-001 | `docs/validation/marine_execution_package/templates/marine_data_request_and_delivery_specification.md` | Marine request template | Defined | High | Required | Check template/request distinction. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| F | M-ART-002 | `docs/validation/marine_execution_package/templates/marine_data_intake_checklist.md` | Marine intake template | Defined | High | Required | Check intake boundary. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| F | M-ART-003 | `docs/validation/marine_execution_package/templates/sensor_inventory_template.md` | Sensor inventory template | Defined | High | Required | Check sensor metadata request. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| F | M-ART-004 | `docs/validation/marine_execution_package/templates/variable_role_mapping_template.md` | Variable role mapping template | Defined | High | Required | Check variable-role boundary. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| H | EXTVAL-SPEC | `docs/external_validation/external_validation_of_project_results_specification.md` | Review specification | Defined | High | Required | Use as review procedure. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| H | EXTVAL-EVIDENCE-MANIFEST | `docs/external_validation/external_validation_evidence_package_manifest.md` | Controlled evidence-package definition | Defined | High | Required | Confirm that the issued evidence package matches this manifest. | Artifact Index hash or current file hash after definition review | Definition-stage manifest; exact issued-package hashes must be frozen before review execution. |
| H | EXTVAL-REVIEWER-DECLARATION | `docs/external_validation/external_reviewer_declaration_template.md` | Reviewer declaration | Defined | High | Required | Complete before appointment. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| H | EXTVAL-REVIEW-FORM | `docs/external_validation/external_validation_review_form.md` | Review form | Defined | High | Required | Complete during review. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
| H | EXTVAL-DECISION-TEMPLATE | `docs/external_validation/external_validation_decision_record_template.md` | Decision record | Defined | High | Required | Complete final decision. | Artifact Index hash or current file hash after definition | Definition package not issued; reviewer not selected. |
