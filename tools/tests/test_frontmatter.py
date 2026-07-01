"""
Unit tests for tools/frontmatter.py, the canonical frontmatter parse/render module.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import frontmatter


class TestRenderPage:
    def test_simple_body_round_trips(self):
        fm = {"type": "entity", "sources": ["https://example.com"]}
        rendered = frontmatter.render_page(fm, "# Title\n\nSome body text.\n")
        out_fm, out_body, has_fm = frontmatter.split_frontmatter(rendered)
        assert has_fm
        assert out_fm == fm
        assert "# Title" in out_body
        assert out_body.count("---\n") == 0

    def test_strips_duplicate_embedded_frontmatter_in_body(self):
        """Subagent drafts sometimes echo a second frontmatter block inside their
        own `content` field. render_page must strip it so the rendered page has
        exactly one frontmatter block, otherwise downstream first-paragraph /
        word-count extraction reads the embedded YAML instead of the real body."""
        fm = {"type": "hardware_target", "sources": ["https://example.com"]}
        embedded_fm_body = (
            "---\n"
            "type: hardware_target\n"
            "tags: [risc-v]\n"
            "---\n"
            "\n"
            "# Real Title\n"
            "\n"
            "This is the real first paragraph that should be evaluated for word "
            "count and dangling references, not the embedded frontmatter block "
            "above it which the subagent mistakenly duplicated into the content "
            "field alongside the separate structured frontmatter dict.\n"
        )
        rendered = frontmatter.render_page(fm, embedded_fm_body)
        out_fm, out_body, has_fm = frontmatter.split_frontmatter(rendered)
        assert has_fm
        assert out_fm == fm
        assert "# Real Title" in out_body
        assert "tags: [risc-v]" not in out_body
        # exactly one frontmatter delimiter pair remains in the whole document
        assert rendered.count("\n---\n") + (1 if rendered.startswith("---\n") else 0) <= 2
