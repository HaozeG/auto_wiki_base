---
canonical_name: RVV Matrix Multiplication Example (Double Precision)
aliases:
- RVV matmul example
- Vectorized matrix multiplication with vfredusum
- Matmul RVV intrinsics example
subtype: null
tags:
- RVV
- matrix multiplication
- example
workloads:
- Matrix multiplication (naive)
datatypes:
- float64
constraints:
- RVV 1.0
- row-major memory layout
- unit stride for A and C
- strided column load (vlse64) for B
- reduction sum using vfredusum
- tail undisturbed (tu) policy for vfmacc
scorecard:
  novelty_delta: 0.5
  claim_density: 0.2
  self_containedness: 0.7
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/abad810c497b3561.md
- https://docs.riscv.org/reference/vector-c-intrinsics/v1.0/rvv-intrinsic-examples.html
source_url: https://docs.riscv.org/reference/vector-c-intrinsics/v1.0/rvv-intrinsic-examples.html
fetched_at: '2026-07-02T09:55:19.656350+00:00'
type: workload_kernel
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# RVV Matrix Multiplication Example (Double Precision)

The RVV matrix multiplication example demonstrates a naive double-precision matrix multiplication (C = A x B) implemented using RISC-V Vector (RVV) intrinsics as specified in the RISC-V Ratified Vector Extension specification, version 1.0. It uses `vfloat64m1_t` vector registers and a reduction sum via `__riscv_vfredusum` to accumulate partial dot products across vector lanes. The implementation employs the `__riscv_vlse64` strided load instruction for column access of matrix B, and uses the tail undisturbed (tu) policy for the `__riscv_vfmacc` multiply-accumulate operation to preserve accumulator state across incomplete vector lengths. This kernel serves as a baseline for vectorized matrix multiplication on RVV 1.0 hardware, targeting arbitrary shapes defined by dimensions `n`, `m`, and `p` with unit stride for row-major data layout on matrices A and C. The example is non-normative and makes no claims about efficiency, but illustrates the use of RVV intrinsics for a core linear algebra operation fundamental to AI and scientific computing workloads.

## Key Claims

- The kernel implements naive matrix multiplication C[n][m] = A[n][p] * B[p][m] using double-precision arithmetic.
- Vector row-column dot products are computed with partial accumulation in `vfloat64m1_t` registers, followed by a final reduction sum (`vfredusum`).
- The implementation uses a strided load (`vlse64`) with stride `sizeof(double) * m` to access columns of B in row-major memory.
- The vector length is dynamically adapted using `__riscv_vsetvl`, and the `tu` (tail undisturbed) policy preserves already-computed partial sums when `vl < vlmax`.
- The kernel is provided as a non-normative reference example; no performance claims are made.

## Kernel Shape

- Operation: C[i][j] = Σ_k A[i][k] * B[k][j]
- Shapes: n, m, p (arbitrary positive integers)
- Datatypes: float64 (double precision)
- Layout: Row-major for all matrices
- Sparsity: Dense (full)
- Baseline implementation: Provided in the source as a reference C loop nest (`matmul_reference`).

## Relationships

- [[sifive-intelligence-x160-gen-2]]: Hardware target supporting RVV 1.0, suitable for executing this kernel.
- [[xuantie-c950]]: A RISC-V processor with potential RVV support; this kernel could be adapted for benchmarking.
- Insufficient context for additional cross-links; no existing workload_kernel pages in the wiki.

## Sources

- [RISC-V Vector Intrinsics Examples Specification](https://docs.riscv.org/reference/vector-c-intrinsics/v1.0/rvv-intrinsic-examples.html)
