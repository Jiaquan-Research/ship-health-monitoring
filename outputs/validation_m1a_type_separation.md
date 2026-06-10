# Validation M-1A Type Separation

## 1. Protocol Reference

Protocol: `docs/review/m1a_type_separation_protocol_v0.1.md`

Diagnosis only.

No remediation was performed.

No new datasets were introduced.

No algorithm replacement is implied.

## 2. M-1A.1 Results

Model Capacity Probe targeting Type A.

| Model | Signal | Max Abs Spearman | Top Condition | Condition R2 |
|---|---|---:|---|---:|
| HVAC-v1 Frozen XGBoost | Residual_RMS | 0.7756 | OA_TEMP_WB | 0.4316 |
| HVAC-v1 Frozen XGBoost | HI_v0 | 0.7148 | CT_SW_TEMPSPT | 0.6881 |
| Random Forest diagnostic | Residual_RMS | 0.8293 | OA_TEMP_WB | 0.5531 |
| Random Forest diagnostic | HI_v0 | 0.7899 | OA_TEMP_WB | 0.7648 |
| Extra Trees diagnostic | Residual_RMS | 0.8505 | OA_TEMP_WB | 0.5872 |
| Extra Trees diagnostic | HI_v0 | 0.7549 | OA_TEMP_WB | 0.7793 |

Detailed condition correlations:

| Model | Signal | Condition | Spearman | Pearson |
|---|---|---|---:|---:|
| HVAC-v1 Frozen XGBoost | Residual_RMS | OA_TEMP_WB | 0.7756 | 0.4449 |
| HVAC-v1 Frozen XGBoost | Residual_RMS | OA_TEMP | 0.7633 | 0.4309 |
| HVAC-v1 Frozen XGBoost | Residual_RMS | CT_SW_TEMPSPT | 0.7573 | 0.4278 |
| HVAC-v1 Frozen XGBoost | Residual_RMS | CWL_PRI_SW_TEMPSPT | -0.7318 | -0.4399 |
| HVAC-v1 Frozen XGBoost | Residual_RMS | CWL_SEC_LOAD | 0.666 | 0.4159 |
| HVAC-v1 Frozen XGBoost | Residual_RMS | CWL_SEC_DPSPT | N/A | N/A |
| HVAC-v1 Frozen XGBoost | HI_v0 | CT_SW_TEMPSPT | 0.7148 | 0.4995 |
| HVAC-v1 Frozen XGBoost | HI_v0 | OA_TEMP | 0.6991 | 0.613 |
| HVAC-v1 Frozen XGBoost | HI_v0 | OA_TEMP_WB | 0.6942 | 0.595 |
| HVAC-v1 Frozen XGBoost | HI_v0 | CWL_PRI_SW_TEMPSPT | -0.6587 | -0.429 |
| HVAC-v1 Frozen XGBoost | HI_v0 | CWL_SEC_LOAD | 0.5398 | 0.2609 |
| HVAC-v1 Frozen XGBoost | HI_v0 | CWL_SEC_DPSPT | N/A | N/A |
| Random Forest diagnostic | Residual_RMS | OA_TEMP_WB | 0.8293 | 0.5132 |
| Random Forest diagnostic | Residual_RMS | OA_TEMP | 0.8146 | 0.4866 |
| Random Forest diagnostic | Residual_RMS | CT_SW_TEMPSPT | 0.766 | 0.4571 |
| Random Forest diagnostic | Residual_RMS | CWL_PRI_SW_TEMPSPT | -0.7524 | -0.508 |
| Random Forest diagnostic | Residual_RMS | CWL_SEC_LOAD | 0.6235 | 0.4255 |
| Random Forest diagnostic | Residual_RMS | CWL_SEC_DPSPT | N/A | N/A |
| Random Forest diagnostic | HI_v0 | OA_TEMP_WB | 0.7899 | 0.677 |
| Random Forest diagnostic | HI_v0 | OA_TEMP | 0.7818 | 0.6653 |
| Random Forest diagnostic | HI_v0 | CT_SW_TEMPSPT | 0.7375 | 0.5414 |
| Random Forest diagnostic | HI_v0 | CWL_PRI_SW_TEMPSPT | -0.7085 | -0.5497 |
| Random Forest diagnostic | HI_v0 | CWL_SEC_LOAD | 0.5449 | 0.3282 |
| Random Forest diagnostic | HI_v0 | CWL_SEC_DPSPT | N/A | N/A |
| Extra Trees diagnostic | Residual_RMS | OA_TEMP_WB | 0.8505 | 0.5224 |
| Extra Trees diagnostic | Residual_RMS | OA_TEMP | 0.8381 | 0.5042 |
| Extra Trees diagnostic | Residual_RMS | CT_SW_TEMPSPT | 0.7872 | 0.4948 |
| Extra Trees diagnostic | Residual_RMS | CWL_PRI_SW_TEMPSPT | -0.7592 | -0.5174 |
| Extra Trees diagnostic | Residual_RMS | CWL_SEC_LOAD | 0.62 | 0.4386 |
| Extra Trees diagnostic | Residual_RMS | CWL_SEC_DPSPT | N/A | N/A |
| Extra Trees diagnostic | HI_v0 | OA_TEMP_WB | 0.7549 | 0.6229 |
| Extra Trees diagnostic | HI_v0 | OA_TEMP | 0.7522 | 0.6367 |
| Extra Trees diagnostic | HI_v0 | CT_SW_TEMPSPT | 0.7286 | 0.519 |
| Extra Trees diagnostic | HI_v0 | CWL_PRI_SW_TEMPSPT | -0.6786 | -0.4614 |
| Extra Trees diagnostic | HI_v0 | CWL_SEC_LOAD | 0.5123 | 0.2118 |
| Extra Trees diagnostic | HI_v0 | CWL_SEC_DPSPT | N/A | N/A |

## 3. M-1A.2 Results

Cross-season Transfer Probe targeting Type C.

| Train | Test | Train Rows | Test Rows | R2 | Residual Mean | Residual Std | Residual RMS | Abs Residual Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Winter | Winter | 129,540 | 129,540 | 0.9984 | 7.879e-07 | 0.03988 | 0.03988 | 0.01692 |
| Summer | Summer | 132,480 | 132,480 | 0.9977 | 2.574e-06 | 0.0475 | 0.0475 | 0.02687 |
| Winter | Summer | 129,540 | 132,480 | -2.214 | 9.321 | 5.415 | 10.78 | 9.346 |
| Summer | Winter | 132,480 | 129,540 | -3.036 | -0.2931 | 0.1603 | 0.3341 | 0.2953 |

Correlation structure for cross-season residual magnitude:

| Train | Test | Condition | Spearman | Pearson |
|---|---|---|---:|---:|
| Winter | Winter | OA_TEMP | -0.2332 | -0.1294 |
| Winter | Winter | OA_TEMP_WB | -0.2311 | -0.1291 |
| Winter | Winter | CWL_SEC_LOAD | -0.141 | 0.03217 |
| Winter | Winter | CT_SW_TEMPSPT | 0.004847 | -0.001439 |
| Winter | Winter | CWL_PRI_SW_TEMPSPT | N/A | 8.383e-17 |
| Winter | Winter | CWL_SEC_DPSPT | N/A | -8.383e-17 |
| Summer | Summer | CWL_SEC_LOAD | -0.244 | -0.2089 |
| Summer | Summer | OA_TEMP_WB | -0.1503 | -0.08272 |
| Summer | Summer | CWL_PRI_SW_TEMPSPT | 0.1466 | 0.0737 |
| Summer | Summer | CT_SW_TEMPSPT | -0.1285 | -0.0496 |
| Summer | Summer | OA_TEMP | -0.1212 | -0.03559 |
| Summer | Summer | CWL_SEC_DPSPT | N/A | N/A |
| Winter | Summer | CT_SW_TEMPSPT | 0.9887 | 0.987 |
| Winter | Summer | OA_TEMP | 0.9857 | 0.9689 |
| Winter | Summer | OA_TEMP_WB | 0.8371 | 0.8476 |
| Winter | Summer | CWL_PRI_SW_TEMPSPT | -0.8257 | -0.8345 |
| Winter | Summer | CWL_SEC_LOAD | 0.6302 | 0.5838 |
| Winter | Summer | CWL_SEC_DPSPT | N/A | N/A |
| Summer | Winter | OA_TEMP | -0.994 | -0.9873 |
| Summer | Winter | OA_TEMP_WB | -0.9877 | -0.9831 |
| Summer | Winter | CWL_SEC_LOAD | -0.097 | -0.06395 |
| Summer | Winter | CT_SW_TEMPSPT | -0.0666 | -0.04663 |
| Summer | Winter | CWL_PRI_SW_TEMPSPT | N/A | -4.078e-17 |
| Summer | Winter | CWL_SEC_DPSPT | N/A | 4.078e-17 |

## 4. M-1A.3 Inventory

Missing Variable Inventory targeting Type B.

| Candidate Category | Present In Raw Data | Matching Columns | In HVAC-v1 |
|---|---|---|---|
| humidity | False | None found | None |
| wet-bulb temperature | True | OA_TEMP_WB | OA_TEMP_WB |
| solar radiation | False | None found | None |
| time features | False | None found | None |
| other outdoor air variables | True | OA_TEMP, OA_TEMP_WB | OA_TEMP, OA_TEMP_WB |
| load variables | True | CWL_SEC_LOAD | CWL_SEC_LOAD |
| setpoint variables | True | CT_SW_TEMPSPT, CWL_PRI_SW_TEMPSPT, CWL_SEC_DPSPT | CT_SW_TEMPSPT, CWL_PRI_SW_TEMPSPT, CWL_SEC_DPSPT |

## 5. Evidence Ranking

| Type | Evidence Strength | Basis |
|---|---|---|
| Type A | Not supported | Signal-wise diagnostic condition R2 comparison: Residual_RMS: HVAC-v1 R2=0.4316, best diagnostic R2=0.5531, reduction=-0.1214; HI_v0: HVAC-v1 R2=0.6881, best diagnostic R2=0.7648, reduction=-0.07675. Higher capacity does not substantially reduce leakage if this value is small. |
| Type C | Strong | Mean same-season R2=0.9981, mean cross-season R2=-2.625, gap=3.623. |
| Type B | Moderate | Potentially relevant categories absent from HVAC-v1: humidity, solar radiation, time features |

## 6. Dominance Assessment

Dominant mechanism: Type C.

Multiple mechanisms may coexist.

## 7. Verdict

Diagnosis complete.

Dominant or high-priority leakage mechanisms became clearer.

## 8. Implications

No remediation path is assumed.

No algorithm changes are implied.

No evidence levels are upgraded.

M-1A is diagnostic only.

## 9. Visualizations

* `outputs\validation_m1a_model_capacity.png`
* `outputs\validation_m1a_cross_season_transfer.png`
* `outputs\validation_m1a_seasonal_summary.png`
* `outputs\validation_m1a_missing_variable_inventory.png`
