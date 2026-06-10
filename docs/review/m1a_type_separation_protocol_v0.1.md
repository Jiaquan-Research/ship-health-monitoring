# Validation M-1A Type Separation Protocol

Date:

2026-06-10

Status:

Pre-registered

Experiment:

M-1A

---

## 1. Motivation

Validation M-1 showed:

Type A

supported.

Type C

supported.

Type B

plausible.

Type D

not primary.

However:

their relative importance remains unknown.

The purpose of M-1A is not to fix leakage.

The purpose is to determine:

which mechanism dominates.

---

## 2. Research Question

Among:

Type A

Model Capacity Limitation

Type B

Incomplete Condition Variables

Type C

Extrapolation Failure

which mechanism contributes most to
the observed condition leakage?

---

## 3. Scope

Use only:

existing LBNL data.

Use frozen HVAC-v1 variable definitions.

Use frozen B1 residual artifacts.

No new datasets.

No Validation D.

No Marine data.

---

## 4. M-1A.1

Model Capacity Probe

Target:

Type A

Question:

Does higher model capacity reduce
condition leakage?

Procedure:

Use identical inputs.

Allow diagnostic models such as:

Random Forest

Extra Trees

Compare:

condition correlations

R²

against HVAC-v1.

Purpose:

diagnosis only.

Not replacement.

---

## 5. M-1A.2

Cross-season Transfer Probe

Target:

Type C

Question:

Does performance degrade when
training and testing occur in
different seasonal regions?

Procedure:

Train and test combinations:

Winter → Winter

Summer → Summer

Winter → Summer

Summer → Winter

Compare:

R²

residual statistics

correlation structure.

Evidence for Type C:

cross-season performance collapse.

---

## 6. M-1A.3

Missing Variable Inventory

Target:

Type B

Question:

Are potentially relevant condition
variables absent from HVAC-v1?

Examples:

humidity

solar radiation

time features

other environmental variables

Purpose:

inventory only.

No new variables are added.

No retraining.

No experiments are performed.

---

## 7. Success Criterion

Dominant leakage mechanism
can be identified.

Relative importance becomes clearer.

---

## 8. Failure Criterion

Type A

Type B

Type C

remain inseparable.

No dominant mechanism emerges.

Further diagnosis required.

---

## 9. Interpretation Rules

Type A dominates if:

higher-capacity models substantially
reduce leakage.

---

Type C dominates if:

same-season performance remains good

while

cross-season transfer collapses.

---

Type B dominates if:

major candidate variables are found
to be absent from HVAC-v1.

---

Multiple mechanisms may coexist.

No single label should be forced.

---

## 10. Consequences

No remediation path is assumed.

No algorithm changes are implied.

No evidence levels are upgraded.

M-1A is diagnostic only.

---

## 11. Philosophy

Classification precedes correction.

Unknown remains acceptable.

Failure is informative.

---

Version History

v0.1

2026-06-10

Initial protocol.
