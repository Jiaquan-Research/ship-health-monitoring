# Exploratory E-1 Cross-Regime Probe

## Scope

This is NOT a validation.

This is NOT M-1A.

No claims are upgraded.

No conclusions about universality are made.

Observation only.

## Frozen C0.2 Selections

* Dataset: `data\ncmapss\data_set\N-CMAPSS_DS02-006.h5`
* Units: `5, 2, 16`
* Condition variables: `alt, Mach, TRA, T2`
* Target: `T50`
* Ground-truth label retained from C0.2: `HPT_eff_mod`

No C0.2 models were retrained or modified.

## Regime Windows

Regime windows are lifecycle partitions only.

They are not interpreted as health states.

| Unit | Regime | Cycle Span | Rows | Mean HPT_eff_mod |
|---:|---|---|---:|---:|
| 5 | Early | 1-17 (17 cycles) | 202,400 | -0.0009712 |
| 5 | Middle | 36-53 (18 cycles) | 189,338 | -0.002378 |
| 5 | Late | 72-89 (18 cycles) | 213,018 | -0.01274 |
| 2 | Early | 1-15 (15 cycles) | 177,856 | -0.0007411 |
| 2 | Middle | 31-45 (15 cycles) | 163,558 | -0.002223 |
| 2 | Late | 61-75 (15 cycles) | 159,596 | -0.01224 |
| 16 | Early | 1-12 (12 cycles) | 156,587 | -0.0007715 |
| 16 | Middle | 26-37 (12 cycles) | 155,829 | -0.001639 |
| 16 | Late | 51-63 (13 cycles) | 146,643 | -0.006585 |

## Transfer Matrix

Mean R2 across units.

| Train \\ Test | Early | Middle | Late |
|---|---:|---:|---:|
| Early | 0.9994 | 0.9928 | 0.8709 |
| Middle | 0.9872 | 0.9993 | 0.8938 |
| Late | 0.8587 | 0.8932 | 0.9978 |

## Detailed Results

| Unit | Train | Test | R2 | MAE | Residual Mean | Residual Std | Residual RMS | Abs Residual Mean |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 5 | Early | Early | 0.9994 | 0.6753 | 4.514e-05 | 1.221 | 1.221 | 0.6753 |
| 5 | Early | Middle | 0.9912 | 3.304 | 1.924 | 4.34 | 4.747 | 3.304 |
| 5 | Early | Late | 0.8559 | 18.48 | 18.36 | 6.781 | 19.57 | 18.48 |
| 5 | Middle | Early | 0.9891 | 3.568 | -3.198 | 4.013 | 5.132 | 3.568 |
| 5 | Middle | Middle | 0.9993 | 0.7447 | 1.468e-05 | 1.336 | 1.336 | 0.7447 |
| 5 | Middle | Late | 0.8899 | 15.85 | 15.73 | 6.7 | 17.1 | 15.85 |
| 5 | Late | Early | 0.8595 | 17.89 | -17.88 | 4.616 | 18.47 | 17.89 |
| 5 | Late | Middle | 0.8839 | 16.34 | -16.3 | 5.558 | 17.22 | 16.34 |
| 5 | Late | Late | 0.9978 | 1.508 | 8.34e-05 | 2.392 | 2.392 | 1.508 |
| 2 | Early | Early | 0.9993 | 0.7362 | 6.345e-05 | 1.456 | 1.456 | 0.7362 |
| 2 | Early | Middle | 0.9942 | 2.908 | 2.283 | 3.199 | 3.93 | 2.908 |
| 2 | Early | Late | 0.8693 | 17.98 | 17.98 | 5.739 | 18.88 | 17.98 |
| 2 | Middle | Early | 0.985 | 3.882 | -2.952 | 6.045 | 6.727 | 3.882 |
| 2 | Middle | Middle | 0.9991 | 0.7142 | -3.651e-05 | 1.586 | 1.586 | 0.7142 |
| 2 | Middle | Late | 0.882 | 16.88 | 16.88 | 6.088 | 17.94 | 16.88 |
| 2 | Late | Early | 0.8591 | 19.34 | -19.32 | 7.202 | 20.62 | 19.34 |
| 2 | Late | Middle | 0.8915 | 16.01 | -15.91 | 5.985 | 17 | 16.01 |
| 2 | Late | Late | 0.9981 | 1.434 | 5.981e-05 | 2.295 | 2.295 | 1.434 |
| 16 | Early | Early | 0.9994 | 0.705 | 2.115e-06 | 1.313 | 1.313 | 0.705 |
| 16 | Early | Middle | 0.993 | 3.331 | 2.567 | 3.431 | 4.285 | 3.331 |
| 16 | Early | Late | 0.8874 | 16.14 | 16.12 | 5.862 | 17.16 | 16.14 |
| 16 | Middle | Early | 0.9875 | 3.632 | -2.981 | 5.129 | 5.932 | 3.632 |
| 16 | Middle | Middle | 0.9994 | 0.693 | -9.294e-05 | 1.233 | 1.233 | 0.693 |
| 16 | Middle | Late | 0.9096 | 14.18 | 14.15 | 6.013 | 15.37 | 14.18 |
| 16 | Late | Early | 0.8576 | 17.63 | -17.59 | 9.644 | 20.06 | 17.63 |
| 16 | Late | Middle | 0.9043 | 14.59 | -14.54 | 6.163 | 15.79 | 14.59 |
| 16 | Late | Late | 0.9976 | 1.535 | -7.167e-05 | 2.491 | 2.491 | 1.535 |

## Summary

* Mean same-window R2: `0.9988`
* Mean cross-window R2: `0.9161`

## Interpretation

If same-window performance is approximately cross-window performance, cross-regime instability is weak.

If cross-window performance collapses while same-window remains good, cross-regime instability exists.

No speculation is provided.

No comparison with HVAC is made.

No universality claim is made.

## Verdict

No obvious instability observed.
