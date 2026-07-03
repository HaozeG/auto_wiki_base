---
canonical_name: Tenstorrent Grayskull e75 MatMul Performance
aliases:
- Grayskull e75 MatMul benchmark
- Tenstorrent Grayskull e75 MatMul
- Grayskull e75 MatMul characterization
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e75
workloads:
- MatMul
datatypes:
- BF16
- FP16
metrics:
- TFLOPs
- TFLOPs/Watt
toolchains: []
hardware_versions:
- Grayskull e75 (12nm process, 1 GHz, 96 Tensix cores, 8 GB LPDDR4, 102.4 GB/s bandwidth)
software_versions: []
measurement_method: Benchmarking matrix multiplication (MatMul) kernels on Tenstorrent
  Grayskull e75 under various grid sizes, matrix dimensions, data formats, and numerical
  precision. Performance and power measurements are compared against Intel Sapphire
  Rapids processors, NVIDIA V100 GPU, and NVIDIA A100 GPU.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/f44e7b65c26d8ecf.md
- https://arxiv.org/html/2505.06085
source_url: https://arxiv.org/html/2505.06085
fetched_at: '2026-07-02T12:52:42.038603+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Tenstorrent Grayskull e75 MatMul Performance

The Tenstorrent Grayskull e75 is a RISC-V based accelerator card fabricated on a 12nm process, operating at 1 GHz, with 96 Tensix cores arranged in a grid, 8 GB of LPDDR4 memory (102.4 GB/s bandwidth), and a peak theoretical performance of 55 TFLOPs for FP16 operations. This benchmark result characterizes its matrix multiplication (MatMul) performance for workloads typical of Large Language Model (LLM) computations, specifically evaluating throughput and energy efficiency across different matrix dimensions, grid sizes, data formats, and numerical precision. The evaluation, conducted by researchers from the University of Bologna and Cineca, compares Grayskull e75 against Intel Sapphire Rapids processors, NVIDIA V100 GPU, and NVIDIA A100 GPU. The key finding is that while NVIDIA GPUs dominate raw performance, the Grayskull e75 achieves a competitive trade-off between power consumption and computational throughput, with a peak efficiency of 1.55 TFLOPs/Watt when using BF16. The study also reveals a significant performance difference between the first execution of a kernel and subsequent executions: first-run time is dominated by matrix tiling (31%) and kernel compilation (66%), while subsequent runs are dominated by data transfer time (62%).

## Key Claims

- Peak performance of 55 TFLOPs for floating-point 16 on Grayskull e75.
- Peak efficiency of 1.55 TFLOPs/Watt with BF16 data format.
- First execution of a MatMul kernel is dominated by tiling (31% of time) and kernel compilation (66% of time).
- Subsequent executions are dominated by data transfer time (62% of time).
- Grayskull e75 shows a competitive performance-per-watt trade-off compared to Intel Sapphire Rapids and NVIDIA GPUs.
- The accelerator is well-suited for LLM MatMul workloads due to its graph-based architecture that overlaps computation and communication.

## Measurement Context

- Hardware version: Tenstorrent Grayskull e75 (12nm, 1 GHz, 96 Tensix cores, 8 GB LPDDR4, 102.4 GB/s bandwidth).
- Software/toolchain version: Not specified in the paper; likely TT-Forge or custom kernels.
- Workload shape: Matrix multiplication (MatMul) with varying matrix dimensions, processor grid sizes, data formats (BF16, FP16), and numerical precision.
- Metric: TFLOPs (raw throughput) and TFLOPs/Watt (energy efficiency).
- Method: Benchmarking MatMul kernel execution with performance counters and power measurements; first-run and subsequent-run timings analyzed separately.
- Evidence strength: measured (experimental characterization from a peer-reviewed research paper).

## Relationships

- [[jacobi-stencil-grayskull-e150-vs-xeon-platinum]]: related via shared bf16, grayskull, tenstorrent.

- [[pulp-nn-optimization-recipe]]: Both this benchmark and PULP-NN address MatMul efficiency on RISC-V platforms, with Grayskull focusing on hardware acceleration and PULP-NN on software-level kernel optimization for quantized neural networks.
- [[cpa-factored-gemmini-systolic-array]]: While CPA-factored Gemmini optimizes systolic array hardware for RISC-V, the Grayskull accelerator employs a different architecture (Tensix cores) but targets similar AI workloads, providing complementary performance data.
- [[earth-shifting-based-vector-memory-access]]: Memory access optimizations like EARTH are relevant to data movement patterns that dominate subsequent-run execution on Grayskull (62% data transfer time).

## Sources

- [Assessing Tenstorrent’s RISC-V MatMul Acceleration Capabilities](https://arxiv.org/html/2505.06085) (arXiv:2505.06085)
