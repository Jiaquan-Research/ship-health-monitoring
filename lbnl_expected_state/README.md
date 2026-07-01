# LBNL Expected State and Health Evidence Framework

This workspace contains the LBNL validation pipeline and the current Health Evidence framework documentation.

The LBNL dataset is used as a pipeline validation dataset for developing and auditing the framework before future marine validation. The project does not treat LBNL results as direct validation of marine diesel generators or other shipboard systems.

## Current Framework

The current framework connects:

```text
Dataset Qualification
-> Expected State
-> Residual
-> Statistical Validity
-> Semantic Admissibility
-> Candidate Health Evidence
-> Evidence Prototype
-> Evidence Committee
-> Engineering Review
-> Maintenance Decision
```

The canonical architecture document is:

[docs/architecture/health_evidence_framework.md](docs/architecture/health_evidence_framework.md)

## Current Phase

Current phase: Phase 2 / H5C preparation.

Completed stages:

- Phase 1 Expected State validation
- Residual Bias Audit
- Residual Leakage Audit
- Phase 1 Scientific Review
- Health Indicator design target review
- Health Indicator evaluation protocol
- Candidate Health Indicator construction
- Residual Semantic Admissibility review
- Semantic Window validation
- Health Evidence prototype benchmark
- Evidence Philosophy taxonomy
- DD-006 Evidence Diversity Principle
- Gate M2 and Gate M2.5 reviews

Next planned stage:

- H5C Evidence Committee Construction

## Current Experimental Status

The project has experimentally validated the framework up to the Evidence Prototype layer using the LBNL validation pipeline.

Current validated layers:

- Dataset Qualification
- Expected State construction
- Residual generation
- Statistical Validity
- Semantic Admissibility
- Candidate Health Evidence
- Evidence Prototype benchmark

Planned or future layers:

- Evidence Committee
- Engineering Review
- Maintenance Decision
- Marine validation
- Cross-domain validation

## Document Locations

Architecture:

- [docs/architecture/health_evidence_framework.md](docs/architecture/health_evidence_framework.md)

Framework taxonomy:

- [docs/framework/evidence_philosophy_taxonomy.md](docs/framework/evidence_philosophy_taxonomy.md)

Decision Documents:

- [docs/decisions/DD-002_residual_evidence_hierarchy.md](docs/decisions/DD-002_residual_evidence_hierarchy.md)
- [docs/decisions/DD-003_project_terminology_standard.md](docs/decisions/DD-003_project_terminology_standard.md)
- [docs/decisions/DD-004_semantic_window_validation.md](docs/decisions/DD-004_semantic_window_validation.md)
- [docs/decisions/DD-005_stateful_health_indicator_lifecycle.md](docs/decisions/DD-005_stateful_health_indicator_lifecycle.md)
- [docs/decisions/DD-006_evidence_diversity_principle.md](docs/decisions/DD-006_evidence_diversity_principle.md)

Gate reviews:

- [docs/gates/gate_m2_phase2_milestone_review.md](docs/gates/gate_m2_phase2_milestone_review.md)
- [docs/gates/gate_m2_5_prototype_freeze_review.md](docs/gates/gate_m2_5_prototype_freeze_review.md)

Phase summary:

- [docs/phase2/h5_summary.md](docs/phase2/h5_summary.md)

Specification:

- [docs/specifications/h5c_evidence_committee_spec.md](docs/specifications/h5c_evidence_committee_spec.md)

Research logs:

- [docs/research_logs/RL-001_three_layer_engineering_architecture.md](docs/research_logs/RL-001_three_layer_engineering_architecture.md)
- [docs/research_logs/RL-002_maintenance_as_second_information_stream.md](docs/research_logs/RL-002_maintenance_as_second_information_stream.md)

## Outputs

Experiment outputs are stored under:

- `outputs/csv/`
- `outputs/figures/`
- `outputs/manifests/`
- `outputs/models/`
- `outputs/reports/`

These outputs are scientific artifacts from the LBNL validation pipeline. Large generated files should be governed by an explicit version-control or archive policy before framework freeze.
