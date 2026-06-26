---
type: entity
tags: [apple, matrix-coprocessor, ml-acceleration, arm, simd]
sources:
  - https://research.meekolab.com/the-elusive-apple-matrix-coprocessor-amx
  - https://www.corsix.org/content/contrasting-intel-amx-and-apple-amx
  - https://github.com/corsix/amx
  - https://commit.csail.mit.edu/papers/2025/Jonathan_Zhou_SB_Thesis.pdf
  - https://arxiv.org/pdf/2502.05317
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Apple AMX (Apple Matrix Coprocessor)

Apple AMX (Apple Matrix Coprocessor) is a proprietary matrix multiply coprocessor embedded in Apple Silicon SoCs starting with the A12X Bionic (2018) and present in every M-series chip through at least M4. It is exposed as undocumented arm64 ISA extensions — no official Apple documentation exists — and has been characterized through reverse engineering by the open-source community. AMX operates as a separate execution unit alongside the CPU cores, maintaining its own register file: two 512-byte registers (X and Y, each comprising 8 × 64-byte rows) and one 4 096-byte accumulator register (Z, 64 × 64-byte rows). The Z register forms a 32 × 32 grid of compute units; each unit performs 16-bit FMA, each 2 × 2 sub-grid can perform 32-bit FMA, and each 4 × 4 sub-grid can perform 64-bit FMA. AMX instructions compute outer-product accumulations between selected X and Y rows, writing into Z. The primary user-facing interface is Apple's Accelerate framework (BLAS/LAPACK), which dispatches AMX instructions automatically; no public API exists for direct AMX access. AMX coexists with ARM SME in later chips and historically preceded it — ARM SME was standardized in part to replace proprietary coprocessors like AMX with an architecturally documented equivalent.

## Key Claims

- AMX is undocumented in Apple's public developer documentation; all instruction semantics have been obtained through reverse engineering, primarily by Dougal Johnson and the corsix/amx project.
- The AMX register file consists of two 512-byte X/Y registers (8 × 64-byte rows each) and one 4 096-byte Z accumulator (64 × 64-byte rows), with the Z grid providing a 32 × 32 array of compute units capable of 16-bit, 32-bit, or 64-bit FMA depending on sub-grid granularity.
- Two AMX versions exist: AMX1 in A-series chips (7-bit writemasks) and AMX2 in M-series chips from M1 onward (9-bit writemasks); M2 added bf16 support; M3 added extra modes to load and integer-matrix instructions.
- Each M1 chip has one AMX unit per CPU cluster (one P-cluster unit, one E-cluster unit); M1 Pro/Max double the P-cluster count to two P-AMX units.
- The M1 AMX achieves approximately 1.9 TFLOPS (FP32) via Accelerate/NumPy, roughly 2× the throughput of ARM NEON SIMD on the same chip.
- Apple's Accelerate framework (BLAS/LAPACK) is the canonical software path to AMX; it outperforms OpenBLAS on medium-to-large matrix sizes because OpenBLAS falls back to NEON.
- Energy efficiency scales strongly across generations: M1 reaches ~56 GFLOPs/Watt (single-batch GEMM), M2 Pro ~369 GFLOPs/Watt, and M4 Pro exceeds 700 GFLOPs/Watt on batched workloads.

## Relationships

- [[arm_sme]]: ARM SME is the architecturally documented successor concept to proprietary coprocessors like AMX; Apple began implementing SME in M4-class chips as a complement or eventual replacement.
- [[arm_sve2]]: AMX and SVE2 coexist on Apple Silicon; AMX handles matrix outer-products while SVE2/NEON handle general vector operations.
- [[apple_neural_engine]]: AMX handles general-purpose GEMM (floating-point, scientific); the Apple Neural Engine handles fixed-function ML inference. Both are present on M-series SoCs but serve different workload profiles.

## Sources

- corsix/amx GitHub repository and blog post (primary reverse-engineering reference for register layout and instruction semantics)
- Jonathan Zhou, "Performance Analysis of the Apple AMX Matrix Accelerator," MIT CSAIL SB Thesis, 2025 — TFLOPS and efficiency numbers
- "Apple vs. Oranges: Evaluating the Apple Silicon M-Series SoCs for HPC," arXiv 2502.05317 — generational GFLOPs/Watt data
- "The Elusive Apple Matrix Coprocessor (AMX)," research.meekolab.com — architectural overview and versioning history
- Apple Developer: Accelerate framework overview — software access path
