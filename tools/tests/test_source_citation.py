"""
Unit tests for deterministic source-citation fix-up (_apply_provenance /
_fix_sources_section_body in orchestrator.py).

No API key or qmd installation required.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from orchestrator import _apply_provenance, _fix_sources_section_body  # noqa: E402


def _entry(url="https://example.com/x", title="Example Page", snapshot="raw/cache/abc123.md"):
    return {
        "candidate": {"url": url, "title": title},
        "source_snapshot": snapshot,
        "source_url": url,
        "fetched_at": "2026-07-09T00:00:00+00:00",
    }


class TestFixSourcesSectionBody:
    def test_rewrites_bare_url_citation_to_snapshot(self):
        draft = {
            "content": (
                "# Example\n\nBody text.\n\n"
                "## Sources\n\n"
                "- [Example Page](https://example.com/x)\n"
            )
        }
        entry = _entry()
        _fix_sources_section_body(draft, entry)

        assert "https://example.com/x" not in draft["content"]
        assert "raw/cache/abc123.md" in draft["content"]
        assert "[Example Page](raw/cache/abc123.md)" in draft["content"]

    def test_preserves_content_before_and_after_sources_section(self):
        draft = {
            "content": (
                "# Title\n\nIntro.\n\n"
                "## Key Claims\n\n- claim one\n\n"
                "## Sources\n\n- https://example.com/x\n"
            )
        }
        entry = _entry()
        _fix_sources_section_body(draft, entry)

        assert "## Key Claims" in draft["content"]
        assert "- claim one" in draft["content"]
        assert draft["content"].index("## Key Claims") < draft["content"].index("## Sources")

    def test_appends_sources_section_when_missing(self):
        draft = {"content": "# Title\n\nBody with no Sources heading.\n"}
        entry = _entry()
        _fix_sources_section_body(draft, entry)

        assert "## Sources" in draft["content"]
        assert "raw/cache/abc123.md" in draft["content"]

    def test_no_snapshot_leaves_content_untouched(self):
        original = "# Title\n\n## Sources\n\n- https://example.com/x\n"
        draft = {"content": original}
        entry = {"candidate": {"url": "https://example.com/x", "title": "X"}}
        _fix_sources_section_body(draft, entry)

        assert draft["content"] == original

    def test_multi_entry_sources_section_all_replaced_by_snapshot_line(self):
        draft = {
            "content": (
                "# Title\n\n## Sources\n\n"
                "- https://example.com/x\n"
                "- https://other.example.com/y\n"
            )
        }
        entry = _entry()
        _fix_sources_section_body(draft, entry)

        assert "other.example.com" not in draft["content"]
        assert "raw/cache/abc123.md" in draft["content"]


class TestApplyProvenanceAndBodyFixTogether:
    def test_frontmatter_and_body_both_cite_snapshot(self):
        draft = {
            "frontmatter": {"sources": ["https://example.com/x"]},
            "content": "# Title\n\n## Sources\n\n- [Example Page](https://example.com/x)\n",
        }
        entry = _entry()
        _apply_provenance(draft, entry)
        _fix_sources_section_body(draft, entry)

        assert "raw/cache/abc123.md" in draft["frontmatter"]["sources"]
        assert "[Example Page](raw/cache/abc123.md)" in draft["content"]
        assert "https://example.com/x" not in draft["content"]
