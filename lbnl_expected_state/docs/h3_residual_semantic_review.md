# H3 Residual Semantic Admissibility Review

## 1. Purpose

This review determines under what operating conditions a residual carries Potential Health Evidence.

H3 does not construct a new Health Indicator.

H3 does not implement a semantic masking algorithm.

H3 defines the semantic boundary between operating-condition variation and Candidate Health Evidence before further Health Indicator construction.

## 2. Background

Phase 1 established that the residual satisfies statistical validity requirements through:

```text
Bias Audit

Leakage Audit

Scientific Review
```

Task H2 evaluated three candidate Health Indicators and reached the following reviewer consensus:

* Candidate A (Raw Residual): Rejected
* Candidate B (Absolute Residual): Accepted with Conditions
* Candidate C (Rolling Mean Absolute Residual): Accepted with Conditions

The dominant observation was that seasonal operating-condition variation, rather than degradation, appeared to dominate the temporal behavior of all three candidates.

Therefore H3 addresses the question:

```text
Under what operating conditions can a residual legitimately support health interpretation?
```

## 3. Scientific Motivation

Residual statistical validity and residual semantic meaning are different questions.

Phase 1 answered:

```text
Can the residual be trusted statistically?
```

H3 answers:

```text
Can the residual be interpreted as Potential Health Evidence?
```

Residuals that pass statistical validation may still represent:

* operating-condition variation
* startup dynamics
* shutdown dynamics
* control transitions
* sensor settling

rather than equipment degradation.

Accumulating these residuals would accumulate operating-condition information instead of health information.

## 4. Scope

H3 evaluates Residual Semantic Admissibility only.

H3 does not evaluate:

* Expected State prediction quality
* model architecture
* Health Indicator construction methods
* Remaining Useful Life
* maintenance decision support
* masking algorithms
* optimization of any kind

## 5. Execution Responsibility

Script and Reviewer responsibilities are explicitly separated.

### Q1 - Script Supported

Q1 is supported by quantitative analysis.

The script generated summary statistics, figures, and descriptive observations for Q1.

The script does not interpret results or make semantic judgments.

### Q2, Q3, Q4 - Reviewer Only

Q2, Q3, and Q4 are Reviewer assessments only.

No semantic masking algorithm is implemented.

No optimization experiment is conducted.

No new Health Indicator is constructed.

Reviewer assessments shall be based on existing figures, Phase 1 evidence, and H2 observations.

## 6. Q1 - Residual Condition Dependence

Q1 asks how much operating-condition information remains within the residual after Phase 1 normalization.

Analysis is Train split only.

Figures show Residual vs Condition Variable with a binned Residual Expectation overlay.

### Q1 Figures

| Condition Variable | Figure |
|---|---|
| OA_TEMP | lbnl_expected_state/outputs/figures/h3/residual_vs_oa_temp.png |
| OA_TEMP_WB | lbnl_expected_state/outputs/figures/h3/residual_vs_oa_temp_wb.png |
| CWL_SEC_LOAD | lbnl_expected_state/outputs/figures/h3/residual_vs_cwl_sec_load.png |
| CWL_SEC_CW_FLOW | lbnl_expected_state/outputs/figures/h3/residual_vs_cwl_sec_cw_flow.png |
| CT_SW_TEMPSPT | lbnl_expected_state/outputs/figures/h3/residual_vs_ct_sw_tempspt.png |
| CWL_PRI_SW_TEMPSPT | lbnl_expected_state/outputs/figures/h3/residual_vs_cwl_pri_sw_tempspt.png |

### Q1 Summary Statistics

| Condition Variable | Spearman Corr. Residual vs Condition | Residual Expectation Lowest Quintile | Residual Expectation Highest Quintile | High - Low |
|---|---:|---:|---:|---:|
| OA_TEMP | 0.051534 | 0.019286 | -0.003285 | -0.022571 |
| OA_TEMP_WB | 0.045698 | 0.018409 | 0.015341 | -0.003068 |
| CWL_SEC_LOAD | 0.078889 | 0.008712 | -0.012040 | -0.020753 |
| CWL_SEC_CW_FLOW | -0.045813 | 0.011202 | 0.007235 | -0.003967 |
| CT_SW_TEMPSPT | 0.027443 | -0.006372 | 0.013290 | 0.019662 |
| CWL_PRI_SW_TEMPSPT | -0.013340 | 0.031792 | -0.000599 | -0.032392 |

Descriptive observation field:

```text
Reviewer to complete.
```

No causal interpretation is made by the script.

## 7. Q2 - Candidate Semantic Mask Regions

Reviewer assessment only.

Reviewer shall identify operating regions where residuals should not be automatically interpreted as Candidate Health Evidence.

Classification options:

```text
Likely requires semantic exclusion
Possibly requires semantic exclusion
Probably acceptable
Not Assessable
```

| Candidate Region | Reviewer Classification | Notes |
|---|---|---|
| Near-zero Load (system startup or shutdown) |  |  |
| Large Load Transitions |  |  |
| Control Stabilization periods |  |  |
| Sensor settling |  |  |
| Seasonal operating-regime boundaries |  |  |

## 8. Q3 - Semantic Admissibility Assessment

Reviewer assessment only.

Reviewer shall evaluate whether excluding candidate semantic regions identified in Q2 would improve the engineering meaning of residual-derived Health Indicators.

Evaluation shall reference:

* Phase 1 Leakage Audit results
* Decision012
* Decision013
* H2 Reviewer Assessment Table
* Q1 quantitative observations

Reviewer assessment:

```text

```

## 9. Q4 - Candidate HI Reassessment

Reviewer assessment only.

Reviewer shall re-evaluate Candidate B and Candidate C from a semantic perspective.

Q4 shall compare candidate HI behavior between operating regions exhibiting low Condition dependence and operating regions exhibiting high Condition dependence, using Phase 1 Leakage Audit and Decision012 / Decision013 as supporting evidence.

Reviewer shall determine whether previously observed limitations originate from:

```text
Residual construction

or

Residual semantic interpretation
```

If limitations primarily arise from semantic interpretation, document the implications for H4.

Reviewer assessment:

```text

```

## 10. Residual Semantic Classification

Classification applies to observed residual patterns and operating regions, not to individual data points.

| Category | Meaning |
|---|---|
| Candidate Health Evidence | Satisfies Statistical Validity and Semantic Admissibility, and may support health interpretation |
| Condition Evidence | Primarily reflects operating-condition variation rather than equipment health |
| Mixed Evidence | Cannot currently separate health from condition influence with available data |
| Potential Health Evidence | May support health interpretation, but has not yet completed all required validation layers |
| Not Assessable | Available evidence is insufficient to classify |

Reviewer classification table:

| Pattern Description | Classification | Engineering Justification |
|---|---|---|
| Seasonal amplitude variation across Train period |  |  |
| Near-zero Load region spikes |  |  |
| Persistent slow drift within stable operating window |  |  |
| High-load region residual scatter |  |  |
| Additional reviewer-identified pattern |  |  |

## 11. Project Architecture Update

Updated conceptual pipeline:

```text
Physics Layer
-----------------------

Expected State

↓

Residual

Engineering Layer
-----------------------

Residual Statistical Validity

↓

Residual Semantic Admissibility

↓

Candidate Health Evidence

↓

Health Indicator Construction

Decision Layer
-----------------------

Health Assessment

↓

Maintenance Recommendation
```

Residual Statistical Validity and Residual Semantic Admissibility are distinct validation stages.

Statistical validity does not imply engineering interpretability as Candidate Health Evidence.

Semantic Admissibility shall be evaluated using both Residual Expectation and Residual Dispersion, as both may contain operating-condition-dependent information.

Physics Layer is validated statistically.

Engineering Layer is validated through engineering interpretation and controlled experiments.

Decision Layer requires operational stakeholder consensus.

## 12. Scientific Boundary

This task does not claim:

* true degradation detection
* fault diagnosis
* Remaining Useful Life prediction
* maintenance effectiveness
* optimal masking strategy

The LBNL dataset contains no labeled degradation events.

Therefore all semantic conclusions remain limited to engineering interpretation within the available operating data.

## 13. Reviewer Questions

Reviewer shall answer:

```text
Q1

Does H3 clearly distinguish statistical validity
from engineering health semantics?

Q2

Have the major operating-condition-driven
residual patterns been identified?

Q3

Is the Residual Semantic Classification
sufficiently justified?

Q4

Can Phase 2 proceed to H4 without introducing
avoidable semantic ambiguity?

Reviewer Decision:

PASS

PASS WITH CONDITIONS

REVISE
```

Reviewer answers:

```text

```

## 14. Recommendations for H4

Reviewer to complete after Q2, Q3, and Q4 assessment.

```text

```
