# Health Indicator Evaluation Protocol

## Section 1

# Evaluation Framework Origin

This document freezes the common evaluation protocol for Health Indicator candidates developed during Phase 2.

The protocol separates evaluation dimensions into two groups:

* Industrial Consensus Dimensions
* Project-Specific Dimensions

All Health Indicator candidates evaluated in Task H2 shall use this common protocol.

No candidate-specific evaluation criteria shall be introduced during candidate evaluation.

---

## Group A — Industrial Consensus Dimensions

Source:

* Coble & Hines (2009)
* Industrial Health Indicator Framework Survey

These dimensions represent broadly accepted PHM evaluation principles.

| Dimension | Definition |
| --- | --- |
| Monotonicity | HI exhibits a generally consistent direction of change as degradation accumulates. |
| Trendability | HI shows a coherent relationship with time or usage across repeated observations. |
| Robustness | HI remains insensitive to operating-condition variation after Condition Normalization while remaining sensitive to persistent degradation. |
| Interpretability | HI meaning can be explained to a domain engineer without statistical or machine-learning training. |

---

## Group B — Project-Specific Dimensions

Source:

* Field Interview Consensus v1.0
* Phase 1 Scientific Review
* Marine deployment requirements

These dimensions reflect the engineering and deployment constraints of this project.

| Dimension | Definition |
| --- | --- |
| Reset Compatibility | Evaluate whether a Health Indicator can correctly re-establish its baseline following maintenance without retaining obsolete health information. |
| Engineering Meaning | HI represents an engineering quantity recognizable and meaningful to marine engineers. |
| Marine Deployability | HI can be computed using data available from typical vessel instrumentation without requiring additional sensors. |
| Traceability | Changes in the HI can be explained through upstream residual behavior and processing steps rather than appearing as unexplained black-box outputs. |

Reset Compatibility qualitative levels:

```text
Excellent

Good

Moderate

Poor
```

For Stateful Health Indicators only, reviewers shall document:

* Reset Strategy
* Warm-up Strategy
* Baseline Transition Strategy

No numerical scoring is required.

Absence of lifecycle documentation shall be treated as an incomplete review item rather than automatic algorithm rejection.

### H5 Lifecycle Extension — Reset Compatibility

Reset Compatibility is appended as a Project-Specific Evaluation Dimension for H5 lifecycle review.

Definition:

Evaluate whether an HI algorithm provides a clear engineering strategy for handling maintenance events and baseline reconstruction.

Evaluation focuses on architecture rather than implementation.

Typical review questions:

* Does the algorithm contain internal state?
* If stateful, is a deterministic reset policy defined?
* Is post-maintenance warm-up behavior documented?
* Can historical contamination be removed in a traceable manner?

Review Policy:

Algorithms lacking Reset Compatibility documentation are treated as:

```text
Incomplete review items
```

rather than:

```text
Automatically rejected algorithms
```

Reset Compatibility is an evaluation dimension, not a disqualification criterion.

---

## Section 2

# Evaluation Method

Every candidate Health Indicator evaluated in Task H2 shall follow exactly the same evaluation procedure.

---

## Step 1

## Qualitative Assessment

For every evaluation dimension, assign one of:

```text
Strong

Acceptable

Weak

Not Assessable
```

Provide one concise sentence explaining the evidence supporting the assessment.

The qualitative assessment shall cover all dimensions from Group A and Group B.

---

## Step 2

## Quantitative Assessment

Where the LBNL dataset permits quantitative evaluation, compute reference metrics.

| Dimension | Reference Metric |
| --- | --- |
| Monotonicity | Proportion of consecutive HI pairs exhibiting consistent direction |
| Trendability | Spearman correlation with time index |
| Robustness | HI variance across operating-condition bins |
| Interpretability | Qualitative assessment only |
| Traceability | Qualitative assessment only |

Prognosability is intentionally excluded because the LBNL dataset contains no run-to-failure trajectories.

This limitation shall be documented rather than compensated by alternative metrics.

---

## Step 3

## Overall Assessment

Assign one overall outcome:

```text
Accepted

Accepted with Conditions

Rejected
```

State one primary justification.

The overall assessment shall be based on the common protocol rather than on candidate-specific criteria.

---

## Section 3

# Evaluation Scope and Limitations

The following limitations define the valid interpretation boundary of Phase 2 Health Indicator evaluation.

---

## Limitation 1

The LBNL dataset contains no labeled degradation events.

Therefore Monotonicity and Trendability can only be evaluated descriptively rather than against confirmed degradation ground truth.

---

## Limitation 2

Prognosability cannot be evaluated.

Defer to Marine validation.

---

## Limitation 3

Marine Deployability is assessed using engineering judgment derived from the Field Interview Consensus.

It is not statistically validated within Phase 2.

---

## Limitation 4

Traceability assessment evaluates engineering explainability only.

It does not evaluate model interpretability algorithms or explainable AI techniques.

---

## Section 4

# Disqualification Criteria

Candidates meeting any of the following conditions shall be rejected immediately without full evaluation.

These represent hard engineering constraints rather than trade-off dimensions.

---

## DQ-1

The Health Indicator cannot be explained to a domain engineer.

---

## DQ-2

The Health Indicator requires measurements unavailable from standard vessel instrumentation.

---

## DQ-3

The Health Indicator conflates operating-condition variation with degradation signal.

---

## DQ-4

The Health Indicator cannot be re-baselined after maintenance without complete reconstruction.

---

## DQ-5

The Health Indicator cannot be meaningfully evaluated using the available evidence within the current project phase.

Experimental ideas lacking an observable validation pathway shall be deferred rather than accepted.

---

## Section 5

# Evaluation Philosophy

Health Indicator candidates shall be compared using one common evaluation protocol rather than candidate-specific evaluation criteria.

Evaluation focuses on engineering usefulness rather than mathematical sophistication.

Algorithmic novelty shall never compensate for weak engineering interpretability.

A candidate shall be accepted only if it demonstrates measurable engineering value within the available evidence in the current project phase.

Future candidates introduced during later phases shall be evaluated using the same protocol unless the protocol itself is formally revised.

---

## Section 6

# Reviewer Sign-off

Reviewer shall answer:

```text
Q1

Do the evaluation dimensions adequately cover the engineering requirements of Phase 2?

Q2

Are the disqualification criteria appropriate?

Q3

Are any important evaluation dimensions still missing?

Reviewer Decision

PASS

REVISE
```

Reviewer completes manually.

The script shall not answer reviewer questions.
