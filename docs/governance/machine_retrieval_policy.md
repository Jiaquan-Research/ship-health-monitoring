# Machine Retrieval Policy

Document status: Governance policy
Task ID: MANIFEST_FIRST_REPOSITORY_GOVERNANCE_IMPLEMENTATION

## Purpose

This policy defines how Deep Research, Codex, Claude, and future agents should retrieve repository knowledge without confusing source authorities, summaries, transports, execution copies, or historical notes.

## Preferred Entry Points

General repository state:

- `SYSTEM_STATE.md`
- `PUBLISHING_STATUS.md`
- `README.md`

Marine Package:

- `docs/marine_package_v1/marine_package_v1.md`
- `docs/marine_package_v1/marine_package_v1_gap_register.md`
- `docs/marine_package_v1/marine_package_v1_artifact_index.md`

External Validation:

- `docs/external_validation/external_validation_definition_approval_and_freeze_record.md`
- `docs/external_validation/external_validation_of_project_results_specification.md`

Deep Research Blind Review:

- `docs/deep_research_blind_review_execution_v2/README_START_HERE.md`
- `docs/deep_research_review_package_transport_v2/00_review_guide_and_pack_index.md`

Framework architecture:

- `lbnl_expected_state/docs/architecture/health_evidence_framework.md`
- `lbnl_expected_state/docs/decisions/`

## Retrieval Priority Rules

Use `manifest/machine_retrieval_manifest.json` for retrieval order. Priority 1 documents should be loaded before lower-priority documents unless the task requires a scoped package.

Authority is not determined by recency. Frozen and scope records remain authoritative within their own scope even if a derived summary is newer.

## Source Versus Transport Versus Execution Copy

`SOURCE` documents are source authorities or direct source records.

`TRANSPORT_COPY` documents are delivery representations for review systems.

`EXECUTION_COPY` documents are upload-ready delivery copies for a specific execution protocol.

Transport and execution copies may be useful for review, but they must not override source authorities or frozen records.

## Curated Review Packages

When a curated package or transport exists for a review task, use it instead of whole-repository retrieval. Whole-repository retrieval is more likely to surface stale notes, duplicate drafts, or non-authoritative files.

## Stale-Document Handling

If documents conflict, apply the authority hierarchy:

1. Scoped frozen records.
2. `SYSTEM_STATE.md`.
3. `PUBLISHING_STATUS.md`.
4. README and documentation map summaries.
5. AI assistant convenience files.
6. Historical notes and archive records.

Report suspected stale documents rather than silently resolving them by recency.

## Access Declaration Requirements

Deep Research and external model reviews should declare which packs or documents were read, partially read, used only for lookup, not accessed, or affected by parser failure.

## Agent Instructions

Codex, Claude, Deep Research, and future agents should:

- read the manifest before broad retrieval;
- preserve repository evidence and external evidence as separate categories;
- avoid strengthening frozen claims;
- avoid treating generated copies as source authorities;
- avoid whole-repository retrieval when a curated package exists;
- report missing or ambiguous authority rather than inventing metadata.
