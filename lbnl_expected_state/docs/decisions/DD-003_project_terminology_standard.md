# DD-003 — Project Terminology Standardization

## Purpose

This Design Decision freezes the engineering vocabulary used throughout the project.

This terminology shall be used consistently across:

* documents
* experiments
* reviewer assessments
* Deep Research
* future publications

## Section 1 — Residual Terminology

| Preferred Term | Deprecated Expression | Definition |
|---|---|---|
| Residual Expectation | Residual Mean | Central tendency of residual conditioned on operating variables |
| Residual Dispersion | Residual Variance | Spread of residual distribution under an operating condition, including variance, IQR, MAD, or equivalent dispersion measure |

## Section 2 — Evidence Terminology

### Statistical Validity

Evaluation of whether the residual is statistically reliable for interpretation, including prediction quality, bias, leakage, and engineering prediction error.

### Semantic Admissibility

Evaluation of whether residual behaviour can reasonably support engineering health interpretation under the observed operating context.

### Candidate Health Evidence

Residual behaviour that has satisfied both Statistical Validity and Semantic Admissibility, but has not been confirmed as degradation by ground truth.

### Condition Evidence

Residual behaviour that primarily reflects operating-condition variation rather than equipment health.

### Mixed Evidence

Residual behaviour where health influence and operating-condition influence cannot currently be separated using available evidence.

### Potential Health Evidence

Residual behaviour that may support health interpretation but has not yet completed all required validation layers.

### Semantic Mask

An evidence-selection boundary used to exclude residual regions that are not semantically admissible for health interpretation.

### Memoryless Health Indicator

A Health Indicator whose output depends only on the current observation and contains no accumulated historical state.

### Stateful Health Indicator

A Health Indicator whose output depends on accumulated historical information and therefore requires explicit lifecycle management.

Classification depends on implementation rather than algorithm family.

### Memoryless Evidence (Type A)

Evidence whose output depends only on the current observation.

No historical state is retained.

Naturally reset-compatible.

### Stateful Evidence (Type B)

Evidence whose output depends on accumulated historical information.

Requires explicit lifecycle management.

May require maintenance-triggered reset depending on engineering judgment.

### Reset Compatibility

The ability of an HI algorithm to explicitly define how maintenance events affect its internal state and historical evidence.

## Section 3 — Operating Context

### Operating Regime

A region of operating behaviour represented by a coherent combination of load, environmental condition, flow, setpoints, and other condition variables.

### Operating Boundary

A boundary where the current operating condition approaches or exceeds the region represented by the validated Expected State evidence.

### Transition Region

An operating period where the system is moving between regimes, including startup, shutdown, control transition, or other non-steady behaviour.

### Steady Operating Window

An operating period where condition variables remain sufficiently stable for residual behaviour to be considered for semantic health interpretation.

## Section 4 — Project Architecture

The project pipeline is frozen as:

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

This terminology shall be used consistently throughout the project.

Physics Layer is validated statistically.

Engineering Layer is validated through engineering interpretation and controlled experiments.

Decision Layer requires operational stakeholder consensus.

## Section 5 — Usage Rules

* Use Residual Expectation instead of Residual Mean.
* Use Residual Dispersion instead of Residual Variance unless statistical variance is explicitly intended.
* Do not describe residuals directly as Health Evidence before Semantic Admissibility has been established.
* Reserve Potential Health Evidence for engineering interpretation without degradation ground truth.
* Use Candidate Health Evidence only after both Statistical Validity and Semantic Admissibility have been satisfied.
