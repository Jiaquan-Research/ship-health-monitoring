# Ship Health Monitoring

This repository develops a Health Evidence framework for continuous industrial equipment monitoring. The current validation path uses the LBNL chiller plant dataset as an engineering pipeline dataset before future marine validation.

The project focus is not algorithm competition. The current objective is to build a traceable engineering framework that connects Expected State modelling, residual validation, semantic admissibility, Health Evidence prototypes, and future Evidence Committee design.

## Current Status

Current phase: Phase 2 / H5C preparation.

Completed framework stages include:

- Phase 1 Expected State construction and validation
- Residual bias audit
- Residual leakage audit
- Phase 1 scientific review
- Phase 2 Health Indicator target and evaluation protocol
- Residual Semantic Admissibility review
- Semantic Window validation
- Health Evidence prototype benchmark
- Evidence Philosophy taxonomy
- DD-006 Evidence Diversity Principle

The next planned framework stage is H5C, Evidence Committee Construction.

## Framework Entry Point

Start here:

[Health Evidence Framework](lbnl_expected_state/docs/architecture/health_evidence_framework.md)

This document is the primary architecture entry point. It explains the current framework pipeline, layered architecture, component responsibilities, validation status, and document dependencies.

## Repository Structure

```text
lbnl_expected_state/
  docs/
    architecture/       Current framework architecture
    decisions/          Frozen Design Decisions
    framework/          Framework-level taxonomy
    gates/              Gate reviews and freeze points
    phase2/             Phase summaries
    research_logs/      Exploratory research logs
    specifications/     Execution specifications
  outputs/              LBNL experiment and framework outputs
  scripts/              Experiment scripts

docs/
  documentation_map.md  Repository documentation navigation map
  deep research/        Research source material and translations
  methodology/          Earlier methodology notes
  exploratory/          Historical exploratory notes

outputs/
  Historical and legacy experiment outputs
```

## Documentation Navigation

Core framework documents:

- [Health Evidence Framework](lbnl_expected_state/docs/architecture/health_evidence_framework.md)
- [Decision Documents](lbnl_expected_state/docs/decisions/)
- [Evidence Philosophy Taxonomy](lbnl_expected_state/docs/framework/evidence_philosophy_taxonomy.md)
- [H5 Summary](lbnl_expected_state/docs/phase2/h5_summary.md)
- [H5C Specification](lbnl_expected_state/docs/specifications/h5c_evidence_committee_spec.md)
- [Repository Documentation Map](docs/documentation_map.md)

Gate reviews:

- [Gate M2 Phase 2 Milestone Review](lbnl_expected_state/docs/gates/gate_m2_phase2_milestone_review.md)
- [Gate M2.5 Prototype Freeze Review](lbnl_expected_state/docs/gates/gate_m2_5_prototype_freeze_review.md)

## Current Scientific Boundary

The current project has experimentally validated the framework only up to the Evidence Prototype layer using the LBNL validation pipeline.

The following remain future work:

- Evidence Committee execution
- Engineering Review layer
- Maintenance Decision layer
- Marine validation
- Cross-domain validation
- Production deployment

## Personal Notes

Chinese review notes, translations, and discussion drafts are retained for personal reference. They are not cleanup targets. For future organization, a separate non-Git workspace is recommended:

```text
personal_notes/
  chinese_reviews/
  deep_research_cn/
  translations/
  discussion_notes/
```
