# Repository Governance Policy

Document status: Governance policy
Task ID: MANIFEST_FIRST_REPOSITORY_GOVERNANCE_IMPLEMENTATION

## Purpose

This policy defines the minimum repository governance layer required before website implementation. It does not change scientific conclusions, validation evidence, frozen artifacts, research claims, review results, or package contents.

## Authority Hierarchy

1. Frozen package and protocol records are authoritative within their own scope.
2. `SYSTEM_STATE.md` is the repository current-state authority.
3. `PUBLISHING_STATUS.md` is the public publishing interpretation of `SYSTEM_STATE.md`.
4. `README.md` is the human landing page and summary.
5. `docs/documentation_map.md` is the navigation index.
6. `CLAUDE.md` is an AI-assistant convenience file and must defer to `SYSTEM_STATE.md`.
7. Operator package README files are task-specific entry points and must not redefine global state.
8. Website pages are derived public views and are never scientific or governance authorities.

## Document Lifecycle

Allowed lifecycle states:

- `DRAFT`
- `REVIEWED`
- `APPROVED`
- `FROZEN`
- `ACTIVE_APPEND_ONLY`
- `SUPERSEDED`
- `ARCHIVED`
- `HISTORICAL_NOTE`

Lifecycle state must be recorded in the repository manifest for governed documents.

## Source-Versus-Copy Roles

Allowed copy roles:

- `SOURCE`: original authoritative or source-level document.
- `DERIVED_SUMMARY`: summary derived from source authorities.
- `TRANSPORT_COPY`: deterministic review transport copy.
- `EXECUTION_COPY`: delivery copy prepared for execution.
- `WEBSITE_DERIVATIVE`: future website view derived from manifest-selected sources.
- `NAVIGATION_RECORD`: map, index, or routing document.

Transport and execution copies must not be treated as scientific source authorities.

## Update Order

For process-state changes:

1. Update the authoritative frozen or scope record if the change belongs to a scoped package or protocol.
2. Update `SYSTEM_STATE.md`.
3. Update `PUBLISHING_STATUS.md`, `README.md`, `docs/documentation_map.md`, and `CLAUDE.md` only as needed.
4. Update repository manifests and hashes.
5. Run governance validation scripts.

## Frozen Artifact Handling

Frozen artifacts must not be edited unless an authorized task explicitly permits the exact change. Derived summaries, website pages, transport copies, and execution copies must preserve the frozen boundary and must not strengthen claims.

## Archive Rules

Historical notes, translations, old drafts, exploratory outputs, and duplicate packages may be marked `ARCHIVE_ONLY` or `HISTORICAL_NOTE`. They must not be deleted, moved, or rewritten without a separate authorized archive task.

## Document-ID Policy

Manifest `document_id` values must be stable, unique, and descriptive. They must not be reused for a different document after a path or authority change.

## Path-Change Rules

Path changes for governed documents require manifest updates, link checks, and review of any frozen records that cite the old path. Frozen package paths must not be changed unless the scope authority permits it.

## Generated-Copy Rules

Generated copies must identify their source through manifest metadata. Delivery packages, transports, and website derivatives are access layers, not evidence authorities.

## Multi-Project Namespace Expectations

Future projects should use explicit project scopes in the manifest and should not overload the ship-health-monitoring state model. Multi-project expansion should introduce project namespaces before adding large new document sets.

## Manifest Update Requirements

Any new governed document must be added to `manifest/repository_manifest.json` with controlled values and a current SHA-256 hash. Public and machine retrieval views must be regenerated from the repository manifest.
