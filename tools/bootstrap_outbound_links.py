#!/usr/bin/env python3
"""
One-time bootstrap: seed `outbound_links` frontmatter for pages written before
that field existed, by parsing their existing Relationships/Connected Pages
body text (see relationship_links.py).

This is a migration, not an ongoing dependency — going forward, _write_page()
in orchestrator.py populates outbound_links automatically at write time.
Pages already carrying outbound_links are left untouched.

Per the plan's guardrail (and the close_linking_debt.py precedent), this is a
reviewed, spot-checked pass: it defaults to --dry-run and prints a diff-like
summary; pass --apply to actually write.

Usage:
    python tools/bootstrap_outbound_links.py wiki/_pages/          # dry run
    python tools/bootstrap_outbound_links.py wiki/_pages/ --apply  # write
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import frontmatter
from relationship_links import extract_outbound_links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages_dir", nargs="?", default="wiki/_pages")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry run)")
    args = parser.parse_args()

    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    touched = 0
    skipped_already_has = 0
    skipped_no_links = 0

    for path in sorted(pages_dir.rglob("*.md")):
        fm, body = frontmatter.parse_page(path)
        if not fm:
            continue
        if fm.get("outbound_links"):
            skipped_already_has += 1
            continue

        links = extract_outbound_links(body)
        if not links:
            skipped_no_links += 1
            continue

        touched += 1
        rel = path.relative_to(pages_dir)
        print(f"{rel}: +{len(links)} outbound_links")
        for link in links:
            print(f"    -> {link['target']}  ({link['reason']})")

        if args.apply:
            fm["outbound_links"] = links
            frontmatter.write_page(path, fm, body)

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"\n[{mode}] {touched} pages seeded, {skipped_already_has} already had "
          f"outbound_links, {skipped_no_links} had no parseable Relationships links.")
    if not args.apply and touched:
        print("Re-run with --apply after reviewing the list above.")


if __name__ == "__main__":
    main()
