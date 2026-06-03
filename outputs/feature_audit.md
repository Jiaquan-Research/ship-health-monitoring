# Feature Audit: Expected State Route

## 1. Dataset Summary

- Source file: `data\lbnl\ChillerPlant.csv`
- Total rows loaded: 525,540
- Total columns loaded, including Datetime: 78
- Target: `CHL_POW_1`

## 2. Filtering Summary

- Rows before filtering: 525,540
- Rows after `CHL_STA_1 != 0`: 525,540
- Percentage retained: 100.00%
- Dropped status/control-state columns: CHL_STA_1, CHL_STA_2, CHL_STA_3, CT_STA_1, CT_STA_2, CT_STA_3, CWL_SEC_PM_STA_1, CWL_SEC_PM_STA_2

## 3. Pearson Top 20

| feature | correlation | abs_correlation |
| --- | --- | --- |
| CHL_COMP_SPD_CTRL_1 | 0.993833 | 0.993833 |
| CWL_SEC_LOAD | 0.927798 | 0.927798 |
| CT_FAN_SPD_CTRL_1 | 0.898775 | 0.898775 |
| CT_FAN_SPD_1 | 0.898775 | 0.898775 |
| CT_POW_1 | 0.89479 | 0.89479 |
| CHL_SWCD_TEMP_1 | 0.891052 | 0.891052 |
| CT_RW_TEMP_1 | 0.890102 | 0.890102 |
| CDWL_RW_TEMP | 0.89005 | 0.89005 |
| CHL_RWCD_TEMP_1 | 0.802008 | 0.802008 |
| CDWL_SW_TEMP | 0.801928 | 0.801928 |
| CT_SW_TEMP_1 | 0.787334 | 0.787334 |
| CWL_PRI_SW_TEMPSPT | -0.776666 | 0.776666 |
| CHL_POW_2 | 0.746046 | 0.746046 |
| CHL_SW_TEMP_1 | -0.74494 | 0.74494 |
| CWL_PRI_SW_TEMP | -0.74469 | 0.74469 |
| CHL_COMP_SPD_CTRL_2 | 0.742167 | 0.742167 |
| CT_SW_TEMPSPT | 0.709323 | 0.709323 |
| CT_FAN_SPD_CTRL_2 | 0.708219 | 0.708219 |
| CT_FAN_SPD_2 | 0.708219 | 0.708219 |
| CT_POW_2 | 0.698495 | 0.698495 |

## 4. Mutual Information Top 20

- MI computed on first 100,000 filtered rows.

| feature | mutual_information |
| --- | --- |
| CHL_SW_TEMP_2 | 4.34333 |
| CHL_SW_TEMP_3 | 4.34317 |
| CHL_RW_TEMP_3 | 4.25856 |
| CHL_RW_TEMP_2 | 4.25838 |
| CHL_SWCD_TEMP_3 | 3.98704 |
| CHL_SWCD_TEMP_2 | 3.98702 |
| CHL_RWCD_TEMP_1 | 3.81357 |
| CDWL_SW_TEMP | 3.4094 |
| CHL_COMP_SPD_CTRL_1 | 3.23015 |
| CHL_SWCD_TEMP_1 | 2.65263 |
| CDWL_RW_TEMP | 2.64495 |
| CT_RW_TEMP_1 | 2.59364 |
| CHL_RWCD_TEMP_2 | 0.881964 |
| CHL_RWCD_TEMP_3 | 0.881944 |
| CT_FLOW_3 | 0.84234 |
| CT_FLOW_2 | 0.842303 |
| CDWL_PM_POW_1 | 0.841 |
| CWL_SEC_PM_SPD_1 | 0.735979 |
| CWL_SEC_CW_FLOW | 0.723509 |
| CWL_SEC_PM_POW_1 | 0.55073 |

## 5. Model A Results

- Purpose: maximum achievable predictive performance using all non-target numeric features except chiller peer power leakage.
- Features used: 66
- R2: 0.999749
- RMSE: 0.273283
- Top 20 feature importances:

| feature | importance |
| --- | --- |
| CHL_COMP_SPD_CTRL_1 | 0.460358 |
| CWL_PRI_CW_FLOW | 0.242958 |
| CWL_SEC_LOAD | 0.197899 |
| CHL_SWCD_TEMP_1 | 0.0199974 |
| CHL_CD_FLOW_2 | 0.0187235 |
| CT_FLOW_2 | 0.0167854 |
| CT_POW_1 | 0.0140549 |
| CT_RW_TEMP_1 | 0.00573796 |
| CT_FAN_SPD_1 | 0.00497097 |
| CWL_PRI_RW_TEMP | 0.00396345 |
| CHL_COMP_SPD_CTRL_2 | 0.00373422 |
| CWL_SEC_SW_TEMP | 0.00287711 |
| CDWL_RW_TEMP | 0.00166846 |
| CT_SW_TEMP_1 | 0.000931357 |
| CT_SW_TEMPSPT | 0.000726835 |
| CWL_SEC_CW_FLOW | 0.000556268 |
| CT_POW_2 | 0.000512123 |
| CWL_PRI_SW_TEMPSPT | 0.000390387 |
| CWL_SEC_PM_SPD_1 | 0.000367486 |
| CWL_PRI_SW_TEMP | 0.000267958 |
- Prediction plot: `outputs/model_a_prediction.png`

## 6. Model B Results

- Purpose: test manually selected engineering Condition Variables.
- Features used: CWL_SEC_LOAD, OA_TEMP, OA_TEMP_WB, CWL_PRI_SW_TEMPSPT, CT_SW_TEMPSPT, CWL_SEC_DPSPT
- R2: 0.960733
- RMSE: 3.416953
- Feature importances:

| feature | importance |
| --- | --- |
| CWL_SEC_LOAD | 0.780613 |
| OA_TEMP_WB | 0.118272 |
| OA_TEMP | 0.0587327 |
| CT_SW_TEMPSPT | 0.0214984 |
| CWL_PRI_SW_TEMPSPT | 0.020884 |
| CWL_SEC_DPSPT | 0 |
- Prediction plot: `outputs/model_b_prediction.png`

## 7. Model C Results

- Purpose: compare engineering intuition against data-discovered predictors.
- Features used: CHL_SW_TEMP_2, CHL_SW_TEMP_3, CHL_RW_TEMP_3, CHL_RW_TEMP_2, CHL_SWCD_TEMP_3, CHL_SWCD_TEMP_2, CHL_RWCD_TEMP_1, CDWL_SW_TEMP, CHL_COMP_SPD_CTRL_1, CHL_SWCD_TEMP_1
- R2: 0.999793
- RMSE: 0.248233
- Feature importances:

| feature | importance |
| --- | --- |
| CHL_COMP_SPD_CTRL_1 | 0.981986 |
| CHL_SWCD_TEMP_1 | 0.0135599 |
| CDWL_SW_TEMP | 0.00212591 |
| CHL_RWCD_TEMP_1 | 0.00134953 |
| CHL_RW_TEMP_2 | 0.000353428 |
| CHL_SWCD_TEMP_3 | 0.000184025 |
| CHL_SW_TEMP_2 | 0.000174971 |
| CHL_SWCD_TEMP_2 | 0.000134071 |
| CHL_RW_TEMP_3 | 0.000103638 |
| CHL_SW_TEMP_3 | 2.80566e-05 |
- Prediction plot: `outputs/model_c_prediction.png`

## 8. Feature Stability Results

- Common seasonal top-10 variables: 4
- Common variables: CDWL_RW_TEMP, CHL_COMP_SPD_CTRL_1, CHL_SWCD_TEMP_1, CT_RW_TEMP_1
- Stability answer: Dominant predictors drift substantially across the year.
- Seasonal drift:
  - January: CHL_RW_TEMP_1, CHL_SW_TEMP_1, CWL_PRI_RW_TEMP, CWL_PRI_SW_TEMP, CWL_SEC_RW_TEMP, CWL_SEC_SW_TEMP
  - June: CDWL_SW_TEMP, CHL_RWCD_TEMP_1, CT_FAN_SPD_1, CT_FAN_SPD_CTRL_1, CT_POW_1, CWL_SEC_LOAD
  - December: CDWL_SW_TEMP, CHL_RWCD_TEMP_1, CWL_PRI_SW_TEMP, CWL_SEC_DP, CWL_SEC_RW_TEMP, CWL_SEC_SW_TEMP

## 9. Feature Classification Summary

| group | count |
| --- | --- |
| Condition Candidates | 7 |
| Control Candidates | 7 |
| Leakage Risk Features | 13 |
| State Candidates | 43 |

- Full classification: `outputs/feature_groups.md`
- Stability detail: `outputs/feature_stability.md`
- Correlation heatmap: `outputs/feature_audit_correlation_plot.png`

## 10. Interpretation

**Q1: Can Condition Variables alone predict `CHL_POW_1`?**

Model B R2 is 0.960733. Strong evidence that Condition Variables are sufficient.

**Q2: How much performance is lost compared to All Features?**

Model A R2 is 0.999749; Model B R2 is 0.960733. Absolute R2 loss is 0.039016. Model B RMSE is 12.50x Model A RMSE.

**Q3: Does engineering intuition agree with data-driven discovery?**

Model C R2 is 0.999793, compared with Model B R2 0.960733. Model C is close to Model B, so engineering variable selection is broadly aligned.

**Q4: Are discovered relationships stable throughout the year?**

Dominant predictors drift substantially across the year.

**Q5: Is the Expected State -> Residual route viable?**

The Expected State -> Residual route is viable for CHL_POW_1.