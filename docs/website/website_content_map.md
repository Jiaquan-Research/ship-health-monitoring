# Website Content Map

Document status: Website planning map
Task ID: MANIFEST_FIRST_REPOSITORY_GOVERNANCE_IMPLEMENTATION
Target site: jqhe.uk

## Purpose

This map defines a proposed website information architecture. It does not implement the website and does not modify repository evidence, frozen artifacts, claims, gaps, or process states.

The website must use manifest-selected content. It must not scan and publish the entire repository automatically.

## Proposed Pages

| page | purpose | target audience | source documents | authority status | allowed claims | prohibited claims | public visibility | update trigger | facing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home | Introduce the project and boundaries | Public | `README.md`; `PUBLISHING_STATUS.md`; `SYSTEM_STATE.md` | Derived public view | Current project is evidence-boundary research; Marine validity not claimed | Marine validity, deployment readiness, External Validation completion | PUBLIC_WITH_BOUNDARIES | State or publishing-status change | Human-facing |
| Current Status | Show current process state | Public; reviewers; agents | `SYSTEM_STATE.md`; `PUBLISHING_STATUS.md` | Derived from repository state authority | Package frozen; External Validation not started; Blind Review not started | Any advanced process state not recorded in SYSTEM_STATE | PUBLIC_WITH_BOUNDARIES | SYSTEM_STATE update | Human- and machine-facing |
| Research | Describe research motivation and method families | Public; reviewers | `docs/marine_package_v1/marine_package_v1.md`; Health Evidence Framework | Derived summary | Public-data evidence supports bounded technical learning | Marine feasibility or operational performance | PUBLIC_WITH_BOUNDARIES | Package or framework update | Human-facing |
| Projects | Route to project-specific pages | Public | `manifest/repository_manifest.json`; `docs/documentation_map.md` | Navigation view | Current project scope and available packages | New project claims without manifest entries | PUBLIC | Manifest update | Human-facing |
| Ship Health Monitoring | Project landing page | Public; collaborators | `README.md`; `docs/marine_package_v1/marine_package_v1.md` | Derived public view | Current ship health monitoring evidence boundary | Product readiness | PUBLIC_WITH_BOUNDARIES | Marine Package or SYSTEM_STATE update | Human-facing |
| Marine Package | Present Marine Package v1.0 | Reviewers; collaborators | `docs/marine_package_v1/marine_package_v1.md`; gap register; artifact index | Scope authority excerpt/view | Marine Package is frozen with documented gaps | Gap closure or Marine validity | PUBLIC_WITH_BOUNDARIES | New Marine Package version | Reviewer-facing |
| Evidence and Claim Boundaries | Explain claims, gaps, and boundaries | Reviewers; agents | claim boundary; evidence map; gap register | Derived from scope authorities | Frozen claims and active gaps as recorded | Stronger claims than frozen package permits | PUBLIC_WITH_BOUNDARIES | Claim/gap authorized change | Reviewer- and machine-facing |
| Framework Architecture | Present framework architecture | Technical readers | Health Evidence Framework; DD documents | Architecture and decision sources | Framework architecture and terminology | Deployment approval or Marine validation | PUBLIC_WITH_BOUNDARIES | Framework decision update | Human-facing |
| Public Dataset Validation | Route to public-data evidence | Reviewers | Marine Package; validation closure records; Transport v2 evidence index | Derived evidence navigation | Public-data evidence roles and limitations | Unified benchmark or Marine transfer proof | PUBLIC_WITH_BOUNDARIES | Evidence package update | Reviewer-facing |
| External Validation | Explain definition and status | External reviewers; collaborators | External Validation specification; approval/freeze record | Scope authority view | Definition approved/frozen; execution not started | Reviewer selected or validation completed | PUBLIC_WITH_BOUNDARIES | External Validation state change | Reviewer-facing |
| Deep Research Review | Explain Blind Review inputs | Operators; reviewers | Transport v2 guide; execution package README; Session Protocol | Delivery-interface view | Review package prepared; execution not started | Deep Research equals External Validation | PUBLIC_WITH_BOUNDARIES | Review execution state change | Reviewer-facing |
| Review Portal | Provide operator-facing upload instructions | Operators | execution package README; prompts; inventory | Execution interface | Upload profiles and prompts prepared | Review findings before execution | PUBLIC_WITH_BOUNDARIES | Execution-package update | Operator-facing |
| Machine Access | Provide manifest and retrieval guidance | Agents; developers | repository manifest; machine retrieval manifest; machine retrieval policy | Machine navigation view | Retrieval priority and authority hierarchy | Recency as authority | PUBLIC_WITH_BOUNDARIES | Manifest update | Machine-facing |
| Governance | Explain repository governance | Reviewers; collaborators | governance policies; repository reviews | Governance source view | Authority hierarchy and publication rules | Scientific conclusions beyond source records | PUBLIC_WITH_BOUNDARIES | Policy update | Human- and machine-facing |
| About | Describe project owner context and collaboration boundary | Public | README; Publishing Status | Derived public view | Collaboration-ready with boundaries | Commercial or deployment guarantee | PUBLIC_WITH_BOUNDARIES | Publishing-status update | Human-facing |
| Archive | Route historical materials selectively | Researchers | Documentation map; future archive manifest | Archive navigation | Historical context exists | Historical notes as current authority | ARCHIVE_ONLY by default | Archive-review task | Human-facing |

## Website Rules

- Website pages are derived views, not source authorities.
- Website content must be selected through the manifest.
- Website content must preserve Marine, External Validation, deployment, and Blind Review boundaries.
- Internal, archive-only, ambiguous-license, and review-package-only documents must not be published automatically.
