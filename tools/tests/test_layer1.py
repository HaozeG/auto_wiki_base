"""
Unit tests for Layer 1 (deterministic structural checks) of eval_summary.py.
These tests require no external dependencies beyond PyYAML.
"""

import sys
from pathlib import Path

import pytest

# Allow importing from tools/
sys.path.insert(0, str(Path(__file__).parent.parent))
from eval_summary import layer1_check, parse_page, _extract_first_paragraph, _extract_rag_summary

FIXTURES = Path(__file__).parent / "fixtures"


class TestLayer1EntityPages:
    def test_pass_entity_exits_clean(self):
        result = layer1_check(FIXTURES / "pass_entity.md", "entity")
        assert result["pass"] is True
        assert result["violations"] == []

    def test_fail_dangling_detected(self):
        result = layer1_check(FIXTURES / "fail_dangling.md", "entity")
        assert result["pass"] is False
        dangling_violations = [v for v in result["violations"] if "DANGLING_REF" in v]
        assert len(dangling_violations) >= 1

    def test_fail_wordcount_too_short(self):
        result = layer1_check(FIXTURES / "fail_wordcount.md", "entity")
        assert result["pass"] is False
        wc_violations = [v for v in result["violations"] if "WORD_COUNT_LOW" in v]
        assert len(wc_violations) == 1

    def test_pass_entity_no_dangling_refs(self):
        result = layer1_check(FIXTURES / "pass_entity.md", "entity")
        dangling = [v for v in result["violations"] if "DANGLING_REF" in v]
        assert dangling == []

    def test_pass_entity_word_count_in_range(self):
        fm, body = parse_page(FIXTURES / "pass_entity.md")
        first_para = _extract_first_paragraph(body)
        word_count = len(first_para.split())
        assert 80 <= word_count <= 300, f"Expected 80-300 words, got {word_count}"


class TestLayer1DanglingPatterns:
    """Test specific dangling reference patterns."""

    def _check_text_for_dangling(self, text: str) -> list[str]:
        """Create a minimal entity page with the given first paragraph and check."""
        import tempfile
        import os
        content = f"""---
type: entity
tags: []
sources: [raw/sources/test.md]
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
---

# Test Entity

{text}

## Key Claims

- Claim one with specific detail.
- Claim two with another fact: 42%.
- Claim three references a named system: BERT.

## Relationships

None.

## Sources

- raw/sources/test.md
"""
        with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False) as f:
            f.write(content)
            tmp_path = Path(f.name)
        try:
            return layer1_check(tmp_path, "entity")["violations"]
        finally:
            os.unlink(tmp_path)

    def test_as_mentioned_above(self):
        violations = self._check_text_for_dangling(
            "As mentioned above, the system processes inputs in parallel. " * 15
        )
        assert any("DANGLING_REF" in v for v in violations)

    def test_see_above(self):
        violations = self._check_text_for_dangling(
            "See above for the full derivation. " * 15 + "The mechanism works by computing attention scores over all positions simultaneously, using scaled dot products."
        )
        assert any("DANGLING_REF" in v for v in violations)

    def test_building_on(self):
        violations = self._check_text_for_dangling(
            "Building on the previous discussion, we can see that the transformer computes weighted sums. " * 12
        )
        assert any("DANGLING_REF" in v for v in violations)

    def test_clean_text_no_violations(self):
        violations = self._check_text_for_dangling(
            "The transformer is a neural network architecture introduced in 2017 by Vaswani et al. "
            "It processes sequences in parallel using self-attention, achieving O(1) path length "
            "between any two positions. The architecture replaced recurrent networks in machine "
            "translation and achieved state-of-the-art BLEU scores. Self-attention computes "
            "compatibility between all pairs of positions simultaneously, enabling richer "
            "representations than sequential processing allows. The model uses residual connections "
            "and layer normalization to stabilize training across many layers. "
        )
        dangling = [v for v in violations if "DANGLING_REF" in v]
        assert dangling == []


class TestLayer1SynthesisPages:
    def test_missing_rag_summary_fails(self, tmp_path):
        page = tmp_path / "no_rag_summary.md"
        page.write_text("""---
type: synthesis
connected_entities: [entity_a, entity_b]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
---

# Test Synthesis

## Full Synthesis

Some narrative content without a RAG Summary block.

## Open Questions

None.

## Connected Pages

None.
""")
        result = layer1_check(page, "synthesis")
        assert result["pass"] is False
        assert any("MISSING_RAG_SUMMARY" in v for v in result["violations"])

    def test_rag_summary_dangling_ref_fails(self, tmp_path):
        page = tmp_path / "dangling_rag.md"
        # 150+ word RAG summary with dangling reference
        filler = "This synthesis connects two entities in a meaningful way. " * 10
        page.write_text(f"""---
type: synthesis
connected_entities: [entity_a, entity_b]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
---

# Test Synthesis

## RAG Summary

As discussed above, {filler}EntityA and EntityB share a fundamental relationship.

---

## Full Synthesis

Content here.

## Open Questions

None.

## Connected Pages

None.
""")
        result = layer1_check(page, "synthesis")
        assert result["pass"] is False
        assert any("DANGLING_REF" in v for v in result["violations"])


class TestGraphStats:
    def test_mean_inbound_links(self):
        from graph_stats import compute_stats
        fixtures_dir = FIXTURES / "graph_test_pages"
        stats = compute_stats(fixtures_dir)
        assert stats["mean_inbound_links"] == 2.0
        assert stats["page_count"] == 3
        assert stats["above_maturity_threshold"] is False  # 2.0 is NOT > 2.0

    def test_empty_directory(self, tmp_path):
        from graph_stats import compute_stats
        stats = compute_stats(tmp_path)
        assert stats["mean_inbound_links"] == 0.0
        assert stats["page_count"] == 0
