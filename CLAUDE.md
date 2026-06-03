# Ship Health Monitoring - Project State

## Project Goal
Build a ship system health hierarchy monitoring system.
Technical pipeline: Condition Normalization -> Expected State Model -> Residual -> Health Index -> Trend/Margin

## Current Phase
Phase 1: LBNL Chiller Plant dataset validation (Pipeline Validation B1)

## Validation Targets
- B1 (LBNL): Can the pipeline run end-to-end?
- B2 (RP-1043): Does HI have physical meaning (monotonicity with fault severity)?
- C (Marine): Can trend detection precede alarms on real ship data?

## Today's Target
Answer: Can Condition Variables sufficiently predict Expected State?

## Key Design Decisions
- Condition Variables: external/load inputs that drive system behavior
- State Variables: system response outputs that reflect health
- Residual = Observed - Predicted (after condition normalization)
- XGBoost for Expected State Model v0 (VIB deferred to later stage)

## File Structure
- data/lbnl/         : LBNL FDD Chiller Plant dataset
- src/               : source modules
- outputs/           : audit reports, model outputs, figures
- docs/              : variable mapping, design decisions

## Status Log
- [ ] Task 1: Project initialization
- [ ] Task 2: LBNL data audit
- [ ] Task 3: Variable mapping frozen
- [ ] Task 4: Expected State Model spike
- [ ] Task 5: Residual output + normal/fault separation
- [x] Validation B1 Expected State Model
- [x] Validation B1 Residual Baseline Pipeline

## Frozen HVAC Variable Mapping v1

Condition Variables:

- CWL_SEC_LOAD
- OA_TEMP
- OA_TEMP_WB
- CWL_PRI_SW_TEMPSPT
- CT_SW_TEMPSPT
- CWL_SEC_DPSPT

State Variables:

- CHL_POW_1
- CHL_SW_TEMP_1
- CT_SW_TEMP_1
- CHL_RWCD_TEMP_1

Domain:

HVAC (LBNL Chiller Plant)

Status:

Validation B1 Complete

## Research Conclusion

Condition Variables can predict State Variables with high accuracy.

Expected State route supported.

Residual baseline established.

Domain Transfer Risk remains open.

Marine validation NOT completed.

## Next

Validation B2

Use:

- coolingtower_fouling_065
- coolingtower_fouling_080
- coolingtower_fouling_095

Question:

Does residual magnitude increase monotonically with fault severity?
