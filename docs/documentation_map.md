# Repository Documentation Map

This document provides the current navigation map for the repository public-publishing state.

For current public status, begin at:

- [Publishing Status](../PUBLISHING_STATUS.md)
- [System State](../SYSTEM_STATE.md)
- [Root README](../README.md)

The canonical framework documentation begins at:

[Health Evidence Framework](../lbnl_expected_state/docs/architecture/health_evidence_framework.md)

## Repository Navigation

```text
Repository
-> Publishing Status
-> Marine Package v1.0
-> External Validation Definition
-> Deep Research Review Package and Transport
-> Blind Review Session Protocol and Execution Package
-> Framework Architecture
-> Decision Documents
-> Research Logs
-> Specifications
-> Reports and Outputs
```

## Publishing Status

Current public publishing entry point:

- [Publishing Status](../PUBLISHING_STATUS.md)

Current repository review record:

- [Repository Publishing Review](repository_review/repository_publishing_review.md)

Current publishing stage:

- Repository prepared for public presentation, future website deployment, Deep Research retrieval, and external collaboration.
- Scientific conclusions, validation evidence, frozen claims, frozen gaps, and process-state decisions are unchanged by publishing preparation.

## Canonical Architecture

Canonical architecture document:

- [Health Evidence Framework](../lbnl_expected_state/docs/architecture/health_evidence_framework.md)

This is the primary entry point for understanding the current Health Evidence framework.

## Decision Documents

Canonical Decision Documents are stored in:

- [lbnl_expected_state/docs/decisions/](../lbnl_expected_state/docs/decisions/)

Current frozen decisions:

- [DD-002 Residual Evidence Hierarchy](../lbnl_expected_state/docs/decisions/DD-002_residual_evidence_hierarchy.md)
- [DD-003 Project Terminology Standard](../lbnl_expected_state/docs/decisions/DD-003_project_terminology_standard.md)
- [DD-004 Semantic Window Validation](../lbnl_expected_state/docs/decisions/DD-004_semantic_window_validation.md)
- [DD-005 Stateful Health Indicator Lifecycle](../lbnl_expected_state/docs/decisions/DD-005_stateful_health_indicator_lifecycle.md)
- [DD-006 Evidence Diversity Principle](../lbnl_expected_state/docs/decisions/DD-006_evidence_diversity_principle.md)

Older task-level decisions are recorded in:

- [LBNL Decision Log](../lbnl_expected_state/docs/decision_log.md)

The Decision Log records experiment-stage decisions. The DD documents record framework-level frozen engineering decisions.

## Framework and Taxonomy

Canonical framework taxonomy:

- [Evidence Philosophy Taxonomy](../lbnl_expected_state/docs/framework/evidence_philosophy_taxonomy.md)

Historical method taxonomy:

- [H5A Health Indicator Method Taxonomy](../lbnl_expected_state/docs/h5a_health_indicator_method_taxonomy.md)

The Evidence Philosophy Taxonomy is the current framework-level taxonomy. H5A is retained as a stage-level foundation document.

## Research Logs

Current LBNL framework research logs are stored in:

- [lbnl_expected_state/docs/research_logs/](../lbnl_expected_state/docs/research_logs/)

Current logs:

- [RL-001 Three Layer Engineering Architecture](../lbnl_expected_state/docs/research_logs/RL-001_three_layer_engineering_architecture.md)
- [RL-002 Maintenance as Second Information Stream](../lbnl_expected_state/docs/research_logs/RL-002_maintenance_as_second_information_stream.md)

Root-level research logs and root `docs/research_logs/` should be treated as historical or project-wide notes unless explicitly linked from the current framework.

## Gate Reviews

Canonical gate reviews are stored in:

- [lbnl_expected_state/docs/gates/](../lbnl_expected_state/docs/gates/)

Current gates:

- [Gate M2 Phase 2 Milestone Review](../lbnl_expected_state/docs/gates/gate_m2_phase2_milestone_review.md)
- [Gate M2.5 Prototype Freeze Review](../lbnl_expected_state/docs/gates/gate_m2_5_prototype_freeze_review.md)
- [Gate M3 Repository Accessibility Test](../lbnl_expected_state/docs/gates/gate_m3_repository_accessibility.md)
- [Gate M3 Audit Response Matrix](../lbnl_expected_state/docs/gates/gate_m3_audit_response_matrix.md)
- [Gate M3 Audit Response Matrix Reviewer #2](governance/gate_m3_audit_response_matrix_r2.md)

Completed governance milestone:

- [ST-001 Framework Stress Test Closure Report](validation/framework_stress_test/ST-001_dataset_attack/ST001_closure_report.md)
- [ST-001 Framework Stress Test Archive Summary](validation/framework_stress_test/ST-001_dataset_attack/ST001_archive_summary.md)

## Governance Documents

Repository-level governance documents are stored in:

- [docs/](.)
- [docs/governance/](governance/)

Current governance documents:

- [Framework Audit Package](framework_audit_package.md)
- [Framework Freeze Manifest](framework_freeze_manifest.md)
- [Dataset Qualification Specification](dataset_qualification_specification.md)
- [Dataset Registry](dataset_registry.md)
- [Artifact Policy](artifact_policy.md)
- [Gate M3 Audit Response Matrix Reviewer #2](governance/gate_m3_audit_response_matrix_r2.md)
- [Repository Governance Policy](governance/repository_governance_policy.md)
- [Publishing Policy](governance/publishing_policy.md)
- [Machine Retrieval Policy](governance/machine_retrieval_policy.md)

## Repository Manifest and Machine Access

Manifest guide:

- [Repository Manifest README](../manifest/README.md)

Machine-readable manifests:

- [Repository Manifest](../manifest/repository_manifest.json)
- [Public Manifest](../manifest/public_manifest.json)
- [Machine Retrieval Manifest](../manifest/machine_retrieval_manifest.json)

Website planning:

- [Website Content Map](website/website_content_map.md)
- [Website Architecture Design](website/website_architecture_design.md)
- [Website Implementation Record v0.1](website/website_implementation_record_v0_1.md)

Website implementation:

- Local Astro source: `website/`
- Implementation status: `WEBSITE_IMPLEMENTATION_V0_1_READY_WITH_DOCUMENTED_LIMITATIONS`
- Deployment: Not started
- Domain binding: Not started

## Specifications

Canonical execution specifications are stored in:

- [lbnl_expected_state/docs/specifications/](../lbnl_expected_state/docs/specifications/)

Current specification:

- [H5C Evidence Committee Specification](../lbnl_expected_state/docs/specifications/h5c_evidence_committee_spec.md)

## Phase Summaries

Canonical phase summaries are stored under:

- [lbnl_expected_state/docs/phase2/](../lbnl_expected_state/docs/phase2/)

Current summary:

- [H5B Summary](../lbnl_expected_state/docs/phase2/h5_summary.md)

## Reports and Experimental Outputs

Canonical LBNL framework reports are stored in:

- `lbnl_expected_state/outputs/reports/` - local/generated output family; not included in the deployment-preparation branch.

Canonical LBNL generated artifacts are stored in:

- `lbnl_expected_state/outputs/csv/` - local/generated output family; not included in the deployment-preparation branch.
- `lbnl_expected_state/outputs/figures/` - local/generated output family; not included in the deployment-preparation branch.
- `lbnl_expected_state/outputs/manifests/` - local/generated output family; not included in the deployment-preparation branch.
- `lbnl_expected_state/outputs/models/` - local/generated output family; not included in the deployment-preparation branch.

Root-level `outputs/` contains historical and exploratory artifacts unless explicitly referenced by current framework documentation.

Public-data nonresidual validation records:

- [N-CMAPSS DS02 Nonresidual Development Closure Report](validation/public_data_nonresidual/ncmapss_ds02_nonresidual_development_closure_report.md) - Closed - development-only evidence
- [N-CMAPSS DS02 Nonresidual Archive Summary](validation/public_data_nonresidual/ncmapss_ds02_nonresidual_archive_summary.md) - Closed - development-only evidence

C-MAPSS FD002 validation records:

- [FD002 Existing-State Audit](validation/framework_validation/FD002_existing_state_audit.md) - Audit - existing-state and lineage, no new execution
- [FD002 Consolidated Closure Report](validation/framework_validation/FD002_consolidated_closure_report.md) - Closed - public-data residual / Evidence / HI / Phase B1 evidence with documented lineage and sensitivity limitations
- [FD002 Archive Summary](validation/framework_validation/FD002_archive_summary.md) - Closed - public-data residual / Evidence / HI / Phase B1 evidence with documented lineage and sensitivity limitations
- [FD002 Closure Manifest](../outputs/cmapss_fd002/closure/FD002_closure_manifest.json) - Closed - public-data residual / Evidence / HI / Phase B1 evidence with documented lineage and sensitivity limitations

Marine Package v1.0 historical framework-freeze milestone:

- Marine Package v1.0 Structure:
  `docs/marine_package_v1/marine_package_v1_structure.md`
  - Frozen framework foundation

- Marine Package v1.0 Claim Boundary:
  `docs/marine_package_v1/marine_package_v1_claim_boundary.md`
  - Frozen claim-boundary foundation

Historical milestone state:

- `MARINE_PACKAGE_V1_FRAMEWORK_READY_FOR_EVIDENCE_MAPPING`

This milestone has been superseded by the current Package status recorded in
the `Marine Package v1.0 Status` section below.

Marine data request:

- Planned - not started

Planned prerequisite documents:

- Marine Package v1.0
- External Validation of Project Results

## Historical and Archive Material

The following areas contain valuable historical material but are not the canonical framework entry points:

- `docs/deep research/` - local historical note directory; not included in the deployment-preparation branch.
- `docs/methodology/` - local historical/method note directory; not included in the deployment-preparation branch.
- `docs/exploratory/` - local exploratory note directory; not included in the deployment-preparation branch.
- [docs/exploration/](exploration/)
- [docs/review/](review/)
- [root outputs](../outputs/)
- `research_logs/` - local historical research-log directory; not included in the deployment-preparation branch.

Completed governance milestones should be indexed here once closed. ST-001 is a completed governance milestone and is retained for archive traceability.

These documents should be retained unless reviewed separately. They should not be treated as Gate M3 cleanup targets without explicit approval.

## Personal Chinese Documents

Chinese review documents, translations, and discussion notes are retained for personal reference.

Do not delete them as part of repository cleanup.

Recommended future non-Git organization:

```text
personal_notes/
  chinese_reviews/
  deep_research_cn/
  translations/
  discussion_notes/
```

This recommendation is organizational only. No files have been moved.

## Canonical Reading Path

Recommended path for a new reviewer:

1. [Root README](../README.md)
2. [Publishing Status](../PUBLISHING_STATUS.md)
3. [Marine Package v1.0](marine_package_v1/marine_package_v1.md)
4. [Marine Package v1.0 Gap Register](marine_package_v1/marine_package_v1_gap_register.md)
5. [External Validation Definition Approval and Freeze Record](external_validation/external_validation_definition_approval_and_freeze_record.md)
6. [Deep Research Review Transport v2 Guide](deep_research_review_package_transport_v2/00_review_guide_and_pack_index.md)
7. [Blind Review v2 Execution Package README](deep_research_blind_review_execution_v2/README_START_HERE.md)
8. [Health Evidence Framework](../lbnl_expected_state/docs/architecture/health_evidence_framework.md)

## Marine Package v1.0 Status

- Marine Package v1.0 Evidence Map: `docs/marine_package_v1/marine_package_v1_evidence_map.csv` - Reviewed
- Marine Package v1.0 Artifact Index: `docs/marine_package_v1/marine_package_v1_artifact_index.md` - Reviewed
- Marine Package v1.0 Gap Register: `docs/marine_package_v1/marine_package_v1_gap_register.md` - Reviewed
- Marine Package v1.0 Completion Review: `docs/marine_package_v1/marine_package_v1_completion_review.md` - Reviewed v1.0
- Marine Package v1.0 Freeze Manifest: `docs/marine_package_v1/marine_package_v1_freeze_manifest.json` - Frozen v1.0
- Marine Package v1.0: `docs/marine_package_v1/marine_package_v1.md` - Frozen v1.0
- Phase 2 reconciliation: Complete
- Phase 2 readiness decision: `MARINE_PACKAGE_V1_READY_FOR_DRAFTING_WITH_DOCUMENTED_GAPS`
- Package completion state: `MARINE_PACKAGE_V1_COMPLETED_WITH_DOCUMENTED_GAPS`
- Package freeze state: `MARINE_PACKAGE_V1_FROZEN`
- Post-freeze metadata correction: Complete - artifact count synchronized and superseded Phase 1 status labeled as historical.
- Drafting decision: `MARINE_PACKAGE_V1_DRAFT_COMPLETE_WITH_REVIEW_ITEMS`
- Draft revision: Complete
- Draft review: Complete
- Marine data request: Planned - not started
- Planned prerequisite documents: Marine Package v1.0; External Validation of Project Results
- External Validation: Planned - incomplete
- Final Marine Package narrative: Frozen v1.0

- Completed next-authorized workstream: `EXTERNAL_VALIDATION_OF_PROJECT_RESULTS_DEFINITION_001`

## External Validation of Project Results

- External Validation of Project Results Specification: `docs/external_validation/external_validation_of_project_results_specification.md` - Frozen v1.0 - Definition approved and frozen
- External Validation Evidence Package Manifest: `docs/external_validation/external_validation_evidence_package_manifest.md` - Frozen v1.0 - Frozen definition, not issued
- External Reviewer Declaration Template: `docs/external_validation/external_reviewer_declaration_template.md` - Frozen Template v1.0 - Reviewer not selected
- External Validation Review Form: `docs/external_validation/external_validation_review_form.md` - Frozen Template v1.0 - Review execution not started
- External Validation Decision Record Template: `docs/external_validation/external_validation_decision_record_template.md` - Frozen Template v1.0 - Marine request gate not evaluated
- Definition workstream: `EXTERNAL_VALIDATION_OF_PROJECT_RESULTS_DEFINITION_001`
- Definition state: `EXTERNAL_VALIDATION_DEFINITION_COMPLETE_WITH_REVIEW_ITEMS`
- External Validation definition: Approved and Frozen
- Definition approval state: `EXTERNAL_VALIDATION_DEFINITION_APPROVED`
- Definition freeze state: `EXTERNAL_VALIDATION_DEFINITION_FROZEN`
- Combined definition state: `EXTERNAL_VALIDATION_DEFINITION_APPROVED_AND_FROZEN`
- Final Review: `EXTERNAL_VALIDATION_DEFINITION_FINAL_REVIEW_APPROVED`
- Approval and Freeze Record: `docs/external_validation/external_validation_definition_approval_and_freeze_record.md`
- Definition Freeze Manifest: `docs/external_validation/external_validation_definition_freeze_manifest.json`
- Evidence package: Frozen definition, not issued
- Definition review: Revisions completed
- Definition revision state: `EXTERNAL_VALIDATION_DEFINITION_REVISION_COMPLETE`
- External reviewer: Not selected
- External Validation execution: Not started
- Marine request gate: Not evaluated
- Marine data request: Planned, not started
- Next authorized phase: `EXTERNAL_VALIDATION_REVIEWER_SELECTION_AND_APPOINTMENT_001`

## Deep Research Review Transport

- Source package: `DEEP_RESEARCH_REVIEW_PACKAGE_001` v1.1
- Transport v1: `docs/deep_research_review_package_transport/` - Verified and archived
- Transport v2: `docs/deep_research_review_package_transport_v2/` - Default LLM Blind Review interface
- Transport v2 architecture: `docs/deep_research_review_package_transport_v2/transport_v2_architecture.md`
- Transport v2 review guide: `docs/deep_research_review_package_transport_v2/00_review_guide_and_pack_index.md`
- Transport v2 integrity manifest: `docs/deep_research_review_package_transport_v2/integrity/transport_v2_integrity_manifest.json`
- Transport v2 verification report: `docs/deep_research_review_package_transport_v2/integrity/transport_v2_verification_report.md`
- Transport v2 freeze manifest: `docs/deep_research_review_package_transport_v2/integrity/transport_v2_freeze_manifest.json`
- Transport v2 approval and freeze record: `docs/deep_research_review_package_transport_v2/transport_v2_approval_and_freeze_record.md`
- Completion state: `DEEP_RESEARCH_REVIEW_TRANSPORT_V2_COMPLETED_AND_VERIFIED`
- Verification state: `DEEP_RESEARCH_REVIEW_TRANSPORT_V2_COMPLETED_AND_VERIFIED`
- Approval state: `DEEP_RESEARCH_REVIEW_TRANSPORT_V2_APPROVED`
- Freeze state: `DEEP_RESEARCH_REVIEW_TRANSPORT_V2_FROZEN`
- Combined state: `DEEP_RESEARCH_REVIEW_TRANSPORT_V2_APPROVED_VERIFIED_AND_FROZEN`
- Authoritative-content boundary: Transport v2 changes delivery architecture only; it does not modify Marine Package v1.0, External Validation definitions, frozen claims, active gaps, evidence strength, Marine validity, or Marine feasibility.
- Execution preparation: Completed and superseded by the frozen Session Protocol.
- Current next authorized workstream: `DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001`

## Deep Research Blind Review v2 Session Protocol

- Session Protocol location: `docs/deep_research_blind_review_v2/`
- Session Protocol verification report: `docs/deep_research_blind_review_v2/blind_review_session_protocol_verification_report.md`
- Session Protocol freeze manifest: `docs/deep_research_blind_review_v2/blind_review_session_protocol_freeze_manifest.json`
- Session Protocol approval and freeze record: `docs/deep_research_blind_review_v2/blind_review_session_protocol_approval_and_freeze_record.md`
- Execution observation log: `docs/deep_research_blind_review_v2/blind_review_execution_observation_log.md`
- Transport v2 dependency: `DEEP_RESEARCH_REVIEW_PACKAGE_TRANSPORT_V2_001`
- Verification state: `DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_VERIFIED`
- Approval state: `DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_APPROVED`
- Freeze state: `DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_FROZEN`
- Combined state: `DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_APPROVED_VERIFIED_AND_FROZEN`
- Blind Review execution: Not started
- Observation log status: Active Execution Log
- Observation log mutability: `ACTIVE_APPEND_ONLY`
- Observation schema status: `FROZEN`
- Post-freeze metadata correction: `DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_POST_FREEZE_METADATA_CORRECTION_COMPLETE`
- Next authorized workstream: `DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001`

## Deep Research Blind Review v2 Execution Package

- Execution package location: `docs/deep_research_blind_review_execution_v2/`
- Operator entry point: `docs/deep_research_blind_review_execution_v2/README_START_HERE.md`
- Verification report: `docs/deep_research_blind_review_execution_v2/integrity/execution_package_verification_report.md`
- Manifest: `docs/deep_research_blind_review_execution_v2/integrity/execution_package_manifest.json`
- Final decision: `DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_PACKAGE_READY`
- Verification state: `DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_PACKAGE_VERIFIED`
- Main Session unique attachment count: 18
- Evidence files uploaded by default: 0
- Session Protocol files uploaded: 0
- Blind Review execution: Not started
- ChatGPT and Claude receive the same Main Session files and same prompts.
- Next task after human execution begins: `DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001`


## Website Deployment Preparation

- Website source: [website/](../website/)
- Website README: [website/README.md](../website/README.md)
- Implementation record: [docs/website/website_implementation_record_v0_1.md](website/website_implementation_record_v0_1.md)
- Status: deployment preparation implemented; Cloudflare deployment and jqhe.uk binding not started.
