#!/usr/bin/env python3
"""Check critical state consistency across public entry documents.

Usage:
    python scripts/repository_governance/check_state_consistency.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FILES = {
    "SYSTEM_STATE": ROOT / "SYSTEM_STATE.md",
    "PUBLISHING_STATUS": ROOT / "PUBLISHING_STATUS.md",
    "README": ROOT / "README.md",
    "CLAUDE": ROOT / "CLAUDE.md",
}

CHECKS = [
    ("Marine Package complete/frozen", [r"Marine Package v1\.0.*complete and frozen", r"Marine Package v1\.0: complete and frozen"]),
    ("External Validation not started", [r"External Validation execution:\s*`?NOT_STARTED`?", r"External Validation execution:\s*not started", r"External Validation.*not started"]),
    ("External reviewer not selected", [r"External reviewer:\s*`?NOT_SELECTED`?", r"external reviewer.*not selected", r"External reviewer:\s*not selected"]),
    ("Blind Review not started", [r"Blind Review execution:\s*not started", r"Deep Research Blind Review execution:\s*not started"]),
    ("Marine data request planned/not started", [r"Marine data request:\s*`?PLANNED_NOT_STARTED`?", r"Marine data request:\s*planned, not started"]),
    ("Marine validation not started", [r"Marine validation:\s*Not started", r"Marine validation:\s*not started"]),
    ("Deployment readiness not demonstrated", [r"Deployment readiness:\s*Not demonstrated", r"deployment readiness", r"Deployment readiness"]),
    ("Next authorized workstream", [r"DEEP_RESEARCH_BLIND_REVIEW_V2_EXECUTION_001"]),
]

CONTRADICTIONS = [
    ("Marine validity overclaim", r"Marine validity (has been )?(is )?(established|validated|claimed)"),
    ("External Validation started/completed", r"External Validation (has )?(started|completed)"),
    ("Reviewer selected", r"External reviewer (has been )?selected"),
    ("Marine data received", r"Marine data (has been )?received"),
    ("Deployment readiness demonstrated", r"Deployment readiness (has been )?demonstrated"),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) for pattern in patterns)


def main() -> int:
    texts = {name: read(path) for name, path in FILES.items()}
    errors: list[str] = []
    authority = texts["SYSTEM_STATE"]

    for label, patterns in CHECKS:
        if not has_any(authority, patterns):
            errors.append(f"SYSTEM_STATE missing authority declaration: {label}")
        for name, text in texts.items():
            if name == "SYSTEM_STATE":
                continue
            if not has_any(text, patterns):
                errors.append(f"{name} missing or unclear state: {label}")

    for name, text in texts.items():
        for label, pattern in CONTRADICTIONS:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                context = text[max(0, match.start() - 500) : match.end() + 120]
                lowered = context.lower()
                if (
                    "not " not in lowered
                    and "do not" not in lowered
                    and "does not" not in lowered
                    and "do not state or imply" not in lowered
                ):
                    errors.append(f"{name} possible contradiction: {label}: {match.group(0)}")

    if errors:
        print("State consistency: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    print("State consistency: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
