---
cold_start: false
constraints:
- long vector architectures
- cross-platform portability
created: '2025-03-04'
datatypes:
- double-precision
evidence_strength: measured
hardware_targets:
- fpga-sdv cluster
inbound_links: 0
metrics:
- speedup factor
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/html/2501.06175v1
tags:
- DGEMM
- batched
- RISC-V
- vector
- SeisSol
toolchains:
- Clang (BSC modified)
type: optimization_recipe
updated: '2026-06-28'
workloads:
- batched DGEMM
- SeisSol-proxy
---

# Batched DGEMM for Long Vector Architectures

This optimization technique introduces a batched DGEMM library written in plain C for long vector architectures, specifically targeting RISC-V systems with the vector extension. The library is designed to be cross-platform portable, avoiding micro-architecture-specific code such as compiler intrinsics. It addresses the limitation of standard BLAS libraries (OpenBLAS, BLIS, Eigen) in leveraging long vector registers when processing many small matrix multiplications typical of scientific codes like SeisSol. The expected effect is a significant performance improvement, with measured speedups ranging from 3.5× to 32.6× on the fpga-sdv cluster compared to reference implementations. Potential failure modes include lack of portability if intrinsics are used, but the plain C approach mitigates this.

## Key Claims

- A batched DGEMM library in plain C achieves speedups of 3.5× to 32.6× over reference BLAS implementations on the fpga-sdv cluster.
- The library is portable across CPU architectures; demonstrated on an Intel CPU with improved execution times.
- The approach integrates into the SeisSol-proxy application without compromising cross-platform compatibility.
- The library avoids platform-specific intrinsics and relies on compiler hints (pragmas) for auto-vectorization.

## Transformation

- Prerequisites: A RISC-V system with vector extension (rvv0.7 or later), a Clang-based compiler supporting auto-vectorization, and the SeisSol-proxy application.
- Steps: 1) Identify small GEMM calls within the application. 2) Batch multiple small GEMM operations into a single function call. 3) Implement the batched kernel in plain C with compiler hints (e.g., `#pragma clang loop vectorize`). 4) Replace individual GEMM calls with the batched interface. 5) Compile with the BSC-modified Clang compiler targeting RISC-V vector extension.
- Expected effect: 3.5× to 32.6× speedup on RISC-V vector hardware; portable performance gains on other architectures.
- Failure modes: If the compiler does not support auto-vectorization, performance may revert to baseline. Inappropriate batching size may reduce effectiveness.
- Measurements: Speedup measured using a custom hardware tracer on the fpga-sdv cluster; results range from 3.5× to 32.6×.

## Relationships

- [[fpga-sdv_RISC-V_Vector_Cluster]] – The hardware target where the optimization was evaluated.
- [[Batched_DGEMM_on_RISC-V_Benchmark_Results]] – The benchmark results associated with this recipe.

## Sources

- [arXiv paper: Batched DGEMMs for scientific codes running on long vector architectures](https://arxiv.org/html/2501.06175v1)
