#!/usr/bin/env python3
"""
Compute small-world graph-topology statistics from wiki page frontmatter.

Usage:
    python tools/graph_topology.py wiki/_pages/ [--verbose]

Implements the measurement side of CLAUDE.md's Graph Topology Philosophy:
clustering coefficient and average shortest path length (Watts-Strogatz
small-world properties), plus deterministic degree/betweenness centrality as
a non-subjective counterpart to the LLM-assigned `bridge_score`/`hub_potential`
scorecard fields.

Builds the graph from each page's `outbound_links` frontmatter field (see
relationship_links.py) — pages without that field are treated as
topologically orphaned, same as graph_stats.py's `inbound_links`-based view.
This module is deliberately additive to graph_stats.py, not a replacement:
`orphan_fraction`/`median_inbound_links` remain a cheap early-cold-start
signal; clustering_coefficient/avg_path_length are only meaningful once
enough pages carry real edges.

Exit codes:
    0 — success (always)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import networkx as nx

from frontmatter import parse_frontmatter


def build_graph(pages_dir: Path) -> nx.DiGraph:
    """Build a directed graph: node per page (by filename stem), edge per
    `outbound_links` entry whose target resolves to another page in the wiki."""
    md_files = list(pages_dir.rglob("*.md"))
    stems = {f.stem for f in md_files}

    graph = nx.DiGraph()
    graph.add_nodes_from(stems)

    for f in md_files:
        fm = parse_frontmatter(f)
        for edge in (fm.get("outbound_links") or []):
            if not isinstance(edge, dict):
                continue
            target = str(edge.get("target", "")).strip()
            if not target or target not in stems or target == f.stem:
                continue
            graph.add_edge(f.stem, target, reason=str(edge.get("reason", "unlabeled")))

    return graph


def compute_topology_stats(pages_dir: Path, verbose: bool = False) -> dict:
    """Compute small-world topology stats. Returns a dict with graph-level
    numbers plus per-page degree/betweenness centrality."""
    graph = build_graph(pages_dir)
    undirected = graph.to_undirected()

    page_count = graph.number_of_nodes()
    if page_count == 0:
        return {
            "page_count": 0,
            "edge_count": 0,
            "clustering_coefficient": 0.0,
            "avg_path_length": None,
            "connected_components": 0,
            "largest_component_size": 0,
            "topologically_orphaned_fraction": 1.0,
        }

    edge_count = graph.number_of_edges()
    clustering_coefficient = round(nx.average_clustering(undirected), 4)

    components = list(nx.connected_components(undirected))
    connected_components = len(components)
    largest = max(components, key=len) if components else set()
    largest_component_size = len(largest)

    avg_path_length = None
    if largest_component_size > 1:
        largest_subgraph = undirected.subgraph(largest)
        avg_path_length = round(nx.average_shortest_path_length(largest_subgraph), 4)

    isolated = sum(1 for n in undirected.nodes if undirected.degree(n) == 0)
    topologically_orphaned_fraction = round(isolated / page_count, 4)

    degree_centrality = {k: round(v, 4) for k, v in nx.degree_centrality(undirected).items()}
    betweenness_centrality = {k: round(v, 4) for k, v in nx.betweenness_centrality(undirected).items()}

    if verbose:
        for node in sorted(undirected.nodes):
            print(f"  {node}: degree={degree_centrality[node]} "
                  f"betweenness={betweenness_centrality[node]}")

    return {
        "page_count": page_count,
        "edge_count": edge_count,
        "clustering_coefficient": clustering_coefficient,
        "avg_path_length": avg_path_length,
        "connected_components": connected_components,
        "largest_component_size": largest_component_size,
        "topologically_orphaned_fraction": topologically_orphaned_fraction,
        "degree_centrality": degree_centrality,
        "betweenness_centrality": betweenness_centrality,
    }


def find_bridge_candidates(pages_dir: Path, max_candidates: int = 5) -> list[dict]:
    """Identify pairs of topologically distant pages — in separate connected
    components — as candidate bridge topics for the research/discovery step.

    This is the proactive half of the Graph Topology Philosophy: surface
    distant clusters as research *context* so new pages are chosen to bridge
    them, instead of reactively linking pages that already exist after the
    fact (the pattern that produced hub inflation in close_linking_debt.py).

    Returns up to max_candidates ``{page_a, page_b, component_size_a,
    component_size_b, reason}`` dicts. The largest component's best-connected
    page is paired against a representative of each smaller component,
    smallest components first (most orphaned, so most worth bridging).
    """
    graph = build_graph(pages_dir).to_undirected()
    components = sorted(nx.connected_components(graph), key=len, reverse=True)
    if len(components) < 2:
        return []

    def representative(component: set) -> str | None:
        if not component:
            return None
        return max(component, key=lambda n: graph.degree(n))

    largest = components[0]
    anchor = representative(largest)
    if anchor is None:
        return []

    candidates = []
    for component in reversed(components[1:]):  # smallest components first
        rep = representative(component)
        if rep is None:
            continue
        candidates.append({
            "page_a": anchor,
            "page_b": rep,
            "component_size_a": len(largest),
            "component_size_b": len(component),
            "reason": (
                f"separate connected components ({len(largest)} vs {len(component)} "
                f"pages) — no path between them in the current graph"
            ),
        })
        if len(candidates) >= max_candidates:
            break
    return candidates


def check_for_goodharting(before: dict, after: dict,
                           orphan_drop_threshold: float = 0.15,
                           path_length_improvement_threshold: float = 0.05) -> str | None:
    """Diagnostic guardrail against the failure mode found in the v2 replication
    run: a linking pass that drops orphan_fraction sharply via generic-token
    reciprocal links, without genuinely shortening the graph or improving local
    clustering. Compares topology snapshots taken before/after a linking pass.

    Returns a warning string if the pass looks like a Goodharted metric push
    rather than genuine bridging, else None. Callers (e.g. a future linking
    script) should log this to wiki/log.md for human review rather than
    silently accepting the pass.
    """
    before_orphan = before.get("topologically_orphaned_fraction", 1.0)
    after_orphan = after.get("topologically_orphaned_fraction", 1.0)
    orphan_drop = before_orphan - after_orphan

    if orphan_drop < orphan_drop_threshold:
        return None  # no meaningful connectivity change to evaluate

    clustering_drop = before.get("clustering_coefficient", 0.0) - after.get("clustering_coefficient", 0.0)

    before_path = before.get("avg_path_length")
    after_path = after.get("avg_path_length")
    path_improved = (
        before_path is not None and after_path is not None
        and (before_path - after_path) >= path_length_improvement_threshold
    )

    if clustering_drop > 0 and not path_improved:
        return (
            f"SUSPECTED GOODHARTING: topologically_orphaned_fraction dropped by "
            f"{orphan_drop:.3f} but clustering_coefficient fell by {clustering_drop:.3f} "
            f"and avg_path_length did not meaningfully improve "
            f"({before_path} -> {after_path}). This matches the hub-inflation pattern "
            f"seen with generic-token reciprocal linking — review new outbound_links "
            f"edges for genuine topical relevance before accepting this pass."
        )
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Compute small-world graph-topology statistics from page frontmatter."
    )
    parser.add_argument(
        "pages_dir",
        nargs="?",
        default="wiki/_pages",
        help="Directory containing wiki pages (default: wiki/_pages)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Show per-page centrality")
    args = parser.parse_args()

    pages_dir = Path(args.pages_dir)
    if not pages_dir.exists():
        print(f"ERROR: directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    stats = compute_topology_stats(pages_dir, verbose=args.verbose)

    print(f"page_count: {stats['page_count']}")
    print(f"edge_count: {stats['edge_count']}")
    print(f"clustering_coefficient: {stats['clustering_coefficient']}")
    print(f"avg_path_length (largest component): {stats['avg_path_length']}")
    print(f"connected_components: {stats['connected_components']}")
    print(f"largest_component_size: {stats['largest_component_size']}")
    print(f"topologically_orphaned_fraction: {stats['topologically_orphaned_fraction']}")


if __name__ == "__main__":
    main()
