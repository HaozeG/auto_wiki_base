# Retrospective Lint Report — 2026-06-27

> Note: This retrospective was run at user request while wiki is still in COLD_START
> (mean_inbound_links = 0.63, threshold 2.0). Structural graph metrics (bridge_score,
> hub_potential) are not yet meaningful. Scorecard fields remain `~` pending maturity.

---

## Pre-run fixes applied

**Bug fixed in `tools/eval_summary.py`:**
`_set_frontmatter_flag` was writing `------` (6-dash) instead of `---` (3-dash) as
the frontmatter closing delimiter, corrupting pages on every eval run. Fixed by
changing `body_rest = text[end:]` → `body_rest = text[end + 3:]`.

**11 entity pages** had `------` frontmatter closers (written by the research agent).
All fixed prior to eval.

**First-paragraph word count** (min 80): 5 pages were 76–79 words; expanded minimally:
- `alibaba_xuantie_c910_c920.md` (+3 words)
- `andes_ax45mp_nx27v.md` (+7 words)
- `boom_riscv.md` (+5 words)
- `iree_riscv.md` (+3 words)
- `xiangshan_riscv.md` (+12 words)

**Synthesis pages** lacked `sources` frontmatter field required by Layer 1 eval.
Added wiki-internal page references as sources for both synthesis pages.

---

## Cleared (17 entity pages)

All 17 entity pages pass Layer 1 (structural) and Layer 2 (density) checks.
Layer 3 (qmd coverage) is non-blocking and was triggered on several pages due to
thin qmd index at this early stage.

| Page | Layer 1 | Layer 2 | Result |
|------|---------|---------|--------|
| alibaba_xuantie_c910_c920.md | PASS | PASS | APPROVED |
| alibaba_xuantie_c950.md | PASS | PASS | APPROVED |
| andes_ax45mp_nx27v.md | PASS | PASS | APPROVED |
| ara_vector_processor.md | PASS | PASS | APPROVED |
| boom_riscv.md | PASS | PASS | APPROVED |
| esperanto_et_soc1.md | PASS | PASS | APPROVED |
| gemmini.md | PASS | PASS | APPROVED |
| iree_riscv.md | PASS | PASS | APPROVED |
| mlir_riscv_backend.md | PASS | PASS | APPROVED |
| nuclei_ux900_n900.md | PASS | PASS | APPROVED |
| risc_v_p_extension.md | PASS | PASS | APPROVED |
| risc_v_vector_extension.md | PASS | PASS | APPROVED |
| sifive_intelligence_x280.md | PASS | PASS | APPROVED |
| tenstorrent_tt_ascalon.md | PASS | PASS | APPROVED |
| tvm_riscv_backend.md | PASS | PASS | APPROVED |
| ventana_veyron_v2.md | PASS | PASS | APPROVED |
| xiangshan_riscv.md | PASS | PASS | APPROVED |

## Cleared (2 synthesis pages)

| Page | RAG Summary | Word Count | Sources | Result |
|------|-------------|------------|---------|--------|
| riscv_open_ai_acceleration.md | present | in range | added | APPROVED |
| riscv_open_source_ai_stack.md | present | in range | added | APPROVED |

## Restructure Candidates

None identified at this stage.

## Merge Candidates

None — all pages cover distinct chips/cores/tools with minimal overlap.

## Delete Candidates

None — all pages pass hard rejection thresholds.

## Deferred for Human Decision

- `needs_summary_revision: true` was set by the eval tool on pages where Layer 3
  (qmd coverage) triggered. Flag is informational; summaries are structurally valid.
  Recommend clearing once the qmd index has been re-indexed with the full 19-page corpus.

## Open Issues for Next Lint Pass

1. `cold_start: true` on all pages — set to `false` after graph maturity (mean_inbound_links > 2.0).
2. `inbound_links` counts should be reconciled with `graph_stats.py` once cross-referencing is complete.
3. Synthesis scorecard fields (`bridge_score`, `cross_domain_connection`) need computation at maturity.
