#!/usr/bin/env python3
"""
Three-layer evaluation pipeline for wiki pages.

Layer 1: Deterministic rule-based checks (dangling references, word counts).
Layer 2: Density metrics via spaCy (entity density, measurement density, compression ratio).
Layer 3: Semantic coverage via qmd (conditionally triggered when Layer 2 is borderline).

Usage:
    python tools/eval_summary.py <page_path> [--type entity|synthesis] [--verbose]

Exit codes:
    0 — pass
    1 — fail (hard rejection)
"""

import argparse
import gzip
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

import frontmatter
import identity
from domain_analysis import validate_benchmark_claim
from qmd_runner import _duplicate_tokens

# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------

_CLAUDE_MD_PATH = Path(__file__).parent.parent / "CLAUDE.md"
_WIKI_PAGES_DIR = Path(__file__).parent.parent / "wiki" / "_pages"
# Canonical types plus a couple of harness-internal kinds (source_note,
# benchmark_result triggers the measurement-field check in layer1_check)
# that aren't necessarily declared as theme subtypes.
_BASE_PAGE_TYPES = {"entity", "synthesis", "source_note", "benchmark_result"}


def _load_claude_md_block(block_name: str) -> dict:
    """Extract a named YAML block from CLAUDE.md."""
    text = _CLAUDE_MD_PATH.read_text(encoding="utf-8")
    pattern = rf"```yaml\n\[{re.escape(block_name)}\](.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _page_types() -> set[str]:
    """Base kinds plus whatever subtypes the active [theme_profile] declares.

    The wiki is domain-agnostic (CLAUDE.md, "Theme Setup"): subtype names
    like `hardware_target` or `ai_accelerator_architecture` are chosen per
    theme by the profile-architect subagent, not fixed in code, so the
    allowed --type values must be read from the live theme profile rather
    than hardcoded to one theme's subtype names.
    """
    profile = _load_claude_md_block("theme_profile")
    subtypes = set((profile.get("page_types") or {}).keys())
    return _BASE_PAGE_TYPES | subtypes


_PAGE_TYPES = _page_types()


def _get_eval_config() -> dict:
    return _load_claude_md_block("eval_config")


def _get_eval_thresholds() -> dict:
    return _load_claude_md_block("eval_thresholds")


# ---------------------------------------------------------------------------
# Frontmatter / body parsing
# ---------------------------------------------------------------------------

def parse_page(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text) for a markdown page."""
    fm, body = frontmatter.parse_page(path)
    return fm, body.strip()


def _extract_first_paragraph(body: str) -> str:
    """Return the first non-empty paragraph from the body (after the h1 title)."""
    lines = body.split("\n")
    in_paragraph = False
    para_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped == "":
            if in_paragraph:
                break
            continue
        in_paragraph = True
        para_lines.append(stripped)
    return " ".join(para_lines)


def _extract_rag_summary(body: str) -> str:
    """Return the content of the RAG Summary block from a synthesis page."""
    match = re.search(
        r"## RAG Summary\s*(?:<!--.*?-->)?\s*(.*?)(?:\n---|\n## |\Z)",
        body,
        re.DOTALL,
    )
    if not match:
        return ""
    content = match.group(1).strip()
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL).strip()
    return content


def _find_page_by_stem_or_alias(ref: str) -> identity.PageRef | None:
    """Look up a connected_entities/outbound_links reference (usually a page
    filename stem) against the live wiki, returning its PageRef (with the
    real canonical_name) or None if it doesn't resolve to anything."""
    ref = (ref or "").strip()
    if not ref:
        return None
    for p in _WIKI_PAGES_DIR.rglob("*.md"):
        if p.stem == ref:
            fm, _ = frontmatter.parse_page(p)
            return identity.PageRef(
                canonical_name=str(fm.get("canonical_name") or p.stem),
                filename=p.name,
                path=p,
            )
    return None


def _name_mentioned(name: str, text: str) -> bool:
    """Fuzzy check: does at least half (min 1) of ``name``'s significant
    tokens appear as whole words in ``text``? Token-overlap rather than an
    exact-substring match so ordinary prose paraphrasing of a name doesn't
    count as a miss — only a genuine omission does."""
    toks = [t for t in _duplicate_tokens(name) if len(t) >= 4]
    if not toks:
        return False
    text_lower = text.lower()
    hits = sum(1 for t in toks if re.search(rf"\b{re.escape(t)}", text_lower))
    return hits >= max(1, len(toks) // 2)


def _find_dangling_outbound_links(fm: dict) -> list[str]:
    """Return outbound_links[].target values that don't resolve to any known
    page's canonical_name/alias/filename stem in the live wiki registry.

    Soft signal, not a hard rejection: a page in a multi-draft batch may
    legitimately reference a sibling draft that hasn't been written to disk
    yet (see orchestrator.py's approved_drafts loop, which runs this pipeline
    per-draft before any of them are written), which would otherwise look
    like a false-positive dangling link. Found live during the v6 freeform
    replication test: a page linked ``[[gap9]]`` in both its body and
    outbound_links, but the real page is ``greenwaves-gap9`` — no page named
    "gap9" exists anywhere in the wiki, and nothing caught it.

    Deliberately checks exact filename-stem match only, the same resolution
    ``graph_topology.py::build_graph`` actually uses to turn outbound_links
    into graph edges — not identity.py's alias-aware ``resolve()``. "gap9" is
    a registered *alias* of greenwaves-gap9.md, so an alias-aware check
    would call it resolved even though Obsidian and graph_topology.py both
    treat it as a broken link (neither follows frontmatter aliases when
    resolving ``[[wikilinks]]``/outbound_links targets)."""
    if not _WIKI_PAGES_DIR.exists():
        return []
    stems = {p.stem for p in _WIKI_PAGES_DIR.rglob("*.md")}
    dangling = []
    for link in fm.get("outbound_links") or []:
        if not isinstance(link, dict):
            continue
        target = str(link.get("target") or "").strip()
        if not target or target in stems:
            continue
        dangling.append(target)
    return dangling


# ---------------------------------------------------------------------------
# Layer 1: Rule-based structural checks
# ---------------------------------------------------------------------------

def layer1_check(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Deterministic structural checks.
    Returns {"pass": bool, "violations": [str], "soft_violations": [str]}
    """
    config = _get_eval_config()
    dangling_patterns = config.get("dangling_patterns", [])
    generic_reason_patterns = config.get("generic_relationship_reason_patterns", [])
    word_count_bounds = config.get("word_count_bounds", {})

    fm, body = parse_page(path)
    violations = []
    soft_violations = []

    # Hard rejection: a second, embedded frontmatter block surviving after the
    # real one (subagent echo that the write-time stripper failed to catch).
    # Detected structurally so malformed YAML inside the block can't hide it --
    # this is what let a corrupted embedded block coast through word-count/
    # entity-density checks by accident (its bulk read as a plausible "first
    # paragraph").
    _, _, _embedded_raw_block = frontmatter.strip_embedded_frontmatter_block(body)
    if _embedded_raw_block is not None:
        violations.append(
            "EMBEDDED_FRONTMATTER: body contains a second '---'-delimited block "
            "after the real frontmatter"
        )

    # Determine the text block to check for dangling references and word count
    if page_type != "synthesis":
        target_text = _extract_first_paragraph(body)
        wc_config = word_count_bounds.get("entity_first_paragraph", {"min": 80, "max": 300})
    else:  # synthesis
        target_text = _extract_rag_summary(body)
        wc_config = word_count_bounds.get("synthesis_rag_summary", {"min": 150, "max": 250})
        if not target_text:
            violations.append("MISSING_RAG_SUMMARY: synthesis page has no RAG Summary block")
        else:
            # Hard rejection (CLAUDE.md Synthesis Page spec): "Must name at
            # least 2 connected entities explicitly." Checked here because
            # validate_output.py only verifies the connected_entities
            # frontmatter *list* has >= 2 entries, never that they're
            # actually named in the RAG Summary text — a synthesis page
            # (kv-cache-optimization-strategies-survey.md) shipped live with
            # a RAG Summary that never mentioned any of its 3 connected
            # entities, uncaught, during the v6 freeform replication test.
            connected = fm.get("connected_entities") or []
            named = 0
            for entity in connected:
                ref = _find_page_by_stem_or_alias(str(entity))
                surfaces = [str(entity)]
                if ref is not None:
                    surfaces.append(ref.canonical_name)
                if any(_name_mentioned(surface, target_text) for surface in surfaces):
                    named += 1
            if named < 2:
                violations.append(
                    f"RAG_SUMMARY_MISSING_ENTITY_NAMES: only {named} of "
                    f"{len(connected)} connected_entities are named in the RAG "
                    f"Summary text (minimum 2 required)"
                )

    # Dangling reference check
    for pattern in dangling_patterns:
        if re.search(pattern, target_text, re.IGNORECASE):
            violations.append(f"DANGLING_REF: matched pattern '{pattern}' in target text")

    # Word count check
    if target_text:
        word_count = len(target_text.split())
        min_words = wc_config.get("min", 0)
        max_words = wc_config.get("max", float("inf"))
        if word_count < min_words:
            violations.append(
                f"WORD_COUNT_LOW: {word_count} words (min {min_words}) in target block"
            )
        elif word_count > max_words:
            violations.append(
                f"WORD_COUNT_HIGH: {word_count} words (max {max_words}) in target block"
            )

    # Hard rejection: sources list must be non-empty
    if not fm.get("sources"):
        violations.append("EMPTY_SOURCES: frontmatter 'sources' list is empty or missing")

    # Hard rejection: entity pages must have at least 3 independently verifiable claims
    if page_type != "synthesis":
        claims_match = re.search(r"## Key Claims\s*\n(.*?)(?:\n## |\Z)", body, re.DOTALL)
        if claims_match:
            claims_text = claims_match.group(1).strip()
            # Count non-empty bullet/numbered list items as individual claims
            claim_lines = [
                l.strip() for l in claims_text.splitlines()
                if re.match(r"^[-*\d]", l.strip()) and len(l.strip()) > 10
            ]
            if len(claim_lines) < 3:
                violations.append(
                    f"TOO_FEW_CLAIMS: only {len(claim_lines)} claim(s) found in ## Key Claims "
                    f"(minimum 3 required)"
                )
        else:
            violations.append("MISSING_KEY_CLAIMS: no '## Key Claims' section found")

    if page_type == "benchmark_result":
        research_config = _load_claude_md_block("research_config")
        benchmark_result = validate_benchmark_claim(fm, body, research_config)
        if not benchmark_result["pass"]:
            if benchmark_result["missing_fields"]:
                violations.append(
                    "BENCHMARK_CONTEXT_MISSING: "
                    + ", ".join(benchmark_result["missing_fields"])
                )
            if benchmark_result["invalid_evidence_strength"]:
                violations.append(
                    "BENCHMARK_EVIDENCE_STRENGTH_INVALID: "
                    + ", ".join(benchmark_result["invalid_evidence_strength"])
                )

    # Soft signal: internal links that don't resolve to any known page.
    dangling_links = _find_dangling_outbound_links(fm)
    if dangling_links:
        soft_violations.append(
            "DANGLING_LINK: outbound_links target(s) not found in the wiki: "
            + ", ".join(dangling_links)
        )

    # Soft signal: empty tags undercut the organic-clustering mechanism
    # (_synthesis_gap_clusters groups pages by tag) even though CLAUDE.md
    # doesn't list an empty tags list as a hard-rejection criterion.
    if not fm.get("tags"):
        soft_violations.append("EMPTY_TAGS: frontmatter 'tags' list is empty")

    # Soft signal: relationship reasons that read as generic tag/token
    # overlap rather than a deliberate bridge (Graph Topology Philosophy).
    generic_reasons = []
    for link in fm.get("outbound_links") or []:
        if not isinstance(link, dict):
            continue
        reason = str(link.get("reason") or "")
        if any(re.search(p, reason, re.IGNORECASE) for p in generic_reason_patterns):
            generic_reasons.append(f"{link.get('target', '?')}: '{reason}'")
    if generic_reasons:
        soft_violations.append(
            "GENERIC_RELATIONSHIP_REASON: " + "; ".join(generic_reasons)
        )

    result = {"pass": len(violations) == 0, "violations": violations, "soft_violations": soft_violations}
    if verbose:
        print(f"[Layer 1] {'PASS' if result['pass'] else 'FAIL'}")
        for v in violations:
            print(f"  - {v}")
        for v in soft_violations:
            print(f"  (soft) {v}")
    return result


# ---------------------------------------------------------------------------
# Layer 2: Density metrics (spaCy)
# ---------------------------------------------------------------------------

def entity_density(text: str, nlp) -> float:
    """Named entities per 100 tokens."""
    doc = nlp(text)
    return (len(doc.ents) / max(len(doc), 1)) * 100


def measurement_density(text: str) -> float:
    """Numeric measurements per 100 words."""
    pattern = r"\d+\.?\d*\s*(ms|GB|TB|TFLOPS|%|ns|MHz|GHz|dB|K|M|B|ops|cycles|tokens)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    words = len(text.split())
    return (len(matches) / max(words, 1)) * 100


def compression_ratio(text: str) -> float:
    """Lower = less redundant. Hard floor: > 0.6 suggests padding."""
    encoded = text.encode("utf-8")
    return len(gzip.compress(encoded)) / len(encoded)


def layer2_check(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Density metric checks using spaCy.
    Returns {"entity_density": float, "measurement_density": float, "compression_ratio": float, "pass": bool}
    Gracefully degrades if spaCy is not installed.
    """
    try:
        import spacy  # noqa: PLC0415
    except ImportError:
        if verbose:
            print("[Layer 2] SKIPPED (spaCy not installed)")
        return {"entity_density": None, "measurement_density": None, "compression_ratio": None, "pass": True, "skipped": True}

    config = _get_eval_config()
    spacy_model = config.get("spacy_model", "en_core_web_sm")
    try:
        nlp = spacy.load(spacy_model)
    except OSError:
        if verbose:
            print(f"[Layer 2] SKIPPED (spaCy model '{spacy_model}' not downloaded)")
        return {"entity_density": None, "measurement_density": None, "compression_ratio": None, "pass": True, "skipped": True}

    thresholds = _get_eval_thresholds()
    if page_type != "synthesis":
        th = thresholds.get("entity_page", {})
    else:
        th = thresholds.get("synthesis_rag_summary", {})

    fm, body = parse_page(path)
    if page_type != "synthesis":
        text = _extract_first_paragraph(body)
    else:
        text = _extract_rag_summary(body)

    ed = entity_density(text, nlp)
    md = measurement_density(text)
    cr = compression_ratio(text)

    ed_min = th.get("entity_density_min", 0.0)
    md_min = th.get("measurement_density_min", 0.0)
    cr_max = th.get("compression_ratio_max", 1.0)

    passed = (ed >= ed_min) and (md >= md_min) and (cr <= cr_max)

    result = {
        "entity_density": round(ed, 4),
        "measurement_density": round(md, 4),
        "compression_ratio": round(cr, 4),
        "pass": passed,
    }

    if verbose:
        print(f"[Layer 2] {'PASS' if passed else 'FAIL'}")
        print(f"  entity_density:      {ed:.4f} (min {ed_min})")
        print(f"  measurement_density: {md:.4f} (min {md_min})")
        print(f"  compression_ratio:   {cr:.4f} (max {cr_max})")

    return result


# ---------------------------------------------------------------------------
# Layer 3: Semantic coverage via qmd (conditionally triggered)
# ---------------------------------------------------------------------------

_BORDERLINE_MARGIN = 0.20  # within 20% of threshold triggers Layer 3


def _layer2_is_borderline(layer2_result: dict) -> bool:
    """Return True if any metric is within BORDERLINE_MARGIN of its threshold."""
    if layer2_result.get("skipped"):
        return False
    thresholds = _get_eval_thresholds()
    th = thresholds.get("entity_page", {})
    ed = layer2_result.get("entity_density")
    cr = layer2_result.get("compression_ratio")
    if ed is not None:
        ed_min = th.get("entity_density_min", 0.0)
        if ed_min > 0 and abs(ed - ed_min) / ed_min < _BORDERLINE_MARGIN:
            return True
    if cr is not None:
        cr_max = th.get("compression_ratio_max", 1.0)
        if abs(cr - cr_max) / cr_max < _BORDERLINE_MARGIN:
            return True
    return False


def _normalize_qmd_file(file_str: str) -> str:
    """Normalize a qmd result 'file' field to a page slug for comparison."""
    name = file_str.split("/")[-1]
    name = re.sub(r":\d+$", "", name)  # strip :line suffix (e.g. foo.md:27)
    return name.replace(".md", "").replace("-", "_")


def _extract_title(body: str) -> str:
    """Return the H1 title text from a page body, or empty string."""
    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def layer3_check(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Self-retrieval precision check via qmd CLI.

    A page passes if it appears in the top-5 results when queried by its own
    H1 title (self-retrieval precision). The title is used because qmd BM25
    silently returns empty results for queries over ~260 characters, making
    first-paragraph queries unreliable. Saturation (how many competitors appear
    in the top-5) is reported as an informational merge-candidate signal only;
    it does not block approval.

    Sets needs_summary_revision in frontmatter: True on fail, False on pass.
    Returns {"self_retrieved": bool, "saturation": float, "saturated": bool,
             "competitors": [str], "pass": bool} or {"skipped": True} if qmd unavailable.
    """
    _, body = parse_page(path)
    query_text = _extract_title(body)

    if not query_text:
        return {"self_retrieved": True, "saturation": 0.0, "saturated": False,
                "competitors": [], "pass": True}

    # Default harness path is BM25-only: vector/query paths require embeddings
    # and local model setup that may not exist in the current qmd environment.
    def _run_qmd_search() -> list | None:
        try:
            r = subprocess.run(
                ["uv", "run", "--no-sync", "qmd", "search", query_text, "-c", "_pages", "-n", "5", "--format", "json"],
                capture_output=True, text=True, timeout=30,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return None  # qmd unavailable
        if r.returncode != 0 or not r.stdout.strip():
            return []
        try:
            parsed = json.loads(r.stdout)
            return parsed if isinstance(parsed, list) else parsed.get("results", [])
        except json.JSONDecodeError:
            return []

    results = _run_qmd_search()
    search_mode = "search(bm25)"
    if results is None:
        if verbose:
            print("[Layer 3] SKIPPED (qmd not installed or timed out)")
        return {"skipped": True, "pass": True}

    slug = path.stem
    top_k = [_normalize_qmd_file(r.get("file", "")) for r in results[:5]]
    self_retrieved = slug in top_k
    competitors = [f for f in top_k if f != slug]
    saturation = len(competitors) / max(len(top_k), 1)

    research_config = _load_claude_md_block("research_config")
    sat_threshold = research_config.get("topic_saturation_hit_threshold", 4)
    saturated = len(competitors) >= sat_threshold

    passed = self_retrieved
    _set_frontmatter_flag(path, "needs_summary_revision", not passed)

    if verbose:
        print(f"[Layer 3] {'PASS' if passed else 'FAIL'} (mode={search_mode})")
        print(f"  self_retrieved: {self_retrieved} (slug='{slug}' in top-{len(top_k)})")
        print(f"  saturation: {saturation:.2f} ({len(competitors)} competitors in top-5)")
        if saturated:
            print(f"  WARNING: topic saturated ({len(competitors)}>={sat_threshold}) — merge candidate")

    return {
        "self_retrieved": self_retrieved,
        "saturation": round(saturation, 4),
        "saturated": saturated,
        "competitors": competitors,
        "search_mode": search_mode,
        "pass": passed,
    }


def _set_frontmatter_flag(path: Path, key: str, value) -> None:
    """Add or update a key in the page's YAML frontmatter (atomic round-trip)."""
    frontmatter.set_page_field(path, key, value)


# ---------------------------------------------------------------------------
# Pipeline entry point
# ---------------------------------------------------------------------------

def run_pipeline(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Run all three layers. Returns combined result dict.
    Exits with code 1 if Layer 1 fails (hard rejection).
    Layer 3 never causes hard rejection.
    """
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    if page_type not in _PAGE_TYPES:
        print(f"ERROR: --type must be one of {sorted(_PAGE_TYPES)}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Evaluating: {path} (type={page_type})")
        print("-" * 60)

    l1 = layer1_check(path, page_type, verbose=verbose)
    if not l1["pass"]:
        if not verbose:
            print(f"FAIL [Layer 1]: {path}")
            for v in l1["violations"]:
                print(f"  {v}")
            for v in l1.get("soft_violations", []):
                print(f"  (soft) {v}")
        result = {"layer1": l1, "final": "rejected", "rejection_layer": 1}
        print(json.dumps(result) if verbose else "", end="")
        return result

    if not verbose and l1.get("soft_violations"):
        print(f"PASS [Layer 1] with soft warnings: {path}")
        for v in l1["soft_violations"]:
            print(f"  (soft) {v}")

    l2 = layer2_check(path, page_type, verbose=verbose)
    l3 = layer3_check(path, page_type, verbose=verbose)

    result = {
        "layer1": l1,
        "layer2": l2,
        "layer3": l3,
        "final": "approved",
    }

    if verbose:
        print("-" * 60)
        print(f"RESULT: {result['final'].upper()}")
        print(json.dumps(result, indent=2))

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a wiki page through the three-layer pipeline."
    )
    parser.add_argument("page_path", help="Path to the markdown page to evaluate")
    parser.add_argument(
        "--type",
        choices=sorted(_PAGE_TYPES),
        default="entity",
        help="Page type (default: entity)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    result = run_pipeline(Path(args.page_path), args.type, verbose=args.verbose)
    sys.exit(0 if result["final"] == "approved" else 1)


if __name__ == "__main__":
    main()
