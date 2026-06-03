# Feature Groups

Heuristic classification for all baseline columns after status-column removal.

## Summary

| group | count |
| --- | --- |
| Condition Candidates | 7 |
| Control Candidates | 7 |
| Leakage Risk Features | 13 |
| State Candidates | 43 |

## Condition Candidates

| feature | group | abs_correlation_to_CHL_POW_1 | mi_rank |
| --- | --- | --- | --- |
| Datetime | Condition Candidates |  |  |
| CT_SW_TEMPSPT | Condition Candidates | 0.709323 | 43 |
| CWL_PRI_SW_TEMPSPT | Condition Candidates | 0.776666 | 44 |
| CWL_SEC_DPSPT | Condition Candidates | 2.7914e-17 | 49 |
| CWL_SEC_LOAD | Condition Candidates | 0.927798 | 27 |
| OA_TEMP | Condition Candidates | 0.583326 | 21 |
| OA_TEMP_WB | Condition Candidates | 0.632768 | 25 |

## State Candidates

| feature | group | abs_correlation_to_CHL_POW_1 | mi_rank |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | State Candidates | 0.677835 | 47 |
| CDWL_PM_POW_1 | State Candidates | 0.619781 | 17 |
| CDWL_PM_POW_2 | State Candidates | 0.68817 | 53 |
| CDWL_PM_POW_3 | State Candidates | 0.131225 | 61 |
| CHL_CD_FLOW_1 | State Candidates | 0.0299306 | 48 |
| CHL_CD_FLOW_2 | State Candidates | 0.687725 | 50 |
| CHL_CD_FLOW_3 | State Candidates | 0.130844 | 51 |
| CHL_CW_FLOW_1 | State Candidates | 0.0299301 | 46 |
| CHL_CW_FLOW_2 | State Candidates | 0.687725 | 59 |
| CHL_CW_FLOW_3 | State Candidates | 0.130844 | 60 |
| CHL_POW_1 | State Candidates |  |  |
| CHL_POW_2 | State Candidates | 0.746046 | 52 |
| CHL_POW_3 | State Candidates | 0.130547 | 64 |
| CHL_RW_TEMP_1 | State Candidates | 0.0989816 | 31 |
| CHL_RWCD_TEMP_2 | State Candidates | 0.354752 | 13 |
| CHL_RWCD_TEMP_3 | State Candidates | 0.393991 | 14 |
| CHL_SW_TEMP_1 | State Candidates | 0.74494 | 35 |
| CT_FAN_SPD_2 | State Candidates | 0.708219 | 56 |
| CT_FAN_SPD_3 | State Candidates | 0.128064 | 55 |
| CT_FLOW_1 | State Candidates | 0.614566 | 24 |
| CT_FLOW_2 | State Candidates | 0.687365 | 16 |
| CT_FLOW_3 | State Candidates | 0.130323 | 15 |
| CT_POW_2 | State Candidates | 0.698495 | 67 |
| CT_POW_3 | State Candidates | 0.111377 | 57 |
| CT_RW_TEMP_2 | State Candidates | 0.677881 | 36 |
| CT_RW_TEMP_3 | State Candidates | 0.328802 | 37 |
| CT_SW_TEMP_1 | State Candidates | 0.787334 | 28 |
| CT_SW_TEMP_2 | State Candidates | 0.541518 | 38 |
| CT_SW_TEMP_3 | State Candidates | 0.348132 | 39 |
| CWL_PRI_CW_FLOW | State Candidates | 0.677835 | 45 |
| CWL_PRI_PM_POW_1 | State Candidates | 0.0323784 | 68 |
| CWL_PRI_PM_POW_2 | State Candidates | 0.688235 | 66 |
| CWL_PRI_PM_POW_3 | State Candidates | 0.131124 | 58 |
| CWL_PRI_RW_TEMP | State Candidates | 0.0991772 | 30 |
| CWL_PRI_SW_TEMP | State Candidates | 0.74469 | 34 |
| CWL_SEC_CW_FLOW | State Candidates | 0.217413 | 19 |
| CWL_SEC_DP | State Candidates | 0.12575 | 29 |
| CWL_SEC_PM_POW_1 | State Candidates | 0.211441 | 20 |
| CWL_SEC_PM_POW_2 | State Candidates | 0.174229 | 32 |
| CWL_SEC_PM_SPD_1 | State Candidates | 0.269837 | 18 |
| CWL_SEC_PM_SPD_2 | State Candidates | 0.272783 | 22 |
| CWL_SEC_RW_TEMP | State Candidates | 0.462132 | 23 |
| CWL_SEC_SW_TEMP | State Candidates | 0.42134 | 26 |

## Control Candidates

| feature | group | abs_correlation_to_CHL_POW_1 | mi_rank |
| --- | --- | --- | --- |
| CHL_COMP_SPD_CTRL_1 | Control Candidates | 0.993833 | 9 |
| CHL_COMP_SPD_CTRL_2 | Control Candidates | 0.742167 | 54 |
| CHL_COMP_SPD_CTRL_3 | Control Candidates | 0.130619 | 63 |
| CT_FAN_SPD_CTRL_1 | Control Candidates | 0.898775 | 41 |
| CT_FAN_SPD_CTRL_2 | Control Candidates | 0.708219 | 62 |
| CT_FAN_SPD_CTRL_3 | Control Candidates | 0.128064 | 65 |
| TWV_CTRL | Control Candidates | 0.532597 | 33 |

## Leakage Risk Features

| feature | group | abs_correlation_to_CHL_POW_1 | mi_rank |
| --- | --- | --- | --- |
| CDWL_RW_TEMP | Leakage Risk Features | 0.89005 | 11 |
| CDWL_SW_TEMP | Leakage Risk Features | 0.801928 | 8 |
| CHL_SWCD_TEMP_1 | Leakage Risk Features | 0.891052 | 10 |
| CHL_SWCD_TEMP_2 | Leakage Risk Features | 0.647576 | 6 |
| CHL_SWCD_TEMP_3 | Leakage Risk Features | 0.385964 | 5 |
| CHL_RW_TEMP_2 | Leakage Risk Features | 0.260501 | 4 |
| CHL_RW_TEMP_3 | Leakage Risk Features | 0.284158 | 3 |
| CHL_RWCD_TEMP_1 | Leakage Risk Features | 0.802008 | 7 |
| CHL_SW_TEMP_2 | Leakage Risk Features | 0.0489882 | 1 |
| CHL_SW_TEMP_3 | Leakage Risk Features | 0.166315 | 2 |
| CT_FAN_SPD_1 | Leakage Risk Features | 0.898775 | 40 |
| CT_POW_1 | Leakage Risk Features | 0.89479 | 42 |
| CT_RW_TEMP_1 | Leakage Risk Features | 0.890102 | 12 |
