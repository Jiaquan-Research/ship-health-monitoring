# Decision DD-004

## Semantic Window Validation

## Purpose

Record the engineering validation of Semantic Window introduced by DD-002.

## Decision Summary

Semantic Window significantly reduces operating-condition dependence of residual-derived Candidate Health Indicators.

Semantic Window is therefore accepted as an engineering preprocessing step before Health Indicator construction.

Current evidence supports reduction of Condition Evidence.

Isolation of true Health Evidence remains unverified because no degradation ground truth exists in the LBNL dataset.

## Evidence

Reference:

```text
H4B
Health Evidence Isolation Validation
```

Evidence includes:

* Condition Dependence reduction, approximately 80%.
* Temporal Persistence reinterpretation.
* Reviewer PASS WITH CONDITIONS.

## Scope

DD-004 applies before all future Health Indicator construction.

It is independent of Expected State implementation.

It is independent of specific Health Indicator algorithms.

It is applicable to all future Candidate Health Indicator evaluations.

## Limitations

DD-004 does not validate degradation detection.

DD-004 does not validate Remaining Useful Life.

DD-004 does not validate Marine deployment.

DD-004 only validates reduction of operating-condition contamination.

## Status

Frozen
