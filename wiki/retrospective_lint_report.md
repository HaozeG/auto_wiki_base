# Retrospective Lint Report — 2026-06-29 (Session 2)

## Summary

Pages evaluated: 54 (all `cold_start: true` pages from research sessions 1–9 + 3 synthesis pages)
Graph state: 136 pages | mean_inbound_links: 2.30 | MATURE

## Cleared (54 pages)

All 54 pages passed eval_summary.py Layer 1 (structural) and Layer 2 (skipped — spaCy not installed). `cold_start` set to `false` on all. `needs_summary_revision: true` flags removed.

### benchmark_result (8)
Ara2_Benchmark_Results, Grayskull_SRAM_Attention_Benchmarks, N_Body_Simulation_on_Tenstorrent_Wormhole_Benchmark, nncase_K230_Benchmark_Results, P_CORE_Packed_SIMD_Extension_Benchmark_Results, RVME_GEMM_Benchmark, Tenstorrent_Grayskull_MatMul_Efficiency, TT_BUDA_Benchmark_Results

### entity (19)
Chipyard_Framework, MLIR, MLIR_software, MLPerf_Inference_Benchmarks, MLPerf_Inference_Benchmark_Suite, MLPerf_Training_Reference_Implementations, PyAi_k210, RISC-V_Matrix_Extension, rvv-bench, RV-VP2, SYCL_MLIR_Compiler, Tenstorrent_Ascalon, Tenstorrent, Tenstorrent_Software_Stack, tt-awesome, TT-Forge, TT_Inference_Server_Benchmarking, TT_Metalium, XuanTie_C930

### hardware_target (19)
Ara2, Ara2_RVV_1.0_Vector_Processor, AraXL, Blackhole_Architecture, Blackhole_Tensix_Processor, NVIDIA_Deep_Learning_Accelerator, P-Box_RISC-V_Packed-SIMD_Implementation, RVME_Matrix_Engine, SiFive_Intelligence_X300_Series, SiFive_Performance_P870_D, SpacemiT_Key_Stone_K1, Tenstorrent_Ascalon (hardware_target), Tenstorrent_Blackhole, Tenstorrent_Grayskull_e150, Tenstorrent_Grayskull, Tenstorrent_Wormhole_n300, T-HEAD_Xuantie_C910, TT-QuietBox_2, Wormhole_Tensix_Processor

### optimization_recipe (5)
EARTH_Efficient_Architecture_RISC_V_Vector_Memory_Access, FlashAttention_on_Tenstorrent_Wormhole_Optimization, Gemmini_IREE_Integration_Strategy, Grayskull_SRAM_Fused_Attention_Kernel, Operator_Fusion_for_LLM_Inference_on_Tensix

### synthesis (3)
MLIR_for_RISC-V_AI_Compilation, RISC-V_ISA_Extensions_for_AI, Tenstorrent_RISC-V_AI_Ecosystem

## Restructure Candidates

None.

## Merge Candidates

None beyond the 4 resolved in lint apply (2026-06-29).

## Delete Candidates

None.

## Deferred for Human Decision

None.

## Notes

- Layer 2 skipped (spaCy `en_core_web_sm` not installed). Run `python -m spacy download en_core_web_sm` to enable entity density checks.
- Layer 3 saturation warnings are endemic to a mature single-domain graph and were not treated as blockers.
