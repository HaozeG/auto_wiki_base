"""
Wiki page context selector for EvalManifest injection.

Uses qmd for similarity search to find the most relevant wiki pages
for a given resource, then greedily selects within a token budget.
Falls back to inbound_links-based ranking when qmd is unavailable.
"""

import subprocess
import sys
from pathlib import Path

import yaml


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
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    try:
        fm = yaml.safe_load(text[3:end].strip()) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, text


def _list_all_pages() -> list[Path]:
    if not _WIKI_PAGES_DIR.exists():
        return []
    return list(_WIKI_PAGES_DIR.rglob("*.md"))


def _qmd_search(query_text: str, top: int = 20) -> list[tuple[str, float]]:
    """
    Run qmd search and return list of (filepath, score) pairs.
    Returns empty list if qmd is unavailable or returns no results.
    """
    try:
        result = subprocess.run(
            ["qmd", "search", query_text[:500], "--index", str(_WIKI_PAGES_DIR), "--top", str(top)],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []

    if result.returncode != 0:
        return []

    ranked: list[tuple[str, float]] = []
    score = float(top)
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        # qmd output format varies; treat each non-empty line as a result
        ranked.append((line, score))
        score -= 1.0
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


def select_context_pages(resource_content: str, max_tokens: int = 4000) -> list[dict]:
    """
    Select wiki pages relevant to resource_content, within max_tokens budget.

    Algorithm:
    1. Shell out: qmd search <resource_content[:500]> --top 20
    2. Parse ranked results; re-rank ties by inbound_links
    3. Greedily include pages until token budget reached
    4. Return list of {filename, type, content} dicts

    Falls back to inbound_links ranking if qmd is unavailable.
    """
    all_pages = _list_all_pages()
    if not all_pages:
        return []

    qmd_results = _qmd_search(resource_content)

    if qmd_results:
        # Build a map from filename stem → page path
        page_map = {p.name: p for p in all_pages}
        ranked_paths: list[tuple[Path, float]] = []
        seen = set()
        for filepath_str, score in qmd_results:
            # qmd may return absolute paths or just filenames
            candidate = Path(filepath_str)
            # Try to match by name
            matched = None
            for pg in all_pages:
                if pg.name == candidate.name or str(pg) == str(candidate):
                    matched = pg
                    break
            if matched and str(matched) not in seen:
                fm, _ = _parse_frontmatter(matched)
                inbound = float(fm.get("inbound_links", 0))
                # Break score ties with inbound_links
                ranked_paths.append((matched, score + inbound * 0.001))
                seen.add(str(matched))
        # Include any pages not in qmd results (score=0) but sort them after
        for pg in all_pages:
            if str(pg) not in seen:
                ranked_paths.append((pg, 0.0))
    else:
        # qmd unavailable — rank by inbound_links
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
