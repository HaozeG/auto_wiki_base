---
canonical_name: IREE MLIR-based uKernel for RVV
aliases:
- RVV MLIR ukernel
- IREE RVV uKernel
- MLIR-based uKernel for RVV
- IREE MLIR Ukernels for RVV
- IREE RVV ukernel
- MLIR-based RVV ukernels in IREE
subtype: null
tags:
- RISC-V
- RVV
- IREE
- MLIR
- uKernel
- Matmul
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/40133e27b2cde023.md
- https://github.com/iree-org/iree/issues/22720
source_url: https://github.com/iree-org/iree/issues/22720
fetched_at: '2026-07-03T13:54:35.514439+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Both target RISC-V AI acceleration on VLEN=128 hardware with Zfh support
    and f16 matmul workloads, but this proposal uses IREE's MLIR-based compiler-driven
    kernel approach rather than SHL's hand-tuned library with instruction fusion
---

# IREE MLIR-based uKernel for RVV

The IREE MLIR-based uKernel for RISC-V Vector (RVV) Extension is a design proposal within the IREE compiler project to implement high-performance, target-specific code generation kernels using pure MLIR operations from the vector dialect, without introducing a target-specific dialect. This approach mirrors the GPU backend's precedent of declarative, tensor-based ukernels. The Minimum Viable Product (MVP) targets a single f16 * f16 -> f32 mixed-precision matrix multiplication kernel with an 8x8x1 tile configuration, assuming a VLEN=128 RISC-V vector unit with the Zfh half-precision floating-point extension. The design emphasizes automatic producer/consumer fusion — such as bias addition and activation injection — via standard compiler fusion passes, and delegates final instruction selection to the LLVM backend, addressing any lowering gaps upstream rather than creating IREE-specific dialect constructs. Prerequisites include a working MLIR toolchain with RVV support in LLVM, the IREE compiler with CPU target support, and a RISC-V platform implementing RVV 1.0 with vector length 128 and the `zfh` half-precision floating-point extension. The expected effect is to enable automatic producer/consumer fusion (e.g., matrix multiply followed by bias addition and activation) via standard MLIR passes, while delegating instruction selection to the LLVM backend. Failure modes are not documented; the design is contingent on the correctness of the MLIR-to-LLVM-IR conversion for vector operations targeting RVV. No performance measurements are yet available as the implementation is currently proposed and not built or run.

## Key Claims

- Implements MLIR-native ukernels for RISC-V RVV targets in IREE, following the GPU backend's precedent of declarative, tensor-based ukernels.
- Uses only the MLIR vector dialect for implementation, employing generic operations such as `vector.fma`, `vector.load`, `vector.store`, and `vector.broadcast`, rather than introducing a target-specific dialect. The LLVM backend is responsible for generating optimal RVV instructions (e.g., `vfmacc.vf`, `vle16.v`, `vse32.v`).
- MVP defines a single f16 * f16 -> f32 mixed-precision matmul ukernel with tile sizes [8, 8, 1] targeting VLEN=128 and the Zfh extension.
- Declarative metadata via `#iree_cpu.data_tiled_layout` attribute for data tiling description, including an inner blocking order of [0, 1, 2], and a CPU feature matcher (`cpu_feature`) for ukernel selection based on target features (+v, +zfh).
- The ukernel specification is a self-contained `.mlir` file (e.g., `iree_uk_riscv_dt_matmul_f16f16f32.mlir`) serving as both specification and implementation.
- Automatic producer/consumer fusion (e.g., bias addition and activation) is supported through standard compiler fusion passes operating on the ukernel interface, specifically via the `%init` accumulator argument.

## Transformation

### Prerequisites
- MLIR toolchain with full support for RVV lowering (verification needed).
- IREE compiler with CPU target backend and support for declarative ukernel attributes.
- RISC-V hardware platform implementing RVV 1.0 with vlen=128 and the `zfh` extension.

### Steps
1. Verify that MLIR `vector` dialect operations (`vector.fma`, `vector.broadcast`, `vector.load`, `vector.store`) are correctly lowered to efficient RVV instructions by the LLVM backend. If gaps exist, contribute missing lowering patterns to upstream MLIR/LLVM.
2. Implement IREE infrastructure for CPU ukernel declaration: create the `#iree_cpu.data_tiled_layout` MLIR attribute to describe optimal data tiling, and implement a `cpu_feature` constraint for ukernel matching.
3. Define and implement the RVV matmul ukernel as a self-contained `.mlir` file (`iree_uk_riscv_dt_matmul_f16f16f32.mlir`) with declarative metadata and implementation using generic `vector` ops.

### Expected Effect
Automatic fusion of matmul with bias and activation operations via standard MLIR compiler passes, enabling portable, target-specific RVV code generation without hand-tuned assembly.

### Failure Modes
Not documented; the approach assumes that the MLIR-to-LLVM-IR conversion and LLVM instruction selector correctly lower the generic vector operations to performant RVV instructions.

### Measurements
None yet; the work is a proposal and has not been implemented or benchmarked.

## Relationships

- [[c908-wino-gemm-optimization]]: Both target RISC-V AI acceleration on VLEN=128 hardware with Zfh support and f16 matmul workloads, but this proposal uses IREE's MLIR-based compiler-driven kernel approach rather than SHL's hand-tuned library with instruction fusion.
- [[mlir-xdsl-rvv-codegen-pipeline]]: Both address the missing lowering path for RVV code generation from MLIR, but the IREE ukernel approach uses the MLIR `vector` dialect and relies on LLVM's backend for instruction selection, whereas the MLIR-xDSL pipeline implements custom lowering stages using xDSL to emit C code with RVV intrinsics.

## Sources

- https://github.com/iree-org/iree/issues/22720
