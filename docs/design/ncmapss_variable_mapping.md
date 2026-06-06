# N-CMAPSS Variable Mapping for Validation C0

**Status:** Frozen for Validation C0 surrogate spike.

**Scope:** Surrogate mechanics validation only. Not maintenance-event evidence. Not Q4b evidence.

## Dataset

- Source file: `data/ncmapss/data_set/N-CMAPSS_DS02-006.h5`
- Split used: `dev` only
- Excluded file: `N-CMAPSS_DS08d-010.h5`

## Condition Variables

From `W_dev`:

| Variable | Interpretation |
|---|---|
| `alt` | Altitude |
| `Mach` | Mach number |
| `TRA` | Throttle resolver angle |
| `T2` | Fan inlet temperature |

## State Variables

From `X_s_dev`:

| Role | Variable | Interpretation |
|---|---|---|
| Primary | `T30` | HPC outlet temperature |
| Secondary | `T24` | Fan outlet temperature |
| Secondary | `Wf` | Fuel flow |

## Ground Truth Degradation Variable

From `T_dev`:

| Variable | Interpretation |
|---|---|
| `HPC_eff_mod` | HPC efficiency degradation modifier. More negative means more degraded. |

## Artificial Lifecycle Zones

For each selected unit:

- Zone A: first 20% of cycles, treated as healthy baseline.
- Zone T: middle 60% of cycles, excluded from primary A/B comparisons.
- Zone B: last 20% of cycles, treated as degraded condition.

These zones are artificial lifecycle segments, not maintenance events.
