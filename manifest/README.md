# Repository Manifest

Document status: Governance reference
Task ID: MANIFEST_FIRST_REPOSITORY_GOVERNANCE_IMPLEMENTATION

## Purpose

The manifest layer provides machine-readable repository governance before website implementation. It identifies current core documents, their authority level, lifecycle state, intended audience, visibility class, retrieval priority, source/copy role, and SHA-256 hash.

The manifest does not change scientific conclusions, validation evidence, frozen artifacts, research claims, review results, or package contents.

## Files

- `repository_manifest.json`: complete governed document set for current core records.
- `public_manifest.json`: public-safe subset derived from the repository manifest.
- `machine_retrieval_manifest.json`: curated retrieval view for Deep Research, Codex, Claude, and future agents.

## Authority Hierarchy

1. Frozen package and protocol records are authoritative within their own scope.
2. `SYSTEM_STATE.md` is the repository current-state authority.
3. `PUBLISHING_STATUS.md` is the public publishing interpretation of `SYSTEM_STATE.md`.
4. `README.md` is the human landing page and summary.
5. `docs/documentation_map.md` is the navigation index.
6. `CLAUDE.md` is an AI-assistant convenience file and must defer to `SYSTEM_STATE.md`.
7. Operator package README files are task-specific entry points and must not redefine global state.
8. Website pages are derived public views and are never scientific or governance authorities.

## Required Entry Fields

Each entry contains:

```text
document_id
path
title
project_scope
document_class
authority_level
lifecycle_state
audience
public_visibility
retrieval_priority
copy_role
canonical_source
canonical_successor
hash
last_reviewed
notes
```

## Controlled Vocabularies

`document_class`: `STATE`, `PUBLIC_ENTRY`, `NAVIGATION`, `GOVERNANCE`, `SCIENTIFIC_SOURCE`, `PACKAGE`, `PROTOCOL`, `EXECUTION_INTERFACE`, `REVIEW`, `ARCHITECTURE`, `DECISION`, `SPECIFICATION`, `HISTORICAL_NOTE`

`authority_level`: `REPOSITORY_STATE_AUTHORITY`, `SCOPE_AUTHORITY`, `DERIVED_SUMMARY`, `NAVIGATION_ONLY`, `OPERATOR_CONTEXT`, `DELIVERY_INTERFACE`, `NON_AUTHORITATIVE`

`lifecycle_state`: `DRAFT`, `REVIEWED`, `APPROVED`, `FROZEN`, `ACTIVE_APPEND_ONLY`, `SUPERSEDED`, `ARCHIVED`, `HISTORICAL_NOTE`

`audience`: `PUBLIC`, `OPERATOR`, `REVIEWER`, `AI_AGENT`, `INTERNAL`, `MIXED`

`public_visibility`: `PUBLIC`, `PUBLIC_WITH_BOUNDARIES`, `INTERNAL`, `ARCHIVE_ONLY`, `REVIEW_PACKAGE_ONLY`

`retrieval_priority`: integer 1 through 5. Priority 1 is highest.

`copy_role`: `SOURCE`, `DERIVED_SUMMARY`, `TRANSPORT_COPY`, `EXECUTION_COPY`, `WEBSITE_DERIVATIVE`, `NAVIGATION_RECORD`

## Update Rules

Update `SYSTEM_STATE.md` first for repository state changes. Then update summaries, manifests, and navigation if needed.

For manifest updates:

1. Add or update the document entry.
2. Compute SHA-256 from the current repository file.
3. Preserve authority boundaries: generated transport and execution copies are not scientific source authorities.
4. Rebuild `public_manifest.json` and `machine_retrieval_manifest.json` from `repository_manifest.json`.
5. Run the repository governance validation scripts.

## Hash Procedure

Hashes are uppercase SHA-256 values computed from current file bytes. Do not infer authority from modification time.

## Future Agent Use

Agents should use `machine_retrieval_manifest.json` for retrieval order and `repository_manifest.json` for authority checks. Whole-repository retrieval should be avoided when a curated review package or transport exists for the task.
