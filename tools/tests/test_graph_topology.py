import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import frontmatter
import graph_topology


def _write(pages_dir: Path, subdir: str, stem: str, outbound_links=None):
    d = pages_dir / subdir
    d.mkdir(parents=True, exist_ok=True)
    fm = {"type": "entity", "outbound_links": outbound_links or []}
    frontmatter.write_page(d / f"{stem}.md", fm, f"\n# {stem}\n\nBody.\n")


def test_build_graph_creates_node_per_page_and_edge_per_outbound_link(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "a", [{"target": "b", "reason": "r"}])
    _write(pages_dir, "entity", "b", [])
    _write(pages_dir, "entity", "c", [])

    graph = graph_topology.build_graph(pages_dir)
    assert set(graph.nodes) == {"a", "b", "c"}
    assert graph.has_edge("a", "b")
    assert graph["a"]["b"]["reason"] == "r"
    assert not graph.has_edge("a", "c")


def test_build_graph_ignores_dangling_and_self_links(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "a", [
        {"target": "nonexistent-page", "reason": "typo"},
        {"target": "a", "reason": "self"},
        {"target": "b", "reason": "real"},
    ])
    _write(pages_dir, "entity", "b", [])

    graph = graph_topology.build_graph(pages_dir)
    assert graph.number_of_edges() == 1
    assert graph.has_edge("a", "b")


def test_compute_topology_stats_empty_dir(tmp_path):
    pages_dir = tmp_path / "_pages"
    pages_dir.mkdir()
    stats = graph_topology.compute_topology_stats(pages_dir)
    assert stats["page_count"] == 0
    assert stats["avg_path_length"] is None


def test_compute_topology_stats_single_connected_component(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "a", [{"target": "b", "reason": "r"}])
    _write(pages_dir, "entity", "b", [{"target": "c", "reason": "r"}])
    _write(pages_dir, "entity", "c", [])

    stats = graph_topology.compute_topology_stats(pages_dir)
    assert stats["page_count"] == 3
    assert stats["connected_components"] == 1
    assert stats["largest_component_size"] == 3
    assert stats["avg_path_length"] is not None
    assert stats["topologically_orphaned_fraction"] == 0.0


def test_compute_topology_stats_detects_disconnected_orphan(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "a", [{"target": "b", "reason": "r"}])
    _write(pages_dir, "entity", "b", [])
    _write(pages_dir, "entity", "orphan", [])  # no edges at all

    stats = graph_topology.compute_topology_stats(pages_dir)
    assert stats["connected_components"] == 2
    assert stats["topologically_orphaned_fraction"] == round(1 / 3, 4)


def test_find_bridge_candidates_reports_distant_components(tmp_path):
    pages_dir = tmp_path / "_pages"
    # Cluster A: a-b-c, cluster B: x-y (disconnected)
    _write(pages_dir, "entity", "a", [{"target": "b", "reason": "r"}])
    _write(pages_dir, "entity", "b", [{"target": "c", "reason": "r"}])
    _write(pages_dir, "entity", "c", [])
    _write(pages_dir, "entity", "x", [{"target": "y", "reason": "r"}])
    _write(pages_dir, "entity", "y", [])

    candidates = graph_topology.find_bridge_candidates(pages_dir)
    assert len(candidates) == 1
    c = candidates[0]
    assert c["page_a"] == "b"  # highest-degree node in largest component {a,b,c}
    assert c["page_b"] in {"x", "y"}
    assert c["component_size_a"] == 3
    assert c["component_size_b"] == 2


def test_find_bridge_candidates_empty_when_single_component(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "a", [{"target": "b", "reason": "r"}])
    _write(pages_dir, "entity", "b", [])

    assert graph_topology.find_bridge_candidates(pages_dir) == []


def test_check_for_goodharting_flags_orphan_drop_without_path_improvement():
    before = {
        "topologically_orphaned_fraction": 0.75,
        "clustering_coefficient": 0.10,
        "avg_path_length": 4.0,
    }
    after = {
        "topologically_orphaned_fraction": 0.20,  # big drop
        "clustering_coefficient": 0.04,  # dropped
        "avg_path_length": 3.98,  # essentially unchanged (below improvement threshold)
    }
    warning = graph_topology.check_for_goodharting(before, after)
    assert warning is not None
    assert "SUSPECTED GOODHARTING" in warning


def test_check_for_goodharting_silent_when_path_length_genuinely_improves():
    before = {
        "topologically_orphaned_fraction": 0.75,
        "clustering_coefficient": 0.10,
        "avg_path_length": 4.0,
    }
    after = {
        "topologically_orphaned_fraction": 0.20,
        "clustering_coefficient": 0.08,
        "avg_path_length": 2.5,  # genuinely shortened
    }
    assert graph_topology.check_for_goodharting(before, after) is None


def test_check_for_goodharting_silent_when_orphan_drop_is_small():
    before = {"topologically_orphaned_fraction": 0.30, "clustering_coefficient": 0.10, "avg_path_length": 4.0}
    after = {"topologically_orphaned_fraction": 0.25, "clustering_coefficient": 0.05, "avg_path_length": 4.0}
    assert graph_topology.check_for_goodharting(before, after) is None
