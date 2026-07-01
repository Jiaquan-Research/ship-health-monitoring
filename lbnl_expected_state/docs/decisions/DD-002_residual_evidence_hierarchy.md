# DD-002 — Residual Evidence Hierarchy

## Purpose

This Design Decision establishes how residuals are interpreted throughout the project.

It applies to:

* LBNL
* Marine Validation
* Future datasets
* Future Expected State models

The purpose is to prevent direct interpretation of residuals as health evidence before both statistical and semantic validation layers have been addressed.

## Background

The project progression is:

```text
Expected State
↓
Residual
↓
Phase 1
Bias Audit
Leakage Audit
↓
Residual passes Statistical Validation
↓
Phase 2 H2/H3
↓
Residual may still contain
operating-condition effects
↓
Need Semantic Admissibility
before HI construction
```

Phase 1 established that residuals can be statistically valid within the evaluated operating regime.

H2 and H3 established that statistically valid residuals may still require semantic screening before they can support health interpretation.

## Decision

The following three-layer engineering hierarchy is frozen:

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

Residuals shall not be interpreted directly as Health Evidence.

Health Indicators shall be constructed only from Candidate Health Evidence.

Physics Layer is validated statistically.

Engineering Layer is validated through engineering interpretation and controlled experiments.

Decision Layer requires operational stakeholder consensus.

## Definition 1

### Residual Statistical Validity

Residual Statistical Validity is the evaluation of statistical reliability.

Typical questions include:

* bias
* leakage
* prediction quality
* engineering prediction error

Statistical Validity answers:

> Can the residual be trusted statistically?

It does not establish health meaning.

## Definition 2

### Residual Semantic Admissibility

Residual Semantic Admissibility is the evaluation of engineering interpretability.

Typical questions include:

* operating-condition dominance
* startup
* shutdown
* controller transition
* model uncertainty
* operating boundaries

Semantic Admissibility answers:

> Can this residual reasonably support health interpretation?

It does not prove degradation.

## Candidate Health Evidence

Candidate Health Evidence represents residual behaviour satisfying both:

* Statistical Validity
* Semantic Admissibility

Candidate Health Evidence is not equivalent to confirmed degradation.

Ground-truth degradation remains necessary for validation.

## Engineering Implications

The conceptual workflow changes from:

```text
Residual

↓

Health Indicator
```

to:

```text
Residual

↓

Statistical Validity

↓

Semantic Admissibility

↓

Candidate Health Evidence

↓

Health Indicator
```

Masking is an evidence-selection operation rather than data cleaning.

Conditioning may improve Semantic Admissibility but does not itself establish health meaning.

## Scope

DD-002 applies independently of prediction algorithm.

Examples include:

* XGBoost
* Random Forest
* VIB
* Transformer
* Future methods

The hierarchy applies to the interpretation of residuals, not to any specific model class.

## Limitations

DD-002 does not define:

* masking implementation
* semantic metrics
* HI construction
* degradation validation

These remain separate design and validation tasks.

## References

Phase 1:

* Bias Audit
* Leakage Audit
* Scientific Review

Phase 2:

* H0
* H1
* H2
* H3

## Decision Summary

The following project principles are frozen:

> Residuals are statistical observations, not Health Evidence.

> Health Indicators shall be constructed only from residual information satisfying both Statistical Validity and Semantic Admissibility.

> Semantic Admissibility shall be evaluated using both Residual Expectation and Residual Dispersion, as both may contain operating-condition-dependent information.

## Validation Status

Originally accepted as a conceptual engineering principle.

Following H4B, DD-002 is upgraded to:

```text
Experimentally Supported
```

within the following scope:

Semantic Admissibility demonstrably reduces operating-condition dependence of residual-derived Candidate Health Indicators.

Validation of degradation-related evidence remains future work.
