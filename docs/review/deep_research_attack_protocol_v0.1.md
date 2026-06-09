# Deep Research Attack Protocol v0.1

Date: 2026-06-09

Status:
Ready

Purpose:

Challenge the current claims.

Seek reasons why the claims may be wrong.

Do not optimize for agreement.

---

## Scope

Claims under review:

C1
Condition → Expected State

C2
Expected State → Residual

C3
Residual → HI

C4
Residual → Trend

C5
Baseline Management

Reference:

docs/review/claim_registry_v0.1.md

---

## General Principle

Assume the claims are false.

Attempt to explain the observations
without relying on the proposed interpretation.

Agreement is unnecessary.

Falsification attempts are encouraged.

---

## Allowed Outputs

Deep Research should identify:

* hidden leakage
* alternative explanations
* missing controls
* statistical weaknesses
* overfitting risks
* domain transfer risks
* survivorship bias
* selection bias
* confounding variables
* invalid assumptions
* engineering counterexamples

---

## Forbidden Behavior

Do NOT:

* summarize the project
* promote the method
* rewrite documents
* strengthen conclusions
* assume correctness

Do NOT optimize for agreement.

---

# Claim-specific Questions

---

## C1

Could Expected State models work only because:

* HVAC systems are strongly controlled?
* Aero engines are low-dimensional?
* Marine generators violate these assumptions?

Could high R² arise from hidden leakage?

What conditions would cause C1 to fail?

---

## C2

Could residual separation arise from:

* label ordering artifacts?
* sensor selection bias?
* target variable choice?

Would residual still separate degradation
if different State Variables were used?

---

## C3

Does HI_v0 truly improve degradation sensitivity?

Or is Rolling RMS merely smoothing noise?

Would:

EWMA
CUSUM
Trend slope

perform equally well or better?

Can C3 be falsified?

---

## C4

B4 used pseudo-degradation paths.

Could trend behavior disappear
under real temporal degradation?

Is there evidence from:

HVAC
Aviation
Nuclear
Gas turbines

that residual trend naturally exists?

Or are alternative explanations stronger?

---

## C5

Could Baseline Management fail because:

* maintenance effects are not discrete?
* segments overlap?
* restoration is partial?
* re-stationarization never occurs?

Are there industrial counterexamples?

How do:

nuclear
aviation
gas turbines
condition-based maintenance

handle this problem?

---

## Output Format

For each claim:

### Claim ID

### Main Weaknesses

### Severity

Low
Medium
High

### Alternative Explanation

### Suggested Experiment

### Whether the current evidence is sufficient

Yes / No

### Recommendation

Maintain

Downgrade

Reject

---

## Deliverable

Expected output:

Claim Attack Review

organized by:

C1
C2
C3
C4
C5

Priority:

Attack quality over completeness.

## Disagreement is preferred over agreement.
