# Expected State Model Performance

Frozen HVAC-v1 condition variables were used as inputs for one XGBoost model per target.

- Total rows loaded: 525,540
- Retained rows: 525,540
- Retention: 100.00%
- Train rows: 420,432
- Test rows: 105,108

| Target | Train R2 | Test R2 | Test RMSE | Mean | Std | Min | Max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | 0.975869 | 0.970508 | 2.96123 | 28.1798 | 51.2097 | 0 | 232.503 |
| CHL_SW_TEMP_1 | 0.997478 | 0.981913 | 0.118656 | 51.8873 | 3.36581 | 42.3878 | 54.53 |
| CT_SW_TEMP_1 | 0.998789 | 0.993331 | 0.254097 | 62.1848 | 7.7943 | 52.8182 | 85.5446 |
| CHL_RWCD_TEMP_1 | 0.99832 | 0.983723 | 0.243074 | 64.2308 | 6.57089 | 59.573 | 86.213 |

## Success Criteria

- CHL_POW_1: Test R2 0.970508 > 0.90: PASS
- CHL_SW_TEMP_1: Test R2 0.981913 > 0.70: PASS
- CT_SW_TEMP_1: Test R2 0.993331 > 0.70: PASS
- CHL_RWCD_TEMP_1: Test R2 0.983723 > 0.70: PASS