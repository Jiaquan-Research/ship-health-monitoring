# Condition Variable Selection Protocol

Status

Frozen decision standard for Task C2.

Purpose

Define how variables are evaluated for eligibility to enter the Condition Space.

This document does not select Condition Variables.

Engineering semantics always precede statistical evidence.

---

## Decision Flow

```text
Phase A

Eligibility Screening

->

Phase B

Representative Selection

->

Condition Variables v1
```

Every variable must be evaluated through this protocol during Task C2.

Failure at any Phase A rule terminates evaluation for that variable.

Pending variables shall not enter Condition Variables v1.

---

## Phase A - Eligibility Screening

### Rule 1

Question

Does the variable describe Operating Condition rather than Equipment Health?

Evidence

Engineering semantics.

Decision

Continue / Reject.

---

### Rule 2

Question

Is the variable the Prediction Target?

Evidence

Experiment specification.

Decision

Reject.

Reason Code

TARGET

---

### Rule 3

Question

Is the variable a Derived Variable?

Examples

* COP
* Efficiency
* Delta-T

Evidence

Engineering taxonomy.

Decision

Reject.

Reason Code

DERIVED

---

### Rule 4

Question

Can this variable encode equipment health information?

Typical examples

* Controller Outputs

Principle

Controller Outputs are rejected by default.

Acceptance requires positive evidence that the signal primarily reflects operating condition rather than equipment-health compensation.

Evidence

Engineering control principles.

Decision

Reject / Accept.

Reason Code

HEALTH_LEAKAGE

---

### Rule 5

Question

Does the variable provide statistical contribution?

Engineering review must be completed before statistical review.

Statistical evidence includes:

* unique value count
* occupancy
* Task B audit results

Example

Variables identified as statistical constants may be rejected.

Decision

Accept / Reject / Pending.

Reason Codes

* CONSTANT
* INSUFFICIENT_EVIDENCE
* TIME_INDEX

Notes

Equipment Status variables not identified as constants during Task B shall be re-evaluated during Task C2 before a final decision.

---

## Phase B - Representative Selection

Variables that pass Phase A enter redundancy evaluation.

### Rule 6

Question

Does this variable belong to a group representing the same physical quantity?

Engineering grouping precedes statistical correlation.

Examples

* Multiple condenser water flow measurements.

Decision

Representative / Standby.

Reason Codes

* REDUNDANT_STANDBY
* REDUNDANT_REJECTED

Engineering grouping shall be established before any correlation analysis.

Correlation supports representative selection only.

It never defines engineering grouping.

---

### Rule 7

Question

Is sufficient evidence available to finalize the decision?

Decision

Accept / Reject / Pending.

Evidence

Combined engineering review and statistical evidence.

Constraint

Pending variables shall **not** enter Condition Variables v1.

Every Pending variable must be resolved before Expected State construction begins.

Before Task C2 closes, each Pending variable must be promoted to Accept or downgraded to Reject.

No Pending status is allowed to propagate beyond Task C.

---

## Decision Table

The following table is mandatory for Task C2.

Every evaluated variable must be recorded.

| Variable | Decision | Evidence | Reason Code |
| -------- | -------- | -------- | ----------- |
|          |          |          |             |

This table becomes the authoritative traceability record for Condition Variables v1.

---

## Decision Table Examples

The following rows illustrate format only. They are not Condition Variable selections.

| Variable | Decision | Evidence | Reason Code |
| -------- | -------- | -------- | ----------- |
| OA_TEMP | Accept | Environment | CONDITION |
| CWL_SEC_LOAD | Accept | Demand | CONDITION |
| CHL_POW_1 | Reject | Prediction Target | TARGET |
| CHL_STA_1 | Reject | Task B Constant Audit | CONSTANT |
| CT_FAN_SPD_CTRL_1 | Reject | Engineering Review | HEALTH_LEAKAGE |

---

## Reason Code Definitions

CONDITION

Variable passed eligibility review as an operating condition descriptor.

TARGET

Variable is the prediction target and cannot enter the Condition Space.

DERIVED

Variable is calculated from other measurements and is excluded from Condition Variables v1.

HEALTH_LEAKAGE

Variable may encode equipment-health information or controller compensation.

CONSTANT

Variable is identified as statistically constant or otherwise non-contributory by approved audit evidence.

INSUFFICIENT_EVIDENCE

Available evidence is not sufficient to finalize Accept or Reject during review.

TIME_INDEX

The variable is metadata describing temporal ordering.

It is not a physical operating-condition variable.

Therefore it is ineligible for the Condition Space.

Typical examples

* Datetime
* Timestamp
* Sample ID
* Sequence Number

REDUNDANT_STANDBY

Variable belongs to a same-quantity group and is retained as standby rather than representative.

REDUNDANT_REJECTED

Variable belongs to a same-quantity group and is rejected because a representative is selected.

Reason Code Dictionary

The Reason Code definitions contained in this protocol are authoritative.

Experimental documents may only reference Reason Codes defined here.

No new Reason Codes may be introduced outside this protocol.

---

## Evidence Traceability Specification

Every variable decision must include:

* variable name
* final decision
* evidence source
* reason code

Allowed decisions:

* Accept
* Reject
* Pending
* Representative
* Standby

Allowed evidence sources include:

* Engineering taxonomy
* Experiment specification
* Task B Data Quality Audit
* Engineering control principles
* Task C2 statistical review
* Task C2 redundancy review

No variable may enter Condition Variables v1 unless it has a recorded Accept or Representative decision with supporting evidence.

No Pending variable may enter Expected State construction.

Task C2 shall execute this protocol without introducing additional selection criteria.
