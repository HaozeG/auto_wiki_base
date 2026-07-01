"""Canonical YAML-frontmatter parsing and atomic mutation for wiki pages.

Single source of truth for reading and writing page frontmatter. Replaces the
~4 duplicated parsers (graph_stats, context_selector, eval_summary, orchestrator)
and the fragile re-splice in orchestrator._increment_frontmatter_field, which
sliced ``text[end:]`` (keeping the closing ``---``) and then prepended another
``---`` on every write — accumulating three dashes per increment and corrupting
the delimiter. All mutation here goes parse -> mutate dict -> re-serialize, so a
malformed delimiter can never be produced by string splicing.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def dump_frontmatter(fm: dict) -> str:
    """Serialize a frontmatter dict to YAML with canonical, deterministic settings."""
    return yaml.safe_dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )


def split_frontmatter(text: str) -> tuple[dict, str, bool]:
    """Split raw markdown into ``(frontmatter, body, has_frontmatter)``.

    ``body`` is everything after the closing ``---`` delimiter (not stripped, so
    a parse->render round-trip is stable). When there is no valid frontmatter
    block, returns ``({}, text, False)``.
    """
    if not text.startswith("---"):
        return {}, text, False
    end = text.find("---", 3)
    if end == -1:
        return {}, text, False
    try:
        fm = yaml.safe_load(text[3:end].strip()) or {}
    except yaml.YAMLError:
        return {}, text, False
    if not isinstance(fm, dict):
        return {}, text, False
    return fm, text[end + 3:], True


def parse_page(path: Path) -> tuple[dict, str]:
    """Return ``(frontmatter, body)`` for a page; ``({}, "")`` if unreadable.

    ``body`` is the content after the closing delimiter (not stripped).
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""
    fm, body, _ = split_frontmatter(text)
    return fm, body


def parse_frontmatter(path: Path) -> dict:
    """Return only the frontmatter dict (compat shim for read-only callers)."""
    return parse_page(path)[0]


def render_page(fm: dict, body: str) -> str:
    """Render frontmatter + body to a single well-formed document with one
    ``---`` delimiter pair and a blank line before the body.

    Subagent drafts occasionally echo a duplicate frontmatter block inside
    their own ``content`` field (in addition to the separate structured
    ``frontmatter`` dict). If left in place, that duplicate block corrupts
    downstream first-paragraph/word-count extraction, so it is stripped here
    before assembling the canonical single-frontmatter document.
    """
    body = body.lstrip("\n")
    _, stripped_body, has_embedded_fm = split_frontmatter(body)
    if has_embedded_fm:
        body = stripped_body.lstrip("\n")
    rendered = f"---\n{dump_frontmatter(fm)}---\n\n{body}"
    if not rendered.endswith("\n"):
        rendered += "\n"
    return rendered


def write_page(path: Path, fm: dict, body: str) -> None:
    """Write frontmatter + body to disk via the canonical renderer."""
    path.write_text(render_page(fm, body), encoding="utf-8")


def set_page_field(path: Path, key: str, value) -> bool:
    """Atomically set/replace one frontmatter field, preserving the body.

    No-op (returns False) when the file has no valid frontmatter block.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    fm, body, has_fm = split_frontmatter(text)
    if not has_fm:
        return False
    fm[key] = value
    path.write_text(render_page(fm, body), encoding="utf-8")
    return True


def increment_page_field(path: Path, field: str, by: int = 1) -> bool:
    """Atomically increment an integer frontmatter field, preserving the body.

    No-op (returns False) when the file has no valid frontmatter block.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    fm, body, has_fm = split_frontmatter(text)
    if not has_fm:
        return False
    try:
        current = int(fm.get(field, 0) or 0)
    except (TypeError, ValueError):
        current = 0
    fm[field] = current + by
    path.write_text(render_page(fm, body), encoding="utf-8")
    return True
