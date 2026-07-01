# Engineering Field Interview Consensus v1.0

Date

2026-06-28

Version

v1.0

Status

Frozen

Evidence Source

* Marine Engineer Interview A
* Marine Engineer Interview B

Purpose

Record qualitative engineering evidence from frontline marine engineers.

This document records observations only.

It does not establish statistical industry conclusions.

---

## Consensus 1

Existing onboard systems provide monitoring, alarms, and trend curves, but do not provide quantitative degradation assessment.

Evidence

Both interviewees indicated that current systems mainly support:

* parameter monitoring
* alarms
* historical trend review

but cannot quantify gradual degradation.

Engineering implication

Current workflow remains:

```text
Sensor

->

Alarm

->

Human Judgment
```

rather than:

```text
Condition

->

Expected State

->

Residual

->

Risk Assessment
```

Confidence

High

---

## Consensus 2

Slow degradation is difficult to perceive consistently.

Evidence

Interviewees repeatedly mentioned:

* gradual parameter drift
* turbocharger speed
* scavenging pressure
* cooling performance

Operators mainly rely on:

* memory
* historical curves
* experience

Engineering implication

Long-term degradation is difficult to detect consistently without quantitative references.

Confidence

High

---

## Consensus 3

Alarm thresholds occur later than engineering attention points.

Evidence

Operators mainly react after alarms.

Small deviations rarely receive attention before alarm thresholds.

Engineering implication

An engineering opportunity exists between:

```text
Normal

->

Alarm
```

Confidence

High

---

## Consensus 4

Historical trend comparison is already common engineering practice.

Evidence

Interviewees naturally compare:

```text
Current

->

Historical Curves

->

Same Operating Condition
```

Comparison is qualitative.

No quantitative deviation metric exists.

Engineering implication

Expected State extends existing engineering practice rather than replacing it.

Confidence

High

---

## Consensus 5

Meaningful comparison requires similar operating conditions.

Evidence

Interviewees repeatedly stressed that comparison requires similar:

* engine load
* engine speed
* seawater temperature
* operating condition

Engineering implication

Strong field evidence supporting Condition Normalization.

Confidence

Very High

---

## Consensus 6

Long-term vessel-specific historical baselines are considered valuable.

Evidence

Interviewees independently proposed ideas such as:

* onboard database
* comparison with previous voyages
* comparison with several months earlier

Engineering implication

Supports long-term historical baseline management.

Confidence

High

---

## Consensus 7

Decision support is preferred over automatic diagnosis.

Evidence

Interviewees expect systems to:

* monitor
* compare
* quantify
* remind

Final engineering decisions remain human responsibilities.

Engineering implication

Supports transparent engineering decision support.

Confidence

Very High

---

## Consensus 8

Main engine and generator are perceived as the highest-value deployment targets.

Evidence

Both interviews converged toward:

Primary deployment targets:

* Main Engine
* Diesel Generator

Engineering implication

Performance degradation directly affects propulsion, electrical supply, fuel efficiency, and maintenance planning.

Generator monitoring capability varies substantially across vessel types and automation configurations.

Some vessels provide only minimal alarm signals.

Others already integrate generator monitoring into alarm and trend systems.

Deployment feasibility therefore requires vessel-specific assessment rather than assuming uniform instrumentation.

Confidence

Medium

Further interviews recommended.

---

## Consensus 9

Current engineering practice relies primarily on experience-based interpretation rather than OEM reference models.

Evidence

Interviewees indicated that routine engineering decisions are mainly based on:

* accumulated operational experience
* historical observations
* engineering judgement

rather than direct use of OEM reference models.

Engineering implication

Vessel-specific historical baselines may improve engineering acceptance by providing references derived from the vessel's own operational history.

Confidence

High

---

## Consensus 10

Operators naturally reason in a condition-normalized manner even without formal terminology.

Evidence

Interviewees repeatedly referred to:

* same operating condition
* same load
* same seawater temperature
* comparison under similar conditions

although they never used the terminology:

* Condition Normalization
* Expected State
* Residual

Engineering implication

Condition Normalization aligns naturally with existing engineering reasoning rather than introducing an unfamiliar workflow.

Confidence

Very High

---

## Overall Engineering Interpretation

Current engineering workflow is approximately:

```text
Monitoring

->

Alarm

->

Human Diagnosis
```

Field interviews consistently indicate demand for:

```text
Condition

->

Expected State

->

Residual

->

Trend

->

Engineering Recommendation

->

Engineer Decision
```

This represents an enhancement of engineering decision support rather than replacement of engineering expertise.

---

## Scope Limitation

This document summarizes qualitative evidence collected from two experienced marine engineers.

The observations should be treated as qualitative field evidence only.

They are not statistically representative of the commercial marine industry.

Further interviews are recommended before generalization.
