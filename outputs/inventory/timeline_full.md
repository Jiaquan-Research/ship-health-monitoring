# Full Timeline Reconstruction

Source command:

`git log --all --pretty=format:"%H|%ad|%s" --date=iso`

## Chronological Commit Table

| Date | Commit hash (short) | Line | Outcome | Message |
| --- | --- | --- | --- | --- |
| 2026-06-03 21:21:21 +0900 | 68dcb4d | Engineering | PASS | feat: validation-b1 expected-state and residual baseline |
| 2026-06-03 21:32:56 +0900 | 2b05b6c | Engineering | FAIL | feat: validation-b2 residual severity analysis |
| 2026-06-03 22:04:14 +0900 | 9a1392a | Engineering | Strong PASS | feat: validation-b21 corrected severity ordering |
| 2026-06-03 22:12:43 +0900 | a545b73 | Engineering | Design | docs: freeze validation chain v0.1 |
| 2026-06-03 22:19:10 +0900 | de87b63 | Engineering | Design | docs: update concept paper v0.4 status |
| 2026-06-04 20:55:41 +0900 | 3b20300 | Engineering | Design | docs: hi_v0 design document v0.1 |
| 2026-06-04 20:56:52 +0900 | 128d4f7 | Engineering | Design | docs: add concept paper v0.4 docx |
| 2026-06-04 20:59:39 +0900 | b9b29df | Engineering | N/A | docs: clarify hi_v0 validation comparison |
| 2026-06-04 21:07:31 +0900 | c7442a9 | Engineering | PASS | feat: hi-v0 rolling-rms validation |
| 2026-06-05 19:23:40 +0900 | aa2f385 | Engineering | Design | docs: concept-paper-v0.6 and marine-data-req-v0.3 |
| 2026-06-05 20:09:37 +0900 | 0fa0474 | Engineering | Strong PASS | feat: validation-b4 residual-trend-audit |
| 2026-06-05 20:42:58 +0900 | 451bb52 | Review | Design | docs: concept-paper-v0.6 evidence-boundary and tighten claims |
| 2026-06-05 23:03:50 +0900 | 0aede63 | Engineering | Audit | data: n-cmapss download and audit |
| 2026-06-05 23:13:47 +0900 | 35c2673 | Review | Design | docs: concept-paper-v0.7 tighten claims and clarify architecture |
| 2026-06-06 12:10:26 +0900 | 83d37f3 | Engineering | Design | docs: baseline-management-v0.1 frozen with 6 enhancements |
| 2026-06-06 12:46:53 +0900 | 5316cc2 | Engineering | N/A | feat: validation-c0-ncmapss-surrogate-spike |
| 2026-06-06 13:10:05 +0900 | 727f780 | Engineering | Audit | feat: validation-c01-label-audit |
| 2026-06-06 13:31:00 +0900 | a0a2c52 | Engineering | Strong PASS | feat: validation-c02-groundtruth-aligned-rerun |
| 2026-06-06 13:50:17 +0900 | cdd0ecf | Engineering | N/A | docs: update project state after validation-c0-series |
| 2026-06-06 14:10:33 +0900 | 79b8731 | Engineering | Design | docs: freeze validation-c0-series findings |
| 2026-06-06 14:32:29 +0900 | dd91926 | Engineering | Design | docs: baseline-management-v0.2 event-detection-heuristics-and-quality-levels |
| 2026-06-06 15:11:57 +0900 | fda3e3a | Engineering | Design | docs: validation-d-protocol-v0.1 marine-generator |
| 2026-06-09 21:41:25 +0900 | 52c5036 | Review | N/A | docs: claim-registry-v0.1 add alternative-explanations and priority section |
| 2026-06-09 21:51:02 +0900 | 7c6afa5 | Infrastructure | N/A | chore: organize repository before first public push |
| 2026-06-09 21:56:20 +0900 | 91e7d1b | Review | Design | docs: add deep research attack protocol v0.1 |
| 2026-06-09 22:42:42 +0900 | 21e6c96 | Review | Audit | docs: incorporate attack review round1 findings |
| 2026-06-09 22:48:45 +0900 | 0bedede | Infrastructure | N/A | chore: remove large residual exports from repository |
| 2026-06-09 22:51:49 +0900 | d6f7a4a | Review | Design | docs: add falsification protocol v0.1 |
| 2026-06-09 22:56:41 +0900 | da6b5b5 | Review | Design | docs: add falsification protocol v0.1 |
| 2026-06-09 23:02:07 +0900 | deec80c | Review | Audit | docs: add independent review checklist v0.1 |
| 2026-06-09 23:06:18 +0900 | bbc1c83 | Review | Audit | docs: enhance independent review checklist |
| 2026-06-10 12:41:55 +0900 | e931efc | Review | Audit | docs: add review package github audit |
| 2026-06-10 12:44:14 +0900 | a8a4814 | Review | Audit | docs: add attack review round2 |
| 2026-06-10 12:46:21 +0900 | b769403 | Engineering | Design | docs: publish concept paper v0.7 |
| 2026-06-10 20:17:55 +0900 | 64fe225 | Review | Audit | docs: add attack review summary v1 |
| 2026-06-10 20:20:18 +0900 | 9ba1f16 | Review | Audit | docs: attack-review-summary add simulation-limitation and negative-control description |
| 2026-06-10 20:26:43 +0900 | d1a442a | Review | Design | docs: add negative control protocol v0.1 |
| 2026-06-10 20:36:27 +0900 | 6420a58 | Review | FAIL | feat: validation-i1 negative control |
| 2026-06-10 20:46:11 +0900 | 3fea729 | Review | FAIL | docs: add validation-i1 postmortem |
| 2026-06-10 20:56:07 +0900 | 8346380 | Review | Design | docs: add m1 condition leakage protocol v0.1 |
| 2026-06-10 21:02:52 +0900 | da213c1 | Review | FAIL | feat: validation-m1 condition leakage audit |
| 2026-06-10 21:19:26 +0900 | f7de0ab | Review | Audit | docs: add validation-m1 postmortem |
| 2026-06-10 21:26:28 +0900 | f42f903 | Review | Audit | docs: add m1a type separation protocol v0.1 |
| 2026-06-10 21:38:31 +0900 | bc08332 | Review | Audit | feat: validation-m1a type separation |
| 2026-06-10 21:52:34 +0900 | 5a2cf05 | Exploration | N/A | explore: e1 cross regime probe |
| 2026-06-10 22:10:10 +0900 | a0ba681 | Unclear | Audit | docs: add battery dataset inventory |
| 2026-06-10 23:49:09 +0900 | a6fd9cb | Unclear | Audit | docs: add industrial dataset zoo inventory |
| 2026-06-11 20:30:35 +0900 | 279805e | Unclear | N/A | docs: add mode conditioned structure research note |
| 2026-06-11 20:33:17 +0900 | 17fe7b7 | Review | Audit | docs: update attack review summary with internal validations |
| 2026-06-11 20:34:34 +0900 | 515d14c | Exploration | Design | docs: add exploration sandbox readme |
| 2026-06-11 20:43:07 +0900 | 9571808 | Review | Audit | docs: attack-review-summary update section-9 post-i1-m1-execution |
| 2026-06-11 20:47:59 +0900 | 6ec812f | Exploration | Design | docs: add q0 global vs piecewise question ledger |
| 2026-06-11 20:55:00 +0900 | 3af5f99 | Exploration | Design | docs: add industrial dataset zoo observation ledger |
| 2026-06-11 21:03:33 +0900 | aec9a41 | Exploration | Design | docs: add method zoo observation ledger |
| 2026-06-11 21:11:38 +0900 | d3dfc68 | Exploration | Audit | docs: add dataset audit protocol v0.1 |
| 2026-06-11 21:17:29 +0900 | 3e62c92 | Exploration | Audit | docs: add dataset census round1 |
| 2026-06-11 21:28:27 +0900 | 951b60a | Exploration | Design | docs: add experiment zoo observation ledger |
| 2026-06-11 21:33:25 +0900 | d4d7911 | Exploration | Design | docs: add question zoo observation ledger |
| 2026-06-11 21:40:49 +0900 | 015e90f | Exploration | Design | docs: add e2 battery cross regime probe protocol |
| 2026-06-11 21:48:53 +0900 | cd3277b | Exploration | N/A | explore: e2 battery cross regime probe |
| 2026-06-11 22:05:44 +0900 | a5c2597 | Exploration | Audit | docs: add battery dataset context audit |
| 2026-06-11 22:09:48 +0900 | 26aed21 | Exploration | Audit | docs: add e2 postmortem and context audit notes |
| 2026-06-11 22:17:38 +0900 | f0f7b39 | Exploration | Design | docs: add condition normalization notes |
| 2026-06-15 21:19:02 +0900 | 108491b | Exploration | Audit | explore: tighten residual-health-notes per review |
| 2026-06-15 21:33:30 +0900 | df59ed7 | Exploration | Audit | explore: battery dataset context audit (p0) |
| 2026-06-15 21:47:43 +0900 | 31624e2 | Exploration | Audit | explore: exploration review week 1 |
| 2026-06-15 21:48:54 +0900 | 65b644e | Exploration | Audit | explore: tighten exploration-review-week1 per review |
| 2026-06-15 22:57:59 +0900 | 4f8e71c | Exploration | Design | docs: integrate regime vocabulary deep research |

## Classification Flags

### Commits not confidently classified

- `a0ba681` docs: add battery dataset inventory
- `a6fd9cb` docs: add industrial dataset zoo inventory
- `279805e` docs: add mode conditioned structure research note

### Timeline / consistency flags

- Duplicate-looking commits for `docs: add falsification protocol v0.1` appear consecutively on 2026-06-09; both touch `docs/review/falsification_protocol_v0.1.md`.
- Commit `7c6afa5` is classified Infrastructure by message but is mixed-purpose: it organizes review/design outputs and adds B3A/B4 source scripts.
- Historical commits `docs: add battery dataset inventory` and `docs: add industrial dataset zoo inventory` refer to `docs/data/...`, but those files are not present in the current working tree; likely superseded by `docs/exploration/dataset_*` inventory.
- No sequence inversion was detected for I-1 -> M-1 -> M-1A -> E-1 -> E-2 -> Battery Context Audit in commit order.
