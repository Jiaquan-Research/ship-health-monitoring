# Gate M2 — Phase 2 Milestone Review

## Residual Evidence Framework Freeze

## Section 1

### Purpose

Gate M2 freezes the Residual Evidence Framework established during Phase 2.

It does not summarize experiments.

It answers four scientific questions and one gate-readiness question.

Its purpose is to determine whether H4 may begin.

## Section 2

### Gate Structure

```text
Gate M1
Phase 1 Freeze
(Expected State Validation)

        ↓

Gate M2   ← Current
Residual Evidence Framework Freeze

        ↓

Gate M3
Health Indicator Framework Freeze

        ↓

Gate M4
Marine Validation Ready

        ↓

Gate M5
Decision Support Ready
```

## Section 3

### Q1 — Has the Residual satisfied Statistical Validity?

Answer:

```text
PASS
```

Evidence:

| Task | Result |
|---|---|
| Bias Audit | Residual bias acceptably small within the Train operating regime across all audited Condition Variables. |
| Leakage Audit | Train nonlinear leakage generally below screening threshold |
| Scientific Review | PASS WITH CONDITIONS |

Statistical Validity is confirmed only within the validated Train operating regime.

Statistical Validity establishes statistical reliability only.

It does not imply engineering interpretability or health relevance.

Operating-Regime Robustness remains future work.

## Section 4

### Q2 — Has the Residual Evidence Framework been established?

Answer:

```text
PASS WITH CONDITIONS
```

Framework:

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

Health Indicator

Decision Layer
-----------------------

Health Assessment

↓

Maintenance Recommendation
```

Physics Layer is validated statistically.

Engineering Layer is validated through engineering interpretation and controlled experiments.

Decision Layer requires operational stakeholder consensus.

H2/H3 findings:

* Residual Expectation exhibits minimal condition dependence.
* Residual Dispersion remains condition-dependent.
* Candidate B/C temporal persistence is largely explained by seasonal operating-condition variation.
* Near-zero load and operating-boundary regions are currently interpreted primarily as Condition Evidence based on the available engineering evidence.

Clarification:

> This conclusion applies to Residual Expectation only. Residual Dispersion remains condition-dependent and therefore requires separate Semantic Admissibility evaluation.

Conditions:

1. No degradation ground truth exists in the LBNL dataset.
2. Candidate Health Evidence remains an engineering interpretation.
3. Semantic Admissibility has not yet been experimentally validated.

## Section 5

### Q3 — What is the current primary unresolved scientific problem?

Answer:

```text
Health Evidence Isolation
```

The project has identified where Candidate Health Evidence may exist.

It has not yet demonstrated that isolating Candidate Health Evidence improves Health Indicator quality.

Formal hypothesis:

```text
H4-H1
```

Definition:

> Applying Semantic Admissibility as an operating-window filter measurably improves the engineering quality of residual-derived Health Indicators.

Null Hypothesis:

```text
H4-H0
```

Definition:

> Applying Semantic Admissibility as an operating-window filter does not measurably improve the engineering quality of residual-derived Health Indicators.

If H4-H1 is rejected, DD-002 remains a conceptually valid but empirically unvalidated engineering principle.

If H4-H1 is supported, DD-002 becomes an experimentally supported engineering principle.

## Section 6

### Q4 — May Phase 2 proceed to H4?

Answer:

```text
PASS WITH CONDITIONS
```

Conditions:

1. H4 validates Semantic Admissibility rather than constructing the final HI.
2. Compare Candidate C under:

   * Full timeline
   * Semantic-Admissible Window

3. Do not introduce:

   * CUSUM
   * EWMA
   * Mahalanobis
   * PCA
   * Autoencoder

4. Do not discuss:

   * RUL
   * Risk
   * Decision Support

5. Produce reviewable experimental evidence supporting or refuting H4-H1.

## Section 7

### Project Maturity Assessment

| Layer | Status | Gate |
|---|---|---|
| Expected State Construction | Mature | M1 |
| Residual Statistical Validity | Mature | M1 |
| Residual Semantic Admissibility | Concept Frozen | M2 |
| Health Evidence Isolation | Next Experiment | H4 |
| Health Indicator Construction | Not Started | H5 |
| Health Assessment | Not Started | Future |
| Marine Validation | Pending Data | M4 |

## Section 8

### Frozen Concepts and Terminology

The following terminology is frozen by DD-002 and DD-003.

### Residual Statistical Validity

Evaluation of whether the residual is statistically reliable for interpretation, including prediction quality, bias, leakage, and engineering prediction error.

### Residual Semantic Admissibility

Evaluation of whether residual behaviour can reasonably support engineering health interpretation under the observed operating context.

### Candidate Health Evidence

Residual behaviour satisfying both Statistical Validity and Semantic Admissibility, without claiming confirmed degradation.

### Residual Expectation

Central tendency of residual conditioned on operating variables.

### Residual Dispersion

Spread of residual distribution under an operating condition, including variance, IQR, MAD, or equivalent dispersion measure.

### Condition Evidence

Residual behaviour that primarily reflects operating-condition variation rather than equipment health.

### Mixed Evidence

Residual behaviour where health influence and operating-condition influence cannot currently be separated using available evidence.

### Semantic Mask

An evidence-selection boundary used to exclude residual regions that are not semantically admissible for health interpretation.

No new terminology is introduced by Gate M2.

## Section 9

### Scientific Boundary

Gate M2 does not claim:

* degradation has been detected;
* Semantic Admissibility has been experimentally validated;
* Candidate Health Evidence implies physical degradation;
* Marine applicability has been validated;
* constructed Health Indicators are ready for maintenance decisions.

Cross-domain validation remains future work.

## Section 10

### Recommended Next Stage

```text
H4 — Health Evidence Isolation Validation
```

Scientific hypothesis:

```text
H4-H1

Applying Semantic Admissibility
as an operating-window filter
measurably improves the engineering quality
of residual-derived Health Indicators.
```

Suggested experiment:

```text
Baseline

Full timeline

↓

Candidate C

↓

H1 Evaluation


Semantic-Admissible Window

↓

Candidate C

↓

H1 Evaluation


Comparison

• Temporal Persistence
• Residual Dispersion
• Condition dependence
• H1 Evaluation dimensions
```

Success Criterion:

H4 succeeds if it provides reviewable evidence either supporting or refuting H4-H1.

## Section 11

### Reviewer Sign-off

```text
Q1
Has the Residual satisfied Statistical Validity?

PASS


Q2
Has the Residual Evidence Framework been established?

PASS WITH CONDITIONS


Q3
Primary unresolved scientific problem?

Health Evidence Isolation


Q4
May Phase 2 proceed to H4?

PASS WITH CONDITIONS


Q5
Has Gate M2 frozen all concepts required before experimental validation of Semantic Admissibility?

PASS / REVISE


Reviewer Decision

PASS WITH CONDITIONS

or

REVISE


Reviewer Notes
```
