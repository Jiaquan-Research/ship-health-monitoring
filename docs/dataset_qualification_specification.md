# Dataset Qualification Specification

Version:

```text
v1.1
```

Governance Status:

```text
Framework Freeze v1.1 Governance Document
```

Purpose: define the minimum dataset requirements before a dataset enters the Health Evidence Framework validation process.

This specification determines suitability for validation. It does not judge the scientific quality, industrial value, or ultimate research usefulness of a dataset.

## Purpose

Dataset Qualification establishes whether a dataset can support a specific framework validation task.

Qualification answers:

> Can this dataset support the intended validation question within clearly stated boundaries?

It does not answer:

> Is this dataset scientifically superior?

or

> Does this dataset validate the framework for all domains?

## Data Audit and Dataset Qualification

Data Audit and Dataset Qualification are separate governance activities.

Data Audit answers:

> What does this dataset contain?

Dataset Qualification answers:

> Is this dataset eligible for Framework Validation?

Data Audit describes observable dataset properties such as rows, columns, timestamps, missing values, duplicated records, data types, and descriptive summaries.

Dataset Qualification uses audit evidence, dataset metadata, and validation-scope requirements to determine whether the dataset may enter a specific framework validation task.

The Dataset Qualification Record is the formal governance artifact connecting audit evidence to an onboarding decision.

### Cross-dataset Onboarding Requirements

In this specification, cross-dataset onboarding requirements mean the dataset-qualification requirements defined here for any dataset seeking entry into Framework Validation.

The term does not add a separate governance layer.

When the Validation Roadmap refers to cross-dataset onboarding requirements, it refers to:

- the minimum dataset requirements in this specification;
- the qualification decision rules in this specification;
- the completed Dataset Qualification Record for the dataset under review.

## Minimum Dataset Requirements

A dataset shall document, at minimum:

- dataset name;
- domain and asset type;
- data source;
- real, simulation, or test-rig status;
- timestamp or sample-order information;
- available sensor variables;
- target or reference variables, if applicable;
- operating-condition variables, if applicable;
- sampling interval or sampling irregularity;
- known train/test or temporal boundary constraints;
- missing-value status;
- duplicate-record status;
- maintenance-event annotation status;
- degradation or fault-label status;
- operating-envelope coverage;
- known licensing or access constraints;
- current project usage boundary.

If any requirement is unavailable, the dataset may still be reviewed, but the missing item shall be recorded as a qualification limitation.

## Recommended Dataset Characteristics

Recommended characteristics include:

- continuous timestamped operation;
- interpretable engineering variables;
- known operating-condition coverage;
- sufficiently documented sensor semantics;
- maintenance-event records when lifecycle behaviour is evaluated;
- degradation or fault labels when degradation validation is claimed;
- stable access path and reproducible loading method;
- clear separation between raw data and generated artifacts.

These characteristics are recommended, not mandatory for every validation task.

## Dataset Qualification Levels

### Qualified

The dataset satisfies the minimum requirements for the intended validation task.

Known limitations are documented and do not block the stated validation objective.

### Qualified with Conditions

The dataset can support the intended validation task only within explicit boundaries.

Examples:

- degradation labels are unavailable;
- maintenance records are unavailable;
- operating coverage is limited;
- signal semantics require manual review;
- validation is restricted to one operating regime.

### Not Qualified

The dataset cannot support the intended validation task.

Examples:

- required variables are unavailable;
- timestamp or sample order is not recoverable;
- operating-condition context is missing for a Condition Normalization task;
- degradation validation is requested but no degradation evidence exists;
- licensing or access prevents reproducible review.

## Qualification Decision Rules

### Audit Verdict Rules

Audit findings shall be converted into one of three audit verdicts.

#### PASS

The dataset satisfies the mandatory requirements for the intended validation task.

No blocking qualification limitation is present.

#### WARNING

The dataset satisfies the mandatory requirements for the intended validation task, but one or more documented limitations restrict how the dataset may be used.

The warning must be reproducible from the recorded audit evidence.

#### FAIL

The dataset does not satisfy one or more mandatory requirements for the intended validation task.

Dataset onboarding is prohibited for that validation task.

### Qualification Decision Rules

Audit Verdict:

PASS

Qualification:

Qualified

Audit Verdict:

WARNING

Qualification:

Qualified with Conditions

Audit Verdict:

FAIL

Qualification:

Not Qualified

### Decision Semantics

Qualified means all mandatory requirements for the intended validation task are satisfied.

Qualified with Conditions means the dataset can support the intended validation task only within explicit boundaries.

Not Qualified means the dataset cannot support the intended validation task.

The qualification record shall state the audit verdict, qualification decision, required conditions, unsupported claims, and validation boundaries.

### Operating Envelope Rule

Constant configuration or status variables indicate a restricted operating envelope when they materially reduce the variety of operating states represented in the dataset.

When this condition is observed and the dataset otherwise satisfies the mandatory requirements for the intended validation task:

1. The audit verdict shall be WARNING.
2. The qualification decision shall be Qualified with Conditions.
3. The qualification record shall document the restricted operating envelope as a limitation.

This rule is intended to be reproducible from the audit evidence and the recorded operating-envelope interpretation.

## Typical Examples

### LBNL Chiller Plant

Qualification Status:

Qualified with Conditions.

Current Role:

Pipeline validation dataset for Expected State, residual validation, Semantic Admissibility, Semantic Window validation, and Evidence Prototype benchmarking.

Known Conditions:

- no confirmed degradation labels;
- no maintenance-event annotations;
- not direct validation for marine systems.

### CODLAG

Qualification Status:

Pending Verification.

Current Role:

Potential future marine propulsion validation dataset.

Known Conditions:

- data availability requires verification;
- signal semantics require verification;
- degradation or maintenance evidence requires verification.

### C-MAPSS

Qualification Status:

Pending Verification.

Current Role:

Potential prognostics benchmark reference.

Known Conditions:

- simulation dataset;
- suitability for the current Health Evidence Framework requires review;
- operating-condition assumptions differ from LBNL validation.

### PRONOSTIA

Qualification Status:

Pending Verification.

Current Role:

Potential cross-domain degradation trajectory validation candidate.

Known Conditions:

- bearing test-rig data;
- run-to-failure behaviour differs from continuous operating-condition validation;
- framework-specific suitability requires separate review.

## Qualification Record

Each dataset qualification should record:

- dataset name;
- intended validation task;
- qualification level;
- audit verdict;
- evidence supporting qualification;
- known limitations;
- reviewer decision;
- reviewer conditions, if any;
- operating-envelope interpretation;
- cross-dataset onboarding requirements reference.

## Boundary

Dataset qualification governs entry into framework validation.

It does not establish:

- final framework validity;
- cross-domain generalization;
- marine applicability;
- degradation detection success;
- production deployment readiness.
