---
canonical_name: IREE MLIR uKernel for RISC-V Vector Extension
aliases:
- IREE RVV uKernel
- MLIR native ukernel for RVV
- IREE uKernel RVV matmul
- MLIR-based ukernels for RISC-V Vector
subtype: null
tags:
- IREE
- MLIR
- RISC-V
- RVV
- ukernel
- matmul
- LLVM
hardware_targets:
- RISC-V RVV vlen=128
workloads:
- matmul f16*f16->f32
datatypes:
- f16
- f32
metrics:
- GFLOPS (expected)
toolchains:
- IREE
- MLIR
- LLVM
constraints:
- RVV vlen=128
- zfh extension
evidence_strength: reported
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/d727433f0a1dd84e.md
- https://github.com/iree-org/iree/issues/22720
source_url: https://github.com/iree-org/iree/issues/22720
fetched_at: '2026-07-02T05:37:21.789570+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# IREE MLIR uKernel for RISC-V Vector Extension

This optimization recipe describes a proposed transformation within the IREE compiler to implement MLIR-native ukernels for RISC-V Vector (RVV) targets by following the GPU backend&#8217;s precedent of using declarative, tensor-based ukernels. The approach replaces hand-written assembly kernels with self-contained `.mlir` files that serve as both specification and implementation, relying on the generic MLIR `vector` dialect rather than a target-specific dialect and delegating instruction selection to the LLVM backend. The recipe targets a Minimum Viable Product (MVP): a single pure matmul ukernel for mixed-precision `f16 * f16 -> f32`, configured for an RVV vector length of 128 bits with the `zfh` half-precision floating-point extension. The transformation preserves IREE&#8217;s ability to perform automatic producer/consumer fusion (e.g., bias addition and activation) via standard compiler passes. No measurements are yet available because this is a proposed design; the recipe identifies prerequisites (IREE, MLIR, LLVM with RVV support), outlines three implementation steps, and notes potential failure modes in the upstream LLVM lowering or in tile sizing. The expected effect is high-performance, target-specific code generation that leverages LLVM&#8217;s instruction selection for optimal RVV instructions, avoiding custom RVV dialect work within IREE.

## Key Claims

- MLIR-based ukernels for RVV can be implemented using the generic vector dialect without introducing a target-specific dialect, by delegating instruction selection to the LLVM backend.
- The MVP will be a single `f16*f16->f32` matmul ukernel targeting vlen=128 and the `zfh` extension, demonstrating automatic fusion of a matmul+bias pattern.
- The engineering plan requires three steps: (1) ensuring robust vector-to-RVV lowering in LLVM, (2) adding IREE infrastructure for CPU ukernel declaration (`#iree_cpu.data_tiled_layout` attribute and CPU feature matcher), and (3) defining the RVV matmul ukernel in a self-contained `.mlir` file.
- The proposed design follows the IREE GPU backend&#8217;s declarative ukernel pattern, enabling the compiler to fuse operations through standard passes.
- The ukernel will use a tile size of 8x8x1 (M0=8, N0=8, K0=1) with inner blocking order [0,1,2].

## Transformation

- Prerequisites: IREE compiler infrastructure (with MLIR and LLVM integration), LLVM backend with RISC-V Vector (RVV) support and the `zfh` extension handling, and a RISC-V hardware target with vlen=128 and `zfh` support (e.g., compatible SiFive cores).
- Steps:
  1. **Ensure Robust Lowering from vector Dialect to RVV in LLVM** - Verify that MLIR vector operations such as `vector.fma`, `vector.load`, `vector.store`, and `vector.broadcast` lower correctly to efficient RVV instructions (e.g., `vfmacc.vf`, `vle16.v`, `vse32.v`, `vmv.v.x`). If gaps exist, upstream improvements to LLVM&#8217;s MLIR-to-LLVM-IR conversion and instruction selector.
  2. **Implement IREE Infrastructure for CPU Ukernel Declaration** - Add a declarative CPU layout attribute (`#iree_cpu.data_tiled_layout`) specifying tile sizes and inner blocking order, and implement a CPU feature matcher that selects the ukernel only when target CPU has required features (e.g., `+v`, `+zfh`).
  3. **Define and Implement the RVV Matmul Ukernel in MLIR** - Create a self-contained `.mlir` file (e.g., `iree_uk_riscv_dt_matmul_f16f16f32.mlir`) with declarative metadata (matching `linalg.matmul` with specific operand types and CPU features) and implementation using generic vector ops: broadcast LHS scalars, load RHS vector once, perform FMA with accumulator reloads, and assemble the result tensor. The file serves as both specification and implementation.
- Expected effect: A compiler-driven approach that generates high-performance, target-specific RVV code automatically fused with adjacent operations (e.g., bias addition), eliminating the need for hand-written assembly while achieving competitive performance on RISC-V vector processors.
- Failure modes: Identified gaps in LLVM&#8217;s lowering of vector operations to efficient RVV instructions (requiring upstream patches); improper tile sizing leading to poor register reuse or cache misses; insufficient handling of VLEN-agnostic execution; lack of hardware support for required extensions (vlen=128, zfh).
- Measurements: No quantitative results are available as this is a proposed design. The MVP is intended to produce a benchmark comparison against existing GEMM implementations (e.g., OpenBLAS) once implemented.

## Relationships

- This recipe relies on the [[llvm_riscv_target]] for the core instruction selection from the MLIR vector dialect to RVV machine code; any gaps in lowering will require contributions to the LLVM backend.
- The alternative approach using MLIR+xDSL for custom RVV lowering is documented in [[mlir_xdsl_rvv_gemm_codegen_recipe]]; this IREE ukernel proposal is complementary, targeting tighter integration within the IREE compiler&#8217;s existing fusion and dispatch infrastructure.
- The MVP targets a single matmul ukernel shape; future validation on hardware such as the [[sifive_performance_p570_gen3]] (which features RVV 1.0 with a 128-bit vector pipeline) would provide concrete measurements.
- This recipe shares conceptual similarity with the generic micro-kernel generation approach described in [[generic_micro_kernel_templates_gemm]] (if that page exists; it is listed in the wiki context but not shown as a direct page—it may be an entity). Insufficient context for additional cross-links.

## Sources

- https://github.com/iree-org/iree/issues/22720 - Issue describing the proposed implementation of MLIR-based ukernels for RISC-V Vector Extension in IREE.
