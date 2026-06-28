---
cold_start: true
constraints:
- RVV 1.0
- 256-bit vector length
- single-core
created: '2025-07-09'
datatypes: []
evidence_strength: reported
hardware_targets:
- SpacemiT KeyStone K1
inbound_links: 2
metrics:
- performance uplift (mean)
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://opencv.org/introducing-hal-riscv-rvv-unleashing-the-power-of-risc-v-cpus-with-rvv-1-0/
tags:
- OpenCV
- HAL
- RVV 1.0
- RISC-V
- SpacemiT
toolchains:
- SpacemiT toolchain 1.0.5
- GCC
- Clang
type: optimization_recipe
updated: '2026-06-28'
workloads:
- OpenCV image processing kernels (119 functions)
---

# HAL riscv-rvv OpenCV Optimization Recipe

HAL riscv-rvv is a Hardware Abstraction Layer for OpenCV that replaces performance-critical functions with RVV 1.0 vectorized implementations for RISC-V CPUs. It was introduced in OpenCV 4.12 and covers 119 functions in the core and imgproc modules, including basic math (div, exp, log, sqrt, norm, meanStdDev), transformation (transpose, flip, split, merge), and image processing operations (cvtColor, filters, median blur, resize, warpAffine, warpPerspective, remap). The HAL provides a mean performance uplift exceeding 200% on single-core tests on SpacemiT KeyStone K1 hardware at 1920×1080 image resolution when built with the SpacemiT toolchain 1.0.5. The transformation uses length-agnostic RVV 1.0 intrinsics and is part of OpenCV's Universal Intrinsics abstraction, making the same code portable across vector width configurations.

## Key Claims

- HAL riscv-rvv covers 119 functions in OpenCV core and imgproc modules.
- Single-core performance uplift exceeds 200% mean across all functions at 1920×1080 image size.
- Hardware target: SpacemiT KeyStone K1 (256-bit RVV 1.0) on MUSE Pi board.
- Toolchain used: SpacemiT toolchain 1.0.5 (GCC and Clang supported).
- The HAL leverages RVV 1.0 length-agnostic vector instructions via OpenCV Universal Intrinsics.
- Build requires setting `-DCPU_BASELINE=RVV -DCPU_BASELINE_REQUIRE=RVV -DRISCV_RVV_SCALABLE=ON`.
- Performance gain varies per operation; larger gains indicate full utilization of RVV 1.0.
- The HAL was developed with support from SpacemiT, Chinese Academy of Sciences, and OpenCV China.

## Transformation

- Prerequisites:
  - OpenCV 4.12 or later.
  - A RISC-V CPU supporting RVV 1.0 (e.g., SpacemiT KeyStone K1).
  - Cross-compilation toolchain (SpacemiT toolchain 1.0.5 or compatible GCC/Clang).
- Steps:
  1. Clone OpenCV source from GitHub.
  2. Set up cross-compilation toolchain path.
  3. Run CMake with required flags: `-DCMAKE_BUILD_TYPE=Release -DCPU_BASELINE=RVV -DCPU_BASELINE_REQUIRE=RVV -DRISCV_RVV_SCALABLE=ON`.
  4. Build with Ninja or make.
- Expected effect:
  - Mean performance uplift >200% for single-threaded operations at 1920×1080.
  - Multithreading support available but single-core tests show raw RVV 1.0 capability.
- Failure modes:
  - If the compiler already well-optimizes the baseline, performance gains may be smaller.
  - Missing toolchain or incorrect CMake flags may disable the HAL.
  - The HAL is currently experimental and not part of official binary releases.
- Measurements:
  - Single-core performance uplift measured on SpacemiT MUSE Pi with KeyStone K1.
  - Tests use OpenCV's own performance test suite.
  - Results: mean uplift >200% across 119 functions.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – Another RISC-V optimization approach using a dedicated systolic array accelerator for matrix operations, contrasting with the vectorized HAL approach.
- [[Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark]] – A benchmark of LLM inference quantization on a RISC-V board, representing another performance optimization area for RISC-V CPUs.

## Sources

- [OpenCV Blog: Introducing HAL riscv-rvv](https://opencv.org/introducing-hal-riscv-rvv-unleashing-the-power-of-risc-v-cpus-with-rvv-1-0/)

