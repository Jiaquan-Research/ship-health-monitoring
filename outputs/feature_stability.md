# Feature Stability Audit

## January

| feature | correlation | abs_correlation |
| --- | --- | --- |
| CHL_COMP_SPD_CTRL_1 | 0.99667 | 0.99667 |
| CWL_PRI_RW_TEMP | 0.992018 | 0.992018 |
| CHL_RW_TEMP_1 | 0.99196 | 0.99196 |
| CWL_SEC_SW_TEMP | 0.991903 | 0.991903 |
| CWL_SEC_RW_TEMP | 0.986076 | 0.986076 |
| CT_RW_TEMP_1 | 0.984402 | 0.984402 |
| CHL_SWCD_TEMP_1 | 0.984379 | 0.984379 |
| CDWL_RW_TEMP | 0.984308 | 0.984308 |
| CHL_SW_TEMP_1 | -0.956381 | 0.956381 |
| CWL_PRI_SW_TEMP | -0.95635 | 0.95635 |

## June

| feature | correlation | abs_correlation |
| --- | --- | --- |
| CHL_COMP_SPD_CTRL_1 | 0.992856 | 0.992856 |
| CWL_SEC_LOAD | 0.904075 | 0.904075 |
| CT_FAN_SPD_1 | 0.882288 | 0.882288 |
| CT_FAN_SPD_CTRL_1 | 0.882288 | 0.882288 |
| CHL_SWCD_TEMP_1 | 0.877337 | 0.877337 |
| CT_RW_TEMP_1 | 0.875756 | 0.875756 |
| CDWL_RW_TEMP | 0.875698 | 0.875698 |
| CT_POW_1 | 0.862375 | 0.862375 |
| CDWL_SW_TEMP | 0.753098 | 0.753098 |
| CHL_RWCD_TEMP_1 | 0.752904 | 0.752904 |

## December

| feature | correlation | abs_correlation |
| --- | --- | --- |
| CHL_RWCD_TEMP_1 | 0.996534 | 0.996534 |
| CDWL_SW_TEMP | 0.996469 | 0.996469 |
| CHL_SWCD_TEMP_1 | 0.99191 | 0.99191 |
| CDWL_RW_TEMP | 0.991861 | 0.991861 |
| CT_RW_TEMP_1 | 0.991328 | 0.991328 |
| CHL_COMP_SPD_CTRL_1 | -0.973157 | 0.973157 |
| CWL_SEC_RW_TEMP | -0.273703 | 0.273703 |
| CWL_SEC_SW_TEMP | -0.265014 | 0.265014 |
| CWL_PRI_SW_TEMP | -0.261556 | 0.261556 |
| CWL_SEC_DP | 0.205631 | 0.205631 |

## Overlap Summary

- Common variables across January, June, and December: 4
- Common variables: CDWL_RW_TEMP, CHL_COMP_SPD_CTRL_1, CHL_SWCD_TEMP_1, CT_RW_TEMP_1
- Variables appearing in at least one seasonal top 10: 17

## Drift

- January: CHL_RW_TEMP_1, CHL_SW_TEMP_1, CWL_PRI_RW_TEMP, CWL_PRI_SW_TEMP, CWL_SEC_RW_TEMP, CWL_SEC_SW_TEMP
- June: CDWL_SW_TEMP, CHL_RWCD_TEMP_1, CT_FAN_SPD_1, CT_FAN_SPD_CTRL_1, CT_POW_1, CWL_SEC_LOAD
- December: CDWL_SW_TEMP, CHL_RWCD_TEMP_1, CWL_PRI_SW_TEMP, CWL_SEC_DP, CWL_SEC_RW_TEMP, CWL_SEC_SW_TEMP

## Answer

Dominant predictors drift substantially across the year.