#!/usr/bin/env python3
"""Validate repository-relative Markdown links in core public/governance docs.

Usage:
    python scripts/repository_governance/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS = [
    "README.md",
    "SYSTEM_STATE.md",
    "PUBLISHING_STATUS.md",
    "CLAUDE.md",
    "docs/documentation_map.md",
    "manifest/README.md",
    "docs/governance/repository_governance_policy.md",
    "docs/governance/publishing_policy.md",
    "docs/governance/machine_retrieval_policy.md",
    "docs/website/website_content_map.md",
    "docs/repository_review/repository_publishing_review.md",
    "docs/repository_review/repository_governance_review.md",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def target_exists(source: Path, href: str) -> bool:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return True
    href = href.split("#", 1)[0]
    if not href:
        return True
    href = href.replace("%20", " ")
    target = (source.parent / href).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return False
    return target.exists()


def main() -> int:
    errors: list[str] = []
    for rel in DOCS:
        source = ROOT / rel
        if not source.exists():
            errors.append(f"missing checked document: {rel}")
            continue
        text = source.read_text(encoding="utf-8-sig")
        for match in LINK_RE.finditer(text):
            href = match.group(1).strip()
            if not target_exists(source, href):
                errors.append(f"{rel}: broken link: {href}")
    if errors:
        print("Link check: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    print("Link check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
