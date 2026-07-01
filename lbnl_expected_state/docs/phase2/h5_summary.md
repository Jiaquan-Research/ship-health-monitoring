# H5 — Health Evidence Prototype Benchmark Summary

Status

```text
Frozen
```

Phase

```text
Phase 2
```

---

## 1. Purpose

H5 evaluates engineering philosophies rather than searching for the best algorithm.

Each prototype represents one way of organizing health evidence.

H5 benchmarks evidence construction strategies.

Prototype comparison is intended to identify complementary information rather than algorithm superiority.

> H5 is not an algorithm competition.

It is an engineering comparison of evidence construction strategies.

---

## 2. Implemented Prototypes

| Prototype | Family | Evidence Philosophy | Stateful |
|---|---|---|---|
| Absolute Residual | Magnitude | Instantaneous evidence | No |
| Rolling Mean | Filtering | Temporal smoothing | Yes |
| Rolling MAD | Filtering | Robust temporal smoothing | Yes |
| EWMA | Filtering | Exponential temporal smoothing | Yes |
| CUSUM | Accumulation | Persistent change accumulation | Yes |
| Mahalanobis Distance | Geometry | Multivariate distance | No |

Thermal / Performance Margin was intentionally deferred because the required physical variables were unavailable.

No surrogate variables were introduced.

---

## 3. Major Findings

### Finding 1

### Evidence Philosophy matters more than algorithm name.

Several algorithms produced similar engineering behaviour because they share the same underlying information organization philosophy.

Examples:

* Rolling Mean
* Rolling MAD
* EWMA

These represent different filtering mechanisms rather than independent evidence sources.

The engineering question is therefore not only which algorithm is used, but what kind of evidence organization the algorithm represents.

### Finding 2

### Four engineering evidence philosophies emerged.

#### Magnitude

* Core information organization principle: current deviation magnitude is treated as evidence.
* Most sensitive to: instantaneous abnormal deviation from expected behaviour.
* Strengths and limitations: highly interpretable and simple, but may remain condition-sensitive.
* Potential Marine PHM applications: first-level deviation monitoring and transparent onboard evidence display.

#### Filtering

* Core information organization principle: local temporal smoothing suppresses short-term noise.
* Most sensitive to: persistent deviation over a local time window.
* Strengths and limitations: improves temporal stability, but related filtering methods may provide overlapping evidence.
* Potential Marine PHM applications: voyage trend review, watchkeeping support, and slow-change monitoring.

#### Accumulation

* Core information organization principle: small persistent deviations become meaningful through accumulated evidence.
* Most sensitive to: sustained weak changes that may not be obvious instantaneously.
* Strengths and limitations: can preserve long-term evidence, but requires explicit lifecycle management and reset policy.
* Potential Marine PHM applications: long-duration degradation monitoring where maintenance state is tracked.

#### Geometry

* Core information organization principle: health evidence is represented as distance from a learned normal evidence space.
* Most sensitive to: multivariate pattern changes rather than single-channel magnitude alone.
* Strengths and limitations: can reduce simple condition dependence and provide complementary information, but baseline quality matters.
* Potential Marine PHM applications: multi-sensor auxiliary system monitoring where stable baseline evidence is available.

### Finding 3

### Condition robustness differs significantly across evidence philosophies.

The H5B benchmark report documented different levels of condition dependence across prototypes.

Benchmark observations include:

* Mahalanobis substantially reduced condition dependence.
* Filtering methods mainly improved temporal stability.
* Absolute Residual remained highly condition-sensitive.

This indicates that evidence philosophy affects robustness to operating-condition influence.

### Finding 4

### CUSUM validates lifecycle architecture.

CUSUM continuously accumulates evidence.

Without maintenance reset, historical accumulation dominates future outputs.

Therefore, DD-005 Reset Compatibility is experimentally justified.

This validates the lifecycle architecture, not algorithm superiority.

### Finding 5

### Engineering philosophy is more important than prototype quantity.

H5 demonstrates that multiple algorithms may belong to the same evidence philosophy.

Future committee construction should therefore prioritize complementary information rather than maximizing algorithm count.

This finding provides the conceptual foundation for H5C.

---

## 4. What H5 Did Not Solve

H5 did not solve:

* Committee construction
* Committee weighting
* Evidence conflict resolution
* Maintenance state transition
* Marine engineering validation
* Cross-domain validation
* Ground-truth degradation validation

These remain future work.

---

## 5. Inputs to H5C

H5 provides the following inputs to H5C:

* Evidence Philosophy taxonomy
* Representative prototype selection
* Complementary information
* Lifecycle compatibility
* Condition robustness

```text
H5 does not recommend selecting the highest-performing prototype.

Instead,

H5 identifies representative evidence philosophies

that provide complementary information

for future committee construction.
```

H5C should use H5 as a conceptual and evidential basis, not as a final Health Indicator selection.

This document does not define H5C implementation.

---

## 6. Engineering Contributions

H5 contributes:

* Prototype benchmark framework
* Evidence philosophy taxonomy
* Reset Compatibility validation
* Relative condition robustness comparison
* Reusable prototype benchmark methodology

Experimental evidence showed that residual dispersion remained condition-dependent after normalization in the LBNL validation dataset.

The current literature survey found limited explicit discussion of this phenomenon in comparable HVAC health-monitoring pipelines.

Further validation across additional datasets is required before broader generalization.

This wording is intentionally conservative.

H5 does not claim universal novelty.

---

## 7. Limitations

H5 limitations:

* LBNL is a pipeline validation dataset.
* No natural degradation is present.
* No maintenance events are present.
* No committee implementation was performed.
* No cross-domain validation was performed.
* No production deployment was performed.
* No final Health Indicator selection was made.

---

## 8. Key Conclusions

1. Evidence philosophy is a stronger organizing principle than algorithm labels.

2. Filtering methods belong to one engineering family and should not be treated as fully independent evidence sources by default.

3. CUSUM demonstrates the necessity of lifecycle management for stateful evidence.

4. Mahalanobis contributes complementary geometric information.

5. Absolute Residual remains useful as a transparent baseline but is strongly condition-sensitive.

6. No single prototype is universally optimal.

7. H5 provides benchmark evidence rather than final HI selection.

8. H5 establishes the engineering foundation for committee design.

9. H5C is the logical continuation of H5.

10. Future Marine PHM validation remains necessary before broad engineering generalization.

---

## Bridge to Next Stage

```text
H5 Prototype Benchmark

↓

H5C Evidence Committee

↓

Future Marine PHM Framework
```

H5 summarizes the evidence construction layer.

H5C will determine how complementary evidence philosophies may be combined without treating algorithm count as engineering value.
