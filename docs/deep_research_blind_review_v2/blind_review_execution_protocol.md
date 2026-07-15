# Deep Research Blind Review v2 Execution Protocol

Document status: Protocol
Task ID: DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_001
Source transport: DEEP_RESEARCH_REVIEW_PACKAGE_TRANSPORT_V2_001
Source package: DEEP_RESEARCH_REVIEW_PACKAGE_001 v1.1

## 1. Purpose

This protocol defines deterministic delivery from Transport v2 into LLM Blind Review sessions. It does not execute Blind Review and does not modify Transport v2, the Review Package, Marine Package v1.0, External Validation definitions, claims, gaps, or evidence.

The protocol distinguishes:

```text
Transport
  -> Session
  -> Execution
```

## 2. Canonical Inputs

Use files from:

```text
docs/deep_research_review_package_transport_v2/
```

The Review Guide is the package entry point. Reading Packs are the default Main Review Session corpus. Evidence Packs are accessed only through Evidence Sessions unless a specific execution record authorizes otherwise.

## 3. Execution Invariants

- Use the same frozen Transport v2 file set for every blind-review system.
- Do not modify prompts based on another reviewer's findings.
- Do not upload Review A findings to Review B.
- Do not regenerate packs between systems.
- Do not treat Deep Research as External Validation.
- Do not treat an AI system as the human External Reviewer.
- Do not claim Marine validity, Marine feasibility, deployment readiness, shipboard RUL, or Marine request readiness.

## 4. Session Model

Execution uses three session types:

1. Main Review Session: reviews all Reading Packs and produces Q1-Q8 findings.
2. Evidence Session: resolves targeted evidence requests using Evidence Packs only.
3. Reconciliation Session: merges Main Review and Evidence Session outputs without new review.

## 5. Delivery Model

Main Review Session:

1. Upload Main Profile A and send the Initial Review prompt.
2. Continue with Main Profile B.
3. Continue with Main Profile C.
4. Record pack-access status and evidence requests.

Evidence Session:

1. Open only if specific evidence is requested.
2. Upload the selected Evidence Profile.
3. Resolve only the requested finding or question.

Reconciliation Session:

1. Combine Main Review output and Evidence Session output.
2. Produce the final report without introducing new review.

## 6. SESSION_CAPACITY

`SESSION_CAPACITY` means the practical file, parser, context, and continuation capacity of one logical platform session. The protocol does not assume unlimited cumulative uploads. Capacity must be recorded as OBSERVED, MEASURED, ASSUMED, or UNKNOWN.

## 7. Pack Access Accounting

Every review output must include pack-access status:

```text
READ
PARTIALLY_READ
LOOKUP_ONLY
NOT_ACCESSED
PARSER_FAILURE
```

The reviewer must not claim complete review if a required Reading Pack is inaccessible, truncated, or not read.

## 8. Completion Boundary

This protocol prepares execution. It does not start execution. The next workstream is:

```text
DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001
```
