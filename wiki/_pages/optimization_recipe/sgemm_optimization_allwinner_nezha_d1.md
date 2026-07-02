---
canonical_name: SGEMM Optimization on Allwinner Nezha D1
aliases:
- Nezha D1 SGEMM
- Allwinner Nezha D1 GEMM optimization
- RISC-V SGEMM optimization blog
subtype: null
tags:
- sgemm
- riscv
- optimization
- allwinner
- nezha-d1
hardware_targets:
- Allwinner Nezha D1
workloads:
- sgemm
datatypes:
- fp32
metrics:
- GFLOPS
- memory bandwidth (GB/s)
toolchains:
- RISC-V cross-compilation toolchain
constraints:
- RISC-V Vector (RVV) extension instructions
evidence_strength: measured
scorecard:
  novelty_delta: 0.85
  claim_density: 0.75
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/aafb776bc14e7ecd.md
- https://zhao-dongyu.github.io/2024/02/26/103_sgemm_riscv_en/
source_url: https://zhao-dongyu.github.io/2024/02/26/103_sgemm_riscv_en/
fetched_at: '2026-07-02T03:53:49.067125+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SGEMM Optimization on Allwinner Nezha D1

This optimization recipe documents a step-by-step SGEMM (single-precision general matrix multiply) optimization project targeting the Allwinner Nezha D1 RISC-V development board that uses the XuanTie C906 core with RVV vector support. The project implements nine versions (0 through 9) of the GEMM kernel, starting from a naive triple-loop baseline through loop interchange and blocking (versions 0–2) and culminating in hand-tuned assembly using RISC-V Vector (RVV) extension instructions (versions 6–9). Benchmarks were conducted on the Nezha D1, which has a theoretical peak of 4 GFLOPS at 1 GHz and a measured memory bandwidth of 2.592 GB/s (DDR3 at 792 MHz). Performance measurements are reported for each version, with the naive version achieving only 0.03 GFLOPS and significant improvements through tiling and vectorization. The recipe includes prerequisites (RISC-V cross-compilation toolchain, familiarity with cache hierarchy), step-by-step transformation descriptions, expected performance effects, common failure modes such as poor spatial locality, and detailed measurement data with roofline analysis.

## Key Claims

- Naive SGEMM (ijk loop order, row-major) achieves 0.03 GFLOPS on the Allwinner Nezha D1 board against a theoretical peak of 4 GFLOPS.
- Loop interchange (kij order) improves performance to 0.180 GFLOPS for square matrices of size 512, demonstrating better spatial locality for matrix B.
- Blocking (tiling) with sub-block size 4×4 further reduces cache misses and improves utilization.
- Measured memory bandwidth is 2.592 GB/s (floating-point load) versus a reported value of 2.727 GB/s from OpenPPL.
- Versions 6 through 9 incorporate assembly-coded RVV vector instructions, achieving higher throughput than the C-only implementations.
- Performance fluctuates at matrix sizes that are multiples of 32 (e.g., 128, 164, 192), likely due to cache line (64 B) and hardware prefetcher interactions.

## Transformation

- **Prerequisites:** Allwinner Nezha D1 board with XuanTie C906 core, RISC-V cross-compilation toolchain (GCC with RVV support), Makefile-based build system, and basic understanding of GEMM and memory hierarchy.
- **Steps:**
  1. **Version 0 – Naive:** Implement triple-nested loop with `i, j, k` order. Performance: 0.03 GFLOPS on 512×512 matrices; spatial locality is poor due to column-major access of matrix B.
  2. **Version 1 – Loop Interchange:** Reorder loops to `k, j, i` (or other permutations) to improve cache reuse for matrix B. Performance climbs to 0.180 GFLOPS for the MKN order on size 512.
  3. **Version 2 – Blocking:** Add outer loops that tile the M and N dimensions (using `DGEMM_MR` and `DGEMM_NR` constants, here 4×4) and call a micro-kernel `AddDot_4x4_opt`. This increases temporal locality.
  4. **Versions 3–5:** Further C-level optimizations (not detailed in source, but implied as iterative improvements).
  5. **Versions 6–9:** Replace inner kernel with handwritten assembly using RVV vector load/store instructions (vle, flw, vlw) and vector arithmetic, targeting the D1’s vector unit to saturate the memory bandwidth and compute pipeline.
- **Expected effect:** Steady performance improvement from 0.03 GFLOPS toward the 4 GFLOPS theoretical ceiling, limited by memory bandwidth and vector instruction throughput.
- **Failure modes:** Excessive cache misses due to poor loop ordering; hardware prefetcher thrashing at certain matrix dimensions (differences of 32 elements correspond to 128 B strides); insufficient vector register usage or instruction scheduling stalls in assembly kernels.
- **Measurements:**
  - Naive: 0.03 GFLOPS (size 512).
  - Loop interchange best (MKN order): 0.180 GFLOPS.
  - Blocking version: Not reported explicitly in source but expected >0.180 GFLOPS.
  - Memory bandwidth test: 2.592 GB/s (floating-point load) vs. theoretical 2.727 GB/s (DDR3 792 MHz).

## Relationships

- The general GEMM kernel design and optimization techniques relate to [[xuantie_c908_fp16_gemm_kernel]], which uses a similar outer-product approach on a different hardware target.
- The use of compiler-based RVV code generation for GEMM is explored in [[mlir_xdsl_rvv_gemm_codegen_recipe]], offering an alternative to hand-tuned assembly.

## Sources

- https://zhao-dongyu.github.io/2024/02/26/103_sgemm_riscv_en/
