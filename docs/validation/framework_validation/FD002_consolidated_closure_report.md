# FD002 Consolidated Closure Report

Document status: Frozen  
Version: v1.0  
Dataset: C-MAPSS FD002  
Closure type: Consolidated public-data validation closure  
Marine validity: Not claimed

## 1. Purpose

This report provides the authoritative consolidated closure for the completed C-MAPSS FD002 public-data validation line. It consolidates existing reviewed repository evidence for BL150 residual execution, BL175 residual sensitivity execution, Health Evidence v0, HI v0, and Phase B1 fixed-channel cross-model validation.

This closure does not perform independent numerical reproduction. It does not rerun models, recompute residuals, recompute Evidence, recompute HI, recompute Phase B1 outputs, compute test metrics, or perform Health Assessment.

## 2. Closure Boundary

This is a documentation and closure task only. It accepts the frozen FD002 existing-state audit as the controlling pre-closure evidence base.

This closure does not imply:

- independent numerical reproduction;
- complete historical reproducibility;
- Health Assessment completion;
- Marine feasibility;
- Marine validity;
- deployment readiness.

Public-data evidence only. No Marine validity claimed. No Health Assessment performed.

## 3. Authoritative Evidence Base

The closure is based on the frozen audit and its supporting tables:

- `docs/validation/framework_validation/FD002_existing_state_audit.md`
- `outputs/cmapss_fd002/existing_state_audit/FD002_claim_audit.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_artifact_inventory.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_dataset_lineage.csv`
- `outputs/cmapss_fd002/existing_state_audit/audit_summary.json`

The audit state verified before closure was:

- Audit status: Frozen
- Audit version: v1.0
- Entry state: `FD002_ENTRY_STATE_E`
- Recommended next action: `CREATE_FD002_CLOSURE`

## 4. FD002 Execution History

The repository evidence reconstructs the following execution chain:

1. Dataset and schema context were documented.
2. Operating-condition and settings-structure checks were performed.
3. Expected State target and RUL reference-window decisions were documented.
4. BL150 residual execution produced archived residual outputs and diagnostics.
5. BL175 residual sensitivity execution produced archived residual outputs and diagnostics.
6. Health Evidence v0 identified primary channel evidence from the residual outputs.
7. HI v0 constructed a canonical scalar HI from the primary Evidence channels.
8. Phase B1 fixed-channel validation compared model-family behavior and recorded cross-model support plus an underfit negative control.

## 5. BL150 Residual Findings

Canonical BL150 residual values:

- sensor_11 absolute-residual correlation: `-0.6090043819301661`
- sensor_11 raw-residual correlation: `-0.691596119241661`

The BL150 execution provides public-data residual evidence for sensor_11 under the 150-cycle reference-window configuration. These correlations are repository-recorded historical results and were not independently recomputed during the consolidated closure.

Correlation alone is not treated as proof of causal degradation measurement, calibrated remaining-life prediction, or Marine residual validity.

## 6. BL175 Sensitivity Findings

Canonical BL175 residual values:

- sensor_11 absolute-residual correlation: `-0.6229008182517646`
- sensor_11 raw-residual correlation: `-0.6911812248771092`

The BL175 execution provides sensitivity evidence under the 175-cycle reference-window configuration. The similarity between BL150 and BL175 supports sensitivity robustness at the tested 150-cycle and 175-cycle reference settings.

These correlations are repository-recorded historical results and were not independently recomputed during the consolidated closure.

## 7. Health Evidence v0 Findings

Primary channels:

- `sensor_11`
- `sensor_4`
- `sensor_15`

Health Evidence v0 identified a small fixed primary channel set with consistent trajectory-related evidence across BL150 and BL175. The Evidence layer establishes public-data development evidence for channel progression and robustness. It does not establish equipment-level Health Assessment or Marine validity.

Documented deferred sensitivity:

- 15% / 20% reference-window sensitivity: `NOT_EXECUTED`
- Classification: `DOCUMENTED_DEFERRED_SENSITIVITY`

This closure does not imply that all originally conceivable reference-window sensitivities were tested.

## 8. HI v0 Findings

Canonical closure metric:

- HI variant: `HI_primary_equal_uncentered`
- Metric: `median_spearman_hi`
- BL150: `0.7583807420883869`
- BL175: `0.7743753188563743`
- fraction_positive: `1.0`

The canonical HI v0 construction produced positive unit-level trajectory association across all evaluated units and retained similar median Spearman performance across BL150 and BL175. The BL150 / BL175 similarity supports robustness to the tested reference-window change.

Alternative HI values in the repository correspond to documented centered, all-candidate, leave-one-out, row-level, or Phase B1 variants. They are not competing values for the canonical closure metric.

This closure does not claim that HI is physically calibrated, equals true degradation, or transfers to ships without further validation.

## 9. Phase B1 Findings

Phase B1 findings:

- poly3: `STABLE_WITH_PHASE_A`
- ridge: `STABLE_WITH_PHASE_A`
- poly1: `UNDERFIT_NEGATIVE_CONTROL`

Phase B1 showed that the fixed-channel evidence and HI conclusions were not restricted to a single upstream model family. poly3 and ridge retained results consistent with the Phase A evidence. poly1 materially weakened the resulting HI and was accepted as an underfit negative control rather than treated as a successful model.

Deferred or not performed:

- Phase B2: `DEFERRED`
- Health Assessment: `NOT_PERFORMED`

This closure does not imply that every possible model family was tested.

## 10. Numerical Lineage Status

Five historical execution groups have confirmed lineage limitations:

| group | historical dataset hash recorded | explicit historical source execution script located | lineage basis | lineage confidence |
|---|---|---|---|---|
| BL150 | NO | NO | DOCUMENT_REFERENCE | MEDIUM |
| BL175 | NO | NO | DOCUMENT_REFERENCE | MEDIUM |
| Health Evidence v0 | NO | NO | DOCUMENT_REFERENCE | MEDIUM |
| HI v0 | NO | NO | DOCUMENT_REFERENCE | MEDIUM |
| Phase B1 | NO | NO | DOCUMENT_REFERENCE | MEDIUM |

The archived numerical artifacts, execution summaries, reviews, and closure records are internally coherent.

However, the historical executions are not fully reproducible from the currently recorded dataset-hash and source-script lineage.

The results are therefore accepted as authoritative repository evidence with documented reproducibility-lineage limitations.

No dataset identity conflict was found. That finding does not prove historical input identity.

## 11. Dataset Identity Status

Current dataset identity:

- Outer dataset package: `data/cmapss/6_Turbofan_Engine_Degradation_Simulation_Data_Set.zip`
- Outer SHA-256: `C9C5DEC12A945A82E8BB4446589D7FB3CC057B5E5D81FA1A12E25EE9912AD3B2`
- Inner `CMAPSSData.zip` SHA-256: `74BEF434A34DB25C7BF72E668EA4CD52AFE5F2CF8E44367C55A82BFD91A5A34F`
- `train_FD002.txt` SHA-256: `DAC6C4DBC4E7C1BDEB5747DA3D313D05C395BB99801B44A002B26A2BA13D788F`
- `test_FD002.txt` SHA-256: `DE7B5BF7E998A985C378488480528B7C02CFF1406A46740DEF362DDA8D9B4E02`
- `RUL_FD002.txt` SHA-256: `C851DD96A6EA6998D3C4A8F834D3C8013AA90E93A6ED950DC826AD0655B2906B`

Conclusion:

- Current dataset identity: `RECORDED`
- Historical dataset hash match: `NOT_VERIFIABLE`
- Dataset identity conflict: `NONE_FOUND`

## 12. Unfinished and Deferred Work

Deferred or unfinished work:

- 15% / 20% reference-window sensitivity: `DOCUMENTED_DEFERRED_SENSITIVITY`
- Phase B2: `DEFERRED`
- Health Assessment: `NOT_PERFORMED`
- Full historical reproduction from recorded dataset hashes and source scripts: `NOT_AVAILABLE`

These are retained as limitations. They do not reopen BL150, BL175, Health Evidence v0, HI v0, or Phase B1 by themselves.

## 13. Claims Supported by FD002

FD002 supports the following claims, with public-data and lineage limitations retained:

- FD002 residual execution was completed for BL150 and BL175.
- sensor_11 showed consistent residual association across BL150 and BL175.
- Health Evidence v0 identified sensor_11, sensor_4, and sensor_15 as the primary channel set.
- The canonical HI v0 construction showed positive unit-level trajectory association with median Spearman approximately 0.758 for BL150 and 0.774 for BL175.
- Phase B1 provided cross-model support from poly3 and ridge and an underfit negative control from poly1.
- FD002 provides public-data evidence for the residual-to-Evidence-to-HI route.

## 14. Claims Not Supported by FD002

FD002 does not support these interpretations:

- FD002 proves Marine validity.
- FD002 proves Marine feasibility.
- FD002 completes Health Assessment.
- FD002 demonstrates deployment readiness.
- FD002 proves causal degradation measurement.
- FD002 is fully historically reproducible.
- FD002 validates all model families or all reference-window settings.

Required boundary:

Public-data evidence only. No Marine validity claimed. No Health Assessment performed.

## 15. Final Closure Decision

Final closure decision:

`CMAPSS_FD002_RESIDUAL_EVIDENCE_HI_AND_PHASE_B1_COMPLETED_WITH_DOCUMENTED_LINEAGE_AND_SENSITIVITY_LIMITATIONS`

Summary state:

| item | state |
|---|---|
| Residual execution | COMPLETE |
| Health Evidence v0 | COMPLETE_WITH_LIMITATIONS |
| HI v0 | COMPLETE |
| Phase B1 | COMPLETE |
| Historical numerical reproduction | NOT_PERFORMED |
| Historical execution reproducibility | LIMITED_BY_MISSING_DATASET_HASH_AND_SOURCE_SCRIPT_LINEAGE |
| Dataset identity conflict | NONE_FOUND |
| Health Assessment | NOT_PERFORMED |
| Marine validity | NOT_CLAIMED |

## 16. Future Reopening Conditions

FD002 may be reopened only for a separately authorized task, such as:

- reconstructing source-script lineage;
- recording reproducible execution manifests;
- rerunning FD002 from canonical source data under a new controlled protocol;
- executing 15% / 20% sensitivity;
- executing Phase B2;
- performing a separate Health Assessment stage.

A reopening task must not overwrite or silently reinterpret the historical FD002 evidence closed here.

## 17. Next-Stage Handoff

FD002 is closed as a public-data residual / Evidence / HI / Phase B1 validation line with documented lineage and sensitivity limitations.

Next authorized stage:

`To be determined by the project roadmap after FD002 closure`
