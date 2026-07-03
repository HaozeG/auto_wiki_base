#!/usr/bin/env python3
"""
Linking-debt closure pass, mirroring the original research/riscv-ai-accelerator
run's manual "lint routine (linking debt pass N)" steps: for each orphan page
(inbound_links == 0), find the most topically-similar existing page (by shared
tags/structured_fields/canonical_name tokens) and add a reciprocal [[wikilink]]
Relationships bullet, bumping the target's inbound_links. This is the step the
autonomous research loop alone does not perform across sessions (linking_debt
in research_state.py only tracks pages created *within one session*), so
orphans accumulate across sessions until this kind of pass runs.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, "tools")
import frontmatter  # noqa: E402

PAGES_DIR = Path("wiki/_pages")


def tokens_for(fm: dict) -> set[str]:
    toks = set()
    for field in ("tags", "hardware_targets", "workloads", "toolchains", "datatypes"):
        for v in fm.get(field) or []:
            toks.add(str(v).strip().lower())
    name = str(fm.get("canonical_name") or "")
    toks.update(w.lower() for w in re.findall(r"[A-Za-z0-9]+", name) if len(w) > 2)
    return toks


def main():
    pages = [p for p in PAGES_DIR.rglob("*.md")]
    records = []
    for p in pages:
        fm, body = frontmatter.parse_page(p)
        if fm.get("type") == "synthesis":
            continue
        records.append((p, fm, body, tokens_for(fm)))

    linked = 0
    for p, fm, body, toks in records:
        if int(fm.get("inbound_links", 0) or 0) > 0:
            continue
        best = None
        best_score = 0
        for p2, fm2, _, toks2 in records:
            if p2 == p:
                continue
            shared = toks & toks2
            if len(shared) > best_score:
                best_score = len(shared)
                best = (p2, fm2, shared)
        if best is None or best_score == 0:
            print(f"SKIP (no similar page found): {p.stem}")
            continue
        target_path, target_fm, shared = best
        reason = ", ".join(sorted(shared))[:80]
        bullet = f"- [[{p.stem}]]: related via shared {reason}.\n"
        # Add reciprocal link in the target page's Relationships section (or append one).
        target_fm2, target_body = frontmatter.parse_page(target_path)
        if "## Relationships" in target_body:
            new_body = target_body.replace(
                "## Relationships\n", f"## Relationships\n\n{bullet}", 1
            )
        else:
            new_body = target_body.rstrip() + f"\n\n## Relationships\n\n{bullet}\n"
        frontmatter.write_page(target_path, target_fm2, new_body)
        # target now links to p, so p (the orphan) gains the inbound link.
        frontmatter.increment_page_field(p, "inbound_links")
        print(f"LINKED: {target_path.stem} -> {p.stem} (shared: {reason})")
        linked += 1

    print(f"\nTotal orphans linked: {linked}")


if __name__ == "__main__":
    main()
