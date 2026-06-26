# Retrospective Lint Report — 2026-06-26

## Pre-Lint Fix Applied

**5 entity pages had malformed YAML frontmatter** — the closing `---` delimiter was written with excess dashes (e.g., `------`, `---------------------`, `---------------------------`). This caused `eval_summary.py` to report `WORD_COUNT_LOW: 1 words` (the residual dashes were parsed as the first paragraph). Fixed before scoring:

- `entity/fpga_riscv_isa_extension_nn_inference.md` (`---------------------------` → `---`)
- `entity/risc_v_vector_extension.md` (`---------------------` → `---`)
- `entity/rva23_profile.md` (`------` → `---`)
- `entity/sifive_intelligence_x280.md` (`------------` → `---`)
- `entity/tenstorrent_blackhole.md` (`------` → `---`)

**Note:** Layer 2 eval (entity/compression density) was skipped on all 10 pages — spaCy model `en_core_web_sm` is not installed. Layer 1 (word count, dangling reference patterns) passed for all pages.

---

## Cleared (9 pages)

All pages listed below pass Layer 1 eval; `cold_start` set to `false`.

| Page | inbound_links | Scorecard state | Notes |
|------|--------------|-----------------|-------|
| `entity/fpga_riscv_isa_extension_nn_inference.md` | 7 | null (scores not yet assigned) | High inbound — well-connected |
| `entity/gemmini.md` | 0 | null | **Orphan** — see below |
| `entity/risc_v_vector_extension.md` | 7 | null | High inbound hub |
| `entity/rva23_profile.md` | 3 | null | |
| `entity/sifive_intelligence_x280.md` | 5 | null | |
| `entity/tenstorrent_automotive_ai_accelerator.md` | 0 | bridge: 0.8, hub: 0.8, novelty: 0.9 | **Orphan** — see below |
| `entity/tenstorrent_blackhole.md` | 3 | bridge: 0.7, hub: 0.5, novelty: 0.8 | |
| `entity/tenstorrent.md` | 0 | bridge: 0.8, hub: 0.7, novelty: 0.9 | **Orphan** — see below |
| `synthesis/riscv_ai_accelerator_landscape.md` | 0 | `~` (unscored) | **Orphan** — see below |

---

## Restructure Candidates

- `entity/intel_itanium.md`: The page's primary claim is comparative-synthetic — Itanium's EPIC ideas are "rediscovered" in NVIDIA GPUs, Google TPU, and RISC-V vector/matrix extensions. This is synthesis content typed as an entity. Also has 0 inbound links.
  - Proposed synthesis title: *"EPIC/VLIW Principles in Modern AI Accelerators: Itanium's Architectural Legacy"*
  - Proposed entity stub: short entity page retaining factual Itanium claims (dates, ISA features, market outcome); synthesis page covering the modern parallels.
  - **Not auto-executed — awaiting `lint apply`.**

---

## Merge Candidates

None identified.

---

## Delete Candidates

None identified.

---

## Deferred for Human Decision

### Orphan Pages (5)

The following pages have `inbound_links: 0` — no other page currently links to them. Per mature-graph lint rules, these should be cross-linked or reviewed.

1. **`entity/gemmini.md`** — describes Google/UC Berkeley's systolic-array RISC-V accelerator. The synthesis page does not include it as a connected entity, and no entity page links to it.
   - Suggested fix: add `[[gemmini]]` to `synthesis/riscv_ai_accelerator_landscape.md` under Connected Pages, and update its `connected_entities` list.

2. **`entity/tenstorrent.md`** — parent company entity. `tenstorrent_blackhole.md` and `tenstorrent_automotive_ai_accelerator.md` both represent Tenstorrent products but neither links back to this page.
   - Suggested fix: add `[[tenstorrent]]` to both product pages' Relationships section; update `tenstorrent.md` inbound_links to 2.

3. **`entity/tenstorrent_automotive_ai_accelerator.md`** — no page links to it; not included in synthesis page connected entities despite being topically relevant.
   - Suggested fix: add to synthesis page's connected entities and Connected Pages block.

4. **`entity/intel_itanium.md`** — 0 inbound links; also a Restructure candidate (see above).

5. **`synthesis/riscv_ai_accelerator_landscape.md`** — synthesis pages are retrieval targets, not link targets, so 0 inbound links is expected. No action required unless entity pages should explicitly link to it.

### Null Scorecards (5 entity pages)

Pages ingested via research harness without explicit scorecard values: `fpga_riscv_isa_extension_nn_inference`, `gemmini`, `risc_v_vector_extension`, `rva23_profile`, `sifive_intelligence_x280`. Scores remain `null`. If Layer 2 eval is needed, install spaCy: `python3 -m spacy download en_core_web_sm`.

### Graph Stats Discrepancy

`graph_stats.py` reports `pages_with_inbound_links: 10` (all pages) while 5 pages have `inbound_links: 0` in frontmatter. Likely explanation: `graph_stats.py` scans for `[[wikilink]]` occurrences across the corpus rather than reading the frontmatter `inbound_links` counter — these are out of sync. The frontmatter counter is canonical per CLAUDE.md.

---

## Summary

| Category | Count |
|----------|-------|
| Cleared | 9 |
| Restructure candidates | 1 (`intel_itanium.md`) |
| Merge candidates | 0 |
| Delete candidates | 0 |
| Deferred (orphan/scorecard) | 5 items |
| Pre-lint structural fixes | 5 (frontmatter delimiters) |
| **Total pages evaluated** | **10** |
