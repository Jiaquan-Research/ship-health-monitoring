# Repository Structure Review

Date: 2026-06-09

## Required Structure Check

| Path | Exists | File Count |
|---|---:|---:|
| `docs/concept/` | True | 1 |
| `docs/design/` | True | 5 |
| `docs/frozen/` | True | 1 |
| `docs/review/` | True | 1 |
| `src/` | True | 17 |
| `outputs/` | True | 100 |
| `data/` | True | 39 |

## Current Tree (depth 2, excluding `.git`, `.venv`, and data contents)

```
docs/
  concept/
    .gitkeep
  design/
    b3a_temporal_resolution_design.md
    baseline_management_v0.2.md
    hi_v0_design.md
    ncmapss_variable_mapping.md
    validation_d_protocol_v0.1.md
  frozen/
    validation_c0_series.md
  review/
    .gitkeep
  Baseline Management in Industrial PHM Systems-report.md
  baseline_management_v0.1.docx
  concept_paper_v0.4.md
  concept_paper_v0.6.docx
  concept_paper_v0.7.docx
  marine_data_requirement_sheet_v0.2.docx
  marine_data_requirement_sheet_v0.3.docx
  ship_health_monitoring_concept_paper_v0.4.docx
  ship_health_monitoring_concept_paper_v0.5.docx
  ship_health_monitoring_concept_paper_v0.6.docx
  ship_health_monitoring_concept_paper_v0.7.docx
  ship_health_monitoring_concept_paper_v0.8.docx
  validation_c0_series_summary.docx
  validation_chain_v0.1.md
notebooks/
outputs/
  docx_render_check/
    baseline_management_v01_updated/
    claim_registry_v01/
    concept_paper_v07/
    concept_v08/
  hi_v0/
    hi_v0_baseline_stats.csv
    hi_v0_monotonicity.csv
    hi_v0_sensitivity.csv
    hi_v0_severity_CHL_POW_1_24h.png
    hi_v0_severity_CHL_RWCD_TEMP_1_24h.png
    hi_v0_severity_CHL_SW_TEMP_1_24h.png
    hi_v0_severity_CT_SW_TEMP_1_24h.png
    hi_v0_severity_stats.csv
    hi_v0_timeseries_CHL_POW_1_24h.png
    hi_v0_timeseries_CHL_RWCD_TEMP_1_24h.png
    hi_v0_timeseries_CHL_SW_TEMP_1_24h.png
    hi_v0_timeseries_CT_SW_TEMP_1_24h.png
    hi_v0_validation.md
    hi_v0_vs_raw_residual.csv
    hi_v0_window_sensitivity.png
  b21_all_targets.png
  b21_rms_CHL_POW_1.png
  b21_rms_CHL_RWCD_TEMP_1.png
  b21_rms_CHL_SW_TEMP_1.png
  b21_rms_CT_SW_TEMP_1.png
  b2_all_targets_comparison.png
  b2_diagnosis.md
  b2_rms_CHL_POW_1.png
  b2_rms_CHL_RWCD_TEMP_1.png
  b2_rms_CHL_SW_TEMP_1.png
  b2_rms_CT_SW_TEMP_1.png
  b3a_b1_results.csv
  b3a_b21_results.csv
  b3a_residual_stats.csv
  b3a_sample_counts.csv
  b3a_sampling_summary.csv
  b3a_sensitivity_retention.csv
  b3a_temporal_resolution.md
  b4_dataset_rows.csv
  b4_monotonicity.csv
  b4_raw_vs_hi_v0.csv
  b4_residual_trend_audit.md
  b4_spearman.csv
  b4_spearman_heatmap.png
  b4_step_no_reversal.csv
  b4_trend_metrics.csv
  b4_trend_path_CHL_POW_1.png
  b4_trend_path_CHL_RWCD_TEMP_1.png
  b4_trend_path_CHL_SW_TEMP_1.png
  b4_trend_path_CT_SW_TEMP_1.png
  b4_trend_strength.csv
  b4_trend_strength.png
  baseline_management_v0.1_updated.docx
  c02_sensor_groundtruth_ranking.csv
  claim_registry_v0.1.docx
  claim_registry_v0.1_1.docx
  doc_revision_log_20260606.md
  feature_audit.md
  feature_audit_correlation_plot.png
  feature_audit_mi_top20.csv
  feature_audit_pearson_top20.csv
  feature_groups.md
  feature_stability.md
  lbnl_data_audit.md
  model_a_feature_importance_top20.csv
  model_a_prediction.png
  model_b_feature_importance.csv
  model_b_prediction.png
  model_c_feature_importance.csv
  model_c_prediction.png
  model_performance.csv
  model_performance.md
  ncmapss_c01_label_audit.md
  ncmapss_c02_groundtruth_aligned.md
  ncmapss_c02_unit_16.png
  ncmapss_c02_unit_2.png
  ncmapss_c02_unit_5.png
  ncmapss_c0_surrogate_spike.md
  ncmapss_c0_unit_16.png
  ncmapss_c0_unit_2.png
  ncmapss_c0_unit_5.png
  ncmapss_data_audit.md
  repository_audit.md
  repository_structure.md
  residual_baseline.md
  residual_distribution_CHL_POW_1.png
  residual_distribution_CHL_RWCD_TEMP_1.png
  residual_distribution_CHL_SW_TEMP_1.png
  residual_distribution_CT_SW_TEMP_1.png
  residual_statistics.csv
  residual_timeseries_CHL_POW_1.png
  residual_timeseries_CHL_RWCD_TEMP_1.png
  residual_timeseries_CHL_SW_TEMP_1.png
  residual_timeseries_CT_SW_TEMP_1.png
  residuals_normal.csv
  validation_b2.md
  validation_b21.md
  validation_b21_filtering.csv
  validation_b21_monotonicity.csv
  validation_b21_residual_statistics.csv
  validation_b21_sensitivity.csv
  validation_b2_filtering.csv
  validation_b2_monotonicity.csv
  validation_b2_residual_statistics.csv
  validation_b2_sensitivity.csv
scripts/
src/
  condition_normalization/
  cusum/
  expected_state_model/
    esm_CHL_POW_1.joblib
    esm_CHL_RWCD_TEMP_1.joblib
    esm_CHL_SW_TEMP_1.joblib
    esm_CT_SW_TEMP_1.joblib
  health_index/
  residual/
  b2_diagnosis.py
  data_audit.py
  feature_audit.py
  hi_v0_validation.py
  ncmapss_c01_label_audit.py
  ncmapss_c02_groundtruth_aligned.py
  ncmapss_c0_surrogate_spike.py
  ncmapss_data_audit.py
  validation_b1_expected_state.py
  validation_b21_corrected_severity.py
  validation_b2_residual_severity.py
  validation_b3a_temporal_resolution.py
  validation_b4_residual_trend.py
tests/
.gitignore
CLAUDE.md
README.md
SYSTEM_STATE.md
```

## Review Layer Audit

- `docs/review/`: True
- `docs/review/claim_registry_v0.1.md`: False

Missing review files (reported only; not created):
- `D:/ship-health-monitoring/docs/review/falsification_protocol_v0.1.md`
- `D:/ship-health-monitoring/docs/review/independent_review_checklist_v0.1.md`
