#!/usr/bin/env python3
"""One-shot: backfill canonical_name / aliases on existing wiki pages.

Identity resolution (see identity.py) needs ``canonical_name`` populated on
existing pages, or the registry is empty and every candidate resolves to
``create``. This is a no-op for a fresh wiki (main's empty template) and a
one-time migration for an already-populated wiki.

Usage:
    python tools/backfill_identity.py wiki/_pages [--dry-run]
"""

import argparse
import sys
from pathlib import Path

import frontmatter


def _title_from_body(body: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def backfill(pages_dir: Path, dry_run: bool = False) -> dict:
    updated = skipped = 0
    for path in sorted(pages_dir.rglob("*.md")):
        fm, body = frontmatter.parse_page(path)
        if not fm or fm.get("canonical_name"):
            skipped += 1
            continue
        title = _title_from_body(body) or path.stem.replace("_", " ")
        stem_alias = path.stem.replace("_", " ")
        aliases = []
        if stem_alias and stem_alias.lower() != title.lower():
            aliases.append(stem_alias)
        if dry_run:
            print(f"[dry-run] {path.name}: canonical_name={title!r} aliases={aliases}")
        else:
            frontmatter.set_page_field(path, "canonical_name", title)
            if aliases and not fm.get("aliases"):
                frontmatter.set_page_field(path, "aliases", aliases)
        updated += 1
    return {"updated": updated, "skipped": skipped}


def main():
    ap = argparse.ArgumentParser(description="Backfill canonical_name/aliases on wiki pages.")
    ap.add_argument("pages_dir", nargs="?", default="wiki/_pages")
    ap.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    args = ap.parse_args()
    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)
    summary = backfill(pages_dir, dry_run=args.dry_run)
    print(f"backfill: {summary}")


if __name__ == "__main__":
    main()
