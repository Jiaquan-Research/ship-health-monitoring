# H5A — Health Indicator Method Taxonomy

## Purpose

This document freezes the engineering taxonomy of Health Indicator construction methods.

The taxonomy organizes Health Indicator methods according to their underlying engineering philosophy rather than mathematical implementation.

It answers:

```text
What engineering information is being extracted?
```

rather than:

```text
Which algorithm is used?
```

This document serves as the conceptual foundation for H5B Prototype Benchmark and H5C Committee Design.

## Scope

H5A includes:

* engineering taxonomy;
* family definitions;
* engineering philosophy;
* industrial maturity;
* data requirements;
* lifecycle characteristics;
* marine applicability.

H5A does not include:

* algorithm benchmarking;
* prototype implementation;
* committee design;
* Remaining Useful Life;
* maintenance decision logic;
* performance comparison.

---

## Family A — Instantaneous Evidence

### Engineering Philosophy

Current observation directly represents equipment condition.

### Typical Information

* residual magnitude
* performance deviation
* efficiency loss
* threshold exceedance

### Typical Examples

* Absolute Residual
* Standardized Residual
* Performance Margin

### Characteristics

* Memoryless
* Reset naturally compatible
* High interpretability

### Industrial Maturity

★★★★★

---

## Family B — Trend Evidence

### Engineering Philosophy

Health information is reflected through local temporal evolution.

### Typical Examples

* Rolling Mean
* Rolling Median
* Rolling MAD
* Rolling Standard Deviation

### Characteristics

* Finite memory
* Window-based
* Noise suppression

### Industrial Maturity

★★★★★

---

## Family C — Statistical Accumulation

### Engineering Philosophy

Persistent small deviations become meaningful after accumulation.

### Typical Examples

* CUSUM
* EWMA
* Page-Hinkley

### Characteristics

* Stateful
* Maintenance reset required
* Long-memory behaviour

### Industrial Maturity

★★★★★

### Reference

Consistent with Design Principle H5-R1.

---

## Family D — Distribution Evidence

### Engineering Philosophy

Health information is represented by statistical distribution changes.

### Typical Examples

* Entropy
* Quantile Shift
* Histogram Drift
* KL Divergence

### Characteristics

* Window-based
* Sensitive to structural changes

### Industrial Maturity

★★★★☆

---

## Family E — Distance Evidence

### Engineering Philosophy

Health is represented by distance from the learned normal operating space.

### Typical Examples

* Mahalanobis Distance
* PCA T²
* SPE / Q Statistic

### Characteristics

* Multi-sensor fusion
* Geometry-based

### Industrial Maturity

★★★★★

---

## Family F — Physics-Based Evidence

### Engineering Philosophy

Health is represented by physically meaningful quantities.

### Typical Examples

* Thermal Efficiency
* Heat Balance
* Compressor Efficiency
* Fuel Margin

### Characteristics

* Physics interpretable
* Asset dependent

### Industrial Maturity

★★★★★

---

## Family G — Committee Evidence

### Engineering Philosophy

Engineering confidence is obtained through evidence fusion rather than a single indicator.

### Typical Examples

* Weighted Voting
* Consensus
* Bayesian Fusion
* Hierarchical Evidence

### Characteristics

* Multiple evidence sources
* Reduced false alarms

### Industrial Maturity

★★★★☆

### Note

Committee implementation belongs to H5C.

---

## Comparison Matrix

| Family | Information | Memory | Reset | Expected State | Industrial Maturity |
|---|---|---|---|---|---|
| Family A — Instantaneous Evidence | Current deviation or performance margin | Memoryless | Naturally compatible | Often useful, not universal | ★★★★★ |
| Family B — Trend Evidence | Local temporal evolution | Finite memory | Window restart or warm-up may be required | Often useful, not universal | ★★★★★ |
| Family C — Statistical Accumulation | Persistent small deviations | Stateful | Required | Often useful, not universal | ★★★★★ |
| Family D — Distribution Evidence | Distributional change | Window-based | Window restart or baseline transition may be required | Optional | ★★★★☆ |
| Family E — Distance Evidence | Distance from normal operating space | Baseline dependent | Baseline transition may be required | Optional | ★★★★★ |
| Family F — Physics-Based Evidence | Physically meaningful performance quantity | Implementation dependent | Depends on baseline and physical state definition | Not universal | ★★★★★ |
| Family G — Committee Evidence | Fused engineering confidence | Implementation dependent | Depends on evidence sources | Depends on evidence sources | ★★★★☆ |

---

## Data Requirement Matrix

| Family | Low-frequency Data | Continuous Sensors | Multi-sensor | Labels Required |
|---|---|---|---|---|
| Family A — Instantaneous Evidence | Suitable | Helpful but not mandatory | Not required | No |
| Family B — Trend Evidence | Suitable if sampling is regular enough for the selected window | Helpful | Not required | No |
| Family C — Statistical Accumulation | Suitable if event timing is adequate | Helpful | Not required | No |
| Family D — Distribution Evidence | Limited unless enough samples exist per window | Helpful | Optional | No |
| Family E — Distance Evidence | Possible but data volume may limit baseline quality | Helpful | Usually yes | No for unsupervised baseline distance |
| Family F — Physics-Based Evidence | Suitable if required physical variables are measured | Helpful | Usually yes | No, but physical calibration may be required |
| Family G — Committee Evidence | Depends on included evidence sources | Depends on included evidence sources | Usually helpful | Not inherently required |

---

## Marine Applicability

| Family | Marine Suitability | Engineering Notes |
|---|---|---|
| Family A — Instantaneous Evidence | High | Interpretable and deployable with limited shipboard data; naturally lifecycle compatible. |
| Family B — Trend Evidence | High | Aligns with existing onboard trend review practice; requires careful window documentation. |
| Family C — Statistical Accumulation | Medium to High | Useful for persistent weak evidence, but lifecycle reset policy is mandatory under H5-R1. |
| Family D — Distribution Evidence | Medium | Can detect structural changes but requires enough stable samples per operating window. |
| Family E — Distance Evidence | Medium | Useful for multi-sensor systems; baseline quality and operating regime coverage are critical. |
| Family F — Physics-Based Evidence | High where physics variables are available | Strong engineering meaning; deployability depends on vessel instrumentation and asset model. |
| Family G — Committee Evidence | Medium to High | Useful when multiple evidence streams exist; implementation belongs to H5C. |

Marine suitability is assessed conceptually using interpretability, deployability, lifecycle compatibility, and expected data availability aboard ships.

---

## Engineering Design Principles

### H5-R1

Stateful Health Indicators shall define explicit maintenance reset behaviour.

### H5-R2

Health Indicator methods should be classified by engineering philosophy rather than mathematical implementation.

### H5-R3

Different HI families should be regarded as complementary evidence extraction mechanisms.

### H5-R4

Expected State is an upstream component for some HI families, but not a universal prerequisite.

### H5-R5

Engineering usefulness has higher priority than algorithm novelty.

---

## Health Indicators as Information Compression

Health Indicators are not prediction algorithms.

Instead, they compress high-dimensional operational observations into a small number of maintenance-relevant engineering variables.

Each family performs this compression through a different principle:

* magnitude;
* temporal smoothing;
* accumulation;
* statistical distribution;
* geometric distance;
* physical interpretation;
* evidence fusion.

This conceptual view serves as the foundation for H5B and H5C.

---

## Reviewer Checklist

Confirm:

* Seven engineering families are clearly defined.
* Classification is based on engineering philosophy rather than mathematical implementation.
* Memoryless and Stateful concepts are used consistently with DD-003 and DD-005.
* H5-R1 through H5-R5 are explicitly stated.
* Health Indicators as Information Compression is included as the conceptual summary.
* No prototype benchmarking is introduced.
* No implementation details are discussed.

Reviewer Decision:

```text
PASS / REVISE
```
