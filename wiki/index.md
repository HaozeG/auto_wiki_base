# Wiki Index

**Topic**: RISC-V AI Accelerator — hardware targets, workload kernels, optimization recipes, and benchmark results for RISC-V based AI/ML acceleration. Covers ISA extensions (V, Zve*, P), NPU/DSP integrations, inference toolchains (LLVM, TVM, IREE, ONNX Runtime), and measured performance across edge and server SoCs.

**Organization**: Workflow-first — pages are typed as `hardware_target`, `workload_kernel`, `optimization_recipe`, `benchmark_result`, `entity`, or `synthesis`.

Last updated: 2026-06-28 | Pages: 27 | Sources: 0

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [XuanTie_C908.md](entity/XuanTie_C908.md) | XuanTie C908 | RISC-V, T-Head, XuanTie, AIoT, processor | 1 | 0 |
| [Kendryte_K510.md](entity/Kendryte_K510.md) | Kendryte K510 | RISC-V, AI, edge_computing, accelerator, Canaan | 1 | 0 |
| [RVLLM-Bench.md](entity/RVLLM-Bench.md) | RVLLM-Bench | RISC-V, LLM, benchmark, RVV, inference | 1 | 0 |
| [IREE.md](entity/IREE.md) | IREE | MLIR, compiler, runtime, AI, machine learning, RISC-V | 1 | 0 |
| [OpenC910_RISC-V_Processor_Core.md](entity/OpenC910_RISC-V_Processor_Core.md) | OpenC910 RISC-V Processor Core | RISC-V, T-Head, open-source, processor_core, simulation | 1 | 0 |
| [MLPerf_Tiny_Benchmark.md](entity/MLPerf_Tiny_Benchmark.md) | MLPerf Tiny Benchmark | TinyML, benchmark, machine_learning, ultra-low-power, MLPerf | 1 | 0 |
| [MLPerf_Tiny.md](entity/MLPerf_Tiny.md) | MLPerf Tiny | benchmark, tinyML, MLPerf | 1 | 0 |
| [RiVEC_Benchmark_Suite.md](entity/RiVEC_Benchmark_Suite.md) | RiVEC Benchmark Suite | RISC-V, benchmark, vector, data-parallel | 1 | 0 |
| [tvmonriscv.md](entity/tvmonriscv.md) | tvmonriscv: TVM Compilation Workflow for RISC-V | RISC-V, TVM, Machine Learning, Workflow | 1 | 0 |
| [Sipeed_LicheePi_4A.md](entity/Sipeed_LicheePi_4A.md) | Sipeed LicheePi 4A | RISC-V, AI, development_board, Sipeed, TH1520 | 3 | 0 |
| [Sipeed_MAIX_series.md](entity/Sipeed_MAIX_series.md) | Sipeed MAIX series | RISC-V, AI, edge_computing, development_board | 1 | 0 |

## Synthesis Pages

| Page | Connected Entities | Status | Inbound |
|------|--------------------|--------|---------|

## Concept Index


## Optimization Pages

| Page | Type | Summary | Tags | Sources | Inbound |
|------|------|---------|------|---------|---------|
| [SiFive_Performance_P870.md](hardware_target/SiFive_Performance_P870.md) | hardware_target | SiFive Performance P870 | RISC-V, SiFive, HPC, data center, out-of-order | 1 | 0 |
| [SiFive_Intelligence_X390.md](hardware_target/SiFive_Intelligence_X390.md) | hardware_target | SiFive Intelligence X390 | RISC-V, SiFive, AI, machine learning, vector | 1 | 0 |
| [DC-ROMA_AI_PC_Benchmarks.md](benchmark_result/DC-ROMA_AI_PC_Benchmarks.md) | benchmark_result | DC-ROMA AI PC Benchmarks | RISC-V, SiFive P550, DC-ROMA, benchmark, Geekbench, HPL, iozone, iperf3, glmark2 | 1 | 0 |
| [DC-ROMA_AI_PC_RISC-V_Mainboard_II.md](hardware_target/DC-ROMA_AI_PC_RISC-V_Mainboard_II.md) | hardware_target | DC-ROMA AI PC RISC-V Mainboard II | RISC-V, SiFive P550, DC-ROMA, AI PC, Framework Laptop | 1 | 0 |
| [llama.cpp_RVV_1.0_Q4_0_8_8_Optimization.md](optimization_recipe/llama.cpp_RVV_1.0_Q4_0_8_8_Optimization.md) | optimization_recipe | llama.cpp RVV 1.0 Q4_0_8_8 Optimization | RISC-V, Vector 1.0, llama.cpp, ggml, Q4_0_8_8, quantization, AI, inference | 1 | 0 |
| [Q4X_Quantization_Optimization_Recipe.md](optimization_recipe/Q4X_Quantization_Optimization_Recipe.md) | optimization_recipe | Q4X Quantization Optimization Recipe | Q4X, quantization, LLM, RISC-V, codebook | 1 | 0 |
| [Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark.md](benchmark_result/Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark.md) | benchmark_result | Q4X Quantization LLM Inference Milk-V Jupiter Benchmark | Q4X, quantization, LLM, RISC-V, Milk-V Jupiter | 1 | 0 |
| [C910_2GHz_Enablement.md](optimization_recipe/C910_2GHz_Enablement.md) | optimization_recipe | C910 2GHz Enablement | C910, Lichee Module 4A, overclocking, device tree | 1 | 0 |
| [T-HEAD_C910_SPEC_CPU_Benchmark.md](benchmark_result/T-HEAD_C910_SPEC_CPU_Benchmark.md) | benchmark_result | T-HEAD C910 SPEC CPU Benchmark | RISC-V, C910, SPEC, benchmark | 1 | 0 |
| [T-HEAD_XuanTie_C910.md](hardware_target/T-HEAD_XuanTie_C910.md) | hardware_target | T-HEAD XuanTie C910 | RISC-V, T-Head, XuanTie, high-performance, out-of-order | 1 | 0 |
| [Batched_DGEMM_for_Long_Vector_Architectures.md](optimization_recipe/Batched_DGEMM_for_Long_Vector_Architectures.md) | optimization_recipe | Batched DGEMM for Long Vector Architectures | DGEMM, batched, RISC-V, vector, SeisSol | 1 | 0 |
| [fpga-sdv_RISC-V_Vector_Cluster.md](hardware_target/fpga-sdv_RISC-V_Vector_Cluster.md) | hardware_target | fpga-sdv RISC-V Vector Cluster | RISC-V, vector, FPGA, BSC | 1 | 0 |
| [GEMM_with_RISC-V_Vector_Extension.md](workload_kernel/GEMM_with_RISC-V_Vector_Extension.md) | workload_kernel | GEMM with RISC-V Vector Extension | GEMM, RISC-V, vector, BLAS, floating-point | 1 | 0 |
| [Ara_simulator.md](hardware_target/Ara_simulator.md) | hardware_target | Ara Simulator | RISC-V, vector, simulator, PULP | 1 | 0 |
| [Vector_RISC-V_DIMC_Architecture.md](hardware_target/Vector_RISC-V_DIMC_Architecture.md) | hardware_target | Vector RISC-V DIMC Architecture | RISC-V, DIMC, Vector, AI, accelerator | 1 | 0 |
| [Kendryte_K210.md](hardware_target/Kendryte_K210.md) | hardware_target | Kendryte K210 | RISC-V, SoC, NPU, edge_AI | 1 | 0 |
