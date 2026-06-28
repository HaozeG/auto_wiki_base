# Retrospective Lint Report — 2026-06-29

Graph maturity reached: mean_inbound_links = 2.033 across 91 pages.

## Cleared (2 synthesis pages created at transition)

- `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md`: eval approved — bridge_score=0.85, cross_domain_connection=0.9
- `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md`: eval approved — bridge_score=0.9, cross_domain_connection=0.85

## Needs Summary Revision (17 pages — needs_summary_revision: true flag)

These pages were flagged by the eval pipeline for RAG summary revision. Deferred for human review.

- `benchmark_result/AI-Assisted_Llama.cpp_Optimization_Benchmark.md`
- `benchmark_result/DC-ROMA_AI_PC_Benchmarks.md`
- `benchmark_result/FPGA_RISC-V_ISA_Extensions_Benchmark_Results.md`
- `benchmark_result/PYNQ-Z2_RISC-V_CNN_ISA_Extensions_Benchmark.md`
- `benchmark_result/RVV_1_0_CNN_Preprocessing_Fallback_Benchmark.md`
- `benchmark_result/SiFive_P550_and_T-HEAD_C910_Benchmark_Comparison.md`
- `benchmark_result/T-HEAD_C910_SPEC_CPU_Benchmark.md`
- `benchmark_result/llama-cpp-mini_benchmark_apple_m4.md`
- `benchmark_result/llama-cpp_rtx3090_27b_benchmark.md`
- `entity/Codasip_Re-targetable_LLVM_Compiler.md`
- `entity/MLPerf_Tiny_v1.1.md`
- `entity/OpenC910_RISC-V_Processor_Core.md`
- `entity/RISC-V_Vector_Extension.md`
- `entity/RVLLM-Bench.md`
- `entity/RVV_1_0_Programming.md`
- `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md`
- `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md`

## Orphan Pages — 42 total (inbound_links = 0)

Pages with no inbound links. At graph maturity these are candidates for merge, restructure, or deletion.

### Candidate for Merge — Duplicates

- `entity/Gemmini.md` + `hardware_target/Gemmini_Architecture.md`: both cover Gemmini accelerator. Recommend merging content into `hardware_target/Gemmini_Architecture.md` and redirecting inbound links. `entity/Gemmini.md` inbound=0; `hardware_target/Gemmini_Architecture.md` inbound=3.
- `entity/Kendryte_K230.md` + `hardware_target/Kendryte_K230.md` + `hardware_target/Kendryte_K230_SoC.md`: three pages for K230. Recommend consolidating into `hardware_target/Kendryte_K230_SoC.md`.
- `hardware_target/T-HEAD_XuanTie_C910.md` + `hardware_target/XuanTie_C910.md`: likely duplicate. `XuanTie_C910.md` has inbound=3 from synthesis; recommend merging `T-HEAD_XuanTie_C910.md` into it.
- `entity/MLPerf_Tiny.md` + `entity/MLPerf_Tiny_Benchmark.md` + `entity/MLPerf_Tiny_v1.1.md`: three pages on MLPerf Tiny. Recommend merging into one authoritative entity page.
- `hardware_target/SiFive_Intelligence_X280.md` + `hardware_target/SiFive_Intelligence_X280_Gen_2.md`: two generations, inbound=0 on both. Recommend merging into one page with versioning section.

### Candidate for Cross-Reference Fix

- `entity/RISC-V_Vector_Extension.md`: foundational entity, should be referenced by RVV-focused optimization_recipe and hardware_target pages.
- `entity/RVV_1_0_Programming.md`: same — should be referenced by optimization_recipe pages using RVV intrinsics.
- `entity/RiVEC_Benchmark_Suite.md`, `entity/RVLLM-Bench.md`: benchmark frameworks with no inbound links; could be referenced by benchmark_result pages.
- `entity/T-Head_Open_Chip_Community.md`, `entity/SpacemiT.md`, `entity/Sipeed.md`: vendor/company pages with no links from product pages.
- `optimization_recipe/GGML_CPU_AARCH64_RISCV_Recipe.md`, `optimization_recipe/IntrinTrans_LLM_Intrinsic_Translator.md`: optimization recipes with no inbound links from benchmark_result pages.
- `optimization_recipe/llama.cpp_RVV_1.0_Q4_0_8_8_Optimization.md`: should link from LLM benchmark pages.

### Candidate for Review — Off-Topic or Weak Pages

- `benchmark_result/Jetson_Orin_Nano_YOLOv8n_INT8_Benchmark.md`: Jetson Orin Nano is NVIDIA/ARM, not RISC-V. Possibly off-topic for this wiki. Recommend deletion or tagging as reference comparison.
- `entity/APS_Framework.md`: newly created, relevance to RISC-V AI accelerator theme unclear. Inbound=0. Deferred for human review.
- `entity/LLM_Performance_Model_Prefill_Decode_Estimator.md`: performance estimation methodology. Inbound=0. Relevant but needs linking from LLM inference pages.

### New Synthesis Pages (Expected Orphans)

- `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md`: new, no pages yet link to it. Expected.
- `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md`: new, no pages yet link to it. Expected.

## Contradictions Found

- **RVV version on MilkV Pioneer SG2042**: `hardware_target/MilkV_Pioneer.md` states "rv64imafdcv vector extensions" while `wiki/patch_queue.md` notes InferLLM documentation specifies RVV 0.7 for SG2042. Needs verification and correction.
- **Duplicate hardware pages**: Multiple pages for XuanTie C910 and Kendryte K230 (see merge candidates above) may contain conflicting claims.

## Actions Taken

- Graph maturity transition logged in `wiki/log.md`.
- `CLAUDE.md` updated: `graph_maturity: true`, `cold_start_page_count: 91`, `mean_inbound_links: 2.033`.
- Two synthesis pages created and validated.
- Inbound links updated in 22 referenced pages.

## Deferred for Human Decision

- Execute MERGE candidates (Gemmini, Kendryte K230, MLPerf Tiny, SiFive X280): requires human approval before merging/deleting.
- DELETE `benchmark_result/Jetson_Orin_Nano_YOLOv8n_INT8_Benchmark.md` if deemed off-topic.
- Resolve RVV version contradiction for MilkV Pioneer SG2042.
- Apply `needs_summary_revision: true` fixes across 17 pages.
- Add cross-references to connect orphan entity pages (RISC-V_Vector_Extension, RVV_1_0_Programming, vendor pages).
