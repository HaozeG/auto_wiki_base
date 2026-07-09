#!/usr/bin/env python3
"""
Measure qmd retrieval quality against a labeled query -> expected-page set.

Every other quality gate in this harness (eval_summary.py, graph_stats.py,
graph_topology.py) scores *page* quality or graph shape. None of them measure
whether qmd search actually surfaces the right page for a query — the one
thing this project had no benchmark for (found by comparing against
claude-obsidian, which reports a measured +32pp top-1 accuracy / +41% error
reduction for its retrieval pipeline changes).

Usage:
    python tools/retrieval_benchmark.py tools/tests/fixtures/retrieval_benchmark_queries.json [--top 5] [--verbose]

Query set format (JSON list):
    [
      {"query": "SiFive Intelligence X280 vector width", "expected": ["sifive-intelligence-x280"]},
      ...
    ]

`expected` lists page filename stems (no path, no extension); any one of them
counting as a hit is enough for that query (use multiple entries when several
pages would be an acceptable answer).

Exit codes:
    0 — always (diagnostic tool, not a pass/fail gate)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from qmd_runner import QmdRunner


def _normalize_stem(file: str) -> str:
    """qmd normalizes filenames to kebab-case internally while disk files may
    use snake_case (see context_selector._resolve_qmd_path) -- compare on a
    hyphen/underscore-insensitive stem so that difference doesn't masquerade
    as a retrieval miss."""
    stem = Path(file.removeprefix("qmd://_pages/")).stem
    return stem.replace("-", "_")


def _is_hit(match_file: str, expected: list[str]) -> bool:
    match_stem = _normalize_stem(match_file)
    return any(match_stem == _normalize_stem(e) for e in expected)


def run_benchmark(queries: list[dict], top: int = 5,
                   qmd_runner: QmdRunner | None = None, verbose: bool = False) -> dict:
    runner = qmd_runner or QmdRunner()
    per_query: list[dict] = []

    for entry in queries:
        query = entry["query"]
        expected = entry.get("expected") or []
        result = runner.search(query, top=top, collection="_pages")

        rank_of_first_hit = None
        if result.ok:
            for match in result.matches:
                if _is_hit(match.file, expected):
                    rank_of_first_hit = match.rank
                    break

        hit_at_1 = rank_of_first_hit == 1
        hit_at_k = rank_of_first_hit is not None
        reciprocal_rank = (1.0 / rank_of_first_hit) if rank_of_first_hit else 0.0

        per_query.append({
            "query": query,
            "expected": expected,
            "ok": result.ok,
            "error": result.error,
            "rank_of_first_hit": rank_of_first_hit,
            "hit_at_1": hit_at_1,
            "hit_at_k": hit_at_k,
            "reciprocal_rank": reciprocal_rank,
        })
        if verbose:
            status = f"rank={rank_of_first_hit}" if hit_at_k else "MISS"
            print(f"  [{status}] {query!r} (expected {expected})")

    n = len(per_query)
    top1_accuracy = round(sum(1 for r in per_query if r["hit_at_1"]) / n, 4) if n else None
    recall_at_k = round(sum(1 for r in per_query if r["hit_at_k"]) / n, 4) if n else None
    mrr = round(sum(r["reciprocal_rank"] for r in per_query) / n, 4) if n else None
    failed_queries = [r["query"] for r in per_query if not r["ok"]]

    return {
        "query_count": n,
        "top": top,
        "top1_accuracy": top1_accuracy,
        f"recall_at_{top}": recall_at_k,
        "mrr": mrr,
        "failed_queries": failed_queries,
        "per_query": per_query,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Measure qmd retrieval quality against a labeled query set."
    )
    parser.add_argument("queries_path", help="Path to a JSON labeled query set")
    parser.add_argument("--top", type=int, default=5, help="How many results to check (default: 5)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show per-query results")
    args = parser.parse_args()

    path = Path(args.queries_path)
    if not path.exists():
        print(f"ERROR: query set not found: {path}", file=sys.stderr)
        sys.exit(1)
    queries = json.loads(path.read_text(encoding="utf-8"))

    stats = run_benchmark(queries, top=args.top, verbose=args.verbose)

    recall_key = f"recall_at_{stats['top']}"
    print(f"query_count: {stats['query_count']}")
    print(f"top1_accuracy: {stats['top1_accuracy']}")
    print(f"{recall_key}: {stats[recall_key]}")
    print(f"mrr: {stats['mrr']}")
    if stats["failed_queries"]:
        print(f"failed_queries ({len(stats['failed_queries'])}): {stats['failed_queries']}")


if __name__ == "__main__":
    main()
