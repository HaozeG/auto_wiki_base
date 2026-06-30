"""
Wiki page context selector for EvalManifest injection.

Uses qmd for similarity search to find the most relevant wiki pages
for a given resource, then greedily selects within a token budget.
Falls back to inbound_links-based ranking when qmd is unavailable.
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


def _fallback_rank_by_inbound(pages: list[Path]) -> list[tuple[Path, float]]:
    """Rank pages by inbound_links when qmd is unavailable."""
    ranked = []
    for page in pages:
        fm, _ = _parse_frontmatter(page)
        inbound = float(fm.get("inbound_links", 0))
        ranked.append((page, inbound))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked


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
            inbound = float(fm.get("inbound_links", 0))
            ranked.append((page, score + inbound * 0.001))
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
                         structured_terms: dict | None = None) -> list[dict]:
    """
    Select wiki pages relevant to resource_content, within max_tokens budget.

    Algorithm:
    1. Shell out: qmd search <resource_content[:500]> -c _pages -n 20 --format json
    2. Parse ranked results with real similarity scores; re-rank ties by inbound_links
    3. Greedily include pages until token budget reached
    4. Return list of {filename, type, content} dicts

    Falls back to inbound_links ranking if qmd is unavailable.
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
                fm, _ = _parse_frontmatter(page)
                inbound = float(fm.get("inbound_links", 0))
                ranked_paths.append((page, score + inbound * 0.001))
                seen.add(str(page))
        for pg in all_pages:
            if str(pg) not in seen:
                ranked_paths.append((pg, 0.0))
    elif qmd_results:
        seen = set()
        ranked_paths: list[tuple[Path, float]] = []
        for page, score in qmd_results:
            if str(page) not in seen:
                fm, _ = _parse_frontmatter(page)
                inbound = float(fm.get("inbound_links", 0))
                # Break score ties with inbound_links (small nudge)
                ranked_paths.append((page, score + inbound * 0.001))
                seen.add(str(page))
        # Include any pages not returned by qmd (score=0) after the ranked ones
        for pg in all_pages:
            if str(pg) not in seen:
                ranked_paths.append((pg, 0.0))
    else:
        # qmd unavailable or no results — rank by inbound_links
        ranked_paths = _fallback_rank_by_inbound(all_pages)

    ranked_paths.sort(key=lambda x: x[1], reverse=True)

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
