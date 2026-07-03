---
canonical_name: OpenGeMM
aliases:
- Open GeMM
- OpenGeMM accelerator
- RVV GEMM Progressive Optimization Benchmark on Banana Pi F3 (SpaceMit K1)
- rvv-gemm benchmark
- AlexanderGSC rvv-gemm results
- BPI-F3 GEMM optimization study
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/1fd2befcfc900c4c.md
- https://arxiv.org/abs/2411.09543
- raw/cache/f6f6ff098eb28eaa.md
- https://github.com/AlexanderGSC/rvv-gemm
source_url: https://arxiv.org/abs/2411.09543
fetched_at: '2026-07-02T03:52:48.156844+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: riscv_gemm_optimization_approaches
  reason: a synthesis page comparing this dedicated-hardware-generation approach against
    compiler-generated RVV code (MLIR+xDSL), hand-tuned assembly (XuanTie C908 kernel),
    and cross-architecture template-based micro-kernels
---

# OpenGeMM

OpenGeMM is an open-source generic matrix multiplication (GeMM) accelerator platform that combines a parameterized Chisel-coded GeMM accelerator, a lightweight RISC-V processor, and a tightly coupled multi-banked scratchpad memory. Designed for extreme edge devices, it aims to overcome the inflexibility of standalone accelerators and the low utilization of RISC-V-coupled accelerator platforms. OpenGeMM achieves high hardware utilization and system efficiency through three key mechanisms: configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access. It is configurable and programmable, supporting diverse CNN and Transformer workloads, and achieves reusable acceleration without sacrificing performance.

## Key Claims

- Hardware utilization ranges from 81.89% to 99.34% across CNN and Transformer workloads.
- Demonstrates 3.58x to 16.40x speedup over the state-of-the-art Gemmini accelerator on normalized throughput.
- Achieves 4.68 TOPS/W system efficiency.
- Implements configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access to boost utilization and efficiency.
- Open-source, parameterized Chisel implementation enables configurability and programmability.

## Relationships

- [[xuantie_c908_fp16_gemm_kernel]] – a related GEMM kernel targeting a different hardware platform (XuanTie C908).
- [[mlir_xdsl_rvv_gemm_codegen_recipe]] – an alternative approach to optimizing GEMM for RISC-V vector processors using MLIR/xDSL.
- [[riscv_gemm_optimization_approaches]]: a synthesis page comparing this dedicated-hardware-generation approach against compiler-generated RVV code (MLIR+xDSL), hand-tuned assembly (XuanTie C908 kernel), and cross-architecture template-based micro-kernels.

## Sources

- https://arxiv.org/abs/2411.09543
