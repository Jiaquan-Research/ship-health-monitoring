# Dataset Audit Protocol

v0.1

---

## 1. Purpose

The goal is to understand available datasets.

Questions:

What data do we have?

How large are they?

What variables exist?

What natural regimes may exist?

No analysis is intended.

No hypotheses are tested.

No conclusions are upgraded.

---

## 2. Principles

Observation first.

No expectations.

Positive and negative findings are equally valuable.

Dataset audit is not dataset analysis.

No dataset is expected to support Q0.

Failure is acceptable.

---

## 3. Standard Fields

For every dataset record:

Dataset Name

Source

Domain

Approximate Size

File Format

Number of Files

Number of Variables

Sequence Length

Sampling Information

Current Status

Natural Regimes (if obvious)

Notes

---

## 4. Natural Regimes

Natural regimes should only be recorded when directly visible.

Examples:

Battery

- temperature
- charge profile
- SOC region

Hydraulic

- pressure region
- relief valve state

Bearing

- speed
- load

HVAC

- season
- cooling mode
- heating mode

C-MAPSS

- operating conditions

These are observations only.

Not hypotheses.

Not evidence.

---

## 5. Explicit Non-Goals

Dataset audit should NOT:

- run experiments
- compare datasets
- support Q0
- support Claim Registry
- modify engineering architecture

---

## 6. Outputs

Recommended outputs:

dataset cards

summary tables

inventory documents

No figures are required.

No statistics are required.

No rankings are intended.

---

## 7. Current Scope

Initial datasets:

HVAC

N-CMAPSS

Battery

Hydraulic (ZEMA)

C-MAPSS FD001-004

Bearing datasets

Future datasets:

Marine DG

TEP

Boilers

Nuclear systems

No commitment implied.

---

## 8. Evidence Status

Evidence level:

None.

Dataset audit itself does not create evidence.

---

## Version History

v0.1

2026-06-11

Initial dataset census protocol created.

Observation only.

No conclusions.

