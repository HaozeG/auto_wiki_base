"""
Tests for graph_stats.py's connectivity stats.

Found live: after 10 research sessions (later scaled to ~100 pages) growing
a hub-and-spoke wiki -- new "leaf" pages each citing one or two existing
pages via outbound_links, without anything citing the leaves back -- an
earlier inbound-only median_inbound_links-based maturity gate never
flipped, because citing something and being cited are different things and
leaves overwhelmingly do the former: no matter how many well-connected leaf
pages you add, fewer than half of all pages will ever themselves accumulate
an inbound link in this shape. orphan_fraction/median_total_links were
changed to use total (inbound + outbound) degree so a leaf with real
outbound edges counts as connected even before anything points back to it --
these tests pin that. The graph_maturity verdict itself was later removed
entirely (three formulas tried, none reliably separated nascent from
established wikis); these are now plain connectivity diagnostics, not gates.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import graph_stats  # noqa: E402


def _write(path: Path, fm_lines: str) -> None:
    path.write_text(f"---\n{fm_lines}---\n\n# Title\n\nBody.\n", encoding="utf-8")


def _outbound_yaml(targets: list[str]) -> str:
    if not targets:
        return ""
    lines = "outbound_links:\n"
    for t in targets:
        lines += f"- target: {t}\n  reason: test reason\n"
    return lines


def test_hub_and_spoke_leaves_are_not_orphans_under_total_links(tmp_path):
    """The exact shape found live: 9 leaves each cite one shared hub via
    outbound_links, gaining zero inbound_links themselves (nothing cites a
    leaf back). Old inbound-only orphan_fraction/median would call this
    orphan-heavy and never mature; total-links must recognize every leaf as
    connected."""
    d = tmp_path / "_pages"
    d.mkdir()
    _write(d / "hub.md", "type: entity\ninbound_links: 9\n")
    for i in range(9):
        _write(d / f"leaf{i}.md", "type: entity\ninbound_links: 0\n" + _outbound_yaml(["hub"]))

    stats = graph_stats.compute_stats(d)

    # Old (inbound-only) view: 9/10 pages have zero inbound_links.
    assert stats["median_inbound_links"] == 0.0
    assert stats["orphan_count"] == 0
    assert stats["orphan_fraction"] == 0.0
    assert stats["median_total_links"] >= 1.0


def test_truly_disconnected_page_still_counts_as_orphan(tmp_path):
    """A page with neither inbound nor outbound links is a genuine orphan
    under total-links too -- the fix must not make orphan detection vacuous."""
    d = tmp_path / "_pages"
    d.mkdir()
    _write(d / "hub.md", "type: entity\ninbound_links: 3\n")
    for i in range(3):
        _write(d / f"leaf{i}.md", "type: entity\ninbound_links: 0\n" + _outbound_yaml(["hub"]))
    _write(d / "isolated.md", "type: entity\ninbound_links: 0\n")

    stats = graph_stats.compute_stats(d)

    assert stats["orphan_count"] == 1
    assert stats["orphan_fraction"] == 0.2


def test_inbound_only_stats_preserved_as_informational(tmp_path):
    """mean/median_inbound_links must still be reported (citation-concentration
    signal) even though they no longer gate maturity."""
    d = tmp_path / "_pages"
    d.mkdir()
    _write(d / "hub.md", "type: entity\ninbound_links: 9\n")
    for i in range(9):
        _write(d / f"leaf{i}.md", "type: entity\ninbound_links: 0\n" + _outbound_yaml(["hub"]))

    stats = graph_stats.compute_stats(d)

    assert stats["mean_inbound_links"] == 0.9
    assert stats["median_inbound_links"] == 0.0
    assert stats["mean_total_links"] > 0.9
    assert stats["median_total_links"] >= 1.0


def test_all_orphans_gives_max_orphan_fraction_and_zero_median(tmp_path):
    d = tmp_path / "_pages"
    d.mkdir()
    for i in range(5):
        _write(d / f"p{i}.md", "type: entity\ninbound_links: 0\n")

    stats = graph_stats.compute_stats(d)

    assert stats["orphan_fraction"] == 1.0
    assert stats["median_total_links"] == 0.0


def test_outbound_links_wrong_type_ignored_gracefully(tmp_path):
    """outbound_links present but not a list (malformed frontmatter) must not
    crash stat computation -- treated as zero outbound edges."""
    d = tmp_path / "_pages"
    d.mkdir()
    _write(d / "weird.md", "type: entity\ninbound_links: 0\noutbound_links: not_a_list\n")

    stats = graph_stats.compute_stats(d)

    assert stats["page_count"] == 1
    assert stats["orphan_count"] == 1
