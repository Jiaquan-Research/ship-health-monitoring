# Repository Documentation Map

This document provides a navigation map for the repository before Gate M3 Framework Audit.

The canonical framework documentation begins at:

[Health Evidence Framework](../lbnl_expected_state/docs/architecture/health_evidence_framework.md)

## Repository Navigation

```text
Repository
-> Architecture
-> Decision Documents
-> Framework
-> Taxonomy
-> Research Logs
-> Specifications
-> Reports
```

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

## Specifications

Canonical execution specifications are stored in:

- [lbnl_expected_state/docs/specifications/](../lbnl_expected_state/docs/specifications/)

Current specification:

- [H5C Evidence Committee Specification](../lbnl_expected_state/docs/specifications/h5c_evidence_committee_spec.md)

## Phase Summaries

Canonical phase summaries are stored under:

- [lbnl_expected_state/docs/phase2/](../lbnl_expected_state/docs/phase2/)

Current summary:

- [H5 Summary](../lbnl_expected_state/docs/phase2/h5_summary.md)

## Reports and Experimental Outputs

Canonical LBNL framework reports are stored in:

- [lbnl_expected_state/outputs/reports/](../lbnl_expected_state/outputs/reports/)

Canonical LBNL generated artifacts are stored in:

- [lbnl_expected_state/outputs/csv/](../lbnl_expected_state/outputs/csv/)
- [lbnl_expected_state/outputs/figures/](../lbnl_expected_state/outputs/figures/)
- [lbnl_expected_state/outputs/manifests/](../lbnl_expected_state/outputs/manifests/)
- [lbnl_expected_state/outputs/models/](../lbnl_expected_state/outputs/models/)

Root-level `outputs/` contains historical and exploratory artifacts unless explicitly referenced by current framework documentation.

## Historical and Archive Material

The following areas contain valuable historical material but are not the canonical framework entry points:

- [docs/deep research/](deep%20research/)
- [docs/methodology/](methodology/)
- [docs/exploratory/](exploratory/)
- [docs/exploration/](exploration/)
- [docs/review/](review/)
- [root outputs](../outputs/)
- [root research logs](../research_logs/)

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
2. [Health Evidence Framework](../lbnl_expected_state/docs/architecture/health_evidence_framework.md)
3. [DD-002 Residual Evidence Hierarchy](../lbnl_expected_state/docs/decisions/DD-002_residual_evidence_hierarchy.md)
4. [DD-003 Project Terminology Standard](../lbnl_expected_state/docs/decisions/DD-003_project_terminology_standard.md)
5. [DD-006 Evidence Diversity Principle](../lbnl_expected_state/docs/decisions/DD-006_evidence_diversity_principle.md)
6. [Evidence Philosophy Taxonomy](../lbnl_expected_state/docs/framework/evidence_philosophy_taxonomy.md)
7. [H5 Summary](../lbnl_expected_state/docs/phase2/h5_summary.md)
8. [H5C Evidence Committee Specification](../lbnl_expected_state/docs/specifications/h5c_evidence_committee_spec.md)
