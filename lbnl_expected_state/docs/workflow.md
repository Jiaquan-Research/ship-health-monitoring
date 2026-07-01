# Experiment Workflow

Each experiment stage must complete the same execution cycle before the next stage begins.

```text
Task

->

Execute

->

Review Outputs

->

PASS?

+-- No
|     |
|     v
|  Fix Current Stage
|     |
|     v
|  Re-execute
|     |
|     v
|  Review Again
|
+-- Yes
      |
      v

Decision Log

->

Git Commit

->

Proceed to Next Stage
```

A stage must never advance before review has passed.

Failed review always returns to the current stage.

## Standard Cycle

1. Task

   Define the stage objective, scope, inputs, outputs, and constraints.

2. Execute

   Run only the approved work for the current stage.

3. Review Outputs

   Inspect generated files and confirm that required deliverables exist.

4. PASS?

   If review fails, fix only the current stage, re-execute, and review again.

5. Decision Log

   Record engineering decisions separately from execution history.

6. Git Commit

   Commit the completed stage once outputs and decisions have been reviewed.

7. Proceed to Next Stage

   Start the next stage only after the current cycle is complete.
