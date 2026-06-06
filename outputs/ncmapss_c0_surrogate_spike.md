# Validation C0 — N-CMAPSS Surrogate Spike

**Scope:** Surrogate — segment mechanics only. Not maintenance-event evidence. Not Q4b evidence.

## Section 1 — Scope Disclaimer

**Surrogate — segment mechanics only. Not maintenance-event evidence. Not Q4b evidence.**

N-CMAPSS contains no real maintenance events. Artificial lifecycle zones are imposed only to test Expected State, Residual, HI, and segment-aware processing mechanics.

## Section 2 — Variable Mapping

- Dataset: `data/ncmapss/data_set/N-CMAPSS_DS02-006.h5`
- Split: dev only (`A_dev`, `W_dev`, `X_s_dev`, `Y_dev`, `T_dev`).
- Condition Variables: alt, Mach, TRA, T2
- State Variables: primary `T30`, secondary `T24`, `Wf`.
- Ground truth degradation: `HPC_eff_mod`; more negative means more degraded.

Array shapes:
- `A_dev`: (5263447, 4)
- `W_dev`: (5263447, 4)
- `X_s_dev`: (5263447, 14)
- `Y_dev`: (5263447, 1)
- `T_dev`: (5263447, 10)

Variable names:
- `A_var`: unit, cycle, Fc, hs
- `W_var`: alt, Mach, TRA, T2
- `X_s_var`: T24, T30, T48, T50, P15, P2, P21, P24, Ps30, P40, P50, Nf, Nc, Wf
- `T_var`: fan_eff_mod, fan_flow_mod, LPC_eff_mod, LPC_flow_mod, HPC_eff_mod, HPC_flow_mod, HPT_eff_mod, HPT_flow_mod, LPT_eff_mod, LPT_flow_mod

Unique units: 6
Cycles per unit: min=63, median=73.0, max=89

| Unit | Cycle Count | Selection Reason |
| --- | --- | --- |
| 5 | 89 | Longest lifecycle unit |
| 2 | 75 | Median lifecycle unit |
| 16 | 63 | Shortest lifecycle unit |

Artificial lifecycle zones:
| Unit | Zone A | Zone T | Zone B |
| --- | --- | --- | --- |
| 5 | 1-17 (17 cycles) | 18-72 (55 cycles) | 73-89 (17 cycles) |
| 2 | 1-15 (15 cycles) | 16-60 (45 cycles) | 61-75 (15 cycles) |
| 16 | 1-12 (12 cycles) | 13-51 (39 cycles) | 52-63 (12 cycles) |

## Section 3 — Expected State Model Results (B1 Analog)

| Unit | Target | Train R2 | Held-out R2 |
| --- | --- | --- | --- |
| 5 | T30 | 1.000 | 0.995 |
| 5 | T24 | 1.000 | 0.992 |
| 5 | Wf | 1.000 | 0.996 |
| 2 | T30 | 1.000 | 0.995 |
| 2 | T24 | 1.000 | 0.994 |
| 2 | Wf | 1.000 | 0.998 |
| 16 | T30 | 1.000 | 0.995 |
| 16 | T24 | 1.000 | 0.997 |
| 16 | Wf | 1.000 | 0.998 |

Primary verdict is based on `T30`; `T24` and `Wf` are supporting evidence.

## Section 4 — Residual Zone Comparison (A vs B)

| Unit | Target | RMS_A | RMS_B | Ratio B/A |
| --- | --- | --- | --- | --- |
| 5 | T30 | 1.748 | 4.247 | 2.429 |
| 5 | T24 | 0.718 | 1.339 | 1.866 |
| 5 | Wf | 0.016 | 0.046 | 2.820 |
| 2 | T30 | 1.749 | 4.667 | 2.668 |
| 2 | T24 | 0.622 | 1.021 | 1.642 |
| 2 | Wf | 0.013 | 0.040 | 2.973 |
| 16 | T30 | 2.037 | 4.715 | 2.315 |
| 16 | T24 | 0.524 | 1.501 | 2.866 |
| 16 | Wf | 0.014 | 0.045 | 3.109 |

Success criterion: Zone B RMS > Zone A RMS for all selected units, primary evaluation using T30.

## Section 5 — Ground Truth Correlation

Ground truth degradation variable availability:
| Unit | HPC_eff_mod Min | HPC_eff_mod Max | HPC_eff_mod Std |
| --- | --- | --- | --- |
| 5.0 | 0.000 | 0.000 | 0.000 |
| 2.0 | 0.000 | 0.000 | 0.000 |
| 16.0 | 0.000 | 0.000 | 0.000 |

| Unit | Residual Spearman | Residual_norm Spearman |
| --- | --- | --- |
| 5.0 | nan | nan |
| 2.0 | nan | nan |
| 16.0 | nan | nan |

Important limitation: `HPC_eff_mod` is constant at 0.0 for the selected DS02 dev units. Spearman correlation is therefore undefined (`nan`). This spike keeps the frozen C0 mapping but cannot use `HPC_eff_mod` as ground-truth degradation evidence for DS02.

## Section 6 — Early Detection Audit

T30 residual RMS by lifecycle third:
| Unit | Early | Mid | Late |
| --- | --- | --- | --- |
| 2.0 | 2.147 | 3.132 | 4.119 |
| 5.0 | 1.695 | 3.156 | 3.582 |
| 16.0 | 2.435 | 3.739 | 4.150 |

Mean HPC_eff_mod by lifecycle third:
| Unit | Early | Mid | Late |
| --- | --- | --- | --- |
| 2.0 | 0.000 | 0.000 | 0.000 |
| 5.0 | 0.000 | 0.000 | 0.000 |
| 16.0 | 0.000 | 0.000 | 0.000 |

First cycle where T30 residual RMS exceeds 1.5 x Early RMS:
| Unit | First Detection Cycle |
| --- | --- |
| 5 | 16 |
| 2 | 13 |
| 16 | 10 |

## Section 7 — HI_v0 Window Comparison

| Unit | Window | HI_A | HI_B | Ratio | Spearman |
| --- | --- | --- | --- | --- | --- |
| 5.0 | 5.0 | 0.594 | 2.221 | 3.738 | nan |
| 5.0 | 10.0 | 0.566 | 2.085 | 3.681 | nan |
| 5.0 | 20.0 | 0.576 | 1.976 | 3.432 | nan |
| 2.0 | 5.0 | 0.718 | 2.398 | 3.341 | nan |
| 2.0 | 10.0 | 0.674 | 2.443 | 3.622 | nan |
| 2.0 | 20.0 | 0.741 | 2.432 | 3.283 | nan |
| 16.0 | 5.0 | 0.683 | 2.295 | 3.358 | nan |
| 16.0 | 10.0 | 0.649 | 2.090 | 3.221 | nan |
| 16.0 | 20.0 | 0.962 | 1.992 | 2.070 | nan |

Best overall window by combined Spearman and separation score: `10` cycles.

Best window per unit:
| Unit | Window | Ratio | Spearman |
| --- | --- | --- | --- |
| 5.0 | 5.0 | 3.738 | nan |
| 2.0 | 10.0 | 3.622 | nan |
| 16.0 | 5.0 | 3.358 | nan |

## Section 8 — Interpretation

**Q1: Does Expected State transfer?** Held-out `T30` R2 minimum across selected units is 0.995. This supports transfer mechanics if the threshold is met.

**Q2: Does Residual → HI transfer?** `T30` Zone B/A residual RMS minimum ratio is 2.315; HI_v0 windows also produce Zone separation where Ratio > 1.

**Q3: Does segment-aware pipeline run end-to-end?** Yes. The spike loads unit/cycle metadata, imposes artificial Zone A/T/B segments, trains Zone A models, computes residuals, computes HI_v0 by cycle, and reports segment-aware comparisons.

**Q4: How early can degradation be detected?** Detection timing is reported as the first cycle where cycle-level T30 residual RMS exceeds 1.5 x Early RMS. This is a surrogate residual-deviation marker, not a maintenance alarm. Because `HPC_eff_mod` is constant in DS02 dev, this cannot be interpreted as confirmed HPC degradation onset.

## Section 9 — Boundary Statement

Validated:
- Expected State transfer mechanics
- Residual generation mechanics
- HI_v0 behavior
- Segment-aware processing

Not Validated:
- Maintenance events
- Baseline reset semantics
- Q4b
- Marine transfer

## Section 10 — Verdict

**Verdict: Weak Evidence.**

Justification: primary T30 held-out R2 minimum=0.995, T30 residual RMS B/A minimum=2.315, max |residual vs HPC_eff_mod Spearman|=undefined because HPC_eff_mod is constant in DS02 dev. Expected State, residual, HI, and segment mechanics run end-to-end, but ground-truth degradation correlation cannot be established with the requested DS02/HPC_eff_mod pairing.
