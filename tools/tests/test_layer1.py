"""
Unit tests for Layer 1 (deterministic structural checks) of eval_summary.py.
These tests require no external dependencies beyond PyYAML.
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Allow importing from tools/
sys.path.insert(0, str(Path(__file__).parent.parent))
import eval_summary
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

    def test_fail_embedded_frontmatter_block_survives_write(self, tmp_path):
        """Reproduces the allwinner_t536.md corruption: a second '---'-delimited
        block (with malformed YAML -- a duplicate `tags:` key) sits between the
        real frontmatter and the real content. Its own bulk is long/technical
        enough to otherwise clear WORD_COUNT_LOW by accident, so Layer 1 needs an
        explicit structural check rather than relying on the word-count/dangling
        checks to catch it indirectly."""
        page = tmp_path / "corrupted.md"
        page.write_text("""---
canonical_name: Allwinner T536
subtype: hardware_target
scorecard:
  novelty_delta: 0.7
sources: [raw/sources/test.md]
type: hardware_target
created: 2026-07-01
updated: 2026-07-01
cold_start: true
inbound_links: 0
---

---
type: hardware_target
tags:
- allwinner
- risc-v
tags: []
- risc-v
- npu
sources:
- https://example.com/t536
constraints:
- Quad-core Cortex-A55 @ 1.6GHz
- 2 TOPS NPU
---

# Allwinner T536

The Allwinner T536 is an industrial embedded SoC combining Cortex-A55 cores
with XuanTie RISC-V microcontrollers and a dedicated NPU for AI inference at
the edge, targeting industrial control and vision applications that need both
general-purpose compute and low-power always-on sensing in a single package.

## Key Claims

- Quad-core Cortex-A55 running at 1.6GHz.
- Includes a 2 TOPS NPU for on-device inference.
- Integrates XuanTie E907 and E902 RISC-V microcontroller cores.

## Relationships

None.

## Sources

- raw/sources/test.md
""")
        result = layer1_check(page, "hardware_target")
        assert result["pass"] is False
        assert any("EMBEDDED_FRONTMATTER" in v for v in result["violations"])


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


class TestLayer1SoftSignalsAndEntityNaming:
    """Fixes found live during the v6 freeform replication test evaluation:
    a dangling outbound_links target, a synthesis RAG Summary that never
    named its connected entities, empty tags, and generic tag-overlap
    relationship reasons — none of which were previously caught anywhere."""

    def _wiki(self, tmp_path, pages: dict[str, str]) -> Path:
        pages_dir = tmp_path / "wiki" / "_pages"
        for rel_path, content in pages.items():
            p = pages_dir / rel_path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
        return pages_dir

    def test_dangling_outbound_link_is_soft_not_hard(self, tmp_path):
        pages_dir = self._wiki(tmp_path, {
            "hardware_target/greenwaves-gap9.md": (
                "---\ntype: hardware_target\ncanonical_name: GreenWaves GAP9\n"
                "sources: [https://example.com/gap9]\n---\n\n# GreenWaves GAP9\n\nBody.\n"
            ),
        })
        page = tmp_path / "candidate.md"
        page.write_text(
            "---\ntype: entity\ncanonical_name: GAP9 MobileNet Benchmark\n"
            "sources: [https://example.com/bench]\ntags: [gap9]\n"
            "outbound_links:\n- target: gap9\n  reason: Hardware target for this benchmark\n"
            "---\n\n"
            "# GAP9 MobileNet Benchmark\n\n"
            "The GAP9 MobileNet benchmark reports MobileNet V1 inference latency and power "
            "consumption measured on the GreenWaves GAP9 RISC-V AI accelerator, a neural "
            "network building block that runs on production silicon fabricated on a 22nm "
            "FD-SOI process. Introduced as a comparative evaluation, it replaced earlier "
            "informal benchmarking approaches with a repeatable measurement methodology at "
            "an image resolution of 160 by 160 pixels with 0.25 channel scaling applied "
            "throughout the convolutional layers of the network under test, reporting a "
            "result of 12 milliseconds per frame at 806 microwatts of average power draw "
            "during continuous always-on inference workloads on battery-powered devices.\n\n"
            "## Key Claims\n\n- Claim one with a number: 12ms.\n- Claim two: 806uW.\n"
            "- Claim three: 160x160 resolution.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", pages_dir):
            result = layer1_check(page, "entity")
        # "gap9" doesn't match the real page "greenwaves-gap9" -> soft, not hard.
        assert result["pass"] is True
        assert any("DANGLING_LINK" in v for v in result["soft_violations"])

    def test_resolvable_outbound_link_is_not_flagged(self, tmp_path):
        pages_dir = self._wiki(tmp_path, {
            "hardware_target/greenwaves-gap9.md": (
                "---\ntype: hardware_target\ncanonical_name: GreenWaves GAP9\n"
                "sources: [https://example.com/gap9]\n---\n\n# GreenWaves GAP9\n\nBody.\n"
            ),
        })
        page = tmp_path / "candidate.md"
        page.write_text(
            "---\ntype: benchmark_result\ncanonical_name: GAP9 MobileNet Benchmark\n"
            "sources: [https://example.com/bench]\ntags: [gap9]\n"
            "outbound_links:\n- target: greenwaves-gap9\n  reason: Hardware target for this benchmark\n"
            "---\n\n"
            "# GAP9 MobileNet Benchmark\n\n"
            "This benchmark reports MobileNet V1 inference latency and power consumption "
            "measured on the GreenWaves GAP9 RISC-V AI accelerator, running production "
            "silicon fabricated on a 22nm FD-SOI process at an image resolution of 160 "
            "by 160 pixels with 0.25 channel scaling applied throughout the convolutional "
            "layers of the network under test, reporting a result of 12 milliseconds per "
            "frame at 806 microwatts of average power draw during continuous inference.\n\n"
            "## Key Claims\n\n- Claim one with a number: 12ms.\n- Claim two: 806uW.\n"
            "- Claim three: 160x160 resolution.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", pages_dir):
            result = layer1_check(page, "benchmark_result")
        assert not any("DANGLING_LINK" in v for v in result["soft_violations"])

    def test_empty_tags_is_soft(self, tmp_path):
        page = tmp_path / "candidate.md"
        page.write_text(
            "---\ntype: entity\ncanonical_name: Some Entity\n"
            "sources: [https://example.com/x]\ntags: []\n---\n\n"
            "# Some Entity\n\n"
            "A self-contained definition with enough words to clear the minimum "
            "paragraph length threshold required by the entity page template, "
            "describing what it is and why it matters in concrete detail across "
            "several independent sentences that together add up to well past "
            "eighty words in total length so the separate word-count check does "
            "not also fire here unexpectedly and confuse this specific assertion "
            "about the tags field alone, since that would make the test ambiguous "
            "about which particular violation is actually being exercised here.\n\n"
            "## Key Claims\n\n- Claim one with a number: 42.\n- Claim two: BERT.\n"
            "- Claim three: 99%.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", tmp_path / "wiki" / "_pages"):
            result = layer1_check(page, "entity")
        assert result["pass"] is True
        assert any("EMPTY_TAGS" in v for v in result["soft_violations"])

    def test_generic_relationship_reason_is_soft(self, tmp_path):
        page = tmp_path / "candidate.md"
        page.write_text(
            "---\ntype: entity\ncanonical_name: Some Entity\n"
            "sources: [https://example.com/x]\ntags: [x]\n"
            "outbound_links:\n- target: other_entity\n"
            "  reason: Another RISC-V-based AI accelerator\n---\n\n"
            "# Some Entity\n\n"
            "A self-contained definition with enough words to clear the minimum "
            "paragraph length threshold required by the entity page template, "
            "describing what it is and why it matters in concrete detail across "
            "several independent sentences that together add up to well past "
            "eighty words in total length so the separate word-count check does "
            "not also fire here unexpectedly and confuse this specific assertion "
            "about the relationship-reason field alone, since that would make the "
            "test ambiguous about which particular violation is being exercised.\n\n"
            "## Key Claims\n\n- Claim one with a number: 42.\n- Claim two: BERT.\n"
            "- Claim three: 99%.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", tmp_path / "wiki" / "_pages"):
            result = layer1_check(page, "entity")
        assert result["pass"] is True
        assert any("GENERIC_RELATIONSHIP_REASON" in v for v in result["soft_violations"])

    def test_synthesis_rag_summary_must_name_connected_entities(self, tmp_path):
        pages_dir = self._wiki(tmp_path, {
            "entity/fai-ara240-m.md": (
                "---\ntype: entity\ncanonical_name: FAI-Ara240-M\n"
                "sources: [https://example.com/a]\n---\n\n# FAI-Ara240-M\n\nBody.\n"
            ),
            "entity/tenstorrent-grayskull-e75.md": (
                "---\ntype: entity\ncanonical_name: Tenstorrent Grayskull e75\n"
                "sources: [https://example.com/b]\n---\n\n# Tenstorrent Grayskull e75\n\nBody.\n"
            ),
        })
        filler = "This survey reviews KV cache optimization strategies for LLM inference. " * 10
        page = tmp_path / "synth.md"
        page.write_text(
            "---\ntype: synthesis\n"
            "connected_entities: [fai-ara240-m, tenstorrent-grayskull-e75]\n"
            "synthesis_status: draft\n---\n\n"
            f"# Test Synthesis\n\n## RAG Summary\n\n{filler}\n\n"
            "## Full Synthesis\n\nContent.\n\n## Open Questions\n\nNone.\n\n"
            "## Connected Pages\n\nNone.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", pages_dir):
            result = layer1_check(page, "synthesis")
        assert result["pass"] is False
        assert any("RAG_SUMMARY_MISSING_ENTITY_NAMES" in v for v in result["violations"])

        # Now with both entities actually named -> passes this check.
        filler2 = (
            "This survey reviews KV cache optimization strategies relevant to the "
            "FAI-Ara240-M and Tenstorrent Grayskull e75 accelerators for LLM inference. " * 10
        )
        page.write_text(
            "---\ntype: synthesis\n"
            "connected_entities: [fai-ara240-m, tenstorrent-grayskull-e75]\n"
            "synthesis_status: draft\n---\n\n"
            f"# Test Synthesis\n\n## RAG Summary\n\n{filler2[:1400]}\n\n"
            "## Full Synthesis\n\nContent.\n\n## Open Questions\n\nNone.\n\n"
            "## Connected Pages\n\nNone.\n",
            encoding="utf-8",
        )
        with patch.object(eval_summary, "_WIKI_PAGES_DIR", pages_dir):
            result = layer1_check(page, "synthesis")
        assert not any("RAG_SUMMARY_MISSING_ENTITY_NAMES" in v for v in result["violations"])


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
