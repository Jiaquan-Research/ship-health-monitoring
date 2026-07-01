# Method Zoo

Observation Ledger

---

## 1. Purpose

This document records potentially relevant methods.

Goals:

- observation
- curiosity
- tool awareness

Not:

- evidence generation
- architecture design
- method ranking

No method is expected to support Q0.

Failure is acceptable.

---

## 2. Method Zoo Rules

No method is preferred.

Complex methods are not automatically superior.

Simple methods should be exhausted first.

Method selection should follow observations,
not curiosity alone.

Computational cost matters.

A method that requires 10x computation
for 5% gain is not automatically better.

Failure is acceptable.

---

## 3. Classical Methods

Examples:

- PCA
- ICA
- NMF
- Clustering
- HDBSCAN
- UMAP

Notes:

Simple and interpretable.

No recommendation implied.

---

## 4. Statistical Methods

Examples:

- Correlation
- Mutual Information
- Transfer Entropy
- Partial Correlation

Notes:

Useful for relationships and dependencies.

No recommendation implied.

---

## 5. Dynamical Systems

Examples:

- DMD
- Koopman Operator
- SINDy

Notes:

Potentially useful for mode structures.

No recommendation implied.

---

## 6. Machine Learning Approaches

Examples:

- Mixture of Experts
- Switching Systems
- Hidden Markov Models
- Gating Networks

Notes:

Possible tools for piecewise mappings.

No recommendation implied.

---

## 7. Current Status

No method is currently planned.

No method is required.

Methods are recorded for future observation only.

---

## 8. Evidence Status

Current evidence level:

Very low.

Nothing in this document should be used to:

- modify Claim Registry
- modify Concept Paper
- modify engineering architecture

---

## 9. Regime Detection Method Assumptions

Source:

Deep Research: Vocabulary for Multi-Regime Industrial Systems

| Method family | Regime assumption | Number of regimes | Membership | Notes |
|---|---|---|---|---|
| HMM / Markov-switching models | Discrete latent regimes | Usually fixed or selected by model comparison | Latent | Temporal dependence assumed |
| Mixture of Experts | Finite experts with soft gating | Selected beforehand | Soft / latent | Useful as a conceptual reference, not currently recommended |
| Clustering-based identification | Finite partitions or soft clusters, depending on algorithm | May be fixed or inferred, depending on method | Inferred | Assumptions vary strongly by algorithm |
| Change-point detection | Piecewise-stationary segments | May be estimated with penalties | Implicit by segment | Boundary-focused rather than reusable regime-state focused |
| Gaussian Mixture Models | Finite mixture components | Set or selected | Latent via posterior responsibility | No temporal persistence unless extended |

This section records assumptions only.

It does not recommend any method.

It does not change current method priorities.

---

## Version History

v0.1

2026-06-11

Initial method observation ledger created.

No conclusions.
