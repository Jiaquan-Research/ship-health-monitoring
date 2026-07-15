# Blind Review v2 Session Protocol

Document status: Protocol
Task ID: DEEP_RESEARCH_BLIND_REVIEW_SESSION_PROTOCOL_001
Applies to: DEEP_RESEARCH_REVIEW_PACKAGE_TRANSPORT_V2_001

## 1. Session Types

Blind Review v2 uses three session types:

- Main Review Session
- Evidence Session
- Reconciliation Session

Each session has a distinct purpose, input set, and stopping rule.

## 2. Main Review Session Rule

The Main Review Session is the only session that performs the primary Q1-Q8 Blind Review. It receives Reading Packs through Main Session profiles and must produce initial findings, pack-access accounting, and any evidence requests.

Evidence Packs are not mandatory Main Review Session inputs.

## 3. Evidence Session Rule

An Evidence Session may be opened only in response to a specific evidence request from the Main Review Session. It receives only the requested Evidence Packs and relevant lookup files. It resolves specific findings only.

Evidence Session outputs are evidence-resolution notes, not a new Blind Review.

## 4. Reconciliation Session Rule

The Reconciliation Session combines Main Review outputs and Evidence Session outputs. It does not inspect new packs, perform new review, or change the original session findings except to record evidence-supported resolution.

## 5. Session Capacity

`SESSION_CAPACITY` means the practical file, parser, context, and continuation capacity of one logical platform session. The protocol treats this as finite and platform-dependent.

Unless project evidence has measured a platform's capacity, capacity must be treated as unknown and managed by conservative session profiles.

## 6. Deterministic Transition

```text
Main Review Complete
  -> Evidence Needed?
     -> No: Final Report
     -> Yes: Evidence Session
             -> Evidence Findings
             -> Reconciliation Session
             -> Final Report
```

## 7. Non-Execution Boundary

This protocol defines execution structure only. It does not start Blind Review, External Validation, Marine request work, or any evidence modification.
