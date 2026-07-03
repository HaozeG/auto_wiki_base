"""Extract structured, reasoned outbound-link edges from a page's Relationships
(or Connected Pages, for synthesis) section.

Implements the "every link should carry a reason, kept alongside the edge, so
it is searchable and analyzable" requirement in CLAUDE.md's Graph Topology
Philosophy. Edges are read from body markdown (the existing authoring surface —
"[[target]]: reason." bullets already match this shape in every page template
and in prior linking passes like close_linking_debt.py) and written back into
frontmatter as ``outbound_links: [{target, reason}, ...]``, so frontmatter stays
the source of truth for graph structure per the existing Constraints section,
while the body stays plain Obsidian-compatible ``[[page]]`` markup.

Only lines inside the Relationships/Connected Pages section are treated as
edges — an inline ``[[mention]]`` elsewhere in prose (e.g. a synthesis RAG
Summary discussing an entity) is not, so this stays a precise edge list rather
than every page name that happens to appear in the text.
"""

from __future__ import annotations

import re

_SECTION_RE = re.compile(r"^##\s+(Relationships|Connected Pages)\s*$", re.MULTILINE)
_HEADING_RE = re.compile(r"^##\s+", re.MULTILINE)
_LINK_LINE_RE = re.compile(r"^-\s*\[\[([^\]]+)\]\](?:\s*:\s*(.+))?$")


def extract_outbound_links(body: str) -> list[dict]:
    """Parse ``[[target]]: reason.`` bullets out of a page's Relationships /
    Connected Pages section. Returns ``[]`` if the section is absent or has no
    link-shaped bullets. Order-preserving, de-duplicated by target."""
    match = _SECTION_RE.search(body)
    if not match:
        return []
    start = match.end()
    next_heading = _HEADING_RE.search(body, start)
    section_text = body[start:next_heading.start()] if next_heading else body[start:]

    links: list[dict] = []
    seen: set[str] = set()
    for line in section_text.splitlines():
        m = _LINK_LINE_RE.match(line.strip())
        if not m:
            continue
        target = m.group(1).strip()
        if not target or target in seen:
            continue
        seen.add(target)
        reason = (m.group(2) or "").strip().rstrip(".") or "unlabeled"
        links.append({"target": target, "reason": reason})
    return links
