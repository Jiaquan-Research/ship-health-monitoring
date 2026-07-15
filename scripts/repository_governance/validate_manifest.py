#!/usr/bin/env python3
"""Validate repository governance manifests.

Usage:
    python scripts/repository_governance/validate_manifest.py
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPO_MANIFEST = ROOT / "manifest" / "repository_manifest.json"
PUBLIC_MANIFEST = ROOT / "manifest" / "public_manifest.json"
MACHINE_MANIFEST = ROOT / "manifest" / "machine_retrieval_manifest.json"

REQUIRED_FIELDS = {
    "document_id",
    "path",
    "title",
    "project_scope",
    "document_class",
    "authority_level",
    "lifecycle_state",
    "audience",
    "public_visibility",
    "retrieval_priority",
    "copy_role",
    "canonical_source",
    "canonical_successor",
    "hash",
    "last_reviewed",
    "notes",
}

VOCABS = {
    "document_class": {
        "STATE",
        "PUBLIC_ENTRY",
        "NAVIGATION",
        "GOVERNANCE",
        "SCIENTIFIC_SOURCE",
        "PACKAGE",
        "PROTOCOL",
        "EXECUTION_INTERFACE",
        "REVIEW",
        "ARCHITECTURE",
        "DECISION",
        "SPECIFICATION",
        "HISTORICAL_NOTE",
    },
    "authority_level": {
        "REPOSITORY_STATE_AUTHORITY",
        "SCOPE_AUTHORITY",
        "DERIVED_SUMMARY",
        "NAVIGATION_ONLY",
        "OPERATOR_CONTEXT",
        "DELIVERY_INTERFACE",
        "NON_AUTHORITATIVE",
    },
    "lifecycle_state": {
        "DRAFT",
        "REVIEWED",
        "APPROVED",
        "FROZEN",
        "ACTIVE_APPEND_ONLY",
        "SUPERSEDED",
        "ARCHIVED",
        "HISTORICAL_NOTE",
    },
    "audience": {"PUBLIC", "OPERATOR", "REVIEWER", "AI_AGENT", "INTERNAL", "MIXED"},
    "public_visibility": {
        "PUBLIC",
        "PUBLIC_WITH_BOUNDARIES",
        "INTERNAL",
        "ARCHIVE_ONLY",
        "REVIEW_PACKAGE_ONLY",
    },
    "copy_role": {
        "SOURCE",
        "DERIVED_SUMMARY",
        "TRANSPORT_COPY",
        "EXECUTION_COPY",
        "WEBSITE_DERIVATIVE",
        "NAVIGATION_RECORD",
    },
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def validate() -> list[str]:
    errors: list[str] = []
    repo = load_json(REPO_MANIFEST)
    public = load_json(PUBLIC_MANIFEST)
    machine = load_json(MACHINE_MANIFEST)
    entries = repo.get("entries", [])
    by_id = {}
    by_path = {}

    for index, entry in enumerate(entries, start=1):
        missing = REQUIRED_FIELDS - set(entry)
        if missing:
            errors.append(f"entry {index} missing fields: {sorted(missing)}")
            continue

        doc_id = entry["document_id"]
        rel_path = entry["path"]
        if doc_id in by_id:
            errors.append(f"duplicate document_id: {doc_id}")
        by_id[doc_id] = entry
        if rel_path in by_path:
            errors.append(f"duplicate path: {rel_path}")
        by_path[rel_path] = entry

        for field, allowed in VOCABS.items():
            if entry[field] not in allowed:
                errors.append(f"{doc_id}: invalid {field}: {entry[field]}")

        priority = entry["retrieval_priority"]
        if not isinstance(priority, int) or not 1 <= priority <= 5:
            errors.append(f"{doc_id}: retrieval_priority must be integer 1-5")

        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"{doc_id}: missing path: {rel_path}")
        else:
            actual = sha256(path)
            if actual != entry["hash"]:
                errors.append(f"{doc_id}: hash mismatch manifest={entry['hash']} actual={actual}")

        for ref_field in ("canonical_source", "canonical_successor"):
            ref = entry.get(ref_field)
            if ref and ref not in by_path and not (ROOT / ref).exists():
                errors.append(f"{doc_id}: {ref_field} target does not exist: {ref}")

        if entry["copy_role"] in {"TRANSPORT_COPY", "EXECUTION_COPY", "WEBSITE_DERIVATIVE"}:
            if entry["authority_level"] in {"REPOSITORY_STATE_AUTHORITY", "SCOPE_AUTHORITY"}:
                errors.append(f"{doc_id}: generated copy cannot be state or scope authority")
            if entry["document_class"] == "SCIENTIFIC_SOURCE":
                errors.append(f"{doc_id}: generated copy cannot be scientific source")

    if "ROOT-SYSTEM-STATE" not in by_id:
        errors.append("SYSTEM_STATE.md entry missing")
    elif by_id["ROOT-SYSTEM-STATE"]["authority_level"] != "REPOSITORY_STATE_AUTHORITY":
        errors.append("SYSTEM_STATE.md must be REPOSITORY_STATE_AUTHORITY")

    public_ids = {entry["document_id"] for entry in public.get("entries", [])}
    for entry in public.get("entries", []):
        if entry["document_id"] not in by_id:
            errors.append(f"public manifest entry missing from repository manifest: {entry['document_id']}")
        if entry["public_visibility"] in {"INTERNAL", "ARCHIVE_ONLY", "REVIEW_PACKAGE_ONLY"}:
            errors.append(f"public manifest exposes non-public entry: {entry['document_id']}")

    expected_public_ids = {
        entry["document_id"]
        for entry in entries
        if entry["public_visibility"] in {"PUBLIC", "PUBLIC_WITH_BOUNDARIES"}
    }
    if public_ids != expected_public_ids:
        errors.append("public manifest is not the expected public subset")

    machine_ids = {entry["document_id"] for entry in machine.get("entries", [])}
    repo_ids = set(by_id)
    if machine_ids != repo_ids:
        errors.append("machine retrieval manifest entries do not match repository manifest entries")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Manifest validation: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    print("Manifest validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
