# Reviewer Prompt Templates

Document status: Protocol Support
Task ID: DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_PREPARATION_001

## Initial Review Prompt

```text
You are performing an independent blind Deep Research review using the attached Transport v2 package files.

This is not External Validation execution. You are not the External Reviewer. Your findings are advisory and require later reconciliation and human judgment.

First, read the Research Brief and Review Guide. Then inspect the uploaded Reading Packs and lookup files. Before issuing findings, provide a Pack Access Declaration listing every uploaded file as READ, PARTIALLY_READ, LOOKUP_ONLY, NOT_ACCESSED, or PARSER_FAILURE.

Do not claim Marine validity, Marine feasibility, deployment readiness, shipboard RUL capability, External Validation completion, or Marine request readiness.

Begin the review using the Research Brief's Q1-Q8 structure.
```

## Continue Review Prompt

```text
Continue the same blind review with the newly uploaded profile files.

First update the Pack Access Declaration. State which prior packs remain accessible and which new packs were read or could not be parsed.

Continue findings under the Research Brief's required report structure. Keep repository evidence and external evidence separately identifiable.
```

## Evidence Follow-up Prompt

```text
The attached files are targeted Evidence Packs or lookup records requested during the review.

Use them only to resolve or support specific findings. Update the Pack Access Declaration and identify which finding IDs or review questions use these Evidence Packs.

Do not broaden the review scope or create new formal gaps or claims.
```

## Clarification Prompt

```text
Clarification request:

Please answer only the specific clarification below. Do not revise unrelated findings unless the clarification changes their evidence basis.

Clarification:
<operator inserts clarification>
```

## Final Report Prompt

```text
Prepare the final blind-review report using the Research Brief's required 13-section structure.

Include the complete Pack Access Declaration. Distinguish verified repository contradictions, external scientific/engineering challenges, interpretive concerns, translation risks, governance/process overhead, and uncertain findings.

State any parser failures or inaccessible packs. Do not claim complete package review if any required Reading Pack was inaccessible or truncated.
```
