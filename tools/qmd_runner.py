"""QMD runner and similarity-gate helpers for the research harness."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


_PROJECT_ROOT = Path(__file__).parent.parent
_DEFAULT_QMD_COMMAND = ["uv", "run", "--no-sync", "qmd"]
_DEFAULT_STOP_WORDS = {
    "the", "a", "an", "of", "for", "in", "and", "on", "with", "by", "to", "is",
    "new", "official", "review", "benchmark", "overview", "launch", "announced",
}
_TITLE_BOILERPLATE_WORDS = {
    "documentation", "docs", "doc", "guide", "user", "manual", "reference",
    "getting", "started", "installing", "installation", "tutorial", "deepwiki",
    "gitfind", "score", "machine", "learning",
}
_GENERIC_FAMILY_TOKENS = {
    "risc", "riscv", "rvv", "ai", "ml", "cpu", "gpu", "npu", "soc", "chip",
    "core", "cores", "processor", "processors", "accelerator", "accelerators",
    "extension", "vector", "open", "source", "server", "edge", "board", "platform", "architecture", "system",
    "hardware", "software", "benchmark", "inference", "llm",
}


@dataclass
class QmdMatch:
    rank: int
    file: str
    title: str | None = None
    score: float | None = None
    snippet: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class QmdSearchResult:
    ok: bool
    matches: list[QmdMatch]
    error: str | None = None

    @property
    def blocked(self) -> bool:
        return not self.ok


class QmdRunner:
    """Small wrapper around the supported qmd CLI path."""

    def __init__(
        self,
        command: list[str] | str | None = None,
        cwd: Path | str = _PROJECT_ROOT,
        timeout: int = 30,
    ) -> None:
        self.command = normalize_qmd_command(command)
        self.cwd = Path(cwd)
        self.timeout = timeout

    def _ensure_collection_points_here(self, name: str = "_pages") -> None:
        """qmd collections are a single global, name-keyed registry (stored in
        ~/.cache/qmd/index.sqlite), not scoped per git worktree or cwd — `qmd
        update` and `qmd search -c _pages` silently operate on whatever
        absolute directory "_pages" was last pointed at, which may belong to
        a different worktree/branch entirely (found live: after running
        research in one worktree, "_pages" still pointed at a different
        worktree's wiki/_pages, so duplicate/saturation checks were silently
        comparing new candidates against the wrong branch's pages instead of
        this project's own). Re-point the collection to this project's own
        wiki/_pages before every update, so results never depend on which
        worktree last touched qmd."""
        expected = str((self.cwd / "wiki" / "_pages").resolve())
        try:
            show = subprocess.run(
                [*self.command, "collection", "show", name],
                capture_output=True,
                text=True,
                cwd=str(self.cwd),
                timeout=self.timeout,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return  # let update() surface the real error
        current_path = None
        if show.returncode == 0:
            match = re.search(r"Path:\s*(\S+)", show.stdout)
            if match:
                current_path = match.group(1).strip()
        if current_path == expected:
            return
        if current_path is not None:
            subprocess.run(
                [*self.command, "collection", "remove", name],
                capture_output=True, text=True, cwd=str(self.cwd), timeout=self.timeout,
            )
        subprocess.run(
            [*self.command, "collection", "add", expected, "--name", name],
            capture_output=True, text=True, cwd=str(self.cwd), timeout=self.timeout,
        )

    def update(self) -> tuple[bool, str | None]:
        self._ensure_collection_points_here()
        try:
            result = subprocess.run(
                [*self.command, "update"],
                capture_output=True,
                text=True,
                cwd=str(self.cwd),
                timeout=self.timeout,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
            return False, str(exc)
        if result.returncode != 0:
            return False, (result.stderr or result.stdout or "qmd update failed").strip()
        return True, None

    def search(self, query_text: str, top: int = 10, collection: str = "_pages") -> QmdSearchResult:
        safe_query = query_text[:500].replace("\x00", "").strip()
        if not safe_query:
            return QmdSearchResult(ok=True, matches=[])
        try:
            result = subprocess.run(
                [
                    *self.command,
                    "search",
                    safe_query,
                    "-c",
                    collection,
                    "-n",
                    str(top),
                    "--format",
                    "json",
                ],
                capture_output=True,
                text=True,
                cwd=str(self.cwd),
                timeout=self.timeout,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
            return QmdSearchResult(ok=False, matches=[], error=str(exc))

        if result.returncode != 0:
            return QmdSearchResult(
                ok=False,
                matches=[],
                error=(result.stderr or result.stdout or "qmd search failed").strip(),
            )
        if not result.stdout.strip():
            return QmdSearchResult(ok=True, matches=[])
        try:
            parsed = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            return QmdSearchResult(ok=False, matches=[], error=f"invalid qmd json: {exc}")
        records = parsed.get("results", []) if isinstance(parsed, dict) else parsed
        if not isinstance(records, list):
            return QmdSearchResult(ok=False, matches=[], error="unexpected qmd json shape")

        matches = [_parse_match(rec, i + 1) for i, rec in enumerate(records) if isinstance(rec, dict)]
        return QmdSearchResult(ok=True, matches=[m for m in matches if m.file])


def normalize_qmd_command(command: list[str] | str | None) -> list[str]:
    if command is None:
        return list(_DEFAULT_QMD_COMMAND)
    if isinstance(command, list):
        return [str(part) for part in command]
    return [part for part in str(command).split() if part]


def _parse_match(rec: dict[str, Any], rank: int) -> QmdMatch:
    score = rec.get("score")
    try:
        score = float(score) if score is not None else None
    except (TypeError, ValueError):
        score = None
    # Found live: with no embeddings populated (the harness's deliberate default —
    # see CLAUDE.md Constraints), qmd search returns a real 0.0 for every query
    # except a near-exact title match, not a graded low-relevance score. A literal
    # 0.0 satisfies neither the `>= threshold` buckets nor the `is None` rank-only
    # fallback in assess_candidate_similarity, so genuinely-related-but-differently
    # -worded candidates silently skip every score-based duplicate signal. Treat
    # 0.0 as "score not meaningful" (same as None) so the rank/overlap fallback,
    # which manual verification confirmed still orders results correctly, applies.
    if score == 0.0:
        score = None
    return QmdMatch(
        rank=rank,
        file=str(rec.get("file") or rec.get("path") or ""),
        title=rec.get("title"),
        score=score,
        snippet=rec.get("snippet") or rec.get("body"),
    )


def candidate_similarity_query(candidate: dict) -> str:
    title = candidate.get("title", "") or ""
    snippet = candidate.get("snippet", "") or candidate.get("relevance_rationale", "") or ""
    return f"{title}\n{snippet[:300]}".strip()


def assess_candidate_similarity(candidate: dict, matches: list[QmdMatch], config: dict) -> dict:
    near_duplicate_score = float(config.get("near_duplicate_score", 0.90))
    topic_similarity_min_score = float(config.get("topic_similarity_min_score", 0.80))
    saturation_threshold = int(config.get("topic_saturation_hit_threshold", 2))
    title_overlap_threshold = float(config.get("title_overlap_threshold", 0.8))

    title = candidate.get("title", "") or ""
    match_dicts = [m.to_dict() for m in matches]
    scored_hits = [m for m in matches if m.score is not None and m.score >= topic_similarity_min_score]
    high_score_hits = [m for m in matches if m.score is not None and m.score >= near_duplicate_score]
    rank_only_hits = [m for m in matches if m.score is None]
    domain_stopwords = set(str(w).lower() for w in config.get("domain_stopwords", []) or [])
    stopwords = _DEFAULT_STOP_WORDS | domain_stopwords

    overlapping_hits = [
        m for m in matches
        if hard_title_duplicate_score(title, _match_label(m), stopwords=stopwords) >= title_overlap_threshold
    ]
    family_hits = [
        m for m in matches[:5]
        if m.score is not None and _same_product_family(title, _match_label(m), stopwords=stopwords)
    ]
    rank_only_name_hits = [
        m for m in rank_only_hits[:3]
        if _rank_only_duplicate_signal(title, _match_label(m), stopwords=stopwords)
    ]

    reason = None
    merge_hint = None
    if high_score_hits and (overlapping_hits or family_hits or high_score_hits[0].rank == 1):
        reason = "near_duplicate_score"
    elif family_hits:
        reason = "same_product_family"
    elif len(scored_hits) >= saturation_threshold:
        merge_hint = "topic_saturation"
    elif rank_only_hits and (overlapping_hits or rank_only_name_hits):
        reason = "rank_only_duplicate_signal"

    return {
        "skip": reason is not None,
        "reason": reason,
        "merge_hint": merge_hint,
        "matches": match_dicts,
    }


def _match_label(match: QmdMatch) -> str:
    label = match.title or match.file
    label = label.split("/")[-1]
    label = re.sub(r":\d+$", "", label)
    label = label.removesuffix(".md")
    return label.replace("_", " ").replace("-", " ")


def normalize_title_subject(text: str) -> str:
    """
    Return the likely subject portion of a web title or page stem.

    Search titles often append site names or generic documentation words. The
    duplicate gate should compare concise subjects, not whole SERP titles.
    """
    text = text.replace("_", " ").replace("-", " ").strip()
    parts = [part.strip() for part in re.split(r"\s*[|—]\s*", text) if part.strip()]
    if parts:
        text = parts[0]
    text = re.split(r"\s+:\s+", text, maxsplit=1)[0].strip()
    return text


def _tokens(text: str, stopwords: set[str] | None = None) -> list[str]:
    stopwords = stopwords or _DEFAULT_STOP_WORDS
    stopwords = stopwords | _TITLE_BOILERPLATE_WORDS
    return [
        tok for tok in re.findall(r"[a-z0-9]+", text.lower().replace("risc-v", "riscv"))
        if tok not in stopwords
    ]


def _duplicate_tokens(text: str, stopwords: set[str] | None = None) -> list[str]:
    return [tok for tok in _tokens(text, stopwords=stopwords) if tok not in _GENERIC_FAMILY_TOKENS]


def _title_overlap(left: str, right: str, stopwords: set[str] | None = None) -> float:
    left_token_list = _duplicate_tokens(normalize_title_subject(left), stopwords=stopwords)
    right_token_list = _duplicate_tokens(normalize_title_subject(right), stopwords=stopwords)
    left_tokens = set(left_token_list)
    right_tokens = set(right_token_list)
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def hard_title_duplicate_score(left: str, right: str, stopwords: set[str] | None = None) -> float:
    """
    Score only hard title duplicates.

    The score deliberately avoids treating one shared vendor/family word as a
    duplicate. It still catches exact concise subjects and compact compound
    filenames such as "Milk-V Pioneer" vs "milkv_pioneer_duo".
    """
    left_token_list = _duplicate_tokens(normalize_title_subject(left), stopwords=stopwords)
    right_token_list = _duplicate_tokens(normalize_title_subject(right), stopwords=stopwords)
    left_tokens = set(left_token_list)
    right_tokens = set(right_token_list)
    if not left_tokens or not right_tokens:
        return 0.0
    if left_tokens == right_tokens:
        return 1.0

    shared = left_tokens & right_tokens
    if not shared:
        return 0.0

    union_score = len(shared) / len(left_tokens | right_tokens)
    left_coverage = len(shared) / len(left_tokens)
    right_coverage = len(shared) / len(right_tokens)

    left_compact = "".join(left_token_list)
    right_compact = "".join(right_token_list)
    compact_match = (
        len(left_tokens) >= 2
        and len(left_compact) >= 6
        and left_compact in right_compact
    )
    if compact_match:
        return 0.95

    if left_tokens <= right_tokens and len(left_tokens) >= 2:
        return max(union_score, left_coverage)
    if right_tokens <= left_tokens and len(right_tokens) >= 2 and left_coverage >= 0.9:
        return max(union_score, right_coverage)

    return union_score


def _family_tokens(text: str, stopwords: set[str] | None = None) -> set[str]:
    return {
        tok for tok in _tokens(text, stopwords=stopwords)
        if len(tok) >= 4 and tok not in _GENERIC_FAMILY_TOKENS
    }


def _same_product_family(left: str, right: str, stopwords: set[str] | None = None) -> bool:
    shared = _family_tokens(left, stopwords=stopwords) & _family_tokens(right, stopwords=stopwords)
    if not shared:
        return False
    left_has_model = any(re.search(r"[a-z]*\d+[a-z]*", tok) for tok in _tokens(left, stopwords=stopwords))
    right_has_model = any(re.search(r"[a-z]*\d+[a-z]*", tok) for tok in _tokens(right, stopwords=stopwords))
    return left_has_model or right_has_model or _title_overlap(left, right, stopwords=stopwords) >= 0.35


def _rank_only_duplicate_signal(left: str, right: str, stopwords: set[str] | None = None) -> bool:
    if hard_title_duplicate_score(left, right, stopwords=stopwords) >= 0.8:
        return True
    shared = _family_tokens(left, stopwords=stopwords) & _family_tokens(right, stopwords=stopwords)
    return len(shared) >= 2
