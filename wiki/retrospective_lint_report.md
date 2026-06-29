# Retrospective Lint Report — 2026-06-29

**Scope:** All 91 pages with `cold_start: true`. Graph maturity confirmed (mean_inbound_links=2.033).
**Eval pipeline:** All 91 pages passed `eval_summary.py` (exit code 0).
**Note:** All 91 pages carry `needs_summary_revision: true` — systemic batch flag, not page-specific. Cleared pages have `cold_start` set to `false`; the `needs_summary_revision` flag should be addressed during routine lint.

---

## Cleared (76 pages)

All pipeline checks pass. `cold_start` set to `false`.

### benchmark_result (16 pages)
- `benchmark_result/AI-Assisted_Llama.cpp_Optimization_Benchmark.md` — inbound=1
- `benchmark_result/Chiplet_RISC_V_AI_SoC_Benchmark_Results.md` — inbound=5
- `benchmark_result/DC-ROMA_AI_PC_Benchmarks.md` — inbound=0
- `benchmark_result/DSC_Fused_Dataflow_Benchmark_Results.md` — inbound=9
- `benchmark_result/HAL_riscv_rvv_Performance_Benchmarks.md` — inbound=1
- `benchmark_result/Jetson_Orin_Nano_YOLOv8n_INT8_Benchmark.md` — inbound=0
- `benchmark_result/llama-cpp-mini_benchmark_apple_m4.md` — inbound=1
- `benchmark_result/llama-cpp_rtx3090_27b_benchmark.md` — inbound=1
- `benchmark_result/PYNQ-Z2_RISC-V_CNN_ISA_Extensions_Benchmark.md` — inbound=1
- `benchmark_result/Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark.md` — inbound=4
- `benchmark_result/RAJA_Performance_Suite_on_Allwinner_D1.md` — inbound=0
- `benchmark_result/RVV_1_0_CNN_Preprocessing_Fallback_Benchmark.md` — inbound=0
- `benchmark_result/RVV_Autovectorization_Compiler_Benchmark_GCC15_LLVM21.md` — inbound=1
- `benchmark_result/SiFive_P550_and_T-HEAD_C910_Benchmark_Comparison.md` — inbound=2
- `benchmark_result/T-HEAD_C910_SPEC_CPU_Benchmark.md` — inbound=17
- `benchmark_result/TVM_and_Gemmini_Accelerator_Benchmark_Results.md` — inbound=4

### entity (23 pages)
- `entity/APS_Framework.md` — inbound=0
- `entity/Codasip_Re-targetable_LLVM_Compiler.md` — inbound=0
- `entity/IREE.md` — inbound=1
- `entity/KPU_Knowledge_Processing_Unit.md` — inbound=0
- `entity/Kendryte_K510.md` — inbound=0
- `entity/LLM_Performance_Model_Prefill_Decode_Estimator.md` — inbound=0
- `entity/llama-cpp-mini.md` — inbound=2
- `entity/ncnn.md` — inbound=1
- `entity/ONNX_Runtime_Build_for_Inferencing.md` — inbound=1
- `entity/onnxruntime-riscv.md` — inbound=1
- `entity/OpenC910_RISC-V_Processor_Core.md` — inbound=0
- `entity/QiMeng_TensorOp.md` — inbound=1
- `entity/RISC-V_Vector_Extension.md` — inbound=0
- `entity/RiVEC_Benchmark_Suite.md` — inbound=0
- `entity/RVLLM-Bench.md` — inbound=0
- `entity/RVV_1_0_Programming.md` — inbound=0
- `entity/Seal5.md` — inbound=1
- `entity/Sipeed.md` — inbound=0
- `entity/Sipeed_LicheePi_4A.md` — inbound=1
- `entity/Sipeed_MAIX_series.md` — inbound=31
- `entity/SpacemiT.md` — inbound=0
- `entity/T-Head_Open_Chip_Community.md` — inbound=0
- `entity/tvmonriscv.md` — inbound=1
- `entity/XuanTie_GNU_Toolchain.md` — inbound=1

### hardware_target (19 pages)
- `hardware_target/Ara_simulator.md` — inbound=1
- `hardware_target/Custom_RISC-V_Core_PYNQ-Z2.md` — inbound=2
- `hardware_target/DC-ROMA_AI_PC_RISC-V_Mainboard_II.md` — inbound=0
- `hardware_target/fpga-sdv_RISC-V_Vector_Cluster.md` — inbound=9
- `hardware_target/GAP8_PULP_Processor.md` — inbound=2
- `hardware_target/Gemmini_Architecture.md` — inbound=3
- `hardware_target/Gemmini_systolic_array_GEMM_accelerator.md` — inbound=7
- `hardware_target/Kendryte_K210.md` — inbound=1
- `hardware_target/MilkV_Pioneer.md` — inbound=3
- `hardware_target/RISC-V_Predictable_Multicore_Vector_Processor.md` — inbound=0
- `hardware_target/SiFive_Intelligence_X280.md` — inbound=0 (distinct from Gen 2; different capability set)
- `hardware_target/SiFive_Intelligence_X280_Gen_2.md` — inbound=0 (distinct successor; retain)
- `hardware_target/SiFive_Intelligence_X390.md` — inbound=6
- `hardware_target/SiFive_Performance_P870.md` — inbound=1
- `hardware_target/SpacemiT_KeyStone_K1.md` — inbound=1
- `hardware_target/Vector_RISC-V_DIMC_Architecture.md` — inbound=0
- `hardware_target/XuanTie_C906.md` — inbound=4
- `hardware_target/XuanTie_C908.md` — inbound=2
- `hardware_target/XuanTie_C910.md` — inbound=3

### optimization_recipe (14 pages)
- `optimization_recipe/AI-Assisted_Llama.cpp_Optimization_Recipe.md` — inbound=0
- `optimization_recipe/Batched_DGEMM_for_Long_Vector_Architectures.md` — inbound=0
- `optimization_recipe/BLAS_Band_Matrix_Optimization_for_RISC-V.md` — inbound=0
- `optimization_recipe/C910_2GHz_Enablement.md` — inbound=0
- `optimization_recipe/DSC_Fused_Dataflow_Optimization_Recipe.md` — inbound=4
- `optimization_recipe/FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe.md` — inbound=1 *(merge target for cluster 6)*
- `optimization_recipe/GGML_CPU_AARCH64_RISCV_Recipe.md` — inbound=0
- `optimization_recipe/HAL_riscv_rvv_OpenCV_Optimization_Recipe.md` — inbound=4
- `optimization_recipe/IntrinTrans_LLM_Intrinsic_Translator.md` — inbound=0
- `optimization_recipe/llama.cpp_RVV_1.0_Q4_0_8_8_Optimization.md` — inbound=0
- `optimization_recipe/Parallel_GEMM_Convolution_on_GAP8.md` — inbound=2
- `optimization_recipe/Q4X_Quantization_Optimization_Recipe.md` — inbound=1
- `optimization_recipe/RVV_1_0_CNN_Preprocessing_Fallback_Optimization.md` — inbound=0
- `optimization_recipe/RVV_Autovectorization_Optimization_Insights.md` — inbound=5
- `optimization_recipe/XuanTie_C908_SHL_GEMM_Optimization.md` — inbound=6

### synthesis (2 pages)
- `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md` — inbound=0 *(orphan; see Deferred)*
- `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md` — inbound=0 *(orphan; see Deferred)*

### workload_kernel (1 page)
- `workload_kernel/GEMM_with_RISC-V_Vector_Extension.md` — inbound=23

---

## Restructure Candidates

- `entity/Chiplet_RISC_V_AI_SoC_Architecture.md`: bridge_score=0.8, inbound=2
  - Entity page contains architecture comparison and cross-vendor claims (multiple chiplet vendors, integration trade-offs, heterogeneous coupling strategies) that belong in a synthesis layer.
  - Proposed synthesis title: `synthesis/Chiplet_RISC_V_AI_Landscape.md`
  - Proposed action: retain entity page for the core architecture definition; split landscape-level comparative claims into the new synthesis page with `connected_entities` linking back.

---

## Merge Candidates

### Cluster 1: MLPerf Tiny (3 → 1)
- `entity/MLPerf_Tiny.md`: inbound=0; YYYY-MM-DD placeholder date; covered by other two pages
- `entity/MLPerf_Tiny_Benchmark.md`: inbound=0; best-grounded source (arxiv paper)
- `entity/MLPerf_Tiny_v1.1.md`: inbound=0; novelty_delta=0.5; version-specific data
  - Proposed action: consolidate all three into `entity/MLPerf_Tiny_Benchmark.md`; absorb v1.1 version data as subsection; delete `MLPerf_Tiny.md` and `MLPerf_Tiny_v1.1.md`.

### Cluster 2: Kendryte K230 (3 → 1)
- `entity/Kendryte_K230.md`: inbound=0; YYYY-MM-DD placeholder date; fully covered by hw_target pages
- `hardware_target/Kendryte_K230.md`: inbound=0; structured but redundant with _SoC page
- `hardware_target/Kendryte_K230_SoC.md`: inbound=1; richest structured constraints (keep)
  - Proposed action: consolidate entity overview paragraph into `hardware_target/Kendryte_K230_SoC.md`; delete `entity/Kendryte_K230.md` and `hardware_target/Kendryte_K230.md`; redirect inbound links.

### Cluster 3: Gemmini entity orphan
- `entity/Gemmini.md`: inbound=0; YYYY-MM-DD placeholder date; fully covered by the two hardware_target Gemmini pages
  - Proposed action: merge unique claims into `hardware_target/Gemmini_systolic_array_GEMM_accelerator.md` (inbound=7); delete `entity/Gemmini.md`.

### Cluster 4: XuanTie C910 duplicate
- `hardware_target/T-HEAD_XuanTie_C910.md`: inbound=0; coarser spec (Sv39 MMU, XIE/XMAE extensions, JTAG, PLIC)
- `hardware_target/XuanTie_C910.md`: inbound=3; full microarchitecture (OoO superscalar, BTB, L2, area/power data)
  - Proposed action: absorb software-facing fields from `T-HEAD_XuanTie_C910.md` into `XuanTie_C910.md`; delete `T-HEAD_XuanTie_C910.md`.

### Cluster 5: XuanTie C908 entity vs hardware_target
- `entity/XuanTie_C908.md`: inbound=1; entity page with blog-post source; partially covered
- `hardware_target/XuanTie_C908.md`: inbound=2; structured constraints (pipeline, RVV 1.0, cluster, bus)
  - Proposed action: absorb AIoT positioning and Alibaba Cloud context from `entity/XuanTie_C908.md` into `hardware_target/XuanTie_C908.md`; delete entity page; update inbound count on hw_target page.

### Cluster 6: FPGA ISA Extensions Optimization Recipe (3 → 1)
- `optimization_recipe/FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe.md`: inbound=1 *(proposed keep)*
- `optimization_recipe/FPGA_Accelerated_RISC_V_ISA_Extensions_Optimization_Recipe.md`: inbound=0
- `optimization_recipe/FPGA_RISC-V_ISA_Extensions_Optimization_Recipe.md`: inbound=0; has best failure-mode analysis
  - All three pages describe the same system: PYNQ-Z2 Zynq-7020, four custom RISC-V extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM), 50 MHz, 2.14× latency speedup, 49.1% energy reduction.
  - Proposed action: absorb failure-mode analysis and resource detail from the other two into `FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe.md`; delete the other two.

### Cluster 7: FPGA ISA Extensions Benchmark Results (2 → 1)
- `benchmark_result/FPGA_Accelerated_RISC_V_ISA_Extensions_Benchmark_Results.md`: inbound=0; datatypes=[]
- `benchmark_result/FPGA_RISC-V_ISA_Extensions_Benchmark_Results.md`: inbound=1; has int16 datatype field *(proposed keep)*
  - Same PYNQ-Z2 measurement context.
  - Proposed action: absorb any unique claims from `FPGA_Accelerated_*` into `FPGA_RISC-V_ISA_Extensions_Benchmark_Results.md`; delete the former.

---

## Delete Candidates

None. All cold_start pages pass the three-layer pipeline. No page has all metrics below threshold without salvageable content.

---

## Deferred for Human Decision

- `synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md` (inbound=0) and `synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md` (inbound=0): Both synthesis pages are cleared but orphaned. After merge actions complete, add bidirectional `[[page_name]]` links from relevant entity/hardware_target pages to these synthesis pages per `relationship_rules` in CLAUDE.md.
- **`needs_summary_revision: true` on all 91 pages**: Appears to be a systemic batch flag from a prior session. Human should confirm whether this flag carries per-page meaning or can be bulk-cleared during routine lint.
- `entity/Kendryte_K510.md` (inbound=0, bridge_score=0.4): Low connectivity and low bridge score; no dedicated hardware_target page. Retained (cleared) since it is the predecessor to the well-connected K230; recommend adding a `[[Kendryte_K230]]` relationship link from this page.

---

## Summary

| Classification | Count |
|----------------|-------|
| Cleared (cold_start → false) | 76 |
| Restructure | 1 |
| Merge clusters | 7 (15 pages involved) |
| Delete | 0 |
| Deferred | 2 synthesis orphans + systemic needs_summary_revision flag |

**Awaiting `lint apply` to execute MERGE and RESTRUCTURE actions.**
