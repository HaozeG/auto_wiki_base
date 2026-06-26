#!/usr/bin/env python3
"""
Compute graph statistics from wiki page frontmatter.

Usage:
    python tools/graph_stats.py wiki/_pages/ [--verbose]

Reads all .md files recursively under the given directory, extracts the
`inbound_links` field from YAML frontmatter, and computes the mean.
Prints the result and exits with a message about graph maturity threshold.

Exit codes:
    0 — success (always, even if below threshold)
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

MATURITY_THRESHOLD = 2.0


def parse_frontmatter(path: Path) -> dict:
    """Return the YAML frontmatter dict from a markdown file, or {} on failure."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end].strip()) or {}
    except yaml.YAMLError:
        return {}


def compute_stats(pages_dir: Path, verbose: bool = False) -> dict:
    """
    Walk pages_dir recursively, collect inbound_links values, return stats dict.
    """
    md_files = list(pages_dir.rglob("*.md"))
    if not md_files:
        return {
            "page_count": 0,
            "mean_inbound_links": 0.0,
            "above_maturity_threshold": False,
            "maturity_threshold": MATURITY_THRESHOLD,
        }

    inbound_values = []
    for f in md_files:
        fm = parse_frontmatter(f)
        val = fm.get("inbound_links")
        if isinstance(val, (int, float)):
            inbound_values.append(float(val))
            if verbose:
                print(f"  {f.relative_to(pages_dir)}: inbound_links={val}")

    if not inbound_values:
        mean = 0.0
    else:
        mean = sum(inbound_values) / len(inbound_values)

    return {
        "page_count": len(md_files),
        "pages_with_inbound_links": len(inbound_values),
        "mean_inbound_links": round(mean, 4),
        "above_maturity_threshold": mean > MATURITY_THRESHOLD,
        "maturity_threshold": MATURITY_THRESHOLD,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute wiki graph statistics from page frontmatter."
    )
    parser.add_argument(
        "pages_dir",
        nargs="?",
        default="wiki/_pages",
        help="Directory containing wiki pages (default: wiki/_pages)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Show per-page data")
    args = parser.parse_args()

    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    stats = compute_stats(pages_dir, verbose=args.verbose)

    print(f"page_count: {stats['page_count']}")
    print(f"pages_with_inbound_links: {stats.get('pages_with_inbound_links', 0)}")
    print(f"mean_inbound_links: {stats['mean_inbound_links']}")

    if stats["above_maturity_threshold"]:
        print(
            f"STATUS: MATURE — mean_inbound_links ({stats['mean_inbound_links']}) "
            f"> threshold ({MATURITY_THRESHOLD}). Set graph_maturity: true in CLAUDE.md."
        )
    else:
        print(
            f"STATUS: COLD_START — mean_inbound_links ({stats['mean_inbound_links']}) "
            f"<= threshold ({MATURITY_THRESHOLD})."
        )


if __name__ == "__main__":
    main()
