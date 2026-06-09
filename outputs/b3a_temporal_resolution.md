# Validation B3A: Temporal Resolution Feasibility Audit

- Verdict: Moderate Evidence
- Minimum viable sampling interval under conservative criteria: 1h
- Scope: Expected State and raw residual severity replication only.
- Excluded: HI_v0, CUSUM, EWMA, VIB, Autoencoder, Transformer, mapping changes.

## Section 1: Sample Count Audit

| Sampling | Dataset | Rows |
| --- | --- | --- |
| 1min | Baseline | 525540 |
| 1min | 095 | 525540 |
| 1min | 080 | 525540 |
| 1min | 065 | 525540 |
| 15min | Baseline | 35036 |
| 15min | 095 | 35036 |
| 15min | 080 | 35036 |
| 15min | 065 | 35036 |
| 1h | Baseline | 8759 |
| 1h | 095 | 8759 |
| 1h | 080 | 8759 |
| 1h | 065 | 8759 |
| 2h | Baseline | 4380 |
| 2h | 095 | 4380 |
| 2h | 080 | 4380 |
| 2h | 065 | 4380 |

## Section 2: B1 Results

| Sampling | Target | Train Rows | Test Rows | Train R2 | Test R2 | RMSE | B1 Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1min | CHL_POW_1 | 420432 | 105108 | 0.975869 | 0.970508 | 2.96123 | True |
| 1min | CT_SW_TEMP_1 | 420432 | 105108 | 0.998789 | 0.993331 | 0.254097 | True |
| 1min | CHL_SW_TEMP_1 | 420432 | 105108 | 0.997478 | 0.981913 | 0.118656 | True |
| 1min | CHL_RWCD_TEMP_1 | 420432 | 105108 | 0.99832 | 0.983723 | 0.243074 | True |
| 15min | CHL_POW_1 | 28028 | 7008 | 0.983548 | 0.973794 | 2.76549 | True |
| 15min | CT_SW_TEMP_1 | 28028 | 7008 | 0.998955 | 0.992499 | 0.269421 | True |
| 15min | CHL_SW_TEMP_1 | 28028 | 7008 | 0.997911 | 0.982204 | 0.117578 | True |
| 15min | CHL_RWCD_TEMP_1 | 28028 | 7008 | 0.998558 | 0.984173 | 0.23957 | True |
| 1h | CHL_POW_1 | 7007 | 1752 | 0.993616 | 0.974693 | 2.69387 | True |
| 1h | CT_SW_TEMP_1 | 7007 | 1752 | 0.999646 | 0.994867 | 0.222681 | True |
| 1h | CHL_SW_TEMP_1 | 7007 | 1752 | 0.999125 | 0.989105 | 0.0918968 | True |
| 1h | CHL_RWCD_TEMP_1 | 7007 | 1752 | 0.999563 | 0.988706 | 0.202022 | True |
| 2h | CHL_POW_1 | 3504 | 876 | 0.997229 | 0.938575 | 4.12831 | True |
| 2h | CT_SW_TEMP_1 | 3504 | 876 | 0.999761 | 0.991954 | 0.278019 | True |
| 2h | CHL_SW_TEMP_1 | 3504 | 876 | 0.999715 | 0.979599 | 0.124303 | True |
| 2h | CHL_RWCD_TEMP_1 | 3504 | 876 | 0.999741 | 0.980606 | 0.263125 | True |

## Section 3: B2.1 Results

| Sampling | Target | RMS_065/RMS_baseline | Strict RMS Monotonic | Strict Mean Monotonic | Strict P95 Monotonic |
| --- | --- | --- | --- | --- | --- |
| 1min | CHL_POW_1 | 1.12649 | True | True | True |
| 1min | CT_SW_TEMP_1 | 5.59509 | True | True | True |
| 1min | CHL_SW_TEMP_1 | 1.25704 | True | False | True |
| 1min | CHL_RWCD_TEMP_1 | 4.086 | True | True | True |
| 15min | CHL_POW_1 | 1.20126 | True | True | True |
| 15min | CT_SW_TEMP_1 | 5.86162 | True | True | True |
| 15min | CHL_SW_TEMP_1 | 1.18541 | True | False | True |
| 15min | CHL_RWCD_TEMP_1 | 4.33269 | True | True | True |
| 1h | CHL_POW_1 | 1.50761 | True | True | True |
| 1h | CT_SW_TEMP_1 | 9.0343 | True | True | True |
| 1h | CHL_SW_TEMP_1 | 1.57157 | True | False | True |
| 1h | CHL_RWCD_TEMP_1 | 6.9097 | True | True | True |
| 2h | CHL_POW_1 | 1.57558 | True | True | True |
| 2h | CT_SW_TEMP_1 | 8.98194 | True | True | True |
| 2h | CHL_SW_TEMP_1 | 1.68744 | False | False | True |
| 2h | CHL_RWCD_TEMP_1 | 6.89 | True | True | True |

### Residual Statistics

| Sampling | Target | Dataset | Residual Mean | Residual RMS | Residual P95 |
| --- | --- | --- | --- | --- | --- |
| 1min | CHL_POW_1 | Baseline | 0.0682649 | 7.79265 | 6.68148 |
| 1min | CHL_POW_1 | 095 | 0.104879 | 7.82836 | 6.85937 |
| 1min | CHL_POW_1 | 080 | 0.309786 | 8.13592 | 7.93277 |
| 1min | CHL_POW_1 | 065 | 0.770306 | 8.77835 | 10.4982 |
| 1min | CT_SW_TEMP_1 | Baseline | 0.00183445 | 0.27819 | 0.35067 |
| 1min | CT_SW_TEMP_1 | 095 | 0.13199 | 0.333712 | 0.510948 |
| 1min | CT_SW_TEMP_1 | 080 | 0.604068 | 0.798706 | 1.3665 |
| 1min | CT_SW_TEMP_1 | 065 | 1.2557 | 1.5565 | 2.75886 |
| 1min | CHL_SW_TEMP_1 | Baseline | 0.00166448 | 0.169252 | 0.185307 |
| 1min | CHL_SW_TEMP_1 | 095 | 0.00136223 | 0.181683 | 0.194897 |
| 1min | CHL_SW_TEMP_1 | 080 | 0.00100041 | 0.186975 | 0.195576 |
| 1min | CHL_SW_TEMP_1 | 065 | 0.000458823 | 0.212758 | 0.20176 |
| 1min | CHL_RWCD_TEMP_1 | Baseline | 0.00264073 | 0.278782 | 0.344879 |
| 1min | CHL_RWCD_TEMP_1 | 095 | 0.0341374 | 0.302231 | 0.498721 |
| 1min | CHL_RWCD_TEMP_1 | 080 | 0.197557 | 0.560362 | 1.24893 |
| 1min | CHL_RWCD_TEMP_1 | 065 | 0.499622 | 1.1391 | 2.47653 |
| 15min | CHL_POW_1 | Baseline | 0.0733862 | 6.38479 | 6.96344 |
| 15min | CHL_POW_1 | 095 | 0.11238 | 6.57215 | 7.16643 |
| 15min | CHL_POW_1 | 080 | 0.311296 | 6.94888 | 8.07484 |
| 15min | CHL_POW_1 | 065 | 0.779739 | 7.66982 | 10.6555 |
| 15min | CT_SW_TEMP_1 | Baseline | 0.00460757 | 0.264809 | 0.339936 |
| 15min | CT_SW_TEMP_1 | 095 | 0.136644 | 0.320821 | 0.497515 |
| 15min | CT_SW_TEMP_1 | 080 | 0.609347 | 0.794708 | 1.35764 |
| 15min | CT_SW_TEMP_1 | 065 | 1.25879 | 1.55221 | 2.73396 |
| 15min | CHL_SW_TEMP_1 | Baseline | 0.00177967 | 0.155354 | 0.188339 |
| 15min | CHL_SW_TEMP_1 | 095 | 0.00184763 | 0.177667 | 0.198604 |
| 15min | CHL_SW_TEMP_1 | 080 | 0.00157288 | 0.180834 | 0.200762 |
| 15min | CHL_SW_TEMP_1 | 065 | 0.00443149 | 0.184158 | 0.208913 |
| 15min | CHL_RWCD_TEMP_1 | Baseline | 0.00225935 | 0.260831 | 0.320247 |
| 15min | CHL_RWCD_TEMP_1 | 095 | 0.0352635 | 0.286286 | 0.481542 |
| 15min | CHL_RWCD_TEMP_1 | 080 | 0.199418 | 0.551355 | 1.22267 |
| 15min | CHL_RWCD_TEMP_1 | 065 | 0.499893 | 1.1301 | 2.45344 |
| 1h | CHL_POW_1 | Baseline | 0.0832143 | 4.03608 | 5.11289 |
| 1h | CHL_POW_1 | 095 | 0.153725 | 4.7297 | 5.66351 |
| 1h | CHL_POW_1 | 080 | 0.327209 | 5.09498 | 6.40593 |
| 1h | CHL_POW_1 | 065 | 0.800214 | 6.08483 | 8.97273 |
| 1h | CT_SW_TEMP_1 | Baseline | 0.00538905 | 0.169424 | 0.238849 |
| 1h | CT_SW_TEMP_1 | 095 | 0.141379 | 0.249812 | 0.424985 |
| 1h | CT_SW_TEMP_1 | 080 | 0.612943 | 0.76757 | 1.28895 |
| 1h | CT_SW_TEMP_1 | 065 | 1.26238 | 1.53063 | 2.60353 |
| 1h | CHL_SW_TEMP_1 | Baseline | 0.00079049 | 0.103089 | 0.114346 |
| 1h | CHL_SW_TEMP_1 | 095 | 0.00236742 | 0.145158 | 0.135663 |
| 1h | CHL_SW_TEMP_1 | 080 | 0.00157926 | 0.145552 | 0.143467 |
| 1h | CHL_SW_TEMP_1 | 065 | 0.00308194 | 0.162012 | 0.152454 |
| 1h | CHL_RWCD_TEMP_1 | Baseline | 0.00249483 | 0.158998 | 0.208714 |
| 1h | CHL_RWCD_TEMP_1 | 095 | 0.0391733 | 0.200166 | 0.392785 |
| 1h | CHL_RWCD_TEMP_1 | 080 | 0.202103 | 0.509746 | 1.13786 |
| 1h | CHL_RWCD_TEMP_1 | 065 | 0.502842 | 1.09863 | 2.32963 |
| 2h | CHL_POW_1 | Baseline | 0.144961 | 3.07581 | 4.19254 |
| 2h | CHL_POW_1 | 095 | 0.207851 | 3.75533 | 4.86196 |
| 2h | CHL_POW_1 | 080 | 0.386376 | 3.8525 | 5.87963 |
| 2h | CHL_POW_1 | 065 | 0.833041 | 4.84618 | 8.21594 |
| 2h | CT_SW_TEMP_1 | Baseline | 0.00797435 | 0.167601 | 0.201103 |
| 2h | CT_SW_TEMP_1 | 095 | 0.14567 | 0.244422 | 0.400785 |
| 2h | CT_SW_TEMP_1 | 080 | 0.616422 | 0.752447 | 1.25128 |
| 2h | CT_SW_TEMP_1 | 065 | 1.26528 | 1.50538 | 2.47859 |
| 2h | CHL_SW_TEMP_1 | Baseline | 0.00231152 | 0.0772974 | 0.0783182 |
| 2h | CHL_SW_TEMP_1 | 095 | 0.00388438 | 0.107826 | 0.100512 |
| 2h | CHL_SW_TEMP_1 | 080 | 0.00224528 | 0.103653 | 0.102077 |
| 2h | CHL_SW_TEMP_1 | 065 | 0.00582414 | 0.130435 | 0.11696 |
| 2h | CHL_RWCD_TEMP_1 | Baseline | 0.00635475 | 0.154589 | 0.180183 |
| 2h | CHL_RWCD_TEMP_1 | 095 | 0.0449209 | 0.19027 | 0.359549 |
| 2h | CHL_RWCD_TEMP_1 | 080 | 0.207116 | 0.488308 | 1.0639 |
| 2h | CHL_RWCD_TEMP_1 | 065 | 0.506852 | 1.06512 | 2.20088 |

## Section 4: Sensitivity Retention Audit

| Sampling | Target | Sensitivity | Retention Ratio |
| --- | --- | --- | --- |
| 1min | CHL_POW_1 | 0.126491 | 1 |
| 1min | CT_SW_TEMP_1 | 4.59509 | 1 |
| 1min | CHL_SW_TEMP_1 | 0.257044 | 1 |
| 1min | CHL_RWCD_TEMP_1 | 3.086 | 1 |
| 15min | CHL_POW_1 | 0.201265 | 1.59114 |
| 15min | CT_SW_TEMP_1 | 4.86162 | 1.058 |
| 15min | CHL_SW_TEMP_1 | 0.18541 | 0.721317 |
| 15min | CHL_RWCD_TEMP_1 | 3.33269 | 1.07994 |
| 1h | CHL_POW_1 | 0.507608 | 4.013 |
| 1h | CT_SW_TEMP_1 | 8.0343 | 1.74845 |
| 1h | CHL_SW_TEMP_1 | 0.571571 | 2.22364 |
| 1h | CHL_RWCD_TEMP_1 | 5.9097 | 1.915 |
| 2h | CHL_POW_1 | 0.575578 | 4.55035 |
| 2h | CT_SW_TEMP_1 | 7.98194 | 1.73706 |
| 2h | CHL_SW_TEMP_1 | 0.687443 | 2.67442 |
| 2h | CHL_RWCD_TEMP_1 | 5.89 | 1.90862 |

### Sampling Summary

| Sampling | B1 Pass | B2.1 RMS Monotonic Pass | Min Retention Ratio | Overall Pass |
| --- | --- | --- | --- | --- |
| 1min | True | True | 1 | True |
| 15min | True | True | 0.721317 | False |
| 1h | True | True | 1.74845 | True |
| 2h | True | False | 1.73706 | False |

## Section 5: Conclusion

### Q1: How far can sampling frequency be reduced before Expected State performance degrades?

Expected State performance passes through: 1min, 15min, 1h, 2h.

### Q2: How far can sampling frequency be reduced before degradation detection fails?

Residual RMS monotonicity passes through: 1min, 15min, 1h.

### Q3: What is the minimum viable sampling interval?

1h

### Q4: Do results support future Marine deployment?

Yes, preliminarily. The conservative audit supports lower-frequency monitoring and suggests marine hourly/logbook-scale data may be usable, subject to marine-domain validation.