# jqhe.uk Website Architecture Design

Document status: Architecture design
Task ID: PHASE_5A_WEBSITE_ARCHITECTURE_PUBLIC_RESEARCH_PORTAL_DESIGN
Target site: jqhe.uk

## Executive Summary

jqhe.uk should be a public research portal derived from the repository governance layer, not a mirror of the repository tree. The site must serve four audiences at the same time:

- public visitors who need a clear project boundary;
- technical collaborators who need method and evidence context;
- external reviewers who need source authority, claims, gaps, and review status;
- AI agents that need machine-readable entry points and retrieval rules.

The core design principle is separation of roles:

- Source authority remains in frozen package, protocol, state, and governance records.
- Website pages are derived summaries and navigation views.
- Review interfaces remain distinct from scientific source records.
- Machine interfaces expose manifests and retrieval priorities without treating generated copies as source authority.

Final recommendation: WEBSITE_ARCHITECTURE_READY.

## Information Architecture

The site uses a hub-and-spoke structure. The Home page and Current Status page establish project boundaries. Project and research pages explain what exists. Review and Machine Access pages expose controlled interfaces for reviewers and agents. Governance pages define how the site avoids overclaiming.

### IA Tree

```text
Home
├─ Current Status
├─ Research
│  ├─ Framework
│  └─ Validation
├─ Projects
│  └─ Ship Health Monitoring
│     ├─ Marine Package
│     ├─ Evidence and Claim Boundaries
│     ├─ Framework
│     ├─ Validation
│     ├─ External Validation
│     └─ Deep Research
├─ Review Portal
│  ├─ Deep Research
│  ├─ Transport Packages
│  ├─ Execution Packages
│  ├─ External Validation
│  ├─ Review Workflow
│  └─ Reviewer Instructions
├─ Machine Access
│  ├─ Manifest Browser
│  ├─ Repository Manifest
│  ├─ Public Manifest
│  ├─ Machine Retrieval Manifest
│  ├─ Governance Vocabularies
│  └─ Future API / MCP
├─ Governance
│  ├─ Authority Hierarchy
│  ├─ Publishing Policy
│  ├─ Machine Retrieval Policy
│  └─ Repository Reviews
├─ Publications
├─ Archive
└─ About
```

### Page Inventory

| page | purpose | audience | parent | children | authority source | update trigger |
| --- | --- | --- | --- | --- | --- | --- |
| Home | State what the project is and is not | Public; collaborators | None | Current Status; Projects; Review Portal; Machine Access | README; PUBLISHING_STATUS; SYSTEM_STATE | README or publishing status update |
| Current Status | Show current process state and boundaries | Public; reviewers; AI agents | Home | None | SYSTEM_STATE; PUBLISHING_STATUS | SYSTEM_STATE update |
| Research | Explain research program and method families | Public; technical collaborators | Home | Framework; Validation | Marine Package; Health Evidence Framework | Framework or package update |
| Projects | List project scopes | Public; collaborators; AI agents | Home | Ship Health Monitoring | repository_manifest; documentation_map | Manifest project-scope update |
| Ship Health Monitoring | Project landing page | Public; collaborators | Projects | Marine Package; Framework; Validation; External Validation; Deep Research | README; Marine Package v1.0 | Project state update |
| Framework | Explain architecture and decision documents | Technical collaborators; reviewers | Research / Project | None | Health Evidence Framework; DD documents | Framework or decision update |
| Validation | Explain public-data validation scope | Reviewers; collaborators | Research / Project | None | Marine Package; validation records listed in manifests | Validation package update |
| Marine Package | Present Marine Package v1.0 and boundaries | Reviewers; collaborators | Ship Health Monitoring | Evidence and Claim Boundaries | Marine Package v1.0; Gap Register; Artifact Index | New package version or authorized correction |
| Evidence and Claim Boundaries | Explain frozen claims, active gaps, evidence limits | Reviewers; AI agents | Marine Package | None | Claim Boundary; Evidence Map; Gap Register | Authorized claim/gap/evidence update |
| External Validation | Explain definition, status, and human-reviewer boundary | External reviewers; collaborators | Ship Health Monitoring / Review Portal | None | External Validation approval/freeze record; specification | External Validation state change |
| Deep Research | Explain Deep Research package, Transport v2, and boundaries | Reviewers; operators; AI agents | Ship Health Monitoring / Review Portal | Transport Packages; Execution Packages | Transport v2; Session Protocol; Execution Package | Review package or transport update |
| Review Portal | Route reviewers/operators to review workflows | Operators; reviewers | Home | Deep Research; External Validation; Reviewer Instructions | Execution Package; Session Protocol; External Validation definition | Review interface update |
| Machine Access | Provide manifests and retrieval rules | AI agents; developers | Home | Manifest Browser; Future API | repository_manifest; machine_retrieval_manifest; policies | Manifest update |
| Governance | Explain authority, lifecycle, publishing rules | Reviewers; collaborators; AI agents | Home | Policies; Repository Reviews | governance policies; repository reviews | Governance policy update |
| Publications | Curate papers, public writeups, and future releases | Public; collaborators | Home | None | public_manifest; publishing policy | Publication approval |
| Archive | Route historical material selectively | Researchers | Home | None | documentation_map; future archive manifest | Archive review task |
| About | Explain project context and collaboration boundary | Public | Home | None | README; PUBLISHING_STATUS | Publishing status update |

## Navigation

### Global Navigation

Global nav should be stable and short:

```text
Status | Research | Projects | Review Portal | Machine Access | Governance | About
```

Secondary pages such as Publications and Archive can live in the footer or under Governance until they contain enough curated content.

### Breadcrumb Rules

Breadcrumbs follow IA hierarchy, not repository paths.

Examples:

```text
Home > Projects > Ship Health Monitoring > Marine Package
Home > Review Portal > Deep Research > Execution Packages
Home > Machine Access > Repository Manifest
```

Breadcrumbs must not imply source authority. A breadcrumb is navigation only.

### Sidebar Rules

Use sidebars for scoped sections:

- Project sidebar: Overview, Marine Package, Boundaries, Framework, Validation, External Validation, Deep Research.
- Review sidebar: Deep Research, Transport, Execution Package, External Validation, Reviewer Instructions, Review Boundaries.
- Machine sidebar: Manifest Browser, Document IDs, Authority Levels, Lifecycle States, Copy Roles, Retrieval Priority, API/MCP.
- Governance sidebar: Authority Hierarchy, Publishing Policy, Machine Retrieval Policy, Archive Policy, Repository Reviews.

### Cross-Page Links

Every page should include:

- source authority links;
- related status links;
- related review links if applicable;
- machine metadata link for AI agents.

Do not cross-link historical notes from primary public pages unless archive classification is complete.

### Search Behavior

Search should default to public-manifest content, not the whole repository. Search facets:

- project scope;
- document class;
- authority level;
- lifecycle state;
- audience;
- copy role;
- retrieval priority.

Search results must badge `SOURCE`, `DERIVED_SUMMARY`, `TRANSPORT_COPY`, `EXECUTION_COPY`, and `NAVIGATION_RECORD`.

### Footer Navigation

Footer links:

- Repository on GitHub;
- Public Manifest;
- Machine Retrieval Manifest;
- Publishing Policy;
- Current Status;
- Archive;
- Contact/About.

### Machine Entry Navigation

Machine entry should be visible in header/footer and available at a stable path:

```text
/machine
/machine/repository-manifest
/machine/public-manifest
/machine/retrieval-manifest
/machine/policies
```

## Page Specifications

Each page follows a shared content model:

- Hero section.
- Summary section.
- Authority banner.
- Current status block where applicable.
- Evidence or source block.
- Related documents.
- Machine metadata.
- Review links where applicable.
- Repository links.

### Home

Hero: "Ship Health Monitoring Research and Evidence Governance"

Summary: concise project description and boundary statement.

Authority banner: Derived from README, PUBLISHING_STATUS, and SYSTEM_STATE.

Current status block: package frozen; External Validation not started; Marine request planned, not started; Blind Review not started.

Evidence block: link to Marine Package and Framework.

Related documents: README, SYSTEM_STATE, PUBLISHING_STATUS.

Machine metadata: ROOT-README, ROOT-SYSTEM-STATE, ROOT-PUBLISHING-STATUS.

Review links: Review Portal.

Repository links: GitHub root and documentation map.

### Current Status

Hero: "Current Project State"

Summary: current stage and latest milestone.

Authority banner: SYSTEM_STATE is the current-state authority.

Current status block: all current process states.

Evidence block: none; this is state, not evidence.

Related documents: SYSTEM_STATE, PUBLISHING_STATUS, Documentation Map.

Machine metadata: authority level `REPOSITORY_STATE_AUTHORITY`.

Review links: External Validation and Deep Research status.

Repository links: SYSTEM_STATE.md.

### Research

Hero: "Research Program"

Summary: evidence-boundary research, not deployment.

Authority banner: derived from Marine Package and Health Evidence Framework.

Current status block: public-data evidence only; Marine validation not started.

Evidence block: framework architecture, public validation records, dataset qualification.

Related documents: Marine Package, Health Evidence Framework, Dataset Qualification Specification.

Machine metadata: project scopes `ship_health_monitoring` and `framework`.

Review links: Validation and Marine Package pages.

Repository links: source documents in public manifest.

### Projects

Hero: "Projects"

Summary: project registry based on manifest project scopes.

Authority banner: repository manifest is the source for project scope list.

Current status block: one active public project: Ship Health Monitoring.

Evidence block: none.

Related documents: repository manifest, documentation map.

Machine metadata: project_scope values.

Review links: project-specific Review Portal links.

Repository links: manifest.

### Ship Health Monitoring

Hero: "Ship Health Monitoring"

Summary: public-data and governance package for future Marine validation preparation.

Authority banner: derived from README and Marine Package v1.0.

Current status block: Marine Package frozen; no Marine validity.

Evidence block: Marine Package, Framework, Validation.

Related documents: Marine Package, Gap Register, Artifact Index.

Machine metadata: project_scope `ship_health_monitoring`.

Review links: External Validation, Deep Research.

Repository links: docs/marine_package_v1.

### Framework

Hero: "Health Evidence Framework"

Summary: architecture and decision documents.

Authority banner: Health Evidence Framework and DD documents are scope authorities.

Current status block: framework records available; no deployment claim.

Evidence block: architecture, DD-002 through DD-006, Dataset Qualification.

Related documents: framework decisions.

Machine metadata: HEF-ARCHITECTURE and DD document IDs.

Review links: Validation.

Repository links: lbnl_expected_state docs.

### Validation

Hero: "Public Dataset Validation"

Summary: public-data evidence and limitations.

Authority banner: Marine Package and manifest-selected validation records.

Current status block: public-data validation only; Marine validation not started.

Evidence block: CODLAG, PRONOSTIA, FD002, N-CMAPSS roles.

Related documents: Marine Package Evidence Map, Artifact Index, validation records.

Machine metadata: evidence document IDs and retrieval priorities.

Review links: Evidence and Claim Boundaries.

Repository links: validation source paths.

### Marine Package

Hero: "Marine Package v1.0"

Summary: frozen evidence and boundary package.

Authority banner: Marine Package v1.0 is scope authority.

Current status block: complete and frozen; documented gaps remain active.

Evidence block: package narrative, gap register, artifact index, evidence map.

Related documents: Claim Boundary, Gap Register, Completion Review, Freeze Manifest.

Machine metadata: MPV1 document IDs.

Review links: External Validation.

Repository links: docs/marine_package_v1.

### Evidence and Claim Boundaries

Hero: "Claims, Evidence, and Gaps"

Summary: frozen claims and active gaps in plain language.

Authority banner: claim boundary, evidence map, and gap register are source authorities.

Current status block: gaps remain as recorded; no automatic closure.

Evidence block: support levels, gap categories, prohibited wording.

Related documents: Claim Boundary, Evidence Map, Gap Register.

Machine metadata: claim/gap source document IDs.

Review links: Deep Research and External Validation.

Repository links: source CSV and Markdown files.

### External Validation

Hero: "External Validation Definition"

Summary: approved and frozen validation mechanism; execution not started.

Authority banner: External Validation approval/freeze record and specification.

Current status block: reviewer not selected; evidence package not issued.

Evidence block: reviewer eligibility, human reviewer requirement, decision labels, Marine request gate.

Related documents: specification, evidence manifest, templates, approval record.

Machine metadata: EXTVAL document IDs.

Review links: Review Portal.

Repository links: docs/external_validation.

### Deep Research

Hero: "Deep Research Blind Review"

Summary: curated advisory review interface, distinct from External Validation.

Authority banner: Transport v2, Session Protocol, and execution package are delivery interfaces.

Current status block: execution package ready; Blind Review not started.

Evidence block: Transport v2 packs, session protocol, prompts.

Related documents: Transport guide, execution package README, Session Protocol.

Machine metadata: TRV2 and BRV2 document IDs.

Review links: Review Portal.

Repository links: transport and execution package directories.

### Review Portal

Hero: "Review Portal"

Summary: controlled entry point for human operators and reviewers.

Authority banner: review workflows are delivery interfaces, not scientific authorities.

Current status block: Deep Research execution not started; External Validation not started.

Evidence block: review workflows and package boundaries.

Related documents: execution package, session protocol, external validation templates.

Machine metadata: delivery-interface document IDs.

Review links: Deep Research, External Validation, Reviewer Instructions.

Repository links: execution package README.

### Machine Access

Hero: "Machine Access"

Summary: manifests, retrieval policies, and future API/MCP access.

Authority banner: repository manifest and machine retrieval policy.

Current status block: manifest v1.0 available.

Evidence block: document IDs, authority levels, lifecycle states, copy roles, retrieval priorities.

Related documents: repository manifest, public manifest, machine retrieval manifest.

Machine metadata: direct JSON links.

Review links: Deep Research transport and execution package.

Repository links: manifest directory and governance policies.

### Governance

Hero: "Repository Governance"

Summary: authority hierarchy, publishing policy, retrieval policy, and reviews.

Authority banner: governance policies are scope authorities for publication and retrieval behavior.

Current status block: manifest-first governance layer implemented.

Evidence block: policy summaries and repository review findings.

Related documents: repository governance policy, publishing policy, machine retrieval policy.

Machine metadata: governance document IDs.

Review links: Repository reviews.

Repository links: docs/governance and docs/repository_review.

### Publications

Hero: "Publications"

Summary: future curated public papers and releases.

Authority banner: publication list must be selected through public manifest and publishing policy.

Current status block: no publication workflow implemented by this architecture phase.

Evidence block: none until publication approval.

Related documents: Publishing Policy.

Machine metadata: future publication document IDs.

Review links: none by default.

Repository links: public manifest.

### Archive

Hero: "Archive"

Summary: historical material and superseded records after archive review.

Authority banner: archive content is not current authority.

Current status block: archive classification incomplete.

Evidence block: none unless an archive manifest is created.

Related documents: documentation map and future archive manifest.

Machine metadata: lifecycle states `ARCHIVED` and `HISTORICAL_NOTE`.

Review links: none by default.

Repository links: documentation map historical sections.

### About

Hero: "About"

Summary: project context and collaboration boundary.

Authority banner: derived from README and Publishing Status.

Current status block: collaboration-ready with boundaries.

Evidence block: none.

Related documents: README, PUBLISHING_STATUS.

Machine metadata: public entry document IDs.

Review links: Review Portal.

Repository links: GitHub and manifest.

## Machine Access

Machine Access is a first-class website section, not a hidden developer page.

### Manifest Browser

The Manifest Browser should expose:

- document ID;
- title;
- path;
- project scope;
- document class;
- authority level;
- lifecycle state;
- audience;
- public visibility;
- retrieval priority;
- copy role;
- canonical source;
- canonical successor;
- hash;
- notes.

It should default to `public_manifest.json` for public users and expose `repository_manifest.json` as a governed JSON download.

### Repository Manifest

Purpose: full governed core document set.

Display: searchable table with authority and lifecycle filters.

Boundary: repository manifest is governance metadata, not scientific evidence.

### Machine Retrieval Manifest

Purpose: curated retrieval order for AI agents.

Display:

- preferred entry points;
- warnings against whole-repository retrieval;
- copy-role distinctions;
- retrieval-priority sorted document list.

### Public Manifest

Purpose: safe public subset.

Display: website content source list.

Use: site generator must select from this manifest by default.

### Governance Vocabularies

Display controlled values for:

- Document IDs;
- Authority Levels;
- Lifecycle States;
- Copy Roles;
- Retrieval Priority;
- Public Visibility.

### Future MCP Endpoint

Future endpoint shape:

```text
/api/manifest/repository
/api/manifest/public
/api/manifest/machine
/api/documents/{document_id}
/api/search?project_scope=&document_class=&authority_level=&copy_role=
/api/status
```

MCP-style tools should expose read-only retrieval against manifests and document metadata. They must not infer authority from recency.

### Future API Layout

API responses should include:

- manifest version;
- generated date;
- source hash;
- document metadata;
- authority warnings;
- source/copy role;
- public visibility.

No endpoint should publish INTERNAL, ARCHIVE_ONLY, or ambiguous-license content by default.

## Review Portal

The Review Portal separates advisory Deep Research, human External Validation, and execution package handling.

### Deep Research

Purpose: explain advisory blind review, Transport v2, Session Protocol, and execution package.

Boundary: Deep Research is not External Validation and does not modify frozen claims or gaps.

### Transport Packages

Show Transport v2 as the default LLM Blind Review interface. Provide:

- Review Guide;
- Reading Packs summary;
- Evidence Packs summary;
- Lookup layer;
- Integrity layer.

Transport files are delivery interfaces, not source authorities.

### Execution Packages

Show the verified execution package:

- Main Session Profile A/B/C;
- Evidence Profiles D/E1/E2;
- prompts;
- operator checklist;
- attachment inventory.

Execution packages are task-specific delivery copies and must not redefine global state.

### External Validation

Show:

- approved and frozen definition;
- human reviewer requirement;
- reviewer not selected;
- execution not started;
- evidence package not issued;
- Marine request gate not evaluated.

External Validation is a human external review mechanism, not an AI-only review.

### Review Workflow

Workflow display:

```text
Current state
→ Deep Research execution package ready
→ Human execution of Deep Research Blind Review
→ Later reconciliation
→ Separate External Validation reviewer selection and execution
```

Do not merge Deep Research and External Validation workflows.

### Reviewer Instructions

Reviewer pages should include:

- access declaration requirement;
- source versus transport distinction;
- repository/external evidence separation;
- no Marine validity claim;
- no complete-review claim after parser failure;
- no cross-model leakage for blind review.

### Review Boundaries

Display prohibited review outcomes:

- no claim changes;
- no gap closure;
- no Marine validation;
- no Marine request gate opening;
- no deployment readiness;
- no reviewer appointment unless a separate process records it.

### Review Status

Status cards:

- Deep Research execution: not started.
- External Validation execution: not started.
- External reviewer: not selected.
- Marine request gate: not evaluated.

## Publication Strategy

### Research

Belongs on website:

- public research overview;
- framework architecture summary;
- public-data validation roles;
- Marine Package boundaries.

Remains GitHub/source-only unless curated:

- raw outputs;
- large generated figures;
- unreviewed exploratory notes.

### Governance

Belongs on website:

- authority hierarchy;
- publishing policy;
- machine retrieval policy;
- public manifest;
- current status.

Remains GitHub/source-only:

- low-level generated manifests unless needed for machine access;
- task-specific intermediate records not selected by public manifest.

### Review

Belongs on website:

- Review Portal;
- Deep Research workflow;
- External Validation definition and boundaries;
- execution package overview.

Remains GitHub/source-only:

- raw model outputs after execution unless explicitly approved for publication;
- evidence session raw logs;
- operator notes containing platform-specific issues until reviewed.

### Historical

Belongs on website:

- curated archive index after archive review;
- supersession notes where needed.

Remains GitHub/source-only or internal:

- personal notes;
- old drafts;
- duplicate DOCX files;
- ambiguous-license translations.

### Personal

Personal notes and translations should not be website content unless separately reviewed and approved.

### Future Blog

Optional. Blog posts must be derived public views and must link to source authorities. They must not introduce new claims or update process state.

## Scalability Review

Assumption: repository grows to 10 research projects, 3,000+ documents, multiple domains, public papers, external collaborators, and multiple AI agents.

### Scalability Risks

- A single Project page will not scale; it needs project-scope filtering.
- Search must be manifest-driven, not filesystem-driven.
- Archive must become a separate governed collection with its own manifest.
- Machine Access must support stable document IDs and API pagination.
- Review Portal must support multiple review campaigns without mixing their evidence.
- Publications need citation and licensing metadata before public exposure.
- Website pages must not become a second state authority.

### Revised Scalable IA

The IA still scales if these constraints are adopted:

- Projects become a manifest-driven project registry.
- Each project gets its own status, evidence, review, and governance sub-tree.
- Machine Access supports filters and API endpoints.
- Archive is manifest-backed.
- Review Portal is campaign-based.
- Publications are curated records, not scanned repository files.

### Future Multi-Project Pattern

```text
Projects
├─ Ship Health Monitoring
│  ├─ Status
│  ├─ Evidence Package
│  ├─ Reviews
│  └─ Governance
├─ Future Project 2
│  ├─ Status
│  ├─ Evidence Package
│  ├─ Reviews
│  └─ Governance
```

## Risks

Priority 1:

- Website copy could strengthen claims beyond frozen authorities.
- Site generator could accidentally publish archive or internal material.
- Machine agents could retrieve execution copies as if they were source authorities.

Priority 2:

- Status drift if website pages store state instead of deriving from SYSTEM_STATE.
- Review Portal confusion between Deep Research and External Validation.
- Search over full repository could surface stale historical notes.

Priority 3:

- Future project growth could overload navigation.
- APIs could expose too much without visibility filtering.
- Archive pages could be mistaken for current project content.

## Recommendations

1. Build the website from `public_manifest.json` by default.
2. Treat all website pages as `WEBSITE_DERIVATIVE` records when they are later implemented.
3. Add a build-time check that prohibits publishing INTERNAL, ARCHIVE_ONLY, or REVIEW_PACKAGE_ONLY documents unless explicitly overridden.
4. Put Current Status behind a single data source derived from SYSTEM_STATE and manifests.
5. Keep Machine Access as a first-class nav item.
6. Keep Review Portal separate from Research pages.
7. Add badges for authority level, lifecycle state, copy role, and public visibility on document pages.
8. Do not implement full-text search over the whole repository until archive and licensing classifications are complete.

## Architecture Diagram

```text
Repository Governance Layer
  ├─ SYSTEM_STATE.md
  ├─ PUBLISHING_STATUS.md
  ├─ repository_manifest.json
  ├─ public_manifest.json
  └─ machine_retrieval_manifest.json
        ↓
Website Source Selection
  ├─ public pages from PUBLIC / PUBLIC_WITH_BOUNDARIES
  ├─ machine pages from manifest metadata
  └─ review pages from delivery-interface records
        ↓
jqhe.uk Public Portal
  ├─ Home / Current Status
  ├─ Research / Projects
  ├─ Review Portal
  ├─ Machine Access
  └─ Governance / Archive
        ↓
Audiences
  ├─ Public visitors
  ├─ Technical collaborators
  ├─ External reviewers
  └─ AI agents
```

## Final Recommendation

WEBSITE_ARCHITECTURE_READY

Justification: the proposed architecture is fully derivable from the repository governance layer, preserves source authority boundaries, separates public summaries from review and machine interfaces, and can scale to multiple projects if future implementation remains manifest-driven.
