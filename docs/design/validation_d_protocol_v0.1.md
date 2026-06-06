# Validation D Protocol v0.1

# Marine Generator — Real Data Validation

Date: 2026-06-06
Status: Protocol Ready — Awaiting Data
Scope: Diesel Generator (DG) on teaching vessel

---

## 1. Purpose

Validation D is the first real Marine-domain validation.

It tests whether the pipeline validated in:

* HVAC
* Aero Engine (N-CMAPSS)

transfers to actual ship machinery.

Primary research question:

Can:

Condition
→ Expected State
→ Residual
→ HI

produce meaningful health indicators from real Marine generator data?

Secondary research question (Q4b):

Can Baseline Management logic correctly handle
real maintenance events in Marine data?

---

## 2. Input Data Requirements

Refer to Marine Data Requirement Sheet v0.3.

Minimum requirements:

### 2.1 Sensor Data

Priority A (required)

| Field                            | Unit     | Notes                            |
| -------------------------------- | -------- | -------------------------------- |
| Timestamp                        | datetime | Required                         |
| Load indicator                   | kW or %  | Primary Condition Variable       |
| Exhaust temperature per cylinder | °C       | Primary State Variable candidate |
| Cooling water outlet temperature | °C       | State Variable                   |
| Lube oil pressure                | bar      | State Variable                   |
| Lube oil temperature             | °C       | State Variable                   |

Minimum duration:

3 months

Preferred:

6+ months

Ideal:

6+ months with at least one maintenance event.

Sampling interval:

Preferred:

≤ 1 hour

Ideal:

≤ 15 minutes

2-hour logbook data may still be usable
for trend-level analysis but must be audited
before use.

---

### 2.2 Maintenance Records

Required for Q4b.

Minimum acceptable:

* approximate date (month-level)
* event description
* affected component

Ideal:

* exact date/time
* component ID
* post-maintenance test result

---

## 3. Pre-Processing

### Step 1 — Data Quality Audit

Run Marine equivalent of:

data_audit.py

Report:

* completeness
* sampling interval
* coverage
* missing values
* obvious sensor artifacts

Flag:

* sensor step changes
* missing periods
* duplicate timestamps

---

### Step 2 — Segment Quality Assignment

For every maintenance event:

Assign:

Quality A
Quality B
Quality C
Quality D

according to:

baseline_management_v0.2.md

Section 15.

---

### Step 3 — Condition Variable Identification

Condition Variables are selected by engineering logic first.

Candidate Condition Variables:

* generator load
* ambient temperature
* seawater temperature
* cooling inlet temperature
* governor command / fuel rack position
* running status

if available.

Important:

Do NOT automatically select Condition Variables
based only on correlation with exhaust temperature.

Correlation ranking may be used for audit,
but engineering causality takes priority.

Expected:

2–4 Condition Variables.

---

### Step 4 — State Variable Selection

State Variables are selected by engineering priority first.

Priority order:

1. Exhaust temperature per cylinder
2. Cooling water outlet temperature
3. Lube oil pressure
4. Lube oil temperature

Residual sensitivity ranking may later be used
to compare State Variables.

Do NOT define State Variables solely from
correlation against a proxy degradation indicator.

---

## 4. Validation Steps

### B1 Analog — Expected State Model

Use earliest healthy segment.

Train:

Condition
→ State Variable

Model:

XGBoost

Success target:

Held-out R² > 0.70

Pause and diagnose if:

R² < 0.50

Likely causes:

* wrong Condition Variables
* poor data quality
* insufficient normalization

---

### B2 Analog — Residual Behavior

Residual interpretation depends on event class.

#### Major Restorative

Expected:

Residual decreases after maintenance.

#### Partial Restorative

Expected:

Affected channels improve.

Unaffected channels remain stable.

#### Fouling Removal

Expected:

Residual improves toward clean-anchor state.

May not return to original commissioning baseline.

#### Sensor Intervention

Expected:

Measurement step.

No health recovery claim.

#### Config Change

Expected:

Prediction baseline shifts.

Do not interpret as health recovery.

---

If no maintenance event exists:

Use:

early segment
vs
late segment

only as exploratory evidence.

Do NOT use pseudo-segments as Q4b evidence.

---

### HI_v0 Analog

Apply:

Rolling RMS

to normalized residual.

Candidate windows:

6h
12h
24h

Compare:

* early vs late
  or
* pre-maintenance vs post-maintenance

depending on available data.

---

### Q4b — Baseline Management

Requires:

Quality A or B maintenance event.

Procedure:

1. Classify event
2. Execute reset logic
3. Create new segment
4. Verify residual re-stationarization
5. Verify new trend direction

---

## 5. Success Criteria

### Tier 1 — Pipeline Transfer

| Criterion                 | Strong PASS | PASS  | Fail  |
| ------------------------- | ----------- | ----- | ----- |
| Expected State R²         | >0.80       | >0.60 | <0.50 |
| Residual Separation Ratio | >2.0        | >1.5  | <1.2  |
| HI vs Time Spearman       | >0.60       | >0.40 | <0.30 |

---

### Tier 2 — Baseline Management

Requires:

At least one Quality A/B event.

| Criterion            | Strong PASS      | PASS                 | Fail             |
| -------------------- | ---------------- | -------------------- | ---------------- |
| Event Classification | Record confirmed | Heuristic consistent | Cannot classify  |
| Re-stationarization  | <1 week          | <2 weeks             | No stabilization |
| Trend Physicality    | Clear            | Weak                 | Random           |

---

## 6. Failure Criteria

Validation D fails if:

| Condition               | Likely Cause                | Response              |
| ----------------------- | --------------------------- | --------------------- |
| R² < 0.50               | Wrong Condition Variables   | Re-audit              |
| No residual separation  | Too little degradation      | Extend collection     |
| Only Quality C/D events | Missing maintenance records | Q4b remains Open      |
| Residual non-stationary | Context shift               | Improve normalization |

Important:

Failure does NOT automatically invalidate the method.

Root-cause diagnosis is required before
changing algorithms.

---

## 7. No-Maintenance Fallback

If no usable maintenance event exists:

Validation D may still evaluate:

* Q1 Marine transfer
* Q2 Marine transfer
* Q3 Marine transfer

Q4b remains:

OPEN

Do NOT infer Baseline Management validity
from pseudo-segments.

---

## 8. Output Artifacts

| Artifact                      | Location     |
| ----------------------------- | ------------ |
| data_audit_marine.md          | outputs/     |
| variable_mapping_marine_v1.md | docs/design/ |
| validation_d_results.md       | outputs/     |
| segment_registry.csv          | outputs/     |
| hi_v0_marine_*.png            | outputs/     |

---

## 9. Segment Quality Reporting Requirement

All Validation D reports must include:

"Primary conclusions based on N Quality A/B segments."

"Quality C analyzed separately."

"Quality D excluded."

Mandatory requirement.

---

## 10. Relationship to Prior Validations

| Validation         | Proven           | Validation D Adds   |
| ------------------ | ---------------- | ------------------- |
| HVAC B1/B2.1/B3A   | HVAC transfer    | Marine transfer     |
| HVAC B4            | Trend candidate  | Real trend          |
| N-CMAPSS C0.2      | Aero transfer    | Marine machinery    |
| Baseline Mgmt v0.2 | Framework design | Real event handling |

Validation D can potentially provide:

* Marine evidence for Q1
* Marine evidence for Q2
* Marine evidence for Q3
* Initial Marine evidence for Q4b

Validation D cannot provide:

* Fleet generalization
* Multi-year lifecycle proof

---

## Version History

| Version | Date       | Change           |
| ------- | ---------- | ---------------- |
| v0.1    | 2026-06-06 | Initial protocol |
