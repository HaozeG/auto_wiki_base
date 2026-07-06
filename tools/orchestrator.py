#!/usr/bin/env python3
"""
Auto research harness orchestrator.

CLI usage:
    python tools/orchestrator.py research \\
        --query "transformer attention mechanisms" \\
        --max-candidates 10 \\
        --max-new-pages 5 \\
        --depth shallow

Requires: ANTHROPIC_API_KEY environment variable.
"""

import argparse
import html
import hashlib
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

# Ensure tools/ is importable
_TOOLS_DIR = Path(__file__).parent
sys.path.insert(0, str(_TOOLS_DIR))

import frontmatter
import graph_stats
import graph_topology
import relationship_links
import identity
from audit import AuditLog
from context_selector import select_context_pages
from domain_analysis import (
    DEFAULT_PAGE_TYPE_TAXONOMY,
    DEFAULT_REQUIRED_MEASUREMENT_FIELDS,
    THEME_PAGE_TYPE_LIBRARY,
    build_gap_manifest,
    build_structured_query,
    extract_evidence,
    propose_theme_profiles,
    source_grounded_snippets,
)
from qmd_runner import QmdRunner, assess_candidate_similarity, candidate_similarity_query, hard_title_duplicate_score
from quota import MAX_TOKENS_PER_SUBAGENT_OUTPUT, MIN_SECONDS_BETWEEN_CALLS, QuotaManager
from research_state import ResearchSessionState, list_sessions, write_key
from subagent_prompts import (
    CONTENT_MERGE_SYSTEM_PROMPT,
    DISCOVERY_SYSTEM_PROMPT,
    EVALUATION_SYSTEM_PROMPT,
    KEYWORD_RECOMMENDER_SYSTEM_PROMPT,
    PROFILE_ARCHITECT_SYSTEM_PROMPT,
    SYNTHESIS_SYSTEM_PROMPT,
)
from validate_output import extract_json_block, validate_and_parse

logger = logging.getLogger(__name__)

_PROJECT_ROOT = _TOOLS_DIR.parent
_WIKI_PAGES_DIR = _PROJECT_ROOT / "wiki" / "_pages"
_INDEX_MD = _PROJECT_ROOT / "wiki" / "index.md"
_LOG_MD = _PROJECT_ROOT / "wiki" / "log.md"
_CLAUDE_MD = _PROJECT_ROOT / "CLAUDE.md"
# Machine-curated, immutable-once-written snapshots of web-fetched content. This
# is the one place the harness writes under raw/ (see design doc §11 Provenance):
# it preserves the "raw is the source of truth" guarantee for the autonomous loop.
_RAW_CACHE_DIR = _PROJECT_ROOT / "raw" / "cache"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _generate_session_id() -> str:
    ts = datetime.now(timezone.utc).isoformat()
    return hashlib.md5(ts.encode()).hexdigest()[:8]


def _now_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _load_claude_md_block(block_name: str) -> dict:
    text = _CLAUDE_MD.read_text(encoding="utf-8")
    pattern = rf"```yaml\n\[{re.escape(block_name)}\](.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _normalize_page_type_taxonomy(value: dict | None) -> dict:
    taxonomy = dict(DEFAULT_PAGE_TYPE_TAXONOMY)
    for key, item in (value or {}).items():
        if isinstance(item, dict):
            taxonomy[key] = item
        else:
            taxonomy[key] = {"description": str(item)}
    return taxonomy


def _load_theme_profile() -> dict:
    profile = _load_claude_md_block("theme_profile")
    if not profile:
        return {}
    if "page_types" in profile:
        profile["page_types"] = _normalize_page_type_taxonomy(profile.get("page_types"))
    return profile


def _load_research_config() -> dict:
    config = _load_claude_md_block("research_config")
    theme_profile = _load_theme_profile()
    config.setdefault("qmd_command", ["uv", "run", "--no-sync", "qmd"])
    config.setdefault("research_state_dir", "wiki/research_state")
    config.setdefault("topic_similarity_min_score", 0.80)
    config.setdefault("near_duplicate_score", 0.90)
    config.setdefault("topic_saturation_hit_threshold", 2)
    config.setdefault("title_overlap_threshold", 0.8)
    config.setdefault("keyword_recommendation_limit", 5)
    config.setdefault("max_keyword_recommender_tokens", 6000)
    config.setdefault("keyword_recommender_model", None)
    config.setdefault("recent_audit_sessions_for_discovery", 10)
    config.setdefault("repeat_url_suppression", True)
    config.setdefault("domain_stopwords", [])
    config.setdefault("preferred_source_types", [
        "official documentation",
        "paper",
        "technical report",
        "implementation repository",
    ])
    config.setdefault("required_measurement_fields", list(DEFAULT_REQUIRED_MEASUREMENT_FIELDS))
    config["page_type_taxonomy"] = _normalize_page_type_taxonomy(config.get("page_type_taxonomy"))
    if theme_profile:
        config["theme_profile"] = theme_profile
        if theme_profile.get("source_preferences"):
            config["preferred_source_types"] = list(theme_profile["source_preferences"])
        if theme_profile.get("page_types"):
            config["page_type_taxonomy"] = _normalize_page_type_taxonomy(theme_profile["page_types"])
        if theme_profile.get("lint_priorities"):
            config["lint_priorities"] = list(theme_profile["lint_priorities"])
        if theme_profile.get("coverage_priorities"):
            config["coverage_priorities"] = list(theme_profile["coverage_priorities"])
        # Theme-specific overrides for domain_analysis.extract_evidence()/
        # build_gap_manifest() (see the note atop domain_analysis._MEASUREMENT_RE):
        # a theme profile may declare these so a non-hardware theme gets real
        # evidence extraction and coverage-gap detection instead of the
        # RISC-V-shaped defaults quietly no-oping. Not yet auto-proposed by
        # the profile-architect subagent/deterministic fallback — add them by
        # hand to [theme_profile] in CLAUDE.md when setting up a new theme,
        # the same way page_types is hand-edited after profile selection.
        if theme_profile.get("extraction_patterns"):
            config["extraction_patterns"] = theme_profile["extraction_patterns"]
        if theme_profile.get("coverage_tracked_page_types"):
            config["coverage_tracked_page_types"] = list(theme_profile["coverage_tracked_page_types"])
        if theme_profile.get("coverage_required_fields"):
            config["coverage_required_fields"] = list(theme_profile["coverage_required_fields"])
    return config


def _research_state_dir(research_config: dict) -> Path:
    state_dir = Path(research_config.get("research_state_dir", "wiki/research_state"))
    if not state_dir.is_absolute():
        state_dir = _PROJECT_ROOT / state_dir
    return state_dir


def _normalize_agent_profile(profile: dict, theme: str) -> dict:
    """Coerce an architect-subagent profile into the deterministic profile shape."""
    page_types = {}
    for name, spec in (profile.get("page_types") or {}).items():
        if isinstance(spec, dict):
            page_types[name] = {
                "description": str(spec.get("description", "")),
                "structured_fields": list(spec.get("structured_fields", []) or []),
            }
        else:
            page_types[name] = {"description": str(spec), "structured_fields": []}
    return {
        "id": str(profile.get("id", "")).strip() or "profile",
        "name": str(profile.get("name", "")).strip() or "Profile",
        "description": str(profile.get("description", "")).strip(),
        "page_types": page_types,
        "source_preferences": list(profile.get("source_preferences", []) or []),
        "coverage_priorities": list(profile.get("coverage_priorities", []) or []),
        "relationship_rules": list(profile.get("relationship_rules", []) or []),
        "lint_priorities": list(profile.get("lint_priorities", []) or []),
        "theme": theme,
    }


def _propose_profiles_via_agent(theme: str) -> list[dict] | None:
    """Ask the profile-architect subagent for organization profiles. Returns None
    on any failure so callers fall back to the deterministic proposer."""
    try:
        research_config = _load_research_config()
        manifest = {"theme": theme, "page_type_library": THEME_PAGE_TYPE_LIBRARY}
        raw = _call_subagent("profile_architect", manifest, research_config)
    except Exception as exc:  # noqa: BLE001 — offline/degraded → deterministic fallback
        logger.warning("profile-architect subagent unavailable (%s); using deterministic profiles", exc)
        return None
    data = validate_and_parse(raw, "ProfileList")
    if not data:
        return None
    profiles = [_normalize_agent_profile(p, theme) for p in data.get("profiles", [])]
    return profiles or None


def _profiles_cache_path(theme: str) -> Path:
    digest = hashlib.sha1(theme.strip().lower().encode("utf-8")).hexdigest()[:12]
    state_dir = _research_state_dir(_load_research_config())
    return state_dir / f"proposed_profiles_{digest}.json"


def _save_cached_profiles(theme: str, profiles: list[dict]) -> None:
    path = _profiles_cache_path(theme)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(profiles, indent=2, ensure_ascii=False), encoding="utf-8")


def _load_cached_profiles(theme: str) -> list[dict] | None:
    """Profiles proposed during the most recent `setup theme` listing, so the id
    the human picked still resolves even though agent output is non-deterministic."""
    path = _profiles_cache_path(theme)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data or None


def propose_profiles(theme: str, use_agent: bool = True) -> list[dict]:
    """Agent-generated organization profiles, with deterministic fallback.

    The chosen profile is what makes the wiki theme-agnostic: structure emerges
    from the theme via the architect subagent rather than a hardcoded rule table.
    """
    if use_agent:
        agentic = _propose_profiles_via_agent(theme)
        if agentic:
            return agentic
    return propose_theme_profiles(theme)


def select_theme_profile(theme: str, choice: str | None = None) -> dict:
    """Select an organization profile by id/name, defaulting to the first option.

    Prefers profiles cached from the most recent `setup theme` listing (so the id
    the human picked matches), then agent-generated, then deterministic."""
    profiles = _load_cached_profiles(theme) or propose_profiles(theme)
    if not profiles:
        raise ValueError(f"No theme profiles available for {theme!r}")
    if choice:
        normalized = choice.strip().lower().replace("-", "_").replace(" ", "_")
        for profile in profiles:
            candidates = {
                str(profile.get("id", "")).lower(),
                str(profile.get("name", "")).lower().replace("-", "_").replace(" ", "_"),
            }
            if normalized in candidates:
                return profile
        valid = ", ".join(str(profile["id"]) for profile in profiles)
        raise ValueError(f"Unknown organization choice {choice!r}; valid choices: {valid}")
    return profiles[0]


def _serializable_theme_profile(profile: dict) -> dict:
    return {
        "theme": profile.get("theme", ""),
        "organization_choice": profile.get("id", ""),
        "organization_name": profile.get("name", ""),
        "page_types": profile.get("page_types", {}),
        "relationship_rules": profile.get("relationship_rules", []),
        "source_preferences": profile.get("source_preferences", []),
        "coverage_priorities": profile.get("coverage_priorities", []),
        "lint_priorities": profile.get("lint_priorities", []),
        # Deliberate top-level hub concepts (optional; absent for themes/
        # profiles that don't declare any). Grouping key for the "Hub
        # Hierarchy" section in rebuild_index_from_frontmatter() — see
        # domain_analysis._risc_v_hub_hierarchy() docstring for why this is
        # a derived index view, not a forced page-creation step.
        "hub_hierarchy": profile.get("hub_hierarchy", []),
    }


def _replace_or_insert_yaml_block(text: str, block_name: str, data: dict) -> str:
    block = f"```yaml\n[{block_name}]\n{yaml.dump(data, sort_keys=False, allow_unicode=True)}```"
    pattern = rf"```yaml\n\[{re.escape(block_name)}\].*?```"
    if re.search(pattern, text, flags=re.DOTALL):
        return re.sub(pattern, block, text, count=1, flags=re.DOTALL)
    insert_before = re.search(r"\n## Research Configuration\n", text)
    if insert_before:
        return text[:insert_before.start()] + "\n## Theme Profile\n\n" + block + "\n" + text[insert_before.start():]
    return text.rstrip() + "\n\n## Theme Profile\n\n" + block + "\n"


def write_theme_profile(profile: dict) -> None:
    """Persist a selected first-run theme profile into CLAUDE.md."""
    text = _CLAUDE_MD.read_text(encoding="utf-8") if _CLAUDE_MD.exists() else "# LLM Wiki\n"
    text = _replace_or_insert_yaml_block(text, "theme_profile", _serializable_theme_profile(profile))
    _CLAUDE_MD.write_text(text, encoding="utf-8")


def setup_theme(theme: str, choice: str | None = None, write: bool = True) -> dict:
    profile = select_theme_profile(theme, choice)
    if write:
        write_theme_profile(profile)
    return _serializable_theme_profile(profile)


def _attach_theme_profile(audit: AuditLog, research_config: dict) -> None:
    setter = getattr(audit, "set_theme_profile", None)
    if callable(setter):
        setter(research_config.get("theme_profile") or None)


def _load_processed_urls() -> set[str]:
    """Extract URLs already processed from wiki/log.md."""
    if not _LOG_MD.exists():
        return set()
    text = _LOG_MD.read_text(encoding="utf-8")
    return set(re.findall(r"https?://\S+", text))


def _clean_model_name(model: str | None) -> str | None:
    if not model:
        return None
    return re.sub(r"\x1b\[[\d;]*m", "", model).strip() or None


def _audit_dir() -> Path:
    return _PROJECT_ROOT / "wiki" / "audit"


def _recent_audit_files(limit: int) -> list[Path]:
    audit_dir = _audit_dir()
    if not audit_dir.exists():
        return []
    return sorted(
        audit_dir.glob("research_*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )[:limit]


def _load_recent_discovery_history(research_config: dict) -> dict:
    """Summarize recent audit URLs/titles for repeat suppression and keyword planning."""
    limit = int(research_config.get("recent_audit_sessions_for_discovery", 10) or 0)
    url_counts: dict[str, int] = {}
    previous_queries: list[str] = []
    repeated_results: list[dict] = []
    rejected_results: list[dict] = []
    zero_yield_queries: list[dict] = []
    seen_repeated: set[str] = set()
    seen_queries: set[str] = set()

    for path in _recent_audit_files(limit):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        summary = data.get("session_summary") or {}
        query = data.get("query")
        # A session can evaluate a full candidate budget and write nothing —
        # e.g. session e545ec7c ("RISC-V verification formal methods hardware
        # bug fuzzing test...") evaluated 10 candidates, all rejected, even
        # after depth escalation. Surface these so the keyword recommender can
        # steer away from repeating a query shape that's already proven
        # unproductive, instead of re-spending a full candidate budget on it.
        if query and summary.get("candidates_evaluated", 0) >= 3 and summary.get("pages_written", 0) == 0:
            zero_yield_queries.append({
                "query": str(query)[:240],
                "candidates_evaluated": summary.get("candidates_evaluated"),
                "pages_rejected_by_subagent": summary.get("pages_rejected_by_subagent"),
            })
        candidate_queries = [data.get("query")]
        candidate_queries.extend(data.get("discovery_queries_used", []) or [])
        candidate_queries.extend(
            item.get("query")
            for item in data.get("keyword_recommendations", []) or []
            if isinstance(item, dict)
        )
        for q in candidate_queries:
            if not q:
                continue
            q = str(q).strip()
            if q and q.lower() not in seen_queries:
                previous_queries.append(q[:240])
                seen_queries.add(q.lower())
        for invocation in data.get("invocations", []):
            manifest = invocation.get("input_manifest", {})
            candidate = manifest.get("candidate", {})
            url = candidate.get("url") or invocation.get("url")
            if not url:
                continue
            title = candidate.get("title", "")
            url_counts[url] = url_counts.get(url, 0) + 1
            reason = invocation.get("skipped_reason")
            if reason:
                rejected_results.append({
                    "url": url,
                    "title": title,
                    "reason": str(reason)[:300],
                })
            if url_counts[url] > 1 and url not in seen_repeated:
                repeated_results.append({"url": url, "title": title, "count": url_counts[url]})
                seen_repeated.add(url)

    return {
        "seen_urls": set(url_counts),
        "previous_queries": previous_queries[:40],
        "repeated_results": repeated_results[:20],
        "rejected_results": rejected_results[:20],
        "zero_yield_queries": zero_yield_queries[:20],
    }


def _wiki_is_mature() -> bool:
    text = _CLAUDE_MD.read_text(encoding="utf-8")
    match = re.search(r"graph_maturity:\s*(true|false)", text)
    return bool(match and match.group(1) == "true")


def _load_system_state() -> dict:
    return _load_claude_md_block("system_state")


def _write_system_state(state: dict) -> None:
    if not _CLAUDE_MD.exists():
        return
    text = _CLAUDE_MD.read_text(encoding="utf-8")
    text = _replace_or_insert_yaml_block(text, "system_state", state)
    _CLAUDE_MD.write_text(text, encoding="utf-8")


def _maybe_transition_maturity(session_id: str) -> None:
    """Refresh connectivity metrics in [system_state] and flip graph_maturity
    when the connectivity predicate (orphan_fraction + median) is satisfied.

    This is the writer the design always implied but that never existed:
    previously nothing flipped graph_maturity, and the threshold was a gameable
    mean. Now maturity is connectivity-based (see graph_stats.is_mature)."""
    stats = graph_stats.compute_stats(_WIKI_PAGES_DIR)
    state = _load_system_state()
    state["orphan_fraction"] = stats.get("orphan_fraction", 1.0)
    state["median_inbound_links"] = stats.get("median_inbound_links", 0.0)
    state["mean_inbound_links"] = stats.get("mean_inbound_links", 0.0)

    # Additive small-world topology metrics (Graph Topology Philosophy). Do not
    # gate graph_maturity on these yet — see the Phase 3b scope guardrail in
    # the harness improvement plan; they're informational until at least one
    # real run has produced before/after numbers to calibrate thresholds.
    try:
        topology = graph_topology.compute_topology_stats(_WIKI_PAGES_DIR)
        state["clustering_coefficient"] = topology.get("clustering_coefficient", 0.0)
        state["avg_path_length"] = topology.get("avg_path_length")
        state["connected_components"] = topology.get("connected_components", 0)
    except Exception as e:
        logger.warning("graph_topology stats failed (non-fatal, informational only): %s", e)

    transitioned = False
    if not state.get("graph_maturity") and stats.get("mature"):
        state["graph_maturity"] = True
        transitioned = True
    _write_system_state(state)
    if transitioned:
        entry = (
            f"## [{_now_date()}] transition | cold_start → mature\n"
            f"session_id: {session_id}\n"
            f"pages_at_transition: {stats.get('page_count', 0)}\n"
            f"orphan_fraction: {stats.get('orphan_fraction')}\n"
            f"median_inbound_links: {stats.get('median_inbound_links')}\n"
            f"mean_inbound_links: {stats.get('mean_inbound_links')}\n"
        )
        if _LOG_MD.exists():
            _LOG_MD.write_text(_LOG_MD.read_text(encoding="utf-8").rstrip() + "\n\n" + entry,
                               encoding="utf-8")
        print(f"[{session_id}] graph maturity transition: cold_start → mature")


def _max_linking_debt(research_config: dict) -> int:
    try:
        return int(research_config.get("max_linking_debt", 5))
    except (TypeError, ValueError):
        return 5


def _current_linking_debt(session_state: ResearchSessionState) -> int:
    """Pages created this session that still have 0 inbound links.

    Computed from live frontmatter (reusing the canonical parser) rather than a
    drifting counter, so within-session links that later point at an earlier page
    correctly reduce the debt."""
    debt = 0
    for stem in session_state.created_page_stems:
        page = _find_page_by_filename(stem)
        if page is None:
            continue
        fm, _ = frontmatter.parse_page(page)
        try:
            inbound = int(fm.get("inbound_links", 0) or 0)
        except (TypeError, ValueError):
            inbound = 0
        if inbound == 0:
            debt += 1
    session_state.linking_debt = debt
    return debt


def _get_wiki_topic_summary() -> str:
    if not _INDEX_MD.exists():
        return ""
    text = _INDEX_MD.read_text(encoding="utf-8")
    lines = text.split("\n")
    summary_lines = []
    for line in lines[:20]:
        stripped = line.strip()
        if stripped:
            summary_lines.append(stripped)
    return " ".join(summary_lines)[:1000]


def _get_repo_research_theme() -> str:
    """Return a compact, domain-level theme for the current wiki/repo."""
    parts: list[str] = []
    readme = _PROJECT_ROOT / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        match = re.search(r"The current example wiki is focused on ([^.]+)\.", text)
        if match:
            focus = re.split(r",\s*but\b", match.group(1).strip(), maxsplit=1)[0]
            parts.append(f"Current wiki focus: {focus}.")

    if _INDEX_MD.exists():
        text = _INDEX_MD.read_text(encoding="utf-8")
        page_count = None
        source_count = None
        representative_pages = []
        tag_counts: dict[str, int] = {}
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("Last updated:"):
                pages_match = re.search(r"Pages:\s*(\d+)", stripped)
                sources_match = re.search(r"Sources:\s*(\d+)", stripped)
                if pages_match:
                    page_count = pages_match.group(1)
                if sources_match:
                    source_count = sources_match.group(1)
            if not (stripped.startswith("| [") and "](" in stripped):
                continue
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if len(cells) < 3:
                continue
            page_cell, summary, tags_cell = cells[:3]
            page_match = re.search(r"\[([^\]]+)\]", page_cell)
            page_name = page_match.group(1) if page_match else page_cell
            for tag in [t.strip() for t in tags_cell.split(",") if t.strip()]:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            if len(representative_pages) < 10:
                representative_pages.append(f"{page_name}: {summary}")
        if page_count or source_count:
            stats = []
            if page_count:
                stats.append(f"{page_count} pages")
            if source_count:
                stats.append(f"{source_count} sources")
            parts.append("Wiki scale: " + ", ".join(stats) + ".")
        if tag_counts:
            top_tags = sorted(tag_counts.items(), key=lambda item: (-item[1], item[0]))[:12]
            parts.append("Recurring tags: " + ", ".join(tag for tag, _count in top_tags) + ".")
        if representative_pages:
            parts.append("Representative pages: " + "; ".join(representative_pages) + ".")

    if not parts:
        parts.append(_get_wiki_topic_summary())
    return " ".join(parts)[:1800]


def _get_concept_gaps() -> list[str]:
    """Extract concepts with no dedicated page from the Concept Index."""
    if not _INDEX_MD.exists():
        return []
    text = _INDEX_MD.read_text(encoding="utf-8")
    gaps = re.findall(r"\*\*(.+?)\*\*:.*?no dedicated page", text)
    return gaps


_STOP_WORDS = {"the", "a", "an", "of", "for", "in", "and", "on", "with", "by", "to", "is"}


def _title_word_overlap(title: str, stem: str) -> float:
    """
    Return hard-duplicate similarity between a candidate title and filename stem.

    This is intentionally stricter than broad topic similarity: one shared
    vendor/family token should not suppress stack subtopics around that vendor.
    """
    return hard_title_duplicate_score(title, stem, stopwords=_STOP_WORDS)


def _title_matches_existing(title: str, extra_stems: set[str] | None = None,
                             overlap_threshold: float = 0.8) -> str | None:
    """
    Return matched filename stem if title is too similar to an existing page or
    a page already written this session (extra_stems).
    Returns None if no match.
    """
    if not title:
        return None

    # Identity key for an alias-aware pre-filter. This is a cheap, NON-authoritative
    # pre-fetch optimization (allowed to miss); the orchestrator's write gate does
    # the deterministic, authoritative identity hard-block (see _write_approved_entry).
    title_key = identity.normalize_canonical(title)

    # Check pages written this session first (not yet in index)
    if extra_stems:
        for stem in extra_stems:
            if _title_word_overlap(title, stem) >= overlap_threshold:
                return stem
            if title_key and identity.normalize_canonical(stem) == title_key:
                return stem

    # Check existing wiki pages on disk
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        if _title_word_overlap(title, p.stem) >= overlap_threshold:
            return p.stem
        if title_key:
            fm, _ = frontmatter.parse_page(p)
            for surface in [fm.get("canonical_name") or "", *(fm.get("aliases") or [])]:
                if surface and identity.normalize_canonical(str(surface)) == title_key:
                    return p.stem
    return None


def _synthesis_gap_clusters(min_cluster_size: int = 3) -> list[tuple[str, list[str]]]:
    """
    Find tag clusters with >= min_cluster_size entity(-subtype) pages that
    have no synthesis page covering them. Returns [(tag, [uncovered page
    stems])], sorted by cluster size descending. Shared by
    _check_synthesis_gaps() (human-readable log strings) and the research
    loop's synthesis-candidate generation (Phase 3 — see wiki/log.md's
    repeated "deferred_for_human: Synthesis gaps persist across sessions"
    notes; this was previously only ever logged, never acted on).

    Deliberately does NOT filter on `fm.get("type") == "entity"`: the design
    doc says a subtype page (hardware_target/benchmark_result/...) "is still
    an entity for retrieval, identity, and dedup," but in practice the eval
    subagent writes the literal subtype name into `type` (e.g.
    `type: hardware_target`), not `type: entity, subtype: hardware_target` —
    confirmed against both this run and the original research/riscv-ai-accelerator
    run's committed pages. An entity-only filter therefore silently excludes
    most of an optimization_first-profile wiki's actual content (18/61
    hardware_target + 13 benchmark_result + 6 optimization_recipe pages here,
    vs. 22 type:entity pages), and those subtype pages are exactly where tags
    are most consistently populated — this filter was the main reason
    synthesis-candidate generation never found a real cluster to work with.
    """
    tag_to_pages: dict[str, list[str]] = {}
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, _ = frontmatter.parse_page(p)
        if fm.get("type") != "synthesis":
            for tag in fm.get("tags", []) or []:
                tag_to_pages.setdefault(tag, []).append(p.stem)

    # Collect all entity pages already named in a synthesis connected_entities list
    covered: set[str] = set()
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, _ = frontmatter.parse_page(p)
        if fm.get("type") == "synthesis":
            covered.update(fm.get("connected_entities", []))

    clusters = []
    for tag, pages in sorted(tag_to_pages.items(), key=lambda x: -len(x[1])):
        uncovered = [pg for pg in pages if pg not in covered]
        if len(uncovered) >= min_cluster_size:
            clusters.append((tag, uncovered))
    return clusters


def _check_synthesis_gaps() -> list[str]:
    """
    Find tag clusters with 3+ entity pages that have no synthesis page covering them.
    Returns a list of human-readable gap descriptions for the log.
    """
    gaps = []
    for tag, uncovered in _synthesis_gap_clusters():
        sample = ", ".join(uncovered[:3])
        gaps.append(
            f"tag='{tag}': {len(uncovered)} entity pages without synthesis coverage "
            f"(e.g. {sample}{'...' if len(uncovered) > 3 else ''})"
        )
    return gaps


def _hub_promotion_candidates(min_cluster_size: int | None = None) -> list[dict]:
    """Phase 2c: propose promoting a tag cluster *within* a declared top-level
    hub into a named sub-hub nested under it, once the cluster grows to
    `synthesis_gap_min_cluster_size` (reused, same threshold as
    _synthesis_gap_clusters — a cluster large enough to deserve its own
    synthesis page is also large enough to deserve its own sub-hub label).

    This is the "continuously build subtype hierarchy along the exploration"
    mechanism: hub_hierarchy in [theme_profile] declares only the top level
    at theme setup; finer structure (e.g. "XuanTie C9-series cores" under
    "Vendor RISC-V Core Families") emerges from real page-tag clustering as
    the wiki grows, surfaced here for human review during routine lint —
    never auto-applied, same principle as retrospective lint's MERGE/DELETE
    gate. Returns [{parent_hub_id, parent_label, tag, member_pages}], not
    persisted anywhere until a human confirms and a real synthesis page
    materializes the sub-hub (mirrors 2a/2b: no forced page creation)."""
    hub_hierarchy = _load_claude_md_block("theme_profile").get("hub_hierarchy") or []
    if not hub_hierarchy:
        return []
    threshold = min_cluster_size or int(
        _load_claude_md_block("research_config").get("synthesis_gap_min_cluster_size", 3) or 3
    )

    pages_by_subtype: dict[str, list[Path]] = {}
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, _ = frontmatter.parse_page(p)
        pages_by_subtype.setdefault(fm.get("type", "entity"), []).append(p)

    covered: set[str] = set()
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, _ = frontmatter.parse_page(p)
        if fm.get("type") == "synthesis":
            covered.update(fm.get("connected_entities", []))

    candidates = []
    for hub in hub_hierarchy:
        subtype = hub.get("subtype", "")
        members = pages_by_subtype.get(subtype, [])
        if len(members) < threshold:
            continue
        tag_to_pages: dict[str, list[str]] = {}
        for p in members:
            fm, _ = frontmatter.parse_page(p)
            for tag in fm.get("tags", []) or []:
                tag_to_pages.setdefault(tag, []).append(p.stem)
        for tag, stems in sorted(tag_to_pages.items(), key=lambda x: -len(x[1])):
            uncovered = [s for s in stems if s not in covered]
            if len(uncovered) >= threshold:
                candidates.append({
                    "parent_hub_id": hub.get("hub_id", ""),
                    "parent_label": hub.get("label", ""),
                    "tag": tag,
                    "member_pages": uncovered,
                })
    return candidates


def _check_hub_promotions() -> list[str]:
    """Human-readable sub-hub promotion candidates for the routine lint log
    (same pairing as _synthesis_gap_clusters/_check_synthesis_gaps)."""
    lines = []
    for c in _hub_promotion_candidates():
        sample = ", ".join(c["member_pages"][:3])
        more = "..." if len(c["member_pages"]) > 3 else ""
        lines.append(
            f"hub='{c['parent_label']}' tag='{c['tag']}': {len(c['member_pages'])} pages "
            f"could form a sub-hub (e.g. {sample}{more})"
        )
    return lines


def _extract_section(body: str, heading: str) -> str:
    """Return the text under a '## heading' section, up to the next '## '."""
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(body)
    return match.group(1).strip() if match else ""


def _summarize_page_for_synthesis(path: Path) -> dict:
    fm, body = frontmatter.parse_page(path)
    lines = [line for line in body.split("\n") if line.strip()]
    summary = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        summary = stripped
        break
    return {
        "filename": path.stem,
        "canonical_name": fm.get("canonical_name") or path.stem,
        "tags": fm.get("tags", []) or [],
        "summary": summary[:400],
        "key_claims": _extract_section(body, "Key Claims")[:800],
        "structured_fields": fm.get("structured_fields") or {},
    }


def _build_synthesis_manifest(tag: str, page_stems: list[str], research_config: dict) -> dict:
    cluster_pages = []
    for stem in page_stems[:8]:
        page = _find_page_by_filename(stem)
        if page is not None:
            cluster_pages.append(_summarize_page_for_synthesis(page))
    existing_titles = []
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, body = frontmatter.parse_page(p)
        if fm.get("type") == "synthesis":
            for line in body.split("\n"):
                if line.strip().startswith("# "):
                    existing_titles.append(line.strip().lstrip("#").strip())
                    break
    return {
        "gap_tag": tag,
        "cluster_pages": cluster_pages,
        "existing_synthesis_titles": existing_titles,
        "synthesis_template": _build_page_templates().get("synthesis_template", ""),
        "page_type_taxonomy": research_config.get("page_type_taxonomy", {}),
    }


def _generate_synthesis_candidate(
    session_state: ResearchSessionState,
    quota: QuotaManager,
    audit: AuditLog,
    research_config: dict,
    session_written_stems: set[str],
) -> str | None:
    """
    Attempt to fill one synthesis-coverage gap per session, gated by the same
    budget as entity pages. The research loop previously only ever *logged*
    synthesis gaps (see _check_synthesis_gaps, called every session) without
    acting on them — wiki/log.md repeatedly deferred this to a human
    ("Synthesis gaps persist across sessions... out of scope for this
    page-count-focused session"), and of the 3 synthesis pages that existed
    before this change, 2 were written manually during a one-off retrospective
    lint pass, not by the research loop itself. This closes that gap without
    a new subagent-orchestration pattern: same call/validate/pipeline/write
    flow as an entity draft, just sourced from existing wiki content instead
    of a freshly fetched external candidate.
    """
    if quota.pages_exceeded() or quota.api_calls_exceeded():
        return None
    clusters = _synthesis_gap_clusters(
        min_cluster_size=int(research_config.get("synthesis_gap_min_cluster_size", 3) or 3)
    )
    if not clusters:
        return None
    tag, page_stems = clusters[0]
    manifest = _build_synthesis_manifest(tag, page_stems, research_config)
    if len(manifest["cluster_pages"]) < 2:
        return None
    ev_idx = audit.record_invocation("synthesis", manifest)
    try:
        time.sleep(MIN_SECONDS_BETWEEN_CALLS)
        quota.record_api_call()
        raw = _call_subagent("synthesis", manifest, research_config)
    except Exception as e:
        logger.warning("Synthesis subagent call failed for tag=%r: %s", tag, e)
        audit.record_response(ev_idx, str(e), schema_valid=False)
        return None
    result = validate_and_parse(raw, "SynthesisResult")
    audit.record_response(ev_idx, raw, schema_valid=(result is not None))
    if result is None or result.get("decision") != "approve":
        reason = (result or {}).get("rejection_reason") or "malformed_or_rejected"
        audit.record_skip(ev_idx, f"synthesis_reject: {reason}")
        print(f"[{session_state.session_id}] Synthesis candidate for tag={tag!r} rejected: {reason}")
        return None
    draft = result["page_draft"]
    # Backfill frontmatter.sources from the cluster pages' own paths (a synthesis
    # page draws from existing, already-grounded wiki content rather than a
    # freshly fetched external source). Not in the literal CLAUDE.md synthesis
    # template, but eval_summary.py's Layer 1 EMPTY_SOURCES check applies to
    # every page type unconditionally, and the original run's manually-written
    # synthesis pages all populate this the same way (paths to their
    # connected_entities' page files) — confirmed against
    # wiki/_pages/synthesis/edge_ai_soc_design_space.md on research/riscv-ai-accelerator.
    # Without this, every synthesis draft fails Layer 1 with EMPTY_SOURCES and
    # _generate_synthesis_candidate() can never actually write a page — this was
    # caught live testing the v2 replication run after the type-filter fix made
    # gap-detection work again.
    draft_fm = draft.setdefault("frontmatter", {})
    if not draft_fm.get("sources"):
        # Relative to _WIKI_PAGES_DIR's grandparent (the wiki root), not the
        # module-level _PROJECT_ROOT constant, so this stays correct when
        # _WIKI_PAGES_DIR is patched elsewhere (tests) or the wiki root ever
        # differs from _PROJECT_ROOT.
        wiki_root = _WIKI_PAGES_DIR.parent.parent
        cluster_paths = []
        for stem in page_stems:
            page = _find_page_by_filename(stem)
            if page is None:
                continue
            try:
                cluster_paths.append(str(page.relative_to(wiki_root)))
            except ValueError:
                cluster_paths.append(str(page))
        if cluster_paths:
            draft_fm["sources"] = cluster_paths
    passes, pipeline_result = _run_eval_pipeline(draft)
    audit.record_pipeline_result(
        ev_idx,
        filename=draft.get("filename", "unknown"),
        layer1_pass=pipeline_result.get("layer1_pass", False),
        layer2_pass=pipeline_result.get("layer2_pass", True),
        layer3_triggered=pipeline_result.get("layer3_triggered", False),
        final_decision=pipeline_result.get("final_decision", "rejected"),
        rejection_detail=pipeline_result.get("rejection_detail"),
    )
    if not passes:
        print(f"[{session_state.session_id}] Synthesis draft for tag={tag!r} failed eval pipeline: "
              f"{pipeline_result.get('rejection_detail')}")
        return None
    synthetic_source_key = f"synthesis-gap:{tag}"
    page_path = _write_draft_once(draft, synthetic_source_key, session_state, quota, session_written_stems)
    if page_path is None:
        return None
    audit.record_page_written(ev_idx, page_path.name)
    print(f"[{session_state.session_id}] Synthesis page generated for gap tag={tag!r}: {page_path.name}")
    return page_path.name


def fetch_resource(url: str, retries: int = 2) -> str | None:
    """Fetch URL content as text. Returns None on failure after retries."""
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (LLM-Wiki-Harness/1.0)"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw = resp.read()
                # Try UTF-8, fall back to latin-1
                try:
                    return raw.decode("utf-8")
                except UnicodeDecodeError:
                    return raw.decode("latin-1", errors="replace")
        except Exception as e:
            logger.warning("fetch_resource: attempt %d failed for %s — %s", attempt + 1, url, e)
            if attempt < retries:
                time.sleep(2)
    return None


# ---------------------------------------------------------------------------
# Source-aware content extraction
# ---------------------------------------------------------------------------

_ARXIV_ABS_RE = re.compile(r"arxiv\.org/abs/([\w.]+)")
_GH_REPO_RE   = re.compile(r"github\.com/([^/]+)/([^/?#]+)/?(?:[?#].*)?$")
_GH_PR_RE     = re.compile(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)")
_GH_BLOB_RE   = re.compile(r"github\.com/([^/]+)/([^/]+)/blob/([^/?#]+)/([^?#]+)")


def _looks_like_html(content: str) -> bool:
    head = content[:1000].lower()
    return "<html" in head or "<!doctype" in head or ("<body" in head and "</" in head)


def _strip_rendered_html(content: str) -> str:
    """Convert rendered HTML shells into compact visible text."""
    text = re.sub(r"<!--.*?-->", " ", content, flags=re.DOTALL)
    text = re.sub(
        r"<(script|style|noscript|template|svg|canvas)\b[^>]*>.*?</\1>",
        " ",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(
        r"<(nav|header|footer|aside|form)\b[^>]*>.*?</\1>",
        " ",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</(p|div|section|article|li|h[1-6]|tr)>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    lines = []
    seen = set()
    for line in text.splitlines():
        line = re.sub(r"\s{2,}", " ", line).strip()
        if not line:
            continue
        lower = line.lower()
        if lower in seen:
            continue
        if len(line) <= 20 and lower in {
            "skip to content", "sign in", "sign up", "pricing", "features", "resources",
            "navigation menu", "main navigation", "footer",
        }:
            continue
        lines.append(line)
        seen.add(lower)
    return "\n".join(lines).strip()


def _content_is_boilerplate_or_thin(content: str, *, was_html: bool = False) -> bool:
    text = content.strip()
    text_chars = len(re.sub(r"\s", "", text))
    if text_chars < 500:
        return True

    lower = text.lower()
    markers = [
        "webpack", "__next_data__", "document.", "window.", "addEventListener",
        "font-family", "background-color", "box-sizing", "display:flex",
        "display: flex", "var(--", ".css-", "github.com",
    ]
    marker_hits = sum(lower.count(marker.lower()) for marker in markers)
    brace_noise = lower.count("{") + lower.count("}") + lower.count("function(")
    words = max(1, len(re.findall(r"\w+", lower)))
    if marker_hits >= 8 and marker_hits / words > 0.02:
        return True
    if was_html and brace_noise > text_chars / 25:
        return True
    return False


def _normalize_source_text(content: str) -> tuple[str, bool]:
    was_html = _looks_like_html(content)
    if was_html:
        return _strip_rendered_html(content), True
    return content, False


def _content_or_enriched_snippet(content: str | None, title: str, snippet: str, url: str) -> str | None:
    if content is None:
        enriched = _enrich_snippet(title, snippet)
        if not enriched:
            return None
        logger.info("fetch failed for %s — using enriched DDG snippet (%d chars)", url, len(enriched))
        return enriched

    if content[:4] in ("%PDF", b"%PDF"[:4] if isinstance(content, bytes) else ""):
        logger.info("binary/PDF content for %s — using enriched snippet", url)
        return _enrich_snippet(title, snippet) or snippet

    normalized, was_html = _normalize_source_text(content)
    if _content_is_boilerplate_or_thin(normalized, was_html=was_html):
        enriched = _enrich_snippet(title, snippet)
        text_chars = len(re.sub(r"\s", "", normalized))
        if enriched:
            logger.info("boilerplate/thin content (%d text chars) for %s — using enriched snippet", text_chars, url)
            return enriched
        logger.info("boilerplate/thin content (%d text chars) for %s — keeping cleaned excerpt", text_chars, url)
        return normalized[:2000]
    return normalized


def _fetch_arxiv(url: str) -> str | None:
    """For arxiv.org/abs/<id>: fetch abstract + attempt full HTML body."""
    m = _ARXIV_ABS_RE.search(url)
    if not m:
        return None
    arxiv_id = m.group(1)
    abs_html = fetch_resource(f"https://arxiv.org/abs/{arxiv_id}")
    abstract = ""
    if abs_html:
        bq = re.search(r'class="abstract[^"]*"[^>]*>(.*?)</blockquote>', abs_html, re.DOTALL)
        if bq:
            abstract = re.sub(r"<[^>]+>", " ", bq.group(1)).strip()
    html_content = fetch_resource(f"https://arxiv.org/html/{arxiv_id}")
    if html_content and len(html_content) > 1000:
        stripped = re.sub(r"<[^>]+>", " ", html_content)
        stripped = re.sub(r"\s{2,}", " ", stripped).strip()
        return f"[arXiv abstract]\n{abstract}\n\n[Paper body excerpt]\n{stripped[:5000]}"
    return abstract or None


def _fetch_github_readme(owner: str, repo: str) -> str | None:
    """Fetch plain-text README from raw.githubusercontent.com."""
    for branch in ("HEAD", "main", "master"):
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md"
        content = fetch_resource(raw_url)
        if content and len(content.strip()) > 100:
            return f"[GitHub README: {owner}/{repo}]\n\n{content[:6000]}"
    return None


def _fetch_github_pr(owner: str, repo: str, pr_num: str) -> str | None:
    """Fetch PR title and description via GitHub REST API."""
    import json as _json
    import os as _os
    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_num}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "LLM-Wiki-Harness/1.0",
    }
    token = _os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = _json.loads(resp.read().decode())
        title = data.get("title", "")
        body  = data.get("body") or "(no description)"
        base  = data.get("base", {}).get("ref", "")
        head  = data.get("head", {}).get("ref", "")
        return (
            f"[GitHub PR #{pr_num}: {title}]\n"
            f"Merges {head} → {base}\n\n"
            f"{body[:4000]}"
        )
    except Exception as e:
        logger.warning("_fetch_github_pr failed for %s/%s#%s: %s", owner, repo, pr_num, e)
        return None


def _fetch_github_blob(owner: str, repo: str, branch: str, path: str) -> str | None:
    """Fetch a GitHub blob URL as raw source text."""
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    content = fetch_resource(raw_url)
    if content and len(content.strip()) > 20:
        return f"[GitHub file: {owner}/{repo}/{branch}/{path}]\n\n{content[:6000]}"
    return None


def _fetch_github(url: str) -> str | None:
    """Dispatch to PR, file, or README fetch based on URL shape."""
    m = _GH_PR_RE.search(url)
    if m:
        return _fetch_github_pr(*m.groups())
    m = _GH_BLOB_RE.search(url)
    if m:
        return _fetch_github_blob(*m.groups())
    m = _GH_REPO_RE.search(url)
    if m:
        return _fetch_github_readme(*m.groups())
    return None


def _fetch_smart(url: str, retries: int = 2) -> str | None:
    """Source-aware fetch: special handling for arXiv and GitHub, generic fallback."""
    lower = url.lower()
    if "arxiv.org/abs/" in lower:
        result = _fetch_arxiv(url)
        if result:
            return result
    if "github.com/" in lower:
        result = _fetch_github(url)
        if result:
            return result
    return fetch_resource(url, retries=retries)


def _snapshot_source(url: str, content: str) -> str | None:
    """Write fetched content to an immutable content-addressed snapshot under
    raw/cache/ and return its project-relative path (skips if already present).

    This makes citations reproducible: a page's `sources` points at the local
    snapshot rather than a bare live URL that may change or disappear."""
    if not content:
        return None
    digest = hashlib.sha1(f"{url}\n{content}".encode("utf-8")).hexdigest()[:16]
    _RAW_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _RAW_CACHE_DIR / f"{digest}.md"
    if not path.exists():
        header = (f"<!-- source_url: {url}\n"
                  f"     fetched_at: {datetime.now(timezone.utc).isoformat()} -->\n\n")
        path.write_text(header + content, encoding="utf-8")
    return str(path.relative_to(_PROJECT_ROOT))


# ---------------------------------------------------------------------------
# Subagent API call
# ---------------------------------------------------------------------------

def _call_subagent(subagent_type: str, manifest: dict, research_config: dict) -> str:
    """
    Make a single Anthropic API call with the given manifest as user content.
    Returns the raw response string.
    Raises on API failure (caller handles).
    """
    try:
        import anthropic  # noqa: PLC0415
    except ImportError:
        raise RuntimeError("anthropic package not installed; run: pip install anthropic")

    client = anthropic.Anthropic()

    # Prefer env-var model so the harness works with any compatible API endpoint
    # (e.g. DeepSeek via ANTHROPIC_BASE_URL). Fall back to a known Anthropic model.
    model = (
        os.environ.get("ANTHROPIC_DEFAULT_HAIKU_MODEL")
        or os.environ.get("CLAUDE_CODE_SUBAGENT_MODEL")
        or "claude-haiku-4-5-20251001"
    )
    # Strip real terminal ANSI escape bytes, but preserve provider-specific
    # suffixes such as DeepSeek's literal "[1m]" thinking budget marker.
    model = _clean_model_name(model) or "claude-haiku-4-5-20251001"

    if subagent_type == "discovery":
        # No current caller passes subagent_type="discovery" — _ddg_discover()
        # ranks/filters candidates deterministically instead. Branch kept for
        # if/when an LLM ranking pass over DDG results is wired back in; see
        # the note atop DISCOVERY_SYSTEM_PROMPT in subagent_prompts.py.
        system = DISCOVERY_SYSTEM_PROMPT
        max_tokens = research_config.get("max_discovery_subagent_tokens", 3000)
    elif subagent_type == "content_merge":
        system = CONTENT_MERGE_SYSTEM_PROMPT
        max_tokens = research_config.get("max_eval_subagent_tokens", 6000)
    elif subagent_type == "profile_architect":
        system = PROFILE_ARCHITECT_SYSTEM_PROMPT
        max_tokens = research_config.get("max_eval_subagent_tokens", 6000)
    elif subagent_type == "synthesis":
        system = SYNTHESIS_SYSTEM_PROMPT
        max_tokens = research_config.get("max_eval_subagent_tokens", 6000)
    else:
        system = EVALUATION_SYSTEM_PROMPT
        max_tokens = research_config.get("max_eval_subagent_tokens", 6000)

    max_tokens = min(max_tokens, MAX_TOKENS_PER_SUBAGENT_OUTPUT)

    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": json.dumps(manifest)}],
    )
    if message.stop_reason == "max_tokens":
        logger.warning(
            "_call_subagent: hit max_tokens (%d) — output truncated. "
            "Increase max_eval_subagent_tokens in research_config.",
            max_tokens,
        )
    for block in message.content:
        if hasattr(block, "text"):
            return block.text
    raise RuntimeError(
        f"No text block in subagent response (stop={message.stop_reason}, "
        f"blocks={[type(b).__name__ for b in message.content]})"
    )


def _keyword_recommender_model(research_config: dict) -> str:
    model = (
        research_config.get("keyword_recommender_model")
        or os.environ.get("ANTHROPIC_MODEL")
        or os.environ.get("ANTHROPIC_DEFAULT_OPUS_MODEL")
        or os.environ.get("ANTHROPIC_DEFAULT_SONNET_MODEL")
        or "claude-opus-4-5-20251101"
    )
    return _clean_model_name(str(model)) or "claude-opus-4-5-20251101"


def _normalize_keyword_plan(data: dict, max_keywords: int, model: str, source: str) -> dict:
    raw_keywords = data.get("recommended_keywords", [])
    keywords: list[dict] = []
    seen_queries: set[str] = set()
    if isinstance(raw_keywords, list):
        for item in raw_keywords:
            if not isinstance(item, dict):
                continue
            query = str(item.get("query", "")).strip()
            if not query or query.lower() in seen_queries:
                continue
            seen_queries.add(query.lower())
            keywords.append({
                "query": query[:240],
                "reason": str(item.get("reason", ""))[:200],
            })
            if len(keywords) >= max_keywords:
                break
    avoid_patterns = data.get("avoid_patterns", [])
    if not isinstance(avoid_patterns, list):
        avoid_patterns = []
    return {
        "recommended_keywords": keywords,
        "avoid_patterns": [str(p)[:160] for p in avoid_patterns[:20]],
        "model": model,
        "source": source,
    }


def _fallback_keyword_plan(query: str, concept_gaps: list[str], max_keywords: int,
                           model: str, reason: str = "fallback",
                           preferred_source_types: list[str] | None = None) -> dict:
    preferred_source_types = preferred_source_types or [
        "official documentation",
        "technical report benchmark",
        "implementation repository",
    ]
    seed_queries = [
        f"site:arxiv.org {query}",
        f"site:github.com {query}",
    ]
    for source_type in preferred_source_types[:4]:
        seed_queries.insert(0, f'"{query}" {source_type}')
    for gap in concept_gaps[:3]:
        seed_queries.append(str(gap))
    return _normalize_keyword_plan(
        {
            "recommended_keywords": [
                {"query": q, "reason": "deterministic fallback to diversify DDG discovery"}
                for q in seed_queries
            ],
            "avoid_patterns": ["javascript-only blog pages", "broad marketing posts"],
        },
        max_keywords=max_keywords,
        model=model,
        source=reason,
    )


def _call_keyword_recommender(manifest: dict, research_config: dict) -> dict:
    model = _keyword_recommender_model(research_config)
    max_keywords = int(manifest.get("max_keywords", 5) or 5)
    try:
        import anthropic  # noqa: PLC0415
    except ImportError:
        return _fallback_keyword_plan(
            manifest.get("base_query", ""),
            manifest.get("concept_gaps", []),
            max_keywords,
            model,
            reason="fallback_anthropic_missing",
            preferred_source_types=manifest.get("preferred_source_types"),
        )

    try:
        client = anthropic.Anthropic()
        max_tokens = min(
            int(research_config.get("max_keyword_recommender_tokens", 6000) or 6000),
            MAX_TOKENS_PER_SUBAGENT_OUTPUT,
        )
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=KEYWORD_RECOMMENDER_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": json.dumps(manifest)}],
        )
        if getattr(message, "stop_reason", None) == "max_tokens":
            logger.warning(
                "keyword recommender hit max_tokens (%d); thinking may have truncated JSON",
                max_tokens,
            )
        raw = ""
        for block in message.content:
            if hasattr(block, "text"):
                raw = block.text
                break
        json_str = extract_json_block(raw)
        if json_str is None:
            raise ValueError("keyword recommender returned no JSON")
        data = json.loads(json_str)
        plan = _normalize_keyword_plan(data, max_keywords, model, source="llm")
        if not plan["recommended_keywords"]:
            raise ValueError("keyword recommender returned no usable queries")
        return plan
    except Exception as e:
        logger.warning("keyword recommender failed; using fallback: %s", e)
        return _fallback_keyword_plan(
            manifest.get("base_query", ""),
            manifest.get("concept_gaps", []),
            max_keywords,
            model,
            reason="fallback_error",
            preferred_source_types=manifest.get("preferred_source_types"),
        )


def _canonical_label(page_path: Path) -> str:
    fm = frontmatter.parse_frontmatter(page_path)
    return str(fm.get("canonical_name") or page_path.stem)


def _hub_member_pages() -> set[str]:
    """Phase 2d: stems of pages belonging to any subtype declared as a
    top-level hub in [theme_profile].hub_hierarchy — see
    graph_topology.find_bridge_candidates' hub_pages docstring for why this
    is a subtype-membership set, not a per-page is_hub flag."""
    hub_hierarchy = _load_claude_md_block("theme_profile").get("hub_hierarchy") or []
    if not hub_hierarchy:
        return set()
    hub_subtypes = {h.get("subtype", "") for h in hub_hierarchy if h.get("subtype")}
    if not hub_subtypes:
        return set()
    members: set[str] = set()
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        fm, _ = frontmatter.parse_page(p)
        if fm.get("type", "entity") in hub_subtypes:
            members.add(p.stem)
    return members


def _bridge_candidates_for_manifest(max_candidates: int = 5) -> list[dict]:
    """Distant connected-component pairs (see graph_topology.find_bridge_candidates),
    with human-readable topic labels, for the keyword recommender manifest —
    the research-time half of the Graph Topology Philosophy: surface
    topologically distant clusters as candidate research angles, rather than
    only linking pages that already exist after the fact."""
    try:
        raw = graph_topology.find_bridge_candidates(
            _WIKI_PAGES_DIR, max_candidates=max_candidates, hub_pages=_hub_member_pages()
        )
    except Exception as e:
        logger.warning("bridge-candidate detection failed: %s", e)
        return []
    enriched = []
    for c in raw:
        page_a = _find_page_by_filename(c["page_a"])
        page_b = _find_page_by_filename(c["page_b"])
        enriched.append({
            "topic_a": _canonical_label(page_a) if page_a else c["page_a"],
            "topic_b": _canonical_label(page_b) if page_b else c["page_b"],
            "reason": c["reason"],
        })
    return enriched


def _build_keyword_plan(query: str, research_config: dict, depth: str,
                        discovery_history: dict, gap_manifest: dict | None = None,
                        audit: "AuditLog | None" = None) -> dict:
    concept_gaps = _get_concept_gaps()
    gap_manifest = gap_manifest or build_gap_manifest(_WIKI_PAGES_DIR, research_config)
    manifest = {
        "base_query": query,
        "repo_research_theme": _get_repo_research_theme(),
        "concept_gaps": concept_gaps[:20],
        "gap_manifest": gap_manifest,
        "preferred_source_types": research_config.get("preferred_source_types", []),
        "wiki_topic_summary": _get_wiki_topic_summary(),
        "previous_search_keywords": discovery_history.get("previous_queries", []),
        "repeated_results": discovery_history.get("repeated_results", []),
        "rejected_results": discovery_history.get("rejected_results", []),
        "zero_yield_queries": discovery_history.get("zero_yield_queries", []),
        "bridge_candidates": _bridge_candidates_for_manifest(),
        "depth": depth,
        "max_keywords": int(research_config.get("keyword_recommendation_limit", 5) or 5),
    }
    # Record the full input manifest (including bridge_candidates/concept_gaps)
    # for post-hoc audit/replay, same pattern as "synthesis"/"evaluation"
    # invocations below -- previously only the recommender's *output*
    # (keyword_plan) was ever saved via audit.set_keyword_plan(), so there was
    # no way to inspect what it actually saw. Optional: tests and other
    # internal callers of _build_keyword_plan don't always have an AuditLog.
    inv_idx = audit.record_invocation("keyword_recommender", manifest) if audit else None
    plan = _call_keyword_recommender(manifest, research_config)
    if audit and inv_idx is not None:
        audit.record_response(inv_idx, json.dumps(plan, ensure_ascii=False), schema_valid=True)
    return plan


# ---------------------------------------------------------------------------
# Wiki write operations
# ---------------------------------------------------------------------------

def _page_subdir(page_type: str) -> Path:
    if page_type in ("entity", "synthesis"):
        return _WIKI_PAGES_DIR / page_type
    return _WIKI_PAGES_DIR / page_type


def _write_page(draft: dict) -> Path:
    """
    Write an approved page draft to the wiki.
    Returns the path written.
    Orchestrator is the only code that calls this.
    """
    page_type = draft["page_type"]
    filename = draft["filename"]
    if not filename.endswith(".md"):
        filename += ".md"

    subdir = _page_subdir(page_type)
    subdir.mkdir(parents=True, exist_ok=True)
    page_path = subdir / filename

    fm = draft.get("frontmatter", {})
    content = draft.get("content", "")

    # Strip any frontmatter the subagent embedded in the content block
    # (subagent sometimes returns the full page; we own the frontmatter here).
    # Structural (delimiter-based) detection so a malformed embedded block
    # (invalid YAML) still gets stripped instead of surviving to disk.
    _stripped_body, _embedded_fm, _raw_block = frontmatter.strip_embedded_frontmatter_block(content)
    if _raw_block is not None:
        content = _stripped_body
        # Merge subagent-supplied fm fields that ours doesn't already have
        for k, v in _embedded_fm.items():
            fm.setdefault(k, v)

    # Ensure required frontmatter fields
    today = _now_date()
    fm.setdefault("type", page_type)
    fm.setdefault("created", today)
    fm["updated"] = today          # always reflect write date
    fm["cold_start"] = True        # new pages always cold until retrospective lint clears them
    fm.setdefault("inbound_links", 0)

    # Synthesis pages: populate connected_entities from body wiki-links when the
    # eval schema omits it (subagent only supplies canonical_name/aliases/subtype).
    if page_type == "synthesis" and not fm.get("connected_entities"):
        fm["connected_entities"] = list(dict.fromkeys(
            re.findall(r"\[\[([^\]]+)\]\]", content)
        ))

    # Graph Topology Philosophy: every link carries a reason, kept in frontmatter
    # alongside the edge so it's searchable/analyzable (see relationship_links.py).
    outbound_links = relationship_links.extract_outbound_links(content)
    if outbound_links:
        fm["outbound_links"] = outbound_links

    frontmatter.write_page(page_path, fm, content)
    return page_path


def _draft_filename(draft: dict) -> str:
    filename = draft["filename"]
    return filename if filename.endswith(".md") else f"{filename}.md"


def _draft_path(draft: dict) -> Path:
    page_type = draft["page_type"]
    subdir = _page_subdir(page_type)
    return subdir / _draft_filename(draft)


def _write_draft_once(
    draft: dict,
    source_url: str,
    session_state: ResearchSessionState,
    quota: QuotaManager,
    session_written_stems: set[str],
) -> Path | None:
    key = write_key(source_url, _draft_filename(draft))
    page_path = _draft_path(draft)
    if key in session_state.written_keys or page_path.exists():
        session_state.mark_written_key(key)
        session_written_stems.add(page_path.stem)
        return page_path
    if quota.pages_exceeded():
        return None
    page_path = _write_page(draft)
    _update_inbound_links(draft)
    _update_index(draft)
    quota.record_page_written()
    session_state.mark_written_key(key)
    session_state.record_created_page(page_path.stem)
    session_written_stems.add(page_path.stem)
    return page_path


def _find_page_by_filename(filename: str) -> Path | None:
    target = filename if filename.endswith(".md") else f"{filename}.md"
    for page in _WIKI_PAGES_DIR.rglob(target):
        return page
    stem = Path(filename).stem
    for page in _WIKI_PAGES_DIR.rglob("*.md"):
        if page.stem == stem:
            return page
    return None


def _patch_queue_path() -> Path:
    return _LOG_MD.parent / "patch_queue.md"


def _apply_update_once(
    update: dict,
    source_url: str,
    session_state: ResearchSessionState,
    quota: QuotaManager,
) -> Path | None:
    filename = str(update.get("filename", "")).strip()
    page_path = _find_page_by_filename(filename)
    if page_path is None:
        return None
    key = write_key(source_url, f"update:{page_path.name}:{update.get('section', '')}")
    if key in session_state.written_keys:
        return _patch_queue_path()
    if quota.pages_exceeded():
        return None
    description = str(update.get("update_description", "")).strip()
    if not description:
        return None
    section = str(update.get("section", "Research Updates")).strip() or "Research Updates"
    queue_path = _patch_queue_path()
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    if queue_path.exists():
        queue_text = queue_path.read_text(encoding="utf-8")
    else:
        queue_text = "# Wiki Patch Queue\n\n"
    entry = (
        f"## [{_now_date()}] pending | {page_path.name}\n"
        f"target_page: {page_path.name}\n"
        f"target_section: {section}\n"
        f"source: {source_url}\n"
        f"status: pending_review\n"
        f"proposed_update: {description}\n"
    )
    if entry in queue_text:
        session_state.mark_written_key(key)
        return queue_path
    queue_path.write_text(queue_text.rstrip() + "\n\n" + entry, encoding="utf-8")
    quota.record_page_written()
    session_state.mark_written_key(key)
    return queue_path


def _update_inbound_links(draft: dict) -> None:
    """Increment inbound_links on pages referenced from this draft's content."""
    content = draft.get("content", "")
    refs = re.findall(r"\[\[([^\]]+)\]\]", content)
    for ref in set(refs):
        for page in _WIKI_PAGES_DIR.rglob(f"{ref}.md"):
            _increment_frontmatter_field(page, "inbound_links")


def _increment_frontmatter_field(path: Path, field: str) -> None:
    frontmatter.increment_page_field(path, field)


def _update_index(draft: dict) -> None:
    """Append a row for the new/updated page to wiki/index.md."""
    if not _INDEX_MD.exists():
        return
    page_type = draft["page_type"]
    filename = draft["filename"]
    if not filename.endswith(".md"):
        filename += ".md"
    fm = draft.get("frontmatter", {})
    tags = ", ".join(fm.get("tags", []))
    sources = str(len(fm.get("sources", [])))
    inbound = str(fm.get("inbound_links", 0))

    text = _INDEX_MD.read_text(encoding="utf-8")

    if page_type == "entity":
        summary = (draft.get("content", "").split("\n")[0]).lstrip("#").strip()[:80]
        new_row = f"| [{filename}](entity/{filename}) | {summary} | {tags} | {sources} | {inbound} |"
        text = text.replace(
            "| [page_name](entity/page_name.md) | One-line summary | tag1, tag2 | 3 | 5 |",
            "",
        )
        # Append after the entity table header if row not present
        if new_row not in text:
            text = re.sub(
                r"(## Entity Pages\n\n\|.*?\|.*?\n\|.*?\|.*?\n)",
                rf"\1{new_row}\n",
                text,
                flags=re.DOTALL,
            )
    elif page_type == "synthesis":
        connected = ", ".join(fm.get("connected_entities", []))
        status = fm.get("synthesis_status", "draft")
        new_row = f"| [{filename}](synthesis/{filename}) | {connected} | {status} | {inbound} |"
        if new_row not in text:
            text = re.sub(
                r"(## Synthesis Pages\n\n\|.*?\|.*?\n\|.*?\|.*?\n)",
                rf"\1{new_row}\n",
                text,
                flags=re.DOTALL,
            )
    else:
        summary = (draft.get("content", "").split("\n")[0]).lstrip("#").strip()[:80]
        new_row = f"| [{filename}]({page_type}/{filename}) | {page_type} | {summary} | {tags} | {sources} | {inbound} |"
        if "## Optimization Pages" not in text:
            text += (
                "\n## Optimization Pages\n\n"
                "| Page | Type | Summary | Tags | Sources | Inbound |\n"
                "|------|------|---------|------|---------|---------|\n"
            )
        if new_row not in text:
            text = re.sub(
                r"(## Optimization Pages\n\n\|.*?\|.*?\n\|.*?\|.*?\n)",
                rf"\1{new_row}\n",
                text,
                flags=re.DOTALL,
            )

    # Update header stats
    page_count = len(list(_WIKI_PAGES_DIR.rglob("*.md")))
    text = re.sub(r"Last updated: \S+", f"Last updated: {_now_date()}", text)
    text = re.sub(r"Pages: \d+", f"Pages: {page_count}", text)
    _INDEX_MD.write_text(text, encoding="utf-8")


def _page_summary(body: str) -> str:
    """First non-empty line of a page body, stripped of a leading '#', truncated."""
    for line in body.split("\n"):
        stripped = line.strip()
        if stripped:
            return stripped.lstrip("#").strip()[:80]
    return ""


def rebuild_index_from_frontmatter() -> None:
    """
    Regenerate the Entity/Synthesis/Optimization tables and header stats in
    wiki/index.md directly from on-disk page frontmatter.

    _update_index() only appends a row at write time, embedding that page's
    inbound_links/sources count as of creation — it never revisits that row
    when a *later* page/lint pass changes the target's frontmatter (e.g. the
    linking-debt passes that increment a target's inbound_links). Over a long
    research run this silently drifts every row except the most recently
    touched one. This function is the full-rebuild source of truth; call it
    after any change that can affect inbound_links/sources counts elsewhere
    in the graph (end of a research session, lint apply).
    """
    if not _INDEX_MD.exists():
        return

    entity_rows: list[str] = []
    synthesis_rows: list[str] = []
    optimization_rows: list[str] = []
    distinct_sources: set[str] = set()

    # Concept Index inputs. Resolved: canonical_name/aliases -> the page that
    # defines them. Gaps: outbound_links targets that don't resolve to any
    # existing page stem, i.e. concepts other pages mention but that have no
    # dedicated page of their own yet -- the signal _get_concept_gaps() reads,
    # via the "**Name**: ... no dedicated page" pattern. This has never been
    # populated by the autonomous research loop (only ever specified in
    # CLAUDE.md's template text, going back to the harness's original Phase 6
    # implementation) -- _get_concept_gaps() has always returned [] as a
    # result, silently. Fed to Discovery/keyword-recommender manifests as
    # concept_gaps, so this was dead input on every prior session.
    resolved_concepts: dict[str, str] = {}   # display name -> "[stem](folder/stem.md)"
    page_stems: dict[str, tuple[str, str]] = {}  # stem -> (folder, filename)
    mentions: dict[str, tuple[str, str, str]] = {}  # target -> (folder, filename, first mentioning page link)
    # Hub Hierarchy inputs: pages grouped by their subtype (subagents write
    # the literal subtype into `type`, e.g. type: hardware_target, not
    # type: entity/subtype: hardware_target -- see the "type" vs "subtype"
    # note in Phase 1's audit). Grouped against [theme_profile].hub_hierarchy
    # at render time, not stored per-page -- see domain_analysis.py's
    # _risc_v_hub_hierarchy() docstring for why this is a derived view.
    pages_by_subtype: dict[str, list[str]] = {}

    for path in sorted(_WIKI_PAGES_DIR.rglob("*.md")):
        fm, body = frontmatter.parse_page(path)
        if not fm:
            continue
        page_type = fm.get("type", "entity")
        folder = path.parent.name
        filename = path.name
        pages_by_subtype.setdefault(page_type, []).append(f"[{path.stem}]({folder}/{filename})")
        tags = ", ".join(fm.get("tags", []) or [])
        sources = fm.get("sources", []) or []
        source_count = str(len(sources))
        for src in sources:
            distinct_sources.add(str(src))
        inbound = str(fm.get("inbound_links", 0))
        page_stems[path.stem] = (folder, filename)

        if page_type == "synthesis":
            connected = ", ".join(fm.get("connected_entities", []) or [])
            status = fm.get("synthesis_status", "draft")
            synthesis_rows.append(
                f"| [{filename}](synthesis/{filename}) | {connected} | {status} | {inbound} |"
            )
        elif folder == "entity":
            summary = _page_summary(body)
            entity_rows.append(
                f"| [{filename}](entity/{filename}) | {summary} | {tags} | {source_count} | {inbound} |"
            )
        else:
            summary = _page_summary(body)
            optimization_rows.append(
                f"| [{filename}]({folder}/{filename}) | {folder} | {summary} | {tags} | "
                f"{source_count} | {inbound} |"
            )

        canonical = fm.get("canonical_name")
        link = f"[{path.stem}]({folder}/{filename})"
        for name in ([canonical] if canonical else []) + list(fm.get("aliases", []) or []):
            name = str(name).strip()
            if name:
                resolved_concepts[name] = link

        for edge in (fm.get("outbound_links") or []):
            if not isinstance(edge, dict):
                continue
            target = str(edge.get("target", "")).strip()
            if target and target not in mentions:
                mentions[target] = (folder, filename, f"[{path.stem}]({folder}/{filename})")

    concept_index_lines: list[str] = []
    for name in sorted(resolved_concepts):
        concept_index_lines.append(f"- **{name}**: → {resolved_concepts[name]}")
    for target in sorted(mentions):
        if target in page_stems:
            continue  # resolved by another page's own canonical_name/aliases; not a gap
        _, _, mention_link = mentions[target]
        concept_index_lines.append(
            f"- **{target}**: mentioned in {mention_link} — *no dedicated page*"
        )

    text = _INDEX_MD.read_text(encoding="utf-8")

    def _replace_table(text: str, header: str, column_line: str, rows: list[str]) -> str:
        """Replace the table under `header` with freshly built rows.

        Line-based rather than a single greedy regex: a DOTALL regex spanning
        "all row lines" can't tell one table's rows from the next table's rows
        (both start with '|'), so it risks swallowing an adjacent table.
        """
        lines = text.split("\n")
        try:
            header_idx = lines.index(header)
        except ValueError:
            new_block = [header, "", column_line] + rows
            return text.rstrip("\n") + "\n\n" + "\n".join(new_block) + "\n"

        # Skip header, blank line, and the two column-definition lines.
        row_start = header_idx + 1
        while row_start < len(lines) and not lines[row_start].strip().startswith("|"):
            row_start += 1
        # First "|" line is the column-name row, second is the separator row.
        row_start += 2
        row_end = row_start
        while row_end < len(lines) and lines[row_end].strip().startswith("|"):
            row_end += 1

        new_block = [header, "", column_line] + rows
        new_lines = lines[:header_idx] + new_block + lines[row_end:]
        return "\n".join(new_lines)

    text = _replace_table(
        text, "## Entity Pages",
        "| Page | Summary | Tags | Sources | Inbound |\n|------|---------|------|---------|---------|",
        entity_rows,
    )
    text = _replace_table(
        text, "## Synthesis Pages",
        "| Page | Connected Entities | Status | Inbound |\n|------|--------------------|--------|---------|",
        synthesis_rows,
    )
    text = _replace_table(
        text, "## Optimization Pages",
        "| Page | Type | Summary | Tags | Sources | Inbound |\n|------|------|---------|------|---------|---------|",
        optimization_rows,
    )

    def _replace_section(text: str, header: str, lines: list[str]) -> str:
        """Replace a plain bullet-list section (no table header) with `lines`,
        up to the next '## ' heading or EOF.

        Found live: a since-removed "trim to exactly one blank line" loop
        decremented end_idx to walk back over trailing blank lines, but then
        used `all_lines[end_idx:]` as the preserved tail -- which still
        *starts* at the first of those same blank lines, not past them. Every
        rebuild call re-added its own single trailing blank on top of the
        untouched, never-actually-trimmed original run, so the blank-line
        count between two sections grew by ~1-2 lines every single research
        session (confirmed: 100+ accumulated blank lines in a long-running
        wiki's index.md). The forward scan below already stops exactly at the
        next '## ' heading (or EOF) with no leading blanks to trim -- new_block
        supplies the single blank line on its own, so no trim-back is needed.
        """
        all_lines = text.split("\n")
        try:
            header_idx = all_lines.index(header)
        except ValueError:
            new_block = [header, ""] + lines
            return text.rstrip("\n") + "\n\n" + "\n".join(new_block) + "\n"
        end_idx = header_idx + 1
        while end_idx < len(all_lines) and not all_lines[end_idx].startswith("## "):
            end_idx += 1
        new_block = [header, ""] + lines + [""]
        new_lines = all_lines[:header_idx] + new_block + all_lines[end_idx:]
        return "\n".join(new_lines)

    text = _replace_section(text, "## Concept Index", concept_index_lines)

    hub_hierarchy = _load_claude_md_block("theme_profile").get("hub_hierarchy") or []
    if hub_hierarchy:
        hub_lines: list[str] = []
        for hub in hub_hierarchy:
            label = hub.get("label", hub.get("hub_id", "?"))
            subtype = hub.get("subtype", "")
            children = pages_by_subtype.get(subtype, [])
            hub_lines.append(f"### {label}")
            hub_lines.append("")
            if hub.get("description"):
                hub_lines.append(f"*{hub['description']}*")
                hub_lines.append("")
            if children:
                hub_lines.extend(f"- {c}" for c in sorted(children))
            else:
                hub_lines.append("*(no pages under this hub yet)*")
            hub_lines.append("")
        if hub_lines and hub_lines[-1] == "":
            hub_lines.pop()
        text = _replace_section(text, "## Hub Hierarchy", hub_lines)

    page_count = len(list(_WIKI_PAGES_DIR.rglob("*.md")))
    text = re.sub(r"Last updated: \S+", f"Last updated: {_now_date()}", text)
    text = re.sub(r"Pages: \d+", f"Pages: {page_count}", text)
    text = re.sub(r"Sources: \d+", f"Sources: {len(distinct_sources)}", text)
    _INDEX_MD.write_text(text, encoding="utf-8")


def _run_graph_stats() -> None:
    """Run graph_stats.py and print output."""
    result = subprocess.run(
        [sys.executable, str(_TOOLS_DIR / "graph_stats.py"), str(_WIKI_PAGES_DIR)],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.strip())


def _run_qmd_update(qmd_runner: QmdRunner) -> tuple[bool, str | None]:
    """Re-index wiki pages so qmd search reflects newly written pages."""
    ok, error = qmd_runner.update()
    if error:
        logger.warning("qmd update failed: %s", error)
    return ok, error


### Frontmatter keys the orchestrator (not the subagent) is authoritative for:
### _write_page/_apply_scorecard_to_draft/_apply_provenance set or hard-overwrite
### these deterministically. An embedded duplicate block must never seed them —
### e.g. a model-hallucinated `created` date would otherwise survive because
### _write_page only does `setdefault("created", today)`.
_ORCHESTRATOR_MANAGED_FRONTMATTER_KEYS = {
    "type", "created", "updated", "cold_start", "inbound_links",
    "scorecard", "sources", "source_url", "fetched_at",
}


def _merge_embedded_frontmatter(draft: dict) -> None:
    """Subagent drafts occasionally echo a second frontmatter block inside their
    own content field, in addition to the separate structured frontmatter dict
    (observed with weaker/cheaper eval-subagent models). If left untouched, the
    embedded block corrupts first-paragraph/word-count extraction downstream
    (frontmatter.render_page strips it defensively). Merge it into
    draft["frontmatter"] first so content-derived fields (tags, hardware_targets,
    toolchains, constraints, etc.) that only exist in the embedded block are not
    silently lost; the structured frontmatter dict wins on key conflicts, and
    orchestrator-managed keys are never taken from the embedded block."""
    content = draft.get("content", "")
    stripped_body, embedded_fm, raw_block = frontmatter.strip_embedded_frontmatter_block(content.lstrip("\n"))
    if raw_block is None:
        return
    fm = draft.setdefault("frontmatter", {})
    for key, value in embedded_fm.items():
        if key not in _ORCHESTRATOR_MANAGED_FRONTMATTER_KEYS:
            fm.setdefault(key, value)
    draft["content"] = stripped_body


def _apply_scorecard_to_draft(draft: dict, eval_scorecard: dict) -> None:
    """
    Copy scorecard scores from the eval agent's top-level scorecard into
    draft["frontmatter"]["scorecard"], mapping by page type.

    Entity fields:  novelty_delta, claim_density, self_containedness, bridge_score, hub_potential
    Synthesis fields: bridge_score, contradiction_potential, cross_domain_connection (unmapped → None)
    """
    page_type = draft.get("page_type", "entity")
    fm = draft.setdefault("frontmatter", {})
    sc = eval_scorecard or {}

    if page_type != "synthesis":
        fm["scorecard"] = {
            "novelty_delta":       sc.get("novelty_delta"),
            "claim_density":       sc.get("claim_density"),
            "self_containedness":  sc.get("self_containedness"),
            "bridge_score":        sc.get("bridge_score"),
            "hub_potential":       sc.get("hub_potential"),
        }
    else:  # synthesis
        fm["scorecard"] = {
            "bridge_score":            sc.get("bridge_score"),
            "contradiction_potential": sc.get("contradiction_potential"),
            "cross_domain_connection": None,  # not produced by eval agent
        }


def _run_eval_pipeline(draft: dict) -> tuple[bool, dict]:
    """
    Write draft to a temp file and run eval_summary.py against it.
    Returns (passes, pipeline_result_dict).
    """
    page_type = draft.get("page_type", "entity")
    fm = draft.get("frontmatter", {})
    content = draft.get("content", "")
    page_md = frontmatter.render_page(fm, content)

    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8") as f:
        f.write(page_md)
        tmp_path = Path(f.name)

    try:
        result = subprocess.run(
            [sys.executable, str(_TOOLS_DIR / "eval_summary.py"), str(tmp_path),
             "--type", page_type],
            capture_output=True,
            text=True,
        )
        passes = result.returncode == 0
        return passes, {
            "layer1_pass": passes or "WORD_COUNT" not in result.stdout,
            "layer2_pass": True,
            "layer3_triggered": False,
            "final_decision": "approved" if passes else "rejected",
            "rejection_detail": result.stdout.strip() if not passes else None,
        }
    finally:
        tmp_path.unlink(missing_ok=True)


def _append_log(session_id: str, pages_written: list[str], audit_path: Path,
                 candidates_found: int, candidates_evaluated: int, query: str,
                 rejected_by_pipeline: int, theme_profile: dict | None = None,
                 coverage_gaps: list[str] | None = None) -> None:
    today = _now_date()
    query_trunc = query[:60]
    total = candidates_evaluated
    rate = f"{(rejected_by_pipeline / max(total, 1) * 100):.0f}%"

    entry = (
        f"\n## [{today}] research | {query_trunc}\n"
        f"session_id: {session_id}\n"
        f"candidates_evaluated: {candidates_evaluated}\n"
        f"pages_written: {len(pages_written)}\n"
        f"pipeline_rejection_rate: {rate}\n"
        f"audit_file: {audit_path}\n"
    )
    if theme_profile:
        entry += (
            f"theme_profile: {theme_profile.get('theme')} | "
            f"{theme_profile.get('organization_choice') or theme_profile.get('organization_name')}\n"
        )
    if coverage_gaps:
        entry += "coverage_gaps:\n" + "".join(f"  - {gap}\n" for gap in coverage_gaps[:10])
    with open(_LOG_MD, "a", encoding="utf-8") as f:
        f.write(entry)


def _build_page_templates(page_type_taxonomy: dict | None = None) -> dict:
    """Return generic page templates for eval manifests."""
    entity_template = """\
---
type: entity
tags: []
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Entity Name>

<First paragraph: self-contained definition.>

## Key Claims

<Structured list of specific, verifiable claims.>

## Relationships

<Explicit links to other pages.>

## Sources

<Citations to source files.>
"""
    synthesis_template = """\
---
type: synthesis
connected_entities: []
synthesis_status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# <Synthesis Title>

## RAG Summary

<150-250 word self-contained summary.>

---

## Full Synthesis

<Narrative content.>

## Open Questions

<Unresolved issues.>

## Connected Pages

<Links to entity pages.>
"""
    hardware_target_template = """\
---
type: hardware_target
tags: []
sources: []
hardware_targets: []
toolchains: []
constraints: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Hardware Target>

<First paragraph: ISA/profile, relevant extensions, memory hierarchy, accelerator interfaces, and compiler support.>

## Key Claims

<Specific source-grounded hardware/software capability claims.>

## Optimization-Relevant Details

- ISA/profile:
- Vector/matrix/accelerator support:
- Memory/cache/TLB/DMA:
- Compiler/toolchain support:

## Relationships

<Links to related workloads, recipes, toolchains, or entity pages.>

## Sources

<Citations to source URLs or raw files.>
"""
    workload_kernel_template = """\
---
type: workload_kernel
tags: []
sources: []
workloads: []
datatypes: []
constraints: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Workload Kernel>

<First paragraph: operation shape, datatype, layout, sparsity, model context, and baseline implementation.>

## Key Claims

<Specific source-grounded workload claims.>

## Kernel Shape

- Operation:
- Shapes:
- Datatypes:
- Layout:
- Sparsity:
- Baseline implementation:

## Relationships

<Links to related hardware targets, recipes, or entity pages.>

## Sources

<Citations to source URLs or raw files.>
"""
    optimization_recipe_template = """\
---
type: optimization_recipe
tags: []
sources: []
hardware_targets: []
workloads: []
datatypes: []
metrics: []
toolchains: []
constraints: []
evidence_strength: reported
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Optimization Recipe>

<First paragraph: transformation, prerequisites, expected effect, failure modes, and measurement status.>

## Key Claims

<Specific source-grounded optimization claims.>

## Transformation

- Prerequisites:
- Steps:
- Expected effect:
- Failure modes:
- Measurements:

## Relationships

<Links to related hardware targets, workload kernels, benchmarks, or entity pages.>

## Sources

<Citations to source URLs or raw files.>
"""
    benchmark_result_template = """\
---
type: benchmark_result
tags: []
sources: []
hardware_targets: []
workloads: []
datatypes: []
metrics: []
toolchains: []
hardware_versions: []
software_versions: []
measurement_method: ""
evidence_strength: reported
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Benchmark Result>

<First paragraph: hardware/software versions, workload shape, metrics, measurement method, and source context.>

## Key Claims

<Specific benchmark claims with metric values and context.>

## Measurement Context

- Hardware version:
- Software/toolchain version:
- Workload shape:
- Metric:
- Method:
- Evidence strength: measured | reported | derived | marketing

## Relationships

<Links to related hardware targets, workloads, recipes, or entity pages.>

## Sources

<Citations to source URLs or raw files.>
"""
    templates = {
        "entity": entity_template,
        "synthesis": synthesis_template,
        "source_note": entity_template.replace("type: entity", "type: source_note", 1),
        "hardware_target": hardware_target_template,
        "workload_kernel": workload_kernel_template,
        "optimization_recipe": optimization_recipe_template,
        "benchmark_result": benchmark_result_template,
    }
    if page_type_taxonomy is None:
        return templates
    allowed = set(page_type_taxonomy)
    return {key: value for key, value in templates.items() if key in allowed}


# ---------------------------------------------------------------------------
# DDG-based discovery (replaces LLM URL hallucination)
# ---------------------------------------------------------------------------

def _ddg_discover(
    query: str,
    max_candidates: int,
    already_processed: set[str],
    research_config: dict,
    depth: str,
    keyword_plan: dict | None = None,
    discovery_metadata: dict | None = None,
    repeat_urls: set[str] | None = None,
) -> list[dict]:
    """
    Search DuckDuckGo for real URLs + snippets.  Returns candidate dicts
    compatible with the rest of the pipeline:
      {"url": ..., "title": ..., "snippet": ..., "estimated_type": "entity"}
    """
    try:
        from ddgs import DDGS  # noqa: PLC0415
    except ImportError:
        logger.warning("ddgs not installed; falling back to empty candidate list. "
                       "Run: pip install ddgs")
        return []

    limit = research_config.get("discovery_search_queries_limit", 5)
    # depth=deep → use more search queries / results per query
    results_per_query = 10 if depth == "deep" else 6

    # Generate search query variants. Recommended queries go first because the
    # base query is exactly what tends to reproduce stale DDG result sets.
    concept_gaps = _get_concept_gaps()
    queries: list[str] = []
    seen_query_text: set[str] = set()

    def _append_query(q: str) -> None:
        cleaned = q.strip()
        if cleaned and cleaned.lower() not in seen_query_text and len(queries) < limit:
            queries.append(cleaned)
            seen_query_text.add(cleaned.lower())

    for item in (keyword_plan or {}).get("recommended_keywords", []):
        _append_query(str(item.get("query", "")))
    _append_query(query)

    # Add concept-gap queries as STANDALONE searches (not appended to base query).
    # Appending gaps to the base query keeps discovery within the same product space;
    # standalone queries widen to adjacent concepts.
    if concept_gaps:
        for gap in concept_gaps[:min(2, len(concept_gaps))]:
            _append_query(gap)

    # Add synthesis-oriented queries to pull in comparison/survey sources, which
    # tend to produce synthesis pages rather than more product entity pages.
    _append_query(f"{query} comparison survey architecture overview")
    _append_query(f"{query} taxonomy ecosystem landscape")

    # Add source-targeted variants for arXiv and GitHub when the query is technical
    # or when depth=deep explicitly requests broader coverage.
    _TECHNICAL_KEYWORDS = ("paper", "arxiv", "repo", "github", "implementation", "code", "algorithm")
    if depth == "deep" or any(kw in query.lower() for kw in _TECHNICAL_KEYWORDS):
        _append_query(f"site:arxiv.org {query}")
        _append_query(f"site:github.com {query}")

    # Pad with broad source-quality refinements without assuming a specific domain.
    refinements = research_config.get("preferred_source_types") or [
        "official documentation",
        "technical report benchmark",
    ]
    for ref in refinements:
        _append_query(f"{query} {ref}")

    # Domains and extensions that reliably yield unusable content for the eval agent
    _URL_BLOCKLIST = (
        "youtube.com", "youtu.be", "slideshare.net", "reddit.com",
        "twitter.com", "x.com", "linkedin.com", "facebook.com",
        "scribd.com", "dl.acm.org", "ieeexplore.ieee.org", "sciencedirect.com",
    )
    avoid_patterns = [
        str(p).lower()
        for p in (keyword_plan or {}).get("avoid_patterns", [])
        if str(p).strip()
    ]
    generic_query_terms = {
        "about", "after", "against", "analysis", "and", "api", "apis", "article",
        "benchmark", "blog", "case", "code", "comparison", "dataset", "datasets",
        "demo", "deploy", "deployment", "docs", "documentation", "example",
        "examples", "for", "from", "github", "guide", "html", "http", "https",
        "implementation", "implementations", "introduction", "library", "official",
        "open", "overview", "paper", "papers", "performance", "project", "report",
        "research", "review", "runtime", "sdk", "sdks", "site", "source", "stack",
        "study", "survey", "technical", "the", "tool", "tools", "tutorial", "using",
        "with",
    }

    def _is_blocked(url: str, title: str = "", snippet: str = "") -> bool:
        lower = url.lower()
        if re.search(r"\.pdf(?:$|[?#])", lower) or "arxiv.org/pdf/" in lower:
            return True
        haystack = f"{lower}\n{title.lower()}\n{snippet.lower()}"
        return any(d in lower for d in _URL_BLOCKLIST) or any(
            pattern in haystack for pattern in avoid_patterns
        )

    def _query_anchor_tokens(q: str) -> set[str]:
        tokens = {
            tok.lower()
            for tok in re.findall(r"[a-zA-Z][a-zA-Z0-9+-]{2,}", q)
        }
        return {
            tok for tok in tokens
            if tok not in generic_query_terms
            and not tok.startswith("site")
        }

    def _matches_query_anchor(q: str, url: str, title: str, snippet: str) -> bool:
        anchors = _query_anchor_tokens(q)
        if not anchors:
            return True
        haystack = f"{url}\n{title}\n{snippet}".lower()
        return any(anchor in haystack for anchor in anchors)

    suppress_repeat_urls = research_config.get("repeat_url_suppression", True)
    repeat_urls = repeat_urls or set()
    seen_urls: set[str] = set(already_processed)
    if suppress_repeat_urls:
        seen_urls |= repeat_urls
    suppressed_repeat_urls: list[str] = []
    produced_by_query: dict[str, int] = {}
    candidates: list[dict] = []

    with DDGS() as ddgs:
        for q in queries:
            if len(candidates) >= max_candidates:
                break
            try:
                for r in ddgs.text(q, max_results=results_per_query):
                    url = r.get("href", "")
                    title = r.get("title", "")
                    snippet = r.get("body", "")
                    if not url or _is_blocked(url, title, snippet):
                        continue
                    if not _matches_query_anchor(q, url, title, snippet):
                        continue
                    if url in seen_urls:
                        if suppress_repeat_urls and url in repeat_urls:
                            suppressed_repeat_urls.append(url)
                        continue
                    seen_urls.add(url)
                    candidates.append({
                        "url": url,
                        "title": title,
                        "snippet": snippet,
                        "estimated_type": "entity",
                    })
                    produced_by_query[q] = produced_by_query.get(q, 0) + 1
                    if len(candidates) >= max_candidates:
                        break
            except Exception as e:
                logger.warning("DDG search failed for %r: %s", q, e)

    if discovery_metadata is not None:
        discovery_metadata["queries_used"] = queries
        discovery_metadata["produced_by_query"] = produced_by_query
        discovery_metadata["suppressed_repeat_urls"] = sorted(set(suppressed_repeat_urls))
    return candidates


def _enrich_snippet(title: str, base_snippet: str) -> str:
    """
    Run a focused DDG search for `title` and concatenate snippets into a
    single resource_content block, giving the eval agent enough text to
    write a 80+ word first paragraph.
    """
    if not title:
        return base_snippet

    try:
        from ddgs import DDGS  # noqa: PLC0415
    except ImportError:
        return base_snippet

    snippets = [f"[Search snippets for: {title}]"]
    if base_snippet:
        snippets.append(base_snippet)

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(title, max_results=5):
                body = r.get("body", "").strip()
                if body and body not in "\n".join(snippets):
                    snippets.append(f"- {r.get('title','')}: {body}")
    except Exception as e:
        logger.warning("_enrich_snippet DDG failed for %r: %s", title, e)

    return "\n".join(snippets)


# ---------------------------------------------------------------------------
# Main research session
# ---------------------------------------------------------------------------

def _blocked_qmd_summary(session_state: ResearchSessionState, audit: AuditLog,
                         error: str | None, evaluated: int, written: list[str],
                         pipeline_rejections: int) -> dict:
    session_state.status = "blocked_qmd"
    session_state.save("blocked_qmd", {"error": error})
    audit.set_candidates_evaluated(evaluated)
    summary = {
        "session_id": session_state.session_id,
        "candidates_found": len(session_state.candidates),
        "candidates_evaluated": evaluated,
        "pages_written": len(written),
        "pipeline_rejection_rate": f"{(pipeline_rejections / max(evaluated, 1) * 100):.0f}%",
        "audit_log_path": str(audit.path),
        "status": "blocked_qmd",
        "error": error,
    }
    print(f"[{session_state.session_id}] Blocked by qmd: {error}")
    return summary


def _restore_quota_from_state(session_state: ResearchSessionState) -> QuotaManager:
    quota = QuotaManager(
        max_candidates=session_state.scope.get("max_candidates", 20),
        max_new_pages=session_state.scope.get("max_new_pages", 10),
    )
    quota._candidates_evaluated = sum(
        1 for c in session_state.candidates
        if c.get("state") in {"eval_rejected", "pipeline_rejected", "approved", "written"}
    )
    quota._pages_written = sum(len(c.get("written_files", [])) for c in session_state.candidates)
    return quota


def _candidate_url(entry: dict) -> str:
    return entry.get("candidate", {}).get("url", "")


_REGISTRY_CACHE: dict[str, dict] = {}


def _session_registry(session_state: ResearchSessionState) -> dict:
    """Build (once per session) and return the in-memory identity registry."""
    cached = _REGISTRY_CACHE.get(session_state.session_id)
    if cached is None:
        cached = identity.build_registry(_WIKI_PAGES_DIR)
        _REGISTRY_CACHE[session_state.session_id] = cached
    return cached


def _draft_canonical(draft: dict) -> tuple[str, list[str]]:
    fm = draft.get("frontmatter", {}) or {}
    canonical = str(fm.get("canonical_name") or draft.get("filename") or "").strip()
    aliases = fm.get("aliases")
    aliases = [str(a) for a in aliases] if isinstance(aliases, list) else []
    return canonical, aliases


def _apply_provenance(draft: dict, entry: dict) -> None:
    """Deterministically set sources/source_url/fetched_at on a draft from the
    fetched-content snapshot, so `sources` always references an immutable local
    file rather than a bare live URL (overrides whatever the subagent guessed)."""
    snapshot = entry.get("source_snapshot")
    if not snapshot:
        return
    fm = draft.setdefault("frontmatter", {})
    sources = fm.get("sources") or []
    if not isinstance(sources, list):
        sources = [sources]
    if snapshot not in sources:
        sources = [snapshot, *sources]
    fm["sources"] = sources
    fm.setdefault("source_url", entry.get("source_url"))
    fm.setdefault("fetched_at", entry.get("fetched_at"))


def _queue_identity_upsert(
    draft: dict,
    ref: "identity.PageRef",
    url: str,
    session_state: ResearchSessionState,
    quota: QuotaManager,
) -> Path:
    """Hard-block path for a duplicate: apply the trivial, safe merges directly
    (union aliases/sources, bump updated) and queue the substantive content
    merge to patch_queue.md for human approval (Part 3b applies it)."""
    existing_fm, _ = frontmatter.parse_page(ref.path)
    draft_fm = draft.get("frontmatter", {}) or {}
    draft_canonical, draft_aliases = _draft_canonical(draft)

    # Union aliases: record the colliding surface form(s) so future lookups hit.
    aliases = list(existing_fm.get("aliases") or [])
    for a in [draft_canonical, *draft_aliases]:
        if a and a != existing_fm.get("canonical_name") and a not in aliases:
            aliases.append(a)
    if aliases:
        frontmatter.set_page_field(ref.path, "aliases", aliases)

    # Union sources (snapshot paths / urls already on the draft).
    sources = list(existing_fm.get("sources") or [])
    for s in (draft_fm.get("sources") or []):
        if s and s not in sources:
            sources.append(s)
    if sources:
        frontmatter.set_page_field(ref.path, "sources", sources)
    frontmatter.set_page_field(ref.path, "updated", _now_date())

    # Queue the content merge for approval.
    queue_path = _patch_queue_path()
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    queue_text = queue_path.read_text(encoding="utf-8") if queue_path.exists() else "# Wiki Patch Queue\n\n"
    body = (draft.get("content", "") or "").strip()
    entry_text = (
        f"## [{_now_date()}] merge_pending | {ref.path.name}\n"
        f"target_page: {ref.path.name}\n"
        f"canonical_name: {ref.canonical_name}\n"
        f"colliding_name: {draft_canonical}\n"
        f"source: {url}\n"
        f"status: pending_review\n"
        f"<!-- merge_draft_body\n{body}\nmerge_draft_body -->\n"
    )
    key = write_key(url, f"merge:{ref.path.name}")
    if entry_text not in queue_text and key not in session_state.written_keys:
        queue_path.write_text(queue_text.rstrip() + "\n\n" + entry_text, encoding="utf-8")
        session_state.mark_written_key(key)
    return queue_path


# ---------------------------------------------------------------------------
# Approval-gated content merge (`patch apply`)
# ---------------------------------------------------------------------------

_MERGE_BODY_RE = re.compile(r"<!--\s*merge_draft_body\n(.*?)\nmerge_draft_body\s*-->", re.DOTALL)


def _patch_block_field(block: str, name: str) -> str | None:
    m = re.search(rf"^{re.escape(name)}:\s*(.+)$", block, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def _parse_merge_block(block: str) -> dict:
    body_m = _MERGE_BODY_RE.search(block)
    return {
        "target_page": _patch_block_field(block, "target_page"),
        "canonical_name": _patch_block_field(block, "canonical_name"),
        "source": _patch_block_field(block, "source"),
        "status": _patch_block_field(block, "status"),
        "new_body": body_m.group(1) if body_m else "",
    }


def _set_patch_status(block: str, new_status: str) -> str:
    return re.sub(r"^status:\s*.+$", f"status: {new_status}",
                  block, count=1, flags=re.MULTILINE)


def _apply_one_merge(block: str, call_subagent, research_config: dict) -> tuple[bool, str]:
    entry = _parse_merge_block(block)
    target = entry.get("target_page")
    page = _find_page_by_filename(target) if target else None
    if page is None:
        return False, _set_patch_status(block, "apply_failed (page not found)")
    fm, body = frontmatter.parse_page(page)
    manifest = {
        "existing_content": body.strip(),
        "new_draft": (entry.get("new_body") or "").strip(),
        "canonical_name": entry.get("canonical_name") or fm.get("canonical_name"),
        "source": entry.get("source"),
    }
    try:
        raw = call_subagent("content_merge", manifest, research_config)
    except Exception as exc:  # noqa: BLE001 — never crash the queue
        logger.warning("content-merge subagent failed: %s", exc)
        return False, _set_patch_status(block, "apply_failed (subagent error)")
    result = validate_and_parse(raw, "MergeResult")
    if result is None:
        return False, _set_patch_status(block, "apply_failed (invalid merge output)")
    merged = result["merged_content"]
    # Deterministic pipeline gate — same gate as any other write.
    page_type = fm.get("type", "entity")
    passes, _ = _run_eval_pipeline({"page_type": page_type, "frontmatter": fm, "content": merged})
    if not passes:
        return False, _set_patch_status(block, "apply_failed (pipeline rejected)")
    # Rewrite the single target page atomically; bump updated; bump inbound only
    # for links that are newly introduced by the merge (avoid double counting).
    old_links = set(re.findall(r"\[\[([^\]]+)\]\]", body))
    new_links = set(re.findall(r"\[\[([^\]]+)\]\]", merged))
    fm["updated"] = _now_date()
    frontmatter.write_page(page, fm, merged)
    for ref in new_links - old_links:
        for linked in _WIKI_PAGES_DIR.rglob(f"{ref}.md"):
            _increment_frontmatter_field(linked, "inbound_links")
    return True, _set_patch_status(block, "applied")


def apply_patch_queue(call_subagent=_call_subagent) -> dict:
    """Apply human-approved merge_pending patches.

    A patch is applied only when its ``status`` is ``approved`` (the human edits
    ``pending_review`` -> ``approved`` in patch_queue.md). Each approved patch runs
    the content-merge subagent, is gated by the deterministic pipeline, and rewrites
    the single target page. ``call_subagent`` is injectable for testing.
    """
    path = _patch_queue_path()
    if not path.exists():
        return {"applied": 0, "skipped": 0, "failed": 0}
    research_config = _load_research_config()
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?=^## \[)", text, flags=re.MULTILINE)
    applied = skipped = failed = 0
    out_blocks: list[str] = []
    for block in blocks:
        header = block.split("\n", 1)[0]
        if "merge_pending" not in header:
            out_blocks.append(block)
            continue
        status = _patch_block_field(block, "status")
        if status != "approved":
            skipped += 1
            out_blocks.append(block)
            continue
        ok, new_block = _apply_one_merge(block, call_subagent, research_config)
        applied += int(ok)
        failed += int(not ok)
        out_blocks.append(new_block)
    path.write_text("".join(out_blocks), encoding="utf-8")
    if applied:
        rebuild_index_from_frontmatter()
    summary = {"applied": applied, "skipped": skipped, "failed": failed}
    print(f"patch apply: {summary}")
    return summary


def _probable_duplicate_by_similarity(
    canonical: str,
    draft: dict,
    qmd_matches: list[dict],
    research_config: dict,
) -> "identity.PageRef | None":
    """Secondary duplicate-detection pass for a ``create`` that
    ``identity.resolve()`` let through because canonical_name strings didn't
    match exactly.

    Exact-key matching missed a real duplicate in production: two
    benchmark_result pages generated from the same paper/hardware/result under
    different generated canonical_name strings (see the MERGE candidate in
    wiki/retrospective_lint_report.md — arXiv:2605.10860, same BananaPi-F3
    GCC15/Clang21 comparison, under "GCC 15 vs Clang 21 Autovectorization on
    BananaPi-F3 (RVV)" vs "Compiler Benchmark Comparison on BananaPi-F3 (RVV
    1.0)"). Deliberately reuses the qmd BM25 matches already computed and
    persisted during this candidate's pre-eval similarity check (entry
    ``qmd_matches``) rather than issuing a fresh qmd search here: the write
    phase must stay qmd-free so an interrupted-and-resumed session writes the
    exact same page deterministically (see
    test_approved_resume_writes_once_and_written_resume_skips). Only flags a
    match when BOTH the BM25 score clears ``near_duplicate_score`` AND the two
    pages share a source snapshot — ordinary same-family cross-references
    (shared vendor/hardware) don't share raw/ source files, so requiring both
    keeps this far less prone to false positives than Layer 3's saturation
    flag. This is advisory, not a hard block: it routes to the same
    human-reviewed patch_queue.md merge path as an exact identity collision,
    it doesn't silently drop the draft.
    """
    fm = draft.get("frontmatter", {}) or {}
    near_dup = float(research_config.get("near_duplicate_score", 0.90))
    draft_sources = {str(s) for s in (fm.get("sources") or [])}
    if not draft_sources:
        return None
    for match in qmd_matches:
        score = match.get("score")
        if score is None or score < near_dup:
            continue
        label = match.get("title") or match.get("file") or ""
        if hard_title_duplicate_score(canonical, label) >= 0.8:
            continue  # already caught by the title-based pre-eval/identity checks
        page = _find_page_by_filename(match.get("file") or "")
        if page is None:
            continue
        existing_fm, _ = frontmatter.parse_page(page)
        existing_sources = {str(s) for s in (existing_fm.get("sources") or [])}
        if draft_sources & existing_sources:
            ref_canonical = str(existing_fm.get("canonical_name") or page.stem)
            return identity.PageRef(canonical_name=ref_canonical, filename=page.name, path=page)
    return None


def _write_approved_entry(
    entry: dict,
    session_state: ResearchSessionState,
    audit: AuditLog,
    quota: QuotaManager,
    qmd_runner: QmdRunner,
    session_written_stems: set[str],
) -> tuple[str, str | None]:
    url = _candidate_url(entry)
    written_files = list(entry.get("written_files", []))
    registry = _session_registry(session_state)
    research_config = _load_research_config()
    max_debt = _max_linking_debt(research_config)
    handled_any = False
    for draft in entry.get("drafts", []):
        _apply_provenance(draft, entry)
        canonical, aliases = _draft_canonical(draft)
        # Authoritative, deterministic identity check (overrides the subagent's
        # advisory identity_action). A collision hard-blocks page creation.
        action, ref = identity.resolve(canonical, registry, aliases)
        if action == "create":
            probable = _probable_duplicate_by_similarity(
                canonical, draft, entry.get("qmd_matches") or [], research_config
            )
            if probable is not None:
                action, ref = "upsert", probable
                print(f"[{session_state.session_id}] Probable duplicate detected via BM25 + "
                      f"shared sources (canonical_name strings didn't match): "
                      f"{canonical!r} → upsert {probable.filename}")
        if action == "upsert" and ref is not None:
            _queue_identity_upsert(draft, ref, url, session_state, quota)
            handled_any = True
            print(f"[{session_state.session_id}] Identity collision (create blocked): "
                  f"{canonical!r} → upsert {ref.filename}")
            continue
        # Linking-debt backpressure: stop creating once too many session pages
        # are still orphaned; remaining work waits for linking/upserts.
        if max_debt > 0 and _current_linking_debt(session_state) >= max_debt:
            print(f"[{session_state.session_id}] Linking-debt cap ({max_debt}) reached; "
                  f"deferring new page {canonical!r}")
            session_state.transition(entry, "deferred_linking_debt", written_files=written_files)
            return "ok", None
        page_path = _write_draft_once(draft, url, session_state, quota, session_written_stems)
        if page_path is None:
            break
        identity.register(registry, canonical, page_path.name, page_path, aliases)
        handled_any = True
        if page_path.name not in written_files:
            written_files.append(page_path.name)
        ev_idx = entry.get("audit_invocation_idx")
        if ev_idx is not None:
            audit.record_page_written(ev_idx, page_path.name)
        session_state.transition(entry, "written", written_files=written_files)
        print(f"[{session_state.session_id}] Written: {page_path}")
        ok, error = _run_qmd_update(qmd_runner)
        if not ok:
            return "blocked_qmd", error
    for update in entry.get("updates", []):
        page_path = _apply_update_once(update, url, session_state, quota)
        if page_path is None:
            continue
        if page_path.name not in written_files:
            written_files.append(page_path.name)
        ev_idx = entry.get("audit_invocation_idx")
        if ev_idx is not None:
            audit.record_page_written(ev_idx, page_path.name)
        session_state.transition(entry, "written", written_files=written_files)
        print(f"[{session_state.session_id}] Updated: {page_path}")
        ok, error = _run_qmd_update(qmd_runner)
        if not ok:
            return "blocked_qmd", error
    # Collision-only entries (every draft hard-blocked into an upsert) produced
    # no created page; mark them terminal so they don't linger as pending.
    from research_state import TERMINAL_STATES
    if handled_any and entry.get("state") not in TERMINAL_STATES:
        session_state.transition(entry, "upserted", written_files=written_files)
    return "ok", None


def _run_research_state(session_state: ResearchSessionState) -> dict:
    session_id = session_state.session_id
    query = session_state.query
    scope = session_state.scope
    if session_state.status == "complete" and not session_state.pending_candidates():
        written_filenames = [
            name for c in session_state.candidates for name in c.get("written_files", [])
        ]
        return {
            "session_id": session_id,
            "candidates_found": len(session_state.candidates),
            "candidates_evaluated": sum(
                1 for c in session_state.candidates
                if c.get("state") in {"eval_rejected", "pipeline_rejected", "approved", "written"}
            ),
            "pages_written": len(written_filenames),
            "pipeline_rejection_rate": "0%",
            "audit_log_path": str(AuditLog(session_id, query, scope).path),
            "status": "complete",
        }
    research_config = _load_research_config()
    qmd_runner = QmdRunner(research_config.get("qmd_command"), cwd=_PROJECT_ROOT)
    audit = AuditLog(session_id, query, scope)
    _attach_theme_profile(audit, research_config)
    quota = _restore_quota_from_state(session_state)
    pipeline_rejections = sum(
        1 for c in session_state.candidates
        if c.get("state") in {"skipped_similarity", "pipeline_rejected"}
    )
    written_filenames = [
        name for c in session_state.candidates for name in c.get("written_files", [])
    ]
    session_written_stems = {Path(name).stem for name in written_filenames}
    effective_depth = session_state.effective_depth or scope.get("depth", "shallow")
    halfway = max(1, (scope.get("max_candidates", 20) + 1) // 2)
    gap_manifest = build_gap_manifest(_WIKI_PAGES_DIR, research_config)
    # Adaptive depth escalation alone doesn't stop a demonstrably unproductive
    # query from burning its whole candidate budget — e.g. session e545ec7c
    # ("RISC-V verification formal methods...") escalated at candidate 5 and
    # still went on to evaluate all 10 with 0 pages written. Once escalated,
    # if the deep-depth candidates keep failing too, stop early rather than
    # spending the remaining budget on a query whose angle is off-theme.
    escalated_at: int | None = None
    early_exit_after = int(research_config.get("early_exit_after_escalation_failures", 5) or 5)

    ok, error = _run_qmd_update(qmd_runner)
    if not ok:
        return _blocked_qmd_summary(
            session_state, audit, error, quota._candidates_evaluated,
            written_filenames, pipeline_rejections,
        )

    # Per-session injection cap: how many times each page has been shown to
    # the drafting subagent as wiki_context so far this session. Found live
    # that unbounded injection of the same page (previously biased toward
    # whichever page already had the most inbound_links) creates a
    # preferential-attachment loop — see context_selector.py's docstring.
    context_injection_counts: dict[str, int] = {}

    for entry in session_state.candidates:
        if quota.any_exceeded():
            print(f"[{session_id}] Quota exceeded, stopping early")
            break
        if (escalated_at is not None and quota._pages_written == 0
                and (quota._candidates_evaluated - escalated_at) >= early_exit_after):
            print(
                f"[{session_id}] Early exit: {quota._candidates_evaluated - escalated_at} "
                f"candidates evaluated since depth escalation with 0 pages written; "
                f"query angle likely unproductive, stopping rather than spending the "
                f"remaining candidate budget."
            )
            session_state.save("early_exit_after_escalation", {
                "escalated_at": escalated_at,
                "candidates_evaluated": quota._candidates_evaluated,
            })
            break
        if entry.get("state") in {"skipped_similarity", "fetch_failed", "eval_rejected", "pipeline_rejected", "written"}:
            continue

        candidate = entry["candidate"]
        url = candidate["url"]
        title = candidate.get("title", "")

        if entry.get("state") == "approved":
            status, error = _write_approved_entry(
                entry, session_state, audit, quota, qmd_runner, session_written_stems
            )
            if status == "blocked_qmd":
                return _blocked_qmd_summary(
                    session_state, audit, error, quota._candidates_evaluated,
                    written_filenames, pipeline_rejections,
                )
            written_filenames = list(set(written_filenames) | set(entry.get("written_files", [])))
            continue

        search_result = qmd_runner.search(candidate_similarity_query(candidate), top=10, collection="_pages")
        if not search_result.ok:
            session_state.transition(entry, "discovered", qmd_matches=[], error=search_result.error)
            return _blocked_qmd_summary(
                session_state, audit, search_result.error, quota._candidates_evaluated,
                written_filenames, pipeline_rejections,
            )

        similarity = assess_candidate_similarity(candidate, search_result.matches, research_config)
        qmd_matches = similarity["matches"]
        entry["qmd_matches"] = qmd_matches
        session_state.save("qmd_similarity", {"id": entry.get("id"), "matches": qmd_matches})

        existing_match = _title_matches_existing(
            title,
            session_written_stems,
            overlap_threshold=research_config.get("title_overlap_threshold", 0.8),
        )
        if similarity["skip"] or existing_match:
            reason = similarity["reason"] or f"title_overlap: matches '{existing_match}'"
            print(f"[{session_id}] Skipping duplicate/saturated topic: {title!r} ({reason})")
            audit.log_skip_pre_eval(url, reason, qmd_matches=qmd_matches)
            session_state.transition(
                entry,
                "skipped_similarity",
                skip_reason=reason,
                qmd_matches=qmd_matches,
            )
            pipeline_rejections += 1
            continue

        print(f"[{session_id}] Evaluating: {url}")
        snippet = candidate.get("snippet", "")
        content = _fetch_smart(
            url, retries=research_config.get("max_retries_on_fetch_failure", 2)
        )
        content = _content_or_enriched_snippet(content, candidate.get("title", ""), snippet, url)
        if not content:
            logger.warning("fetch failed and no enriched snippet for %s — skipping", url)
            session_state.transition(entry, "fetch_failed", error="fetch failed and no snippet")
            continue

        # Provenance: snapshot fetched content immutably so citations are
        # reproducible and `sources` references a local file, not a live URL.
        entry["source_snapshot"] = _snapshot_source(url, content)
        entry["source_url"] = url
        entry["fetched_at"] = datetime.now(timezone.utc).isoformat()

        if effective_depth == "deep" and content:
            supplement = _enrich_snippet(candidate.get("title", ""), candidate.get("snippet", ""))
            if supplement:
                content = content + "\n\n[DDG supplemental context]\n" + supplement

        content_limit = 10000 if effective_depth == "deep" else 6000
        evidence = extract_evidence(content[:content_limit], candidate, research_config)
        structured_terms = {
            "hardware_targets": evidence.get("hardware_names", []),
            "workloads": evidence.get("workload_names", []),
            "metrics": evidence.get("metrics", []),
            "toolchains": evidence.get("toolchain_names", []),
        }
        structured_query = build_structured_query(candidate, evidence)
        injected_pages = select_context_pages(
            content[:content_limit],
            qmd_runner=qmd_runner,
            structured_terms=structured_terms,
            injection_counts=context_injection_counts,
            injection_cap=int(research_config.get("context_injection_cap", 3) or 3),
        )
        for injected in injected_pages:
            stem = Path(injected["filename"]).stem
            context_injection_counts[stem] = context_injection_counts.get(stem, 0) + 1
        is_cold_start = not _wiki_is_mature()
        eval_config = _load_claude_md_block("eval_thresholds")
        eval_manifest = {
            "candidate": {"url": url, "title": candidate.get("title", "")},
            "resource_content": content[:content_limit],
            "evidence_extraction": evidence,
            "source_grounded_snippets": {
                "benchmark_result": source_grounded_snippets(content[:content_limit], "benchmark_result"),
                "optimization_recipe": source_grounded_snippets(content[:content_limit], "optimization_recipe"),
            },
            "qmd_similarity": {
                "matches": qmd_matches,
                "gate_decision": "allow",
                "merge_hint": similarity.get("merge_hint"),
                "structured_query": structured_query,
            },
            "wiki_context": {
                "relevant_pages": injected_pages,
                "concept_gaps": _get_concept_gaps(),
                "gap_manifest": gap_manifest,
                "graph_maturity": not is_cold_start,
                "depth": effective_depth,
            },
            "domain_config": {
                "theme_profile": research_config.get("theme_profile", {}),
                "preferred_source_types": research_config.get("preferred_source_types", []),
                "required_measurement_fields": research_config.get("required_measurement_fields", []),
                "page_type_taxonomy": research_config.get("page_type_taxonomy", {}),
                "coverage_priorities": research_config.get("coverage_priorities", []),
                "lint_priorities": research_config.get("lint_priorities", []),
            },
            "scorecard_config": {
                "variant": "cold_start" if is_cold_start else candidate.get("estimated_type", "entity"),
                "weights": eval_config,
                "acceptance_threshold": 0.4,
                "hard_rejection_threshold": 0.2,
            },
            "page_templates": _build_page_templates(research_config.get("page_type_taxonomy", {})),
        }

        ev_idx = audit.record_invocation("evaluation", eval_manifest)
        session_state.transition(entry, "evaluating", audit_invocation_idx=ev_idx, qmd_matches=qmd_matches)
        try:
            time.sleep(MIN_SECONDS_BETWEEN_CALLS)
            quota.record_api_call()
            raw_eval = _call_subagent("evaluation", eval_manifest, research_config)
        except Exception as e:
            logger.error("Evaluation API call failed for %s: %s", url, e)
            audit.record_response(ev_idx, str(e), schema_valid=False)
            session_state.transition(entry, "eval_rejected", error=str(e))
            continue

        eval_result = validate_and_parse(raw_eval, "EvalResult")
        audit.record_response(ev_idx, raw_eval, schema_valid=(eval_result is not None))
        quota.record_candidate_evaluated()
        if eval_result is None:
            audit.record_skip(ev_idx, "malformed_eval_output")
            session_state.transition(entry, "eval_rejected", skip_reason="malformed_eval_output")
            continue

        if (quota._candidates_evaluated == halfway
                and quota._pages_written == 0
                and effective_depth == "shallow"):
            effective_depth = "deep"
            session_state.effective_depth = effective_depth
            escalated_at = quota._candidates_evaluated
            session_state.save("depth_escalated", {"at_candidate": halfway})
            print(f"[{session_id}] Adaptive escalation: 0 pages after {halfway} candidates -> depth=deep")
            audit.log_escalation(halfway)

        if eval_result.get("decision") == "reject":
            reason = f"subagent_reject: {eval_result.get('rejection_reason', '')}"
            audit.record_skip(ev_idx, reason)
            session_state.transition(entry, "eval_rejected", skip_reason=reason, eval_result=eval_result)
            continue

        eval_sc = eval_result.get("scorecard", {})
        weighted_total = eval_sc.get("weighted_total", 0.0) or 0.0
        acceptance_threshold = eval_manifest["scorecard_config"].get("acceptance_threshold", 0.4)
        hard_rejection_threshold = eval_manifest["scorecard_config"].get("hard_rejection_threshold", 0.2)
        any_hard_fail = any(
            (float(v) or 0.0) < hard_rejection_threshold
            for k, v in eval_sc.items()
            if k not in ("weighted_total", "contradiction_potential") and v is not None
        )
        if weighted_total < acceptance_threshold:
            reason = (
                f"score_gate_reject: weighted_total={weighted_total:.2f} "
                f"< acceptance_threshold={acceptance_threshold}"
            )
            audit.record_skip(ev_idx, reason)
            session_state.transition(entry, "pipeline_rejected", skip_reason=reason, eval_result=eval_result)
            pipeline_rejections += 1
            continue
        if any_hard_fail:
            reason = (
                f"score_gate_reject: a scorecard dimension is below "
                f"hard_rejection_threshold={hard_rejection_threshold}"
            )
            audit.record_skip(ev_idx, reason)
            session_state.transition(entry, "pipeline_rejected", skip_reason=reason, eval_result=eval_result)
            pipeline_rejections += 1
            continue

        approved_drafts = []
        for draft in (eval_result.get("page_drafts") or []):
            _merge_embedded_frontmatter(draft)
            _apply_scorecard_to_draft(draft, eval_sc)
            # Inject source URL into frontmatter.sources before pipeline checks
            # EMPTY_SOURCES (provenance must be set before the gate, not after).
            _url = _candidate_url(entry)
            if _url:
                _fm = draft.setdefault("frontmatter", {})
                _srcs = _fm.get("sources") or []
                if not isinstance(_srcs, list):
                    _srcs = [_srcs]
                if _url not in _srcs:
                    _fm["sources"] = [_url, *_srcs]
            passes, pipeline_result = _run_eval_pipeline(draft)
            audit.record_pipeline_result(
                ev_idx,
                filename=draft.get("filename", "unknown"),
                layer1_pass=pipeline_result.get("layer1_pass", False),
                layer2_pass=pipeline_result.get("layer2_pass", True),
                layer3_triggered=pipeline_result.get("layer3_triggered", False),
                final_decision=pipeline_result.get("final_decision", "rejected"),
                rejection_detail=pipeline_result.get("rejection_detail"),
            )
            if passes:
                approved_drafts.append(draft)
            else:
                pipeline_rejections += 1

        approved_updates = [
            update for update in (eval_result.get("pages_to_update") or [])
            if isinstance(update, dict) and update.get("filename") and update.get("update_description")
        ]

        if not approved_drafts and not approved_updates:
            session_state.transition(entry, "pipeline_rejected", eval_result=eval_result)
            continue

        session_state.transition(
            entry,
            "approved",
            drafts=approved_drafts,
            updates=approved_updates,
            eval_result=eval_result,
        )
        status, error = _write_approved_entry(
            entry, session_state, audit, quota, qmd_runner, session_written_stems
        )
        written_filenames = list(set(written_filenames) | set(entry.get("written_files", [])))
        if status == "blocked_qmd":
            return _blocked_qmd_summary(
                session_state, audit, error, quota._candidates_evaluated,
                written_filenames, pipeline_rejections,
            )

    audit.set_candidates_evaluated(quota._candidates_evaluated)

    synthesis_gaps = _check_synthesis_gaps()
    if synthesis_gaps:
        print(f"[{session_id}] Synthesis gaps detected ({len(synthesis_gaps)}):")
        for gap in synthesis_gaps[:5]:
            print(f"  {gap}")
        # Only after the wiki has graduated cold-start bootstrapping (entity
        # pages take priority there per the ingest protocol) and only if this
        # session still has page budget left, after entity candidates for
        # this query are exhausted — one synthesis draft per session, so it
        # doesn't compete with page-count-focused sessions for budget.
        if _wiki_is_mature():
            synthesis_filename = _generate_synthesis_candidate(
                session_state, quota, audit, research_config, session_written_stems
            )
            if synthesis_filename:
                written_filenames = list(set(written_filenames) | {synthesis_filename})

    _run_graph_stats()
    rebuild_index_from_frontmatter()

    session_state.status = "complete"
    session_state.save("session_complete")
    _append_log(
        session_id=session_id,
        pages_written=written_filenames,
        audit_path=audit.path,
        candidates_found=len(session_state.candidates),
        candidates_evaluated=quota._candidates_evaluated,
        query=query,
        rejected_by_pipeline=pipeline_rejections,
        theme_profile=research_config.get("theme_profile"),
        coverage_gaps=(gap_manifest.get("gap_types", []) if isinstance(gap_manifest, dict) else []),
    )
    # Refresh connectivity metrics and flip graph_maturity if the connectivity
    # predicate is now satisfied (the transition writer the design implied).
    _maybe_transition_maturity(session_id)

    summary = {
        "session_id": session_id,
        "candidates_found": len(session_state.candidates),
        "candidates_evaluated": quota._candidates_evaluated,
        "pages_written": len(written_filenames),
        "pipeline_rejection_rate": f"{(pipeline_rejections / max(quota._candidates_evaluated, 1) * 100):.0f}%",
        "audit_log_path": str(audit.path),
        "status": "complete",
    }
    print(f"[{session_id}] Session complete: {summary}")
    return summary


def run_research_session(query: str, max_candidates: int, max_new_pages: int,
                          depth: str) -> dict:
    session_id = _generate_session_id()
    scope = {"max_candidates": max_candidates, "max_new_pages": max_new_pages, "depth": depth}
    research_config = _load_research_config()
    session_state = ResearchSessionState.create(
        session_id=session_id,
        query=query,
        scope=scope,
        state_dir=_research_state_dir(research_config),
    )
    print(f"[{session_id}] Starting research session: {query!r}")
    qmd_runner = QmdRunner(research_config.get("qmd_command"), cwd=_PROJECT_ROOT)
    ok, error = _run_qmd_update(qmd_runner)
    if not ok:
        audit = AuditLog(session_id, query, scope)
        _attach_theme_profile(audit, research_config)
        return _blocked_qmd_summary(session_state, audit, error, 0, [], 0)

    audit = AuditLog(session_id, query, scope)
    _attach_theme_profile(audit, research_config)
    discovery_history = _load_recent_discovery_history(research_config)
    gap_manifest = build_gap_manifest(_WIKI_PAGES_DIR, research_config)
    keyword_plan = _build_keyword_plan(
        query, research_config, depth, discovery_history, gap_manifest=gap_manifest, audit=audit
    )
    session_state.set_keyword_plan(keyword_plan)
    audit.set_keyword_plan(keyword_plan)

    already_processed = _load_processed_urls()
    discovery_metadata: dict = {"gap_manifest": gap_manifest}
    candidates = _ddg_discover(
        query,
        max_candidates,
        already_processed,
        research_config,
        depth,
        keyword_plan=keyword_plan,
        discovery_metadata=discovery_metadata,
        repeat_urls=discovery_history.get("seen_urls", set()),
    )
    if depth == "shallow" and len(candidates) < int(max_candidates * 0.75):
        seen_so_far = already_processed | {c["url"] for c in candidates}
        needed = max_candidates - len(candidates)
        deep_metadata: dict = {}
        deep_extras = _ddg_discover(
            query,
            needed,
            seen_so_far,
            research_config,
            "deep",
            keyword_plan=keyword_plan,
            discovery_metadata=deep_metadata,
            repeat_urls=discovery_history.get("seen_urls", set()),
        )
        if deep_extras:
            candidates.extend(deep_extras)
            discovery_metadata["queries_used"] = (
                discovery_metadata.get("queries_used", [])
                + deep_metadata.get("queries_used", [])
            )
            discovery_metadata["suppressed_repeat_urls"] = sorted(set(
                discovery_metadata.get("suppressed_repeat_urls", [])
                + deep_metadata.get("suppressed_repeat_urls", [])
            ))
            produced = dict(discovery_metadata.get("produced_by_query", {}))
            for q, count in deep_metadata.get("produced_by_query", {}).items():
                produced[q] = produced.get(q, 0) + count
            discovery_metadata["produced_by_query"] = produced
            print(f"[{session_id}] Low discovery yield — added {len(deep_extras)} deep candidates")

    session_state.set_candidates(candidates)
    session_state.set_discovery_metadata(discovery_metadata)
    audit.set_discovery_metadata(discovery_metadata)
    audit.set_candidates_found(len(candidates))
    print(f"[{session_id}] DDG discovery found {len(candidates)} candidates")
    return _run_research_state(session_state)


def resume_research_session(session_id: str) -> dict:
    research_config = _load_research_config()
    session_state = ResearchSessionState.load(session_id, _research_state_dir(research_config))
    print(f"[{session_id}] Resuming research session: {session_state.query!r}")
    return _run_research_state(session_state)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LLM Wiki auto research harness")
    subparsers = parser.add_subparsers(dest="command")

    setup_parser = subparsers.add_parser("setup", help="Configure first-run wiki setup")
    setup_subparsers = setup_parser.add_subparsers(dest="setup_command")
    theme_parser = setup_subparsers.add_parser("theme", help="Choose a theme-derived organization profile")
    theme_parser.add_argument("theme", help="Broad wiki theme, e.g. 'RISC-V AI accelerator'")
    theme_parser.add_argument(
        "--choice",
        help="Organization profile id/name to write. Omit to list options without writing.",
    )
    theme_parser.add_argument("--dry-run", action="store_true", help="Show the selected profile without writing")

    research_parser = subparsers.add_parser("research", help="Run a research session")
    research_parser.add_argument("--query", help="Research query")
    research_parser.add_argument("--max-candidates", type=int, default=10)
    research_parser.add_argument("--max-new-pages", type=int, default=5)
    research_parser.add_argument("--depth", choices=["shallow", "deep"], default="shallow")
    research_parser.add_argument("--resume", help="Resume a prior session id")
    research_parser.add_argument("--list-sessions", action="store_true", help="List resumable research sessions")

    patch_parser = subparsers.add_parser("patch", help="Operate on the wiki patch queue")
    patch_subparsers = patch_parser.add_subparsers(dest="patch_command")
    patch_subparsers.add_parser(
        "apply",
        help="Apply human-approved merge_pending patches (status: approved) via the content-merge subagent",
    )

    index_parser = subparsers.add_parser("index", help="Operate on wiki/index.md")
    index_subparsers = index_parser.add_subparsers(dest="index_command")
    index_subparsers.add_parser(
        "rebuild",
        help="Regenerate wiki/index.md tables and header stats from page frontmatter "
             "(fixes drift left by manual edits, e.g. retrospective lint MERGE/DELETE/RESTRUCTURE)",
    )

    args = parser.parse_args()
    if args.command == "setup":
        if args.setup_command != "theme":
            setup_parser.print_help()
            sys.exit(1)
        if not args.choice:
            profiles = propose_profiles(args.theme)
            _save_cached_profiles(args.theme, profiles)
            for profile in profiles:
                print(f"{profile['id']}\t{profile['name']}\t{profile['description']}")
            print("Pass --choice <id> to write the selected profile into CLAUDE.md.")
            sys.exit(0)
        try:
            profile = setup_theme(args.theme, args.choice, write=not args.dry_run)
        except ValueError as e:
            theme_parser.error(str(e))
        print(yaml.dump(profile, sort_keys=False, allow_unicode=True).strip())
        sys.exit(0)
    if args.command == "research":
        logging.basicConfig(level=logging.WARNING)
        research_config = _load_research_config()
        if args.list_sessions:
            for session in list_sessions(_research_state_dir(research_config)):
                print(
                    f"{session['session_id']}\t{session.get('status')}\t"
                    f"{session.get('updated_at')}\t{session.get('query')}"
                )
            sys.exit(0)
        if args.resume:
            result = resume_research_session(args.resume)
        else:
            if not args.query:
                research_parser.error("--query is required unless --resume or --list-sessions is used")
            result = run_research_session(
                query=args.query,
                max_candidates=args.max_candidates,
                max_new_pages=args.max_new_pages,
                depth=args.depth,
            )
        sys.exit(0 if result.get("status") in ("complete", "discovery_failed") else 1)
    if args.command == "patch":
        if args.patch_command != "apply":
            patch_parser.print_help()
            sys.exit(1)
        logging.basicConfig(level=logging.WARNING)
        summary = apply_patch_queue()
        sys.exit(0 if summary.get("failed", 0) == 0 else 1)
    if args.command == "index":
        if args.index_command != "rebuild":
            index_parser.print_help()
            sys.exit(1)
        rebuild_index_from_frontmatter()
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
