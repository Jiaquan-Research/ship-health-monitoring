# Evidence Philosophy Taxonomy

Status

```text
Framework Draft
```

Purpose

Provide a reusable conceptual taxonomy describing how different Health Evidence prototypes organize information.

This taxonomy classifies **Evidence Philosophies**, not algorithms.

Multiple algorithms may belong to the same philosophy.

Evidence Committee design should prioritize diversity of Evidence Philosophies rather than multiple implementations of the same philosophy.

---

## 1. Why Evidence Philosophy?

Algorithm names are not sufficient for engineering organization.

Examples:

* Rolling Mean
* Rolling MAD
* EWMA

These appear different mathematically, but share essentially the same information organization philosophy.

The purpose of this taxonomy is to classify:

> how evidence is constructed

rather than:

> how evidence is numerically computed

This distinction prevents Evidence Committee design from counting multiple implementations of the same engineering idea as independent evidence sources.

---

## 2. Current Evidence Philosophy Taxonomy

```text
Health Evidence

├── Magnitude Philosophy

├── Filtering Philosophy

├── Accumulation Philosophy

└── Geometry Philosophy
```

This taxonomy reflects the current validated H5 prototype families.

Future philosophies are intentionally reserved.

---

## 3. Philosophy Definitions

## Magnitude Philosophy

### Definition

Magnitude Philosophy treats the current size of a deviation as engineering evidence.

### Underlying Assumption

> Larger deviation implies stronger abnormality.

### Core Information Organization

Immediate deviation.

### Typical Algorithms

* Absolute Residual

### Strengths

* Direct engineering interpretation.
* Minimal lifecycle complexity.
* Naturally explainable to operators and engineers.

### Weaknesses

* Sensitive to operating-condition variation.
* May react to transient disturbances.
* Does not distinguish persistent behaviour from isolated deviation.

### Evidence Invalidation Conditions

* Startup
* Shutdown
* Boundary operating regions
* Out-of-distribution conditions

These are engineering guidance notes rather than formal rejection rules.

### Marine Examples

A ship engineer observes that current fuel consumption, exhaust temperature, or cooling deviation is larger than expected under the current operating condition.

This is a conceptual example only and does not claim validation.

### Lifecycle Considerations

Magnitude evidence is generally stateless.

It is naturally reset-compatible because it does not retain historical state.

### Representative Prototype

Absolute Residual.

---

## Filtering Philosophy

### Definition

Filtering Philosophy treats locally persistent behaviour as more meaningful than instantaneous fluctuation.

### Underlying Assumption

> Persistent behaviour is more informative than instantaneous fluctuation.

### Core Information Organization

Temporal smoothing.

### Typical Algorithms

* Rolling Mean
* Rolling MAD
* EWMA

### Strengths

* Reduces short-term noise.
* Supports trend review.
* Aligns with existing engineering practice of reviewing historical curves.

### Weaknesses

* Different filters may provide overlapping evidence.
* Window or smoothing state requires documentation.
* May delay response to abrupt changes.

### Evidence Invalidation Conditions

* Maintenance reset
* Warm-up period
* Large operating regime transition

These are engineering guidance notes rather than formal rejection rules.

### Marine Examples

A ship engineer compares a smoothed trend of cooling deviation or power deviation over a watch period instead of reacting to each individual sample.

This is a conceptual example only and does not claim validation.

### Lifecycle Considerations

Filtering may have finite memory or recursive state depending on implementation.

Warm-up behaviour and maintenance reset implications should be documented where state is retained.

### Representative Prototype

Rolling Mean.

---

## Accumulation Philosophy

### Definition

Accumulation Philosophy treats repeated small deviations as meaningful once they accumulate over time.

### Underlying Assumption

> Small deviations become meaningful through accumulation.

### Core Information Organization

Historical accumulation.

### Typical Algorithms

* CUSUM

### Strengths

* Sensitive to sustained weak changes.
* Captures history that may be invisible in instantaneous evidence.
* Useful where persistent change matters more than single-sample magnitude.

### Weaknesses

* Requires lifecycle management.
* Historical contamination can dominate future outputs.
* Maintenance reset behaviour is mandatory.

### Evidence Invalidation Conditions

* Missing reset
* Historical contamination
* Evidence saturation

These are engineering guidance notes rather than formal rejection rules.

### Marine Examples

A ship engineer observes that small deviations in fuel margin, cooling performance, or vibration evidence accumulate across many operating hours.

This is a conceptual example only and does not claim validation.

### Lifecycle Considerations

Accumulation evidence is stateful.

Maintenance events may invalidate accumulated evidence.

Reset policy, warm-up behaviour, and state persistence must be documented.

### Representative Prototype

CUSUM.

---

## Geometry Philosophy

### Definition

Geometry Philosophy treats evidence as distance from a learned normal evidence space.

### Underlying Assumption

> Healthy operation occupies a stable region in feature space.

### Core Information Organization

Multivariate spatial relationship.

### Typical Algorithms

* Mahalanobis Distance

### Strengths

* Captures relationships among multiple evidence dimensions.
* Can organize multivariate deviation as a single engineering signal.
* Provides complementary information to magnitude or filtering evidence.

### Weaknesses

* Depends on the quality of the reference distribution.
* Can be affected by training distribution mismatch.
* May be difficult to interpret without supporting evidence views.

### Evidence Invalidation Conditions

* Training distribution mismatch
* Covariance instability
* Novel operating regime

These are engineering guidance notes rather than formal rejection rules.

### Marine Examples

A ship engineer reviews whether multiple related measurements jointly deviate from the normal operating region, even if no single signal alone is extreme.

This is a conceptual example only and does not claim validation.

### Lifecycle Considerations

Geometry evidence is reference-distribution dependent.

Baseline transition may be required when equipment condition, configuration, or operating regime changes.

### Representative Prototype

Mahalanobis Distance.

---

## 4. Relationship Between Philosophies

These philosophies are complementary rather than competitive.

```text
Evidence

↓

Multiple Information Organization Philosophies

↓

Evidence Committee

↓

Engineering Judgment
```

Evidence Committee should maximize philosophy diversity rather than algorithm quantity.

---

## 5. Reserved Future Philosophies

Reserved future philosophies preserve extensibility.

They are not implemented in the current project.

### Physics Philosophy

Expected Information Organization

```text
Physical consistency
Constraint satisfaction
Energy conservation
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

### Representation Philosophy

Expected Information Organization

```text
Learned latent representation
Compressed operating state
Representation-level deviation
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

### Structural Philosophy

Expected Information Organization

```text
System structure
Subsystem relationship
Causal or dependency pattern
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

### Bayesian Philosophy

Expected Information Organization

```text
Belief state
Uncertainty update
Evidence likelihood
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

### World Model Philosophy

Expected Information Organization

```text
Predicted system evolution
Counterfactual operating state
State transition consistency
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

### Committee Philosophy

Expected Information Organization

```text
Evidence fusion
Consensus formation
Conflict management
```

Reason Deferred

```text
Requires future experimental validation.
Not implemented in the current project.
```

---

## 6. Taxonomy Boundary

This taxonomy is:

* Classification of evidence philosophies.
* Framework organization.
* Engineering communication.
* Committee design foundation.

This taxonomy is not:

* Algorithm ranking.
* Performance benchmark.
* Model selection guide.
* Deployment recommendation.
* Research novelty claim.

---

## 7. Relationship to Existing Documents

This taxonomy relates to the current documentation system as follows:

* Health Evidence Framework defines system organization.
* Decision Documents define frozen engineering principles.
* Research Logs capture exploratory thinking.
* Taxonomy classifies evidence philosophies.
* H5 Summary documents experimental findings.

These documents serve complementary purposes.

The taxonomy should be used as the conceptual reference for future Evidence Committee design and future prototype classification within the Health Evidence Toolkit.
