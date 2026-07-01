# Negative Control Protocol v0.1

Date:

2026-06-10

Status:

Pre-registered

Experiment:

Validation I-1

---

## 1. Motivation

Previous validations focused on
known degradation scenarios.

No experiment has yet tested:

Can residual and HI remain stable
when no degradation exists?

This experiment addresses that question.

---

## 2. Research Question

Q:

Will residual or HI exhibit trend-like
behavior on healthy trajectories?

---

## 3. Null Hypothesis

H0:

Residual and HI remain stationary.

No systematic trend exists.

Observed fluctuations represent noise.

---

## 4. Alternative Hypothesis

H1:

Residual and/or HI exhibit systematic
trend-like behavior even without degradation.

Possible explanations include:

* condition leakage;
* model incompleteness;
* residual construct problems;
* false-positive mechanisms.

---

## 5. Data Scope

No retraining.

No new datasets.

No new models.

### LBNL healthy period definition

Use:

Baseline dataset only
(ChillerPlant.csv)

Exclude:

first 5% of samples

last 5% of samples

No fault datasets are allowed.

---

### N-CMAPSS supplementary evidence

Use:

Zone A only

(first 20% lifecycle)

from frozen C0.2 units.

Do NOT use:

Zone T

Zone B

---

## 6. Metrics

Primary metric:

Spearman(time, HI_v0)

computed over:

the entire healthy period.

---

Secondary metrics:

Spearman(time, residual RMS)

trend slope

monotonicity

---

Window stability audit:

Split healthy period into:

three equal sub-windows.

Compute the same metrics inside:

Window 1

Window 2

Window 3

Experiment succeeds only if:

both

full-period

and

sub-window results

pass.

---

## 7. Success Criterion

Expected observations:

Spearman approximately zero.

No consistent monotonic increase.

Residual and HI fluctuate around
stable levels.

Sub-window behavior remains stable.

No obvious trend-like behavior.

---

## 8. Failure Criterion

Trend-like behavior appears
on healthy data.

Examples:

persistent monotonic increase;

strong Spearman correlation;

stable positive slope;

false-alarm behavior.

Sub-window instability also counts
as failure.

---

## 9. Consequences of Failure

Failure does NOT invalidate the project.

Failure suggests:

Residual may contain:

* condition leakage;
* context effects;
* model deficiencies.

Failure indicates that
residual construct validity
must be re-examined.

Actions:

* suspend forward validation work;

* re-examine condition normalization;

* re-examine Expected State formulation;

* re-assess residual construct validity;

* Validation D remains blocked
  until I-1 passes.

No specific remediation path
is assumed.

---

## 10. Consequences of Success

Success does NOT prove Trend.

Success only demonstrates:

Residual and HI do not generate
obvious false trends
on healthy trajectories.

Trend interpretation remains
an open question.

---

## 11. Prohibited Actions

Not allowed:

changing thresholds
after seeing results;

changing metrics
after execution;

changing healthy periods post-hoc;

changing outcome definitions;

re-labeling results.

---

## 12. Philosophy

A successful negative control
increases confidence.

A failed negative control
increases understanding.

Both outcomes are valuable.

Every PASS should correspond
to a test that could genuinely FAIL.

Unknown remains a valid outcome.

---

## Version History

v0.1

2026-06-10

Initial pre-registration.
