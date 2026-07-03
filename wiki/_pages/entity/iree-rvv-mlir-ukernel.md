---
canonical_name: IREE MLIR-based uKernel for RVV
aliases:
- RVV MLIR ukernel
- IREE RVV uKernel
- MLIR-based uKernel for RVV
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
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Both target RISC-V AI acceleration on VLEN=128 hardware with Zfh support
    and f16 matmul workloads, but this proposal uses IREE's MLIR-based compiler-driven
    kernel approach rather than SHL's hand-tuned library with instruction fusion
---

# IREE MLIR-based uKernel for RVV

The IREE MLIR-based uKernel for RISC-V Vector (RVV) Extension is a design proposal within the IREE compiler project to implement high-performance, target-specific code generation kernels using pure MLIR operations from the vector dialect, without introducing a target-specific dialect. This approach mirrors the GPU backend's precedent of declarative, tensor-based ukernels. The Minimum Viable Product (MVP) targets a single f16 * f16 -> f32 mixed-precision matrix multiplication kernel with an 8x8x1 tile configuration, assuming a VLEN=128 RISC-V vector unit with the Zfh half-precision floating-point extension. The design emphasizes automatic producer/consumer fusion — such as bias addition and activation injection — via standard compiler fusion passes, and delegates final instruction selection to the LLVM backend, addressing any lowering gaps upstream rather than creating IREE-specific dialect constructs.

## Key Claims

- Implements MLIR-native ukernels for RISC-V RVV targets in IREE, following the GPU backend's precedent of declarative, tensor-based ukernels.
- Uses only the MLIR vector dialect for implementation, avoiding a target-specific dialect, and relies on the LLVM backend for instruction selection.
- MVP defines a single f16 * f16 -> f32 mixed-precision matmul ukernel with tile sizes [8, 8, 1] targeting VLEN=128 and the Zfh extension.
- Declarative metadata via `#iree_cpu.data_tiled_layout` attribute for data tiling description and a CPU feature matcher (`cpu_feature`) for ukernel selection based on target features (+v, +zfh).
- The ukernel specification is a self-contained `.mlir` file serving as both specification and implementation.
- Automatic producer/consumer fusion (e.g., bias addition and activation) is supported through standard compiler fusion passes operating on the ukernel interface.

## Relationships

- [[c908-wino-gemm-optimization]]: Both target RISC-V AI acceleration on VLEN=128 hardware with Zfh support and f16 matmul workloads, but this proposal uses IREE's MLIR-based compiler-driven kernel approach rather than SHL's hand-tuned library with instruction fusion.

## Sources

- https://github.com/iree-org/iree/issues/22720
