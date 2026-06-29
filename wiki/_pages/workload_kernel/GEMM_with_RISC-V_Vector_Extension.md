---
cold_start: false
constraints:
- Arbitrary matrix sizes (M, N, K)
- No transpose, alpha, or beta support (initial implementation)
created: '2025-03-04'
datatypes:
- double-precision (f64)
- single-precision (f32)
- half-precision (f16)
inbound_links: 21
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://www.luffca.com/2023/02/gemm-riscv-vector-part1/
tags:
- GEMM
- RISC-V
- vector
- BLAS
- floating-point
type: workload_kernel
updated: '2026-06-28'
workloads:
- GEMM
---

# GEMM with RISC-V Vector Extension

The GEMM (General Matrix Multiply) kernel implemented with the RISC-V Vector Extension targets CBLAS-compatible matrix multiplication (C = alpha * op(A) * op(B) + beta * C) for double-precision, single-precision, and half-precision floating-point data. The implementation described in Part 1 of the Luffca blog supports arbitrary matrix sizes (M, N, K) but does not include transposition, alpha, or beta scaling. The kernel is designed to run on the Ara RTL simulator, evaluating performance using the vector processing units. Baseline implementation is derived from the Netlib cblas_dgemm prototype.

## Key Claims

- Supports double-precision (dgemm), single-precision (sgemm), and half-precision (hgemm) floating-point matrix multiplication.
- Arbitrary matrix sizes are supported; kernel handles any M, N, K values.
- Initial implementation does not support transpose, alpha, or beta parameters.
- Performance evaluated on Ara's 4-lane (256-bit) configuration yields high utilization (>95% for double-precision, >85% for half-precision).
- Poor utilization observed for odd matrix sizes, especially for single-precision (drops to ~50% at size 65).

## Kernel Shape

- Operation: C = alpha * op(A) * op(B) + beta * C
- Shapes: op(A) = M x K, op(B) = K x N, C = M x N
- Datatypes: double-precision (f64), single-precision (f32), half-precision (f16)
- Layout: Row-major (CBLAS_LAYOUT not specified; assumed CblasRowMajor)
- Sparsity: Dense
- Baseline implementation: Reference cblas_dgemm from Netlib, adapted for RISC-V Vector

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V platforms, though different application domains.
- (Insufficient context for additional cross-links)

## Sources

- [GEMM based on the RISC-V Vector Extension (Part 1) - Luffca](https://www.luffca.com/2023/02/gemm-riscv-vector-part1/)

