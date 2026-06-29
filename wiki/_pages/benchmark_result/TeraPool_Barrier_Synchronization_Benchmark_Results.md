---
cold_start: true
created: '2025-07-10'
datatypes: []
evidence_strength: reported
hardware_targets:
- TeraPool (1024 RISC-V processors, non-uniform memory access, 4MB shared L1 data
  memory)
hardware_versions:
- TeraPool cluster (core microarchitecture not specified in abstract)
inbound_links: 0
measurement_method: Empirical benchmarking of optimized tree barrier implementations
  against a naive central counter barrier on the TeraPool cluster; results for parallel
  kernels and a 5G application reported in the paper.
metrics:
- synchronization overhead (%)
- speedup
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.7
software_versions: []
sources:
- https://arxiv.org/abs/2307.10248
tags:
- RISC-V
- TeraPool
- barrier synchronization
- many-core
- shared memory
toolchains: []
type: benchmark_result
updated: '2026-06-29'
workloads:
- signal-processing and telecommunications parallel kernels (FFT, MATMUL)
- 5G application
- 4×16 FFTs of 4096 points
- MATMUL (32×64 × 64×4096)
---

# TeraPool Barrier Synchronization Benchmark Results

This page reports benchmark results for barrier synchronization on the TeraPool cluster, a many-core system comprising 1024 RISC-V processors with non-uniform memory access to a tightly coupled 4 MB shared L1 data memory. The paper "Fast Shared-Memory Barrier Synchronization for a 1024-Cores RISC-V Many-Core Cluster" (arXiv:2307.10248) evaluates multiple barrier implementations in the context of a fork-join OpenMP-style programming model. Workloads include signal-processing and telecommunications parallel kernels, specifically 4×16 FFTs of 4096 points and a matrix multiplication (MATMUL) between a 32×64 and a 64×4096 matrix, as well as a representative 5G application. Measurement context: hardware target is the TeraPool cluster (core microarchitecture unspecified in the abstract); metrics include synchronization overhead as a percentage of total runtime and speedup relative to a naive central counter barrier. The method involves empirical benchmarking of optimized tree barriers, with evidence strength classified as reported.

## Key Claims

- Synchronization overhead remains below 10% of total runtime for problems fitting the 4 MB L1 data memory.
- Fine-tuned tree barriers achieve a 1.6× speed-up over a naive central counter barrier.
- On a typical 5G application, the overhead is only 6.2%, even with a challenging multistage synchronization kernel.
- This is the first known work demonstrating shared-memory barrier synchronization for a thousand processing elements tightly coupled to shared data memory.

## Measurement Context

- **Hardware version:** TeraPool cluster (1024 RISC-V processors, non-uniform memory access, 4 MB shared L1 data memory). The specific RISC-V core microarchitecture is not disclosed in the abstract.
- **Software/toolchain version:** Not specified in the available resource.
- **Workload shape:** Parallel kernels from signal processing and telecommunications: 4×16 FFTs of 4096 points; MATMUL with dimensions 32×64 × 64×4096; and a multistage 5G application kernel.
- **Metric:** Synchronization overhead (percentage of total runtime), speedup (relative to central counter barrier).
- **Method:** Empirical comparison of optimized tree barrier implementations against a central counter barrier, executed on the TeraPool cluster. Details of the measurement methodology are described in the paper.
- **Evidence strength:** reported (based on claims in the preprint; independent verification not available in extracted content).

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – An optimization recipe for parallel GEMM-based convolution on the GAP8 RISC-V platform, involving synchronization and parallelization on a different many-core architecture.
- [[T-SAR_Benchmark_Results]] – Benchmark results for ternary LLM inference on CPUs, providing a contrasting workload and measurement context.

## Sources

- [arXiv:2307.10248](https://arxiv.org/abs/2307.10248)

