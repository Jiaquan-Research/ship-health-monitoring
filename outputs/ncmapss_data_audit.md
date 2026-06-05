# N-CMAPSS Data Audit

## 1. Download Source and Files

- Succeeded URL: https://phm-datasets.s3.amazonaws.com/NASA/17.+Turbofan+Engine+Degradation+Simulation+Data+Set+2.zip
- Source label: NASA PCoE Prognostic Data Repository, Turbofan Engine Degradation Simulation Data Set 2
- Total downloaded/extracted size under `data/ncmapss/`: 60.75 GB

| File | Size MB |
|---|---:|
| `17. Turbofan Engine Degradation Simulation Data Set 2/data_set.zip` | 15814.4 |
| `17_Turbofan_Engine_Degradation_Simulation_Data_Set_2.zip` | 15760.4 |
| `data_set/N-CMAPSS_DS01-005.h5` | 2873.4 |
| `data_set/N-CMAPSS_DS02-006.h5` | 2450.5 |
| `data_set/N-CMAPSS_DS03-012.h5` | 3693.4 |
| `data_set/N-CMAPSS_DS04.h5` | 3752.5 |
| `data_set/N-CMAPSS_DS05.h5` | 2599.2 |
| `data_set/N-CMAPSS_DS06.h5` | 2549.2 |
| `data_set/N-CMAPSS_DS07.h5` | 2714.7 |
| `data_set/N-CMAPSS_DS08a-009.h5` | 3236.8 |
| `data_set/N-CMAPSS_DS08c-008.h5` | 2413.1 |
| `data_set/N-CMAPSS_DS08d-010.h5` | 2885.0 |
| `data_set/N-CMAPSS_Example_data_loading_and_exploration.ipynb` | 4.6 |
| `data_set/Run_to_Failure_Simulation_Under_Real_Flight_Conditions_Dataset.pdf` | 0.9 |

## 2. File Format and Structure

- File format confirmed: HDF5 (`.h5`) inside nested ZIP archives.
- HDF5 files found: 10
- Sample file audited in detail: `data_set/N-CMAPSS_DS01-005.h5`
- Data integrity note: outer and inner ZIP archives passed `testzip`; however, the following HDF5 file(s) could not be opened by `h5py`:
  - `N-CMAPSS_DS08d-010.h5`: OSError: Unable to synchronously open file (truncated file: eof = 2885034848, sblock->base_addr = 0, stored_eof = 2885034880)

Top-level HDF5 keys in sample file:

- `A_dev`: shape=(4906636, 4), dtype=float64
- `A_test`: shape=(2735232, 4), dtype=float64
- `A_var`: shape=(4,), dtype=|S5
- `T_dev`: shape=(4906636, 10), dtype=float64
- `T_test`: shape=(2735232, 10), dtype=float64
- `T_var`: shape=(10,), dtype=|S12
- `W_dev`: shape=(4906636, 4), dtype=float64
- `W_test`: shape=(2735232, 4), dtype=float64
- `W_var`: shape=(4,), dtype=|S4
- `X_s_dev`: shape=(4906636, 14), dtype=float64
- `X_s_test`: shape=(2735232, 14), dtype=float64
- `X_s_var`: shape=(14,), dtype=|S4
- `X_v_dev`: shape=(4906636, 14), dtype=float64
- `X_v_test`: shape=(2735232, 14), dtype=float64
- `X_v_var`: shape=(14,), dtype=|S5
- `Y_dev`: shape=(4906636, 1), dtype=int64
- `Y_test`: shape=(2735232, 1), dtype=int64

## 3. Channel List

### Condition Variables

`alt`, `Mach`, `TRA`, `T2`

### Auxiliary / Index Variables

`unit`, `cycle`, `Fc`, `hs`

### State Variables / Sensors

`T24`, `T30`, `T48`, `T50`, `P15`, `P2`, `P21`, `P24`, `Ps30`, `P40`, `P50`, `Nf`, `Nc`, `Wf`

### Virtual Sensors

`T40`, `P30`, `P45`, `W21`, `W22`, `W25`, `W31`, `W32`, `W48`, `W50`, `SmFan`, `SmLPC`, `SmHPC`, `phi`

### Health State / Degradation Labels

`fan_eff_mod`, `fan_flow_mod`, `LPC_eff_mod`, `LPC_flow_mod`, `HPC_eff_mod`, `HPC_flow_mod`, `HPT_eff_mod`, `HPT_flow_mod`, `LPT_eff_mod`, `LPT_flow_mod`

Requested key-channel presence:

| Category | Present | Missing |
|---|---|---|
| Condition | Mach, T2, TRA, alt | None |
| State/Sensor | Nc, Nf, P15, P2, P30, P45, P50, T24, T30, T48, T50, Wf | None |
| Health State | HPC_eff_mod, HPT_eff_mod, LPC_eff_mod, LPT_eff_mod, fan_eff_mod | None |

## 4. Units and Flight Cycles

| H5 file | Units | Dev rows | Test rows | Dev cycles | Test cycles | RUL range dev | RUL range test |
|---|---:|---:|---:|---:|---:|---|---|
| `N-CMAPSS_DS01-005.h5` | 10 | 4,906,636 | 2,735,232 | 100 | 90 | 0 to 99 | 0 to 89 |
| `N-CMAPSS_DS02-006.h5` | 9 | 5,263,447 | 1,253,743 | 89 | 76 | 0 to 88 | 0 to 75 |
| `N-CMAPSS_DS03-012.h5` | 15 | 5,571,277 | 4,251,560 | 93 | 93 | 0 to 92 | 0 to 92 |
| `N-CMAPSS_DS04.h5` | 10 | 6,377,452 | 3,602,561 | 100 | 99 | 0 to 99 | 0 to 98 |
| `N-CMAPSS_DS05.h5` | 10 | 4,350,606 | 2,562,046 | 100 | 91 | 0 to 99 | 0 to 90 |
| `N-CMAPSS_DS06.h5` | 10 | 4,257,209 | 2,522,447 | 99 | 91 | 0 to 98 | 0 to 90 |
| `N-CMAPSS_DS07.h5` | 10 | 4,350,176 | 2,869,786 | 85 | 96 | 0 to 84 | 0 to 95 |
| `N-CMAPSS_DS08a-009.h5` | 15 | 4,885,389 | 3,722,997 | 95 | 78 | 0 to 94 | 0 to 77 |
| `N-CMAPSS_DS08c-008.h5` | 10 | 4,299,918 | 2,117,819 | 60 | 62 | 0 to 59 | 0 to 61 |
| `N-CMAPSS_DS08d-010.h5` | 0 | 0 | 0 | 0 | 0 | n/a to n/a | n/a to n/a |

- Unique unit identifiers observed across all files: 18
- Flight cycle index confirmed: `cycle` is present in `A_var`.
- Unit index confirmed: `unit` is present in `A_var`.
- Remaining useful life label confirmed: `Y_dev` / `Y_test`.

## 5. Maintenance Event Check

| Check | Result | Evidence |
|---|---|---|
| Maintenance event channel present? | No | No HDF5 key or variable name matched maintenance/repair/replacement/reset keywords. |
| Multiple run-to-failure cycles per unit? | No evidence | Dataset provides degradation trajectories and RUL labels, but no lifecycle segment or post-repair restart indicator was found. |
| Baseline reset indicator present? | No | No baseline/reset/segment field is present in keys or channel names. |

Keyword scan result: no maintenance-related field names found.

## 6. Suitability Assessment

- Q4b direct validation: **Not suitable**. N-CMAPSS does not contain real maintenance events, component replacement events, or baseline reset labels.
- Surrogate use for segment-aware mechanics: **Suitable**. It has unit identifiers, flight-cycle indices, operating conditions, sensor/state variables, health-state degradation labels, and RUL labels.
- Interpretation boundary: N-CMAPSS can validate whether code can handle units/cycles/segments if artificial segment markers are imposed, but it cannot prove real Baseline Management logic.

## 7. Recommended Next Steps

1. Use N-CMAPSS only as a surrogate scaffold for segment-aware pipeline mechanics.
2. Define artificial segment boundaries explicitly and label them as synthetic baseline resets.
3. Continue searching for a dataset with real maintenance records before claiming Q4b validation.
4. Keep Marine validation status open until real ship maintenance/event logs are available.
