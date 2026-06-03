# Residual Baseline Analysis

## Model Performance

| Target | Train R2 | Test R2 | Test RMSE | Mean | Std | Min | Max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | 0.975869 | 0.970508 | 2.96123 | 28.1798 | 51.2097 | 0 | 232.503 |
| CHL_SW_TEMP_1 | 0.997478 | 0.981913 | 0.118656 | 51.8873 | 3.36581 | 42.3878 | 54.53 |
| CT_SW_TEMP_1 | 0.998789 | 0.993331 | 0.254097 | 62.1848 | 7.7943 | 52.8182 | 85.5446 |
| CHL_RWCD_TEMP_1 | 0.99832 | 0.983723 | 0.243074 | 64.2308 | 6.57089 | 59.573 | 86.213 |

## Residual Statistics

| Target | Residual Mean | Residual Std | Residual Min | Residual Max | Residual P05 | Residual P95 | Train Target Std | Residual Std / Target Range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | 0.0682649 | 7.79236 | -160.37 | 198.421 | -7.6908 | 6.68148 | 55.2694 | 0.0335151 |
| CHL_SW_TEMP_1 | 0.00166448 | 0.169244 | -5.18277 | 3.85148 | -0.160671 | 0.185307 | 3.57785 | 0.0139385 |
| CT_SW_TEMP_1 | 0.00183445 | 0.278185 | -5.19045 | 7.83322 | -0.322232 | 0.35067 | 8.15655 | 0.00850029 |
| CHL_RWCD_TEMP_1 | 0.00264073 | 0.27877 | -4.98735 | 7.06826 | -0.305287 | 0.344879 | 7.00279 | 0.0104643 |

## Residual Stability Summary

| Target | Residual Std | Monthly Mean Range | Monthly Std Range | Seasonal Pattern Visible | Approximately Stationary |
| --- | --- | --- | --- | --- | --- |
| CHL_POW_1 | 7.79236 | 1.01886 | 13.3976 | False | True |
| CHL_SW_TEMP_1 | 0.169244 | 0.0230556 | 0.255541 | False | True |
| CT_SW_TEMP_1 | 0.278185 | 0.0617519 | 0.35895 | False | True |
| CHL_RWCD_TEMP_1 | 0.27877 | 0.0694678 | 0.409918 | False | True |

## Residual Interpretation

### Q1: Do residuals center near zero?

Yes. Residual means are small relative to residual standard deviations, so the models are approximately unbiased.

### Q2: Is residual variance small relative to target range?

Yes. Residual standard deviations are small relative to target ranges, indicating most baseline behavior is explained by Condition Variables.

### Q3: Are seasonal patterns visible in residuals?

No strong seasonal residual pattern is visible under the monthly drift heuristic.

### Q4: Are residuals approximately stationary throughout the year?

Yes. All targets pass the monthly drift stationarity heuristic.

### Q5: Which target provides the cleanest residual baseline?

| Rank | Target | Residual Std | Monthly Mean Range | Monthly Std Range | Seasonal Pattern Visible | Approximately Stationary |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CHL_SW_TEMP_1 | 0.169244 | 0.0230556 | 0.255541 | False | True |
| 2 | CT_SW_TEMP_1 | 0.278185 | 0.0617519 | 0.35895 | False | True |
| 3 | CHL_RWCD_TEMP_1 | 0.27877 | 0.0694678 | 0.409918 | False | True |
| 4 | CHL_POW_1 | 7.79236 | 1.01886 | 13.3976 | False | True |

Preferred candidate for Validation B2: `CHL_SW_TEMP_1`.

## B1 Conclusion

Condition Variables predict State Variables accurately enough to support a Residual-based Health Monitoring architecture.
Validation B1 supports the Expected State -> Residual route, while degradation and marine transfer remain unproven.