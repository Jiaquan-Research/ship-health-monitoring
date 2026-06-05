# Validation B4: Residual Trend Audit

- Verdict: Strong PASS
- Q4a status: Initial Evidence
- Best trend metric: RMS
- Targets with reliable trend: 4/4
- Input: frozen Validation B2.1 residuals only. No residuals recomputed. No models retrained.

## Dataset Load Check

| Dataset | Rows |
| --- | --- |
| Baseline | 525540 |
| 095 | 525540 |
| 080 | 525540 |
| 065 | 525540 |

## Section 1: Trend Metrics Table

| Target | Metric | Baseline | 095 | 080 | 065 |
| --- | --- | --- | --- | --- | --- |
| CT_SW_TEMP_1 | AbsMean | 0.12531 | 0.221194 | 0.642253 | 1.2729 |
| CT_SW_TEMP_1 | RMS | 0.27819 | 0.333712 | 0.798706 | 1.5565 |
| CT_SW_TEMP_1 | P95 | 0.35067 | 0.510948 | 1.3665 | 2.75886 |
| CT_SW_TEMP_1 | P99 | 0.899511 | 1.11344 | 2.48459 | 4.98181 |
| CT_SW_TEMP_1 | Std | 0.278185 | 0.306501 | 0.522526 | 0.919739 |
| CHL_SW_TEMP_1 | AbsMean | 0.063705 | 0.0665075 | 0.0672935 | 0.0706663 |
| CHL_SW_TEMP_1 | RMS | 0.169252 | 0.181683 | 0.186975 | 0.212758 |
| CHL_SW_TEMP_1 | P95 | 0.185307 | 0.194897 | 0.195576 | 0.20176 |
| CHL_SW_TEMP_1 | P99 | 0.490246 | 0.520119 | 0.530659 | 0.5523 |
| CHL_SW_TEMP_1 | Std | 0.169244 | 0.181678 | 0.186972 | 0.212757 |
| CHL_RWCD_TEMP_1 | AbsMean | 0.115802 | 0.128619 | 0.246714 | 0.527207 |
| CHL_RWCD_TEMP_1 | RMS | 0.278782 | 0.302231 | 0.560362 | 1.1391 |
| CHL_RWCD_TEMP_1 | P95 | 0.344879 | 0.498721 | 1.24893 | 2.47653 |
| CHL_RWCD_TEMP_1 | P99 | 0.937455 | 1.13184 | 2.45375 | 4.99345 |
| CHL_RWCD_TEMP_1 | Std | 0.27877 | 0.300297 | 0.524382 | 1.02369 |
| CHL_POW_1 | AbsMean | 2.5835 | 2.60177 | 2.72002 | 2.97231 |
| CHL_POW_1 | RMS | 7.79265 | 7.82836 | 8.13592 | 8.77835 |
| CHL_POW_1 | P95 | 6.68148 | 6.85937 | 7.93277 | 10.4982 |
| CHL_POW_1 | P99 | 26.911 | 27.4535 | 30.1386 | 35.801 |
| CHL_POW_1 | Std | 7.79236 | 7.82767 | 8.13003 | 8.74449 |

## Section 2: Spearman Correlation Table

| Target | Metric | Spearman_rho |
| --- | --- | --- |
| CT_SW_TEMP_1 | AbsMean | 1 |
| CT_SW_TEMP_1 | RMS | 1 |
| CT_SW_TEMP_1 | P95 | 1 |
| CT_SW_TEMP_1 | P99 | 1 |
| CT_SW_TEMP_1 | Std | 1 |
| CHL_SW_TEMP_1 | AbsMean | 1 |
| CHL_SW_TEMP_1 | RMS | 1 |
| CHL_SW_TEMP_1 | P95 | 1 |
| CHL_SW_TEMP_1 | P99 | 1 |
| CHL_SW_TEMP_1 | Std | 1 |
| CHL_RWCD_TEMP_1 | AbsMean | 1 |
| CHL_RWCD_TEMP_1 | RMS | 1 |
| CHL_RWCD_TEMP_1 | P95 | 1 |
| CHL_RWCD_TEMP_1 | P99 | 1 |
| CHL_RWCD_TEMP_1 | Std | 1 |
| CHL_POW_1 | AbsMean | 1 |
| CHL_POW_1 | RMS | 1 |
| CHL_POW_1 | P95 | 1 |
| CHL_POW_1 | P99 | 1 |
| CHL_POW_1 | Std | 1 |

## Section 3: Monotonicity Results

| Target | Metric | Strict_Monotonic |
| --- | --- | --- |
| CT_SW_TEMP_1 | AbsMean | True |
| CT_SW_TEMP_1 | RMS | True |
| CT_SW_TEMP_1 | P95 | True |
| CT_SW_TEMP_1 | P99 | True |
| CT_SW_TEMP_1 | Std | True |
| CHL_SW_TEMP_1 | AbsMean | True |
| CHL_SW_TEMP_1 | RMS | True |
| CHL_SW_TEMP_1 | P95 | True |
| CHL_SW_TEMP_1 | P99 | True |
| CHL_SW_TEMP_1 | Std | True |
| CHL_RWCD_TEMP_1 | AbsMean | True |
| CHL_RWCD_TEMP_1 | RMS | True |
| CHL_RWCD_TEMP_1 | P95 | True |
| CHL_RWCD_TEMP_1 | P99 | True |
| CHL_RWCD_TEMP_1 | Std | True |
| CHL_POW_1 | AbsMean | True |
| CHL_POW_1 | RMS | True |
| CHL_POW_1 | P95 | True |
| CHL_POW_1 | P99 | True |
| CHL_POW_1 | Std | True |

## Section 4: Trend Strength

| Target | Metric | Delta | Ratio | Cohen_d |
| --- | --- | --- | --- | --- |
| CT_SW_TEMP_1 | AbsMean | 1.14759 | 10.158 | 1.84541 |
| CT_SW_TEMP_1 | RMS | 1.27831 | 5.59509 | 1.84541 |
| CT_SW_TEMP_1 | P95 | 2.40819 | 7.86741 | 1.84541 |
| CT_SW_TEMP_1 | P99 | 4.0823 | 5.53835 | 1.84541 |
| CT_SW_TEMP_1 | Std | 0.641554 | 3.30622 | 1.84541 |
| CHL_SW_TEMP_1 | AbsMean | 0.00696127 | 1.10927 | -0.00627177 |
| CHL_SW_TEMP_1 | RMS | 0.0435053 | 1.25704 | -0.00627177 |
| CHL_SW_TEMP_1 | P95 | 0.0164535 | 1.08879 | -0.00627177 |
| CHL_SW_TEMP_1 | P99 | 0.0620541 | 1.12658 | -0.00627177 |
| CHL_SW_TEMP_1 | Std | 0.043513 | 1.2571 | -0.00627177 |
| CHL_RWCD_TEMP_1 | AbsMean | 0.411405 | 4.55266 | 0.66245 |
| CHL_RWCD_TEMP_1 | RMS | 0.860321 | 4.086 | 0.66245 |
| CHL_RWCD_TEMP_1 | P95 | 2.13165 | 7.18086 | 0.66245 |
| CHL_RWCD_TEMP_1 | P99 | 4.05599 | 5.3266 | 0.66245 |
| CHL_RWCD_TEMP_1 | Std | 0.744917 | 3.67216 | 0.66245 |
| CHL_POW_1 | AbsMean | 0.388809 | 1.1505 | 0.0847658 |
| CHL_POW_1 | RMS | 0.985699 | 1.12649 | 0.0847658 |
| CHL_POW_1 | P95 | 3.81669 | 1.57123 | 0.0847658 |
| CHL_POW_1 | P99 | 8.88992 | 1.33034 | 0.0847658 |
| CHL_POW_1 | Std | 0.952136 | 1.12219 | 0.0847658 |

## Section 5: Step-wise No-Reversal

| Target | Metric | Step1 | Step2 | Step3 | No_Reversal |
| --- | --- | --- | --- | --- | --- |
| CT_SW_TEMP_1 | AbsMean | 0.095884 | 0.421059 | 0.630651 | True |
| CT_SW_TEMP_1 | RMS | 0.0555221 | 0.464994 | 0.757795 | True |
| CT_SW_TEMP_1 | P95 | 0.160278 | 0.855554 | 1.39236 | True |
| CT_SW_TEMP_1 | P99 | 0.213932 | 1.37115 | 2.49722 | True |
| CT_SW_TEMP_1 | Std | 0.0283162 | 0.216026 | 0.397212 | True |
| CHL_SW_TEMP_1 | AbsMean | 0.00280252 | 0.000785962 | 0.00337279 | True |
| CHL_SW_TEMP_1 | RMS | 0.0124307 | 0.00529152 | 0.0257831 | True |
| CHL_SW_TEMP_1 | P95 | 0.00959056 | 0.000678206 | 0.00618478 | True |
| CHL_SW_TEMP_1 | P99 | 0.0298737 | 0.0105394 | 0.021641 | True |
| CHL_SW_TEMP_1 | Std | 0.0124338 | 0.00529395 | 0.0257853 | True |
| CHL_RWCD_TEMP_1 | AbsMean | 0.012817 | 0.118096 | 0.280492 | True |
| CHL_RWCD_TEMP_1 | RMS | 0.0234493 | 0.25813 | 0.578741 | True |
| CHL_RWCD_TEMP_1 | P95 | 0.153842 | 0.75021 | 1.22759 | True |
| CHL_RWCD_TEMP_1 | P99 | 0.19438 | 1.32192 | 2.53969 | True |
| CHL_RWCD_TEMP_1 | Std | 0.0215277 | 0.224085 | 0.499305 | True |
| CHL_POW_1 | AbsMean | 0.0182712 | 0.118243 | 0.252295 | True |
| CHL_POW_1 | RMS | 0.0357124 | 0.307564 | 0.642422 | True |
| CHL_POW_1 | P95 | 0.177887 | 1.0734 | 2.5654 | True |
| CHL_POW_1 | P99 | 0.542413 | 2.68513 | 5.66238 | True |
| CHL_POW_1 | Std | 0.0353089 | 0.302367 | 0.61446 | True |

## Section 6: Raw Residual vs HI_v0

| Carrier | Baseline | 095 | 080 | 065 | Ratio_065/Baseline | Strict_Monotonic |
| --- | --- | --- | --- | --- | --- | --- |
| Raw residual RMS | 0.27819 | 0.333712 | 0.798706 | 1.5565 | 5.59509 | True |
| HI_v0 Rolling RMS 24h | 0.0255308 | 0.0368661 | 0.0927773 | 0.178481 | 6.9908 | True |

HI_v0 Rolling RMS increases CT_SW_TEMP_1 trend ratio over raw residual RMS while preserving strict monotonicity.

## Section 7: Interpretation

### Q1: Does residual naturally form a trend along the pseudo degradation path?

Yes. Raw residual metrics form monotonic pseudo-degradation trends for the primary target and multiple secondary targets.

### Q2: Which trend metric is most reliable?

`RMS` is recommended because it is monotonic, has Spearman rho = 1.0, and has no step reversal for the primary target.

### Q3: How many targets show reliable trend?

4/4 targets show at least one reliable residual trend metric.

### Q4: Does Rolling RMS improve over raw residual as a trend carrier?

Yes for CT_SW_TEMP_1 under W=24h: HI_v0 has a larger strongest-vs-baseline ratio than raw residual RMS.

### Q5: Does this support Q4a Initial Evidence?

Yes. Residual -> Trend exists in the HVAC pseudo-degradation path, so Q4a can be marked Initial Evidence.

### Q6: What is the recommended primary Trend Metric for future Validation C/D?

Use `RMS` on `CT_SW_TEMP_1` as the primary trend metric, with AbsMean/P95/P99 as corroborating metrics.

## Generated Outputs

- `outputs/b4_trend_metrics.csv`
- `outputs/b4_spearman.csv`
- `outputs/b4_monotonicity.csv`
- `outputs/b4_trend_strength.csv`
- `outputs/b4_step_no_reversal.csv`
- `outputs/b4_raw_vs_hi_v0.csv`
- `outputs/b4_spearman_heatmap.png`
- `outputs/b4_trend_strength.png`
- `outputs/b4_trend_path_CT_SW_TEMP_1.png`
- `outputs/b4_trend_path_CHL_SW_TEMP_1.png`
- `outputs/b4_trend_path_CHL_RWCD_TEMP_1.png`
- `outputs/b4_trend_path_CHL_POW_1.png`