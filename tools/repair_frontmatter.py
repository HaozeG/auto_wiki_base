#!/usr/bin/env python3
"""One-time repair script: fix accumulated dashes in frontmatter closing delimiter.

Bug: _increment_frontmatter_field wrote f"---\n{yaml}---{body}" where body
already starts with "---". Each increment added 3 dashes. After n increments
the closing delimiter becomes 3+3n dashes. This script normalises it back to "---".

Run from repo root: uv run --no-sync python tools/repair_frontmatter.py
"""
import re
from pathlib import Path

PAGES_DIR = Path("wiki/_pages")


def repair_page(page: Path) -> bool:
    text = page.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    # Find the first line that consists solely of 3+ dashes (the closing delimiter)
    fixed = re.sub(r"\n(-{3,})\n", "\n---\n", text, count=1)
    if fixed == text:
        return False
    page.write_text(fixed, encoding="utf-8")
    return True


repaired = []
for page in sorted(PAGES_DIR.rglob("*.md")):
    if repair_page(page):
        repaired.append(page)

if repaired:
    print(f"Repaired {len(repaired)} pages:")
    for p in repaired:
        print(f"  {p}")
else:
    print("No pages needed repair.")
