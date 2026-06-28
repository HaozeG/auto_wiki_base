"""
Unit tests for Phase 6 harness modules.
No API key or qmd installation required.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from validate_output import extract_json_block, validate_and_parse
from quota import QuotaManager, MAX_API_CALLS_PER_SESSION


class TestExtractJsonBlock:
    def test_clean_json(self):
        raw = '{"key": "value"}'
        assert extract_json_block(raw) == '{"key": "value"}'

    def test_json_with_preamble(self):
        raw = 'Here is the response:\n{"key": "value"}'
        assert extract_json_block(raw) == '{"key": "value"}'

    def test_nested_json(self):
        raw = '{"a": {"b": 1}}'
        result = extract_json_block(raw)
        assert result == '{"a": {"b": 1}}'

    def test_no_json_returns_none(self):
        raw = "No JSON here at all"
        assert extract_json_block(raw) is None

    def test_empty_string_returns_none(self):
        assert extract_json_block("") is None


class TestValidateAndParse:
    def test_valid_candidate_list(self):
        raw = """{
            "candidates": [
                {
                    "url": "https://example.com/paper",
                    "title": "Example Paper",
                    "relevance_rationale": "Directly relevant to the query topic.",
                    "estimated_type": "entity"
                }
            ],
            "search_queries_used": ["example query"]
        }"""
        result = validate_and_parse(raw, "CandidateList")
        assert result is not None
        assert len(result["candidates"]) == 1
        assert result["candidates"][0]["url"] == "https://example.com/paper"

    def test_malformed_json_returns_none(self):
        raw = "This is not JSON {broken"
        assert validate_and_parse(raw, "CandidateList") is None

    def test_schema_mismatch_returns_none(self):
        raw = '{"wrong_field": "value"}'
        assert validate_and_parse(raw, "CandidateList") is None

    def test_never_raises_on_garbage(self):
        for bad in ["", "   ", "\x00\x01", "null", "[]", "true"]:
            result = validate_and_parse(bad, "CandidateList")
            assert result is None  # never raises

    def test_valid_eval_result_approve(self):
        raw = """{
            "decision": "approve",
            "rejection_reason": null,
            "scorecard": {
                "novelty_delta": 0.8,
                "claim_density": 0.7,
                "self_containedness": 0.9,
                "bridge_score": 0.5,
                "hub_potential": 0.4,
                "gap_fill_score": 0.6,
                "contradiction_potential": 0.2,
                "weighted_total": 0.65
            },
            "page_drafts": [
                {
                    "page_type": "entity",
                    "filename": "example_entity",
                    "frontmatter": {"type": "entity", "tags": ["test"]},
                    "content": "# Example\\n\\nContent here."
                }
            ],
            "pages_to_update": [],
            "contradictions_found": []
        }"""
        result = validate_and_parse(raw, "EvalResult")
        assert result is not None
        assert result["decision"] == "approve"
        assert len(result["page_drafts"]) == 1

    def test_valid_eval_result_reject(self):
        raw = """{
            "decision": "reject",
            "rejection_reason": "Content is too general with no verifiable claims.",
            "scorecard": {
                "novelty_delta": 0.1,
                "claim_density": 0.05,
                "self_containedness": 0.3,
                "bridge_score": 0.0,
                "hub_potential": 0.0,
                "gap_fill_score": 0.0,
                "contradiction_potential": 0.0,
                "weighted_total": 0.08
            },
            "page_drafts": [],
            "pages_to_update": [],
            "contradictions_found": []
        }"""
        result = validate_and_parse(raw, "EvalResult")
        assert result is not None
        assert result["decision"] == "reject"

    def test_invalid_decision_returns_none(self):
        raw = """{
            "decision": "maybe",
            "rejection_reason": null,
            "scorecard": {},
            "page_drafts": [],
            "pages_to_update": [],
            "contradictions_found": []
        }"""
        assert validate_and_parse(raw, "EvalResult") is None

    def test_json_with_trailing_text(self):
        raw = '{"candidates": [], "search_queries_used": ["q"]} Some trailing text'
        result = validate_and_parse(raw, "CandidateList")
        assert result is not None

    def test_unknown_schema_returns_none(self):
        raw = '{"key": "value"}'
        assert validate_and_parse(raw, "UnknownSchema") is None


class TestQuotaManager:
    def test_initial_state_not_exceeded(self):
        q = QuotaManager(max_candidates=5, max_new_pages=3)
        assert not q.any_exceeded()

    def test_candidates_exceeded(self):
        q = QuotaManager(max_candidates=2, max_new_pages=10)
        q.record_candidate_evaluated()
        q.record_candidate_evaluated()
        assert q.candidates_exceeded()
        assert q.any_exceeded()

    def test_pages_exceeded(self):
        q = QuotaManager(max_candidates=10, max_new_pages=1)
        q.record_page_written()
        assert q.pages_exceeded()
        assert q.any_exceeded()

    def test_api_calls_hard_cap(self):
        q = QuotaManager()
        for _ in range(MAX_API_CALLS_PER_SESSION):
            q.record_api_call()
        assert q.api_calls_exceeded()
        assert q.any_exceeded()

    def test_status_dict(self):
        q = QuotaManager(max_candidates=5, max_new_pages=3)
        q.record_candidate_evaluated()
        q.record_page_written()
        q.record_api_call()
        status = q.status()
        assert status["candidates_evaluated"] == 1
        assert status["pages_written"] == 1
        assert status["api_calls"] == 1
        assert status["max_candidates"] == 5

    def test_not_exceeded_until_at_cap(self):
        q = QuotaManager(max_candidates=3, max_new_pages=10)
        for _ in range(3):
            q.record_candidate_evaluated()
        # At exactly max — should be exceeded (>= comparison)
        assert q.candidates_exceeded()


class TestContextSelectorFallback:
    """Tests context_selector without qmd (fallback path)."""

    def test_empty_pages_dir_returns_empty(self, tmp_path):
        from unittest.mock import patch
        import context_selector as cs

        with patch.object(cs, "_WIKI_PAGES_DIR", tmp_path):
            result = cs.select_context_pages("some resource content")
        assert result == []

    def test_pages_ranked_by_inbound_links_fallback(self, tmp_path):
        from unittest.mock import patch
        import context_selector as cs

        # Create 2 test pages
        (tmp_path / "high_inbound.md").write_text(
            "---\ntype: entity\ninbound_links: 10\n---\n\nHigh inbound page with lots of content.\n",
            encoding="utf-8",
        )
        (tmp_path / "low_inbound.md").write_text(
            "---\ntype: entity\ninbound_links: 1\n---\n\nLow inbound page.\n",
            encoding="utf-8",
        )

        with patch.object(cs, "_WIKI_PAGES_DIR", tmp_path), \
             patch.object(cs, "_qmd_search", return_value=[]):
            result = cs.select_context_pages("resource content about entities", max_tokens=10000)

        # With qmd returning nothing (empty list), fallback ranks by inbound_links
        assert len(result) <= 2
        if len(result) == 2:
            assert result[0]["filename"] == "high_inbound.md"


# ---------------------------------------------------------------------------
# _increment_frontmatter_field and _update_inbound_links regression tests
# ---------------------------------------------------------------------------

_PAGE_BODY = "\n\n# Test Page\n\nSome content here.\n"
_PAGE_FM = "---\ninbound_links: 0\ntype: entity\n---"
_PAGE_CONTENT = _PAGE_FM + _PAGE_BODY


def _read_fm(path):
    import yaml
    text = path.read_text(encoding="utf-8")
    end = text.find("---", 3)
    return yaml.safe_load(text[3:end].strip()) or {}, text


class TestIncrementFrontmatterField:
    def setup_method(self):
        from unittest.mock import patch
        import orchestrator
        self._orchestrator = orchestrator

    def test_single_increment_updates_field(self, tmp_path):
        page = tmp_path / "page.md"
        page.write_text(_PAGE_CONTENT, encoding="utf-8")
        self._orchestrator._increment_frontmatter_field(page, "inbound_links")
        fm, _ = _read_fm(page)
        assert fm["inbound_links"] == 1

    def test_single_increment_delimiter_stays_three_dashes(self, tmp_path):
        page = tmp_path / "page.md"
        page.write_text(_PAGE_CONTENT, encoding="utf-8")
        self._orchestrator._increment_frontmatter_field(page, "inbound_links")
        text = page.read_text(encoding="utf-8")
        # Find the closing delimiter: line after the YAML block must be exactly "---"
        lines = text.split("\n")
        # First line is "---" (opening), then yaml lines, then closing "---"
        # The closing delimiter must be exactly 3 dashes
        yaml_end_line = next(
            i for i, ln in enumerate(lines[1:], 1) if ln.startswith("-") and ln == "-" * len(ln) and len(ln) >= 3
        )
        assert lines[yaml_end_line] == "---", (
            f"Expected '---' but got {lines[yaml_end_line]!r} — delimiter accumulated"
        )

    def test_n_increments_no_dash_accumulation(self, tmp_path):
        """Calling N times must not grow the closing delimiter (regression for double---- bug)."""
        import yaml
        page = tmp_path / "page.md"
        page.write_text(_PAGE_CONTENT, encoding="utf-8")
        N = 5
        for _ in range(N):
            self._orchestrator._increment_frontmatter_field(page, "inbound_links")
        text = page.read_text(encoding="utf-8")
        # The closing delimiter line must still be exactly "---"
        lines = text.split("\n")
        yaml_end_line = next(
            i for i, ln in enumerate(lines[1:], 1) if ln.startswith("-") and len(ln) >= 3 and ln == "-" * len(ln)
        )
        assert lines[yaml_end_line] == "---", (
            f"After {N} increments delimiter is {lines[yaml_end_line]!r} ({len(lines[yaml_end_line])} dashes)"
        )
        # Field value must equal N
        end = text.find("---", 3)
        fm = yaml.safe_load(text[3:end].strip()) or {}
        assert fm["inbound_links"] == N
        # Body must be unchanged
        body_start = text.find(_PAGE_BODY.lstrip("\n"), end)
        assert body_start != -1

    def test_frontmatter_parseable_after_increments(self, tmp_path):
        """yaml.safe_load must not raise after multiple increments."""
        import yaml
        page = tmp_path / "page.md"
        page.write_text(_PAGE_CONTENT, encoding="utf-8")
        for _ in range(3):
            self._orchestrator._increment_frontmatter_field(page, "inbound_links")
        text = page.read_text(encoding="utf-8")
        end = text.find("---", 3)
        fm = yaml.safe_load(text[3:end].strip())
        assert fm is not None

    def test_missing_page_skips_gracefully(self, tmp_path):
        nonexistent = tmp_path / "does_not_exist.md"
        # Must not raise
        self._orchestrator._increment_frontmatter_field(nonexistent, "inbound_links")

    def test_non_frontmatter_file_unchanged(self, tmp_path):
        page = tmp_path / "plain.md"
        original = "# Just a markdown file\n\nNo frontmatter here.\n"
        page.write_text(original, encoding="utf-8")
        self._orchestrator._increment_frontmatter_field(page, "inbound_links")
        assert page.read_text(encoding="utf-8") == original


class TestUpdateInboundLinks:
    def setup_method(self):
        import orchestrator
        self._orchestrator = orchestrator

    def _make_page(self, tmp_path, name, inbound=0):
        page = tmp_path / f"{name}.md"
        page.write_text(
            f"---\ninbound_links: {inbound}\ntype: entity\n---\n\n# {name}\n",
            encoding="utf-8",
        )
        return page

    def _get_inbound(self, page):
        import yaml
        text = page.read_text(encoding="utf-8")
        end = text.find("---", 3)
        return (yaml.safe_load(text[3:end].strip()) or {}).get("inbound_links", 0)

    def test_body_wiki_links_increment(self, tmp_path, monkeypatch):
        monkeypatch.setattr(self._orchestrator, "_WIKI_PAGES_DIR", tmp_path)
        page_a = self._make_page(tmp_path, "Page_A")
        draft = {"content": "See [[Page_A]] for details.", "frontmatter": {}}
        self._orchestrator._update_inbound_links(draft)
        assert self._get_inbound(page_a) == 1

    def test_connected_entities_increments(self, tmp_path, monkeypatch):
        monkeypatch.setattr(self._orchestrator, "_WIKI_PAGES_DIR", tmp_path)
        page_b = self._make_page(tmp_path, "Page_B")
        draft = {
            "content": "## RAG Summary\nSome synthesis.",
            "frontmatter": {"connected_entities": ["Page_B"]},
        }
        self._orchestrator._update_inbound_links(draft)
        assert self._get_inbound(page_b) == 1

    def test_connected_entities_with_md_suffix(self, tmp_path, monkeypatch):
        monkeypatch.setattr(self._orchestrator, "_WIKI_PAGES_DIR", tmp_path)
        page_c = self._make_page(tmp_path, "Page_C")
        draft = {
            "content": "",
            "frontmatter": {"connected_entities": ["Page_C.md"]},
        }
        self._orchestrator._update_inbound_links(draft)
        assert self._get_inbound(page_c) == 1

    def test_no_double_count_when_in_both(self, tmp_path, monkeypatch):
        monkeypatch.setattr(self._orchestrator, "_WIKI_PAGES_DIR", tmp_path)
        page_x = self._make_page(tmp_path, "Page_X")
        draft = {
            "content": "See [[Page_X]] for details.",
            "frontmatter": {"connected_entities": ["Page_X"]},
        }
        self._orchestrator._update_inbound_links(draft)
        # Must be 1, not 2 — deduplication via set
        assert self._get_inbound(page_x) == 1
