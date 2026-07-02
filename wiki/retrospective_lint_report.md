# Retrospective Lint Report — 2026-07-02

Scope: all 101 pages currently marked `cold_start: true` (100% of the wiki). Each page was run through `tools/eval_summary.py --verbose` with its declared `type`. Results: **101/101 pass Layer 1** (grounding, dangling-reference, word-count checks) and **101/101 pass Layer 2** (entity/measurement density, compression ratio). Layer 3 (qmd BM25 self-retrieval + topic-saturation) flagged 49 pages as "saturated" (≥2 competitors in top-5 search) — per `CLAUDE.md`, saturation is a **merge/update hint, not a verdict**, and this wiki's `optimization_first` profile deliberately cross-links `hardware_target` / `optimization_recipe` / `benchmark_result` / `workload_kernel` subtypes about the same chip, so shared vocabulary between e.g. a chip page and its own benchmark-result page is expected structure, not duplication. Each saturation flag was manually reviewed against actual file contents before classification below; the large majority are false positives from this expected cross-referencing (including two self-match artifacts caused by BM25 hyphen/underscore normalization: `xuantie-c910.md` and `rvv-lite.md` each appeared as their own "competitor" under a re-tokenized slug — no such separate pages exist).

## Cleared (98 pages)

All pages not listed under Restructure/Merge/Delete below are **CLEARED**: Layer 1 + Layer 2 pass, and any Layer 3 saturation warning traces to expected same-hardware cross-referencing (e.g. `xuantie_c908.md` co-occurring with `xuantie_c908_fp16_gemm_kernel.md` and `xuantie_c908_ai_inference_performance.md`; `pulp_platform.md` co-occurring with `pulpissimo.md`/`pulp_nn.md`; `semidynamics.md` co-occurring with `semidynamics_tensor_unit.md`; `sifive_intelligence_x280.md`/`x390.md`/`family.md` siblings; etc.) rather than genuine redundant content. `cold_start` can be set to `false` for these pages.

(Full list: all 101 pages in `wiki/_pages/` minus the 3 pages below.)

## Restructure Candidates

- `hardware_target/k230.md`: bridge_score=0.7, inbound_links=44. The Relationships section has grown to 12+ entries spanning task-scheduling theory, RISC-V+GPU integration trends, cross-vendor ONNX/Jetson benchmarks, YOLOv8, and multiple unrelated benchmarking tools — content that increasingly compares/synthesizes across the wiki rather than describing the K230 itself.
  - Proposed synthesis title: "Edge AI SoC Design Space: KPU/Fixed-Function vs. Vector-Only vs. Many-Core Approaches" (would draw K230, ET-SoC-1, Rockchip RK3588, Grayskull e75, Semidynamics Tensor Unit into a comparison page, leaving K230's entity page to hold only its own hardware description).
- `optimization_recipe/mlir_xdsl_rvv_gemm_codegen_recipe.md`: bridge_score=0.7, inbound_links=43. Similarly accumulated a wide Relationships section (OpenGeMM, generic ARM/x86 micro-kernel templates, Tile Language, MLIR itself, multiple hardware targets) that reads as a comparison of RISC-V GEMM code-generation approaches rather than a single recipe.
  - Proposed synthesis title: "Compiler-Generated vs. Hand-Tuned vs. Hardware-Accelerated GEMM on RISC-V" (would draw this recipe, OpenGeMM, generic_micro_kernel_templates_gemm, and the XuanTie C908 hand-tuned kernel into one comparison page).

## Merge Candidates

- `benchmark_result/gcc15_clang21_autovectorization_rvv_bananapi_f3.md`: 85%+ content overlap with `benchmark_result/compiler_benchmark_bananapi_f3_gcc15_clang21.md`.
  - Both pages are grounded in the same paper (arXiv:2605.10860, fetched as `/abs/` on 2026-07-02T04:32 and `/html/...v2` on 2026-07-02T05:28), same hardware (BananaPi-F3, RVV 1.0), same comparison (GCC 15 vs. Clang 21 autovectorization: 35% predication overhead, 4x strided-load cost, GCC winning 4/6 benchmarks). Identity Resolution missed this because the two `canonical_name` values ("GCC 15 vs Clang 21 Autovectorization on BananaPi-F3 (RVV)" vs. "Compiler Benchmark Comparison on BananaPi-F3 (RVV 1.0)") don't string-normalize to the same key.
  - Proposed action: merge into `compiler_benchmark_bananapi_f3_gcc15_clang21.md` (the more complete of the two — it also covers the Qsim quantum-simulator RVV backend finding that the other page omits), redirect inbound links (currently: `sifive_performance_p570_gen3.md` and `llvm_riscv_target.md` link to the shorter page; `spacemit_x60.md` links to the target page), then delete `gcc15_clang21_autovectorization_rvv_bananapi_f3.md`.

## Delete Candidates

None. No page's metrics fall below the entity/synthesis `hard_rejection_threshold` (0.2), and no page lacks salvageable, RISC-V-relevant, sourced content.

## Deferred for Human Decision

- `entity/systolic_tensor_units.md`: scorecard averages 0.43 (novelty_delta 0.6, claim_density 0.3, self_containedness 0.4, bridge_score 0.2) — the weakest page in the wiki, but not below the hard-rejection floor. Its content is largely generic Google TPU background (systolic-array dataflow, TPU v4 vs v3) with only a thin RISC-V/Gemmini tie-in via one Relationships bullet. Candidates: (a) leave as-is (it's a legitimate cross-reference target for `gemmini.md` and other systolic-array discussions), or (b) fold its content into `gemmini.md`'s body as background context and delete the standalone page. Deferring since this is a judgment call about wiki granularity, not a correctness issue.
- Both Restructure candidates above (`k230.md`, `mlir_xdsl_rvv_gemm_codegen_recipe.md`) are proposals, not executed splits — writing the two proposed synthesis pages is nontrivial editorial work (drawing in 4-5 entity pages each) that should be scoped as its own task rather than folded into `lint apply`.
