# Repository Governance and Knowledge Architecture Review

Document status: Governance review
Task ID: REPOSITORY_GOVERNANCE_KNOWLEDGE_ARCHITECTURE_REVIEW

## Executive Summary

The repository is publishable as a serious research and governance repository, but its knowledge architecture is approaching the point where informal navigation will not scale. The current public entry points are much better than the earlier state: README, SYSTEM_STATE, PUBLISHING_STATUS, documentation_map, and CLAUDE now align on the main process boundaries. However, they still duplicate current-state facts across several files.

Overall assessment: READY_WITH_MINOR_IMPROVEMENTS.

The repository does not need a scientific rewrite or evidence reorganization before public presentation. It does need a formal Single Source of Truth hierarchy, a machine-readable repository manifest, a public/internal/archive boundary, and a scalable directory policy before it grows into a 1,000+ document multi-project repository.

## Repository Architecture

### Strengths

- The repository has strong evidence-governance records: Marine Package v1.0, gap register, artifact index, freeze manifests, External Validation definition artifacts, Deep Research packages, Transport v2, and Session Protocol records.
- Public-facing status has been consolidated into README, SYSTEM_STATE, PUBLISHING_STATUS, and documentation_map.
- Review and delivery artifacts are separated from primary source content through Transport v2 and the Blind Review execution package.
- The repository preserves important historical context instead of silently deleting or rewriting it.
- Deep Research and operator workflows now have explicit prepared packages rather than relying on ad hoc file selection.

### Weaknesses

- Current-state facts are repeated in multiple documents. This is manageable now but will create drift as the repository evolves.
- `docs/` mixes canonical artifacts, governance records, personal notes, translations, draft Word documents, PDFs, historical reviews, and review packages.
- There is no repository-level machine-readable manifest that declares document role, audience, authority level, lifecycle state, and retrieval priority.
- There is no explicit public/internal/archive classification for documents.
- Root-level directories contain personal-note and historical material with inconsistent naming conventions.
- Git status currently contains many untracked generated and governance artifacts, which creates release-governance ambiguity.

## Single Source of Truth

### Documents That Describe Repository Status

- `README.md`: public repository entry point.
- `SYSTEM_STATE.md`: concise current operational state.
- `PUBLISHING_STATUS.md`: public publishing state and readiness.
- `docs/documentation_map.md`: navigation map and detailed document routing.
- `CLAUDE.md`: AI assistant and operator context.
- `docs/repository_review/repository_publishing_review.md`: publication-readiness review.
- Governance records inside `docs/marine_package_v1/`, `docs/external_validation/`, `docs/deep_research_review_package_transport_v2/`, and `docs/deep_research_blind_review_v2/`.

### Current Authority Roles

- Authoritative repository state: `SYSTEM_STATE.md`, backed by frozen package and protocol records.
- Public entry point: `README.md`.
- Publishing entry point: `PUBLISHING_STATUS.md`.
- Navigation entry point: `docs/documentation_map.md`.
- AI assistant entry point: `CLAUDE.md`.
- Operator entry point for Blind Review: `docs/deep_research_blind_review_execution_v2/README_START_HERE.md`.

### Duplicated State Definitions

The same process states appear in README, SYSTEM_STATE, PUBLISHING_STATUS, documentation_map, and CLAUDE. They currently agree at the high level, but future updates could easily leave one stale.

### Recommended Hierarchy

Use this hierarchy going forward:

1. Frozen package and protocol records are the authority for their own scope.
2. `SYSTEM_STATE.md` is the single current-state rollup.
3. `PUBLISHING_STATUS.md` is the public publishing interpretation of `SYSTEM_STATE.md`.
4. `README.md` is the human landing page and should summarize, not duplicate, detailed states.
5. `docs/documentation_map.md` is the navigation index and should link to current authorities.
6. `CLAUDE.md` is an AI-assistant convenience file and must defer to `SYSTEM_STATE.md`.
7. Operator package READMEs are task-specific entry points and must not redefine global state.

Recommended rule: any future process-state update must update `SYSTEM_STATE.md` first, then update dependent entry points only if their summary changes.

## Knowledge Architecture Review

### Discoverability

Discoverability is adequate for the current repository after the publishing update. A new reader can now follow README to Publishing Status, Documentation Map, Marine Package, External Validation, and Blind Review execution artifacts.

The main discoverability risk is volume: `docs/` contains many high-value but non-canonical documents at the same visual level as canonical governance artifacts.

### Maintainability

Maintainability is acceptable for a single project but strained for future multi-project growth. The repository already has separate conceptual domains:

- Framework architecture.
- Marine Package governance.
- External Validation governance.
- Deep Research package preparation.
- Transport engineering.
- Blind Review session execution.
- Historical exploratory research.

These domains are currently discoverable, but not yet governed by a shared repository taxonomy.

### Scalability

The current architecture will not scale cleanly to thousands of documents unless the repository adds explicit manifests, document classes, and archive boundaries. Without that, new review packages and generated execution copies will multiply faster than humans or retrieval systems can identify the canonical source.

## Website Readiness

The repository can support a future `jqhe.uk` website, but the website should not mirror the repository tree directly.

### Canonical Website Pages

Recommended initial website information architecture:

1. Home / Project Boundary
2. Current Status
3. Marine Package v1.0
4. Evidence and Claims Boundary
5. External Validation Definition
6. Deep Research Review Interface
7. Framework Architecture
8. Dataset and Validation Artifacts
9. Governance and Change Control
10. Archive / Historical Notes

### Suitable for Publication

- README and PUBLISHING_STATUS.
- Marine Package v1.0 narrative and boundary records.
- External Validation definition and approval/freeze records.
- Transport v2 architecture and review guide.
- Blind Review execution package README and prompts, if framed as review inputs.
- Health Evidence Framework and design decisions.

### Should Remain Internal or Archived by Default

- Personal notes and translations.
- Older concept paper drafts and duplicate DOCX files.
- Large PDFs used as research background unless licensing/publication status is clear.
- Temporary review packages and compressed archives unless needed for reproducibility.
- Raw generated outputs not referenced by current package manifests.

### Website Assessment

Website readiness: READY_WITH_MINOR_IMPROVEMENTS.

The repository has the content needed for a site. It needs a website content map and a publication policy before implementation.

## Machine Readiness

### Deep Research

Deep Research readiness is strong because Transport v2 and the execution package exist. These provide curated reading packs, lookup files, evidence packs, prompts, and attachment inventories.

Risk: general repository retrieval may still pick stale historical notes if pointed at the whole repo instead of the curated transport.

### Codex and Claude

Codex and Claude benefit from README, SYSTEM_STATE, PUBLISHING_STATUS, documentation_map, and CLAUDE. The main risk is duplicated status. Assistants should be instructed to treat SYSTEM_STATE as the current-state rollup and frozen records as scope authorities.

### Future MCP-Style Tooling

The repository is missing a machine-readable repository manifest. Recommended file:

`manifest/repository_manifest.json`

Minimum fields:

- document_id
- path
- title
- document_class
- authority_level
- lifecycle_state
- audience
- project_scope
- retrieval_priority
- public_visibility
- canonical_successor
- hash
- last_reviewed

This should be generated or validated automatically rather than maintained only by hand.

## Governance Review

### Naming Conventions

Strength: recent governance artifacts use explicit task IDs, states, and package names.

Weakness: older files use mixed casing, spaces, Chinese names, DOCX variants, and duplicate version strings. This is acceptable for archive material but weak for public navigation.

### Document Lifecycle

Current lifecycle states exist but are not governed globally. Examples include Draft, Frozen, Approved, Active Execution Log, Template, Reviewed, Archived, and Historical.

Recommended standard lifecycle vocabulary:

- DRAFT
- REVIEWED
- APPROVED
- FROZEN
- ACTIVE_APPEND_ONLY
- SUPERSEDED
- ARCHIVED
- HISTORICAL_NOTE

### Frozen Artifact Policy

Frozen artifact discipline is strong within Marine Package, External Validation, Transport v2, and Session Protocol. The governance risk is not the frozen artifacts themselves; it is the lack of a repo-wide rule for how frozen artifacts relate to generated copies, public pages, and future website transformations.

### Archive Policy

Archive policy is currently informal. A formal archive policy should define what can be moved, what must remain hash-stable, and what is personal or internal.

### Publishing Policy

Publishing policy should define:

- public-safe documents
- internal-only documents
- generated review interfaces
- external-collaboration packages
- citation or licensing considerations for PDFs and third-party papers
- prohibited public claims

### Public/Private Boundaries

The repository includes personal notes, translations, and possibly third-party PDFs. Before broad public release, determine whether each is intended for publication.

## Directory Architecture

Current structure is workable but not future-proof. Recommended future structure:

```text
docs/
  public/                 Public narrative pages and website-source documents
  governance/             Repository-wide governance policies and status records
  archive/                Historical notes, drafts, translations, and superseded docs
  repository_review/      Repository architecture and publishing reviews

projects/
  ship_health_monitoring/
    marine_package_v1/
    external_validation/
    validation/
    framework/

review/
  deep_research/
    package/
    transport_v2/
    session_protocol/
    execution_package/

manifest/
  repository_manifest.json
  public_manifest.json
  machine_retrieval_manifest.json

website/
  content/
  assets/
  build/
```

This should not be implemented automatically. It should be introduced through a separate migration plan because many frozen and hashed records reference current paths.

## Long-Term Maintainability

If this repository evolves for several years, it will need:

- a stable project namespace model;
- explicit document lifecycle rules;
- generated machine manifests;
- archive workflows;
- public/private document classification;
- automated link and hash checks;
- a policy for generated review copies versus source authorities;
- a website content source strategy;
- agent instructions that prevent stale or non-authoritative retrieval.

The current repository can support the next stage, but not indefinite growth without governance refactoring.

## Challenge Review

Assumption tested: the repository eventually contains 1,000+ documents, multiple independent research projects, public website content, external reviewers, Deep Research packages, Codex, Claude, and future AI agents.

### Scalability Risks

- Single `docs/` namespace will become too crowded for human review and machine retrieval.
- Duplicated current-state summaries will drift unless a state-update protocol is enforced.
- Frozen artifact path references will make later directory migration costly.
- Generated review packages may dominate retrieval results if not tagged as delivery copies.
- Public website content may accidentally quote or summarize frozen claims in a way that changes their strength.
- AI agents may prefer recent files over authoritative files unless retrieval priority is machine-readable.
- External reviewers may confuse source evidence, transport copies, execution copies, and website pages without explicit document roles.
- Multiple research projects will need independent state files; one root SYSTEM_STATE will become overloaded.

### Revised Recommendations From Challenge Review

The architecture should not rely only on human-readable README/navigation files. It needs a manifest-first governance layer before major expansion.

Revised priority:

1. Create a repository manifest and document taxonomy before website implementation.
2. Define a source-versus-transport-versus-execution-copy policy.
3. Define a public/private/archive classification policy.
4. Add automated checks for link validity, duplicate state strings, and retrieval-priority conflicts.
5. Only then consider directory migration or website generation.

## Risks

Priority 1 risks:

- State drift across README, SYSTEM_STATE, PUBLISHING_STATUS, documentation_map, and CLAUDE.
- Public release of personal notes or third-party materials not intended as public project artifacts.
- Deep Research retrieval against the whole repository instead of curated packages.

Priority 2 risks:

- Path instability if later directory reorganization happens after more freeze records are created.
- Generated delivery copies mistaken for source authorities.
- Website copy strengthening claims beyond frozen package boundaries.

Priority 3 risks:

- Long-term contributor confusion without document lifecycle labels.
- Manual governance burden increasing faster than the evidence base.
- Multi-project collisions in naming, claims, gaps, and review packages.

## Recommendations

### Priority 1

1. Adopt the Single Source of Truth hierarchy in this report.
2. Create `manifest/repository_manifest.json` with document roles, authority levels, lifecycle states, retrieval priorities, and public-visibility labels.
3. Create a repository governance policy covering document lifecycle, archive status, public/private status, and generated-copy handling.
4. Add a website content map before implementing `jqhe.uk`.

### Priority 2

5. Create an archive review task for historical notes, translations, old DOCX drafts, and duplicate concept papers.
6. Create a machine-retrieval guide for Deep Research, Codex, Claude, and future agents.
7. Add automated checks for broken links, stale next-workstream labels, and duplicate current-state definitions.
8. Add a public claims-and-boundaries page derived from Marine Package v1.0 without changing frozen claim text.

### Priority 3

9. Plan a future directory migration only after manifests exist.
10. Separate future multi-project content under a project namespace.
11. Treat website pages as derived public views, not as source evidence.
12. Maintain review packages and transport packages as delivery layers, not as scientific authorities.

## Final Decision

READY_WITH_MINOR_IMPROVEMENTS

Justification: the repository is currently coherent enough for public presentation, external collaboration preparation, Deep Research execution, and future website planning. The remaining issues are governance scalability issues, not immediate blockers. However, if the repository is expected to grow into a multi-project, AI-retrieved, website-backed knowledge base, a manifest-first governance layer should be added before substantial new growth.
