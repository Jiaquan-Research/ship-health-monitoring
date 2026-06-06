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

## Validation B2 Result

Status:

FAIL

Key findings:

- Frozen Validation B1 Expected State Models were applied without retraining.
- Cooling-tower fouling residuals did not increase monotonically under the requested Baseline -> 065 -> 080 -> 095 ordering.
- No target passed strict or relaxed monotonicity using AbsMean, RMS, or P95.
- `CT_SW_TEMP_1` had the strongest sensitivity score, but the response was not monotonic.
- The tested residual metrics do not yet support Expected State -> Residual -> Degradation for this fault family.

Implication:

A simple HI_v0 is not justified from this B2 result alone.

Next action:

Audit the physical meaning of fouling severity labels and confirm whether lower fouling factor values represent more severe degradation before redesigning HI_v0.

## Validation B2.1 Result

Status:

PASS - Strong PASS

Corrected severity ordering:

Baseline -> 095 -> 080 -> 065

Key findings:

- B2 diagnosis showed 095 is weakest fouling, 080 is moderate fouling, and 065 is strongest fouling.
- Frozen Validation B1 Expected State Models were reused without retraining.
- All 4 targets showed strict monotonicity for AbsMean, RMS, and P95 under corrected ordering.
- Most sensitive target: `CT_SW_TEMP_1`.
- Sensitivity ranking: `CT_SW_TEMP_1`, `CHL_RWCD_TEMP_1`, `CHL_SW_TEMP_1`, `CHL_POW_1`.
- Expected State -> Residual -> Physical Degradation is preliminarily supported for LBNL cooling-tower fouling.
- Q2 of the Concept Paper can be marked Preliminary Supported with the caveat that evidence is HVAC-domain and label-order dependent.

## HI_v0 Validation

Status:

PASS - Moderate PASS

Best target:

CT_SW_TEMP_1

Best window:

W = 6h

Q3 status:

Preliminary Supported

Key findings:

- HI_v0 was computed only from frozen B2.1 normalized residuals.
- No residuals were recomputed and no Expected State Models were retrained.
- HI_v0A (`CT_SW_TEMP_1`) showed the strongest sensitivity and clear monotonic response.
- Primary 24h window showed monotonic HI_mean for all 4 targets.
- HI_v0 improved sensitivity over raw residual RMS mainly for `CT_SW_TEMP_1`; broader improvement across all targets was not demonstrated.
- Q3 is Preliminary Supported for HVAC-domain single-variable HI construction, with marine transfer still unvalidated.

## Validation B4 Residual Trend Audit

Status:

PASS - Strong PASS

Q4a status:

Initial Evidence

Best trend metric:

RMS

Targets with reliable trend:

4/4

Key findings:

- B4 used frozen Validation B2.1 residuals only.
- No residuals were recomputed and no Expected State Models were retrained.
- Stage order: Baseline -> 095 -> 080 -> 065.
- All 4 targets showed strict monotonicity for AbsMean, RMS, P95, P99, and Std.
- Spearman rho = 1.0 for all target/metric combinations.
- HI_v0 Rolling RMS 24h improved the CT_SW_TEMP_1 strongest-vs-baseline trend ratio over raw residual RMS.
- Residual -> Trend exists in the HVAC pseudo-degradation path; Q4a can be marked Initial Evidence.

---

## Validation C0 Series — FROZEN (2026-06-06)

### C0: N-CMAPSS Surrogate Spike
Result: Weak Evidence (Ground Truth issue)
Finding: HPC_eff_mod = 0 in DS02-006, Spearman undefined

### C0.1: Label Audit
Result: Diagnosis complete
Finding: DS02-006 is HPT fault type. Use HPT_eff_mod.

### C0.2: Ground Truth Aligned Rerun
Result: STRONG PASS
T50 Held-out R²: 0.992~0.996
Residual |Spearman|: 0.772~0.826
HI |Spearman|: 0.951~0.994
HI B/A Ratio: 8.5~12.3x
Best target: T50 (HPT outlet temp)
Best window: W=5 cycles
Early detection: ~20-29% lifecycle

### Cross-Domain Evidence Status
Q1: Strong Evidence (HVAC + Aero Engine)
Q2: Strong Evidence (HVAC + Aero Engine)
Q3: Moderate Evidence (HVAC + Aero Engine)
Q4a: Initial Evidence
Q4b: Open — Architecture Defined, awaiting Marine data

### Explicitly NOT Current Priorities
- Further N-CMAPSS experiments
- HI_v1 implementation
- RUL prediction
- Deep learning models

### Next Priority
P1: Marine data acquisition (teaching vessel)
P2: Baseline Management validation with real data
P3: Validation D (Marine generator)
