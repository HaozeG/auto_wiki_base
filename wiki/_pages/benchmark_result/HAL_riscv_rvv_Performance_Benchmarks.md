---
cold_start: true
created: '2025-07-09'
datatypes: []
evidence_strength: reported
hardware_targets:
- SpacemiT KeyStone K1
hardware_versions:
- SpacemiT KeyStone K1 (256-bit RVV 1.0) on MUSE Pi board
inbound_links: 0
measurement_method: Single-core performance tests using OpenCV's own performance test
  suite at 1920×1080 image size on SpacemiT MUSE Pi board with SpacemiT toolchain
  1.0.5. Multithreading disabled to isolate RVV 1.0 core capability.
metrics:
- performance uplift (mean)
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- OpenCV 4.12
sources:
- https://opencv.org/introducing-hal-riscv-rvv-unleashing-the-power-of-risc-v-cpus-with-rvv-1-0/
tags:
- OpenCV
- HAL
- RVV 1.0
- RISC-V
- benchmark
- SpacemiT
toolchains:
- SpacemiT toolchain 1.0.5
- GCC
- Clang
type: benchmark_result
updated: '2026-06-28'
workloads:
- OpenCV image processing kernels (119 functions)
---

# HAL riscv-rvv Performance Benchmarks

The HAL riscv-rvv benchmark documents single-core performance uplift of OpenCV functions when accelerated with RVV 1.0 on the SpacemiT KeyStone K1 CPU (256-bit RVV 1.0) on a MUSE Pi board. Tests were conducted using OpenCV's own performance test suite at 1920×1080 image size with the SpacemiT toolchain 1.0.5. The mean performance uplift across 119 functions in the core and imgproc modules exceeded 200%. The functions cover basic math operations (div, exp, log, sqrt, norm, meanStdDev), transformations (transpose, flip, split, merge), and image processing (cvtColor, filters, median blur, resize, warpAffine, warpPerspective, remap). The benchmark aims to showcase the single-core RVV 1.0 capability; multithreading was disabled to isolate the vector extension's contribution.

## Key Claims

- Mean single-core performance uplift >200% across 119 OpenCV functions.
- Hardware: SpacemiT KeyStone K1 (256-bit RVV 1.0) on MUSE Pi board with 8 cores (single-core tested).
- Image resolution: 1920×1080.
- Toolchain: SpacemiT toolchain 1.0.5 (both GCC and Clang tested).
- Performance gain varies per operation; larger gains indicate full utilization of RVV 1.0.
- Smaller gains can occur when the baseline is already well-optimized by the compiler.
- Functions include basic math, transformation, and image processing categories.

## Measurement Context

- Hardware version: SpacemiT KeyStone K1 (256-bit RVV 1.0) on MUSE Pi board.
- Software/toolchain version: OpenCV 4.12, SpacemiT toolchain 1.0.5 (GCC and Clang cross-compilation).
- Workload shape: 119 OpenCV functions in core and imgproc modules; 1920×1080 image input.
- Metric: Performance uplift (mean percentage improvement over baseline).
- Method: Single-core tests using OpenCV's performance test suite; multithreading disabled.
- Evidence strength: reported (blog post from OpenCV China team, not independently verified measurements).

## Relationships

- [[HAL_riscv_rvv_OpenCV_Optimization_Recipe]] – The optimization recipe describing how to build and use the HAL that produced these benchmarks.
- [[Gemmini_systolic_array_GEMM_accelerator]] – Another RISC-V accelerator with benchmark results, providing contrast between vectorized and dedicated hardware approaches.

## Sources

- [OpenCV Blog: Introducing HAL riscv-rvv](https://opencv.org/introducing-hal-riscv-rvv-unleashing-the-power-of-risc-v-cpus-with-rvv-1-0/)

