# Validation Chain v0.1 (Frozen)

Date: 2026-06-03

Status: Frozen

---

# 1. Purpose

This document records the current validation status of the Ship System Health Monitoring research line.

It is intended to answer:

Can a Health Monitoring pipeline be constructed using:

Condition Variables
-> Expected State Model
-> Residual
-> Health Indicator

for industrial systems?

This document records validated findings only.

Unvalidated assumptions are explicitly marked.

---

# 2. Validation Roadmap

## Validation A

TEP Structure Discovery

Question:

Do performance-degradation faults exhibit stable statistical structure?

Result:

PASS

Status:

Frozen

Conclusion:

Performance-degradation faults can exhibit stable statistical signatures in representation space.

Note:

This validation was conducted on TEP.

No direct claim is made regarding marine systems.

---

## Validation B1

Expected State Model

Dataset:

LBNL Chiller Plant

Question:

Can Condition Variables accurately predict State Variables?

Result:

PASS

Key Results:

CHL_POW_1:
R2 = 0.970

CHL_SW_TEMP_1:
R2 = 0.982

CT_SW_TEMP_1:
R2 = 0.993

CHL_RWCD_TEMP_1:
R2 = 0.984

Conclusion:

Condition Variables contain sufficient information to reconstruct normal system behavior.

Expected State Models are feasible.

---

## Validation B2

Residual vs Severity

Initial Result:

FAIL

Investigation:

Label semantics audit performed.

Finding:

Fault labels were interpreted incorrectly.

Observed ordering:

065
080
095

was assumed to mean:

weak
-> medium
-> strong

Raw process analysis showed the opposite relationship.

Diagnosis:

095 = weakest fouling

080 = medium fouling

065 = strongest fouling

Conclusion:

Validation failure caused by incorrect severity ordering assumption.

Pipeline itself was not invalidated.

---

## Validation B2.1

Residual vs Physical Degradation

Dataset:

LBNL Chiller Plant

Corrected severity order:

Baseline
-> 095
-> 080
-> 065

Result:

STRONG PASS

Key Finding:

All four State Variables showed strict monotonic response.

Metrics:

AbsMean:
4 / 4 monotonic

RMS:
4 / 4 monotonic

P95:
4 / 4 monotonic

Conclusion:

Residual magnitude increases consistently with physical degradation.

Evidence supports:

Expected State
-> Residual
-> Physical Degradation

relationship.

---

# 3. Current Evidence Chain

Validated:

Condition Variables
↓
Expected State Model
↓
Residual
↓
Physical Degradation

Status:

Preliminary Supported

Evidence Source:

HVAC Domain
(LBNL Chiller Plant)

---

# 4. Sensitivity Ranking

Validation B2.1

Most sensitive indicators:

1. CT_SW_TEMP_1
2. CHL_RWCD_TEMP_1
3. CHL_SW_TEMP_1
4. CHL_POW_1

Interpretation:

Cooling-system temperatures respond more strongly than power consumption under cooling tower fouling.

This is physically plausible and consistent with heat-transfer degradation mechanisms.

Note:

This ranking applies to cooling-tower fouling in the HVAC domain. Sensitivity ranking for marine systems (e.g. exhaust temperature vs lube oil pressure) may differ significantly and requires independent validation.

---

# 5. Concept Paper Status

Q1

Can Condition Variables support Condition Normalization and Expected State Modeling?

Status:

Preliminary Supported

Supporting Evidence:

Validation B1

---

Q2

Does Residual contain degradation information?

Status:

Preliminary Supported

Supporting Evidence:

Validation B2.1

---

Q3

Can a Health Indicator be constructed from Residual?

Status:

Not Yet Validated

---

Q4

Can the Health Indicator track long-term degradation trends?

Status:

Not Yet Validated

---

Q5

Can Health Monitoring outputs drive Maintenance Guidance?

Status:

Not Yet Validated

---

# 6. Known Limitations

Limitation 1

All evidence currently comes from HVAC systems.

No marine validation has been completed.

---

Limitation 2

LBNL datasets are fault-injection datasets.

Long-term natural degradation has not yet been validated.

---

Limitation 3

Maintenance-cycle effects have not yet been studied.

Baseline reset logic remains an open problem.

---

Limitation 4

Health Indicator formulation remains undefined.

No frozen HI equation exists.

---

# 7. Research Status

Completed:

- Validation A
- Validation B1
- Validation B2
- Validation B2.1

Current State:

Expected State route validated.

Residual route validated.

Health Indicator research may begin.

---

# 8. Recommended Next Steps

Priority 1

Freeze Validation results.

---

Priority 2

Update Concept Paper.

Reflect Q1 and Q2 status changes.

---

Priority 3

Design HI_v0.

Design only.

No implementation yet.

---

Priority 4

Await marine generator data acquisition.

Begin Validation C once real-world data becomes available.

---

# One-Sentence Summary

As of 2026-06-03, the Expected State -> Residual -> Physical Degradation route has obtained preliminary experimental support in the HVAC domain and is ready to advance to Health Indicator design.
