# Deep Research Review Transport v2 Architecture

Document status: Implementation Reference
Task ID: DEEP_RESEARCH_REVIEW_TRANSPORT_V2_BUILD_001
Source package: DEEP_RESEARCH_REVIEW_PACKAGE_001 v1.1

## 1. Purpose

Transport v2 is a reader-oriented transport architecture for the locked Deep Research Review Package. It preserves authoritative project artifacts byte-for-byte while separating reading, lookup, and integrity functions.

Transport v2 does not summarize, rewrite, reinterpret, correct, or replace any authoritative project artifact.

## 2. Design Rationale

Transport v1 prioritized byte recovery and cryptographic verification in large bundles. That made verification strong but placed repeated metadata and machine-oriented artifacts in the default reading path. Transport v2 keeps deterministic recovery while making the default interface easier for LLM systems to parse and navigate.

## 3. Layer Responsibilities

Layer 0, Research Brief: retains the governing review instructions unchanged from the locked v1.1 package.

Layer A, Review Guide and Pack Index: provides the package entry point, pack inventory, Q1-Q8 routing, document coverage, parser-failure protocol, and pack-access declaration template.

Layer B, Reading Packs: contains narrative, governance, boundary, closure, audit, and interpretation documents expected to be read directly.

Layer C, Evidence Packs: contains machine-oriented CSV/JSON files, large tables, numerical artifacts, and targeted lookup evidence.

Layer D, Lookup Index: provides navigation files for document IDs, claims, gaps, datasets, review questions, and artifact lookup.

Layer E, Integrity Manifest: records SHA-256 values, byte lengths, content offsets, part metadata, and reconstruction metadata.

## 4. Implementation Strategy

The builder reads `docs/deep_research_review_package/deep_research_review_package_manifest.json`, excludes the Research Brief from source-document packing, and assigns stable document IDs `DOC-001` through `DOC-036` in manifest order.

Reading and Evidence Pack allocation is deterministic. CSV and JSON files, the Evidence Map, the Artifact Index, and numerical-support artifacts are routed to Evidence Packs. Other narrative and governance documents are routed to Reading Packs by topic and source order.

Source content is inserted inside minimal document wrappers. Integrity metadata is kept in `integrity/transport_v2_integrity_manifest.json`.

## 5. Migration From Transport v1

Transport v1 remains archived and untouched. Transport v2 is generated under `docs/deep_research_review_package_transport_v2/` and does not overwrite v1 bundle files or the v1 transport manifest.

## 6. Directory Organization

```text
docs/deep_research_review_package_transport_v2/
  deep_research_review_brief.md
  transport_v2_architecture.md
  00_review_guide_and_pack_index.md
  reading/
  evidence/
  lookup/
  integrity/
  scripts/
  transport_v2_build_summary.md
```

## 7. Boundary

This architecture changes only the delivery form for LLM Blind Review. It does not modify Marine Package v1.0, External Validation definitions, claims, gaps, evidence strength, Marine validity, Marine feasibility, or any process state.
