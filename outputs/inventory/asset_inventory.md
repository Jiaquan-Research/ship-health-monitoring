# Asset Inventory

Flags are heuristic reference flags: `ACTIVE` means referenced by current documents or obviously current; `SUPERSEDED` means a later versioned file exists; `ORPHANED` means no reference was found and status is unclear.


## docs/frozen/

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/frozen/validation_c0_series.md | Validation C0 Series — FROZEN | Frozen — No further N-CMAPSS experiments planned | ACTIVE |

## docs/design/

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/design/b3a_temporal_resolution_design.md | Validation B3A: Temporal Resolution Feasibility Audit | Design Only | ACTIVE |
| docs/design/baseline_management_v0.2.md | Baseline Management v0.1 | v0.1 | ACTIVE |
| docs/design/hi_v0_design.md | HI_v0 Design Document |  | ACTIVE |
| docs/design/ncmapss_variable_mapping.md | N-CMAPSS Variable Mapping for Validation C0 |  | ACTIVE |
| docs/design/validation_d_protocol_v0.1.md | Validation D Protocol v0.1 | Protocol Ready — Awaiting Data | ACTIVE |

## docs/review/

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/review/.gitkeep | Project artifact. |  | ACTIVE |
| docs/review/attack_review_round1.md | Attack Review Round 1 |  | ACTIVE |
| docs/review/attack_review_round2.md | Attack Review Round 2 |  | ACTIVE |
| docs/review/attack_review_summary_v1.md | Attack Review Summary v1 | Review Layer Convergence | ACTIVE |
| docs/review/claim_registry_v0.1.md | Claim Registry v0.1 | Open to independent review | ACTIVE |
| docs/review/deep_research_attack_protocol_v0.1.md | Deep Research Attack Protocol v0.1 | Ready | ACTIVE |
| docs/review/falsification_protocol_v0.1.md | Falsification Protocol v0.1 | Open | ACTIVE |
| docs/review/i1_postmortem.md | Validation I-1 Postmortem | FAIL | ORPHANED |
| docs/review/independent_review_checklist_v0.1.md | Independent Review Checklist v0.1 | Open | ACTIVE |
| docs/review/m1_condition_leakage_protocol_v0.1.md | Validation M-1 Condition Leakage Audit Protocol | Pre-registered | ACTIVE |
| docs/review/m1_postmortem.md | Validation M-1 Postmortem | FAIL | ORPHANED |
| docs/review/m1a_type_separation_protocol_v0.1.md | Validation M-1A Type Separation Protocol | Pre-registered | ACTIVE |
| docs/review/negative_control_protocol_v0.1.md | Negative Control Protocol v0.1 | Pre-registered | ACTIVE |
| docs/review/reproducible_artifacts_policy.md | Reproducible Artifacts Policy |  | ORPHANED |

## docs/exploration/

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/exploration/battery_dataset_context_audit.md | Battery Dataset Context Audit (P0) | Audit only. | ACTIVE |
| docs/exploration/condition_normalization_notes.md | Condition Normalization Notes |  | ORPHANED |
| docs/exploration/dataset_audit_v0.1.md | Dataset Audit Protocol | v0.1 | ACTIVE |
| docs/exploration/dataset_cards/battery_nasa.md | Dataset Card: NASA Battery Dataset | Observation only. | ACTIVE |
| docs/exploration/dataset_cards/battery_oxford.md | Dataset Card: Oxford Battery Degradation Dataset 1 | Observation only. | ACTIVE |
| docs/exploration/dataset_cards/fd001.md | Dataset Card: C-MAPSS FD001 | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/fd002.md | Dataset Card: C-MAPSS FD002 | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/fd003.md | Dataset Card: C-MAPSS FD003 | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/fd004.md | Dataset Card: C-MAPSS FD004 | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/femto.md | Dataset Card: FEMTO Bearing Dataset | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/paderborn.md | Dataset Card: Paderborn Bearing Dataset | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/xjtu_sy.md | Dataset Card: XJTU-SY Bearing Dataset | Observation only. | ORPHANED |
| docs/exploration/dataset_cards/zema.md | Dataset Card: ZEMA Hydraulic Dataset | Observation only. | ORPHANED |
| docs/exploration/dataset_census_round1.md | Dataset Census Round 1 | Observation only. | ACTIVE |
| docs/exploration/dataset_zoo.md | Industrial Dataset Zoo |  | ORPHANED |
| docs/exploration/e2_battery_cross_regime_probe_v0.1.md | E-2 | v0.1 | ACTIVE |
| docs/exploration/e2_postmortem.md | E-2 Postmortem | Context Audit Pending. | ACTIVE |
| docs/exploration/experiment_zoo.md | Experiment Zoo | Completed | ORPHANED |
| docs/exploration/exploration_review_week1.md | Exploration Review — Week 1 | Periodic Review (Exploration Line) | ACTIVE |
| docs/exploration/method_zoo.md | Method Zoo |  | ORPHANED |
| docs/exploration/q0_global_vs_piecewise.md | Q0 | v0.1 | ACTIVE |
| docs/exploration/question_zoo.md | Question Zoo |  | ORPHANED |
| docs/exploration/README.md | Exploration Sandbox |  | ACTIVE |
| docs/exploration/regime_vocabulary_notes.md | Regime Vocabulary Notes | Reference notes only. | ACTIVE |
| docs/exploration/residual_health_notes.md | Residual ≠ Health: Exploratory Notes | Observation only. Not hypothesis. Not theory. Not evidence. | ACTIVE |

## docs/notes/

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/notes/mode_conditioned_structure_idea.md | Mode Conditioned Structure: |  | ORPHANED |

## docs/ root-level files

| File | Description | Status/version | Flag |
| --- | --- | --- | --- |
| docs/Adversarial Review & Next-Phase Roadmap - ship-health-monitoring.md | Adversarial Review & Next-Phase Roadmap: ship-health-monitoring |  | ORPHANED |
| docs/Baseline Management in Industrial PHM Systems-report.md | Baseline Management in Industrial PHM Systems |  | ACTIVE |
| docs/baseline_management_v0.1.docx | Word document artifact. |  | ACTIVE |
| docs/concept_paper_v0.4.md | Concept Paper v0.4 | Updated after Validation B2.1 | ACTIVE |
| docs/concept_paper_v0.6.docx | Word document artifact. |  | SUPERSEDED by `docs/concept_paper_v0.7.docx` |
| docs/concept_paper_v0.7.docx | Word document artifact. |  | ACTIVE |
| docs/marine_data_requirement_sheet_v0.2.docx | Word document artifact. |  | SUPERSEDED by `docs/marine_data_requirement_sheet_v0.3.docx` |
| docs/marine_data_requirement_sheet_v0.3.docx | Word document artifact. |  | ACTIVE |
| docs/ship_health_monitoring_concept_paper_v0.4.docx | Word document artifact. |  | SUPERSEDED by `docs/ship_health_monitoring_concept_paper_v0.8.docx` |
| docs/ship_health_monitoring_concept_paper_v0.5.docx | Word document artifact. |  | SUPERSEDED by `docs/ship_health_monitoring_concept_paper_v0.8.docx` |
| docs/ship_health_monitoring_concept_paper_v0.6.docx | Word document artifact. |  | SUPERSEDED by `docs/ship_health_monitoring_concept_paper_v0.8.docx` |
| docs/ship_health_monitoring_concept_paper_v0.7.docx | Word document artifact. |  | SUPERSEDED by `docs/ship_health_monitoring_concept_paper_v0.8.docx` |
| docs/ship_health_monitoring_concept_paper_v0.8.docx | Word document artifact. |  | ACTIVE |
| docs/validation_c0_series_summary.docx | Word document artifact. |  | ACTIVE |
| docs/validation_chain_v0.1.md | Validation Chain v0.1 (Frozen) | Frozen | ACTIVE |
| docs/Vocabulary for Multi-Regime Industrial Systems.md | Vocabulary for Multi-Regime Industrial Systems |  | ORPHANED |

## src/

| File | Description | Produced by / produces | Flag |
| --- | --- | --- | --- |
| src/b2_diagnosis.py | Python source script. | See script description | ACTIVE |
| src/data_audit.py | Python source script. | See script description | ACTIVE |
| src/exploratory_e1_cross_regime_probe.py | Runs exploratory cross-regime probe and writes exploratory report. | See script description | ORPHANED |
| src/exploratory_e2_battery_cross_regime_probe.py | Runs exploratory cross-regime probe and writes exploratory report. | See script description | ACTIVE |
| src/feature_audit.py | Python source script. | See script description | ACTIVE |
| src/hi_v0_validation.py | Python source script. | See script description | ACTIVE |
| src/ncmapss_c01_label_audit.py | Runs N-CMAPSS audit/validation helper and writes N-CMAPSS outputs. | See script description | ACTIVE |
| src/ncmapss_c02_groundtruth_aligned.py | Runs N-CMAPSS audit/validation helper and writes N-CMAPSS outputs. | See script description | ACTIVE |
| src/ncmapss_c0_surrogate_spike.py | Runs N-CMAPSS audit/validation helper and writes N-CMAPSS outputs. | See script description | ACTIVE |
| src/ncmapss_data_audit.py | Runs N-CMAPSS audit/validation helper and writes N-CMAPSS outputs. | See script description | ACTIVE |
| src/validation_b1_expected_state.py | Trains B1 expected-state models and writes residual baseline artifacts. | See script description | ACTIVE |
| src/validation_b21_corrected_severity.py | Runs corrected B2.1 severity validation and writes B2.1 outputs. | See script description | ACTIVE |
| src/validation_b2_residual_severity.py | Runs original B2 residual severity validation and writes B2 outputs. | See script description | ACTIVE |
| src/validation_b3a_temporal_resolution.py | Runs B3A temporal resolution audit and writes B3A outputs. | See script description | ACTIVE |
| src/validation_b4_residual_trend.py | Runs B4 residual trend audit and writes B4 outputs. | See script description | ACTIVE |
| src/validation_i1_negative_control.py | Executes Validation I-1 negative control and writes I-1 report/figures. | See script description | ORPHANED |
| src/validation_m1_condition_leakage.py | Executes M-1 condition-leakage audit and writes M-1 report/figures. | See script description | ORPHANED |
| src/validation_m1a_type_separation.py | Executes M-1A type-separation diagnostic and writes M-1A report/figures. | See script description | ORPHANED |

## outputs/

| File | Description | Produced by / produces | Flag |
| --- | --- | --- | --- |
| outputs/b21_all_targets.png | Figure output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/b21_rms_CHL_POW_1.png | Figure output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/b21_rms_CHL_RWCD_TEMP_1.png | Figure output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/b21_rms_CHL_SW_TEMP_1.png | Figure output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/b21_rms_CT_SW_TEMP_1.png | Figure output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/b2_all_targets_comparison.png | Figure output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/b2_diagnosis.md | Validation B2 Diagnosis | src/b2_diagnosis.py | ACTIVE |
| outputs/b2_rms_CHL_POW_1.png | Figure output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/b2_rms_CHL_RWCD_TEMP_1.png | Figure output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/b2_rms_CHL_SW_TEMP_1.png | Figure output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/b2_rms_CT_SW_TEMP_1.png | Figure output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/b3a_b1_results.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_b21_results.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_residual_stats.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_sample_counts.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_sampling_summary.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_sensitivity_retention.csv | CSV output artifact. | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b3a_temporal_resolution.md | Validation B3A: Temporal Resolution Feasibility Audit | src/validation_b3a_temporal_resolution.py | ACTIVE |
| outputs/b4_dataset_rows.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_monotonicity.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_raw_vs_hi_v0.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_residual_trend_audit.md | Validation B4: Residual Trend Audit | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_spearman.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_spearman_heatmap.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_step_no_reversal.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_metrics.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_path_CHL_POW_1.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_path_CHL_RWCD_TEMP_1.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_path_CHL_SW_TEMP_1.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_path_CT_SW_TEMP_1.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_strength.csv | CSV output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/b4_trend_strength.png | Figure output artifact. | src/validation_b4_residual_trend.py | ACTIVE |
| outputs/baseline_management_v0.1_updated.docx | Word document artifact. |  | ACTIVE |
| outputs/c02_sensor_groundtruth_ranking.csv | CSV output artifact. | src/ncmapss_c02_groundtruth_aligned.py | ACTIVE |
| outputs/claim_registry_v0.1.docx | Word document artifact. |  | SUPERSEDED by `outputs/claim_registry_v0.1_1.docx` |
| outputs/claim_registry_v0.1_1.docx | Word document artifact. |  | ACTIVE |
| outputs/doc_revision_log_20260606.md | Documentation Revision Log — 2026-06-06 |  | ACTIVE |
| outputs/exploratory_e1_cross_regime_probe.md | Exploratory E-1 Cross-Regime Probe | src/exploratory_e1_cross_regime_probe.py | ACTIVE |
| outputs/exploratory_e2_battery_cross_regime_probe.md | Exploratory E-2 Battery Cross-Regime Probe | src/exploratory_e2_battery_cross_regime_probe.py | ACTIVE |
| outputs/feature_audit.md | Feature Audit: Expected State Route | src/feature_audit.py | ACTIVE |
| outputs/feature_audit_correlation_plot.png | Figure output artifact. | src/feature_audit.py | ACTIVE |
| outputs/feature_audit_mi_top20.csv | CSV output artifact. | src/feature_audit.py | ACTIVE |
| outputs/feature_audit_pearson_top20.csv | CSV output artifact. | src/feature_audit.py | ACTIVE |
| outputs/feature_groups.md | Feature Groups | src/feature_audit.py | ACTIVE |
| outputs/feature_stability.md | Feature Stability Audit | src/feature_audit.py | ACTIVE |
| outputs/github_push_audit.md | GitHub Push Audit |  | ORPHANED |
| outputs/hi_v0/hi_v0_baseline_stats.csv | CSV output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_monotonicity.csv | CSV output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_sensitivity.csv | CSV output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_severity_CHL_POW_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_severity_CHL_RWCD_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_severity_CHL_SW_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_severity_CT_SW_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_severity_stats.csv | CSV output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_timeseries_CHL_POW_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_timeseries_CHL_RWCD_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_timeseries_CHL_SW_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_timeseries_CT_SW_TEMP_1_24h.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_validation.md | HI_v0 Rolling RMS Validation | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_vs_raw_residual.csv | CSV output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/hi_v0/hi_v0_window_sensitivity.png | Figure output artifact. | src/hi_v0_validation.py | ACTIVE |
| outputs/inventory/consistency_check.md | Document/Code Consistency Check |  | ORPHANED |
| outputs/inventory/number_provenance.md | Key Number Provenance Table |  | ORPHANED |
| outputs/inventory/timeline_full.md | Full Timeline Reconstruction |  | ORPHANED |
| outputs/lbnl_data_audit.md | LBNL Chiller Plant Data Audit | src/data_audit.py | ACTIVE |
| outputs/model_a_feature_importance_top20.csv | CSV output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_a_prediction.png | Figure output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_b_feature_importance.csv | CSV output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_b_prediction.png | Figure output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_c_feature_importance.csv | CSV output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_c_prediction.png | Figure output artifact. | src/feature_audit.py | ACTIVE |
| outputs/model_performance.csv | CSV output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/model_performance.md | Expected State Model Performance | src/validation_b1_expected_state.py | ACTIVE |
| outputs/ncmapss_c01_label_audit.md | Validation C0.1 — T_dev Label Audit | src/ncmapss_c01_label_audit.py | ACTIVE |
| outputs/ncmapss_c02_groundtruth_aligned.md | Validation C0.2 — Ground Truth Aligned Rerun | src/ncmapss_c02_groundtruth_aligned.py | ACTIVE |
| outputs/ncmapss_c02_unit_16.png | Figure output artifact. | src/ncmapss_c02_groundtruth_aligned.py | ACTIVE |
| outputs/ncmapss_c02_unit_2.png | Figure output artifact. | src/ncmapss_c02_groundtruth_aligned.py | ACTIVE |
| outputs/ncmapss_c02_unit_5.png | Figure output artifact. | src/ncmapss_c02_groundtruth_aligned.py | ACTIVE |
| outputs/ncmapss_c0_surrogate_spike.md | Validation C0 — N-CMAPSS Surrogate Spike | src/ncmapss_c0_surrogate_spike.py | ACTIVE |
| outputs/ncmapss_c0_unit_16.png | Figure output artifact. | src/ncmapss_c0_surrogate_spike.py | ACTIVE |
| outputs/ncmapss_c0_unit_2.png | Figure output artifact. | src/ncmapss_c0_surrogate_spike.py | ACTIVE |
| outputs/ncmapss_c0_unit_5.png | Figure output artifact. | src/ncmapss_c0_surrogate_spike.py | ACTIVE |
| outputs/ncmapss_data_audit.md | N-CMAPSS Data Audit | src/ncmapss_data_audit.py | ACTIVE |
| outputs/repository_audit.md | Repository Audit |  | ACTIVE |
| outputs/repository_structure.md | Repository Structure Review |  | ORPHANED |
| outputs/residual_baseline.md | Residual Baseline Analysis | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_distribution_CHL_POW_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_distribution_CHL_RWCD_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_distribution_CHL_SW_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_distribution_CT_SW_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_statistics.csv | CSV output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/residual_timeseries_CHL_POW_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_timeseries_CHL_RWCD_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_timeseries_CHL_SW_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residual_timeseries_CT_SW_TEMP_1.png | Figure output artifact. | src/validation_b1_expected_state.py | ACTIVE |
| outputs/residuals_normal.csv | CSV output artifact. | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/review_package_github_audit.md | Review Package GitHub Audit |  | ORPHANED |
| outputs/review_package_github_audit_round2.md | Review Package GitHub Audit Round 2 |  | ORPHANED |
| outputs/validation_b2.md | Validation B2: Residual Severity Analysis | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/validation_b21.md | Validation B2.1: Corrected Severity Ordering | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/validation_b21_filtering.csv | CSV output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/validation_b21_monotonicity.csv | CSV output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/validation_b21_residual_statistics.csv | CSV output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/validation_b21_sensitivity.csv | CSV output artifact. | src/validation_b21_corrected_severity.py | ACTIVE |
| outputs/validation_b2_filtering.csv | CSV output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/validation_b2_monotonicity.csv | CSV output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/validation_b2_residual_statistics.csv | CSV output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/validation_b2_sensitivity.csv | CSV output artifact. | src/validation_b2_residual_severity.py | ACTIVE |
| outputs/validation_i1_conditions_overlay.png | Figure output artifact. | src/validation_i1_negative_control.py | ACTIVE |
| outputs/validation_i1_hi_v0_full.png | Figure output artifact. | src/validation_i1_negative_control.py | ACTIVE |
| outputs/validation_i1_negative_control.md | Validation I-1 Negative Control | src/validation_i1_negative_control.py | ACTIVE |
| outputs/validation_i1_residual_rms.png | Figure output artifact. | src/validation_i1_negative_control.py | ACTIVE |
| outputs/validation_i1_summary_stats.png | Figure output artifact. | src/validation_i1_negative_control.py | ACTIVE |
| outputs/validation_m1_condition_leakage.md | Validation M-1 Condition Leakage Audit | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/validation_m1_hi_condition_corr.png | Figure output artifact. | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/validation_m1_r2_summary.png | Figure output artifact. | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/validation_m1_residual_condition_corr.png | Figure output artifact. | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/validation_m1_seasonal_comparison.png | Figure output artifact. | src/validation_m1_condition_leakage.py | ACTIVE |
| outputs/validation_m1a_cross_season_transfer.png | Figure output artifact. | src/validation_m1a_type_separation.py | ACTIVE |
| outputs/validation_m1a_missing_variable_inventory.png | Figure output artifact. | src/validation_m1a_type_separation.py | ACTIVE |
| outputs/validation_m1a_model_capacity.png | Figure output artifact. | src/validation_m1a_type_separation.py | ACTIVE |
| outputs/validation_m1a_seasonal_summary.png | Figure output artifact. | src/validation_m1a_type_separation.py | ACTIVE |
| outputs/validation_m1a_type_separation.md | Validation M-1A Type Separation | src/validation_m1a_type_separation.py | ACTIVE |
