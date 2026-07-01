# LBNL Expected State Experiment

## Phase 1 — Constructing an Engineering Expected State

Version: v1.0 (Frozen)

Status: Execution Specification

---

# 1. Background

Following two weeks of Deep Research, Constraint Extraction, CN Question Tree, and Marine Translation, the project now returns to data-driven experimentation.

The objective of this phase is **not** to optimize prediction accuracy.

It is **not** an algorithm benchmark.

It is **not** yet a Health Indicator study.

The objective is to answer one engineering question:

> **What should a healthy system output under the current operating condition?**

Only after an engineering-credible Expected State is established can Residuals acquire engineering meaning.

Residual-based Health Indicators, Trend Monitoring, Baseline Management, and Marine Translation all depend on this foundation.

---

# 2. Relation to Previous LBNL Work

Previous work (Outcome 2) investigated:

```
Prediction Target
        ↓
Information Usage
```

Its focus was prediction behavior.

The present study investigates:

```
Condition
        ↓
Expected State
```

Its focus is engineering state construction.

---

# 3. Scope of Phase 1

Phase 1 is intentionally limited.

Only the following question is addressed:

> Can an engineering-credible Expected State be established?

Therefore Phase 1 ends after Residual Leakage Audit.

The following topics are explicitly postponed to Phase 2:

* Residual Temporal Structure
* Feature Importance
* SHAP Analysis
* Health Indicator Construction

---

# 4. MVP Experimental Flow

```
Stage 0

Data Audit

↓

Condition Space Coverage Audit

↓

Train/Test Coverage Audit

↓

Condition Correlation Audit

↓

Stage 1

Condition Variable Selection

↓

Stage 2

Expected State Construction

↓

Stage 3

Prediction Stability Audit

↓

Stage 4

Residual Bias Audit

↓

Stage 5

Residual Leakage Audit
```

---

# 5. Stage Definitions

## Stage 0 — Data & Condition Audit

Objective:

Determine whether the dataset supports Expected State construction.

### 0.1 Data Quality Audit

Check:

* Missing values
* Duplicate timestamps
* Constant variables
* Sensor range violations
* Physically impossible observations
* Large temporal gaps

Output:

* Data Quality Report

### 0.2 Condition Space Coverage

Evaluate coverage of:

* Outdoor Temperature
* Cooling Load
* Flow
* Setpoint
* Operating Region

Visualization:

* Scatter plots
* Density plots
* Histograms

Output:

Condition Space Coverage Report.

### 0.3 Train/Test Coverage

Compare Condition Space between temporal train and test periods.

Output:

* Train/Test Coverage Overlay

### 0.4 Correlation Audit

Evaluate multicollinearity among candidate Condition Variables.

Output:

* Correlation Matrix

### 0.5 Operating Envelope

Summarize the operating region represented by the dataset.

The Expected State is considered valid only inside this observed operating envelope.

Output:

* Operating Envelope Summary

---

## Stage 1 — Condition Variable Selection

Select variables describing operating condition.

Avoid variables potentially containing health information.

Output:

* Frozen Condition Variable Set

---

## Stage 2 — Expected State Construction

Prediction Target:

* Chiller Power

Baseline Model:

* XGBoost

Objective:

```
Condition
        ↓
Expected Power
```

The objective is engineering credibility rather than maximum predictive accuracy.

---

## Stage 3 — Prediction Stability Audit

Evaluate whether the Expected State is sufficiently stable for engineering analysis.

Evaluation includes:

* RMSE
* MAE
* R²

These metrics are descriptive rather than acceptance criteria.

Stability assessment includes:

* Train/Test performance gap
* Time-block consistency
* Residual mean stability
* Regional error distribution

Validation uses temporal split.

Random split is intentionally avoided.

---

## Stage 4 — Residual Bias Audit

Objective:

Determine whether systematic bias remains.

Evaluate:

```
E(Residual | Condition)
```

Examples:

* Residual vs Load
* Residual vs Outdoor Temperature

Output:

Bias Report.

---

## Stage 5 — Residual Leakage Audit

Primary objective of Phase 1.

Question:

Does Residual still contain Condition Information?

Evaluation:

Level 1

* Linear Regression

Level 2

* Tree-based Model

  * XGBoost or Random Forest

The objective is not pass/fail classification.

The objective is quantitative leakage estimation.

Negative Control:

Residual Shuffle

Residual→Condition prediction after shuffling should collapse near the finite-sample baseline.

Engineering thresholds are intentionally not predefined.

---

# 6. Deliverables

Figures

1. Data Quality Summary
2. Condition Space Coverage
3. Train/Test Coverage
4. Prediction vs Ground Truth
5. Residual Distribution
6. Residual vs Load
7. Residual vs Outdoor Temperature

Outputs

* Expected State Model
* Residual Dataset
* Bias Audit Report
* Leakage Audit Report
* Operating Envelope Summary
* Experiment Manifest

---

# 7. Experiment Manifest

Each experimental run should archive a manifest containing:

* Dataset version
* Target variable
* Condition Variables
* Train/Test periods
* Model type
* Random seed
* Feature version

This guarantees experiment reproducibility.

---

# 8. Success Criteria

Minimum Success:

✓ Condition Variables frozen

✓ Target variable fixed

✓ Temporal Train/Test split completed

✓ Engineering Expected State established

✓ Residual Dataset generated

✓ Bias Audit completed

✓ Leakage Audit completed

Final conclusion shall be reported as one of the following:

A

Expected State is usable.

—

B

Expected State is usable with known bias.

—

C

Expected State is not usable.

Return to Condition definition.

---

# 9. Current Consensus

The following principles are frozen for Phase 1.

① No predefined engineering thresholds.

Phase 1 emphasizes observation rather than acceptance testing.

---

② Prediction accuracy is not the primary objective.

Engineering interpretability of Residual is.

---

③ Bias and Information Leakage are treated as independent questions.

Stage 4

Bias

Stage 5

Information Leakage

---

④ Phase 1 ends after Residual.

Temporal structure, Feature Importance, SHAP, Health Indicator and Marine Translation validation belong to later phases.

---

# 10. Position within the Overall Project

```
Condition
        ↓
Expected State
        ↓
Residual
        ↓
Health Indicator
        ↓
Trend Monitoring
        ↓
Marine Translation Validation
```

Phase 1 establishes the first experimentally verifiable layer of the Marine Health Monitoring framework.

Its purpose is to evaluate whether an engineering-credible Expected State can be established under the current experimental setting.

No broader conclusions are implied beyond this scope.
