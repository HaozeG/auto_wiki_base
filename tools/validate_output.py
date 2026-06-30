"""
Schema validation and JSON extraction for subagent outputs.
Never raises — all failures return None and are logged.
"""

import json
import logging
import re
from typing import Any

logger = logging.getLogger(__name__)


def extract_json_block(text: str) -> str | None:
    """
    Extract the outermost {...} JSON block from text.
    Handles accidental preamble text before the JSON.
    Returns the JSON string or None if not found.
    """
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    for i, ch in enumerate(text[start:], start=start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


_CANDIDATE_LIST_REQUIRED = {"candidates", "search_queries_used"}
_CANDIDATE_REQUIRED = {"url", "title", "relevance_rationale", "estimated_type"}
_EVAL_RESULT_REQUIRED = {"decision", "rejection_reason", "scorecard", "page_drafts",
                          "pages_to_update", "contradictions_found"}
_SCORECARD_REQUIRED = {"novelty_delta", "claim_density", "self_containedness",
                        "bridge_score", "hub_potential", "gap_fill_score",
                        "contradiction_potential", "weighted_total"}
_PAGE_DRAFT_REQUIRED = {"page_type", "filename", "frontmatter", "content"}
_PAGE_TYPES = {
    "entity",
    "synthesis",
    "source_note",
    "hardware_target",
    "workload_kernel",
    "optimization_recipe",
    "benchmark_result",
}


def _valid_page_type(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_]{1,63}", value) is not None


def _validate_candidate_list(data: dict) -> None:
    missing = _CANDIDATE_LIST_REQUIRED - data.keys()
    if missing:
        raise ValueError(f"CandidateList missing fields: {missing}")
    if not isinstance(data["candidates"], list):
        raise TypeError("candidates must be a list")
    for i, c in enumerate(data["candidates"]):
        missing_c = _CANDIDATE_REQUIRED - c.keys()
        if missing_c:
            raise ValueError(f"Candidate {i} missing fields: {missing_c}")
        if c.get("estimated_type") != "unknown" and not _valid_page_type(c.get("estimated_type")):
            raise ValueError(f"Candidate {i} invalid estimated_type: {c.get('estimated_type')}")


def _validate_eval_result(data: dict) -> None:
    missing = _EVAL_RESULT_REQUIRED - data.keys()
    if missing:
        raise ValueError(f"EvalResult missing fields: {missing}")
    if data["decision"] not in ("approve", "reject"):
        raise ValueError(f"Invalid decision: {data['decision']}")
    if data["decision"] == "approve":
        sc = data.get("scorecard", {})
        missing_sc = _SCORECARD_REQUIRED - sc.keys()
        if missing_sc:
            raise ValueError(f"Scorecard missing fields: {missing_sc}")
        for draft in data.get("page_drafts", []):
            missing_d = _PAGE_DRAFT_REQUIRED - draft.keys()
            if missing_d:
                raise ValueError(f"PageDraft missing fields: {missing_d}")
            if not _valid_page_type(draft.get("page_type")):
                raise ValueError(f"Invalid page_type: {draft.get('page_type')}")
            if not isinstance(draft.get("frontmatter"), dict):
                raise TypeError("PageDraft.frontmatter must be a dict")
            # identity_action is advisory; validate only its value when present.
            action = draft.get("identity_action")
            if action is not None and action not in ("create", "upsert", "alias"):
                raise ValueError(f"Invalid identity_action: {action}")


_MERGE_RESULT_REQUIRED = {"merged_content"}


def _validate_merge_result(data: dict) -> None:
    missing = _MERGE_RESULT_REQUIRED - data.keys()
    if missing:
        raise ValueError(f"MergeResult missing fields: {missing}")
    if not isinstance(data["merged_content"], str) or not data["merged_content"].strip():
        raise ValueError("MergeResult.merged_content must be a non-empty string")


def _validate_profile_list(data: dict) -> None:
    profiles = data.get("profiles")
    if not isinstance(profiles, list) or not profiles:
        raise ValueError("ProfileList.profiles must be a non-empty list")
    for i, p in enumerate(profiles):
        for key in ("id", "name", "description"):
            if not isinstance(p.get(key), str) or not p.get(key).strip():
                raise ValueError(f"Profile {i} missing/invalid {key}")
        if not isinstance(p.get("page_types"), dict) or not p["page_types"]:
            raise ValueError(f"Profile {i} must define page_types (subtypes)")


_SCHEMA_VALIDATORS = {
    "CandidateList": _validate_candidate_list,
    "EvalResult": _validate_eval_result,
    "MergeResult": _validate_merge_result,
    "ProfileList": _validate_profile_list,
}


def validate_and_parse(raw_response: str, schema: str) -> dict | None:
    """
    Extract JSON from raw_response, validate against named schema.
    Returns parsed dict on success, None on any failure.
    Never raises.

    schema: one of "CandidateList", "EvalResult"
    """
    try:
        json_str = extract_json_block(raw_response)
        if json_str is None:
            logger.warning("validate_and_parse: no JSON block found in response")
            return None
        data = json.loads(json_str)
        validator = _SCHEMA_VALIDATORS.get(schema)
        if validator is None:
            raise ValueError(f"Unknown schema: {schema}")
        validator(data)
        return data
    except Exception as e:
        logger.warning("validate_and_parse: validation failed — %s", e)
        return None
