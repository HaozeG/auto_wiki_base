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


def compute_stats(pages_dir: Path, verbose: bool = False,
                  use_median: bool = False, exclude_hubs_above: int = 0) -> dict:
    """
    Walk pages_dir recursively, collect inbound_links values, return stats dict.

    exclude_hubs_above: if > 0, pages with inbound_links > this value are excluded
      from the mean/median computation to avoid hub distortion.
    use_median: compute median instead of mean.
    """
    md_files = list(pages_dir.rglob("*.md"))
    if not md_files:
        return {
            "page_count": 0,
            "mean_inbound_links": 0.0,
            "median_inbound_links": 0.0,
            "above_maturity_threshold": False,
            "maturity_threshold": MATURITY_THRESHOLD,
        }

    all_values = []
    hub_count = 0
    for f in md_files:
        fm = parse_frontmatter(f)
        val = fm.get("inbound_links")
        if isinstance(val, (int, float)):
            all_values.append(float(val))
            if verbose:
                print(f"  {f.relative_to(pages_dir)}: inbound_links={val}")

    if not all_values:
        mean = median = 0.0
    else:
        mean = sum(all_values) / len(all_values)
        sorted_vals = sorted(all_values)
        n = len(sorted_vals)
        median = (sorted_vals[n // 2] if n % 2 else
                  (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2)

    # Compute hub-excluded stats if requested
    if exclude_hubs_above > 0:
        non_hub = [v for v in all_values if v <= exclude_hubs_above]
        hub_count = len(all_values) - len(non_hub)
        if non_hub:
            excl_mean = sum(non_hub) / len(non_hub)
            s = sorted(non_hub)
            n = len(s)
            excl_median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
        else:
            excl_mean = excl_median = 0.0
    else:
        excl_mean = excl_median = None

    primary = median if use_median else mean

    return {
        "page_count": len(md_files),
        "pages_with_inbound_links": len(all_values),
        "mean_inbound_links": round(mean, 4),
        "median_inbound_links": round(median, 4),
        "hubs_excluded": hub_count,
        "excl_mean_inbound_links": round(excl_mean, 4) if excl_mean is not None else None,
        "excl_median_inbound_links": round(excl_median, 4) if excl_median is not None else None,
        "above_maturity_threshold": primary > MATURITY_THRESHOLD,
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
    parser.add_argument("--median", action="store_true",
                        help="Use median (instead of mean) for maturity threshold comparison")
    parser.add_argument("--exclude-hubs", type=int, default=0, metavar="N",
                        help="Exclude pages with inbound_links > N from stats (0 = include all)")
    args = parser.parse_args()

    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    stats = compute_stats(pages_dir, verbose=args.verbose,
                          use_median=args.median, exclude_hubs_above=args.exclude_hubs)

    print(f"page_count: {stats['page_count']}")
    print(f"pages_with_inbound_links: {stats.get('pages_with_inbound_links', 0)}")
    print(f"mean_inbound_links: {stats['mean_inbound_links']}")
    print(f"median_inbound_links: {stats['median_inbound_links']}")
    if args.exclude_hubs > 0:
        print(f"hubs_excluded (>{args.exclude_hubs} links): {stats['hubs_excluded']}")
        print(f"excl_mean_inbound_links: {stats['excl_mean_inbound_links']}")
        print(f"excl_median_inbound_links: {stats['excl_median_inbound_links']}")

    primary_label = "median" if args.median else "mean"
    primary_val = stats["median_inbound_links"] if args.median else stats["mean_inbound_links"]

    if stats["above_maturity_threshold"]:
        print(
            f"STATUS: MATURE — {primary_label}_inbound_links ({primary_val}) "
            f"> threshold ({MATURITY_THRESHOLD}). Set graph_maturity: true in CLAUDE.md."
        )
    else:
        print(
            f"STATUS: COLD_START — {primary_label}_inbound_links ({primary_val}) "
            f"<= threshold ({MATURITY_THRESHOLD})."
        )


if __name__ == "__main__":
    main()
