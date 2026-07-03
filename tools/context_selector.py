"""
Wiki page context selector for EvalManifest injection.

Uses qmd for similarity search to find the most relevant wiki pages
for a given resource, then greedily selects within a token budget.
Falls back to a neutral (non-hub-biased) ranking when qmd is unavailable.

Found live (2026-07-03): ranking candidate pages by `inbound_links` — as a
tie-break nudge here, and as the sole sort key in the qmd-unavailable
fallback — is a preferential-attachment loop, not a legitimate relevance
signal. A page with many inbound links gets shown to the drafting subagent
more often as "context," so new pages cite it more, so its inbound_links
grows further. Measured on two independent replication runs: a single
incidental hardware-target page was injected into 59-76% of all evaluation
invocations, and ~75% of the resulting Relationships citations were generic
"for comparison" boilerplate rather than specific reasoned relationships —
this is design-doc-specified behavior (§12.7: "rank ... by inbound_links,
hub pages first"), not a regression, but it directly violates CLAUDE.md's
Graph Topology Philosophy ("bridges should be few, deliberate, and
reasoned, not numerous and shallow"). `inbound_links` no longer influences
ranking anywhere in this module; injection is additionally capped per page
per session (`injection_counts`/`injection_cap`) so even a genuinely
relevant page can't dominate every drafting context in a row.
"""

import re
import sys
from pathlib import Path

from frontmatter import split_frontmatter
from qmd_runner import QmdRunner


_WIKI_PAGES_DIR = Path(__file__).parent.parent / "wiki" / "_pages"
_APPROX_CHARS_PER_TOKEN = 4


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // _APPROX_CHARS_PER_TOKEN)


def _parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, full_text) for a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""
    fm, _body, _ = split_frontmatter(text)
    return fm, text


def _list_all_pages() -> list[Path]:
    if not _WIKI_PAGES_DIR.exists():
        return []
    return list(_WIKI_PAGES_DIR.rglob("*.md"))


def _resolve_qmd_path(qmd_file: str) -> Path | None:
    """
    Convert a qmd:// file path to an actual on-disk Path.

    qmd normalizes filenames to kebab-case internally (e.g. milkv-pioneer.md)
    while disk files use snake_case (milkv_pioneer.md). Try both.
    """
    # Strip the qmd:// prefix and the _pages/ collection prefix
    # qmd://_pages/entity/milkv-pioneer.md -> entity/milkv-pioneer.md
    rel = re.sub(r"^qmd://_pages/", "", qmd_file)
    if not rel:
        return None

    # Try as-is (hyphens), then with hyphens replaced by underscores
    for candidate in (rel, rel.replace("-", "_")):
        resolved = _WIKI_PAGES_DIR / candidate
        if resolved.exists():
            return resolved
    return None


def _qmd_search(query_text: str, top: int = 20, qmd_runner: QmdRunner | None = None) -> list[tuple[Path, float]]:
    """
    Run qmd search and return list of (page_path, score) pairs.
    Returns empty list if qmd is unavailable or returns no results.

    Uses JSON output format for reliable parsing and real similarity scores.
    """
    runner = qmd_runner or QmdRunner()
    result = runner.search(query_text, top=top, collection="_pages")
    if not result.ok:
        return []

    ranked: list[tuple[Path, float]] = []
    for rec in result.matches:
        qmd_file = rec.file
        score = float(rec.score or 0.0)
        if not qmd_file or score <= 0:
            continue
        path = _resolve_qmd_path(qmd_file)
        if path is not None:
            ranked.append((path, score))

    return ranked


def _fallback_rank_neutral(pages: list[Path]) -> list[tuple[Path, float]]:
    """Rank pages when qmd is unavailable and no structured terms matched.

    No topical signal exists at this point, so use a stable, bias-free
    order (filename) rather than `inbound_links` — sorting by inbound count
    here was the purest form of the preferential-attachment loop documented
    at module level, with no relevance signal at all to justify it."""
    return [(page, 0.0) for page in sorted(pages, key=lambda p: p.name)]


def _as_terms(value) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        raw = re.split(r"[,;]", value)
    elif isinstance(value, (list, tuple, set)):
        raw = value
    else:
        raw = [value]
    return {str(item).strip().lower() for item in raw if str(item).strip()}


def _structured_rank(
    pages: list[Path],
    structured_terms: dict | None,
) -> list[tuple[Path, float]]:
    """Rank pages by overlapping structured frontmatter fields."""
    if not structured_terms:
        return []
    fields = (
        "hardware_targets",
        "workloads",
        "datatypes",
        "metrics",
        "toolchains",
        "constraints",
        "evidence_strength",
    )
    query_terms = {field: _as_terms(structured_terms.get(field)) for field in fields}
    ranked: list[tuple[Path, float]] = []
    for page in pages:
        fm, _ = _parse_frontmatter(page)
        score = 0.0
        for field, terms in query_terms.items():
            if not terms:
                continue
            page_terms = _as_terms(fm.get(field))
            overlap = terms & page_terms
            if overlap:
                score += len(overlap)
        if score > 0:
            ranked.append((page, score))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked


def get_topic_hit_count(query_text: str, min_score: float = 0.5,
                        qmd_runner: QmdRunner | None = None) -> int:
    """
    Return how many wiki pages have meaningful similarity to query_text.
    Used by orchestrator as a pre-eval duplicate gate.
    """
    results = _qmd_search(query_text, top=10, qmd_runner=qmd_runner)
    return sum(1 for _, score in results if score >= min_score)


def select_context_pages(resource_content: str, max_tokens: int = 4000,
                         qmd_runner: QmdRunner | None = None,
                         structured_terms: dict | None = None,
                         injection_counts: dict[str, int] | None = None,
                         injection_cap: int = 3) -> list[dict]:
    """
    Select wiki pages relevant to resource_content, within max_tokens budget.

    Algorithm:
    1. Shell out: qmd search <resource_content[:500]> -c _pages -n 20 --format json
    2. Parse ranked results with real similarity scores (no inbound_links nudge —
       see module docstring)
    3. Deprioritize (not exclude) pages that have already hit `injection_cap`
       injections this session, per `injection_counts`
    4. Greedily include pages until token budget reached
    5. Return list of {filename, type, content} dicts

    Falls back to a neutral, bias-free ranking if qmd is unavailable.
    """
    all_pages = _list_all_pages()
    if not all_pages:
        return []

    structured_results = _structured_rank(all_pages, structured_terms)
    qmd_results = _qmd_search(resource_content, qmd_runner=qmd_runner)

    if structured_results:
        seen = set()
        ranked_paths = []
        for page, score in structured_results:
            ranked_paths.append((page, score + 100.0))
            seen.add(str(page))
        for page, score in qmd_results:
            if str(page) not in seen:
                ranked_paths.append((page, score))
                seen.add(str(page))
        for pg in all_pages:
            if str(pg) not in seen:
                ranked_paths.append((pg, 0.0))
    elif qmd_results:
        seen = set()
        ranked_paths: list[tuple[Path, float]] = []
        for page, score in qmd_results:
            if str(page) not in seen:
                ranked_paths.append((page, score))
                seen.add(str(page))
        # Include any pages not returned by qmd (score=0) after the ranked ones
        for pg in all_pages:
            if str(pg) not in seen:
                ranked_paths.append((pg, 0.0))
    else:
        # qmd unavailable or no results — rank neutrally, not by inbound_links
        ranked_paths = _fallback_rank_neutral(all_pages)

    ranked_paths.sort(key=lambda x: x[1], reverse=True)

    # Deprioritize (stable-partition, don't drop) pages already at/over the
    # per-session injection cap — keeps them eligible as a last resort if
    # nothing else is topically relevant, but stops them from crowding out
    # other candidates purely because they were shown before. Only reorder
    # within the positive-score prefix: zero-score filler pages must stay
    # last regardless of cap state, or they'd trip the "stop at first
    # zero-score page" rule below before a legitimately relevant but capped
    # page ever gets a chance.
    if injection_counts:
        positive = [rp for rp in ranked_paths if rp[1] > 0]
        zero = [rp for rp in ranked_paths if rp[1] <= 0]
        under_cap = [rp for rp in positive if injection_counts.get(rp[0].stem, 0) < injection_cap]
        at_cap = [rp for rp in positive if injection_counts.get(rp[0].stem, 0) >= injection_cap]
        ranked_paths = under_cap + at_cap + zero

    selected: list[dict] = []
    token_count = 0

    for page, score in ranked_paths:
        if score == 0.0 and selected:
            break  # no similarity signal — stop adding zero-score pages
        fm, full_text = _parse_frontmatter(page)
        page_tokens = _estimate_tokens(full_text)
        if token_count + page_tokens > max_tokens:
            continue  # skip this page, try smaller ones
        page_type = fm.get("type", "entity")
        selected.append({
            "filename": page.name,
            "type": page_type,
            "content": full_text,
        })
        token_count += page_tokens

    return selected
