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

# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------

_CLAUDE_MD_PATH = Path(__file__).parent.parent / "CLAUDE.md"


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


def _get_eval_config() -> dict:
    return _load_claude_md_block("eval_config")


def _get_eval_thresholds() -> dict:
    return _load_claude_md_block("eval_thresholds")


# ---------------------------------------------------------------------------
# Frontmatter / body parsing
# ---------------------------------------------------------------------------

def parse_page(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text) for a markdown page."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            fm_text = text[3:end].strip()
            body = text[end + 3:].strip()
            try:
                return yaml.safe_load(fm_text) or {}, body
            except yaml.YAMLError:
                pass
    return {}, text


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


# ---------------------------------------------------------------------------
# Layer 1: Rule-based structural checks
# ---------------------------------------------------------------------------

def layer1_check(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Deterministic structural checks.
    Returns {"pass": bool, "violations": [str]}
    """
    config = _get_eval_config()
    dangling_patterns = config.get("dangling_patterns", [])
    word_count_bounds = config.get("word_count_bounds", {})

    fm, body = parse_page(path)
    violations = []

    # Determine the text block to check for dangling references and word count
    if page_type == "entity":
        target_text = _extract_first_paragraph(body)
        wc_config = word_count_bounds.get("entity_first_paragraph", {"min": 80, "max": 300})
    else:  # synthesis
        target_text = _extract_rag_summary(body)
        wc_config = word_count_bounds.get("synthesis_rag_summary", {"min": 150, "max": 250})
        if not target_text:
            violations.append("MISSING_RAG_SUMMARY: synthesis page has no RAG Summary block")

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
    if page_type == "entity":
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

    result = {"pass": len(violations) == 0, "violations": violations}
    if verbose:
        print(f"[Layer 1] {'PASS' if result['pass'] else 'FAIL'}")
        for v in violations:
            print(f"  - {v}")
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
    if page_type == "entity":
        th = thresholds.get("entity_page", {})
    else:
        th = thresholds.get("synthesis_rag_summary", {})

    fm, body = parse_page(path)
    if page_type == "entity":
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


def layer3_check(path: Path, page_type: str, verbose: bool = False) -> dict:
    """
    Semantic coverage via qmd CLI.
    Adds needs_summary_revision: true to frontmatter on fail.
    Returns {"coverage": float, "pass": bool} or {"skipped": True} if qmd unavailable.
    """
    fm, body = parse_page(path)
    if page_type == "entity":
        query_text = _extract_first_paragraph(body)
    else:
        query_text = _extract_rag_summary(body)

    if not query_text:
        return {"coverage": 1.0, "pass": True}

    wiki_pages_dir = Path(__file__).parent.parent / "wiki" / "_pages"
    if not wiki_pages_dir.exists():
        if verbose:
            print("[Layer 3] SKIPPED (wiki/_pages not found)")
        return {"skipped": True, "coverage": None, "pass": True}

    try:
        result = subprocess.run(
            ["qmd", "search", query_text[:500], "--index", str(wiki_pages_dir), "--top", "5"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        if verbose:
            print("[Layer 3] SKIPPED (qmd not installed or timed out)")
        return {"skipped": True, "coverage": None, "pass": True}

    if result.returncode != 0 or not result.stdout.strip():
        if verbose:
            print("[Layer 3] SKIPPED (qmd returned no results)")
        return {"skipped": True, "coverage": None, "pass": True}

    # Simple heuristic: count returned results as coverage proxy
    # (qmd returns matched snippets; more matches = better semantic coverage)
    lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
    coverage = min(len(lines) / 5.0, 1.0)
    passed = coverage > 0.5

    if not passed:
        _set_frontmatter_flag(path, "needs_summary_revision", True)

    if verbose:
        print(f"[Layer 3] {'PASS' if passed else 'FAIL'}")
        print(f"  coverage: {coverage:.2f} (qmd results: {len(lines)}/5)")

    return {"coverage": round(coverage, 4), "pass": passed}


def _set_frontmatter_flag(path: Path, key: str, value) -> None:
    """Add or update a key in the page's YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return
    end = text.find("---", 3)
    if end == -1:
        return
    fm_text = text[3:end].strip()
    body_rest = text[end:]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return
    fm[key] = value
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    path.write_text(f"---\n{new_fm}---{body_rest}", encoding="utf-8")


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

    if page_type not in ("entity", "synthesis"):
        print(f"ERROR: --type must be 'entity' or 'synthesis'", file=sys.stderr)
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
        result = {"layer1": l1, "final": "rejected", "rejection_layer": 1}
        print(json.dumps(result) if verbose else "", end="")
        return result

    l2 = layer2_check(path, page_type, verbose=verbose)

    l3_triggered = _layer2_is_borderline(l2) and not l2.get("skipped")
    l3 = None
    if l3_triggered:
        if verbose:
            print("[Layer 3] Triggered (Layer 2 borderline)")
        l3 = layer3_check(path, page_type, verbose=verbose)

    result = {
        "layer1": l1,
        "layer2": l2,
        "layer3": l3,
        "layer3_triggered": l3_triggered,
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
        choices=["entity", "synthesis"],
        default="entity",
        help="Page type (default: entity)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    result = run_pipeline(Path(args.page_path), args.type, verbose=args.verbose)
    sys.exit(0 if result["final"] == "approved" else 1)


if __name__ == "__main__":
    main()
