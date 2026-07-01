# DD-006

Title

```text
Evidence Diversity Principle
```

Status

```text
Frozen Engineering Decision
```

Decision Date

```text
2026-06-30
```

---

## 1. Background

H5B evaluated multiple Health Evidence prototypes.

Although six prototypes were implemented, engineering analysis revealed that several mathematically different implementations actually shared the same underlying information organization philosophy.

Examples:

```text
Rolling Mean

Rolling MAD

EWMA
```

These algorithms differ mathematically, but organize engineering information using the same temporal filtering philosophy.

Therefore, algorithm diversity and evidence diversity are not equivalent.

This observation motivated the creation of DD-006.

---

## 2. Decision

The following engineering principles are frozen.

### Decision D6-1

Committee diversity shall be measured by:

> **Evidence Philosophy Diversity**

rather than:

> **Algorithm Quantity**

Evidence Philosophy Diversity refers to diversity in information organization mechanisms rather than diversity in mathematical implementations.

### Decision D6-2

Multiple implementations belonging to the same Evidence Philosophy should normally contribute only one representative to an Evidence Committee.

Example:

```text
Filtering Philosophy

Rolling Mean

Rolling MAD

EWMA

↓

One representative.
```

#### Exception

Multiple representatives from the same Evidence Philosophy may be included only if experimental evidence demonstrates that they provide complementary engineering information.

Such exceptions require:

* explicit Reviewer justification,
* documented experimental evidence,
* and permanent documentation of the rationale.

This exception is expected to be uncommon.

### Decision D6-3

Committee construction should prioritize complementary engineering viewpoints.

Examples:

```text
Magnitude

Filtering

Accumulation

Geometry
```

Each philosophy represents a distinct way of organizing Health Evidence.

### Decision D6-4

Committee membership shall be justified by conceptual complementarity rather than benchmark superiority.

Committee members are selected because they contribute different engineering evidence, not because they achieve the highest numerical performance.

---

## 3. Engineering Rationale

DD-006 is necessary because adding more algorithms does not automatically add more engineering evidence.

Multiple highly correlated evidence sources usually contribute limited engineering value.

Committee diversity should therefore maximize complementary information organization mechanisms.

This supports:

* Information redundancy control
* Engineering interpretability
* Committee robustness
* Lifecycle diversity
* Cross-domain portability

If committee members represent distinct Evidence Philosophies, engineering reviewers can understand why each member exists and what type of evidence it contributes.

If committee members differ only by implementation detail, the committee may become larger without becoming more informative.

---

## 4. Relationship to Evidence Philosophy Taxonomy

Evidence Philosophy Taxonomy answers:

> What philosophy does this prototype belong to?

DD-006 answers:

> How should committee members be selected?

These documents serve complementary purposes.

The Taxonomy classifies.

DD-006 governs committee construction.

---

## 5. Scope

DD-006 applies to:

* Future Evidence Committee construction
* Prototype selection
* Toolkit development
* Cross-domain reuse

DD-006 does not apply to:

* Prototype benchmarking
* Algorithm comparison
* Hyperparameter optimization
* Experimental exploration

---

## 6. Known Limitations

The current Evidence Philosophy Taxonomy contains only four experimentally supported philosophies.

Future philosophies may be added later, including:

* Physics Philosophy
* Representation Philosophy
* Structural Philosophy
* Bayesian Philosophy
* World Model Philosophy

DD-006 remains valid regardless of future taxonomy expansion.

The decision governs how diversity is interpreted, not which philosophies exist in a given taxonomy version.

---

## 7. Deferred Questions

The following topics are intentionally unresolved:

* Committee vote aggregation
* Committee weighting
* Confidence estimation
* Evidence conflict resolution
* Adaptive committee construction
* Dynamic committee selection

These topics are reserved for future framework development.

---

## 8. Relationship to Existing Decisions

DD-006 relates to:

* DD-002 — Residual Evidence Hierarchy
* DD-003 — Terminology Standard
* DD-004 — Semantic Window Validation
* DD-005 — Maintenance Lifecycle / Reset Compatibility

DD-006 extends the framework by defining diversity at the committee level.

---

## 9. Supporting Experimental Evidence

Supporting evidence references:

* H4B
* H5B
* Evidence Philosophy Taxonomy
* Health Evidence Framework

Evidence chain:

H4B demonstrated that operating-condition dependence should first be reduced before meaningful evidence comparison becomes possible.

> Committee diversity over condition-contaminated evidence provides limited engineering value.

H5B subsequently demonstrated that, once evidence becomes sufficiently comparable, multiple mathematically different prototypes naturally organize into a small number of distinct Evidence Philosophies.

DD-006 freezes this engineering interpretation.

This section does not include benchmark numbers and does not duplicate H4B or H5B reports.

---

## 10. Consequences

Expected engineering impact:

* Future Committee design becomes philosophy-driven.
* Algorithm duplication is discouraged.
* Cross-domain portability is improved.
* Framework consistency is strengthened.
* Committee design becomes easier to explain to engineering reviewers.
* Future prototype expansion becomes taxonomy-based rather than benchmark-based.

DD-006 is a framework-level engineering decision.

It remains valid even as new Evidence Philosophies are added in future versions of the framework.
