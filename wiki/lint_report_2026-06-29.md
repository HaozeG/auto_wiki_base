# Routine Lint Report — 2026-06-29

**Wiki state**: 140 pages | mean_inbound_links: 2.24 | graph_maturity: MATURE  
**cold_start: true pages**: 58 (all from this session — retrospective lint not yet run)

---

## Issue 1 — Orphan Pages (61 pages, inbound_links: 0)

All synthesis pages and most entity/hardware/benchmark pages added this session have no inbound links yet. This is expected for pages that haven't been referenced from other pages. No action required until retrospective lint — orphan status post-retrospective will identify true orphans.

**Synthesis orphans (5)** — these are actionable: synthesis pages should accumulate inbound links from entities as they are updated:

| Page | Recommendation |
|------|---------------|
| `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md` | Bump inbound links from connected entity pages |
| `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md` | Bump inbound links from connected entity pages |
| `synthesis/MLIR_for_RISC-V_AI_Compilation.md` | Just created — acceptable |
| `synthesis/RISC-V_ISA_Extensions_for_AI.md` | Just created — acceptable |
| `synthesis/Tenstorrent_RISC-V_AI_Ecosystem.md` | Just created — acceptable |

**Deferred**: All 56 entity/hardware/benchmark/recipe orphans are deferred to retrospective lint.

---

## Issue 2 — Off-Theme Pages (2 pages)

These pages were written by the orchestrator during session 7 (query drift on "MLIR compiler backend" → Qwen/LLM models). They contain no RISC-V AI accelerator content.

| Page | Problem | Recommendation |
|------|---------|---------------|
| `entity/Qwen3.6.md` | RTX 6000 GPU LLM benchmarks, no RISC-V content | **DELETE** |
| `entity/Qwen2.5-Coder-1.5B-Instruct-GGUF.md` | GGUF model card, no RISC-V content | **DELETE** |

**Deferred for human**: These are DELETE candidates. Both have `inbound_links: 0`. Confirm deletion.

---

## Issue 3 — Duplicate / Redundant Pages (4 pages across 2 groups)

### Group A: Gemmini (3 pages)

| Page | Type | cold_start | Inbound |
|------|------|------------|---------|
| `entity/Gemmini.md` | entity | true | 0 |
| `hardware_target/Gemmini_Architecture.md` | hardware_target | false | 5 |
| `hardware_target/Gemmini_systolic_array_GEMM_accelerator.md` | hardware_target | false | 3 |

`Gemmini_Architecture.md` (mature, 5 inbound) is the canonical page. `entity/Gemmini.md` (cold_start, 0 inbound) was added by session 6 and overlaps ~70%. `Gemmini_systolic_array_GEMM_accelerator.md` covers the same accelerator at a more detailed hardware level.

**Recommendation**: MERGE `entity/Gemmini.md` → `hardware_target/Gemmini_Architecture.md`. Delete entity page, redirect inbound links (none to redirect).

### Group B: RVME (2 pages)

| Page | Type | cold_start | Inbound |
|------|------|------------|---------|
| `hardware_target/RVME_Matrix_Engine.md` | hardware_target | true | 1 |
| `hardware_target/RVME_Model.md` | hardware_target | true | 0 |

Both were written by session 8 targeting the same RVME paper. `RVME_Matrix_Engine.md` is the primary ingest page (written by earlier manual ingest). `RVME_Model.md` adds model/simulation details from GitHub.

**Recommendation**: MERGE `RVME_Model.md` content into `RVME_Matrix_Engine.md` under a "Model/Simulation" subsection. Delete `RVME_Model.md`.

**Deferred for human**: Both groups require human confirmation before merge/delete.

---

## Issue 4 — `needs_summary_revision: true` (80 pages)

The `eval_summary.py` Layer 3 check sets this flag when BM25 saturation score ≥ 2 competitors in top-5. On a 140-page wiki covering a single domain, nearly every page is "saturated" by this metric — this is a false-positive endemic to the mature graph state.

**Root cause**: Layer 3 was designed for cold-start filtering (reject near-duplicates before write). On an already-mature graph, it flags legitimate pages that are simply in a dense topic cluster.

**Recommendation**: For the 80 pages flagged, do not auto-clear — run `lint retrospective` (using `eval_summary.py --verbose`) to distinguish true quality failures from saturation false-positives. The `needs_summary_revision` flag on pages that PASS Layer 1 (structure) and Layer 2 (entity density) should be cleared.

**Pages that likely have real issues** (Layer 1 or structure failures, not just saturation):
- Any page with empty `sources:` list
- Any page whose first paragraph contains dangling reference patterns

Spot-check of flagged pages shows most pass Layer 1 and fail only Layer 3 — confirming false-positive hypothesis. No immediate action needed.

---

## Issue 5 — Missing Cross-References

The orchestrator reported synthesis gaps throughout this session. Three clusters remain uncovered after the synthesis pages written today:

| Tag | Uncovered Entity Pages | Current Synthesis |
|-----|----------------------|-------------------|
| `benchmark` | 6 pages (MLPerf_Inference_Benchmarks, RiVEC, rvv-bench, MLPerf_Tiny, MLPerf_Tiny_v1.1, MLPerf_Inference_Benchmark_Suite) | None |
| `inference` | 3 pages (MLPerf_Inference_Benchmarks, RVLLM-Bench, MLPerf_Inference_Benchmark_Suite) | None |
| `AI` | 5 pages (PyAi_k210, Sipeed, Kendryte_K510, KPU, SpacemiT) | Partial (RISC-V_AI_Hardware_Target_Taxonomy) |

**Recommendation**: A "RISC-V AI Benchmarking Landscape" synthesis page connecting MLPerf Tiny, MLPerf Inference, RiVEC, rvv-bench, and RVLLM-Bench would close both the `benchmark` and `inference` gaps. Deferred for next session or on explicit request.

---

## Issue 6 — Synthesis Pages Without Inbound Links

The 3 synthesis pages written today (`Tenstorrent_RISC-V_AI_Ecosystem`, `MLIR_for_RISC-V_AI_Compilation`, `RISC-V_ISA_Extensions_for_AI`) have `inbound_links: 0`. This is expected — their connected entity pages do not yet back-reference the synthesis. This can be fixed by adding a `## Referenced By` or relationship entry on key entity pages pointing to the synthesis.

**Deferred**: Low priority. Entity pages will accumulate synthesis references during retrospective lint or next editing pass.

---

## Actions Required (Human Confirmation Needed)

1. **DELETE** `entity/Qwen3.6.md` — off-theme, no RISC-V content, 0 inbound links
2. **DELETE** `entity/Qwen2.5-Coder-1.5B-Instruct-GGUF.md` — off-theme, 0 inbound links
3. **MERGE** `entity/Gemmini.md` → `hardware_target/Gemmini_Architecture.md`, then delete entity page
4. **MERGE** `hardware_target/RVME_Model.md` → `hardware_target/RVME_Matrix_Engine.md`, then delete Model page
5. **RUN** `lint retrospective` to evaluate all 58 cold_start pages from this session

## No-Action Items

- 56 non-synthesis orphan pages: acceptable until retrospective lint
- 80 `needs_summary_revision` flags: mostly Layer 3 saturation false-positives; defer to retrospective
