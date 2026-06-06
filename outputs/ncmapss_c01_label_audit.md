# Validation C0.1 — T_dev Label Audit

Read-only audit of N-CMAPSS degradation labels. No model retraining and no residual recomputation were performed.

## 1. Global T_dev Statistics — DS02-006 Dev

| Column | Min | Max | Mean | Std | All_Zero |
| --- | --- | --- | --- | --- | --- |
| fan_eff_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| fan_flow_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| LPC_eff_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| LPC_flow_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| HPC_eff_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| HPC_flow_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| HPT_eff_mod | -0.018668 | 0.000021 | -0.003463 | 0.003747 | False |
| HPT_flow_mod | 0.000000 | 0.000000 | 0.000000 | 0.000000 | True |
| LPT_eff_mod | -0.023184 | 0.000075 | -0.001655 | 0.003480 | False |
| LPT_flow_mod | -0.017672 | 0.000000 | -0.001468 | 0.002694 | False |

## 2. Per-unit T_dev Max Absolute Values — DS02-006 Dev

A `*` marks max_abs > 0.001.

| Unit | fan_eff_mod | fan_flow_mod | LPC_eff_mod | LPC_flow_mod | HPC_eff_mod | HPC_flow_mod | HPT_eff_mod | HPT_flow_mod | LPT_eff_mod | LPT_flow_mod |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.018145* | 0.000000 | 0.000000 | 0.000000 |
| 5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.018668* | 0.000000 | 0.000000 | 0.000000 |
| 10 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.018137* | 0.000000 | 0.000000 | 0.000000 |
| 16 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.008968* | 0.000000 | 0.005504* | 0.017672* |
| 18 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.007836* | 0.000000 | 0.017766* | 0.011139* |
| 20 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.007693* | 0.000000 | 0.023184* | 0.006428* |

## 3. Usable Ground Truth Summary

- Usable ground truth columns: HPT_eff_mod, LPT_eff_mod, LPT_flow_mod
- Zero columns: fan_eff_mod, fan_flow_mod, LPC_eff_mod, LPC_flow_mod, HPC_eff_mod, HPC_flow_mod, HPT_flow_mod

| Column | Usable | Nonzero Units | Min | Max |
| --- | --- | --- | --- | --- |
| fan_eff_mod | False | None | 0.000000 | 0.000000 |
| fan_flow_mod | False | None | 0.000000 | 0.000000 |
| LPC_eff_mod | False | None | 0.000000 | 0.000000 |
| LPC_flow_mod | False | None | 0.000000 | 0.000000 |
| HPC_eff_mod | False | None | 0.000000 | 0.000000 |
| HPC_flow_mod | False | None | 0.000000 | 0.000000 |
| HPT_eff_mod | True | 2, 5, 10, 16, 18, 20 | -0.018668 | 0.000021 |
| HPT_flow_mod | False | None | 0.000000 | 0.000000 |
| LPT_eff_mod | True | 16, 18, 20 | -0.023184 | 0.000075 |
| LPT_flow_mod | True | 16, 18, 20 | -0.017672 | 0.000000 |

## 4. Dev vs Test Comparison — DS02-006

| Column | Dev_Std | Test_Std | Non-zero in Dev | Non-zero in Test |
| --- | --- | --- | --- | --- |
| fan_eff_mod | 0.000000 | 0.000000 | False | False |
| fan_flow_mod | 0.000000 | 0.000000 | False | False |
| LPC_eff_mod | 0.000000 | 0.000000 | False | False |
| LPC_flow_mod | 0.000000 | 0.000000 | False | False |
| HPC_eff_mod | 0.000000 | 0.000000 | False | False |
| HPC_flow_mod | 0.000000 | 0.000000 | False | False |
| HPT_eff_mod | 0.003747 | 0.002815 | True | True |
| HPT_flow_mod | 0.000000 | 0.000000 | False | False |
| LPT_eff_mod | 0.003480 | 0.002221 | True | True |
| LPT_flow_mod | 0.002694 | 0.003393 | True | True |

## 5. Cross-file Comparison — DS02-006 vs DS01-005 Dev

- Non-zero DS02-006 dev columns: HPT_eff_mod, LPT_eff_mod, LPT_flow_mod
- Non-zero DS01-005 dev columns: HPT_eff_mod

| Column | DS02_dev_nonzero | DS01_dev_nonzero |
| --- | --- | --- |
| fan_eff_mod | False | False |
| fan_flow_mod | False | False |
| LPC_eff_mod | False | False |
| LPC_flow_mod | False | False |
| HPC_eff_mod | False | False |
| HPC_flow_mod | False | False |
| HPT_eff_mod | True | True |
| HPT_flow_mod | False | False |
| LPT_eff_mod | True | False |
| LPT_flow_mod | True | False |

## 6. Diagnosis

**Q1: Is HPC_eff_mod the only zero column, or is the entire T_dev block zero?**

HPC_eff_mod is zero, but the entire T_dev block is not empty. DS02-006 dev has non-zero HPT_eff_mod, LPT_eff_mod, and LPT_flow_mod.

**Q2: Which units have non-zero degradation labels?**

All DS02-006 dev units show non-trivial non-zero values for HPT_eff_mod. Units 16, 18, and 20 also show non-zero LPT_eff_mod and LPT_flow_mod. HPC_eff_mod remains zero for all units.

**Q3: Which ground truth column should be used for Spearman correlation instead of HPC_eff_mod?**

For DS02-006 dev, use `HPT_eff_mod`. It is non-zero across the selected units and is the clearest efficiency degradation label in this file.

**Q4: Is DS02-006 dev split suitable for ground truth correlation validation? If not, which DS file is recommended?**

DS02-006 dev is not suitable for HPC_eff_mod correlation validation because HPC_eff_mod is constant zero. It is suitable only if the C0 rerun switches the ground-truth label to a non-zero DS02 component such as HPT_eff_mod. For HPC-specific validation, the DS01 spot check should be used only if its HPC_eff_mod is non-zero; otherwise pick a file whose component degradation matches the target variable.

## 7. Recommendation

- Best ground truth column for a DS02 C0 Spearman rerun: `HPT_eff_mod`.
- Best DS file from this spot check: `N-CMAPSS_DS01-005.h5 using HPT_eff_mod`.
- Recommended rerun rule: align the state target with the component that actually degrades in the selected DS file. Do not reuse HPC_eff_mod when it is constant zero.
