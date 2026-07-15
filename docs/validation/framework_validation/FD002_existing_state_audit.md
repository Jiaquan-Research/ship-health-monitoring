# FD002 Existing-State Audit

Document status: Frozen  
Version: v1.0  
Audit type: Existing-state and evidence-lineage audit  
Dataset: C-MAPSS FD002  
Marine validity: Not claimed  
Audit date: 2026-07-12

## 1. Purpose

This audit reconstructs the current repository state for C-MAPSS FD002 before any new FD002 work is authorized. It determines what was designed, executed, reviewed, frozen, incomplete, historical, and usable as an entry point.

This audit does not rerun or extend FD002 validation. It determines the authoritative repository state before any new work.

No model training, residual recomputation, Evidence recomputation, HI recomputation, test evaluation, or Health Assessment work was performed.

In this audit, `VERIFIED` means that a historical claim matches the currently archived repository artifacts, execution summaries, and review records. `VERIFIED` does not mean that the numerical result was independently recomputed or reproduced during this audit.

## 2. Repository Scope

The audit searched `docs/`, `outputs/`, `scripts/`, `src/`, `data/`, and `tests/` for FD002-related files and references using the required terms. The generated audit tables are:

- `outputs/cmapss_fd002/existing_state_audit/FD002_artifact_inventory.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_dataset_inventory.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_dataset_lineage.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_stage_reconstruction.csv`
- `outputs/cmapss_fd002/existing_state_audit/FD002_claim_audit.csv`

## 3. Inventory Summary

| category | count |
|---|---:|
| FD002-related artifacts inventoried | 86 |
| active design/context documents | 8 |
| execution summaries | 5 |
| review/audit/closure documents | 5 |
| closure documents | 2 |
| numerical output groups | 5 |
| orphaned artifacts | 1 |
| unsupported claims found in repository documents | 0 |
| prohibited claim classes explicitly checked | 1 |
| confirmed byte-level duplicate groups | 0 |
| context / supersession relationship groups reviewed | 3 |

The active evidence groups are BL150, BL175, Health Evidence v0, HI v0, and Phase B1 fixed-channel validation. Generic root `outputs/hi_v0/` artifacts are historical/non-FD002 context where matched by search terms, not authoritative FD002 evidence.

## 4. Reconstructed FD002 Timeline

1. FD002 dataset and schema context were documented.
2. Settings structure and operating-condition audits were completed.
3. Expected State target and RUL reference-window decisions were documented.
4. BL150 residual execution produced train residuals and diagnostics.
5. BL175 residual execution produced sensitivity residuals and diagnostics.
6. Phase A closure accepted residual evidence with documented conditions.
7. Health Evidence v0 was designed and executed from BL150/BL175 residuals.
8. HI v0 was designed, executed, and closure-reviewed.
9. Phase B1 fixed-channel validation was executed and independently reviewed.
10. No single consolidated FD002 closure document was found before this audit.

## 5. Stage-by-Stage Status

The detailed stage table is `FD002_stage_reconstruction.csv`.

| stage | status | key issue |
|---|---|---|
| Dataset onboarding / schema audit | COMPLETE_WITH_LIMITATIONS | Current dataset package is identifiable; historical dataset hashes were not recorded. |
| Expected State and residual execution | CLOSED | BL150/BL175 outputs and closure review exist; explicit FD002 source execution scripts were not found. |
| Health Evidence v0 | COMPLETE_WITH_LIMITATIONS | Outputs and frozen execution summary exist; 15% / 20% sensitivity remained pending. |
| HI v0 | CLOSED | Execution summary and closure review exist. |
| Phase B1 fixed-channel validation | CLOSED | Execution summary and diagnostic review exist; B2 was deferred. |
| Overall FD002 closure | COMPLETE_WITH_LIMITATIONS | Stage-level closure exists; consolidated closure should be created before future FD002 claims are broadened. |

## 6. Numerical Lineage Assessment

BL150 and BL175 residual train outputs exist at the reported paths and are treated as frozen historical outputs for this audit. Health Evidence v0, HI v0, and Phase B1 numerical outputs also exist and are hash-recorded in the inventory.

Lineage limitations:

- Historical execution records do not record FD002 dataset hashes.
- Explicit FD002 source execution script paths were not found in the current repository for BL150/BL175, Health Evidence v0, HI v0, or Phase B1.
- The five historical execution groups have document-level lineage only and medium lineage confidence in `FD002_dataset_lineage.csv`.
- Matching filenames and row counts are not treated as hash verification.
- No contradictory FD002 dataset copy was found under the repository data tree.

Repository evidence is internally coherent, but the historical executions are not fully reproducible from the currently recorded dataset-hash and source-script lineage. These limitations do not invalidate the historical outputs, but they require wording such as `SUPPORTED_WITH_LINEAGE_LIMITATION` for reproducibility claims.

## 7. Design / Execution / Review Distinctions

Design documents are not treated as proof of execution. Execution is accepted only where numerical outputs and execution summaries are present. Review or closure is accepted only where review, closure, or frozen execution-decision documents exist.

- BL150 / BL175: executed and reviewed through Phase A closure.
- Health Evidence v0: executed with frozen summary; review evidence is embedded in that summary.
- HI v0: executed and closure-reviewed.
- Phase B1: executed and diagnostic-reviewed.
- Health Assessment: not started in this audit and not completed by FD002 evidence.

## 8. Duplicate and Supersession Findings

The artifact inventory contains no confirmed byte-identical duplicate groups across the 86 audited artifact hashes. The three groups below are context / supersession relationship groups, not byte-level duplicate files.

| group | canonical artifact | older / related artifacts | finding |
|---|---|---|---|
| Health Evidence v0 | `docs/validation/framework_validation/FD002_health_evidence_v0_execution_summary.md` | `docs/research/FD002_health_evidence_research_brief.md` | Research brief is contextual; execution summary is authoritative for executed state. |
| HI v0 | `docs/validation/framework_validation/FD002_HI_v0_execution_summary.md` and closure review | `docs/design/hi_v0_design.md`, root `outputs/hi_v0/` | Root HI v0 materials are non-FD002 historical context. |
| Phase B1 | `Phase_B1_fixed_channel_execution_summary.md` and diagnostic review | Phase B1 CSV outputs | Summary/review are authoritative narrative; CSVs are numerical evidence. |

No files were deleted or modified as part of this duplicate audit.

## 9. Claim Audit

The detailed claim audit is `FD002_claim_audit.csv`.

Key verified claims:

- BL150 sensor_11 absolute-residual correlation with RUL_proxy: `-0.6090043819301661`; raw residual correlation: `-0.691596119241661`.
- BL175 sensor_11 absolute-residual correlation with RUL_proxy: `-0.6229008182517646`; raw residual correlation: `-0.6911812248771092`.
- Evidence v0 primary channels: `sensor_11`, `sensor_4`, `sensor_15`.
- HI v0 median Spearman: BL150 `0.7583807420883869`, BL175 `0.7743753188563743`.
- HI v0 fraction_positive: `1.0`.
- Phase B1: poly3 and ridge are stable with Phase A; poly1 is an underfit / negative-control result.

Unsupported claim class:

- The audit explicitly checked the prohibited class `Marine validity / deployment readiness`.
- Unsupported claims found in repository documents: 0.
- FD002 does not establish Marine validity, Marine feasibility, Health Assessment completion, or deployment readiness.

The prohibited-claim boundary row in `FD002_claim_audit.csv` is a boundary-control check. It is not a discovered violation in an authoritative FD002 document.

## 9.1 HI Numeric State

HI numeric state:

`HI_NUMERIC_STATE_B: Two or more result sets exist and their metric definitions differ`

Canonical closure metric:

- Source file: `outputs/cmapss_fd002/hi_v0/CMAPSS_FD002_HI_v0_benchmark_summary.csv`
- Exact metric name: `median_spearman_hi`
- HI variant: `HI_primary_equal_uncentered`
- Channel set: primary Evidence v0 channels, equal uncentered HI
- Centering choice: uncentered
- Unit population: FD002 training units represented in the archived HI v0 benchmark
- Aggregation rule: median Spearman across units
- Filtering rule: benchmark-summary inclusion rules from HI v0 execution
- Document status: supported by frozen HI v0 execution summary and closure review
- Canonical BL150 value: `0.7583807420883869`
- Canonical BL175 value: `0.7743753188563743`

Other located HI v0 result sets are documented sensitivity or robustness variants:

- `HI_primary_equal_centered`: centered sensitivity variant.
- `HI_all_candidates_equal_uncentered`: all-candidate sensitivity variant.
- `HI_primary_equal_without_sensor_11`, `HI_primary_equal_without_sensor_4`, `HI_primary_equal_without_sensor_15`: leave-one-out robustness variants.

The searched value `0.766416` was found as a row-level HI timeseries value, not as a closure-level median Spearman. The searched value `0.780452` was found in a Phase B1 residual row, not as an HI v0 median Spearman. No repository-level numeric ambiguity remains for the canonical closure metric.

## 10. Historical Completion Claims and Dataset Identity

Historical completion memory was treated as a claim to verify, not as an audit premise.

| remembered item | verification result |
|---|---|
| FD002 Phase A + Option D CLOSED | VERIFIED_WITH_LIMITATIONS |
| sensor_11 absolute-residual correlations about -0.609 / -0.623 | VERIFIED |
| Evidence v0 primary channels sensor_11, sensor_4, sensor_15 | VERIFIED |
| HI v0 median Spearman about 0.758 / 0.774 | VERIFIED |
| HI v0 fraction_positive 1.000 | VERIFIED |
| Phase B1 poly3/ridge stable and poly1 negative control | VERIFIED |

Dataset identity:

- Current outer package: `data/cmapss/6_Turbofan_Engine_Degradation_Simulation_Data_Set.zip`
- Current outer SHA-256: `C9C5DEC12A945A82E8BB4446589D7FB3CC057B5E5D81FA1A12E25EE9912AD3B2`
- Current inner CMAPSSData.zip SHA-256: `74BEF434A34DB25C7BF72E668EA4CD52AFE5F2CF8E44367C55A82BFD91A5A34F`
- FD002 source files found inside the nested package: `train_FD002.txt`, `test_FD002.txt`, `RUL_FD002.txt`.
- Historical dataset hashes recorded in execution summaries: none found.
- Dataset identity conflict: none found.

The absence of historical dataset hashes is a lineage limitation. It is not, by itself, a contradiction because no competing FD002 source copy was found.

## 11. Open Gaps

| gap | severity | status |
|---|---|---|
| Historical dataset hashes missing from FD002 execution records | medium | LINEAGE_LIMITATION |
| Explicit FD002 execution script paths not found in current repository | medium | LINEAGE_LIMITATION |
| No single consolidated FD002 closure document found | medium | CLOSURE_GAP |
| Health Evidence v0 15% / 20% window sensitivity noted as pending | low / medium | DOCUMENTED_LIMITATION |
| Health Assessment not executed | scope boundary | NOT_A_DEFECT |

## 12. Recommended Next Action

Recommended next action: `CREATE_FD002_CLOSURE`.

Do not rerun BL150, BL175, Health Evidence v0, HI v0, or Phase B1 merely because they are historical. Existing evidence is authoritative as repository evidence with lineage limitations. A consolidated closure should state what is complete, what is limited by missing historical dataset hashes/source-script lineage, and what remains outside scope.

## 13. Final Audit Decision

Selected FD002 entry state:

`FD002_ENTRY_STATE_E: FD002_RESIDUAL_EVIDENCE_HI_AND_PHASE_B1_COMPLETE`

Decision rationale:

- Residual execution outputs exist for BL150 and BL175.
- Evidence v0 execution outputs exist.
- HI v0 execution outputs and closure review exist.
- Phase B1 execution outputs and diagnostic review exist.
- Major historical completion claims match current numerical artifacts.
- No FD002 dataset identity conflict was found.
- Missing historical dataset hashes and explicit source script paths are documented lineage limitations, not evidence contradictions.

Final audit decision:

`FD002_EXISTING_STATE_AUDIT_COMPLETE_WITH_LINEAGE_LIMITATIONS`

Boundary:

Public-data repository evidence only. No new FD002 execution. No Health Assessment execution. No Marine validity claimed.
