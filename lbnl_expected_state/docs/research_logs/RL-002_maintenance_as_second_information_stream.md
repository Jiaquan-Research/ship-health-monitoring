# RL-002 — Maintenance as Second Information Stream

## Purpose

Record an exploratory architectural observation.

This is not a frozen engineering decision.

## Observation

Health Indicators are influenced by two distinct information streams.

```text
Sensor Stream
        │
        ▼
Evidence Pipeline
        │
        ▼
Health Indicator

Maintenance Stream
        │
        ▼
Lifecycle Management
        │
        ▼
State Reset / Baseline Transition
```

## Interpretation

Sensor history determines accumulated evidence.

Maintenance history determines whether previously accumulated evidence remains valid.

Maintenance records constitute a second engineering information stream.

```text
Sensor Data
        ↓
Equipment Behaviour

Maintenance Records
        ↓
Equipment Lifecycle
```

The Sensor Stream describes equipment behaviour through observed measurements.

The Maintenance Stream describes lifecycle events that may change whether accumulated evidence remains valid.

Future State Manager concepts may integrate both streams.

The current project does not yet implement such integration.

This remains an exploratory architectural observation.

## Relation to Current Project

This observation connects to:

* Reset Compatibility
* DD-005
* H5 lifecycle design

It does not claim implementation.

## Future Work

Potential future investigations include:

* Maintenance Taxonomy
* Lifecycle Manager
* Event-driven Health Indicator management
* Expected State version management
* Maintenance-triggered baseline transition

These are exploratory ideas only.

## Status

Exploratory.

Not a frozen engineering decision.
