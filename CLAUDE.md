# Ship Health Monitoring - Agent Context

This file summarizes the current repository state for AI assistants and repository operators. It is not a scientific evidence artifact and does not override frozen package records.

## Current State

Current stage: repository publishing preparation after Blind Review v2 execution-package build.

Latest completed milestone:

`DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_PACKAGE_READY`

## Canonical Public Entry Points

- [README](README.md)
- [Publishing Status](PUBLISHING_STATUS.md)
- [Documentation Map](docs/documentation_map.md)
- [Marine Package v1.0](docs/marine_package_v1/marine_package_v1.md)
- [External Validation Definition Approval and Freeze Record](docs/external_validation/external_validation_definition_approval_and_freeze_record.md)
- [Deep Research Blind Review Execution Package README](docs/deep_research_blind_review_execution_v2/README_START_HERE.md)

## Process Boundaries

Do not state or imply:

- Marine validity has been established.
- Marine feasibility has been established.
- Deployment readiness has been demonstrated.
- Shipboard RUL capability has been validated.
- External Validation has started or completed.
- An External Reviewer has been selected.
- Marine data has been requested, received, or qualified.

Current process states:

- Marine Package v1.0: complete and frozen.
- External Validation definition: approved and frozen.
- External Validation execution: not started.
- External reviewer: not selected.
- Deep Research Blind Review execution: not started.
- Marine request gate: not evaluated.
- Marine data request: planned, not started.
- Marine validation: not started.

Next authorized workstream:

`DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001`

## Repository Layout

```text
docs/marine_package_v1/                         Frozen Marine Package v1.0
docs/external_validation/                       Frozen External Validation definition
docs/deep_research_review_package/              Locked Deep Research Review Package v1.1
docs/deep_research_review_package_transport_v2/ Frozen Transport v2
docs/deep_research_blind_review_v2/             Frozen Session Protocol
docs/deep_research_blind_review_execution_v2/   Verified execution package
lbnl_expected_state/                            Framework architecture, decisions, outputs, scripts
src/                                            Source and exploratory validation scripts
outputs/                                        Public-data outputs and historical generated artifacts
```

## Editing Rules

Do not modify frozen Marine Package, External Validation, Transport v2, Session Protocol, claim, gap, or evidence artifacts unless a task card explicitly authorizes that exact change.

For publication-readiness work, prefer updating public navigation and status documents rather than rewriting research artifacts.

## Manifest and Retrieval Rules

Use [SYSTEM_STATE.md](SYSTEM_STATE.md) as the current-state authority.

Use [manifest/repository_manifest.json](manifest/repository_manifest.json) to check document authority, lifecycle, visibility, retrieval priority, and source/copy role.

Use [manifest/machine_retrieval_manifest.json](manifest/machine_retrieval_manifest.json) for curated machine retrieval order. Do not treat generated transport or execution copies as scientific source authorities.
