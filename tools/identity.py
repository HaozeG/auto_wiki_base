"""Concept identity resolution for write-time duplicate prevention.

Duplicate pages historically slipped through because dedup keyed on filename,
folder, and title — the three things that differ between ``entity/Gemmini`` and
``hardware_target/Gemmini_Architecture``. Identity resolution keys instead on a
normalized ``canonical_name`` (plus aliases) that is independent of all three.

The normalizer folds vendor/family/boilerplate tokens (reusing qmd_runner's
token sets) but *preserves model/version discriminators*, so:
    Gemmini            == Gemmini Architecture        (merge)
    MLIR               == MLIR (software)             (merge)
    XuanTie C908       != XuanTie C910                (distinct — digit tokens)
    MLPerf Inference   != MLPerf Tiny                 (distinct — "tiny" kept)

The orchestrator's write gate is the authoritative enforcement point: it calls
``resolve`` on the eval subagent's returned ``canonical_name`` and hard-blocks a
``create`` that collides with an existing page. The subagent's own
``identity_action`` is advisory only.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from qmd_runner import _duplicate_tokens, _tokens, normalize_title_subject


def normalize_canonical(name: str, aliases: list[str] | None = None) -> str:
    """Return the normalized identity key for a concept name.

    Folds vendor/family/boilerplate tokens but keeps version/model
    discriminators. Returns "" only for an empty input.
    """
    base = normalize_title_subject(name or "")
    toks = _duplicate_tokens(base)
    if not toks:
        # Name was entirely generic/boilerplate (e.g. "Vector Extension");
        # fall back to keeping those tokens so we still produce a stable key.
        toks = _tokens(base)
    if not toks:
        return re.sub(r"\s+", " ", (name or "").strip().lower())
    return " ".join(sorted(set(toks)))


@dataclass(frozen=True)
class PageRef:
    canonical_name: str
    filename: str
    path: Path


def _page_identity(fm: dict, path: Path) -> tuple[str, list[str]]:
    """Best-effort (canonical_name, aliases) for a page.

    Falls back to the page stem when ``canonical_name`` is absent, so identity
    resolution still works on wikis not yet backfilled (see backfill_identity)."""
    canonical = str(fm.get("canonical_name") or "").strip()
    if not canonical:
        canonical = path.stem.replace("_", " ")
    aliases = fm.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = [str(aliases)]
    return canonical, [str(a) for a in aliases]


def build_registry(pages_dir: Path) -> dict[str, PageRef]:
    """Build an in-memory identity registry from page frontmatter.

    Maps the normalized canonical_name AND every normalized alias to the page.
    Frontmatter is the source of truth; index.md's Concept Index is a projection.
    """
    registry: dict[str, PageRef] = {}
    if not pages_dir.exists():
        return registry
    for path in pages_dir.rglob("*.md"):
        fm, _ = frontmatter.parse_page(path)
        canonical, aliases = _page_identity(fm, path)
        ref = PageRef(canonical_name=canonical, filename=path.name, path=path)
        for surface in [canonical, *aliases]:
            key = normalize_canonical(surface)
            if key:
                registry.setdefault(key, ref)
    return registry


def resolve(canonical_name: str, registry: dict[str, PageRef],
            aliases: list[str] | None = None) -> tuple[str, PageRef | None]:
    """Resolve a concept to ``("create", None)`` or ``("upsert", PageRef)``.

    Checks the canonical name first, then any provided aliases (a known concept
    arriving under a new surface form).
    """
    key = normalize_canonical(canonical_name)
    if key and key in registry:
        return "upsert", registry[key]
    for alias in aliases or []:
        akey = normalize_canonical(alias)
        if akey and akey in registry:
            return "upsert", registry[akey]
    return "create", None


def register(registry: dict[str, PageRef], canonical_name: str, filename: str,
             path: Path, aliases: list[str] | None = None) -> None:
    """Add a newly created page's identity to a live registry (so later
    candidates in the same session collide with it)."""
    ref = PageRef(canonical_name=canonical_name, filename=filename, path=path)
    for surface in [canonical_name, *(aliases or [])]:
        key = normalize_canonical(surface)
        if key:
            registry.setdefault(key, ref)
