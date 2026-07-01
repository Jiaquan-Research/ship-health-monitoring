# Validation I-1 Postmortem

Date:

2026-06-10

Status:

FAIL

---

## 1. Purpose

Validation I-1 was designed as the first
negative-control experiment.

Question:

Can residual and HI remain stable on
healthy trajectories?

This experiment followed the
pre-registered protocol:

docs/review/negative_control_protocol_v0.1.md

No thresholds were modified.

No post-hoc changes were made.

---

## 2. Verdict

FAIL

Reason:

Sub-window instability appeared
within healthy baseline data.

This triggered the protocol-defined
failure condition.

---

## 3. Main Findings

Full-period metrics:

Spearman(time, HI_v0)

≈ 0.24

Spearman(time, residual RMS)

≈ 0.23

These values alone do not indicate
strong trend behavior.

However:

Window-level behavior was inconsistent.

Window 1:

positive trend

Window 2:

positive trend

Window 3:

negative trend

Trend direction reversed.

This constitutes instability.

---

## 4. Trend Attribution

Strong correlations were observed:

HI vs OA_TEMP

≈ 0.72

Residual RMS vs OA_TEMP

≈ 0.78

HI vs Load

≈ 0.52

Residual RMS vs Load

≈ 0.67

Observed trend therefore appears
strongly associated with:

seasonal pattern

and

operating load.

---

## 5. Interpretation

The failure does NOT suggest:

"HI generates false degradation
signals spontaneously."

Instead, the evidence suggests:

Residual and HI remain sensitive
to condition changes.

Likely cause:

Condition leakage.

Residual construct validity therefore
remains incomplete.

---

## 6. Relationship to Previous Findings

This result is consistent with:

B3A seasonal stability observations.

Seasonal effects had already been
identified qualitatively.

Validation I-1 provides
quantitative confirmation.

---

## 7. Relationship to Fable5 Review

Fable5 argued:

Residual may contain
condition information rather than
pure health information.

Validation I-1 partially confirms
this concern.

However:

The observed trend appears explainable
by OA_TEMP and load.

The result therefore supports:

condition leakage

more strongly than:

spurious degradation behavior.

---

## 8. Project Impact

According to the protocol:

Forward validation work is suspended.

Validation D remains blocked.

Residual construct validity
must be re-examined.

Condition normalization becomes
the highest-priority issue.

---

## 9. What I-1 Does NOT Show

I-1 does NOT prove:

that the pipeline is invalid.

I-1 does NOT prove:

that HI has no value.

I-1 does NOT prove:

that Trend interpretation is impossible.

The experiment only demonstrates:

healthy trajectories still contain
condition-related residual structure.

---

## 10. Next Question

M-1:

Condition Leakage Audit

Question:

Why do OA_TEMP and load remain
strongly correlated with residual
and HI despite being included
as Condition Variables?

Possible explanations:

* incomplete normalization;

* missing variables;

* non-linear effects;

* model extrapolation limits.

---

## 11. Lessons Learned

Validation I-1 became the first
pre-registered experiment to fail.

No thresholds were changed.

No data segments were replaced.

No post-hoc reinterpretation occurred.

Failure was accepted.

Understanding increased.

---

## Version History

v1

2026-06-10

Initial postmortem.
