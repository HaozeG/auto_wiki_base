---
canonical_name: RVV Dialect (MLIR)
aliases:
- RISC-V Vector Extension Dialect
- RVV MLIR Dialect
subtype: null
tags:
- MLIR
- RVV
- RISC-V
- dialect
- compiler
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/bb641be14cc75d0d.md
- https://discourse.llvm.org/t/rfc-add-risc-v-vector-extension-rvv-dialect/4146
source_url: https://discourse.llvm.org/t/rfc-add-risc-v-vector-extension-rvv-dialect/4146
fetched_at: '2026-07-03T13:55:16.269424+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: The RVV instructions targeted by the SHL optimization on the XuanTie C908
    are represented at compile-time through the RVV Dialect in MLIR, connecting the
    software library optimization to the compiler infrastructure that lowers these
    instructions
---

# RVV Dialect (MLIR)

The RVV Dialect is an architectural-specific MLIR dialect for the RISC-V Vector Extension (RVV), proposed as an RFC to the MLIR community in August 2021. It provides MLIR-level representation of scalable vector types and operations that map directly to RVV instructions, following the same design pattern as the existing Arm SVE dialect in MLIR. The dialect defines scalable vector types parameterized by vector length multiplier (LMUL) and element size (SEW), supporting all combinations from LMUL=1/8 to LMUL=8 across integer and floating-point element types. The initial patch includes arithmetic operations (add, sub, mul, div), memory operations (load and store), and corresponding masked variants, along with intrinsic operations that bind one-to-one to LLVM IR intrinsics. A two-step lowering path converts RVV dialect operations to RVV intrinsic operations and then to LLVM IR, enabling end-to-end compilation through the MLIR pipeline. The proposal explicitly references the SVE dialect as a template for scalable vector type implementation, noting that while the syntax is shared, the semantics differ between the two architectures.

## Key Claims

- The RVV Dialect introduces scalable vector types with LMUL and SEW parameters, allowing register grouping for arbitrary vector lengths, as shown by the mapping table from RVV to LLVM types (e.g., `!rvv.vector<8xi32>` corresponds to `<vscale x 8 x i32>` in LLVM IR).
- The dialect defines separate RVV Operations (higher-level abstractions) and RVV Intrinsic Operations (LLVM-bound), with a one-to-one lowering between them for basic arithmetic operations, while memory operations require additional memref-to-pointer conversion.
- Arithmetic operations support mask and vector-scalar forms, including rvv.add, rvv.sub, rvv.mul, rvv.div and their masked variants (rvv.masked.add, etc.), directly corresponding to RVV intrinsic operations.
- The two-step lowering path first converts RVV operations to RVV intrinsic operations (one-to-one for arithmetic, plus memref conversion for memory), then translates intrinsic operations to LLVM IR via a natural one-to-one mapping.
- The RVV Dialect follows the same scalable vector type pattern used by the ArmSVE dialect in MLIR, but targets RISC-V Vector Extension v1.0 candidate semantics rather than SVE.
- The RFC includes a complete first patch with dialect definition, scalable vector type, operations, intrinsic operations, and translation from RVV Dialect to LLVM Dialect.

## Relationships

- [[c908-wino-gemm-optimization]]: The RVV instructions targeted by the SHL optimization on the XuanTie C908 are represented at compile-time through the RVV Dialect in MLIR, connecting the software library optimization to the compiler infrastructure that lowers these instructions.

## Sources

- https://discourse.llvm.org/t/rfc-add-risc-v-vector-extension-rvv-dialect/4146
