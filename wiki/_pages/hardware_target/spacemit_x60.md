---
canonical_name: SpacemiT X60
aliases:
- X60
- SpacemiT X60 RISC-V processor
subtype: null
tags:
- RISC-V
- SpacemiT
- LLVM
hardware_targets:
- SpacemiT X60
toolchains:
- LLVM
constraints:
- in-order
- 8-core
- RVA22U64 profile
- RVV 1.0
- 256-bit vectors
- Banana Pi BPI-F3 board
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.5
sources:
- raw/cache/e33233e6a6f364e1.md
- https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
source_url: https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
fetched_at: '2026-07-02T04:33:14.593320+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 4
needs_summary_revision: false
---

# SpacemiT X60

The SpacemiT X60 is an in-order, 8-core RISC-V processor that implements the RVA22U64 profile and supports the RISC-V Vector Extension 1.0 (RVV) with 256-bit vectors. It is the system-on-chip at the heart of the Banana Pi BPI-F3 single-board computer, and its scheduling behavior was the subject of a detailed LLVM optimization project that resulted in significant SPEC CPU 2017 performance improvements. The processor's design emphasizes efficient vector processing and integer operations, making it a target for compiler optimization work aimed at reducing the performance gap between LLVM and GCC for RISC-V.

## Key Claims

- In-order, 8-core RISC-V processor implementing RVA22U64 and RVV 1.0 with 256-bit vectors.
- Used in the Banana Pi BPI-F3 board.
- Subject of a 10-month RISE project that built a full LLVM scheduling model, requiring microbenchmarking of 201 scalar, 82 FP, and 9185 RVV instruction combinations.
- LLVM scheduling model alone yielded up to 16.8% execution time improvement on 538.imagick_r, with no regressions.
- Combined with vectorization across calls and IPRA support, overall SPEC CPU 2017 improvement reached up to 16%.

## Optimization-Relevant Details

- ISA/profile: RVA22U64, RVV 1.0
- Vector/matrix/accelerator support: 256-bit RVV vectors
- Memory/cache/TLB/DMA: not specified
- Compiler/toolchain support: LLVM, GCC

## Relationships

- [[llvm_riscv_target]]: The LLVM RISC-V backend that received the scheduling model and other patches targeting this processor.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: Another optimization recipe targeting the same Banana Pi F3 board, though with a different code generation approach using MLIR and xDSL for GEMM micro-kernels.
- [[spacemit_x60_llvm_spec_cpu2017_benchmark]]: The detailed SPEC CPU 2017 measurement results from the LLVM scheduling/vectorization/IPRA work on this core.
- [[compiler_benchmark_bananapi_f3_gcc15_clang21]]: A GCC 15 vs. Clang 21 autovectorization comparison (SGEMM, DGEMM, Qsim) on this same SoC/board.

## Sources

- https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
