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
from context_selector import get_topic_hit_count, select_context_pages
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


_STOP_WORDS = {"the", "a", "an", "of", "for", "in", "and", "on", "with", "by", "to", "is"}


def _title_word_overlap(title: str, stem: str) -> float:
    """
    Return similarity between a candidate title and a filename stem.

    Combines Jaccard on word sets with a substring check. The substring check
    handles compound filenames like 'milkv_pioneer' where 'milk' and 'pioneer'
    are concatenated without separator.

    Title is cleaned by taking the first segment before '|', '—', ' - ' separators
    (web page titles often append site names or descriptions after these).
    """
    # Strip page-title boilerplate (e.g. "Milk-V Pioneer | Make native RISC-V...")
    clean = re.split(r"\s*[|—]\s*|\s+-\s+", title)[0].strip()
    t_words = set(re.findall(r"\w+", clean.lower())) - _STOP_WORDS
    s_words = set(re.findall(r"\w+", stem.replace("_", " ").replace("-", " ").lower())) - _STOP_WORDS

    if not t_words:
        return 0.0

    # Standard Jaccard on tokenized words
    union = t_words | s_words
    jaccard = len(t_words & s_words) / len(union) if union else 0.0

    # Substring check: handles "milk" ⊂ "milkv_pioneer" (concatenated compound words)
    stem_compact = stem.lower().replace("_", "").replace("-", "")
    long_t = [w for w in t_words if len(w) > 3]
    if long_t:
        contained = sum(1 for w in long_t if w in stem_compact)
        substr_ratio = contained / len(long_t)
    else:
        substr_ratio = 0.0

    return max(jaccard, substr_ratio)


def _title_matches_existing(title: str, extra_stems: set[str] | None = None,
                             overlap_threshold: float = 0.6) -> str | None:
    """
    Return matched filename stem if title is too similar to an existing page or
    a page already written this session (extra_stems).
    Returns None if no match.
    """
    if not title:
        return None

    # Check pages written this session first (not yet in index)
    if extra_stems:
        for stem in extra_stems:
            if _title_word_overlap(title, stem) >= overlap_threshold:
                return stem

    # Check existing wiki pages on disk
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        if _title_word_overlap(title, p.stem) >= overlap_threshold:
            return p.stem
    return None


def _check_synthesis_gaps() -> list[str]:
    """
    Find tag clusters with 3+ entity pages that have no synthesis page covering them.
    Returns a list of human-readable gap descriptions for the log.
    """
    tag_to_pages: dict[str, list[str]] = {}
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[3:end].strip()) or {}
        except yaml.YAMLError:
            continue
        if fm.get("type") == "entity":
            for tag in fm.get("tags", []):
                tag_to_pages.setdefault(tag, []).append(p.stem)

    # Collect all entity pages already named in a synthesis connected_entities list
    covered: set[str] = set()
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[3:end].strip()) or {}
        except yaml.YAMLError:
            continue
        if fm.get("type") == "synthesis":
            covered.update(fm.get("connected_entities", []))

    gaps = []
    for tag, pages in sorted(tag_to_pages.items(), key=lambda x: -len(x[1])):
        uncovered = [pg for pg in pages if pg not in covered]
        if len(uncovered) >= 3:
            sample = ", ".join(uncovered[:3])
            gaps.append(
                f"tag='{tag}': {len(uncovered)} entity pages without synthesis coverage "
                f"(e.g. {sample}{'...' if len(uncovered) > 3 else ''})"
            )
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
# Source-aware content extraction
# ---------------------------------------------------------------------------

_ARXIV_ABS_RE = re.compile(r"arxiv\.org/abs/([\w.]+)")
_GH_REPO_RE   = re.compile(r"github\.com/([^/]+)/([^/?#]+)/?(?:[?#].*)?$")
_GH_PR_RE     = re.compile(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)")


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


def _fetch_github(url: str) -> str | None:
    """Dispatch to PR or README fetch based on URL shape."""
    m = _GH_PR_RE.search(url)
    if m:
        return _fetch_github_pr(*m.groups())
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
    import os as _os
    model = (
        _os.environ.get("ANTHROPIC_DEFAULT_HAIKU_MODEL")
        or _os.environ.get("CLAUDE_CODE_SUBAGENT_MODEL")
        or "claude-haiku-4-5-20251001"
    )
    # Strip any stray ANSI-code artifacts that may appear in env values (e.g. [1m])
    model = re.sub(r"\[[\d;]*m\]?", "", model).strip()

    if subagent_type == "discovery":
        system = DISCOVERY_SYSTEM_PROMPT
        max_tokens = research_config.get("max_discovery_subagent_tokens", 3000)
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
            "_call_subagent: hit max_tokens (%d) before text output — "
            "thinking model exhausted budget. Increase max_tokens.",
            max_tokens,
        )
    for block in message.content:
        if hasattr(block, "text"):
            return block.text
    raise RuntimeError(
        f"No text block in subagent response (stop={message.stop_reason}, "
        f"blocks={[type(b).__name__ for b in message.content]})"
    )


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
    fm["updated"] = today          # always reflect write date
    fm["cold_start"] = True        # new pages always cold until retrospective lint clears them
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


def _run_qmd_update() -> None:
    """Re-index wiki pages so qmd search reflects newly written pages."""
    result = subprocess.run(
        ["qmd", "update"],
        capture_output=True,
        text=True,
        cwd=str(_PROJECT_ROOT),
    )
    if result.stdout:
        logger.info("qmd update: %s", result.stdout.strip())


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

    if page_type == "entity":
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
# DDG-based discovery (replaces LLM URL hallucination)
# ---------------------------------------------------------------------------

def _ddg_discover(query: str, max_candidates: int, already_processed: set[str],
                  research_config: dict, depth: str) -> list[dict]:
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

    # Generate search query variants from the base query
    concept_gaps = _get_concept_gaps()
    queries = [query]

    # Add concept-gap queries as STANDALONE searches (not appended to base query).
    # Appending gaps to the base query keeps discovery within the same product space;
    # standalone queries widen to adjacent concepts.
    if concept_gaps:
        for gap in concept_gaps[:min(2, len(concept_gaps))]:
            if len(queries) < limit:
                queries.append(gap)

    # Add synthesis-oriented queries to pull in comparison/survey sources, which
    # tend to produce synthesis pages rather than more product entity pages.
    if len(queries) < limit:
        queries.append(f"{query} comparison survey architecture overview")
    if len(queries) < limit:
        queries.append(f"{query} taxonomy ecosystem landscape")

    # Add source-targeted variants for arXiv and GitHub when the query is technical
    # or when depth=deep explicitly requests broader coverage.
    _TECHNICAL_KEYWORDS = ("paper", "arxiv", "repo", "github", "implementation", "code", "algorithm")
    if depth == "deep" or any(kw in query.lower() for kw in _TECHNICAL_KEYWORDS):
        if len(queries) < limit:
            queries.append(f"site:arxiv.org {query}")
        if len(queries) < limit:
            queries.append(f"site:github.com {query}")

    # Pad with topic refinements
    refinements = ["chip specifications performance", "ISA extension benchmark"]
    for ref in refinements:
        if len(queries) >= limit:
            break
        queries.append(f"{query} {ref}")

    # Domains and extensions that reliably yield unusable content for the eval agent
    _URL_BLOCKLIST = (
        "youtube.com", "youtu.be", "slideshare.net", "reddit.com",
        "twitter.com", "x.com", "linkedin.com", "facebook.com",
    )

    def _is_blocked(url: str) -> bool:
        lower = url.lower()
        if lower.endswith(".pdf"):
            return True
        return any(d in lower for d in _URL_BLOCKLIST)

    seen_urls: set[str] = set(already_processed)
    candidates: list[dict] = []

    with DDGS() as ddgs:
        for q in queries:
            if len(candidates) >= max_candidates:
                break
            try:
                for r in ddgs.text(q, max_results=results_per_query):
                    url = r.get("href", "")
                    if not url or url in seen_urls or _is_blocked(url):
                        continue
                    seen_urls.add(url)
                    candidates.append({
                        "url": url,
                        "title": r.get("title", ""),
                        "snippet": r.get("body", ""),
                        "estimated_type": "entity",
                    })
                    if len(candidates) >= max_candidates:
                        break
            except Exception as e:
                logger.warning("DDG search failed for %r: %s", q, e)

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

def run_research_session(query: str, max_candidates: int, max_new_pages: int,
                          depth: str) -> dict:
    session_id = _generate_session_id()
    scope = {"max_candidates": max_candidates, "max_new_pages": max_new_pages, "depth": depth}
    research_config = _load_claude_md_block("research_config")
    audit = AuditLog(session_id, query, scope)
    quota = QuotaManager(max_candidates=max_candidates, max_new_pages=max_new_pages)

    print(f"[{session_id}] Starting research session: {query!r}")

    # --- Step 1: Discovery via DuckDuckGo (real URLs, no hallucination) ---
    already_processed = _load_processed_urls()
    candidates = _ddg_discover(query, max_candidates, already_processed, research_config, depth)

    # Trigger 1: if shallow discovery yielded < 75% of requested candidates, do a
    # second deep pass immediately (no API cost — just more DDG queries).
    if depth == "shallow" and len(candidates) < int(max_candidates * 0.75):
        seen_so_far = already_processed | {c["url"] for c in candidates}
        needed = max_candidates - len(candidates)
        deep_extras = _ddg_discover(query, needed, seen_so_far, research_config, "deep")
        if deep_extras:
            candidates.extend(deep_extras)
            print(f"[{session_id}] Low discovery yield — added {len(deep_extras)} deep candidates")

    audit.set_candidates_found(len(candidates))
    print(f"[{session_id}] DDG discovery found {len(candidates)} candidates")

    # --- Step 3: Evaluate each candidate ---
    approved_pages: list[tuple[dict, str]] = []
    pipeline_rejections = 0
    # effective_depth may be upgraded to "deep" mid-session (Trigger 2).
    effective_depth = depth
    halfway = max(1, (max_candidates + 1) // 2)
    # Track filename stems of pages already written this session for within-session dedup.
    session_written_stems: set[str] = set()

    for candidate in candidates:
        if quota.any_exceeded():
            print(f"[{session_id}] Quota exceeded, stopping early")
            break

        url = candidate["url"]
        title = candidate.get("title", "")

        # Pre-eval gate 1: within-session and on-disk title dedup.
        # Check before fetching content to avoid wasting API calls on duplicates.
        existing_match = _title_matches_existing(title, session_written_stems)
        if existing_match:
            print(f"[{session_id}] Skipping duplicate: {title!r} overlaps with '{existing_match}'")
            audit.log_skip_pre_eval(url, f"title_overlap: matches '{existing_match}'")
            pipeline_rejections += 1
            continue

        # Pre-eval gate 2: qmd similarity — skip if wiki already has many pages on this topic.
        # A high hit count means the concept is well-covered; the candidate would be redundant.
        snippet = candidate.get("snippet", "")
        topic_hits = get_topic_hit_count(f"{title} {snippet[:200]}")
        if topic_hits >= 4:
            print(f"[{session_id}] Skipping over-covered topic: {title!r} ({topic_hits} similar pages)")
            audit.log_skip_pre_eval(url, f"topic_saturation: {topic_hits} similar pages in wiki")
            pipeline_rejections += 1
            continue

        print(f"[{session_id}] Evaluating: {url}")

        content = _fetch_smart(
            url, retries=research_config.get("max_retries_on_fetch_failure", 2)
        )
        # Fall back to DDG snippet when fetch fails or returns only JS boilerplate
        # (heuristic: <500 non-whitespace chars of body text → treat as empty)
        if content is None:
            # Fetch failed — enrich snippet by running a focused DDG search for the title
            enriched = _enrich_snippet(candidate.get("title", ""), snippet)
            if not enriched:
                logger.warning("fetch failed and no enriched snippet for %s — skipping", url)
                continue
            logger.info("fetch failed for %s — using enriched DDG snippet (%d chars)", url, len(enriched))
            content = enriched
        else:
            # Strip HTML tags to get plain text — removes CSS/nav boilerplate that fills
            # the first N chars of JS-heavy pages and confuses the eval agent.
            if "<html" in content[:500].lower() or "<!doctype" in content[:200].lower():
                content = re.sub(r"<[^>]+>", " ", content)
                content = re.sub(r"\s{2,}", " ", content).strip()
            text_chars = len(re.sub(r"\s", "", content))
            if text_chars < 500:
                enriched = _enrich_snippet(candidate.get("title", ""), snippet)
                logger.info("thin page (%d text chars) for %s — using enriched snippet", text_chars, url)
                content = enriched or content[:2000]

        # Also reject raw binary content (e.g. PDFs that slipped past the URL filter)
        if content and content[:4] in ("%PDF", b"%PDF"[:4] if isinstance(content, bytes) else ""):
            logger.info("binary/PDF content for %s — using enriched snippet", url)
            content = _enrich_snippet(candidate.get("title", ""), snippet) or snippet

        # Trigger 4: in deep mode, proactively supplement primary content with DDG
        # snippets so the eval agent has multiple perspectives even on good fetches.
        if effective_depth == "deep" and content:
            supplement = _enrich_snippet(candidate.get("title", ""), candidate.get("snippet", ""))
            if supplement:
                content = content + "\n\n[DDG supplemental context]\n" + supplement

        # Trigger 3: expand content window in deep mode to capture more of long documents.
        content_limit = 10000 if effective_depth == "deep" else 6000

        injected_pages = select_context_pages(content[:content_limit])
        is_cold_start = not _wiki_is_mature()
        eval_config = _load_claude_md_block("eval_thresholds")

        eval_manifest = {
            "candidate": {"url": url, "title": candidate.get("title", "")},
            "resource_content": content[:content_limit],
            "wiki_context": {
                "relevant_pages": injected_pages,
                "concept_gaps": _get_concept_gaps(),
                "graph_maturity": not is_cold_start,
                "depth": effective_depth,
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

        eval_result = validate_and_parse(raw_eval, "EvalResult")
        audit.record_response(ev_idx, raw_eval, schema_valid=(eval_result is not None))
        if eval_result is None:
            audit.record_skip(ev_idx, "malformed_eval_output")
            continue

        quota.record_candidate_evaluated()

        # Trigger 2: mid-session adaptive depth escalation.
        # If we're at the halfway point and have written nothing, upgrade to deep
        # for the remaining candidates to push harder on content quality.
        if (quota._candidates_evaluated == halfway
                and quota._pages_written == 0
                and effective_depth == "shallow"):
            effective_depth = "deep"
            print(f"[{session_id}] Adaptive escalation: 0 pages after {halfway} candidates → depth=deep")
            audit.log_escalation(halfway)

        if eval_result.get("decision") == "reject":
            audit.record_skip(ev_idx, f"subagent_reject: {eval_result.get('rejection_reason', '')}")
            continue

        # --- Programmatic score gate ---
        # Enforce weighted_total threshold regardless of LLM's approve decision.
        eval_sc = eval_result.get("scorecard", {})
        weighted_total = eval_sc.get("weighted_total", 0.0) or 0.0
        acceptance_threshold = (
            eval_manifest["scorecard_config"].get("acceptance_threshold", 0.4)
        )
        hard_rejection_threshold = (
            eval_manifest["scorecard_config"].get("hard_rejection_threshold", 0.2)
        )
        any_hard_fail = any(
            (v or 0.0) < hard_rejection_threshold
            for k, v in eval_sc.items()
            if k not in ("weighted_total", "contradiction_potential")
            and v is not None
        )
        if weighted_total < acceptance_threshold:
            reason = (
                f"score_gate_reject: weighted_total={weighted_total:.2f} "
                f"< acceptance_threshold={acceptance_threshold}"
            )
            audit.record_skip(ev_idx, reason)
            pipeline_rejections += 1
            continue
        if any_hard_fail:
            reason = (
                f"score_gate_reject: a scorecard dimension is below "
                f"hard_rejection_threshold={hard_rejection_threshold}"
            )
            audit.record_skip(ev_idx, reason)
            pipeline_rejections += 1
            continue

        # --- Step 4: Deterministic pipeline gate ---
        for draft in eval_result.get("page_drafts", []):
            # Transfer scorecard scores from eval result into draft frontmatter
            _apply_scorecard_to_draft(draft, eval_sc)
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
                approved_pages.append((draft, url, ev_idx))
            else:
                pipeline_rejections += 1

    # Snapshot evaluated count before writes so a crash in the write loop
    # still preserves an accurate candidates_evaluated in the audit.
    audit.set_candidates_evaluated(quota._candidates_evaluated)

    # --- Step 5: Write approved pages ---
    written_filenames = []
    for draft, _source_url, ev_idx in approved_pages:
        if quota.pages_exceeded():
            break
        try:
            page_path = _write_page(draft)
            _update_inbound_links(draft)
            _update_index(draft)
            quota.record_page_written()
            written_filenames.append(page_path.name)
            session_written_stems.add(page_path.stem)
            audit.record_page_written(ev_idx, page_path.name)
            print(f"[{session_id}] Written: {page_path}")
        except Exception as e:
            logger.error("Failed to write page %s: %s", draft.get("filename"), e)

    # --- Step 6: Post-session bookkeeping ---
    _run_graph_stats()
    _run_qmd_update()

    synthesis_gaps = _check_synthesis_gaps()
    if synthesis_gaps:
        print(f"[{session_id}] Synthesis gaps detected ({len(synthesis_gaps)}):")
        for gap in synthesis_gaps[:5]:
            print(f"  {gap}")

    _append_log(
        session_id=session_id,
        pages_written=written_filenames,
        audit_path=audit.path,
        candidates_found=len(candidates),
        candidates_evaluated=quota._candidates_evaluated,
        query=query,
        rejected_by_pipeline=pipeline_rejections,
    )

    summary = {
        "session_id": session_id,
        "candidates_found": len(candidates),
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
