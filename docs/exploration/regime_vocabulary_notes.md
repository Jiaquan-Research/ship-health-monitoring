# Regime Vocabulary Notes

Source:

Deep Research: Vocabulary for Multi-Regime Industrial Systems

Status:

Reference notes only.

Not evidence.

Not theory.

Not Q0 support.

---

## 1. Purpose

This document records vocabulary and conceptual mappings
from literature on multi-regime industrial systems.

The goal is to reduce terminology confusion, not to answer
Q0.

These notes are a cross-domain reference. They do not define
a project taxonomy or upgrade any conclusion.

---

## 2. Core Finding

No single cross-domain standards-level taxonomy was found.

However, stable local distinctions exist across:

- control / hybrid systems
- PHM / CBM
- process monitoring
- HVAC
- batteries
- gas turbines / aero engines
- nuclear / power plants
- marine propulsion
- hydraulic systems

A cross-domain mapping is therefore useful as a Rosetta
stone, but not as a universal standard.

---

## 3. Rosetta Stone Table

| Term | Typical meaning | Closest correspondence | Caution |
|---|---|---|---|
| operating mode | A discrete configuration or logic-selected behavior under which different equations, control laws, or monitoring models may apply | discrete regime; operational state | Mode is often discrete/configurational and should not be treated as identical to a continuous operating point. |
| regime | A segment or region in which the system follows a distinct statistical or physical relation | mode; segment; operating region | Usage varies across fields and may refer to observed, inferred, discrete, continuous, or time-segmented structure. |
| condition | An operating/environmental condition or an asset health condition | operating condition; health state | Condition can mean operating condition or health condition; the scope must be stated. |
| state | The variable set describing current system status; formal dynamical meaning in control, broader usage elsewhere | dynamical state; hybrid state; health state | State is formal in control theory but loose in PHM and is not automatically interchangeable with mode. |
| context | External explanatory information such as environment, mission, schedule, or scenario | exogenous variables; operating conditions | Context is less standardized and may not be part of the system's formal state. |
| operating point | A local point in an operating envelope, often indexed by continuous scheduling variables | design point; continuous regime index | Operating point is usually continuous/local rather than a discrete mode. |
| duty cycle / operational profile | A time-distributed sequence or distribution of loads, phases, rest periods, or operating states | load profile; mission profile; test cycle | Duty cycle is a temporal load pattern, not an instantaneous mode. |

---

## 4. Two Vocabularies That Should Not Be Merged Casually

General ML/statistical vocabulary:

- dataset shift
- covariate shift
- domain shift
- concept drift
- change point / regime change

Engineering-practical vocabulary:

- off-design condition
- false alarms during transitions
- false positives under dynamic operating conditions
- ambient-condition dependence
- operating-condition dependence
- load-profile mismatch
- field-versus-test condition mismatch

The first vocabulary classifies changes in distributions,
relations, or time-series segments. The second usually
describes the operational symptom or engineering mismatch.
They overlap, but they are not interchangeable by default.

The project-internal label "Type C" should not be
automatically mapped to any single external term.

It may correspond to different terms depending on context.

---

## 5. Five Practical Recognition Patterns

The reviewed literature commonly recognizes cross-regime
application failure through these patterns:

- residuals or alarms spike at mode transitions;
- performance deteriorates outside the training operating
  envelope;
- uncorrected indicators move with ambient/load/context
  variables more than with time or wear;
- stratifying or correcting by operating condition removes
  much of the apparent anomaly;
- standardized retest at matched conditions shows the
  deviation was operational rather than permanent.

M-1A resembles the third pattern.

No conclusion is implied.

---

## 6. Domain Notes

### HVAC / Chiller Plants

Operating-condition vocabulary commonly includes load,
water temperatures, flows, season, and steady versus
dynamic operation.

### Battery Systems

Operating conditions or stress factors commonly include
temperature, SOC, C-rate, DOD, and calendar versus cycling
aging.

No universal dataset comparability rule was found.

### Aero Engines / Gas Turbines

Common vocabulary includes operating point, off-design
condition, ambient condition, power setting, and mission or
flight phase.

### Hydraulic Systems

Working conditions commonly include pressure, flow,
temperature, load cycle, and duty-cycle segment.

Review-level regime vocabulary appears thinner than in
process, HVAC, or nuclear literature.

### Chemical Process Plants

Common vocabulary includes multimode process, steady-state
modes, and transition processes.

The vocabulary is relatively mature.

### Power Plants / Nuclear

Operational states or modes commonly include startup, hot
standby, hot shutdown, cold shutdown, refueling, and
load-following.

### Marine Propulsion / Marine Diesel Engines

Vocabulary often uses operational profile, load profile,
test cycle, and propeller-law operation.

Review-grade abstract regime vocabulary appears thinner.

Propeller-law operation is a useful term to record, not yet
a conclusion.

---

## 7. Regime Boundary Variables

Common regime boundary variables include:

- load / power
- temperature
- SOC
- C-rate
- DOD
- control-state variables
- auxiliary equipment status
- operational phases
- startup / steady-state / shutdown
- maneuvering states
- flow / pressure / speed

Boundaries may be crisp, fuzzy, or probabilistic.

Procedures, standards, and control logic may produce crisp
boundaries. Boundaries inferred from operating data may
instead be soft or uncertain.

---

## 8. Battery E-2 Implication

Deep Research supports the decision not to interpret E-2
directly.

Battery literature emphasizes operating-condition and
stress-factor alignment.

No single universal comparability rule was found.

Therefore:

Battery should not re-enter Q0 inventory until E-2 is
redesigned with aligned internal regime definitions.

No conclusion about Battery Type C is implied.

---

## 9. Marine Note

Marine literature often emphasizes operational profile,
load profile, test cycle, and propeller-law operation rather
than an abstract regime taxonomy.

This suggests that future Marine regime work should begin
from marine-native vocabulary rather than importing HVAC or
ML terms directly.

This note is not expanded into theory.

---

## 10. Non-Goals

This document does NOT:

- answer Q0
- recommend terminology adoption
- modify Dataset Zoo evidence counts
- modify Method Zoo priorities
- support Validation D
- support Claim Registry

---

## Version History

v0.1

2026-06-12

Initial vocabulary notes created from Deep Research.

No conclusions.
