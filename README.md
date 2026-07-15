# Ship Health Monitoring

This repository contains a traceable research and governance package for a ship health monitoring framework. The current public state is an evidence-boundary package: it consolidates public-data validation evidence, framework architecture, claim boundaries, open gaps, and review protocols before any Marine data request or Marine validation begins.

The repository does not claim Marine validity, Marine feasibility, deployment readiness, shipboard remaining-life capability, or completed External Validation.

## Current Status

Current stage: public repository publishing preparation after Deep Research Blind Review v2 execution-package build.

Latest completed milestone:

`DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_PACKAGE_READY`

Stable completed components:

- Marine Package v1.0 is complete and frozen with documented gaps.
- External Validation definition is approved and frozen.
- Deep Research Review Package v1.1 is locked.
- Transport v2 is approved, verified, and frozen as the default LLM Blind Review interface.
- Blind Review v2 Session Protocol is approved, verified, and frozen.
- Blind Review v2 execution package is verified and ready for human execution.

Open process states:

- External Validation execution: not started.
- External reviewer: not selected.
- Evidence package for External Validation: frozen definition, not issued.
- Deep Research Blind Review execution: not started.
- Marine request gate: not evaluated.
- Marine data request: planned, not started.
- Marine data received: no.
- Marine validation: not started.

## Start Here

For public readers:

1. [Publishing Status](PUBLISHING_STATUS.md)
2. [Repository Documentation Map](docs/documentation_map.md)
3. [Marine Package v1.0](docs/marine_package_v1/marine_package_v1.md)
4. [External Validation Definition Approval and Freeze Record](docs/external_validation/external_validation_definition_approval_and_freeze_record.md)
5. [Deep Research Blind Review Execution Package](docs/deep_research_blind_review_execution_v2/README_START_HERE.md)

Website architecture and implementation:

- [Website Architecture Design](docs/website/website_architecture_design.md)
- [Website Implementation Record v0.1](docs/website/website_implementation_record_v0_1.md)
- Local site source: `website/`

For framework architecture:

- [Health Evidence Framework](lbnl_expected_state/docs/architecture/health_evidence_framework.md)
- [Decision Documents](lbnl_expected_state/docs/decisions/)
- [Dataset Qualification Specification](docs/dataset_qualification_specification.md)

## Repository Structure

```text
docs/
  documentation_map.md                         Repository navigation map
  marine_package_v1/                           Frozen Marine Package v1.0
  external_validation/                         Frozen External Validation definition and templates
  deep_research_review_package/                Locked Deep Research Review Package v1.1
  deep_research_review_package_transport_v2/   Frozen Transport v2 review interface
  deep_research_blind_review_v2/               Frozen Blind Review Session Protocol
  deep_research_blind_review_execution_v2/     Submission-ready execution package
  repository_review/                           Repository publishing review records

lbnl_expected_state/
  docs/                                        Framework architecture, decisions, specifications, gates
  outputs/                                     Framework outputs and generated artifacts
  scripts/                                     Framework scripts

src/
  condition_normalization/
  expected_state_model/
  residual/
  health_index/
  cusum/
  legacy and exploratory validation scripts

outputs/
  Public-data validation outputs, historical reports, figures, and generated artifacts
```

## Validation Boundary

The current project uses public datasets and framework records to support technical and architectural learning. Public-data evidence supports bounded statements about residual, Health Evidence, Health Indicator, nonresidual trend, and review-process design routes.

The following are not established:

- Marine performance.
- Marine feasibility.
- Deployment readiness.
- Shipboard failure prediction.
- Shipboard remaining useful life.
- Validated shipboard alarms.
- Marine data qualification.
- External Validation completion.

## Review and Collaboration Status

External Validation has a frozen definition and human-reviewer protocol, but execution has not started and no external reviewer has been selected.

Deep Research Blind Review has a verified execution package for ChatGPT and Claude sessions. The package is prepared for human operation, but no Blind Review has been executed by this repository task.

jqhe.uk website v0.1 has been implemented as a static Astro site under `website/`. It is a derived publication layer and is not deployed by this repository task.

Next authorized workstream:

`DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001`

## Reproducibility Notes

The repository contains controlled manifests, artifact indexes, review packages, transport manifests, and verification reports. Some historical and exploratory outputs remain in the repository for traceability and are not the current canonical entry points.

Use [docs/documentation_map.md](docs/documentation_map.md) and [PUBLISHING_STATUS.md](PUBLISHING_STATUS.md) to distinguish current authoritative records from historical notes.


Repository URL: https://github.com/Jiaquan-Research/ship-health-monitoring

Website note: Cloudflare Pages deployment preparation is available under `website/`; deployment and domain binding are not performed in this repository commit.
