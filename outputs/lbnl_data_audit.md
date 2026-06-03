# LBNL Chiller Plant Data Audit

- Data directory: `D:\ship-health-monitoring\data\lbnl`
- CSV files found: 24

## ChillerPlant.csv

- Size: 409.5 MB (429,363,044 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.578 | 964.775 | 362.989 |
| CDWL_PM_POW_1 | 7.60929 | 141.965 | 23.501 |
| CDWL_PM_POW_2 | 0 | 135.491 | 5.79149 |
| CDWL_PM_POW_3 | 0 | 86.46 | 0.203992 |
| CDWL_RW_TEMP | 59.5756 | 94.7835 | 65.8038 |
| CDWL_SW_TEMP | 59.5267 | 85.7998 | 64.0885 |
| CHL_CD_FLOW_1 | 202.659 | 492.895 | 321.582 |
| CHL_CD_FLOW_2 | 0.000245415 | 412.667 | 40.0056 |
| CHL_CD_FLOW_3 | 0.000170286 | 321.589 | 1.40109 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152195 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0802652 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.0027075 |
| CHL_CW_FLOW_1 | 176.029 | 428.125 | 279.324 |
| CHL_CW_FLOW_2 | 0.000213166 | 358.44 | 34.7486 |
| CHL_CW_FLOW_3 | 0.00014791 | 279.33 | 1.21698 |
| CHL_POW_1 | 0 | 232.503 | 28.1798 |
| CHL_POW_2 | 0 | 225.902 | 15.1084 |
| CHL_POW_3 | 0 | 224.805 | 0.499459 |
| CHL_SWCD_TEMP_1 | 59.5756 | 94.7837 | 65.8094 |
| CHL_SWCD_TEMP_2 | 69.7193 | 94.486 | 75.1709 |
| CHL_SWCD_TEMP_3 | 73.9343 | 92.2133 | 79.5733 |
| CHL_RW_TEMP_1 | 42.4928 | 73.2186 | 53.5081 |
| CHL_RW_TEMP_2 | 42.2273 | 61.7249 | 49.2224 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9747 | 49.3614 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124413 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.573 | 86.213 | 64.2308 |
| CHL_RWCD_TEMP_2 | 66.2553 | 86.213 | 73.0065 |
| CHL_RWCD_TEMP_3 | 73.2734 | 86.202 | 76.8449 |
| CHL_SW_TEMP_1 | 42.3878 | 54.53 | 51.8873 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6955 | 46.5649 |
| CHL_SW_TEMP_3 | 42.0492 | 49.806 | 46.009 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205347 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0949906 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00285376 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205347 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0949906 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00285376 |
| CT_FLOW_1 | 3.48634 | 575.172 | 142.101 |
| CT_FLOW_2 | 2.866e-08 | 448.843 | 39.7842 |
| CT_FLOW_3 | 2.866e-08 | 320.538 | 1.39046 |
| CT_POW_1 | 0 | 9.99999 | 1.40169 |
| CT_POW_2 | 0 | 9.99999 | 0.655699 |
| CT_POW_3 | 0 | 9.99999 | 0.0147773 |
| CT_RW_TEMP_1 | 59.5757 | 94.7837 | 65.8038 |
| CT_RW_TEMP_2 | 68.7045 | 94.4859 | 73.6803 |
| CT_RW_TEMP_3 | 68.7045 | 93.4031 | 78.2484 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124413 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 52.8182 | 85.5446 | 62.1848 |
| CT_SW_TEMP_2 | 65.9535 | 85.5448 | 71.8334 |
| CT_SW_TEMP_3 | 69.6975 | 88.0187 | 76.0096 |
| CWL_PRI_CW_FLOW | 279.321 | 837.998 | 315.29 |
| CWL_PRI_PM_POW_1 | 5.96561 | 35.2881 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.0974 | 1.87006 |
| CWL_PRI_PM_POW_3 | 0 | 21.6653 | 0.0655926 |
| CWL_PRI_RW_TEMP | 42.4927 | 73.3141 | 53.5081 |
| CWL_PRI_SW_TEMP | 42.3877 | 54.5306 | 51.887 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 5.93421e-07 | 837.929 | 443.799 |
| CWL_SEC_DP | 529.004 | 979.552 | 956.517 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90611e+06 | 96029.3 |
| CWL_SEC_PM_POW_1 | 5.62839e-08 | 53.6388 | 24.8959 |
| CWL_SEC_PM_POW_2 | 0 | 51.7282 | 23.9039 |
| CWL_SEC_PM_SPD_1 | 0.344676 | 1.00238 | 0.709597 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.567994 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.63575 |
| CWL_SEC_RW_TEMP | 43.87 | 61.7642 | 52.0547 |
| CWL_SEC_SW_TEMP | 50.1453 | 73.1072 | 53.9739 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.780365 | 0.22897 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460156, 1.0: 65384 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460156, 1.0: 65384 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334112, 0.0: 191428 |

## ChillerPlant_bypass_leakage_025.csv

- Size: 411.6 MB (431,552,841 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.583 | 643.168 | 335.553 |
| CDWL_PM_POW_1 | 3.3268 | 18.801 | 7.81467 |
| CDWL_PM_POW_2 | 0 | 16.6318 | 0.370767 |
| CDWL_PM_POW_3 | 0 | 1.66743e-13 | 1.14536e-18 |
| CDWL_RW_TEMP | 59.7168 | 147.043 | 80.9542 |
| CDWL_SW_TEMP | 59.56 | 141.886 | 79.3958 |
| CHL_CD_FLOW_1 | 203.501 | 493.116 | 321.583 |
| CHL_CD_FLOW_2 | 0.000208757 | 321.59 | 13.9691 |
| CHL_CD_FLOW_3 | 0.000171703 | 0.00100819 | 0.000428782 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.303523 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.043281 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0 | 0 |
| CHL_CW_FLOW_1 | 176.76 | 428.318 | 279.325 |
| CHL_CW_FLOW_2 | 0.000181325 | 279.331 | 12.1335 |
| CHL_CW_FLOW_3 | 0.000149141 | 0.000875711 | 0.000372437 |
| CHL_POW_1 | 0 | 278.911 | 42.3625 |
| CHL_POW_2 | 0 | 223.94 | 7.73623 |
| CHL_POW_3 | 0 | 0 | 0 |
| CHL_SWCD_TEMP_1 | 59.7167 | 147.043 | 80.9563 |
| CHL_SWCD_TEMP_2 | 73.9737 | 127.408 | 98.5312 |
| CHL_SWCD_TEMP_3 | 73.1329 | 74.9948 | 73.8765 |
| CHL_RW_TEMP_1 | 43.2225 | 95.5604 | 57.5209 |
| CHL_RW_TEMP_2 | 42.2273 | 79.6806 | 54.6584 |
| CHL_RW_TEMP_3 | 42.2273 | 46.9486 | 44.8256 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.0434391 |
| CHL_STA_3 | 0 | 0 | 0 |
| CHL_RWCD_TEMP_1 | 59.6062 | 141.934 | 79.4431 |
| CHL_RWCD_TEMP_2 | 73.8154 | 122.809 | 96.778 |
| CHL_RWCD_TEMP_3 | 73.8154 | 78.2302 | 75.8809 |
| CHL_SW_TEMP_1 | 43.1178 | 90.9275 | 56.0743 |
| CHL_SW_TEMP_2 | 42.0492 | 71.6749 | 51.622 |
| CHL_SW_TEMP_3 | 42.0492 | 46.2983 | 44.3889 |
| CT_FAN_SPD_1 | 0 | 1 | 0.144194 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0136503 |
| CT_FAN_SPD_3 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.144194 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0136503 |
| CT_FAN_SPD_CTRL_3 | 0 | 0 | 0 |
| CT_FLOW_1 | 6.51133 | 52.5626 | 21.674 |
| CT_FLOW_2 | 9.27e-08 | 49.3539 | 2.14121 |
| CT_FLOW_3 | 9.27e-08 | 6.04079e-06 | 1.21117e-06 |
| CT_POW_1 | 0 | 9.99999 | 0.0904187 |
| CT_POW_2 | 0 | 9.99999 | 0.0154867 |
| CT_POW_3 | 0 | 0 | 0 |
| CT_RW_TEMP_1 | 59.7169 | 147.043 | 80.9542 |
| CT_RW_TEMP_2 | 68.2766 | 127.408 | 96.9286 |
| CT_RW_TEMP_3 | 68.2766 | 68.2769 | 68.2767 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.0434391 |
| CT_STA_3 | 0 | 0 | 0 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8182 | 85.3795 | 62.7878 |
| CT_SW_TEMP_2 | 66.9436 | 84.9925 | 72.3265 |
| CT_SW_TEMP_3 | 68.6687 | 68.6688 | 68.6687 |
| CWL_PRI_CW_FLOW | 279.325 | 558.652 | 291.459 |
| CWL_PRI_PM_POW_1 | 6.01525 | 35.3199 | 15.0214 |
| CWL_PRI_PM_POW_2 | 0 | 31.0041 | 0.653084 |
| CWL_PRI_PM_POW_3 | 0 | 7.58094e-13 | 1.38806e-17 |
| CWL_PRI_RW_TEMP | 43.2225 | 95.5604 | 57.5208 |
| CWL_PRI_SW_TEMP | 43.1178 | 90.9274 | 56.0737 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 1.49562e-06 | 837.901 | 561.012 |
| CWL_SEC_DP | 529.016 | 974.252 | 956.698 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | -1.31007e+06 | 0 | -65531.3 |
| CWL_SEC_PM_POW_1 | 1.41803e-07 | 53.6388 | 32.9558 |
| CWL_SEC_PM_POW_2 | 0 | 51.7235 | 32.3504 |
| CWL_SEC_PM_SPD_1 | 0.345033 | 1.0002 | 0.789891 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00004 | 0.685973 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.721403 |
| CWL_SEC_RW_TEMP | 49.3381 | 93.936 | 56.9372 |
| CWL_SEC_SW_TEMP | 52.2579 | 95.4557 | 57.5012 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.627887 | 0.204057 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_COMP_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CHL_POW_3 | 1 | 0.0: 525540 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 502711, 1.0: 22829 |
| CHL_STA_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CT_POW_3 | 1 | 0.0: 525540 |
| CT_RW_TEMP_3 | 7 | 68.27658000000001: 208147, 68.27691: 150857, 68.276634: 47366, 68.276794: 33773, 68.276855: 32252, 68.27669: 27465, 68.27675: 25680 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 502711, 1.0: 22829 |
| CT_STA_3 | 1 | 0.0: 525540 |
| CT_SW_TEMP_3 | 3 | 68.668686: 247052, 68.66879: 192534, 68.66873000000001: 85954 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 379126, 0.0: 146414 |

## ChillerPlant_bypass_leakage_050.csv

- Size: 402.0 MB (421,577,746 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.583 | 321.583 | 321.583 |
| CDWL_PM_POW_1 | 7.61604 | 7.64695 | 7.64576 |
| CDWL_PM_POW_2 | 0 | 1.43552e-12 | 4.25278e-18 |
| CDWL_PM_POW_3 | 0 | 3.10278e-13 | 2.34365e-18 |
| CDWL_RW_TEMP | 59.6292 | 158 | 91.9566 |
| CDWL_SW_TEMP | 59.4702 | 155.594 | 91.0332 |
| CHL_CD_FLOW_1 | 321.582 | 321.582 | 321.582 |
| CHL_CD_FLOW_2 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_CD_FLOW_3 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.401177 |
| CHL_COMP_SPD_CTRL_2 | 0 | 0 | 0 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0 | 0 |
| CHL_CW_FLOW_1 | 279.324 | 279.324 | 279.324 |
| CHL_CW_FLOW_2 | 0.000372431 | 0.000372432 | 0.000372431 |
| CHL_CW_FLOW_3 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_POW_1 | 0 | 241.354 | 26.8718 |
| CHL_POW_2 | 0 | 0 | 0 |
| CHL_POW_3 | 0 | 0 | 0 |
| CHL_SWCD_TEMP_1 | 59.6292 | 158 | 91.9566 |
| CHL_SWCD_TEMP_2 | 73.3802 | 74.9923 | 73.947 |
| CHL_SWCD_TEMP_3 | 73.3802 | 74.9923 | 73.947 |
| CHL_RW_TEMP_1 | 47.1119 | 104.144 | 60.428 |
| CHL_RW_TEMP_2 | 42.2276 | 47.8657 | 45.3038 |
| CHL_RW_TEMP_3 | 42.2276 | 47.8657 | 45.3038 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 0 | 0 |
| CHL_STA_3 | 0 | 0 | 0 |
| CHL_RWCD_TEMP_1 | 59.5164 | 155.64 | 91.0795 |
| CHL_RWCD_TEMP_2 | 74.0501 | 81.7165 | 77.6582 |
| CHL_RWCD_TEMP_3 | 74.0501 | 81.7165 | 77.6582 |
| CHL_SW_TEMP_1 | 47.0073 | 102.076 | 59.6059 |
| CHL_SW_TEMP_2 | 42.0492 | 47.3615 | 44.945 |
| CHL_SW_TEMP_3 | 42.0492 | 47.3615 | 44.945 |
| CT_FAN_SPD_1 | 0 | 1 | 0.228092 |
| CT_FAN_SPD_2 | 0 | 0 | 0 |
| CT_FAN_SPD_3 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.228092 |
| CT_FAN_SPD_CTRL_2 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_3 | 0 | 0 | 0 |
| CT_FLOW_1 | 5.5545 | 10.5992 | 10.4308 |
| CT_FLOW_2 | 6.7553e-08 | 2.45633e-07 | 2.3878e-07 |
| CT_FLOW_3 | 6.7553e-08 | 2.45633e-07 | 2.3878e-07 |
| CT_POW_1 | 0 | 9.99999 | 0.109402 |
| CT_POW_2 | 0 | 0 | 0 |
| CT_POW_3 | 0 | 0 | 0 |
| CT_RW_TEMP_1 | 59.6294 | 158 | 91.9566 |
| CT_RW_TEMP_2 | 68.0814 | 68.0814 | 68.0814 |
| CT_RW_TEMP_3 | 68.0814 | 68.0814 | 68.0814 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 0 | 0 |
| CT_STA_3 | 0 | 0 | 0 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5363 |
| CT_SW_TEMP_1 | 52.8182 | 85.7387 | 63.8452 |
| CT_SW_TEMP_2 | 68.1924 | 68.1924 | 68.1924 |
| CT_SW_TEMP_3 | 68.1924 | 68.1924 | 68.1924 |
| CWL_PRI_CW_FLOW | 279.325 | 279.325 | 279.325 |
| CWL_PRI_PM_POW_1 | 15.0212 | 15.0212 | 15.0212 |
| CWL_PRI_PM_POW_2 | 0 | 1.01925e-12 | 4.25945e-17 |
| CWL_PRI_PM_POW_3 | 0 | 1.54318e-12 | 3.06614e-17 |
| CWL_PRI_RW_TEMP | 47.1119 | 104.144 | 60.428 |
| CWL_PRI_SW_TEMP | 47.0073 | 102.076 | 59.6058 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 4.50863e-06 | 837.854 | 525.64 |
| CWL_SEC_DP | 529.023 | 974.698 | 958.936 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 542554 | 30157.3 |
| CWL_SEC_PM_POW_1 | 9.2962e-07 | 54.3097 | 30.9513 |
| CWL_SEC_PM_POW_2 | 0 | 51.7173 | 30.6436 |
| CWL_SEC_PM_SPD_1 | 0.345034 | 1.01423 | 0.764051 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00001 | 0.652419 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.688629 |
| CWL_SEC_RW_TEMP | 52.7244 | 103.374 | 60.0264 |
| CWL_SEC_SW_TEMP | 53.389 | 104.039 | 60.2709 |
| OA_TEMP | -9.74049 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.02199 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.669107 | 0.0491504 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CDWL_CW_FLOW | 1 | 321.582963402: 525540 |
| CHL_CD_FLOW_1 | 1 | 321.582107112: 525540 |
| CHL_CD_FLOW_2 | 10 | 0.000428775001096: 525495, 0.000428774972553: 26, 0.000428775058182: 4, 0.00042877494401: 4, 0.000428775115268: 3, 0.000428774886924: 2, 0.000428775257983: 2, 0.000428774801295: 2, 0.000428774772752: 1, 0.000428775143811: 1 |
| CHL_CD_FLOW_3 | 4 | 0.000428775001096: 525532, 0.000428774972553: 6, 0.00042877494401: 1, 0.000428775058182: 1 |
| CHL_COMP_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CHL_COMP_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CHL_CW_FLOW_1 | 1 | 279.324281241: 525540 |
| CHL_CW_FLOW_2 | 8 | 0.000372431375983: 525523, 0.00037243134744: 4, 0.000372431404526: 4, 0.000372431290354: 3, 0.000372431433069: 2, 0.000372431261811: 2, 0.000372431176182: 1, 0.000372431604327: 1 |
| CHL_CW_FLOW_3 | 3 | 0.000372431375983: 525537, 0.00037243134744: 2, 0.000372431176182: 1 |
| CHL_POW_2 | 1 | 0.0: 525540 |
| CHL_POW_3 | 1 | 0.0: 525540 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 1 | 0.0: 525540 |
| CHL_STA_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CT_POW_2 | 1 | 0.0: 525540 |
| CT_POW_3 | 1 | 0.0: 525540 |
| CT_RW_TEMP_2 | 1 | 68.08135: 525540 |
| CT_RW_TEMP_3 | 1 | 68.08135: 525540 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 1 | 0.0: 525540 |
| CT_STA_3 | 1 | 0.0: 525540 |
| CT_SW_TEMP_2 | 1 | 68.19243: 525540 |
| CT_SW_TEMP_3 | 1 | 68.19243: 525540 |
| CWL_PRI_CW_FLOW | 1 | 279.3250147961: 525540 |
| CWL_PRI_PM_POW_1 | 1 | 15.0211884094: 525540 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 361902, 0.0: 163638 |

## ChillerPlant_bypass_leakage_075.csv

- Size: 409.7 MB (429,552,248 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.583 | 321.583 | 321.583 |
| CDWL_PM_POW_1 | 7.6106 | 7.6106 | 7.6106 |
| CDWL_PM_POW_2 | 0 | 3.49227e-14 | 1.14307e-19 |
| CDWL_PM_POW_3 | 0 | 9.44852e-15 | 4.03968e-20 |
| CDWL_RW_TEMP | 72.2097 | 163.377 | 103.795 |
| CDWL_SW_TEMP | 72.0582 | 162.35 | 103.308 |
| CHL_CD_FLOW_1 | 321.582 | 321.582 | 321.582 |
| CHL_CD_FLOW_2 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_CD_FLOW_3 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.492021 |
| CHL_COMP_SPD_CTRL_2 | 0 | 0 | 0 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0 | 0 |
| CHL_CW_FLOW_1 | 279.324 | 279.324 | 279.324 |
| CHL_CW_FLOW_2 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_CW_FLOW_3 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_POW_1 | 0 | 172.198 | 14.0024 |
| CHL_POW_2 | 0 | 0 | 0 |
| CHL_POW_3 | 0 | 0 | 0 |
| CHL_SWCD_TEMP_1 | 72.2097 | 163.377 | 103.795 |
| CHL_SWCD_TEMP_2 | 73.6438 | 74.9909 | 74.0389 |
| CHL_SWCD_TEMP_3 | 73.6438 | 74.9909 | 74.0389 |
| CHL_RW_TEMP_1 | 50.0544 | 108.866 | 62.8442 |
| CHL_RW_TEMP_2 | 42.2274 | 48.6271 | 45.7034 |
| CHL_RW_TEMP_3 | 42.2274 | 48.6271 | 45.7034 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 0 | 0 |
| CHL_STA_3 | 0 | 0 | 0 |
| CHL_RWCD_TEMP_1 | 72.1043 | 162.396 | 103.354 |
| CHL_RWCD_TEMP_2 | 74.9458 | 85.081 | 79.649 |
| CHL_RWCD_TEMP_3 | 74.9458 | 85.081 | 79.649 |
| CHL_SW_TEMP_1 | 49.9498 | 108.014 | 62.4341 |
| CHL_SW_TEMP_2 | 42.0493 | 48.2142 | 45.3928 |
| CHL_SW_TEMP_3 | 42.0493 | 48.2142 | 45.3928 |
| CT_FAN_SPD_1 | 0 | 1 | 0.292039 |
| CT_FAN_SPD_2 | 0 | 0 | 0 |
| CT_FAN_SPD_3 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.292039 |
| CT_FAN_SPD_CTRL_2 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_3 | 0 | 0 | 0 |
| CT_FLOW_1 | 3.99197 | 3.99197 | 3.99197 |
| CT_FLOW_2 | 3.62296e-08 | 3.62296e-08 | 3.62296e-08 |
| CT_FLOW_3 | 3.62296e-08 | 3.62296e-08 | 3.62296e-08 |
| CT_POW_1 | 0 | 9.99999 | 0.177824 |
| CT_POW_2 | 0 | 0 | 0 |
| CT_POW_3 | 0 | 0 | 0 |
| CT_RW_TEMP_1 | 72.2097 | 163.376 | 103.795 |
| CT_RW_TEMP_2 | 68.0147 | 68.0147 | 68.0147 |
| CT_RW_TEMP_3 | 68.0147 | 68.0147 | 68.0147 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 0 | 0 |
| CT_STA_3 | 0 | 0 | 0 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5363 |
| CT_SW_TEMP_1 | 59.6454 | 85.7281 | 64.5366 |
| CT_SW_TEMP_2 | 68.0339 | 68.0339 | 68.0339 |
| CT_SW_TEMP_3 | 68.0339 | 68.0339 | 68.0339 |
| CWL_PRI_CW_FLOW | 279.325 | 279.325 | 279.325 |
| CWL_PRI_PM_POW_1 | 15.0212 | 15.0212 | 15.0212 |
| CWL_PRI_PM_POW_2 | 0 | 6.69828e-12 | 4.06776e-17 |
| CWL_PRI_PM_POW_3 | 0 | 1.32601e-12 | 1.91545e-17 |
| CWL_PRI_RW_TEMP | 50.0544 | 108.866 | 62.8442 |
| CWL_PRI_SW_TEMP | 49.9497 | 108.014 | 62.4341 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 5.90936e-06 | 837.847 | 463.746 |
| CWL_SEC_DP | 529.049 | 973.387 | 959.877 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | -345598 | 0 | -14310.1 |
| CWL_SEC_PM_POW_1 | 0.000107046 | 53.6387 | 28.4425 |
| CWL_SEC_PM_POW_2 | 0 | 51.7162 | 28.2708 |
| CWL_SEC_PM_SPD_1 | 0.345034 | 1.00056 | 0.709069 |
| CWL_SEC_PM_SPD_2 | 0 | 1 | 0.555117 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.560637 |
| CWL_SEC_RW_TEMP | 53.7395 | 108.494 | 62.5582 |
| CWL_SEC_SW_TEMP | 53.7562 | 108.761 | 62.6709 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0 | 0 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CDWL_CW_FLOW | 1 | 321.582963402: 525540 |
| CDWL_PM_POW_1 | 1 | 7.6106045059: 525540 |
| CHL_CD_FLOW_1 | 1 | 321.582107112: 525540 |
| CHL_CD_FLOW_2 | 6 | 0.000428775001096: 525523, 0.000428774972553: 13, 0.000428775058182: 1, 0.000428775086725: 1, 0.000428775115268: 1, 0.000428774915467: 1 |
| CHL_CD_FLOW_3 | 2 | 0.000428775001096: 525534, 0.000428774972553: 6 |
| CHL_COMP_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CHL_COMP_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CHL_CW_FLOW_1 | 1 | 279.324281241: 525540 |
| CHL_CW_FLOW_2 | 4 | 0.000372431375983: 525534, 0.000372431404526: 3, 0.00037243134744: 2, 0.000372431233268: 1 |
| CHL_CW_FLOW_3 | 3 | 0.000372431375983: 525534, 0.000372431404526: 4, 0.00037243134744: 2 |
| CHL_POW_2 | 1 | 0.0: 525540 |
| CHL_POW_3 | 1 | 0.0: 525540 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 1 | 0.0: 525540 |
| CHL_STA_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CT_FLOW_1 | 1 | 3.99197003373: 525540 |
| CT_FLOW_2 | 1 | 3.62295870855e-08: 525540 |
| CT_FLOW_3 | 1 | 3.62295870855e-08: 525540 |
| CT_POW_2 | 1 | 0.0: 525540 |
| CT_POW_3 | 1 | 0.0: 525540 |
| CT_RW_TEMP_2 | 1 | 68.01465999999999: 525540 |
| CT_RW_TEMP_3 | 1 | 68.01465999999999: 525540 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 1 | 0.0: 525540 |
| CT_STA_3 | 1 | 0.0: 525540 |
| CT_SW_TEMP_2 | 1 | 68.03389: 525540 |
| CT_SW_TEMP_3 | 1 | 68.03389: 525540 |
| CWL_PRI_CW_FLOW | 1 | 279.3250147961: 525540 |
| CWL_PRI_PM_POW_1 | 1 | 15.0211884094: 525540 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 294637, 0.0: 230903 |
| TWV_CTRL | 1 | 0.0: 525540 |

## ChillerPlant_bypass_stuck_050.csv

- Size: 407.9 MB (427,758,853 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.583 | 321.583 | 321.583 |
| CDWL_PM_POW_1 | 7.62003 | 46.0841 | 7.65195 |
| CDWL_PM_POW_2 | 0 | 7.4628e-14 | 1.0956e-18 |
| CDWL_PM_POW_3 | 0 | 3.48425e-13 | 1.68217e-18 |
| CDWL_RW_TEMP | 41.6372 | 158 | 91.0985 |
| CDWL_SW_TEMP | 41.4913 | 155.594 | 90.1758 |
| CHL_CD_FLOW_1 | 321.582 | 321.582 | 321.582 |
| CHL_CD_FLOW_2 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_CD_FLOW_3 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.400878 |
| CHL_COMP_SPD_CTRL_2 | 0 | 0 | 0 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0 | 0 |
| CHL_CW_FLOW_1 | 279.324 | 279.324 | 279.324 |
| CHL_CW_FLOW_2 | 0.000372431 | 0.000372432 | 0.000372431 |
| CHL_CW_FLOW_3 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_POW_1 | 0 | 238.725 | 26.8234 |
| CHL_POW_2 | 0 | 0 | 0 |
| CHL_POW_3 | 0 | 0 | 0 |
| CHL_SWCD_TEMP_1 | 41.637 | 158 | 91.0986 |
| CHL_SWCD_TEMP_2 | 73.3606 | 74.996 | 73.9383 |
| CHL_SWCD_TEMP_3 | 73.3606 | 74.996 | 73.9383 |
| CHL_RW_TEMP_1 | 47.112 | 104.144 | 60.4276 |
| CHL_RW_TEMP_2 | 42.2273 | 47.8656 | 45.3034 |
| CHL_RW_TEMP_3 | 42.2273 | 47.8656 | 45.3034 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 0 | 0 |
| CHL_STA_3 | 0 | 0 | 0 |
| CHL_RWCD_TEMP_1 | 41.5376 | 155.64 | 90.2221 |
| CHL_RWCD_TEMP_2 | 74.0976 | 81.7361 | 77.7058 |
| CHL_RWCD_TEMP_3 | 74.0976 | 81.7361 | 77.7058 |
| CHL_SW_TEMP_1 | 47.0073 | 102.076 | 59.6055 |
| CHL_SW_TEMP_2 | 42.0492 | 47.3615 | 44.9448 |
| CHL_SW_TEMP_3 | 42.0492 | 47.3615 | 44.9448 |
| CT_FAN_SPD_1 | 0 | 1 | 0.225366 |
| CT_FAN_SPD_2 | 0 | 0 | 0 |
| CT_FAN_SPD_3 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.225366 |
| CT_FAN_SPD_CTRL_2 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_3 | 0 | 0 | 0 |
| CT_FLOW_1 | 6.43504 | 318.419 | 10.6472 |
| CT_FLOW_2 | 9.05403e-08 | 0.000221686 | 2.74448e-07 |
| CT_FLOW_3 | 9.05403e-08 | 0.000221686 | 2.74448e-07 |
| CT_POW_1 | 0 | 9.99999 | 0.109408 |
| CT_POW_2 | 0 | 0 | 0 |
| CT_POW_3 | 0 | 0 | 0 |
| CT_RW_TEMP_1 | 41.6372 | 158 | 91.0985 |
| CT_RW_TEMP_2 | 68.7045 | 68.7047 | 68.7047 |
| CT_RW_TEMP_3 | 68.7045 | 68.7047 | 68.7047 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 0 | 0 |
| CT_STA_3 | 0 | 0 | 0 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.536 |
| CT_SW_TEMP_1 | 36.8039 | 85.6805 | 63.1302 |
| CT_SW_TEMP_2 | 69.6975 | 69.6976 | 69.6976 |
| CT_SW_TEMP_3 | 69.6975 | 69.6976 | 69.6976 |
| CWL_PRI_CW_FLOW | 279.325 | 279.325 | 279.325 |
| CWL_PRI_PM_POW_1 | 15.0212 | 15.0212 | 15.0212 |
| CWL_PRI_PM_POW_2 | 0 | 5.04504e-12 | 4.66916e-17 |
| CWL_PRI_PM_POW_3 | 0 | 1.54557e-12 | 2.42039e-17 |
| CWL_PRI_RW_TEMP | 47.1119 | 104.144 | 60.4276 |
| CWL_PRI_SW_TEMP | 47.0073 | 102.076 | 59.6055 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 4.48652e-06 | 837.87 | 525.865 |
| CWL_SEC_DP | 529.037 | 968.498 | 958.934 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 542603 | 30157 |
| CWL_SEC_PM_POW_1 | 1.30814e-06 | 53.6388 | 30.962 |
| CWL_SEC_PM_POW_2 | 0 | 51.7199 | 30.653 |
| CWL_SEC_PM_SPD_1 | 0.345033 | 1.00093 | 0.764126 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00002 | 0.652454 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.688471 |
| CWL_SEC_RW_TEMP | 52.7243 | 103.374 | 60.0583 |
| CWL_SEC_SW_TEMP | 53.3891 | 104.039 | 60.3024 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 1 | 0.118678 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CDWL_CW_FLOW | 1 | 321.582963402: 525540 |
| CHL_CD_FLOW_1 | 1 | 321.582107112: 525540 |
| CHL_CD_FLOW_2 | 14 | 0.000428775001096: 525485, 0.000428774972553: 37, 0.00042877494401: 5, 0.000428775058182: 2, 0.000428775086725: 2, 0.000428774915467: 1, 0.000428775143811: 1, 0.000428774801295: 1, 0.0004287752294399: 1, 0.00042877465858: 1, 0.000428775286526: 1, 0.000428775343612: 1, 0.000428775115268: 1, 0.000428774572951: 1 |
| CHL_CD_FLOW_3 | 2 | 0.000428775001096: 525530, 0.000428774972553: 10 |
| CHL_COMP_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CHL_COMP_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CHL_CW_FLOW_1 | 1 | 279.324281241: 525540 |
| CHL_CW_FLOW_2 | 8 | 0.000372431375983: 525522, 0.000372431433069: 6, 0.000372431404526: 5, 0.00037243134744: 2, 0.0003724314616119: 2, 0.000372431290354: 1, 0.000372431575784: 1, 0.000372431490155: 1 |
| CHL_CW_FLOW_3 | 6 | 0.000372431375983: 525532, 0.00037243134744: 3, 0.000372431404526: 2, 0.000372431261811: 1, 0.000372431433069: 1, 0.000372431233268: 1 |
| CHL_POW_2 | 1 | 0.0: 525540 |
| CHL_POW_3 | 1 | 0.0: 525540 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 1 | 0.0: 525540 |
| CHL_STA_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CT_POW_2 | 1 | 0.0: 525540 |
| CT_POW_3 | 1 | 0.0: 525540 |
| CT_RW_TEMP_2 | 4 | 68.70470999999999: 525497, 68.704666: 18, 68.704605: 15, 68.70455: 10 |
| CT_RW_TEMP_3 | 4 | 68.70470999999999: 525497, 68.704666: 18, 68.704605: 15, 68.70455: 10 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 1 | 0.0: 525540 |
| CT_STA_3 | 1 | 0.0: 525540 |
| CT_SW_TEMP_2 | 3 | 69.6976: 525490, 69.697556: 39, 69.69749499999999: 11 |
| CT_SW_TEMP_3 | 3 | 69.6976: 525490, 69.697556: 39, 69.69749499999999: 11 |
| CWL_PRI_CW_FLOW | 1 | 279.3250147961: 525540 |
| CWL_PRI_PM_POW_1 | 1 | 15.0211884094: 525540 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 361819, 0.0: 163721 |

## ChillerPlant_bypass_stuck_075.csv

- Size: 409.7 MB (429,638,303 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.583 | 321.583 | 321.583 |
| CDWL_PM_POW_1 | 7.6106 | 7.6106 | 7.6106 |
| CDWL_PM_POW_2 | 0 | 1.0683e-14 | 4.71774e-20 |
| CDWL_PM_POW_3 | 0 | 4.40494e-15 | 3.95495e-20 |
| CDWL_RW_TEMP | 72.2097 | 163.377 | 103.795 |
| CDWL_SW_TEMP | 72.0582 | 162.35 | 103.308 |
| CHL_CD_FLOW_1 | 321.582 | 321.582 | 321.582 |
| CHL_CD_FLOW_2 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_CD_FLOW_3 | 0.000428775 | 0.000428775 | 0.000428775 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.492022 |
| CHL_COMP_SPD_CTRL_2 | 0 | 0 | 0 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0 | 0 |
| CHL_CW_FLOW_1 | 279.324 | 279.324 | 279.324 |
| CHL_CW_FLOW_2 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_CW_FLOW_3 | 0.000372431 | 0.000372431 | 0.000372431 |
| CHL_POW_1 | 0 | 175.325 | 14.0026 |
| CHL_POW_2 | 0 | 0 | 0 |
| CHL_POW_3 | 0 | 0 | 0 |
| CHL_SWCD_TEMP_1 | 72.2097 | 163.377 | 103.795 |
| CHL_SWCD_TEMP_2 | 73.6438 | 74.9909 | 74.0389 |
| CHL_SWCD_TEMP_3 | 73.6438 | 74.9909 | 74.0389 |
| CHL_RW_TEMP_1 | 50.0544 | 108.866 | 62.8442 |
| CHL_RW_TEMP_2 | 42.2274 | 48.6271 | 45.7034 |
| CHL_RW_TEMP_3 | 42.2274 | 48.6271 | 45.7034 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 0 | 0 |
| CHL_STA_3 | 0 | 0 | 0 |
| CHL_RWCD_TEMP_1 | 72.1043 | 162.396 | 103.354 |
| CHL_RWCD_TEMP_2 | 74.9458 | 85.0811 | 79.649 |
| CHL_RWCD_TEMP_3 | 74.9458 | 85.0811 | 79.649 |
| CHL_SW_TEMP_1 | 49.9498 | 108.014 | 62.4341 |
| CHL_SW_TEMP_2 | 42.0492 | 48.2142 | 45.3928 |
| CHL_SW_TEMP_3 | 42.0492 | 48.2142 | 45.3928 |
| CT_FAN_SPD_1 | 0 | 1 | 0.292082 |
| CT_FAN_SPD_2 | 0 | 0 | 0 |
| CT_FAN_SPD_3 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.292082 |
| CT_FAN_SPD_CTRL_2 | 0 | 0 | 0 |
| CT_FAN_SPD_CTRL_3 | 0 | 0 | 0 |
| CT_FLOW_1 | 3.99197 | 3.99197 | 3.99197 |
| CT_FLOW_2 | 3.62296e-08 | 3.62296e-08 | 3.62296e-08 |
| CT_FLOW_3 | 3.62296e-08 | 3.62296e-08 | 3.62296e-08 |
| CT_POW_1 | 0 | 9.99999 | 0.178271 |
| CT_POW_2 | 0 | 0 | 0 |
| CT_POW_3 | 0 | 0 | 0 |
| CT_RW_TEMP_1 | 72.2097 | 163.376 | 103.795 |
| CT_RW_TEMP_2 | 68.0153 | 68.0153 | 68.0153 |
| CT_RW_TEMP_3 | 68.0153 | 68.0153 | 68.0153 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 0 | 0 |
| CT_STA_3 | 0 | 0 | 0 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 59.6454 | 85.7281 | 64.5366 |
| CT_SW_TEMP_2 | 68.0354 | 68.0354 | 68.0354 |
| CT_SW_TEMP_3 | 68.0354 | 68.0354 | 68.0354 |
| CWL_PRI_CW_FLOW | 279.325 | 279.325 | 279.325 |
| CWL_PRI_PM_POW_1 | 15.0212 | 15.0212 | 15.0212 |
| CWL_PRI_PM_POW_2 | 0 | 7.18141e-13 | 2.69202e-17 |
| CWL_PRI_PM_POW_3 | 0 | 4.99332e-13 | 1.61284e-17 |
| CWL_PRI_RW_TEMP | 50.0544 | 108.866 | 62.8442 |
| CWL_PRI_SW_TEMP | 49.9497 | 108.014 | 62.4341 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 5.91138e-06 | 837.847 | 463.746 |
| CWL_SEC_DP | 529.049 | 973.387 | 959.877 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | -345598 | 0 | -14310.1 |
| CWL_SEC_PM_POW_1 | 0.000107046 | 53.6387 | 28.4425 |
| CWL_SEC_PM_POW_2 | 0 | 51.7162 | 28.2708 |
| CWL_SEC_PM_SPD_1 | 0.345034 | 1.00056 | 0.709069 |
| CWL_SEC_PM_SPD_2 | 0 | 1 | 0.555117 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.560644 |
| CWL_SEC_RW_TEMP | 53.7395 | 108.494 | 62.5582 |
| CWL_SEC_SW_TEMP | 53.7562 | 108.761 | 62.6709 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0 | 0 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CDWL_CW_FLOW | 1 | 321.582963402: 525540 |
| CDWL_PM_POW_1 | 1 | 7.6106045059: 525540 |
| CHL_CD_FLOW_1 | 1 | 321.582107112: 525540 |
| CHL_CD_FLOW_2 | 7 | 0.000428775001096: 525519, 0.000428774972553: 15, 0.000428774915467: 2, 0.00042877494401: 1, 0.000428774772752: 1, 0.000428775058182: 1, 0.000428775115268: 1 |
| CHL_CD_FLOW_3 | 2 | 0.000428775001096: 525535, 0.000428774972553: 5 |
| CHL_COMP_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CHL_COMP_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CHL_CW_FLOW_1 | 1 | 279.324281241: 525540 |
| CHL_CW_FLOW_2 | 4 | 0.000372431375983: 525532, 0.000372431404526: 6, 0.000372431433069: 1, 0.00037243134744: 1 |
| CHL_CW_FLOW_3 | 4 | 0.000372431375983: 525537, 0.000372431433069: 1, 0.00037243134744: 1, 0.000372431404526: 1 |
| CHL_POW_2 | 1 | 0.0: 525540 |
| CHL_POW_3 | 1 | 0.0: 525540 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 1 | 0.0: 525540 |
| CHL_STA_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_3 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_2 | 1 | 0.0: 525540 |
| CT_FAN_SPD_CTRL_3 | 1 | 0.0: 525540 |
| CT_FLOW_1 | 1 | 3.99197003373: 525540 |
| CT_FLOW_2 | 1 | 3.62295870855e-08: 525540 |
| CT_FLOW_3 | 1 | 3.62295870855e-08: 525540 |
| CT_POW_2 | 1 | 0.0: 525540 |
| CT_POW_3 | 1 | 0.0: 525540 |
| CT_RW_TEMP_2 | 1 | 68.01531999999999: 525540 |
| CT_RW_TEMP_3 | 1 | 68.01531999999999: 525540 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 1 | 0.0: 525540 |
| CT_STA_3 | 1 | 0.0: 525540 |
| CT_SW_TEMP_2 | 1 | 68.03543: 525540 |
| CT_SW_TEMP_3 | 1 | 68.03543: 525540 |
| CWL_PRI_CW_FLOW | 1 | 279.3250147961: 525540 |
| CWL_PRI_PM_POW_1 | 1 | 15.0211884094: 525540 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 294641, 0.0: 230899 |
| TWV_CTRL | 1 | 0.0: 525540 |

## ChillerPlant_chiller_bias_-1.csv

- Size: 405.6 MB (425,325,916 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.566 | 964.749 | 360.885 |
| CDWL_PM_POW_1 | 7.60653 | 142.277 | 22.8721 |
| CDWL_PM_POW_2 | 0 | 135.485 | 5.52402 |
| CDWL_PM_POW_3 | 0 | 87.2206 | 0.166311 |
| CDWL_RW_TEMP | 59.5738 | 94.8238 | 65.6959 |
| CDWL_SW_TEMP | 59.5247 | 85.8615 | 64.0565 |
| CHL_CD_FLOW_1 | 202.86 | 492.846 | 321.583 |
| CHL_CD_FLOW_2 | 0.000222214 | 398.576 | 38.1574 |
| CHL_CD_FLOW_3 | 0.000170623 | 321.589 | 1.14453 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.132152 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0868832 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0.943645 | 0.00254476 |
| CHL_CW_FLOW_1 | 176.203 | 428.083 | 279.325 |
| CHL_CW_FLOW_2 | 0.000193014 | 346.201 | 33.1433 |
| CHL_CW_FLOW_3 | 0.000148202 | 279.33 | 0.99413 |
| CHL_POW_1 | 0 | 233.229 | 24.1506 |
| CHL_POW_2 | 0 | 226.358 | 16.9812 |
| CHL_POW_3 | 0 | 204.141 | 0.484782 |
| CHL_SWCD_TEMP_1 | 59.5738 | 94.8236 | 65.5997 |
| CHL_SWCD_TEMP_2 | 70.0906 | 95.0629 | 75.6863 |
| CHL_SWCD_TEMP_3 | 73.8767 | 93.6324 | 79.8363 |
| CHL_RW_TEMP_1 | 43.1391 | 73.1301 | 55.0738 |
| CHL_RW_TEMP_2 | 42.2273 | 62.0905 | 49.7397 |
| CHL_RW_TEMP_3 | 42.2273 | 58.1766 | 49.3109 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.118665 |
| CHL_STA_3 | 0 | 1 | 0.00355824 |
| CHL_RWCD_TEMP_1 | 59.571 | 86.2029 | 64.195 |
| CHL_RWCD_TEMP_2 | 66.2201 | 86.2029 | 73.0083 |
| CHL_RWCD_TEMP_3 | 73.2193 | 86.1963 | 76.7976 |
| CHL_SW_TEMP_1 | 41.3865 | 54.3326 | 51.825 |
| CHL_SW_TEMP_2 | 42.0493 | 52.8167 | 46.6823 |
| CHL_SW_TEMP_3 | 42.0493 | 50.0148 | 45.8803 |
| CT_FAN_SPD_1 | 0 | 1 | 0.195265 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0909283 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00236028 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.195265 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0909283 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00236028 |
| CT_FLOW_1 | 2.02076 | 575.171 | 135.726 |
| CT_FLOW_2 | 1.27256e-08 | 453.292 | 37.9456 |
| CT_FLOW_3 | 1.27256e-08 | 320.538 | 1.13663 |
| CT_POW_1 | 0 | 9.99999 | 1.33868 |
| CT_POW_2 | 0 | 9.99999 | 0.630396 |
| CT_POW_3 | 0 | 9.99999 | 0.0124146 |
| CT_RW_TEMP_1 | 59.5738 | 94.8236 | 65.6958 |
| CT_RW_TEMP_2 | 68.7045 | 94.4979 | 73.4331 |
| CT_RW_TEMP_3 | 68.7045 | 94.2952 | 77.819 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.118665 |
| CT_STA_3 | 0 | 1 | 0.00355824 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 52.8178 | 85.5142 | 62.121 |
| CT_SW_TEMP_2 | 65.953 | 85.5149 | 71.8559 |
| CT_SW_TEMP_3 | 69.6974 | 88.0512 | 75.8015 |
| CWL_PRI_CW_FLOW | 279.311 | 837.975 | 313.463 |
| CWL_PRI_PM_POW_1 | 5.97741 | 35.2811 | 15.0217 |
| CWL_PRI_PM_POW_2 | 0 | 31.1079 | 1.78376 |
| CWL_PRI_PM_POW_3 | 0 | 22.4451 | 0.0535081 |
| CWL_PRI_RW_TEMP | 43.1391 | 73.2115 | 55.0738 |
| CWL_PRI_SW_TEMP | 43.0344 | 56.1336 | 53.5249 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 2.81078e-07 | 837.914 | 674.246 |
| CWL_SEC_DP | 529.074 | 979.333 | 957.368 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.8341e+06 | 92158.6 |
| CWL_SEC_PM_POW_1 | 2.66672e-08 | 53.6387 | 41.0874 |
| CWL_SEC_PM_POW_2 | 0 | 51.7265 | 40.5813 |
| CWL_SEC_PM_SPD_1 | 0.34482 | 1.00407 | 0.880246 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00006 | 0.8226 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.851657 |
| CWL_SEC_RW_TEMP | 44.5552 | 62.2717 | 53.7845 |
| CWL_SEC_SW_TEMP | 50.334 | 73.0196 | 55.2322 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.885307 | 0.267719 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 463177, 1.0: 62363 |
| CHL_STA_3 | 2 | 0.0: 523670, 1.0: 1870 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 463177, 1.0: 62363 |
| CT_STA_3 | 2 | 0.0: 523670, 1.0: 1870 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 447580, 0.0: 77960 |

## ChillerPlant_chiller_bias_-2.csv

- Size: 409.2 MB (429,103,173 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.581 | 964.749 | 357.347 |
| CDWL_PM_POW_1 | 7.60653 | 141.889 | 22.2781 |
| CDWL_PM_POW_2 | 0 | 135.572 | 5.03618 |
| CDWL_PM_POW_3 | 0 | 87.1115 | 0.142455 |
| CDWL_RW_TEMP | 59.5134 | 94.8316 | 65.6021 |
| CDWL_SW_TEMP | 59.4639 | 86.0127 | 64.0225 |
| CHL_CD_FLOW_1 | 202.057 | 493.239 | 321.584 |
| CHL_CD_FLOW_2 | 0.000212314 | 413.643 | 34.7827 |
| CHL_CD_FLOW_3 | 0.000169276 | 321.592 | 0.980357 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.116725 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0883664 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00252911 |
| CHL_CW_FLOW_1 | 175.506 | 428.424 | 279.326 |
| CHL_CW_FLOW_2 | 0.000184414 | 359.288 | 30.2121 |
| CHL_CW_FLOW_3 | 0.000147032 | 279.333 | 0.851532 |
| CHL_POW_1 | 0 | 234.832 | 21.2887 |
| CHL_POW_2 | 0 | 227.758 | 17.9714 |
| CHL_POW_3 | 0 | 220.268 | 0.505143 |
| CHL_SWCD_TEMP_1 | 59.5134 | 94.4827 | 65.4302 |
| CHL_SWCD_TEMP_2 | 70.3676 | 95.4394 | 76.1204 |
| CHL_SWCD_TEMP_3 | 73.8766 | 95.2688 | 81.0173 |
| CHL_RW_TEMP_1 | 43.3124 | 73.0193 | 56.6414 |
| CHL_RW_TEMP_2 | 42.2273 | 63.3903 | 50.098 |
| CHL_RW_TEMP_3 | 42.2273 | 57.5703 | 49.8257 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.108173 |
| CHL_STA_3 | 0 | 1 | 0.00304639 |
| CHL_RWCD_TEMP_1 | 59.5101 | 86.4425 | 64.1574 |
| CHL_RWCD_TEMP_2 | 66.0252 | 86.4425 | 72.9926 |
| CHL_RWCD_TEMP_3 | 73.2159 | 86.4466 | 77.6196 |
| CHL_SW_TEMP_1 | 39.7532 | 54.1938 | 51.7245 |
| CHL_SW_TEMP_2 | 42.0493 | 52.8617 | 46.7836 |
| CHL_SW_TEMP_3 | 42.0493 | 50.0498 | 45.8041 |
| CT_FAN_SPD_1 | 0 | 1 | 0.186021 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0832636 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00205765 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.186021 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0832636 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00205765 |
| CT_FLOW_1 | 2.02238 | 575.118 | 130.026 |
| CT_FLOW_2 | 1.27391e-08 | 454.092 | 34.5882 |
| CT_FLOW_3 | 1.27391e-08 | 320.549 | 0.97359 |
| CT_POW_1 | 0 | 9.99999 | 1.28002 |
| CT_POW_2 | 0 | 9.99999 | 0.580575 |
| CT_POW_3 | 0 | 9.99999 | 0.0109642 |
| CT_RW_TEMP_1 | 59.5135 | 94.8316 | 65.602 |
| CT_RW_TEMP_2 | 68.7045 | 94.8316 | 73.0946 |
| CT_RW_TEMP_3 | 68.7045 | 94.8316 | 78.4435 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.108173 |
| CT_STA_3 | 0 | 1 | 0.00304639 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8175 | 85.7462 | 62.0653 |
| CT_SW_TEMP_2 | 65.8789 | 85.7461 | 71.8693 |
| CT_SW_TEMP_3 | 69.6974 | 88.007 | 76.4779 |
| CWL_PRI_CW_FLOW | 279.323 | 837.975 | 310.389 |
| CWL_PRI_PM_POW_1 | 5.93022 | 35.3374 | 15.0217 |
| CWL_PRI_PM_POW_2 | 0 | 31.107 | 1.62611 |
| CWL_PRI_PM_POW_3 | 0 | 22.638 | 0.0458375 |
| CWL_PRI_RW_TEMP | 43.3124 | 73.0733 | 56.6413 |
| CWL_PRI_SW_TEMP | 43.2077 | 57.7914 | 55.1496 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 3.02331e-06 | 837.961 | 716.162 |
| CWL_SEC_DP | 529.037 | 979.404 | 957.946 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.72891e+06 | 87535.4 |
| CWL_SEC_PM_POW_1 | 2.87808e-07 | 53.6388 | 43.8496 |
| CWL_SEC_PM_POW_2 | 0 | 51.7328 | 43.4657 |
| CWL_SEC_PM_SPD_1 | 0.344982 | 1.00192 | 0.910309 |
| CWL_SEC_PM_SPD_2 | 0 | 1.0001 | 0.865911 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.885187 |
| CWL_SEC_RW_TEMP | 45.1548 | 62.8316 | 55.4975 |
| CWL_SEC_SW_TEMP | 50.504 | 72.9107 | 56.6315 |
| OA_TEMP | -9.74049 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.02199 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.885173 | 0.289825 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 468691, 1.0: 56849 |
| CHL_STA_3 | 2 | 0.0: 523939, 1.0: 1601 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 468691, 1.0: 56849 |
| CT_STA_3 | 2 | 0.0: 523939, 1.0: 1601 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 465201, 0.0: 60339 |

## ChillerPlant_chiller_bias_1.csv

- Size: 407.2 MB (427,004,563 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.557 | 964.751 | 364.787 |
| CDWL_PM_POW_1 | 7.60945 | 142.115 | 23.5283 |
| CDWL_PM_POW_2 | 0 | 135.442 | 6.01112 |
| CDWL_PM_POW_3 | 0 | 86.6519 | 0.244743 |
| CDWL_RW_TEMP | 59.4664 | 94.6185 | 65.8466 |
| CDWL_SW_TEMP | 59.3508 | 85.8314 | 64.0953 |
| CHL_CD_FLOW_1 | 201.784 | 491.993 | 321.582 |
| CHL_CD_FLOW_2 | 0.00027156 | 411.242 | 41.5219 |
| CHL_CD_FLOW_3 | 0.000168818 | 321.592 | 1.68333 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.169825 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0726416 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00293686 |
| CHL_CW_FLOW_1 | 175.268 | 427.342 | 279.324 |
| CHL_CW_FLOW_2 | 0.000235875 | 357.202 | 36.0657 |
| CHL_CW_FLOW_3 | 0.000146634 | 279.333 | 1.46213 |
| CHL_POW_1 | 0 | 231.819 | 31.8866 |
| CHL_POW_2 | 0 | 225.882 | 13.3004 |
| CHL_POW_3 | 0 | 223.541 | 0.530453 |
| CHL_SWCD_TEMP_1 | 59.4663 | 94.6185 | 65.9565 |
| CHL_SWCD_TEMP_2 | 69.4181 | 94.4689 | 74.5002 |
| CHL_SWCD_TEMP_3 | 73.9404 | 91.592 | 78.9683 |
| CHL_RW_TEMP_1 | 40.9294 | 73.2534 | 51.8609 |
| CHL_RW_TEMP_2 | 41.3411 | 61.2851 | 47.4923 |
| CHL_RW_TEMP_3 | 41.3745 | 57.5773 | 49.0341 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.129121 |
| CHL_STA_3 | 0 | 1 | 0.00523271 |
| CHL_RWCD_TEMP_1 | 59.3969 | 86.1872 | 64.2377 |
| CHL_RWCD_TEMP_2 | 66.2564 | 86.1872 | 73.1447 |
| CHL_RWCD_TEMP_3 | 73.7968 | 86.1875 | 76.5806 |
| CHL_SW_TEMP_1 | 42.5497 | 54.7116 | 51.9046 |
| CHL_SW_TEMP_2 | 41.39 | 52.199 | 45.7669 |
| CHL_SW_TEMP_3 | 42.0422 | 49.8626 | 45.9755 |
| CT_FAN_SPD_1 | 0 | 1 | 0.210139 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0982023 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00346428 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.210139 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0982023 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00346428 |
| CT_FLOW_1 | 3.55333 | 575.188 | 141.936 |
| CT_FLOW_2 | 2.95952e-08 | 454.254 | 41.2917 |
| CT_FLOW_3 | 2.95952e-08 | 320.552 | 1.67207 |
| CT_POW_1 | 0 | 9.99999 | 1.44535 |
| CT_POW_2 | 0 | 9.99999 | 0.670308 |
| CT_POW_3 | 0 | 9.99999 | 0.0181781 |
| CT_RW_TEMP_1 | 59.4666 | 94.6185 | 65.8466 |
| CT_RW_TEMP_2 | 68.7828 | 94.4689 | 73.5369 |
| CT_RW_TEMP_3 | 68.7828 | 93.3684 | 77.9471 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.129121 |
| CT_STA_3 | 0 | 1 | 0.00523271 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 52.8185 | 85.4834 | 62.1885 |
| CT_SW_TEMP_2 | 65.9553 | 85.4835 | 71.6349 |
| CT_SW_TEMP_3 | 69.6941 | 88.0481 | 75.5586 |
| CWL_PRI_CW_FLOW | 279.303 | 837.977 | 316.852 |
| CWL_PRI_PM_POW_1 | 5.91415 | 35.1592 | 15.0215 |
| CWL_PRI_PM_POW_2 | 0 | 31.1228 | 1.9409 |
| CWL_PRI_PM_POW_3 | 0 | 22.8357 | 0.078736 |
| CWL_PRI_RW_TEMP | 40.9288 | 73.3637 | 51.8608 |
| CWL_PRI_SW_TEMP | 40.8132 | 52.9091 | 50.2065 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 5.88209e-06 | 837.924 | 133.092 |
| CWL_SEC_DP | 529.004 | 979.313 | 956.854 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.97357e+06 | 98474.1 |
| CWL_SEC_PM_POW_1 | 5.59467e-07 | 53.6388 | 7.62957 |
| CWL_SEC_PM_POW_2 | 0 | 51.7275 | 6.21969 |
| CWL_SEC_PM_SPD_1 | 0.344762 | 1.00373 | 0.470302 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.182062 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.232622 |
| CWL_SEC_RW_TEMP | 42.2463 | 61.2992 | 50.4363 |
| CWL_SEC_SW_TEMP | 50.1401 | 73.1409 | 53.4574 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.776202 | 0.230606 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 457682, 1.0: 67858 |
| CHL_STA_3 | 2 | 0.0: 522790, 1.0: 2750 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 457682, 1.0: 67858 |
| CT_STA_3 | 2 | 0.0: 522790, 1.0: 2750 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 0.0: 403288, 1.0: 122252 |

## ChillerPlant_chiller_bias_2.csv

- Size: 406.3 MB (426,079,519 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.566 | 964.753 | 365.775 |
| CDWL_PM_POW_1 | 7.609 | 142.114 | 23.5142 |
| CDWL_PM_POW_2 | 0 | 135.499 | 6.14725 |
| CDWL_PM_POW_3 | 0 | 87.2423 | 0.251282 |
| CDWL_RW_TEMP | 59.3874 | 94.4679 | 65.8613 |
| CDWL_SW_TEMP | 59.2949 | 85.8428 | 64.0971 |
| CHL_CD_FLOW_1 | 201.896 | 492.785 | 321.582 |
| CHL_CD_FLOW_2 | 0.000220392 | 395.431 | 42.4646 |
| CHL_CD_FLOW_3 | 0.000169005 | 321.59 | 1.72865 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.184982 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0643562 |
| CHL_COMP_SPD_CTRL_3 | 0 | 0.957738 | 0.00277877 |
| CHL_CW_FLOW_1 | 175.365 | 428.03 | 279.324 |
| CHL_CW_FLOW_2 | 0.000191431 | 343.469 | 36.8845 |
| CHL_CW_FLOW_3 | 0.000146797 | 279.331 | 1.5015 |
| CHL_POW_1 | 0 | 230.967 | 35.3265 |
| CHL_POW_2 | 0 | 225.632 | 11.6667 |
| CHL_POW_3 | 0 | 204.18 | 0.495962 |
| CHL_SWCD_TEMP_1 | 59.3874 | 94.5601 | 66.0696 |
| CHL_SWCD_TEMP_2 | 68.6321 | 94.4679 | 74.1083 |
| CHL_SWCD_TEMP_3 | 73.942 | 91.387 | 78.8357 |
| CHL_RW_TEMP_1 | 39.0882 | 73.1873 | 50.204 |
| CHL_RW_TEMP_2 | 39.6095 | 60.9249 | 46.0492 |
| CHL_RW_TEMP_3 | 40.9076 | 56.6834 | 48.6541 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.132055 |
| CHL_STA_3 | 0 | 1 | 0.00537352 |
| CHL_RWCD_TEMP_1 | 59.341 | 86.1734 | 64.2394 |
| CHL_RWCD_TEMP_2 | 66.2579 | 86.1734 | 73.2746 |
| CHL_RWCD_TEMP_3 | 74.0875 | 86.1738 | 76.8578 |
| CHL_SW_TEMP_1 | 42.5728 | 55.3012 | 51.9434 |
| CHL_SW_TEMP_2 | 39.7468 | 52.2408 | 44.9477 |
| CHL_SW_TEMP_3 | 42.0402 | 49.7107 | 45.8401 |
| CT_FAN_SPD_1 | 0 | 1 | 0.212374 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0999401 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00354524 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.212374 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0999401 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00354524 |
| CT_FLOW_1 | 3.36476 | 575.124 | 141.846 |
| CT_FLOW_2 | 2.70135e-08 | 452.235 | 42.2303 |
| CT_FLOW_3 | 2.70135e-08 | 320.541 | 1.71677 |
| CT_POW_1 | 0 | 9.99999 | 1.47866 |
| CT_POW_2 | 0 | 9.99999 | 0.673898 |
| CT_POW_3 | 0 | 9.99999 | 0.0184165 |
| CT_RW_TEMP_1 | 59.3879 | 94.4679 | 65.8613 |
| CT_RW_TEMP_2 | 68.8351 | 94.4679 | 73.4798 |
| CT_RW_TEMP_3 | 68.8351 | 93.3196 | 78.3471 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.132055 |
| CT_STA_3 | 0 | 1 | 0.00537352 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 52.8189 | 85.4675 | 62.1878 |
| CT_SW_TEMP_2 | 65.9571 | 85.4677 | 71.5933 |
| CT_SW_TEMP_3 | 69.6949 | 88.106 | 75.8802 |
| CWL_PRI_CW_FLOW | 279.31 | 837.979 | 317.71 |
| CWL_PRI_PM_POW_1 | 5.92071 | 35.2725 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.1069 | 1.98493 |
| CWL_PRI_PM_POW_3 | 0 | 22.2349 | 0.0808325 |
| CWL_PRI_RW_TEMP | 39.0875 | 73.3012 | 50.204 |
| CWL_PRI_SW_TEMP | 38.9729 | 51.4153 | 48.542 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 2.24636e-06 | 837.854 | 90.0822 |
| CWL_SEC_DP | 529.02 | 979.337 | 958.691 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.98406e+06 | 99120.9 |
| CWL_SEC_PM_POW_1 | 2.13014e-07 | 53.6388 | 5.37514 |
| CWL_SEC_PM_POW_2 | 0 | 51.7173 | 3.05953 |
| CWL_SEC_PM_SPD_1 | 0.344814 | 1.00516 | 0.448744 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00004 | 0.110996 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.153924 |
| CWL_SEC_RW_TEMP | 40.4158 | 60.9076 | 48.6474 |
| CWL_SEC_SW_TEMP | 50.0318 | 73.0746 | 53.3363 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.788054 | 0.230317 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 456140, 1.0: 69400 |
| CHL_STA_3 | 2 | 0.0: 522716, 1.0: 2824 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 456140, 1.0: 69400 |
| CT_STA_3 | 2 | 0.0: 522716, 1.0: 2824 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 0.0: 444647, 1.0: 80893 |

## ChillerPlant_chiller_fouling_065.csv

- Size: 410.4 MB (430,296,656 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.576 | 964.751 | 353.027 |
| CDWL_PM_POW_1 | 7.60937 | 141.707 | 23.5801 |
| CDWL_PM_POW_2 | 0 | 135.341 | 4.50259 |
| CDWL_PM_POW_3 | 0 | 86.6554 | 0.0484744 |
| CDWL_RW_TEMP | 59.5787 | 94.8319 | 65.9567 |
| CDWL_SW_TEMP | 59.5298 | 85.8005 | 64.0943 |
| CHL_CD_FLOW_1 | 205.672 | 492.363 | 321.583 |
| CHL_CD_FLOW_2 | 0.000233845 | 415.263 | 31.1121 |
| CHL_CD_FLOW_3 | 0.000175386 | 321.588 | 0.33185 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.222974 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0723319 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.000726795 |
| CHL_CW_FLOW_1 | 178.645 | 427.664 | 279.325 |
| CHL_CW_FLOW_2 | 0.000203116 | 360.695 | 27.0238 |
| CHL_CW_FLOW_3 | 0.000152339 | 279.329 | 0.288243 |
| CHL_POW_1 | 0 | 241.059 | 45.4917 |
| CHL_POW_2 | 0 | 232.853 | 14.5797 |
| CHL_POW_3 | 0 | 230.836 | 0.143516 |
| CHL_SWCD_TEMP_1 | 59.5787 | 93.2064 | 65.9169 |
| CHL_SWCD_TEMP_2 | 69.6735 | 95.8974 | 75.8633 |
| CHL_SWCD_TEMP_3 | 73.6821 | 95.6714 | 78.7903 |
| CHL_RW_TEMP_1 | 42.6654 | 73.1109 | 54.0007 |
| CHL_RW_TEMP_2 | 42.2273 | 64.7273 | 48.2898 |
| CHL_RW_TEMP_3 | 42.2273 | 61.2772 | 48.2763 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.0967576 |
| CHL_STA_3 | 0 | 1 | 0.00103322 |
| CHL_RWCD_TEMP_1 | 59.5761 | 86.0824 | 64.237 |
| CHL_RWCD_TEMP_2 | 68.2312 | 86.0824 | 73.7648 |
| CHL_RWCD_TEMP_3 | 73.1243 | 86.0824 | 76.2314 |
| CHL_SW_TEMP_1 | 42.4641 | 56.8723 | 52.3838 |
| CHL_SW_TEMP_2 | 42.0493 | 53.0142 | 45.169 |
| CHL_SW_TEMP_3 | 42.0493 | 50.2439 | 45.37 |
| CT_FAN_SPD_1 | 0 | 1 | 0.219461 |
| CT_FAN_SPD_2 | 0 | 1 | 0.077195 |
| CT_FAN_SPD_3 | 0 | 1 | 0.000767132 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.219461 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.077195 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.000767132 |
| CT_FLOW_1 | 3.51941 | 574.357 | 143.079 |
| CT_FLOW_2 | 2.91191e-08 | 449.563 | 30.94 |
| CT_FLOW_3 | 2.91191e-08 | 320.535 | 0.328933 |
| CT_POW_1 | 0 | 9.99999 | 1.62898 |
| CT_POW_2 | 0 | 9.99999 | 0.577818 |
| CT_POW_3 | 0 | 9.99999 | 0.00547153 |
| CT_RW_TEMP_1 | 59.5788 | 94.8319 | 65.9567 |
| CT_RW_TEMP_2 | 68.7045 | 94.8319 | 74.4805 |
| CT_RW_TEMP_3 | 68.7045 | 94.8319 | 76.7193 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.0967576 |
| CT_STA_3 | 0 | 1 | 0.00103322 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8249 | 85.7709 | 62.1985 |
| CT_SW_TEMP_2 | 67.9667 | 85.7709 | 72.6082 |
| CT_SW_TEMP_3 | 69.6975 | 86.7594 | 74.9852 |
| CWL_PRI_CW_FLOW | 279.319 | 837.977 | 306.637 |
| CWL_PRI_PM_POW_1 | 6.14426 | 35.2121 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.107 | 1.45429 |
| CWL_PRI_PM_POW_3 | 0 | 21.7758 | 0.0155765 |
| CWL_PRI_RW_TEMP | 42.6653 | 73.184 | 54.0006 |
| CWL_PRI_SW_TEMP | 42.5608 | 56.6923 | 52.3163 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 5.0425e-06 | 837.946 | 404.094 |
| CWL_SEC_DP | 529.04 | 979.643 | 956.195 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.7978e+06 | 92053 |
| CWL_SEC_PM_POW_1 | 4.78073e-07 | 53.6387 | 22.1293 |
| CWL_SEC_PM_POW_2 | 0 | 51.7319 | 21.395 |
| CWL_SEC_PM_SPD_1 | 0.3449 | 1.00244 | 0.68272 |
| CWL_SEC_PM_SPD_2 | 0 | 1.0001 | 0.549069 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.640899 |
| CWL_SEC_RW_TEMP | 43.9228 | 62.4519 | 52.9979 |
| CWL_SEC_SW_TEMP | 50.3128 | 73.0011 | 54.3557 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.778306 | 0.222623 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 474690, 1.0: 50850 |
| CHL_STA_3 | 2 | 0.0: 524997, 1.0: 543 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 474690, 1.0: 50850 |
| CT_STA_3 | 2 | 0.0: 524997, 1.0: 543 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 336818, 0.0: 188722 |

## ChillerPlant_chiller_fouling_095.csv

- Size: 413.1 MB (433,209,407 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.561 | 964.749 | 362.984 |
| CDWL_PM_POW_1 | 7.60929 | 142.149 | 23.5075 |
| CDWL_PM_POW_2 | 0 | 135.493 | 5.78768 |
| CDWL_PM_POW_3 | 0 | 87.104 | 0.207217 |
| CDWL_RW_TEMP | 59.5757 | 94.461 | 65.8126 |
| CDWL_SW_TEMP | 59.5267 | 85.828 | 64.0903 |
| CHL_CD_FLOW_1 | 202.36 | 493.648 | 321.583 |
| CHL_CD_FLOW_2 | 0.000212494 | 406.84 | 39.978 |
| CHL_CD_FLOW_3 | 0.000169784 | 321.588 | 1.42356 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.159888 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0803285 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00277405 |
| CHL_CW_FLOW_1 | 175.769 | 428.78 | 279.325 |
| CHL_CW_FLOW_2 | 0.000184571 | 353.379 | 34.7247 |
| CHL_CW_FLOW_3 | 0.000147473 | 279.33 | 1.2365 |
| CHL_POW_1 | 0 | 233.213 | 29.9516 |
| CHL_POW_2 | 0 | 225.903 | 15.1338 |
| CHL_POW_3 | 0 | 221.531 | 0.512757 |
| CHL_SWCD_TEMP_1 | 59.5756 | 94.4609 | 65.8202 |
| CHL_SWCD_TEMP_2 | 69.7072 | 94.5843 | 75.1694 |
| CHL_SWCD_TEMP_3 | 73.9343 | 92.2147 | 79.5854 |
| CHL_RW_TEMP_1 | 42.4997 | 73.2092 | 53.5117 |
| CHL_RW_TEMP_2 | 42.2273 | 61.894 | 49.2188 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9412 | 49.3796 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124325 |
| CHL_STA_3 | 0 | 1 | 0.00442783 |
| CHL_RWCD_TEMP_1 | 59.573 | 86.1958 | 64.2325 |
| CHL_RWCD_TEMP_2 | 66.2467 | 86.1958 | 73.0059 |
| CHL_RWCD_TEMP_3 | 73.2735 | 86.189 | 76.8438 |
| CHL_SW_TEMP_1 | 42.4082 | 54.5484 | 51.8927 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6893 | 46.5644 |
| CHL_SW_TEMP_3 | 42.0492 | 49.9922 | 46.0105 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205815 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0951358 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00290017 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205815 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0951358 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00290017 |
| CT_FLOW_1 | 3.48618 | 575.143 | 142.183 |
| CT_FLOW_2 | 2.86578e-08 | 454.486 | 39.757 |
| CT_FLOW_3 | 2.86578e-08 | 320.535 | 1.41242 |
| CT_POW_1 | 0 | 9.99999 | 1.40973 |
| CT_POW_2 | 0 | 9.99999 | 0.659519 |
| CT_POW_3 | 0 | 9.99999 | 0.0150539 |
| CT_RW_TEMP_1 | 59.5757 | 94.4609 | 65.8126 |
| CT_RW_TEMP_2 | 68.7045 | 94.4263 | 73.6905 |
| CT_RW_TEMP_3 | 68.7045 | 93.3705 | 78.2725 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124325 |
| CT_STA_3 | 0 | 1 | 0.00442783 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5363 |
| CT_SW_TEMP_1 | 52.8188 | 85.518 | 62.187 |
| CT_SW_TEMP_2 | 65.9534 | 85.5182 | 71.8342 |
| CT_SW_TEMP_3 | 69.6975 | 88.0666 | 76.0128 |
| CWL_PRI_CW_FLOW | 279.306 | 837.975 | 315.286 |
| CWL_PRI_PM_POW_1 | 5.94801 | 35.3961 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.0169 | 1.86883 |
| CWL_PRI_PM_POW_3 | 0 | 22.8304 | 0.0666264 |
| CWL_PRI_RW_TEMP | 42.4998 | 73.3044 | 53.5116 |
| CWL_PRI_SW_TEMP | 42.3946 | 54.5486 | 51.8912 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9324 |
| CWL_SEC_CW_FLOW | 1.10614e-06 | 837.935 | 438.882 |
| CWL_SEC_DP | 529.011 | 979.668 | 956.462 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90535e+06 | 96007 |
| CWL_SEC_PM_POW_1 | 1.04913e-07 | 53.6388 | 24.4339 |
| CWL_SEC_PM_POW_2 | 0 | 51.7294 | 23.4913 |
| CWL_SEC_PM_SPD_1 | 0.344682 | 1.00265 | 0.705545 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00008 | 0.565099 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635655 |
| CWL_SEC_RW_TEMP | 43.869 | 61.8135 | 52.0646 |
| CWL_SEC_SW_TEMP | 50.1591 | 73.0978 | 53.9728 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.780373 | 0.228338 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460202, 1.0: 65338 |
| CHL_STA_3 | 2 | 0.0: 523213, 1.0: 2327 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460202, 1.0: 65338 |
| CT_STA_3 | 2 | 0.0: 523213, 1.0: 2327 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334062, 0.0: 191478 |

## ChillerPlant_coolingtower_bias_-1.csv

- Size: 408.6 MB (428,458,030 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.574 | 964.749 | 362.988 |
| CDWL_PM_POW_1 | 7.60978 | 142.168 | 23.5477 |
| CDWL_PM_POW_2 | 0 | 135.492 | 5.79168 |
| CDWL_PM_POW_3 | 0 | 87.2852 | 0.204175 |
| CDWL_RW_TEMP | 59.6173 | 96.3058 | 66.1697 |
| CDWL_SW_TEMP | 59.5687 | 87.2375 | 64.4513 |
| CHL_CD_FLOW_1 | 202.225 | 492.882 | 321.583 |
| CHL_CD_FLOW_2 | 0.000251078 | 415.293 | 40.0037 |
| CHL_CD_FLOW_3 | 0.000169558 | 321.589 | 1.40116 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152973 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0809938 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00274634 |
| CHL_CW_FLOW_1 | 175.652 | 428.114 | 279.325 |
| CHL_CW_FLOW_2 | 0.000218085 | 360.721 | 34.747 |
| CHL_CW_FLOW_3 | 0.000147277 | 279.33 | 1.21704 |
| CHL_POW_1 | 0 | 233.574 | 28.6961 |
| CHL_POW_2 | 0 | 227.11 | 15.3455 |
| CHL_POW_3 | 0 | 221.628 | 0.507643 |
| CHL_SWCD_TEMP_1 | 59.6173 | 96.3055 | 66.1754 |
| CHL_SWCD_TEMP_2 | 70.0508 | 95.3256 | 75.736 |
| CHL_SWCD_TEMP_3 | 73.9347 | 92.8084 | 79.9529 |
| CHL_RW_TEMP_1 | 42.4862 | 73.2188 | 53.5096 |
| CHL_RW_TEMP_2 | 42.2273 | 61.7675 | 49.2222 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9733 | 49.3731 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124403 |
| CHL_STA_3 | 0 | 1 | 0.00436123 |
| CHL_RWCD_TEMP_1 | 59.6149 | 87.5164 | 64.5938 |
| CHL_RWCD_TEMP_2 | 67.1576 | 87.0674 | 73.8871 |
| CHL_RWCD_TEMP_3 | 73.3018 | 87.0647 | 77.3642 |
| CHL_SW_TEMP_1 | 42.3811 | 54.53 | 51.8889 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6976 | 46.5647 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8107 | 46.01 |
| CT_FAN_SPD_1 | 0 | 1 | 0.163517 |
| CT_FAN_SPD_2 | 0 | 1 | 0.102507 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00300012 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.163517 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.102507 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00300012 |
| CT_FLOW_1 | 3.68483 | 575.176 | 142.31 |
| CT_FLOW_2 | 3.14903e-08 | 454.46 | 39.782 |
| CT_FLOW_3 | 3.14903e-08 | 320.538 | 1.39043 |
| CT_POW_1 | 0 | 9.99999 | 0.80014 |
| CT_POW_2 | 0 | 9.99999 | 0.80291 |
| CT_POW_3 | 0 | 9.99999 | 0.0171297 |
| CT_RW_TEMP_1 | 59.6174 | 96.3054 | 66.1697 |
| CT_RW_TEMP_2 | 68.7045 | 95.3256 | 74.2955 |
| CT_RW_TEMP_3 | 68.7045 | 94.2393 | 78.6612 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124403 |
| CT_STA_3 | 0 | 1 | 0.00436123 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 51.0182 | 85.3528 | 60.856 |
| CT_SW_TEMP_2 | 65.959 | 85.8058 | 72.03 |
| CT_SW_TEMP_3 | 69.6975 | 88.332 | 76.1747 |
| CWL_PRI_CW_FLOW | 279.317 | 837.975 | 315.289 |
| CWL_PRI_PM_POW_1 | 5.94007 | 35.2864 | 15.0217 |
| CWL_PRI_PM_POW_2 | 0 | 30.9389 | 1.87008 |
| CWL_PRI_PM_POW_3 | 0 | 22.8335 | 0.0656487 |
| CWL_PRI_RW_TEMP | 42.4862 | 73.3144 | 53.5096 |
| CWL_PRI_SW_TEMP | 42.3811 | 54.5306 | 51.8886 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 1.92731e-06 | 837.93 | 444.675 |
| CWL_SEC_DP | 529.011 | 979.461 | 956.495 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90617e+06 | 96026.1 |
| CWL_SEC_PM_POW_1 | 6.82853e-07 | 53.6388 | 24.9724 |
| CWL_SEC_PM_POW_2 | 0 | 51.7284 | 23.9658 |
| CWL_SEC_PM_SPD_1 | 0.344676 | 1.00136 | 0.710288 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00008 | 0.568488 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635813 |
| CWL_SEC_RW_TEMP | 43.8652 | 61.7642 | 52.0594 |
| CWL_SEC_SW_TEMP | 50.1502 | 73.1074 | 53.9745 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.768169 | 0.228788 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460161, 1.0: 65379 |
| CHL_STA_3 | 2 | 0.0: 523248, 1.0: 2292 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460161, 1.0: 65379 |
| CT_STA_3 | 2 | 0.0: 523248, 1.0: 2292 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334145, 0.0: 191395 |

## ChillerPlant_coolingtower_bias_-2.csv

- Size: 409.5 MB (429,383,143 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.575 | 964.755 | 363.001 |
| CDWL_PM_POW_1 | 7.61004 | 142.057 | 23.5826 |
| CDWL_PM_POW_2 | 0 | 135.49 | 5.79026 |
| CDWL_PM_POW_3 | 0 | 86.581 | 0.2073 |
| CDWL_RW_TEMP | 59.6545 | 97.7909 | 66.5474 |
| CDWL_SW_TEMP | 59.6061 | 89.0384 | 64.8262 |
| CHL_CD_FLOW_1 | 201.861 | 493.463 | 321.582 |
| CHL_CD_FLOW_2 | 0.000262492 | 414.5 | 39.9947 |
| CHL_CD_FLOW_3 | 0.000168947 | 321.589 | 1.42414 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.154033 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0817835 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00284385 |
| CHL_CW_FLOW_1 | 175.335 | 428.619 | 279.325 |
| CHL_CW_FLOW_2 | 0.000227999 | 360.032 | 34.7392 |
| CHL_CW_FLOW_3 | 0.000146746 | 279.33 | 1.237 |
| CHL_POW_1 | 0 | 234.717 | 29.2772 |
| CHL_POW_2 | 0 | 228.54 | 15.5885 |
| CHL_POW_3 | 0 | 224.2 | 0.527362 |
| CHL_SWCD_TEMP_1 | 59.6544 | 97.7908 | 66.5537 |
| CHL_SWCD_TEMP_2 | 70.1794 | 96.3442 | 76.243 |
| CHL_SWCD_TEMP_3 | 73.935 | 93.5259 | 80.3373 |
| CHL_RW_TEMP_1 | 42.5542 | 73.2191 | 53.512 |
| CHL_RW_TEMP_2 | 42.2273 | 61.8138 | 49.2216 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9091 | 49.3927 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124379 |
| CHL_STA_3 | 0 | 1 | 0.00443163 |
| CHL_RWCD_TEMP_1 | 59.6523 | 89.3173 | 64.9689 |
| CHL_RWCD_TEMP_2 | 68.0613 | 88.0091 | 74.7006 |
| CHL_RWCD_TEMP_3 | 73.3314 | 88.0068 | 77.8827 |
| CHL_SW_TEMP_1 | 42.4483 | 54.53 | 51.8917 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6993 | 46.5649 |
| CHL_SW_TEMP_3 | 42.0492 | 50.0094 | 46.013 |
| CT_FAN_SPD_1 | 0 | 1 | 0.131422 |
| CT_FAN_SPD_2 | 0 | 1 | 0.109388 |
| CT_FAN_SPD_3 | 0 | 1 | 0.0031715 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.131422 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.109388 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.0031715 |
| CT_FLOW_1 | 3.78313 | 574.027 | 142.559 |
| CT_FLOW_2 | 3.29589e-08 | 454.507 | 39.773 |
| CT_FLOW_3 | 3.29589e-08 | 320.538 | 1.41318 |
| CT_POW_1 | 0 | 9.99999 | 0.466125 |
| CT_POW_2 | 0 | 9.99999 | 0.944471 |
| CT_POW_3 | 0 | 9.99999 | 0.0196193 |
| CT_RW_TEMP_1 | 59.6545 | 97.7907 | 66.5474 |
| CT_RW_TEMP_2 | 68.7045 | 96.3442 | 74.8491 |
| CT_RW_TEMP_3 | 68.7045 | 94.989 | 79.0801 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124379 |
| CT_STA_3 | 0 | 1 | 0.00443163 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5359 |
| CT_SW_TEMP_1 | 49.2182 | 85.3565 | 59.5392 |
| CT_SW_TEMP_2 | 65.9668 | 86.0649 | 72.1871 |
| CT_SW_TEMP_3 | 69.6975 | 88.68 | 76.3384 |
| CWL_PRI_CW_FLOW | 279.318 | 837.98 | 315.301 |
| CWL_PRI_PM_POW_1 | 5.91867 | 35.3695 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.1054 | 1.8696 |
| CWL_PRI_PM_POW_3 | 0 | 22.7838 | 0.0666568 |
| CWL_PRI_RW_TEMP | 42.5545 | 73.3146 | 53.512 |
| CWL_PRI_SW_TEMP | 42.4484 | 54.5306 | 51.8914 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 2.13047e-06 | 837.914 | 445.423 |
| CWL_SEC_DP | 529.006 | 979.479 | 956.427 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90626e+06 | 96022.5 |
| CWL_SEC_PM_POW_1 | 5.15737e-07 | 53.6388 | 25.034 |
| CWL_SEC_PM_POW_2 | 0 | 51.7263 | 24.0166 |
| CWL_SEC_PM_SPD_1 | 0.344678 | 1.00136 | 0.710845 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00006 | 0.56892 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635875 |
| CWL_SEC_RW_TEMP | 43.8606 | 61.7642 | 52.067 |
| CWL_SEC_SW_TEMP | 50.1912 | 73.1076 | 53.9743 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.76226 | 0.228583 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460174, 1.0: 65366 |
| CHL_STA_3 | 2 | 0.0: 523211, 1.0: 2329 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460174, 1.0: 65366 |
| CT_STA_3 | 2 | 0.0: 523211, 1.0: 2329 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334178, 0.0: 191362 |

## ChillerPlant_coolingtower_bias_1.csv

- Size: 410.4 MB (430,370,457 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.569 | 964.751 | 362.989 |
| CDWL_PM_POW_1 | 7.60933 | 141.915 | 22.6185 |
| CDWL_PM_POW_2 | 0 | 135.492 | 5.79147 |
| CDWL_PM_POW_3 | 0 | 86.461 | 0.203924 |
| CDWL_RW_TEMP | 59.5666 | 94.4826 | 65.5442 |
| CDWL_SW_TEMP | 59.5174 | 85.6043 | 63.8365 |
| CHL_CD_FLOW_1 | 202.662 | 492.915 | 321.582 |
| CHL_CD_FLOW_2 | 0.000224797 | 408.592 | 40.0056 |
| CHL_CD_FLOW_3 | 0.000170291 | 321.589 | 1.40086 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.151684 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0797296 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00268141 |
| CHL_CW_FLOW_1 | 176.031 | 428.143 | 279.325 |
| CHL_CW_FLOW_2 | 0.000195257 | 354.901 | 34.7487 |
| CHL_CW_FLOW_3 | 0.000147914 | 279.33 | 1.21678 |
| CHL_POW_1 | 0 | 231.993 | 27.8365 |
| CHL_POW_2 | 0 | 225.267 | 14.93 |
| CHL_POW_3 | 0 | 221.928 | 0.493926 |
| CHL_SWCD_TEMP_1 | 59.5666 | 94.4826 | 65.5499 |
| CHL_SWCD_TEMP_2 | 68.4752 | 94.4826 | 74.5391 |
| CHL_SWCD_TEMP_3 | 73.9342 | 92.13 | 79.2423 |
| CHL_RW_TEMP_1 | 42.4938 | 73.2186 | 53.5075 |
| CHL_RW_TEMP_2 | 42.2273 | 61.7154 | 49.223 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9732 | 49.3589 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124415 |
| CHL_STA_3 | 0 | 1 | 0.00435742 |
| CHL_RWCD_TEMP_1 | 59.5637 | 86.0364 | 63.9734 |
| CHL_RWCD_TEMP_2 | 64.6844 | 86.0364 | 72.0662 |
| CHL_RWCD_TEMP_3 | 73.2556 | 86.0401 | 76.3707 |
| CHL_SW_TEMP_1 | 42.3888 | 54.53 | 51.8866 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6951 | 46.5655 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8032 | 46.0082 |
| CT_FAN_SPD_1 | 0 | 1 | 0.27324 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0890342 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00274068 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.27324 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0890342 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00274068 |
| CT_FLOW_1 | 3.5035 | 575.156 | 136.113 |
| CT_FLOW_2 | 2.88976e-08 | 448.846 | 39.7843 |
| CT_FLOW_3 | 2.88976e-08 | 320.538 | 1.39026 |
| CT_POW_1 | 0 | 9.99999 | 2.08909 |
| CT_POW_2 | 0 | 9.99999 | 0.552875 |
| CT_POW_3 | 0 | 9.99999 | 0.0131033 |
| CT_RW_TEMP_1 | 59.5667 | 94.4826 | 65.5442 |
| CT_RW_TEMP_2 | 68.4313 | 94.4826 | 73.0017 |
| CT_RW_TEMP_3 | 68.7045 | 92.8241 | 77.8911 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124415 |
| CT_STA_3 | 0 | 1 | 0.00435742 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 54.2974 | 87.0632 | 63.5574 |
| CT_SW_TEMP_2 | 65.9429 | 85.3825 | 71.5466 |
| CT_SW_TEMP_3 | 69.6975 | 87.7486 | 75.8672 |
| CWL_PRI_CW_FLOW | 279.313 | 837.977 | 315.29 |
| CWL_PRI_PM_POW_1 | 5.96578 | 35.291 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 30.9868 | 1.87006 |
| CWL_PRI_PM_POW_3 | 0 | 21.6658 | 0.0655713 |
| CWL_PRI_RW_TEMP | 42.4938 | 73.314 | 53.5075 |
| CWL_PRI_SW_TEMP | 42.3888 | 54.5306 | 51.8863 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 1.9273e-06 | 837.929 | 443.251 |
| CWL_SEC_DP | 529.007 | 979.496 | 956.521 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90608e+06 | 96030.5 |
| CWL_SEC_PM_POW_1 | 7.11923e-07 | 53.6388 | 24.8469 |
| CWL_SEC_PM_POW_2 | 0 | 51.7282 | 23.8684 |
| CWL_SEC_PM_SPD_1 | 0.344676 | 1.00657 | 0.709093 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.567712 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635704 |
| CWL_SEC_RW_TEMP | 43.8736 | 61.7642 | 52.0521 |
| CWL_SEC_SW_TEMP | 50.1452 | 73.1071 | 53.9736 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.779302 | 0.234847 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460155, 1.0: 65385 |
| CHL_STA_3 | 2 | 0.0: 523250, 1.0: 2290 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460155, 1.0: 65385 |
| CT_STA_3 | 2 | 0.0: 523250, 1.0: 2290 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334088, 0.0: 191452 |

## ChillerPlant_coolingtower_bias_2.csv

- Size: 414.3 MB (434,412,715 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.576 | 964.754 | 362.989 |
| CDWL_PM_POW_1 | 7.60544 | 141.895 | 21.7999 |
| CDWL_PM_POW_2 | 0 | 135.492 | 5.79151 |
| CDWL_PM_POW_3 | 0 | 86.4611 | 0.20392 |
| CDWL_RW_TEMP | 59.4034 | 94.4826 | 65.4151 |
| CDWL_SW_TEMP | 59.3524 | 85.5795 | 63.7133 |
| CHL_CD_FLOW_1 | 202.696 | 492.951 | 321.582 |
| CHL_CD_FLOW_2 | 0.000226467 | 408.476 | 40.0058 |
| CHL_CD_FLOW_3 | 0.000170348 | 321.589 | 1.40082 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.15166 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0796551 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00267846 |
| CHL_CW_FLOW_1 | 176.061 | 428.174 | 279.325 |
| CHL_CW_FLOW_2 | 0.000196708 | 354.8 | 34.7488 |
| CHL_CW_FLOW_3 | 0.000147963 | 279.33 | 1.21674 |
| CHL_POW_1 | 0 | 231.492 | 27.7366 |
| CHL_POW_2 | 0 | 225.049 | 14.9049 |
| CHL_POW_3 | 0 | 221.926 | 0.49329 |
| CHL_SWCD_TEMP_1 | 59.4034 | 94.4826 | 65.4212 |
| CHL_SWCD_TEMP_2 | 67.2855 | 94.4826 | 74.1029 |
| CHL_SWCD_TEMP_3 | 73.9341 | 92.1322 | 79.1617 |
| CHL_RW_TEMP_1 | 42.4938 | 73.2187 | 53.5075 |
| CHL_RW_TEMP_2 | 42.2273 | 61.7102 | 49.2233 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9771 | 49.3584 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124417 |
| CHL_STA_3 | 0 | 1 | 0.00435742 |
| CHL_RWCD_TEMP_1 | 59.3985 | 86.0115 | 63.8452 |
| CHL_RWCD_TEMP_2 | 64.5736 | 86.0115 | 71.3728 |
| CHL_RWCD_TEMP_3 | 73.2467 | 86.0152 | 76.2456 |
| CHL_SW_TEMP_1 | 42.3888 | 54.5298 | 51.8865 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6953 | 46.5657 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8025 | 46.0076 |
| CT_FAN_SPD_1 | 0 | 1 | 0.383018 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0885398 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00272999 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.383018 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0885398 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00272999 |
| CT_FLOW_1 | 1.15504 | 575.146 | 127.86 |
| CT_FLOW_2 | 6.48179e-09 | 448.848 | 39.7844 |
| CT_FLOW_3 | 6.48179e-09 | 320.538 | 1.39019 |
| CT_POW_1 | 0 | 9.99999 | 2.3996 |
| CT_POW_2 | 0 | 9.99999 | 0.550784 |
| CT_POW_3 | 0 | 9.99999 | 0.0129566 |
| CT_RW_TEMP_1 | 59.4036 | 94.4826 | 65.415 |
| CT_RW_TEMP_2 | 67.196 | 94.4826 | 72.5264 |
| CT_RW_TEMP_3 | 68.7045 | 92.7908 | 77.8086 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124417 |
| CT_STA_3 | 0 | 1 | 0.00435742 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 54.2974 | 88.8455 | 64.7535 |
| CT_SW_TEMP_2 | 65.9432 | 85.3775 | 71.2838 |
| CT_SW_TEMP_3 | 69.6975 | 87.6728 | 75.8326 |
| CWL_PRI_CW_FLOW | 279.319 | 837.98 | 315.29 |
| CWL_PRI_PM_POW_1 | 5.96778 | 35.2962 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.1094 | 1.87008 |
| CWL_PRI_PM_POW_3 | 0 | 21.666 | 0.0655691 |
| CWL_PRI_RW_TEMP | 42.4938 | 73.3143 | 53.5074 |
| CWL_PRI_SW_TEMP | 42.3888 | 54.5303 | 51.8862 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 2.12532e-06 | 837.929 | 442.86 |
| CWL_SEC_DP | 529.008 | 979.618 | 956.522 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90625e+06 | 96030.4 |
| CWL_SEC_PM_POW_1 | 6.8887e-07 | 53.6388 | 24.8096 |
| CWL_SEC_PM_POW_2 | 0 | 51.7282 | 23.8344 |
| CWL_SEC_PM_SPD_1 | 0.344675 | 1.00657 | 0.70879 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.567468 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635685 |
| CWL_SEC_RW_TEMP | 43.8744 | 61.7642 | 52.0516 |
| CWL_SEC_SW_TEMP | 50.1452 | 73.1072 | 53.9735 |
| OA_TEMP | -9.75686 | 80.4784 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.972233 | 0.273727 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460154, 1.0: 65386 |
| CHL_STA_3 | 2 | 0.0: 523250, 1.0: 2290 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460154, 1.0: 65386 |
| CT_STA_3 | 2 | 0.0: 523250, 1.0: 2290 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334078, 0.0: 191462 |

## ChillerPlant_coolingtower_fouling_065.csv

- Size: 406.3 MB (426,059,644 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.578 | 964.758 | 362.965 |
| CDWL_PM_POW_1 | 7.61941 | 141.362 | 24.3049 |
| CDWL_PM_POW_2 | 0 | 135.491 | 5.78836 |
| CDWL_PM_POW_3 | 0 | 86.8052 | 0.203921 |
| CDWL_RW_TEMP | 59.7025 | 97.5105 | 66.3055 |
| CDWL_SW_TEMP | 59.6543 | 89.0378 | 64.5831 |
| CHL_CD_FLOW_1 | 202.781 | 493.733 | 321.584 |
| CHL_CD_FLOW_2 | 0.000231378 | 415.027 | 39.9798 |
| CHL_CD_FLOW_3 | 0.000170491 | 321.589 | 1.40121 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.153388 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0808082 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00273682 |
| CHL_CW_FLOW_1 | 176.135 | 428.854 | 279.326 |
| CHL_CW_FLOW_2 | 0.000200973 | 360.49 | 34.7262 |
| CHL_CW_FLOW_3 | 0.000148087 | 279.33 | 1.21709 |
| CHL_POW_1 | 0 | 236.79 | 28.8878 |
| CHL_POW_2 | 0 | 227.615 | 15.2965 |
| CHL_POW_3 | 0 | 225.699 | 0.505967 |
| CHL_SWCD_TEMP_1 | 59.7025 | 97.5112 | 66.313 |
| CHL_SWCD_TEMP_2 | 69.7528 | 96.2825 | 75.2803 |
| CHL_SWCD_TEMP_3 | 73.9349 | 92.9385 | 79.6878 |
| CHL_RW_TEMP_1 | 42.5341 | 73.2192 | 53.5111 |
| CHL_RW_TEMP_2 | 42.2274 | 61.8472 | 49.2233 |
| CHL_RW_TEMP_3 | 42.2274 | 57.9092 | 49.3773 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124341 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.7008 | 89.3172 | 64.7302 |
| CHL_RWCD_TEMP_2 | 66.3202 | 87.5043 | 73.2067 |
| CHL_RWCD_TEMP_3 | 73.425 | 87.4537 | 77.0417 |
| CHL_SW_TEMP_1 | 42.4285 | 54.526 | 51.8902 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6933 | 46.5658 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8089 | 46.0086 |
| CT_FAN_SPD_1 | 0 | 1 | 0.249364 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0992253 |
| CT_FAN_SPD_3 | 0 | 1 | 0.0029502 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.249364 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0992253 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.0029502 |
| CT_FLOW_1 | 6.30625 | 574.657 | 152.29 |
| CT_FLOW_2 | 8.69528e-08 | 450.461 | 39.7585 |
| CT_FLOW_3 | 8.69528e-08 | 320.538 | 1.39076 |
| CT_POW_1 | 0 | 9.99999 | 2.16147 |
| CT_POW_2 | 0 | 9.99999 | 0.744636 |
| CT_POW_3 | 0 | 9.99999 | 0.0161799 |
| CT_RW_TEMP_1 | 59.7025 | 97.5111 | 66.3055 |
| CT_RW_TEMP_2 | 68.7065 | 96.2825 | 73.7959 |
| CT_RW_TEMP_3 | 68.7065 | 94.2652 | 78.3691 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124341 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5363 |
| CT_SW_TEMP_1 | 55.2261 | 88.9553 | 63.4408 |
| CT_SW_TEMP_2 | 65.9401 | 85.8466 | 71.8635 |
| CT_SW_TEMP_3 | 69.6985 | 88.1768 | 76.0512 |
| CWL_PRI_CW_FLOW | 279.321 | 837.983 | 315.269 |
| CWL_PRI_PM_POW_1 | 5.97278 | 35.4083 | 15.0218 |
| CWL_PRI_PM_POW_2 | 0 | 30.9941 | 1.86909 |
| CWL_PRI_PM_POW_3 | 0 | 22.2837 | 0.0655816 |
| CWL_PRI_RW_TEMP | 42.5342 | 73.3147 | 53.511 |
| CWL_PRI_SW_TEMP | 42.4286 | 54.5266 | 51.8899 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 6.31599e-06 | 837.929 | 444.166 |
| CWL_SEC_DP | 529 | 979.552 | 956.502 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90636e+06 | 96020.6 |
| CWL_SEC_PM_POW_1 | 6.04476e-07 | 53.6388 | 24.9259 |
| CWL_SEC_PM_POW_2 | 0 | 51.7281 | 23.9313 |
| CWL_SEC_PM_SPD_1 | 0.34468 | 1.00137 | 0.709845 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.568228 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635763 |
| CWL_SEC_RW_TEMP | 43.8639 | 61.7569 | 52.0621 |
| CWL_SEC_SW_TEMP | 50.1803 | 73.1078 | 53.9751 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.63624 | 0.162072 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460194, 1.0: 65346 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460194, 1.0: 65346 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334119, 0.0: 191421 |

## ChillerPlant_coolingtower_fouling_080.csv

- Size: 406.4 MB (426,117,020 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.576 | 964.752 | 362.979 |
| CDWL_PM_POW_1 | 7.61307 | 142.16 | 23.8741 |
| CDWL_PM_POW_2 | 0 | 135.492 | 5.79026 |
| CDWL_PM_POW_3 | 0 | 87.2971 | 0.204096 |
| CDWL_RW_TEMP | 59.6385 | 95.5646 | 66.0034 |
| CDWL_SW_TEMP | 59.59 | 86.847 | 64.2853 |
| CHL_CD_FLOW_1 | 201.824 | 492.885 | 321.582 |
| CHL_CD_FLOW_2 | 0.000235846 | 415.227 | 39.9959 |
| CHL_CD_FLOW_3 | 0.000168885 | 321.589 | 1.40085 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.15247 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.080381 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00271641 |
| CHL_CW_FLOW_1 | 175.303 | 428.117 | 279.324 |
| CHL_CW_FLOW_2 | 0.000204854 | 360.664 | 34.7402 |
| CHL_CW_FLOW_3 | 0.000146692 | 279.33 | 1.21677 |
| CHL_POW_1 | 0 | 234.727 | 28.4248 |
| CHL_POW_2 | 0 | 226.254 | 15.155 |
| CHL_POW_3 | 0 | 222.848 | 0.501492 |
| CHL_SWCD_TEMP_1 | 59.6385 | 95.5648 | 66.0098 |
| CHL_SWCD_TEMP_2 | 69.8057 | 95.3787 | 75.2059 |
| CHL_SWCD_TEMP_3 | 73.9347 | 92.5426 | 79.5792 |
| CHL_RW_TEMP_1 | 42.4853 | 73.2187 | 53.5088 |
| CHL_RW_TEMP_2 | 42.2272 | 61.7767 | 49.2223 |
| CHL_RW_TEMP_3 | 42.2272 | 57.9611 | 49.364 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124377 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.6363 | 87.1261 | 64.4298 |
| CHL_RWCD_TEMP_2 | 66.2328 | 86.7465 | 73.089 |
| CHL_RWCD_TEMP_3 | 73.3543 | 86.751 | 76.8869 |
| CHL_SW_TEMP_1 | 42.3802 | 54.5281 | 51.8879 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6969 | 46.5649 |
| CHL_SW_TEMP_3 | 42.0492 | 49.806 | 46.0087 |
| CT_FAN_SPD_1 | 0 | 1 | 0.232051 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0958586 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00287104 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.232051 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0958586 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00287104 |
| CT_FLOW_1 | 4.77815 | 575.159 | 146.919 |
| CT_FLOW_2 | 5.04525e-08 | 453.507 | 39.7742 |
| CT_FLOW_3 | 5.04525e-08 | 320.539 | 1.39017 |
| CT_POW_1 | 0 | 9.99999 | 1.88048 |
| CT_POW_2 | 0 | 9.99999 | 0.674403 |
| CT_POW_3 | 0 | 9.99999 | 0.0150142 |
| CT_RW_TEMP_1 | 59.6385 | 95.5648 | 66.0034 |
| CT_RW_TEMP_2 | 68.7054 | 95.3787 | 73.7183 |
| CT_RW_TEMP_3 | 68.7054 | 93.6524 | 78.2541 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124377 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 54.1758 | 86.9255 | 62.7914 |
| CT_SW_TEMP_2 | 65.9524 | 85.6306 | 71.8492 |
| CT_SW_TEMP_3 | 69.6976 | 88.0516 | 76.0107 |
| CWL_PRI_CW_FLOW | 279.319 | 837.978 | 315.281 |
| CWL_PRI_PM_POW_1 | 5.91651 | 35.2867 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.0454 | 1.86962 |
| CWL_PRI_PM_POW_3 | 0 | 22.7621 | 0.0656253 |
| CWL_PRI_RW_TEMP | 42.4853 | 73.3143 | 53.5088 |
| CWL_PRI_SW_TEMP | 42.3802 | 54.5287 | 51.8876 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 1.94224e-06 | 837.929 | 443.912 |
| CWL_SEC_DP | 529.002 | 979.552 | 956.515 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90611e+06 | 96025.8 |
| CWL_SEC_PM_POW_1 | 6.08407e-07 | 53.6388 | 24.9056 |
| CWL_SEC_PM_POW_2 | 0 | 51.7281 | 23.9136 |
| CWL_SEC_PM_SPD_1 | 0.344677 | 1.00137 | 0.70967 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.568068 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635752 |
| CWL_SEC_RW_TEMP | 43.8693 | 61.7589 | 52.0562 |
| CWL_SEC_SW_TEMP | 50.1499 | 73.1073 | 53.9744 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.707048 | 0.194095 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460175, 1.0: 65365 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460175, 1.0: 65365 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334113, 0.0: 191427 |

## ChillerPlant_coolingtower_fouling_095.csv

- Size: 407.5 MB (427,244,611 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.574 | 964.753 | 362.988 |
| CDWL_PM_POW_1 | 7.61 | 141.86 | 23.578 |
| CDWL_PM_POW_2 | 0 | 135.492 | 5.79164 |
| CDWL_PM_POW_3 | 0 | 86.4601 | 0.203998 |
| CDWL_RW_TEMP | 59.5891 | 94.8017 | 65.84 |
| CDWL_SW_TEMP | 59.5403 | 85.8366 | 64.1242 |
| CHL_CD_FLOW_1 | 202.566 | 493.76 | 321.583 |
| CHL_CD_FLOW_2 | 0.000236048 | 412.998 | 40.0047 |
| CHL_CD_FLOW_3 | 0.000170129 | 321.589 | 1.40109 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152223 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0802705 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00270811 |
| CHL_CW_FLOW_1 | 175.948 | 428.877 | 279.325 |
| CHL_CW_FLOW_2 | 0.00020503 | 358.727 | 34.7479 |
| CHL_CW_FLOW_3 | 0.000147773 | 279.33 | 1.21698 |
| CHL_POW_1 | 0 | 232.98 | 28.2163 |
| CHL_POW_2 | 0 | 225.959 | 15.1116 |
| CHL_POW_3 | 0 | 221.994 | 0.499549 |
| CHL_SWCD_TEMP_1 | 59.589 | 94.8015 | 65.8457 |
| CHL_SWCD_TEMP_2 | 69.758 | 94.6823 | 75.1777 |
| CHL_SWCD_TEMP_3 | 73.9344 | 92.2189 | 79.5714 |
| CHL_RW_TEMP_1 | 42.4878 | 73.2186 | 53.5082 |
| CHL_RW_TEMP_2 | 42.2274 | 61.7364 | 49.2223 |
| CHL_RW_TEMP_3 | 42.2274 | 57.9766 | 49.3614 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124407 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.5865 | 86.2852 | 64.2669 |
| CHL_RWCD_TEMP_2 | 66.2499 | 86.2852 | 73.0245 |
| CHL_RWCD_TEMP_3 | 73.2922 | 86.2715 | 76.8514 |
| CHL_SW_TEMP_1 | 42.3828 | 54.5296 | 51.8873 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6959 | 46.5649 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8061 | 46.009 |
| CT_FAN_SPD_1 | 0 | 1 | 0.211381 |
| CT_FAN_SPD_2 | 0 | 1 | 0.095074 |
| CT_FAN_SPD_3 | 0 | 1 | 0.0028552 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.211381 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.095074 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.0028552 |
| CT_FLOW_1 | 3.76888 | 575.131 | 143.124 |
| CT_FLOW_2 | 3.27432e-08 | 448.843 | 39.783 |
| CT_FLOW_3 | 3.27432e-08 | 320.538 | 1.39044 |
| CT_POW_1 | 0 | 9.99999 | 1.51057 |
| CT_POW_2 | 0 | 9.99999 | 0.657295 |
| CT_POW_3 | 0 | 9.99999 | 0.014786 |
| CT_RW_TEMP_1 | 59.5891 | 94.8015 | 65.84 |
| CT_RW_TEMP_2 | 68.7049 | 94.6823 | 73.6879 |
| CT_RW_TEMP_3 | 68.7049 | 93.4036 | 78.2463 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124407 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 53.1533 | 85.706 | 62.32 |
| CT_SW_TEMP_2 | 65.9534 | 85.5448 | 71.8382 |
| CT_SW_TEMP_3 | 69.6979 | 88.0178 | 76.0087 |
| CWL_PRI_CW_FLOW | 279.318 | 837.979 | 315.289 |
| CWL_PRI_PM_POW_1 | 5.96009 | 35.4122 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 30.9299 | 1.87007 |
| CWL_PRI_PM_POW_3 | 0 | 21.6653 | 0.0655938 |
| CWL_PRI_RW_TEMP | 42.4878 | 73.3141 | 53.5081 |
| CWL_PRI_SW_TEMP | 42.3828 | 54.5302 | 51.887 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9324 |
| CWL_SEC_CW_FLOW | 3.23048e-07 | 837.929 | 443.824 |
| CWL_SEC_DP | 529.003 | 979.552 | 956.517 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.9061e+06 | 96028.7 |
| CWL_SEC_PM_POW_1 | 3.06399e-08 | 53.6388 | 24.8982 |
| CWL_SEC_PM_POW_2 | 0 | 51.7282 | 23.9056 |
| CWL_SEC_PM_SPD_1 | 0.344676 | 1.00243 | 0.709619 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00007 | 0.568007 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.635738 |
| CWL_SEC_RW_TEMP | 43.87 | 61.7629 | 52.0548 |
| CWL_SEC_SW_TEMP | 50.146 | 73.1072 | 53.9739 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.763117 | 0.220928 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460159, 1.0: 65381 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460159, 1.0: 65381 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 334106, 0.0: 191434 |

## ChillerPlant_coolingtower_PI.csv

- Size: 409.4 MB (429,257,394 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.565 | 964.751 | 362.001 |
| CDWL_PM_POW_1 | 7.60551 | 142.127 | 23.7567 |
| CDWL_PM_POW_2 | 0 | 135.491 | 5.64475 |
| CDWL_PM_POW_3 | 0 | 86.5324 | 0.20779 |
| CDWL_RW_TEMP | 59.3414 | 123.322 | 67.505 |
| CDWL_SW_TEMP | 59.2886 | 117.172 | 65.788 |
| CHL_CD_FLOW_1 | 201.945 | 493.73 | 321.583 |
| CHL_CD_FLOW_2 | 0.000250761 | 414.967 | 38.9899 |
| CHL_CD_FLOW_3 | 0.000169088 | 321.589 | 1.42745 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.162401 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0799205 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00280632 |
| CHL_CW_FLOW_1 | 175.408 | 428.851 | 279.325 |
| CHL_CW_FLOW_2 | 0.00021781 | 360.438 | 33.8664 |
| CHL_CW_FLOW_3 | 0.000146869 | 279.33 | 1.23987 |
| CHL_POW_1 | 0 | 274.451 | 30.5011 |
| CHL_POW_2 | 0 | 248.515 | 15.2303 |
| CHL_POW_3 | 0 | 222.32 | 0.52009 |
| CHL_SWCD_TEMP_1 | 59.3413 | 123.322 | 67.5124 |
| CHL_SWCD_TEMP_2 | 68.5194 | 98.2939 | 75.5786 |
| CHL_SWCD_TEMP_3 | 73.9386 | 92.8166 | 79.8219 |
| CHL_RW_TEMP_1 | 42.4959 | 73.2193 | 53.6345 |
| CHL_RW_TEMP_2 | 42.2272 | 70.4106 | 49.2826 |
| CHL_RW_TEMP_3 | 42.2272 | 57.9254 | 49.378 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.121254 |
| CHL_STA_3 | 0 | 1 | 0.00443924 |
| CHL_RWCD_TEMP_1 | 59.3347 | 117.451 | 65.9318 |
| CHL_RWCD_TEMP_2 | 66.165 | 101.621 | 73.5367 |
| CHL_RWCD_TEMP_3 | 73.6206 | 87.7066 | 77.1986 |
| CHL_SW_TEMP_1 | 42.3908 | 65.3898 | 52.0274 |
| CHL_SW_TEMP_2 | 42.0492 | 56.4158 | 46.5874 |
| CHL_SW_TEMP_3 | 42.0492 | 50.0024 | 46.0163 |
| CT_FAN_SPD_1 | 0 | 0.960552 | 0.171789 |
| CT_FAN_SPD_2 | 0 | 1 | 0.100407 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00303462 |
| CT_FAN_SPD_CTRL_1 | 0 | 0.960552 | 0.171789 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.100407 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00303462 |
| CT_FLOW_1 | 1.21647 | 575.098 | 143.482 |
| CT_FLOW_2 | 6.87121e-09 | 450.23 | 38.7753 |
| CT_FLOW_3 | 6.87121e-09 | 320.539 | 1.41647 |
| CT_POW_1 | 0 | 9.20349 | 0.5553 |
| CT_POW_2 | 0 | 9.99999 | 0.801504 |
| CT_POW_3 | 0 | 9.99999 | 0.0170801 |
| CT_RW_TEMP_1 | 59.3422 | 123.322 | 67.505 |
| CT_RW_TEMP_2 | 68.4491 | 104.875 | 74.1044 |
| CT_RW_TEMP_3 | 68.7035 | 94.3968 | 78.5264 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.121254 |
| CT_STA_3 | 0 | 1 | 0.00443924 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5362 |
| CT_SW_TEMP_1 | 52.8182 | 117.112 | 63.9855 |
| CT_SW_TEMP_2 | 65.7237 | 85.8767 | 71.9031 |
| CT_SW_TEMP_3 | 69.6952 | 88.3026 | 76.1385 |
| CWL_PRI_CW_FLOW | 279.309 | 837.977 | 314.432 |
| CWL_PRI_PM_POW_1 | 5.92363 | 35.4078 | 15.0217 |
| CWL_PRI_PM_POW_2 | 0 | 31.084 | 1.82269 |
| CWL_PRI_PM_POW_3 | 0 | 22.2434 | 0.0668108 |
| CWL_PRI_RW_TEMP | 42.496 | 73.3149 | 53.6344 |
| CWL_PRI_SW_TEMP | 42.3908 | 65.3896 | 52.0264 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 6.0126e-06 | 837.913 | 451.085 |
| CWL_SEC_DP | 529.003 | 979.479 | 956.485 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.90636e+06 | 94918.6 |
| CWL_SEC_PM_POW_1 | 6.79714e-07 | 53.6388 | 25.4017 |
| CWL_SEC_PM_POW_2 | 0 | 51.7261 | 24.4213 |
| CWL_SEC_PM_SPD_1 | 0.344678 | 1.00658 | 0.714886 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00006 | 0.575137 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.64079 |
| CWL_SEC_RW_TEMP | 43.8655 | 68.5696 | 52.2688 |
| CWL_SEC_SW_TEMP | 50.1566 | 73.1079 | 54.0813 |
| OA_TEMP | -9.75686 | 80.4929 | 44.9141 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.964599 | 0.231383 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 461816, 1.0: 63724 |
| CHL_STA_3 | 2 | 0.0: 523207, 1.0: 2333 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 461816, 1.0: 63724 |
| CT_STA_3 | 2 | 0.0: 523207, 1.0: 2333 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 336761, 0.0: 188779 |

## ChillerPlant_secondary_chilled_water_pressure_bias_-010.csv

- Size: 407.9 MB (427,747,477 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.579 | 964.77 | 362.989 |
| CDWL_PM_POW_1 | 7.60929 | 141.857 | 23.4998 |
| CDWL_PM_POW_2 | 0 | 135.444 | 5.79148 |
| CDWL_PM_POW_3 | 0 | 87.1272 | 0.203898 |
| CDWL_RW_TEMP | 59.5755 | 94.7833 | 65.8037 |
| CDWL_SW_TEMP | 59.5266 | 85.7998 | 64.0885 |
| CHL_CD_FLOW_1 | 202.909 | 493.539 | 321.582 |
| CHL_CD_FLOW_2 | 0.000250771 | 413.295 | 40.0067 |
| CHL_CD_FLOW_3 | 0.000170706 | 321.589 | 1.40069 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.15215 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.080239 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00270581 |
| CHL_CW_FLOW_1 | 176.245 | 428.685 | 279.324 |
| CHL_CW_FLOW_2 | 0.000217819 | 358.986 | 34.7496 |
| CHL_CW_FLOW_3 | 0.000148274 | 279.33 | 1.21663 |
| CHL_POW_1 | 0 | 232.419 | 28.1712 |
| CHL_POW_2 | 0 | 225.905 | 15.1027 |
| CHL_POW_3 | 0 | 221.948 | 0.499068 |
| CHL_SWCD_TEMP_1 | 59.5755 | 94.7835 | 65.8093 |
| CHL_SWCD_TEMP_2 | 69.7192 | 94.4859 | 75.1729 |
| CHL_SWCD_TEMP_3 | 73.9343 | 92.2133 | 79.5729 |
| CHL_RW_TEMP_1 | 42.4923 | 72.9059 | 53.5081 |
| CHL_RW_TEMP_2 | 42.2273 | 61.6994 | 49.2191 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9834 | 49.3613 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124411 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.5728 | 86.2131 | 64.2307 |
| CHL_RWCD_TEMP_2 | 66.2556 | 86.2131 | 73.0068 |
| CHL_RWCD_TEMP_3 | 73.2734 | 86.2022 | 76.8449 |
| CHL_SW_TEMP_1 | 42.3875 | 54.5243 | 51.8872 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6957 | 46.5647 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8059 | 46.0089 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205372 |
| CT_FAN_SPD_2 | 0 | 1 | 0.095008 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00285776 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205372 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.095008 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00285776 |
| CT_FLOW_1 | 3.48508 | 575.044 | 142.092 |
| CT_FLOW_2 | 2.86425e-08 | 451.541 | 39.7854 |
| CT_FLOW_3 | 2.86425e-08 | 320.538 | 1.39014 |
| CT_POW_1 | 0 | 9.99999 | 1.40214 |
| CT_POW_2 | 0 | 9.99999 | 0.655885 |
| CT_POW_3 | 0 | 9.99999 | 0.0148216 |
| CT_RW_TEMP_1 | 59.5755 | 94.7835 | 65.8037 |
| CT_RW_TEMP_2 | 68.7045 | 94.4859 | 73.6819 |
| CT_RW_TEMP_3 | 68.7045 | 93.4037 | 78.2478 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124411 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8182 | 85.5446 | 62.1847 |
| CT_SW_TEMP_2 | 65.9535 | 85.5447 | 71.8344 |
| CT_SW_TEMP_3 | 69.6975 | 88.0185 | 76.0092 |
| CWL_PRI_CW_FLOW | 279.322 | 837.993 | 315.29 |
| CWL_PRI_PM_POW_1 | 5.9803 | 35.3804 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.1101 | 1.87008 |
| CWL_PRI_PM_POW_3 | 0 | 22.1071 | 0.0655693 |
| CWL_PRI_RW_TEMP | 42.4923 | 72.9968 | 53.508 |
| CWL_PRI_SW_TEMP | 42.3875 | 54.5251 | 51.8869 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9326 |
| CWL_SEC_CW_FLOW | 2.37219e-06 | 837.897 | 464.543 |
| CWL_SEC_DP | 476.092 | 978.102 | 932.472 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.88509e+06 | 96028.3 |
| CWL_SEC_PM_POW_1 | 2.49979e-07 | 53.6389 | 27.8849 |
| CWL_SEC_PM_POW_2 | 0 | 51.7177 | 26.9602 |
| CWL_SEC_PM_SPD_1 | 0.363088 | 1.00342 | 0.738141 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00342 | 0.595112 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.643451 |
| CWL_SEC_RW_TEMP | 43.8699 | 61.7642 | 52.0577 |
| CWL_SEC_SW_TEMP | 50.1405 | 72.7948 | 53.9715 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.780443 | 0.228979 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460157, 1.0: 65383 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460157, 1.0: 65383 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 338159, 0.0: 187381 |

## ChillerPlant_secondary_chilled_water_pressure_bias_-020.csv

- Size: 407.3 MB (427,127,698 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.575 | 964.754 | 363.005 |
| CDWL_PM_POW_1 | 7.60929 | 142.175 | 23.4986 |
| CDWL_PM_POW_2 | 0 | 135.444 | 5.79391 |
| CDWL_PM_POW_3 | 0 | 86.4469 | 0.203859 |
| CDWL_RW_TEMP | 59.5754 | 94.7831 | 65.8036 |
| CDWL_SW_TEMP | 59.5265 | 85.7998 | 64.0886 |
| CHL_CD_FLOW_1 | 203.176 | 493.657 | 321.582 |
| CHL_CD_FLOW_2 | 0.000250769 | 413.806 | 40.0223 |
| CHL_CD_FLOW_3 | 0.000171156 | 321.589 | 1.40093 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152203 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0802932 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00270934 |
| CHL_CW_FLOW_1 | 176.478 | 428.787 | 279.324 |
| CHL_CW_FLOW_2 | 0.000217817 | 359.429 | 34.7632 |
| CHL_CW_FLOW_3 | 0.000148665 | 279.33 | 1.21684 |
| CHL_POW_1 | 0 | 232.317 | 28.1797 |
| CHL_POW_2 | 0 | 225.905 | 15.1122 |
| CHL_POW_3 | 0 | 222.672 | 0.49975 |
| CHL_SWCD_TEMP_1 | 59.5754 | 94.7833 | 65.8091 |
| CHL_SWCD_TEMP_2 | 69.719 | 94.4859 | 75.1773 |
| CHL_SWCD_TEMP_3 | 73.9343 | 92.2133 | 79.572 |
| CHL_RW_TEMP_1 | 42.4924 | 72.604 | 53.508 |
| CHL_RW_TEMP_2 | 42.2273 | 61.6937 | 49.2156 |
| CHL_RW_TEMP_3 | 42.2273 | 57.9823 | 49.3612 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.124455 |
| CHL_STA_3 | 0 | 1 | 0.00435933 |
| CHL_RWCD_TEMP_1 | 59.5728 | 86.2132 | 64.2308 |
| CHL_RWCD_TEMP_2 | 66.2558 | 86.2132 | 73.0073 |
| CHL_RWCD_TEMP_3 | 73.2734 | 86.2023 | 76.8447 |
| CHL_SW_TEMP_1 | 42.3876 | 54.5191 | 51.8873 |
| CHL_SW_TEMP_2 | 42.0492 | 52.6955 | 46.5644 |
| CHL_SW_TEMP_3 | 42.0492 | 49.8052 | 46.0088 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205311 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0950024 |
| CT_FAN_SPD_3 | 0 | 1 | 0.0028545 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205311 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0950024 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.0028545 |
| CT_FLOW_1 | 3.48412 | 575.146 | 142.082 |
| CT_FLOW_2 | 2.86293e-08 | 448.797 | 39.8006 |
| CT_FLOW_3 | 2.86293e-08 | 320.538 | 1.39046 |
| CT_POW_1 | 0 | 9.99999 | 1.40147 |
| CT_POW_2 | 0 | 9.99999 | 0.655616 |
| CT_POW_3 | 0 | 9.99999 | 0.0147685 |
| CT_RW_TEMP_1 | 59.5755 | 94.7832 | 65.8036 |
| CT_RW_TEMP_2 | 68.7045 | 94.4859 | 73.6858 |
| CT_RW_TEMP_3 | 68.7045 | 93.4041 | 78.2469 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.124455 |
| CT_STA_3 | 0 | 1 | 0.00435933 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5363 |
| CT_SW_TEMP_1 | 52.8182 | 85.5446 | 62.1847 |
| CT_SW_TEMP_2 | 65.9535 | 85.5447 | 71.8364 |
| CT_SW_TEMP_3 | 69.6975 | 88.0182 | 76.0088 |
| CWL_PRI_CW_FLOW | 279.318 | 837.98 | 315.304 |
| CWL_PRI_PM_POW_1 | 5.99606 | 35.3973 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.1124 | 1.87082 |
| CWL_PRI_PM_POW_3 | 0 | 21.6584 | 0.0655615 |
| CWL_PRI_RW_TEMP | 42.4924 | 72.6889 | 53.5079 |
| CWL_PRI_SW_TEMP | 42.3876 | 54.5202 | 51.887 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 4.94581e-06 | 837.904 | 474.246 |
| CWL_SEC_DP | 423.196 | 977.761 | 890.954 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.86385e+06 | 96031.2 |
| CWL_SEC_PM_POW_1 | 6.77009e-07 | 53.6389 | 29.4185 |
| CWL_SEC_PM_POW_2 | 0 | 51.7179 | 28.6684 |
| CWL_SEC_PM_SPD_1 | 0.384856 | 1.00531 | 0.756656 |
| CWL_SEC_PM_SPD_2 | 0 | 1.00213 | 0.614083 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.654243 |
| CWL_SEC_RW_TEMP | 43.8699 | 61.7642 | 52.0602 |
| CWL_SEC_SW_TEMP | 50.1384 | 72.4936 | 53.9708 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.780501 | 0.228987 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 460134, 1.0: 65406 |
| CHL_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 460134, 1.0: 65406 |
| CT_STA_3 | 2 | 0.0: 523249, 1.0: 2291 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 343831, 0.0: 181709 |

## ChillerPlant_secondary_chilled_water_pressure_bias_010.csv

- Size: 409.7 MB (429,650,075 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.546 | 964.749 | 363.439 |
| CDWL_PM_POW_1 | 7.60931 | 142.137 | 23.5038 |
| CDWL_PM_POW_2 | 0 | 135.512 | 5.84071 |
| CDWL_PM_POW_3 | 0 | 87.0655 | 0.219949 |
| CDWL_RW_TEMP | 59.5761 | 94.7396 | 65.8028 |
| CDWL_SW_TEMP | 59.5271 | 85.8081 | 64.088 |
| CHL_CD_FLOW_1 | 201.811 | 493.417 | 321.581 |
| CHL_CD_FLOW_2 | 0.00025068 | 415.288 | 40.3465 |
| CHL_CD_FLOW_3 | 0.000168864 | 321.592 | 1.5114 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152097 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0808089 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00289817 |
| CHL_CW_FLOW_1 | 175.292 | 428.579 | 279.324 |
| CHL_CW_FLOW_2 | 0.000217739 | 360.717 | 35.0448 |
| CHL_CW_FLOW_3 | 0.000146674 | 279.333 | 1.31279 |
| CHL_POW_1 | 0 | 232.444 | 28.1346 |
| CHL_POW_2 | 0 | 226.019 | 15.1991 |
| CHL_POW_3 | 0 | 222.587 | 0.534368 |
| CHL_SWCD_TEMP_1 | 59.576 | 94.7397 | 65.8081 |
| CHL_SWCD_TEMP_2 | 69.7195 | 94.4857 | 75.2073 |
| CHL_SWCD_TEMP_3 | 73.9344 | 92.2127 | 79.5476 |
| CHL_RW_TEMP_1 | 42.4928 | 73.5428 | 53.5071 |
| CHL_RW_TEMP_2 | 42.2273 | 61.6897 | 49.2432 |
| CHL_RW_TEMP_3 | 42.2273 | 57.4112 | 49.3799 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.125463 |
| CHL_STA_3 | 0 | 1 | 0.00469612 |
| CHL_RWCD_TEMP_1 | 59.5734 | 86.2882 | 64.2303 |
| CHL_RWCD_TEMP_2 | 66.2543 | 86.2882 | 73.0208 |
| CHL_RWCD_TEMP_3 | 73.2735 | 86.2891 | 76.8218 |
| CHL_SW_TEMP_1 | 42.3877 | 54.535 | 51.8869 |
| CHL_SW_TEMP_2 | 42.0492 | 52.8092 | 46.5757 |
| CHL_SW_TEMP_3 | 42.0492 | 50.3572 | 46.0383 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205387 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0957655 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00305838 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205387 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0957655 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00305838 |
| CT_FLOW_1 | 3.49244 | 574.802 | 142.108 |
| CT_FLOW_2 | 2.87443e-08 | 454.432 | 40.1237 |
| CT_FLOW_3 | 2.87443e-08 | 320.551 | 1.49983 |
| CT_POW_1 | 0 | 9.99999 | 1.40196 |
| CT_POW_2 | 0 | 9.99999 | 0.660394 |
| CT_POW_3 | 0 | 9.99999 | 0.0157511 |
| CT_RW_TEMP_1 | 59.5761 | 94.7397 | 65.8028 |
| CT_RW_TEMP_2 | 68.7045 | 94.4857 | 73.7225 |
| CT_RW_TEMP_3 | 68.7045 | 93.2595 | 78.2322 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.125463 |
| CT_STA_3 | 0 | 1 | 0.00469612 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8182 | 85.5718 | 62.184 |
| CT_SW_TEMP_2 | 65.9536 | 85.5722 | 71.8492 |
| CT_SW_TEMP_3 | 69.6975 | 88.0757 | 75.9914 |
| CWL_PRI_CW_FLOW | 279.293 | 837.975 | 315.681 |
| CWL_PRI_PM_POW_1 | 5.91577 | 35.363 | 15.0216 |
| CWL_PRI_PM_POW_2 | 0 | 31.0436 | 1.88595 |
| CWL_PRI_PM_POW_3 | 0 | 22.8355 | 0.0707245 |
| CWL_PRI_RW_TEMP | 42.4928 | 73.6447 | 53.5071 |
| CWL_PRI_SW_TEMP | 42.3877 | 54.5357 | 51.8863 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 4.62542e-06 | 837.847 | 404.638 |
| CWL_SEC_DP | 529.202 | 978.062 | 956.98 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.92837e+06 | 96339.4 |
| CWL_SEC_PM_POW_1 | 5.0161e-07 | 53.6388 | 19.8233 |
| CWL_SEC_PM_POW_2 | 0 | 51.7161 | 18.9219 |
| CWL_SEC_PM_SPD_1 | 0.328841 | 1.00155 | 0.662384 |
| CWL_SEC_PM_SPD_2 | 0 | 1 | 0.52798 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.633324 |
| CWL_SEC_RW_TEMP | 43.87 | 61.7642 | 52.009 |
| CWL_SEC_SW_TEMP | 50.1398 | 73.4308 | 53.9772 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.779992 | 0.229022 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 459604, 1.0: 65936 |
| CHL_STA_3 | 2 | 0.0: 523072, 1.0: 2468 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 459604, 1.0: 65936 |
| CT_STA_3 | 2 | 0.0: 523072, 1.0: 2468 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 332837, 0.0: 192703 |

## ChillerPlant_secondary_chilled_water_pressure_bias_020.csv

- Size: 409.8 MB (429,710,361 bytes)
- Rows: 525,540
- Columns: 78
- Time column: `Datetime`
- Time range: 2018-01-01 01:00:00 to 2018-12-31 23:59:00
- Sampling interval:
  - Median: 0 days 00:01:00
  - Mode: 0 days 00:01:00 (525539 occurrences)
  - Min: 0 days 00:01:00
  - Max: 0 days 00:01:00

### Columns, Data Types, and Missing Values

| Column | Dtype | Missing Count | Missing % |
| --- | --- | --- | --- |
| Datetime | str | 0 | 0.000% |
| CDWL_CW_FLOW | float64 | 0 | 0.000% |
| CDWL_PM_POW_1 | float64 | 0 | 0.000% |
| CDWL_PM_POW_2 | float64 | 0 | 0.000% |
| CDWL_PM_POW_3 | float64 | 0 | 0.000% |
| CDWL_RW_TEMP | float64 | 0 | 0.000% |
| CDWL_SW_TEMP | float64 | 0 | 0.000% |
| CHL_CD_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CD_FLOW_3 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CHL_COMP_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_1 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_2 | float64 | 0 | 0.000% |
| CHL_CW_FLOW_3 | float64 | 0 | 0.000% |
| CHL_POW_1 | float64 | 0 | 0.000% |
| CHL_POW_2 | float64 | 0 | 0.000% |
| CHL_POW_3 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RW_TEMP_3 | float64 | 0 | 0.000% |
| CHL_STA_1 | float64 | 0 | 0.000% |
| CHL_STA_2 | float64 | 0 | 0.000% |
| CHL_STA_3 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_1 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_2 | float64 | 0 | 0.000% |
| CHL_RWCD_TEMP_3 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_1 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_2 | float64 | 0 | 0.000% |
| CHL_SW_TEMP_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_3 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_1 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_2 | float64 | 0 | 0.000% |
| CT_FAN_SPD_CTRL_3 | float64 | 0 | 0.000% |
| CT_FLOW_1 | float64 | 0 | 0.000% |
| CT_FLOW_2 | float64 | 0 | 0.000% |
| CT_FLOW_3 | float64 | 0 | 0.000% |
| CT_POW_1 | float64 | 0 | 0.000% |
| CT_POW_2 | float64 | 0 | 0.000% |
| CT_POW_3 | float64 | 0 | 0.000% |
| CT_RW_TEMP_1 | float64 | 0 | 0.000% |
| CT_RW_TEMP_2 | float64 | 0 | 0.000% |
| CT_RW_TEMP_3 | float64 | 0 | 0.000% |
| CT_STA_1 | float64 | 0 | 0.000% |
| CT_STA_2 | float64 | 0 | 0.000% |
| CT_STA_3 | float64 | 0 | 0.000% |
| CT_SW_TEMPSPT | float64 | 0 | 0.000% |
| CT_SW_TEMP_1 | float64 | 0 | 0.000% |
| CT_SW_TEMP_2 | float64 | 0 | 0.000% |
| CT_SW_TEMP_3 | float64 | 0 | 0.000% |
| CWL_PRI_CW_FLOW | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_PRI_PM_POW_3 | float64 | 0 | 0.000% |
| CWL_PRI_RW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMP | float64 | 0 | 0.000% |
| CWL_PRI_SW_TEMPSPT | float64 | 0 | 0.000% |
| CWL_SEC_CW_FLOW | float64 | 0 | 0.000% |
| CWL_SEC_DP | float64 | 0 | 0.000% |
| CWL_SEC_DPSPT | float64 | 0 | 0.000% |
| CWL_SEC_LOAD | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_POW_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_SPD_2 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_1 | float64 | 0 | 0.000% |
| CWL_SEC_PM_STA_2 | float64 | 0 | 0.000% |
| CWL_SEC_RW_TEMP | float64 | 0 | 0.000% |
| CWL_SEC_SW_TEMP | float64 | 0 | 0.000% |
| OA_TEMP | float64 | 0 | 0.000% |
| OA_TEMP_WB | float64 | 0 | 0.000% |
| TWV_CTRL | float64 | 0 | 0.000% |

### Numeric Basic Statistics

| Column | Min | Max | Mean |
| --- | --- | --- | --- |
| CDWL_CW_FLOW | 321.56 | 964.749 | 363.799 |
| CDWL_PM_POW_1 | 7.60932 | 142.169 | 23.5042 |
| CDWL_PM_POW_2 | 0 | 135.451 | 5.8651 |
| CDWL_PM_POW_3 | 0 | 87.2842 | 0.24857 |
| CDWL_RW_TEMP | 59.5768 | 94.7375 | 65.8049 |
| CDWL_SW_TEMP | 59.5279 | 85.81 | 64.089 |
| CHL_CD_FLOW_1 | 202.161 | 493.745 | 321.583 |
| CHL_CD_FLOW_2 | 0.0002403 | 415.299 | 40.5092 |
| CHL_CD_FLOW_3 | 0.00016945 | 321.59 | 1.70761 |
| CHL_COMP_SPD_CTRL_1 | 0 | 1 | 0.152157 |
| CHL_COMP_SPD_CTRL_2 | 0 | 1 | 0.0809528 |
| CHL_COMP_SPD_CTRL_3 | 0 | 1 | 0.00321992 |
| CHL_CW_FLOW_1 | 175.596 | 428.864 | 279.325 |
| CHL_CW_FLOW_2 | 0.000208723 | 360.726 | 35.1861 |
| CHL_CW_FLOW_3 | 0.000147183 | 279.331 | 1.48322 |
| CHL_POW_1 | 0 | 232.343 | 28.124 |
| CHL_POW_2 | 0 | 226.149 | 15.2145 |
| CHL_POW_3 | 0 | 222.68 | 0.592288 |
| CHL_SWCD_TEMP_1 | 59.5768 | 94.7376 | 65.8101 |
| CHL_SWCD_TEMP_2 | 69.7191 | 94.4853 | 75.2509 |
| CHL_SWCD_TEMP_3 | 73.9343 | 92.2125 | 79.5568 |
| CHL_RW_TEMP_1 | 42.4931 | 73.8934 | 53.5082 |
| CHL_RW_TEMP_2 | 42.2273 | 61.6435 | 49.2903 |
| CHL_RW_TEMP_3 | 42.2273 | 57.0693 | 49.545 |
| CHL_STA_1 | 1 | 1 | 1 |
| CHL_STA_2 | 0 | 1 | 0.125971 |
| CHL_STA_3 | 0 | 1 | 0.00530692 |
| CHL_RWCD_TEMP_1 | 59.5741 | 86.2934 | 64.2313 |
| CHL_RWCD_TEMP_2 | 66.2559 | 86.2934 | 73.0352 |
| CHL_RWCD_TEMP_3 | 73.2735 | 86.2927 | 76.8303 |
| CHL_SW_TEMP_1 | 42.3879 | 54.5402 | 51.8867 |
| CHL_SW_TEMP_2 | 42.0492 | 52.9507 | 46.5832 |
| CHL_SW_TEMP_3 | 42.0492 | 50.3328 | 46.0677 |
| CT_FAN_SPD_1 | 0 | 1 | 0.205542 |
| CT_FAN_SPD_2 | 0 | 1 | 0.0960488 |
| CT_FAN_SPD_3 | 0 | 1 | 0.00344404 |
| CT_FAN_SPD_CTRL_1 | 0 | 1 | 0.205542 |
| CT_FAN_SPD_CTRL_2 | 0 | 1 | 0.0960488 |
| CT_FAN_SPD_CTRL_3 | 0 | 1 | 0.00344404 |
| CT_FLOW_1 | 3.49992 | 575.162 | 142.089 |
| CT_FLOW_2 | 2.8848e-08 | 453.775 | 40.2853 |
| CT_FLOW_3 | 2.8848e-08 | 320.543 | 1.6949 |
| CT_POW_1 | 0 | 9.99999 | 1.40327 |
| CT_POW_2 | 0 | 9.99999 | 0.660671 |
| CT_POW_3 | 0 | 9.99999 | 0.0174416 |
| CT_RW_TEMP_1 | 59.5768 | 94.7376 | 65.805 |
| CT_RW_TEMP_2 | 68.7045 | 94.4853 | 73.7739 |
| CT_RW_TEMP_3 | 68.7045 | 93.2642 | 78.2643 |
| CT_STA_1 | 1 | 1 | 1 |
| CT_STA_2 | 0 | 1 | 0.125971 |
| CT_STA_3 | 0 | 1 | 0.00530692 |
| CT_SW_TEMPSPT | 60.008 | 84.992 | 64.5361 |
| CT_SW_TEMP_1 | 52.8182 | 85.5836 | 62.1847 |
| CT_SW_TEMP_2 | 65.9537 | 85.5841 | 71.871 |
| CT_SW_TEMP_3 | 69.6975 | 88.0817 | 76.0069 |
| CWL_PRI_CW_FLOW | 279.305 | 837.975 | 315.994 |
| CWL_PRI_PM_POW_1 | 5.9363 | 35.4101 | 15.0217 |
| CWL_PRI_PM_POW_2 | 0 | 31.1009 | 1.8937 |
| CWL_PRI_PM_POW_3 | 0 | 22.557 | 0.0799338 |
| CWL_PRI_RW_TEMP | 42.4931 | 74.0013 | 53.5082 |
| CWL_PRI_SW_TEMP | 42.3878 | 54.5407 | 51.8859 |
| CWL_PRI_SW_TEMPSPT | 44.0006 | 53.9996 | 51.9325 |
| CWL_SEC_CW_FLOW | 3.13127e-08 | 837.847 | 371.39 |
| CWL_SEC_DP | 529.202 | 976.788 | 957.523 |
| CWL_SEC_DPSPT | 960.961 | 960.961 | 960.961 |
| CWL_SEC_LOAD | 0 | 1.95174e+06 | 96597.7 |
| CWL_SEC_PM_POW_1 | 4.58759e-07 | 53.6388 | 16.1281 |
| CWL_SEC_PM_POW_2 | 0 | 51.7161 | 15.3314 |
| CWL_SEC_PM_SPD_1 | 0.314971 | 1.00096 | 0.622255 |
| CWL_SEC_PM_SPD_2 | 0 | 1 | 0.494663 |
| CWL_SEC_PM_STA_1 | 1 | 1 | 1 |
| CWL_SEC_PM_STA_2 | 0 | 1 | 0.631897 |
| CWL_SEC_RW_TEMP | 43.87 | 61.7642 | 51.9674 |
| CWL_SEC_SW_TEMP | 50.1385 | 73.7811 | 53.9804 |
| OA_TEMP | -9.75686 | 80.4929 | 44.914 |
| OA_TEMP_WB | -9.03998 | 95 | 49.9823 |
| TWV_CTRL | 0 | 0.779521 | 0.229114 |

### Categorical / Label-Like Unique Values

| Column | Unique Values | Top Values |
| --- | --- | --- |
| Datetime | 525540 | '2018-01-01 01:00:00': 1, '2018-01-01 01:01:00': 1, '2018-01-01 01:02:00': 1, '2018-01-01 01:03:00': 1, '2018-01-01 01:04:00': 1, '2018-01-01 01:05:00': 1, '2018-01-01 01:06:00': 1, '2018-01-01 01:07:00': 1, '2018-01-01 01:08:00': 1, '2018-01-01 01:09:00': 1, '2018-01-01 01:10:00': 1, '2018-01-01 01:11:00': 1, '2018-01-01 01:12:00': 1, '2018-01-01 01:13:00': 1, '2018-01-01 01:14:00': 1, '2018-01-01 01:15:00': 1, '2018-01-01 01:16:00': 1, '2018-01-01 01:17:00': 1, '2018-01-01 01:18:00': 1, '2018-01-01 01:19:00': 1, '2018-01-01 01:20:00': 1, '2018-01-01 01:21:00': 1, '2018-01-01 01:22:00': 1, '2018-01-01 01:23:00': 1, '2018-01-01 01:24:00': 1, '2018-01-01 01:25:00': 1, '2018-01-01 01:26:00': 1, '2018-01-01 01:27:00': 1, '2018-01-01 01:28:00': 1, '2018-01-01 01:29:00': 1 |
| CHL_STA_1 | 1 | 1.0: 525540 |
| CHL_STA_2 | 2 | 0.0: 459337, 1.0: 66203 |
| CHL_STA_3 | 2 | 0.0: 522751, 1.0: 2789 |
| CT_STA_1 | 1 | 1.0: 525540 |
| CT_STA_2 | 2 | 0.0: 459337, 1.0: 66203 |
| CT_STA_3 | 2 | 0.0: 522751, 1.0: 2789 |
| CWL_SEC_DPSPT | 1 | 960.960801796: 525540 |
| CWL_SEC_PM_STA_1 | 1 | 1.0: 525540 |
| CWL_SEC_PM_STA_2 | 2 | 1.0: 332087, 0.0: 193453 |
