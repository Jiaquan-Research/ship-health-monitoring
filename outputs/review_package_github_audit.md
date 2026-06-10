# Review Package GitHub Audit

Date: 2026-06-10

Repository:

https://github.com/Jiaquan-Research/ship-health-monitoring

## Summary

Current branch: `master`

Latest local commit at review-package verification: `bbc1c83bcf0363b8694fd57253026473d4ad04f7`

Latest remote commit at review-package verification: `bbc1c83bcf0363b8694fd57253026473d4ad04f7`

Push needed for review-package files: No. `git push origin master:main` returned `Everything up-to-date`.

Remote verification method:

* `git fetch origin main`
* `git ls-tree -r origin/main --name-only docs/review docs/frozen docs/concept docs/design`

## File Audit

| File | Local Exists | Local Size | Last Modified | Git Tracked | Remote Exists | Required/Optional |
|---|---:|---:|---|---:|---:|---|
| docs/review/claim_registry_v0.1.md | Yes | 2826 bytes | 2026-06-09 22:41:26 | Yes | Yes | Required |
| docs/review/attack_review_round1.md | Yes | 723 bytes | 2026-06-09 22:41:26 | Yes | Yes | Required |
| docs/review/attack_review_round2.md | No | N/A | N/A | No | No | Required |
| docs/review/falsification_protocol_v0.1.md | Yes | 4310 bytes | 2026-06-09 22:56:23 | Yes | Yes | Required |
| docs/review/independent_review_checklist_v0.1.md | Yes | 3645 bytes | 2026-06-09 23:05:52 | Yes | Yes | Required |
| docs/frozen/validation_c0_series.md | Yes | 2635 bytes | 2026-06-06 14:10:12 | Yes | Yes | Required |
| docs/concept/concept_paper_v0.7.md | No | N/A | N/A | No | No | Required |
| docs/review/deep_research_attack_protocol_v0.1.md | Yes | 2815 bytes | 2026-06-09 21:56:09 | Yes | Yes | Optional |
| docs/design/baseline_management_v0.2.md | Yes | 27127 bytes | 2026-06-06 14:31:48 | Yes | Yes | Optional |
| docs/design/validation_d_protocol_v0.1.md | Yes | 8108 bytes | 2026-06-06 15:11:43 | Yes | Yes | Optional |

## Missing Files

Required files missing locally and remotely:

* `docs/review/attack_review_round2.md`
* `docs/concept/concept_paper_v0.7.md`

## Notes

All existing required and optional review-package files are tracked by Git and present on `origin/main`.

No missing existing file had to be added.

No experiment outputs were modified or rerun.
