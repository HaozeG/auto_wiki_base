import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import context_selector
from qmd_runner import QmdMatch, QmdSearchResult


def _write(pages_dir: Path, subdir: str, stem: str, inbound_links: int = 0):
    d = pages_dir / subdir
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{stem}.md").write_text(
        f"---\ntype: entity\ninbound_links: {inbound_links}\n---\n\n# {stem}\n\nBody.\n",
        encoding="utf-8",
    )


class _FakeQmdRunner:
    """Returns identical similarity scores for every page, so any residual
    ranking difference must come from something other than qmd's own score —
    i.e. it isolates whether inbound_links still influences the outcome."""

    def __init__(self, pages: list[Path], score: float = 0.5):
        self._pages = pages
        self._score = score

    def search(self, query_text, top=20, collection="_pages"):
        matches = [
            QmdMatch(rank=i + 1, file=f"qmd://_pages/entity/{p.stem}.md", score=self._score)
            for i, p in enumerate(self._pages)
        ]
        return QmdSearchResult(ok=True, matches=matches)


def test_inbound_links_no_longer_breaks_ties(tmp_path, monkeypatch):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "low-inbound", inbound_links=0)
    _write(pages_dir, "entity", "high-inbound", inbound_links=500)
    monkeypatch.setattr(context_selector, "_WIKI_PAGES_DIR", pages_dir)

    all_pages = context_selector._list_all_pages()
    runner = _FakeQmdRunner(all_pages, score=0.5)

    selected = context_selector.select_context_pages(
        "some resource content", qmd_runner=runner, max_tokens=100000,
    )

    # Both pages tie on qmd score; previously inbound_links * 0.001 would
    # have deterministically ordered high-inbound first. With the fix,
    # ranked_paths.sort is stable and both keep their original (qmd-result)
    # order — high inbound_links must not force high-inbound to rank first
    # when the underlying scores are otherwise identical.
    filenames = [s["filename"] for s in selected]
    assert set(filenames) == {"low-inbound.md", "high-inbound.md"}
    # Direct check: no ranking function still reads frontmatter's
    # inbound_links field (docstrings/comments mention the term in prose
    # explaining the historic bug, so check the actual functional read
    # pattern — fm.get("inbound_links" — not the bare word).
    import inspect
    for fn in (context_selector.select_context_pages, context_selector._structured_rank,
               context_selector._fallback_rank_neutral, context_selector._qmd_search):
        assert 'get("inbound_links"' not in inspect.getsource(fn)
        assert "get('inbound_links'" not in inspect.getsource(fn)


def test_fallback_rank_neutral_ignores_inbound_links(tmp_path):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "zzz-high-inbound", inbound_links=999)
    _write(pages_dir, "entity", "aaa-low-inbound", inbound_links=0)

    pages = [pages_dir / "entity" / "zzz-high-inbound.md", pages_dir / "entity" / "aaa-low-inbound.md"]
    ranked = context_selector._fallback_rank_neutral(pages)

    # Neutral fallback orders by filename, not by inbound_links — the
    # high-inbound page must not be forced first.
    assert [p.stem for p, _ in ranked] == ["aaa-low-inbound", "zzz-high-inbound"]


def test_fair_share_cap_deprioritizes_over_represented_page(tmp_path, monkeypatch):
    pages_dir = tmp_path / "_pages"
    _write(pages_dir, "entity", "overshown", inbound_links=0)
    _write(pages_dir, "entity", "fresh", inbound_links=0)
    monkeypatch.setattr(context_selector, "_WIKI_PAGES_DIR", pages_dir)

    all_pages = context_selector._list_all_pages()
    # "overshown" scores higher than "fresh" on pure topical similarity...
    runner = _FakeQmdRunner([], score=0.0)

    def fake_search(query_text, top=20, qmd_runner=None):
        overshown = pages_dir / "entity" / "overshown.md"
        fresh = pages_dir / "entity" / "fresh.md"
        return [(overshown, 0.9), (fresh, 0.5)]

    monkeypatch.setattr(context_selector, "_qmd_search", fake_search)

    # ...but its decayed share of past injection events (9 out of the last 10
    # ticks) is far above its fair share of these 2 pages (0.5), even after a
    # generous 1.2x fair-share multiplier (threshold 0.6) — see
    # injection_history.py for why this is a share, not a raw count vs cap.
    injection_counts = {"overshown": 9.0}
    selected = context_selector.select_context_pages(
        "resource content",
        injection_counts=injection_counts,
        injection_total_ticks=10.0,
        fair_share_multiplier=1.2,
        max_tokens=100000,
    )

    filenames = [s["filename"] for s in selected]
    # "fresh" (lower topical score, but not over-represented) must be
    # prioritized ahead of "overshown" (higher topical score, but
    # over-represented) — the whole point of the cap is to stop a page
    # dominating every drafting context in a row.
    assert filenames.index("fresh.md") < filenames.index("overshown.md")
