#!/usr/bin/env python3
"""
Compute graph statistics from wiki page frontmatter.

Usage:
    python tools/graph_stats.py wiki/_pages/ [--verbose]

Reads all .md files recursively under the given directory and computes
connectivity stats from the `inbound_links` and `outbound_links` frontmatter
fields.

This module used to also compute a `graph_maturity` pass/fail verdict. It was
removed: three different formulas were tried in turn --
  - mean_inbound_links: gameable, a couple of hub pages lift it past any
    threshold while most pages stay disconnected.
  - median_inbound_links (inbound-only): structurally could never reach 1 in
    a hub-and-spoke wiki, since most pages cite rather than get cited -- it
    never flipped even at 100+ pages, not because the wiki wasn't connected
    but because citing and being cited are different things.
  - median_total_links (inbound + outbound): flips almost immediately, the
    moment linking works at all -- it measures "is linking functioning", not
    "is this wiki established".
Graph degree kept being the wrong instrument for "mature vs nascent" no
matter which direction or normalization was tried. The orphan_fraction/
median_total_links/mean_total_links numbers below remain useful connectivity
diagnostics on their own terms -- they're just no longer collapsed into a
verdict or wired to a state transition.

Exit codes:
    0 — success (always)
"""

import argparse
import sys
from pathlib import Path

from frontmatter import parse_frontmatter


def _median(values: list[float]) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def compute_stats(pages_dir: Path, verbose: bool = False, exclude_hubs_above: int = 0) -> dict:
    """
    Walk pages_dir recursively, collect inbound_links/outbound_links values,
    return stats dict.

    exclude_hubs_above: if > 0, pages with inbound_links > this value are excluded
      from the inbound mean/median computation to avoid hub distortion.
    """
    md_files = list(pages_dir.rglob("*.md"))
    if not md_files:
        return {
            "page_count": 0,
            "mean_inbound_links": 0.0,
            "median_inbound_links": 0.0,
            "mean_total_links": 0.0,
            "median_total_links": 0.0,
            "orphan_fraction": 1.0,
            "orphan_count": 0,
        }

    inbound_values = []
    total_values = []
    for f in md_files:
        fm = parse_frontmatter(f)
        inbound = fm.get("inbound_links")
        inbound = float(inbound) if isinstance(inbound, (int, float)) else 0.0
        outbound = fm.get("outbound_links")
        outbound_count = float(len(outbound)) if isinstance(outbound, list) else 0.0
        inbound_values.append(inbound)
        total_values.append(inbound + outbound_count)
        if verbose:
            print(f"  {f.relative_to(pages_dir)}: inbound_links={inbound:g} "
                  f"outbound_links={outbound_count:g}")

    mean_inbound = sum(inbound_values) / len(inbound_values)
    median_inbound = _median(inbound_values)
    mean_total = sum(total_values) / len(total_values)
    median_total = _median(total_values)

    # Hub-excluded inbound stats if requested (informational only).
    if exclude_hubs_above > 0:
        non_hub = [v for v in inbound_values if v <= exclude_hubs_above]
        hub_count = len(inbound_values) - len(non_hub)
        excl_mean = sum(non_hub) / len(non_hub) if non_hub else 0.0
        excl_median = _median(non_hub)
    else:
        hub_count = 0
        excl_mean = excl_median = None

    # Orphan = zero total degree (no inbound AND no outbound), not inbound-only:
    # a page that cites others is connected to the graph even before anything
    # cites it back. See module docstring.
    orphan_count = sum(1 for v in total_values if v == 0)
    orphan_fraction = orphan_count / len(total_values)

    return {
        "page_count": len(md_files),
        "pages_with_inbound_links": len(inbound_values),
        "mean_inbound_links": round(mean_inbound, 4),
        "median_inbound_links": round(median_inbound, 4),
        "mean_total_links": round(mean_total, 4),
        "median_total_links": round(median_total, 4),
        "orphan_count": orphan_count,
        "orphan_fraction": round(orphan_fraction, 4),
        "hubs_excluded": hub_count,
        "excl_mean_inbound_links": round(excl_mean, 4) if excl_mean is not None else None,
        "excl_median_inbound_links": round(excl_median, 4) if excl_median is not None else None,
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
    parser.add_argument("--exclude-hubs", type=int, default=0, metavar="N",
                        help="Exclude pages with inbound_links > N from stats (0 = include all)")
    args = parser.parse_args()

    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    stats = compute_stats(pages_dir, verbose=args.verbose, exclude_hubs_above=args.exclude_hubs)

    print(f"page_count: {stats['page_count']}")
    print(f"mean_inbound_links: {stats['mean_inbound_links']} (informational — citation concentration)")
    print(f"median_inbound_links: {stats['median_inbound_links']} (informational — citation concentration)")
    print(f"mean_total_links: {stats['mean_total_links']}")
    print(f"median_total_links: {stats['median_total_links']}")
    print(f"orphan_count: {stats.get('orphan_count', 0)}")
    print(f"orphan_fraction: {stats.get('orphan_fraction', 1.0)}")
    if args.exclude_hubs > 0:
        print(f"hubs_excluded (>{args.exclude_hubs} inbound links): {stats['hubs_excluded']}")
        print(f"excl_mean_inbound_links: {stats['excl_mean_inbound_links']}")
        print(f"excl_median_inbound_links: {stats['excl_median_inbound_links']}")


if __name__ == "__main__":
    main()
