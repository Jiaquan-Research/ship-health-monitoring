# Validation C0.2 — Ground Truth Aligned Rerun

**Scope:** Surrogate only. Not maintenance-event evidence. Not Q4b evidence.

## 1. Scope Disclaimer

**Surrogate only. Not maintenance-event evidence. Not Q4b evidence.**

This rerun uses the C0.1 finding that DS02-006 contains active `HPT_eff_mod` degradation while `HPC_eff_mod` is zero. It remains a surrogate mechanics validation only.

## 2. Ground Truth Selection

- Primary degradation label: `HPT_eff_mod`
- Reason: C0.1 confirmed `HPT_eff_mod` is active across units 2, 5, 10, 16, 18, and 20, while `HPC_eff_mod = 0` for all units.
- HPT_eff_mod range: -0.018668 to 0.000021
- HPT_eff_mod mean: -0.003463
- HPT_eff_mod std: 0.003747

| Unit | Cycles | Reason |
| --- | --- | --- |
| 5 | 89 | Longest lifecycle |
| 2 | 75 | Median lifecycle |
| 16 | 63 | Shortest lifecycle |

Lifecycle zones:
| Unit | Zone A | Zone T | Zone B |
| --- | --- | --- | --- |
| 5 | 1-17 (17 cycles) | 18-72 (55 cycles) | 73-89 (17 cycles) |
| 2 | 1-15 (15 cycles) | 16-60 (45 cycles) | 61-75 (15 cycles) |
| 16 | 1-12 (12 cycles) | 13-51 (39 cycles) | 52-63 (12 cycles) |

## 3. Sensor Ranking

| Sensor | Spearman | AbsSpearman |
| --- | --- | --- |
| T50 | -0.128 | 0.128 |
| T48 | -0.091 | 0.091 |
| Nc | 0.023 | 0.023 |
| Wf | -0.023 | 0.023 |
| T24 | -0.015 | 0.015 |
| P24 | -0.010 | 0.010 |
| T30 | 0.008 | 0.008 |
| P15 | -0.007 | 0.007 |
| P21 | -0.007 | 0.007 |
| P50 | -0.006 | 0.006 |
| P2 | -0.006 | 0.006 |
| P40 | 0.003 | 0.003 |
| Ps30 | 0.002 | 0.002 |
| Nf | 0.001 | 0.001 |

Final target selection:
- Primary target: `T50` (highest-ranked preferred temperature sensor among T48/T50)
- Secondary target: `Nc` (highest-ranked flow/speed sensor excluding Wf when possible)
- Continuity target: `Wf`

## 4. Model Performance

| Unit | Target | Train R2 | Held-out R2 |
| --- | --- | --- | --- |
| 5 | T50 | 0.999 | 0.992 |
| 5 | Nc | 1.000 | 0.998 |
| 5 | Wf | 1.000 | 0.996 |
| 2 | T50 | 0.999 | 0.996 |
| 2 | Nc | 1.000 | 0.997 |
| 2 | Wf | 1.000 | 0.998 |
| 16 | T50 | 0.999 | 0.994 |
| 16 | Nc | 1.000 | 0.996 |
| 16 | Wf | 1.000 | 0.998 |

## 5. Residual Results

| Unit | Target | RMS_A | RMS_B | Ratio |
| --- | --- | --- | --- | --- |
| 5 | T50 | 2.116 | 19.625 | 9.273 |
| 5 | Nc | 4.194 | 20.054 | 4.782 |
| 5 | Wf | 0.016 | 0.046 | 2.820 |
| 2 | T50 | 1.949 | 19.786 | 10.150 |
| 2 | Nc | 5.060 | 20.794 | 4.109 |
| 2 | Wf | 0.013 | 0.040 | 2.973 |
| 16 | T50 | 2.140 | 18.191 | 8.499 |
| 16 | Nc | 6.143 | 21.535 | 3.506 |
| 16 | Wf | 0.014 | 0.045 | 3.109 |

## 6. Ground Truth Correlation

| Unit | Target | Spearman | AbsSpearman |
| --- | --- | --- | --- |
| 5 | T50 | -0.783 | 0.783 |
| 5 | Nc | 0.596 | 0.596 |
| 5 | Wf | -0.299 | 0.299 |
| 2 | T50 | -0.826 | 0.826 |
| 2 | Nc | 0.560 | 0.560 |
| 2 | Wf | -0.386 | 0.386 |
| 16 | T50 | -0.772 | 0.772 |
| 16 | Nc | 0.560 | 0.560 |
| 16 | Wf | -0.292 | 0.292 |

Note: `HPT_eff_mod` is negative when degraded. Negative Spearman indicates residual tends to increase as degradation becomes more negative.

## 7. HI_v0 Results

| Unit | Target | Window | HI Ratio | Spearman | AbsSpearman |
| --- | --- | --- | --- | --- | --- |
| 5 | T50 | 5 | 12.263 | -0.951 | 0.951 |
| 5 | T50 | 10 | 11.456 | -0.964 | 0.964 |
| 5 | T50 | 20 | 9.127 | -0.986 | 0.986 |
| 5 | Nc | 5 | 5.654 | -0.919 | 0.919 |
| 5 | Nc | 10 | 5.390 | -0.964 | 0.964 |
| 5 | Nc | 20 | 4.779 | -0.981 | 0.981 |
| 5 | Wf | 5 | 4.573 | -0.679 | 0.679 |
| 5 | Wf | 10 | 4.393 | -0.672 | 0.672 |
| 5 | Wf | 20 | 3.788 | -0.572 | 0.572 |
| 2 | T50 | 5 | 10.042 | -0.961 | 0.961 |
| 2 | T50 | 10 | 9.392 | -0.978 | 0.978 |
| 2 | T50 | 20 | 7.297 | -0.994 | 0.994 |
| 2 | Nc | 5 | 4.852 | -0.821 | 0.821 |
| 2 | Nc | 10 | 4.846 | -0.889 | 0.889 |
| 2 | Nc | 20 | 4.134 | -0.930 | 0.930 |
| 2 | Wf | 5 | 3.415 | -0.651 | 0.651 |
| 2 | Wf | 10 | 3.588 | -0.618 | 0.618 |
| 2 | Wf | 20 | 3.370 | -0.830 | 0.830 |
| 16 | T50 | 5 | 9.426 | -0.938 | 0.938 |
| 16 | T50 | 10 | 8.616 | -0.972 | 0.972 |
| 16 | T50 | 20 | 5.148 | -0.979 | 0.979 |
| 16 | Nc | 5 | 4.699 | -0.828 | 0.828 |
| 16 | Nc | 10 | 4.432 | -0.848 | 0.848 |
| 16 | Nc | 20 | 2.689 | -0.900 | 0.900 |
| 16 | Wf | 5 | 4.249 | -0.708 | 0.708 |
| 16 | Wf | 10 | 4.243 | -0.793 | 0.793 |
| 16 | Wf | 20 | 3.001 | -0.912 | 0.912 |

Best target/window: `T50`, W=5 cycles.

## 8. Early Detection

| Unit | Detection Cycle | Lifecycle % | Threshold |
| --- | --- | --- | --- |
| 5.0 | 18.0 | 20.225 | 1.611 |
| 2.0 | 22.0 | 29.333 | 1.720 |
| 16.0 | 13.0 | 20.635 | 1.891 |

## 9. Interpretation

**Q1: Does residual track actual degradation?**
Best residual |Spearman| = 0.826. Alignment with `HPT_eff_mod` provides a real, non-constant degradation label unlike C0.

**Q2: Does HI track actual degradation?**
Best HI |Spearman| = 0.994, with best HI Ratio = 12.263.

**Q3: Does alignment improve over C0?**
Yes. C0 ground-truth correlation was undefined (`HPC_eff_mod` constant zero); C0.2 obtains finite correlations against active `HPT_eff_mod`.

**Q4: What is the best sensor for degradation monitoring?**
`T50` is the best target in this rerun based on HI separation and Spearman score. Sensor ranking should be consulted for domain interpretation.

**Q5: How early can degradation be detected?**
Detection cycles are reported using the best target/window and threshold `HI_v0 > 1.5 x Early-Life HI`. This is a surrogate detectability marker, not an operational alarm.

## 10. Verdict

**Verdict: Strong PASS.**

Justification: C0.2 corrects the C0 ground-truth mismatch by using active `HPT_eff_mod`. Minimum held-out R2=0.992; maximum residual |Spearman|=0.826; maximum HI |Spearman|=0.994; maximum HI Ratio=12.263.

Compared with Validation C0, this rerun strengthens evidence for residual/HI mechanics because the degradation label is no longer constant. It still does not validate maintenance events, baseline reset, Q4b, or Marine transfer.
