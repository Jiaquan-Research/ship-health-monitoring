# Decision Log

This log records engineering decisions for the LBNL Expected State experiment.

It is separate from:

* `logs/experiment_log.md`, which records what happened during execution.
* frozen documents, which record agreed specifications.

Each entry records what decision was made, why it was made, what evidence supported it, and what downstream impact it has.

---

## Decision Template

```text
Decision ID

Decision Type

Date

Stage

Observation

Decision

Evidence

Impact

Status
```

Decision Type shall use one of:

```text
Data

Engineering

Methodology

Experiment

Architecture
```

---

## Decision 001

Decision ID

Decision001

Decision Type

Data

Date

2026-06-27

Stage

Stage B - Data Quality Audit

Observation

The LBNL dataset contains:

* 525,540 rows
* 78 variables
* no missing values
* no duplicated timestamps
* continuous one-minute sampling throughout 2018

Decision

Treat the dataset as a regularly sampled time series.

Evidence

Task B Data Quality Audit.

Impact

Temporal analyses may assume uniform sampling.

Status

Frozen.

---

## Decision 002

Decision ID

Decision002

Decision Type

Methodology

Date

2026-06-27

Stage

Stage B - Data Quality Audit

Observation

Task B is a descriptive audit.

Decision

Task B shall report observations only.

No preprocessing recommendations or modeling conclusions are permitted.

Evidence

Task B Execution Specification v1.0.

Impact

Clear separation between audit and modeling.

Status

Frozen.

---

## Decision 003

Decision ID

Decision003

Decision Type

Engineering

Date

2026-06-27

Stage

Stage C - Condition Space Audit

Observation

Engineering semantics determine Condition variables.

Decision

Condition Variables shall be selected primarily using engineering meaning.

Statistical correlation serves only as supporting evidence.

Evidence

Project design consensus.

Impact

Prevents target leakage and statistically-driven variable selection.

Status

Frozen.

---

## Decision 004

Decision ID

Decision004

Decision Type

Methodology

Date

2026-06-27

Stage

Stage C0 - Engineering Variable Taxonomy

Observation

Engineering semantics and statistical relationships answer different questions.

Engineering meaning explains what a variable represents.

Statistical analysis explains relationships among variables.

Decision

Semantic classification shall always precede statistical analysis.

Statistical methods shall only be applied after engineering screening has produced candidate variables.

Evidence

Expected State project methodology.

Project design consensus.

Impact

Correlation analysis shall only be performed on semantically screened candidate variables.

Prevents statistical methods from determining engineering meaning.

Status

Frozen.

---

## Decision 005

Decision ID

Decision005

Decision Type

Architecture

Date

2026-06-27

Stage

Stage C0

Observation

Engineering taxonomy describes the physical meaning of variables.

Model targets describe prediction objectives.

Decision

Engineering taxonomy shall remain independent of prediction target selection.

Changing the prediction target shall not require rebuilding the engineering taxonomy.

Evidence

Task C0.

Project methodology.

Impact

Engineering semantics become a stable project asset independent of individual experiments.

Status

Frozen.

---

## Decision 006

Decision ID

Decision006

Decision Type

Methodology

Date

2026-06-27

Stage

Stage C0

Observation

Setpoints and controller outputs represent different engineering concepts.

Controller outputs may contain embedded health information.

Decision

Setpoints and Controller Outputs shall be treated as independent categories.

Their eligibility for the Condition Space shall be evaluated separately.

Evidence

Engineering control principles.

Task C0 review.

Impact

Reduces the risk of unintentionally removing health information during Condition Normalization.

Status

Frozen.

---

## Decision 007

Decision ID

Decision007

Decision Type

Methodology

Date

2026-06-27

Stage

Task C1 - Condition Variable Selection Decision Protocol

Observation

Engineering Variable Taxonomy and Condition Variable Selection answer two different scientific questions.

Engineering Taxonomy describes **what a variable represents**.

Condition Variable Selection determines **whether that variable is eligible to enter the Condition Space**.

These two activities have different purposes and should not be coupled.

Decision

Engineering Variable Taxonomy shall remain independent of the Condition Variable Selection process.

Changes to Condition Variable eligibility shall not require modifications to the Engineering Taxonomy.

Similarly, improvements to the Engineering Taxonomy shall not automatically change the Condition Variable Selection Protocol.

Evidence

Task C0 - Engineering Variable Taxonomy

Task C1 - Condition Variable Selection Decision Protocol

Project methodology consensus

Impact

Engineering semantics become a stable knowledge layer.

Selection criteria evolve independently based on experimental evidence.

This separation improves reproducibility, traceability, and long-term maintainability of the Expected State framework.

Status

Frozen

--- 

## Decision 009

Decision ID

Decision009

Decision Type

Methodology

Date

2026-06-27

Stage

Task C2 - Condition Variables v1

Observation

Some variables may plausibly describe operating conditions while also encoding equipment-health information.

Current engineering evidence is insufficient to demonstrate that their inclusion preserves Condition Normalization.

Decision

Such variables shall remain excluded from Condition Variables v1 until experimental evidence demonstrates that their inclusion does **not** compromise Condition Normalization.

The primary validation criterion shall be Residual leakage analysis rather than prediction accuracy.

Evidence

Task C2

Expected State methodology

Impact

Future evolution from Condition Variables v1 to v2 shall be driven by experimental evidence instead of engineering intuition alone.

Status

Frozen

---

## Decision 010

Decision ID

Decision010

Decision Type

Experiment

Date

2026-06-28

Stage

Task D1 - Expected State Baseline

Observation

The temporal Train/Test split produces different operating-power regimes.

The training period contains substantially more high-power operating conditions than the testing period.

Therefore, Test performance reflects both model generalization and operating-regime shift.

Test metrics alone shall not be interpreted as the engineering quality of the Expected State.

Decision

Expected State v1 is accepted as the baseline engineering model.

Residual Dataset v1 is approved for downstream analysis.

All subsequent Residual interpretation shall be stratified by operating regime.

At minimum:

* Train vs Test
* Load / Power region

shall be analyzed separately.

Aggregate residual statistics alone are insufficient.

Evidence

Task D1 prediction performance.

Prediction scatter plots.

Expected State v1 Report.

Impact

Task E shall perform stratified Bias Audit.

Residual interpretation must explicitly consider operating-regime differences.

Status

Frozen

---

## Decision 011

Decision ID

Decision011

Title

Field interviews confirm project positioning toward transparent engineering decision support.

Decision

Future project positioning shall emphasize transparent engineering decision support based on:

* Expected State
* Residual analysis
* Trend monitoring
* Traceable engineering evidence

rather than opaque diagnostic outputs whose reasoning cannot be independently verified by engineers.

Evidence

Engineering Field Interview Consensus v1.0

Impact

Future Marine Translation

Decision Distillation

Product Positioning

Risk Assessment

Status

Accepted

---

## Decision012

Title

Residual Bias Audit Boundary

Status

Accepted

Source

Task E1 - Residual Bias Audit v1

---

Observation

Residual Bias Audit demonstrates that Expected State v1 is approximately unbiased within the operating regime represented by the training dataset.

Test-set bias is observed for selected variables.

This observation shall be treated as an experimental boundary rather than evidence that Expected State construction has failed.

---

Engineering Conclusions

1.

Expected State v1 satisfies the bias requirement within the training operating regime.

2.

Bias observed in the Test split shall be interpreted separately from Leakage.

3.

Variables exhibiting insufficient operating-range coverage cannot support meaningful Bias or Leakage evaluation within that operating regime.

---

Constraints for Task E2

E2 shall distinguish:

Residual Bias

and

Residual Leakage

These are independent experimental questions.

---

For variables:

* OA_TEMP
* OA_TEMP_WB

Leakage interpretation shall consider the previously observed Test bias.

---

For variables:

* CDWL_CW_FLOW
* CWL_PRI_CW_FLOW

Leakage evaluation shall be skipped for the Test split because operating-range coverage is insufficient.

Only Train results shall be interpreted.

---

Rationale

Task E1 establishes that Expected State validity depends on both:

* residual bias
* operating-regime coverage

Coverage limitations shall be documented explicitly rather than interpreted as Expected State failure.

---

## Decision013

Title

Expected State Validity Depends on Operating Coverage

Status

Accepted

Source

Task E1

Task E2

---

Observation

Expected State v1 performs well within the operating regime represented by the training dataset.

Residual Bias and Residual Leakage are both acceptably small under this condition.

However, substantially different operating regimes may reduce prediction reliability without implying failure of the Expected State methodology.

---

Engineering Interpretation

Expected State should therefore be interpreted together with its operating-domain applicability.

Model confidence depends not only on prediction quality but also on whether the current operating condition is sufficiently represented by historical training data.

---

Methodological Implication

Expected State validation now consists of three complementary dimensions:

* Prediction Accuracy
* Residual Independence
* Operating-Regime Robustness

These dimensions shall be evaluated separately.

---

Future Work

Future versions of the framework should include an explicit Operating Coverage Assessment (or equivalent confidence layer) before Expected State interpretation.

This capability is not yet implemented and remains future work.

---

Boundary

Decision013 introduces a methodological interpretation only.

It does not modify:

* Expected State v1
* Condition Variables
* Residual construction
* Leakage results
