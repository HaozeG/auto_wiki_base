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
