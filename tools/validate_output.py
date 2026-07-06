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

# Always valid regardless of theme: the two canonical RAG-retrieval types, plus
# source_note (a source-grounded staging kind used before a page is page-worthy).
# Everything else must be a subtype the theme actually declared.
_BASE_PAGE_TYPES = {"entity", "synthesis", "source_note"}


def _valid_page_type(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_]{1,63}", value) is not None


def _valid_page_type_for_taxonomy(value: Any, allowed_page_types: set[str] | None) -> bool:
    """
    Format check, plus (when a taxonomy is supplied) membership check against
    the theme's currently declared page types. `allowed_page_types` is expected
    to already include any subtype registered earlier this session by the
    taxonomy-evolution mechanism (tools/orchestrator.py) — this function has no
    theme-specific knowledge of its own.
    """
    if not _valid_page_type(value):
        return False
    if allowed_page_types is None:
        return True
    return value in _BASE_PAGE_TYPES or value in allowed_page_types


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


def _validate_eval_result(data: dict, allowed_page_types: set[str] | None = None) -> None:
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
            if not _valid_page_type_for_taxonomy(draft.get("page_type"), allowed_page_types):
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


_SYNTHESIS_RESULT_REQUIRED = {"decision", "rejection_reason", "page_draft"}


def _validate_synthesis_result(data: dict) -> None:
    missing = _SYNTHESIS_RESULT_REQUIRED - data.keys()
    if missing:
        raise ValueError(f"SynthesisResult missing fields: {missing}")
    if data["decision"] not in ("approve", "reject"):
        raise ValueError(f"Invalid decision: {data['decision']}")
    if data["decision"] == "approve":
        draft = data.get("page_draft")
        if not isinstance(draft, dict):
            raise TypeError("SynthesisResult.page_draft must be a dict when approved")
        missing_d = _PAGE_DRAFT_REQUIRED - draft.keys()
        if missing_d:
            raise ValueError(f"PageDraft missing fields: {missing_d}")
        if draft.get("page_type") != "synthesis":
            raise ValueError(f"SynthesisResult.page_draft.page_type must be 'synthesis': {draft.get('page_type')}")
        if not isinstance(draft.get("frontmatter"), dict):
            raise TypeError("PageDraft.frontmatter must be a dict")
        connected = draft["frontmatter"].get("connected_entities")
        if not isinstance(connected, list) or len(connected) < 2:
            raise ValueError("SynthesisResult.page_draft.frontmatter.connected_entities must name >= 2 entities")


_SUBTYPE_PROPOSAL_REQUIRED = {
    "decision", "rejection_reason", "subtype_name", "label",
    "description", "structured_fields", "parent_hub_ids",
}


def _validate_subtype_proposal(data: dict) -> None:
    missing = _SUBTYPE_PROPOSAL_REQUIRED - data.keys()
    if missing:
        raise ValueError(f"SubtypeProposal missing fields: {missing}")
    if data["decision"] not in ("approve", "reject"):
        raise ValueError(f"Invalid decision: {data['decision']}")
    if data["decision"] == "approve":
        if not _valid_page_type(data.get("subtype_name")):
            raise ValueError(f"Invalid subtype_name: {data.get('subtype_name')}")
        if not isinstance(data.get("label"), str) or not data["label"].strip():
            raise ValueError("SubtypeProposal.label must be a non-empty string")
        parent_ids = data.get("parent_hub_ids")
        if not isinstance(parent_ids, list) or not (1 <= len(parent_ids) <= 2):
            raise ValueError("SubtypeProposal.parent_hub_ids must have 1 or 2 entries")


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
    "SynthesisResult": _validate_synthesis_result,
    "SubtypeProposal": _validate_subtype_proposal,
}


def validate_and_parse(
    raw_response: str, schema: str, allowed_page_types: set[str] | None = None
) -> dict | None:
    """
    Extract JSON from raw_response, validate against named schema.
    Returns parsed dict on success, None on any failure.
    Never raises.

    schema: one of "CandidateList", "EvalResult"
    allowed_page_types: only consulted for "EvalResult" — when supplied, each
        page_draft.page_type must be a base type (entity/synthesis/source_note)
        or a member of this set, else the whole response fails validation.
        Callers pass the theme's current page_type_taxonomy keys, including any
        subtype registered earlier this session by the taxonomy-evolution
        mechanism. Omit (None) to fall back to format-only checking.
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
        if schema == "EvalResult":
            validator(data, allowed_page_types=allowed_page_types)
        else:
            validator(data)
        return data
    except Exception as e:
        logger.warning("validate_and_parse: validation failed — %s", e)
        return None
