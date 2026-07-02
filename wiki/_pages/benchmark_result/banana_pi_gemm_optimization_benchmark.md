---
canonical_name: riscv-gemm-optimization (Babar Hussain)
aliases:
- RISC-V GEMM optimization
- BabarHussain786/riscv-gemm-optimization
subtype: null
tags: []
hardware_targets:
- Banana Pi Board
workloads:
- gemm (matrix multiplication)
datatypes:
- fp32
metrics:
- time (seconds)
- speedup (vs baseline)
toolchains:
- gcc-riscv64-linux-gnu
hardware_versions: []
software_versions:
- GCC -O3 -march=rv64imac -mabi=lp64
measurement_method: perf stat -e L1-dcache-loads,L1-dcache-load-misses
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/95638c3e198ad6b9.md
- https://github.com/BabarHussain786/riscv-gemm-optimization
source_url: https://github.com/BabarHussain786/riscv-gemm-optimization
fetched_at: '2026-07-02T03:54:54.399713+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Banana Pi GEMM Optimization Benchmark

This benchmark report presents measured execution times and speedups for various matrix multiplication (GEMM) optimizations on a Banana Pi board running a RISC-V platform. The implementations were compiled with the RISC-V GCC toolchain (cross-compiler `gcc-riscv64-linux-gnu`) using `-O3` optimization and the `rv64imac` architecture target. The baseline is a naive triple-loop matrix multiplication; optimized variants include loop interchange, recursive divide-and-conquer, tiling, OpenMP parallelization, and RISC-V Vector Extension (RVV) auto-vectorization. Timing was collected using Linux `perf stat` for cache event profiling. The results demonstrate that loop interchange yields the largest speedup (41.5x) on a 4096×4096 matrix, underscoring the importance of cache locality on RISC-V hardware without out-of-order execution. The project was developed at the University of Salerno's HPC course and is maintained on GitHub under the repository `BabarHussain786/riscv-gemm-optimization`.

## Key Claims

- Baseline naive GEMM on 4096×4096 matrices takes 15755.16 seconds on the Banana Pi board.
- Loop interchange optimization achieves a 41.5× speedup over baseline, reducing execution time to 379.62 seconds.
- Recursive multiplication with block size 128 achieves a 9.2× speedup (1712.26 seconds).
- Tiled OpenMP parallelization on 1024×1024 matrices achieves a 13.1× speedup (17.21 seconds).
- RVV auto-vectorization (RVV2 recursive) yields a variable speedup between 1.0× and 2.6× on the same 4096×4096 workload.
- Compiler optimization flags, particularly -O3, significantly impact performance.
- Algorithm-architecture synergy (tiling, recursion) effectively exploits the RISC-V memory hierarchy.
- OpenMP and RVV extensions scale well on multi-core RISC-V chips.

## Measurement Context

- Hardware version: Banana Pi Board (exact model unspecified, claims use of real RISC-V hardware)
- Software/toolchain version: gcc-riscv64-linux-gnu, compiled with `-O3 -march=rv64imac -mabi=lp64`
- Workload shape: 4096×4096 square matrices for most tests; 1024×1024 for the Tiled OpenMP variant
- Metric: Wall-clock time in seconds; speedup factor relative to baseline
- Method: Execution on real hardware with timing via `perf stat -e L1-dcache-loads,L1-dcache-load-misses`; detailed methodology available in the project's Final Report PDF
- Evidence strength: reported (project README and accompanying report)

## Relationships

- The benchmarks complement the MLIR+xDSL code generation recipe for RVV GEMM micro-kernels on similar hardware: [[mlir_xdsl_rvv_gemm_codegen_recipe]]
- Results can be compared with the hand-tuned XuanTie C908 FP16 GEMM kernel, which targets a different RISC-V core and datatype: [[xuantie_c908_fp16_gemm_kernel]]

## Sources

- https://github.com/BabarHussain786/riscv-gemm-optimization
