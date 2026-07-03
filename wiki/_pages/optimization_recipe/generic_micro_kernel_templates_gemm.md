---
canonical_name: Template-Based Micro-kernel Generation for GEMM
aliases:
- Generic GEMM Micro-kernel Templates
- Intrinsics-based GEMM micro-kernels
- Portable micro-kernel generation for matrix multiplication
subtype: null
tags:
- gemm
- micro-kernel
- SIMD
- intrinsics
- BLIS
- ARM
- x86
hardware_targets:
- ARM Neon (128-bit SIMD)
- ARM SVE (variable-length SIMD)
- Intel AVX512 (512-bit SIMD)
- NVIDIA Carmel
- Fujitsu A64FX
- AMD EPYC 7282
workloads:
- gemm (matrix multiplication for deep learning)
datatypes:
- fp32
- fp64
metrics:
- floating-point throughput
- relative speedup vs BLIS
- AMD AOCL
- ARMPL
toolchains:
- BLIS
- vector intrinsics compilers (GCC
- Clang)
constraints:
- SIMD unit presence
- explicit vector length and register pressure management
evidence_strength: reported
scorecard:
  novelty_delta: 0.85
  claim_density: 0.75
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.6
sources:
- raw/cache/d993c46d31b3a032.md
- https://link.springer.com/article/10.1007/s11227-022-05003-3
source_url: https://link.springer.com/article/10.1007/s11227-022-05003-3
fetched_at: '2026-07-01T03:54:15.902442+00:00'
type: optimization_recipe
created: '2026-07-01'
updated: '2026-07-01'
cold_start: false
inbound_links: 3
needs_summary_revision: false
outbound_links:
- target: riscv_gemm_optimization_approaches
  reason: a synthesis page using this ARM/x86 template-based technique as an existence
    proof for the RISC-V-specific compiler-generated (MLIR+xDSL), hand-tuned (XuanTie
    C908), and hardware-generated (OpenGeMM) approaches
---

# Template-Based Micro-kernel Generation for GEMM

This optimization recipe describes a method to systematically generate high-performance micro-kernels for general matrix multiplication (gemm) using generic templates based on vector intrinsics. The approach enables portability across diverse processor architectures—including ARM Neon (128-bit SIMD), ARM SVE (variable-length SIMD), and Intel AVX512 (512-bit SIMD)—without sacrificing performance. The templates are parameterised by two configuration variables (micro-kernel dimensions \(m_r \times n_r\)) and a set of architecture-specific macros, allowing instantiation for a specific SIMD unit. When integrated into the BLIS family of algorithms (variants B3A2C0, A3B2C0, etc.), the generated micro-kernels deliver floating-point throughput on par with or exceeding that of hand-tuned, assembly-level implementations in libraries such as BLIS, AMD AOCL, and ARMPL, as demonstrated on NVIDIA Carmel (ARM Neon), Fujitsu A64FX (ARM SVE), and AMD EPYC 7282 (256-bit SIMD).

## Key Claims

- A generic micro-kernel template, expressed with a few macros and two dimension variables, can be instantiated for multiple SIMD architectures while retaining high performance.
- The template leverages vector intrinsics to exploit SIMD units, avoiding the need for per-architecture assembly.
- Integration into the BLIS family (including all six algorithm variants) is straightforward by instantiating the micro-kernel and configuring cache-level parameters.
- On the evaluated platforms (NVIDIA Carmel, Fujitsu A64FX, AMD EPYC 7282), the intrinsics-based micro-kernels match or beat the throughput of highly optimised standard implementations.

## Transformation

- Prerequisites: Access to a BLIS framework or equivalent macro-kernel infrastructure; target compiler with vector intrinsic support (GCC, Clang); SIMD-capable processor.
- Steps:
  1. Define the generic micro-kernel template in C with placeholders for SIMD intrinsics, using two integer parameters \(m_r, n_r\) for tile dimensions.
  2. Create architecture-specific mappings of the placeholder macros to the actual vector intrinsics (e.g., Neon `vmlaq_f32`, SVE `svmla_f32_m`, AVX512 `_mm512_fmadd_ps`), and tune loop order and prefetching.
  3. Instantiate the template with desired tile dimensions (e.g., \(6\times8\) for Neon, \(8\times12\) for AVX512) and wrap the micro-kernel into the BLIS macro-kernel loops.
  4. Set cache configuration parameters (\(m_c, n_c, k_c\)) to match the target processor’s memory hierarchy, and adjust packing routines for appropriate alignment and storage.
  5. Validate the micro-kernel against a reference implementation and compare performance against BLIS or vendor library.
- Expected effect: Portable, maintainable micro-kernels that achieve at least the same floating-point throughput as hand-optimized assembly versions; the approach can quickly target new architectures by changing the intrinsic mapping.
- Failure modes: Inappropriate tile dimensions causing register spill; misaligned data degrading SIMD efficiency; macro expansion errors leading to incorrect results; insufficient cache tuning causing bandwidth bottlenecks; compilers failing to optimise intrinsics as efficiently as assembly.
- Measurements: On NVIDIA Carmel (ARM Neon), Fujitsu A64FX (ARM SVE), and AMD EPYC 7282 (256-bit AVX2), the generated micro-kernels delivered gemm throughput on par with or higher than the respective BLIS, AMD AOCL, and ARMPL implementations for deep learning matrix shapes; exact GFLOPS values vary with tile size and problem dimensions but consistently show competitive results.

## Relationships

- Related workload kernel: [[xuantie_c908_fp16_gemm_kernel]] (vendor-specific GEMM kernel for a different architecture).
- Alternative code-generation optimization recipe: [[mlir_xdsl_rvv_gemm_codegen_recipe]] (MLIR/xDSL pipeline for RISC-V vector micro-kernels).
- Base algorithmic framework: The BLIS family of algorithms (B3A2C0, A3B2C0, etc.) underpins the macro-kernel structure used to integrate these micro-kernels.
- [[riscv_gemm_optimization_approaches]]: a synthesis page using this ARM/x86 template-based technique as an existence proof for the RISC-V-specific compiler-generated (MLIR+xDSL), hand-tuned (XuanTie C908), and hardware-generated (OpenGeMM) approaches.

## Sources

- Micro-kernels for portable and efficient matrix multiplication in deep learning, The Journal of Supercomputing, 79, 8124–8147 (2023). https://link.springer.com/article/10.1007/s11227-022-05003-3
