# Validation M-1 Condition Leakage Audit Protocol

Date:

2026-06-10

Status:

Pre-registered

Experiment:

M-1

---

## 1. Motivation

Validation I-1 failed.

Observed trends were strongly correlated with:

OA_TEMP

and

CWL_SEC_LOAD.

This suggests that residual and HI
may still contain condition information.

The objective of M-1 is to determine:

Why does condition information remain
inside the residual?

---

## 2. Research Question

Q:

Why do residual and HI remain correlated
with condition variables despite those
variables already being included in
the Expected State model?

---

## 3. Null Hypothesis

H0:

Residual is condition-independent.

Residual and HI contain primarily
health-related information.

Condition variables explain
little additional variance.

---

## 4. Alternative Hypothesis

H1:

Residual still contains significant
condition information.

Residual construct validity
remains incomplete.

---

## 5. Dataset Scope

Use existing LBNL Baseline data.

Use frozen residuals.

No retraining.

No new datasets.

No fault data.

---

## 6. Metrics

Measure correlations between:

Residual RMS

and:

OA_TEMP

CWL_SEC_LOAD

and other available condition variables.

Also evaluate:

HI_v0

against:

OA_TEMP

and load.

Compute:

Spearman

Pearson

R²

where appropriate.

---

## 7. Leakage Taxonomy

If leakage is confirmed,
classify it into one of four types.

### Type A

Model Capacity Limitation

Condition variables are present.

Model fitting is insufficient.

Possible remedy:

feature engineering

or

higher model capacity.

---

### Type B

Incomplete Condition Variables

Important seasonal drivers are missing.

Possible remedy:

expand condition variable set.

---

### Type C

Extrapolation Failure

Training distribution differs
from operating distribution.

Possible remedy:

season-specific models

or

training set redesign.

---

### Type D

Residual Definition Problem

Expected State formulation itself
may be incorrect.

Possible remedy:

re-examine pipeline assumptions.

---

## 8. Success Criterion

Residual and HI show weak dependence
on condition variables.

Condition information explains
little variance.

Residual construct validity survives.

---

## 9. Failure Criterion

Strong condition dependence remains.

Leakage type can be identified.

Residual construct validity
requires revision.

---

## 10. Consequences of Failure

Failure does NOT invalidate
the project.

Failure indicates:

Expected State → Residual

requires further study.

Forward validation remains suspended.

Validation D remains blocked.

No specific remediation path
is assumed.

Leakage taxonomy should guide
future investigation.

---

## 11. Philosophy

Leakage is not an error.

Leakage is information.

Classification comes before correction.

Unknown remains acceptable.

---

## Version History

v0.1

2026-06-10

Initial protocol.
