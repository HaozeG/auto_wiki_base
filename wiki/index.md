# Wiki Index

Last updated: 2026-07-02 | Pages: 36 | Sources: 3

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [llvm_ir.md](entity/llvm_ir.md) | LLVM IR | compiler, intermediate representation, SSA | 2 | 0 |
| [opengemm.md](entity/opengemm.md) | OpenGeMM |  | 2 | 0 |
| [boardcon_picot536.md](entity/boardcon_picot536.md) | Boardcon PICOT536 |  | 2 | 0 |
| [mlperf_inference_tiny_benchmark_suite.md](entity/mlperf_inference_tiny_benchmark_suite.md) | MLPerf Inference: Tiny | benchmark, MLPerf, TinyML | 2 | 0 |
| [llvm_riscv_target.md](entity/llvm_riscv_target.md) | LLVM RISC-V Target | LLVM, RISC-V, compiler | 2 | 1 |
| [sifive_intelligence_family.md](entity/sifive_intelligence_family.md) | SiFive Intelligence Family |  | 2 | 0 |
| [rvismith_fuzzer_rvv_intrinsics.md](entity/rvismith_fuzzer_rvv_intrinsics.md) | RVISmith | fuzzing, compiler testing, RVV, RISC-V, intrinsics | 2 | 1 |
| [xuantie_c930.md](entity/xuantie_c930.md) | XuanTie C930 | risc-v, xuantie, server, alibaba | 2 | 0 |
| [riscv_vector_extension.md](entity/riscv_vector_extension.md) | RISC-V Vector Extension (RVV) | riscv, vector, specification | 2 | 1 |
| [integrated_matrix_extension.md](entity/integrated_matrix_extension.md) | Integrated Matrix Extension (IME) | RISC-V, ISA, Matrix Extension | 2 | 1 |
| [matrix_tile_extension.md](entity/matrix_tile_extension.md) | Matrix Tile Extension (MTE) |  | 2 | 1 |
| [riscv_matrix_extension_proposal.md](entity/riscv_matrix_extension_proposal.md) | RISC-V Matrix Specification Proposal | risc-v, matrix-extension, isa, accelerator | 1 | 2 |
| [xuantie-c910.md](entity/xuantie-c910.md) | XuanTie C910 |  | 2 | 1 |
| [gemmini.md](entity/gemmini.md) | Gemmini |  | 2 | 2 |

## Synthesis Pages

| Page | Connected Entities | Status | Inbound |
|------|--------------------|--------|---------|
| [riscv_matrix_extension_design_space.md](synthesis/riscv_matrix_extension_design_space.md) | integrated_matrix_extension, matrix_tile_extension, riscv_matrix_extension_proposal, riscv_vector_extension, rvme, llvm_riscv_target | draft | 0 |

## Concept Index

- **RISC-V Matrix Specification Proposal**: → [riscv_matrix_extension_proposal](entity/riscv_matrix_extension_proposal.md)
- **XuanTie C908**: → [xuantie_c908](hardware_target/xuantie_c908.md)
- **XuanTie C910**: → [xuantie-c910](entity/xuantie-c910.md)
- **Gemmini**: → [gemmini](entity/gemmini.md)
- **RVME**: → [rvme](hardware_target/rvme.md)
- **RVME GEMM benchmark comparison**: → [rvme_gemm_benchmark_comparison](benchmark_result/rvme_gemm_benchmark_comparison.md)
- **Meta MTIA**: → [meta_mtia](hardware_target/meta_mtia.md)
- **RISC-V Vector Extension (RVV)**: → [riscv_vector_extension](entity/riscv_vector_extension.md)
- **Integrated Matrix Extension (IME)**: → [integrated_matrix_extension](entity/integrated_matrix_extension.md)
- **Matrix Tile Extension (MTE)**: → [matrix_tile_extension](entity/matrix_tile_extension.md)
- **Template-Based Micro-kernel Generation for GEMM**: → [generic_micro_kernel_templates_gemm](optimization_recipe/generic_micro_kernel_templates_gemm.md)
- **MLIR+xDSL RISC-V Vector GEMM Benchmark**: → [mlir_xdsl_gemm_benchmark_k230_bananapi_f3](benchmark_result/mlir_xdsl_gemm_benchmark_k230_bananapi_f3.md)
- **MLIR+xDSL RVV GEMM Codegen Recipe**: → [mlir_xdsl_rvv_gemm_codegen_recipe](optimization_recipe/mlir_xdsl_rvv_gemm_codegen_recipe.md)
- **LLVM RISC-V Target**: → [llvm_riscv_target](entity/llvm_riscv_target.md)
- **SiFive Intelligence Family**: → [sifive_intelligence_family](entity/sifive_intelligence_family.md)
- **RVISmith**: → [rvismith_fuzzer_rvv_intrinsics](entity/rvismith_fuzzer_rvv_intrinsics.md)
- **XuanTie C930**: → [xuantie_c930](entity/xuantie_c930.md)
- **XuanTie C906**: → [xuantie_c906](hardware_target/xuantie_c906.md)
- **XuanTie C950**: → [xuantie_c950](hardware_target/xuantie_c950.md)
- **StarFive VisionFive2**: → [starfive_visionfive2_jh7110](hardware_target/starfive_visionfive2_jh7110.md)
- **K230**: → [k230](hardware_target/k230.md)
- **SiFive Intelligence X280**: → [sifive_intelligence_x280](hardware_target/sifive_intelligence_x280.md)
- **SiFive Intelligence X200 Series**: → [sifive_intelligence_x200_series](hardware_target/sifive_intelligence_x200_series.md)
- **Competing Approaches to Matrix Acceleration on RISC-V**: → [riscv_matrix_extension_design_space](synthesis/riscv_matrix_extension_design_space.md)

## Optimization Pages

| Page | Type | Summary | Tags | Sources | Inbound |
|------|------|---------|------|---------|---------|
| [banana_pi_gemm_optimization_benchmark.md](benchmark_result/banana_pi_gemm_optimization_benchmark.md) | benchmark_result | Banana Pi GEMM Optimization Benchmark |  | 2 | 0 |
| [sgemm_optimization_allwinner_nezha_d1.md](optimization_recipe/sgemm_optimization_allwinner_nezha_d1.md) | optimization_recipe | SGEMM Optimization on Allwinner Nezha D1 | sgemm, riscv, optimization, allwinner, nezha-d1 | 2 | 0 |
| [xuantie_c907.md](hardware_target/xuantie_c907.md) | hardware_target | XuanTie C907 | risc-v, matrix-extension, mme, xuantie, t-head, ai | 2 | 0 |
| [allwinner_v853.md](hardware_target/allwinner_v853.md) | hardware_target | Allwinner V853 |  | 2 | 0 |
| [allwinner_t536.md](hardware_target/allwinner_t536.md) | hardware_target | Allwinner T536 | allwinner, risc-v, arm, npu, industrial | 2 | 1 |
| [allwinner_v851s.md](hardware_target/allwinner_v851s.md) | hardware_target | Allwinner V851s | allwinner, ip-camera, risc-v, arm-cortex-a7, npu | 2 | 0 |
| [xuantie_e907.md](hardware_target/xuantie_e907.md) | hardware_target | XuanTie E907 | e907, risc-v, xuantie | 2 | 0 |
| [sifive_intelligence_x200_series.md](hardware_target/sifive_intelligence_x200_series.md) | hardware_target | SiFive Intelligence X200 Series |  | 2 | 0 |
| [sifive_intelligence_x280.md](hardware_target/sifive_intelligence_x280.md) | hardware_target | SiFive Intelligence X280 |  | 2 | 0 |
| [xuantie_c950.md](hardware_target/xuantie_c950.md) | hardware_target | XuanTie C950 | risc-v, alibaba | 2 | 0 |
| [xuantie_c906.md](hardware_target/xuantie_c906.md) | hardware_target | XuanTie C906 |  | 2 | 0 |
| [starfive_visionfive2_jh7110.md](hardware_target/starfive_visionfive2_jh7110.md) | hardware_target | StarFive VisionFive2 | risc-v, jh7110, starfive, sdk | 2 | 0 |
| [k230.md](hardware_target/k230.md) | hardware_target | K230 | SoC, K230, Kendryte, RISC-V | 2 | 0 |
| [generic_micro_kernel_templates_gemm.md](optimization_recipe/generic_micro_kernel_templates_gemm.md) | optimization_recipe | Template-Based Micro-kernel Generation for GEMM | gemm, micro-kernel, SIMD, intrinsics, BLIS, ARM, x86 | 2 | 0 |
| [mlir_xdsl_gemm_benchmark_k230_bananapi_f3.md](benchmark_result/mlir_xdsl_gemm_benchmark_k230_bananapi_f3.md) | benchmark_result | MLIR+xDSL RISC-V Vector GEMM Benchmark on K230 and BananaPi F3 vs OpenBLAS | GEMM, RVV, MLIR, xDSL, OpenBLAS | 2 | 0 |
| [mlir_xdsl_rvv_gemm_codegen_recipe.md](optimization_recipe/mlir_xdsl_rvv_gemm_codegen_recipe.md) | optimization_recipe | MLIR+xDSL Lowering Pipeline for RISC-V Vector GEMM Micro-kernels | MLIR, xDSL, RISC-V, RVV, GEMM, code generation | 2 | 11 |
| [rvme.md](hardware_target/rvme.md) | hardware_target | RVME | risc-v, matrix-extension, accelerator, gemm, gem5 | 1 | 9 |
| [meta_mtia.md](hardware_target/meta_mtia.md) | hardware_target | Meta MTIA | risc-v, accelerator, dlrm, triton, compiler | 1 | 0 |
| [rvme_gemm_benchmark_comparison.md](benchmark_result/rvme_gemm_benchmark_comparison.md) | benchmark_result | RVME GEMM benchmark comparison | risc-v, benchmark, gemm, accelerator-comparison | 1 | 1 |
| [xuantie_c908_fp16_gemm_kernel.md](workload_kernel/xuantie_c908_fp16_gemm_kernel.md) | workload_kernel | XuanTie C908 FP16 GEMM Outer Product Kernel |  | 2 | 7 |
| [xuantie_c908.md](hardware_target/xuantie_c908.md) | hardware_target | XuanTie C908 |  | 2 | 10 |
