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
import hashlib
import json
import logging
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

from audit import AuditLog
from context_selector import select_context_pages
from quota import MAX_TOKENS_PER_SUBAGENT_OUTPUT, MIN_SECONDS_BETWEEN_CALLS, QuotaManager
from subagent_prompts import DISCOVERY_SYSTEM_PROMPT, EVALUATION_SYSTEM_PROMPT
from validate_output import validate_and_parse

logger = logging.getLogger(__name__)

_PROJECT_ROOT = _TOOLS_DIR.parent
_WIKI_PAGES_DIR = _PROJECT_ROOT / "wiki" / "_pages"
_INDEX_MD = _PROJECT_ROOT / "wiki" / "index.md"
_LOG_MD = _PROJECT_ROOT / "wiki" / "log.md"
_CLAUDE_MD = _PROJECT_ROOT / "CLAUDE.md"

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


def _load_processed_urls() -> set[str]:
    """Extract URLs already processed from wiki/log.md."""
    if not _LOG_MD.exists():
        return set()
    text = _LOG_MD.read_text(encoding="utf-8")
    return set(re.findall(r"https?://\S+", text))


def _wiki_is_mature() -> bool:
    text = _CLAUDE_MD.read_text(encoding="utf-8")
    match = re.search(r"graph_maturity:\s*(true|false)", text)
    return bool(match and match.group(1) == "true")


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


def _get_concept_gaps() -> list[str]:
    """Extract concepts with no dedicated page from the Concept Index."""
    if not _INDEX_MD.exists():
        return []
    text = _INDEX_MD.read_text(encoding="utf-8")
    gaps = re.findall(r"\*\*(.+?)\*\*:.*?no dedicated page", text)
    return gaps


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

    if subagent_type == "discovery":
        system = DISCOVERY_SYSTEM_PROMPT
        max_tokens = research_config.get("max_discovery_subagent_tokens", 1000)
    else:
        system = EVALUATION_SYSTEM_PROMPT
        max_tokens = research_config.get("max_eval_subagent_tokens", 2000)

    max_tokens = min(max_tokens, MAX_TOKENS_PER_SUBAGENT_OUTPUT)

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": json.dumps(manifest)}],
    )
    return message.content[0].text


# ---------------------------------------------------------------------------
# Wiki write operations
# ---------------------------------------------------------------------------

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

    subdir = _WIKI_PAGES_DIR / ("entity" if page_type == "entity" else "synthesis")
    subdir.mkdir(parents=True, exist_ok=True)
    page_path = subdir / filename

    fm = draft.get("frontmatter", {})
    content = draft.get("content", "")

    # Ensure required frontmatter fields
    today = _now_date()
    fm.setdefault("type", page_type)
    fm.setdefault("created", today)
    fm.setdefault("updated", today)
    fm.setdefault("cold_start", not _wiki_is_mature())
    fm.setdefault("inbound_links", 0)

    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    page_path.write_text(f"---\n{fm_yaml}---\n\n{content}\n", encoding="utf-8")
    return page_path


def _update_inbound_links(draft: dict) -> None:
    """Increment inbound_links on pages referenced from this draft's content."""
    content = draft.get("content", "")
    refs = re.findall(r"\[\[([^\]]+)\]\]", content)
    for ref in set(refs):
        for page in _WIKI_PAGES_DIR.rglob(f"{ref}.md"):
            _increment_frontmatter_field(page, "inbound_links")


def _increment_frontmatter_field(path: Path, field: str) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return
    end = text.find("---", 3)
    if end == -1:
        return
    try:
        fm = yaml.safe_load(text[3:end].strip()) or {}
    except yaml.YAMLError:
        return
    fm[field] = int(fm.get(field, 0)) + 1
    body = text[end:]
    path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---{body}",
                    encoding="utf-8")


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
    else:
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

    # Update header stats
    page_count = len(list(_WIKI_PAGES_DIR.rglob("*.md")))
    text = re.sub(r"Last updated: \S+", f"Last updated: {_now_date()}", text)
    text = re.sub(r"Pages: \d+", f"Pages: {page_count}", text)
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


def _run_eval_pipeline(draft: dict) -> tuple[bool, dict]:
    """
    Write draft to a temp file and run eval_summary.py against it.
    Returns (passes, pipeline_result_dict).
    """
    page_type = draft.get("page_type", "entity")
    fm = draft.get("frontmatter", {})
    content = draft.get("content", "")
    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    page_md = f"---\n{fm_yaml}---\n\n{content}\n"

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
                 rejected_by_pipeline: int) -> None:
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
    with open(_LOG_MD, "a", encoding="utf-8") as f:
        f.write(entry)


def _build_page_templates() -> dict:
    """Return entity and synthesis page templates from CLAUDE.md."""
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
    return {"entity": entity_template, "synthesis": synthesis_template}


# ---------------------------------------------------------------------------
# Main research session
# ---------------------------------------------------------------------------

def run_research_session(query: str, max_candidates: int, max_new_pages: int,
                          depth: str) -> dict:
    session_id = _generate_session_id()
    scope = {"max_candidates": max_candidates, "max_new_pages": max_new_pages, "depth": depth}
    research_config = _load_claude_md_block("research_config")
    audit = AuditLog(session_id, query, scope)
    quota = QuotaManager(max_candidates=max_candidates, max_new_pages=max_new_pages)

    print(f"[{session_id}] Starting research session: {query!r}")

    # --- Step 1: Discovery ---
    already_processed = list(_load_processed_urls())
    discovery_manifest = {
        "query": query,
        "scope": {"max_candidates": max_candidates, "depth": depth},
        "already_processed_urls": already_processed,
        "wiki_topic_summary": _get_wiki_topic_summary(),
        "existing_concept_gaps": _get_concept_gaps(),
    }

    inv_idx = audit.record_invocation("discovery", discovery_manifest)
    try:
        time.sleep(MIN_SECONDS_BETWEEN_CALLS)
        quota.record_api_call()
        raw_discovery = _call_subagent("discovery", discovery_manifest, research_config)
    except Exception as e:
        logger.error("Discovery API call failed: %s", e)
        audit.record_response(inv_idx, str(e), schema_valid=False)
        return {"status": "discovery_failed", "session_id": session_id}

    audit.record_response(inv_idx, raw_discovery, schema_valid=False)
    candidate_list = validate_and_parse(raw_discovery, "CandidateList")
    if candidate_list is None:
        audit.record_skip(inv_idx, "schema_validation_failure")
        return {"status": "discovery_failed", "session_id": session_id}

    audit.record_response(inv_idx, raw_discovery, schema_valid=True)
    candidates = candidate_list.get("candidates", [])
    audit.set_candidates_found(len(candidates))
    print(f"[{session_id}] Discovery found {len(candidates)} candidates")

    # --- Step 2: Dedup + cap ---
    processed_urls = _load_processed_urls()
    candidates = [c for c in candidates if c["url"] not in processed_urls]
    candidates = candidates[:max_candidates]

    # --- Step 3: Evaluate each candidate ---
    approved_pages: list[tuple[dict, str]] = []
    pipeline_rejections = 0

    for candidate in candidates:
        if quota.any_exceeded():
            print(f"[{session_id}] Quota exceeded, stopping early")
            break

        url = candidate["url"]
        print(f"[{session_id}] Evaluating: {url}")

        content = fetch_resource(
            url, retries=research_config.get("max_retries_on_fetch_failure", 2)
        )
        if content is None:
            logger.warning("fetch failed for %s", url)
            continue

        injected_pages = select_context_pages(content[:6000])
        is_cold_start = not _wiki_is_mature()
        eval_config = _load_claude_md_block("eval_thresholds")

        eval_manifest = {
            "candidate": {"url": url, "title": candidate.get("title", "")},
            "resource_content": content[:6000],
            "wiki_context": {
                "relevant_pages": injected_pages,
                "concept_gaps": _get_concept_gaps(),
                "graph_maturity": not is_cold_start,
            },
            "scorecard_config": {
                "variant": "cold_start" if is_cold_start else candidate.get("estimated_type", "entity"),
                "weights": eval_config,
                "acceptance_threshold": 0.4,
                "hard_rejection_threshold": 0.2,
            },
            "page_templates": _build_page_templates(),
        }

        ev_idx = audit.record_invocation("evaluation", eval_manifest)
        try:
            time.sleep(MIN_SECONDS_BETWEEN_CALLS)
            quota.record_api_call()
            raw_eval = _call_subagent("evaluation", eval_manifest, research_config)
        except Exception as e:
            logger.error("Evaluation API call failed for %s: %s", url, e)
            audit.record_response(ev_idx, str(e), schema_valid=False)
            continue

        audit.record_response(ev_idx, raw_eval, schema_valid=False)
        eval_result = validate_and_parse(raw_eval, "EvalResult")
        if eval_result is None:
            audit.record_skip(ev_idx, "malformed_eval_output")
            continue

        audit.record_response(ev_idx, raw_eval, schema_valid=True)
        quota.record_candidate_evaluated()

        if eval_result.get("decision") == "reject":
            audit.record_skip(ev_idx, f"subagent_reject: {eval_result.get('rejection_reason', '')}")
            continue

        # --- Step 4: Deterministic pipeline gate ---
        for draft in eval_result.get("page_drafts", []):
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
                approved_pages.append((draft, url))
            else:
                pipeline_rejections += 1

    # --- Step 5: Write approved pages ---
    written_filenames = []
    for draft, _source_url in approved_pages:
        if quota.pages_exceeded():
            break
        page_path = _write_page(draft)
        _update_inbound_links(draft)
        _update_index(draft)
        quota.record_page_written()
        written_filenames.append(page_path.name)
        audit.record_page_written(
            next(
                i for i, inv in enumerate(audit._invocations)
                if inv["subagent_type"] == "evaluation"
                and inv.get("schema_valid")
            ),
            page_path.name,
        )
        print(f"[{session_id}] Written: {page_path}")

    # --- Step 6: Post-session bookkeeping ---
    _run_graph_stats()
    audit.set_candidates_evaluated(quota._candidates_evaluated)
    _append_log(
        session_id=session_id,
        pages_written=written_filenames,
        audit_path=audit.path,
        candidates_found=len(candidate_list.get("candidates", [])),
        candidates_evaluated=quota._candidates_evaluated,
        query=query,
        rejected_by_pipeline=pipeline_rejections,
    )

    summary = {
        "session_id": session_id,
        "candidates_found": len(candidate_list.get("candidates", [])),
        "candidates_evaluated": quota._candidates_evaluated,
        "pages_written": len(written_filenames),
        "pipeline_rejection_rate": f"{(pipeline_rejections / max(quota._candidates_evaluated, 1) * 100):.0f}%",
        "audit_log_path": str(audit.path),
        "status": "complete",
    }
    print(f"[{session_id}] Session complete: {summary}")
    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LLM Wiki auto research harness")
    subparsers = parser.add_subparsers(dest="command")

    research_parser = subparsers.add_parser("research", help="Run a research session")
    research_parser.add_argument("--query", required=True, help="Research query")
    research_parser.add_argument("--max-candidates", type=int, default=10)
    research_parser.add_argument("--max-new-pages", type=int, default=5)
    research_parser.add_argument("--depth", choices=["shallow", "deep"], default="shallow")

    args = parser.parse_args()
    if args.command == "research":
        logging.basicConfig(level=logging.WARNING)
        result = run_research_session(
            query=args.query,
            max_candidates=args.max_candidates,
            max_new_pages=args.max_new_pages,
            depth=args.depth,
        )
        sys.exit(0 if result.get("status") in ("complete", "discovery_failed") else 1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
