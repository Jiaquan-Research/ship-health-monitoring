# DD-005 — Stateful Health Indicator Lifecycle

## Purpose

Lifecycle management becomes necessary once a Health Indicator contains accumulated historical information.

When a Health Indicator depends on prior observations, its current value may continue to reflect evidence accumulated before a maintenance event, baseline change, or operating context change.

DD-005 freezes the lifecycle principles governing stateful Health Indicators before H5 implementation begins.

## Design Principle H5-R1

> Every stateful Health Indicator shall explicitly define its State Reset Policy.

This is an architectural requirement rather than an algorithm-specific rule.

The requirement applies whenever a Health Indicator carries accumulated historical state, regardless of how the indicator is implemented.

## Health Indicator Classification

| Type | Definition | Reset Required |
|---|---|---|
| Memoryless Health Indicator | Output depends only on current observation | No |
| Stateful Health Indicator | Output depends on accumulated historical information | Yes |

Classification depends on implementation rather than algorithm family.

Specific algorithm families shall not be classified as inherently Memoryless or Stateful by DD-005.

## Mandatory Lifecycle Documentation

Every Stateful Health Indicator shall explicitly document:

* Reset Strategy
* Warm-up Strategy
* Baseline Dependency
* State Persistence

These are documentation requirements.

They are not implementation requirements.

## Maintenance Event

A Maintenance Event is a lifecycle event that may invalidate previously accumulated health evidence.

Whether a specific maintenance event requires state reset is determined by engineering judgment at the time of the event, not by automatic rule.

Maintenance Event is an observable engineering event.

State Reset is an engineering decision.

The existence of a maintenance record does not automatically imply lifecycle reset.

DD-005 does not define:

* which maintenance actions require reset;
* when reset should occur;
* reset policies for individual maintenance operations.

These remain future work.

### Scope Boundary

DD-005 defines lifecycle interfaces only.

It does not define:

* Maintenance taxonomy
* Maintenance decision workflow
* State Manager implementation
* Expected State version control
* Automatic reset policies
* Maintenance scheduling logic

Those remain future work.

## Scope

Applicable to:

* H5
* Marine Validation
* Future online deployment

Not applicable to:

* Phase 1
* Phase 2 completed experiments

## Limitations

DD-005 does not define:

* Maintenance Taxonomy
* State Manager
* Expected State Version Control
* Automatic Maintenance Detection

These remain exploratory.

## Status

Frozen
