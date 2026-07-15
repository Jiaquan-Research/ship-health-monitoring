# Website Implementation Record v0.1

Document status: Implementation record
Task ID: PHASE_5B_JQHE_UK_ASTRO_WEBSITE_IMPLEMENTATION_V0_1

## Implementation Scope

Implemented a static Astro v0.1 public research portal under `website/`.

The website is a derived publication layer. It does not modify scientific conclusions, validation evidence, frozen artifacts, research claims, review outputs, claims, gaps, or repository process state.

## Routes

- `/`
- `/status`
- `/research`
- `/projects`
- `/projects/ship-health-monitoring`
- `/projects/ship-health-monitoring/marine-package`
- `/projects/ship-health-monitoring/boundaries`
- `/projects/ship-health-monitoring/framework`
- `/projects/ship-health-monitoring/validation`
- `/projects/ship-health-monitoring/external-validation`
- `/projects/ship-health-monitoring/deep-research`
- `/review`
- `/review/deep-research`
- `/review/external-validation`
- `/machine`
- `/machine/manifest`
- `/machine/public-manifest`
- `/machine/retrieval-manifest`
- `/machine/governance`
- `/governance`
- `/about`
- `/404`
- `/sitemap.xml`

## Source Mappings

Public pages use `manifest/public_manifest.json` by default through copied files in `website/public/manifests/`.

Machine Access pages expose:

- `/manifests/public_manifest.json`
- `/manifests/machine_retrieval_manifest.json`
- `/manifests/repository_manifest.json`

## Design Decisions

- Static Astro output only.
- No backend, database, authentication, analytics, CMS, or external API.
- Restrained engineering/research visual style.
- Authority, lifecycle, copy-role, and visibility badges exposed on source lists.
- Review Portal separated from Research pages.
- Machine Access is a first-class section.

## Known Limitations

- No full-text search in v0.1.
- No Publications or Archive content beyond navigation concept in architecture.
- No local browser visual QA was required by the task; build verification is the primary check.
- Manifest copies must be refreshed manually or by a future script when repository manifests change.

## Build Verification

Commands executed:

```text
cd website
npm install
npm run validate
npm run build
```

Observed result:

- `npm install --cache .npm-cache`: completed.
- `npm run validate`: Publication validation PASS.
- `npm run build`: completed; 22 pages built.

Note: `npm install` through the default PowerShell shim was blocked by local execution policy, and the default npm cache path was not writable from this sandbox. Installation succeeded with `npm.cmd install --cache .npm-cache`.

## Deployment Readiness

Cloudflare Pages settings are documented in `website/README.md`.

Deployment, domain binding, and Cloudflare configuration are not performed in this task.

## Authority Boundary

Website pages are derived views. They are not scientific evidence, review results, process-state authorities, or governance authorities.

## Deployment-Preparation Amendment

Task: jqhe.uk Website v0.1 deployment preparation.

Changes applied:

- Corrected website source links to `https://github.com/Jiaquan-Research/ship-health-monitoring`.
- Added automatic manifest synchronization through `website/scripts/sync-manifests.mjs`.
- Updated `npm run validate` so manifest synchronization runs before publication validation.
- Strengthened publication validation for cross-manifest consistency, visibility boundaries, generated-copy authority boundaries, source URL correctness, duplicate IDs/paths, and copied-manifest hash equality.
- Updated `.gitignore` to exclude website install/build/cache artifacts and environment files while preserving source files and lockfiles.

Final local verification for deployment preparation is recorded in the deployment-preparation task report. Cloudflare deployment and domain binding remain not started.

## Deployment-Preparation Verification

Commands executed in the clean `website-deploy-v0.1` worktree:

```text
python scripts/repository_governance/validate_manifest.py
python scripts/repository_governance/check_state_consistency.py
python scripts/repository_governance/check_links.py
cd website
npm.cmd install --cache .npm-cache
npm.cmd run sync-manifests
npm.cmd run validate
npm.cmd run build
npm.cmd audit --json
```

Observed results:

- Repository manifest validation: PASS.
- State consistency check: PASS.
- Link check: PASS.
- Manifest synchronization: PASS.
- Publication validation: PASS.
- Astro static build: PASS; 22 pages built.
- Generated manifest files present under `website/dist/manifests/`.
- Generated HTML uses `https://github.com/Jiaquan-Research/ship-health-monitoring`.
- No generated HTML occurrence of `https://github.com/jqhe/ship-health-monitoring` was found.

Manifest synchronization hashes observed:

```text
repository_manifest.json BE6B0F0490CC56FDC7FA80D1100050A450E936334DBA5F5DC0DC3BD0EB22EC5F
public_manifest.json 6A7DC6A46826C3666197543158F0E4F20EDDEAB6D01856A2A794BE1F49ED2FB2
machine_retrieval_manifest.json DE3A9D5115DF59FA54DC76FD2C741CD6B9A6F244B2811D265B667F91B5E3EC81
```

Dependency audit classification:

- Total vulnerabilities: 3 package findings.
- Severity summary: 1 moderate, 2 high.
- Affected packages: `astro` direct production/build dependency; transitive `vite` and `esbuild`.
- Available npm fix: Astro `7.0.9`, semver-major.
- Action taken: no automatic fix applied because the available fix requires a major framework upgrade.

Visual browser QA remains pending for a future Cloudflare preview deployment.
