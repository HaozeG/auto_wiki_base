---
canonical_name: TVM RISC-V Vector/Matrix Extension Support
aliases:
- RISC-V Vector Extension TVM support
- RISC-V Matrix Extension TVM
- RVV TVM integration
- RMM TVM integration
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/3308447a09f5c62c.md
- https://discuss.tvm.apache.org/t/discuss-introduce-risc-v-vector-matrix-extension/16490
source_url: https://discuss.tvm.apache.org/t/discuss-introduce-risc-v-vector-matrix-extension/16490
fetched_at: '2026-07-02T13:14:49.514431+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# TVM RISC-V Vector/Matrix Extension Support

The TVM RISC-V Vector/Matrix Extension Support refers to the proposed integration of RISC-V Vector extension (RVV) and Matrix extension (RMM) into the Apache TVM compiler framework, as discussed in a community RFC in March 2024. RISC-V Vector extension is a variable-length vector computing instruction set similar to ARM SVE, with register widths transparent to the programmer and data length controlled via the vl register. The Matrix extension is used for matrix block multiplication and also adopts a variable-length design where M/N/K dimensions are configurable. The proposal aims to enable TVM to generate efficient code for RISC-V vector and matrix operations, addressing challenges such as TVM's inability to represent variable vector lengths and the impact of tensor shapes that are not evenly divisible by SIMD register widths. Two implementation methods are considered: extending TVM's codegen_c to generate intrinsic C code, or extending codegen_llvm to interface with LLVM IR intrinsics. The proposal also highlights common problems like the use of T.where causing ineffective vectorization and the need for padding or loop partitioning to handle non-divisible shapes.

## Key Claims

- RISC-V Vector extension (RVV) is a variable-length vector ISA similar to ARM SVE, with transparent register width and vl-controlled data length.
- RISC-V Matrix extension (RMM) is a configurable matrix block multiplication extension.
- TVM currently cannot represent variable vector lengths or the vl-controlled processing model of RISC-V Vector extension.
- Tensor shapes not evenly divisible by SIMD register width cause ineffective vectorization when using T.where.
- Two implementation methods: codegen_c with intrinsic C code generation, and codegen_llvm with LLVM IR intrinsics.
- There are common problems with both methods: inability to handle variable vector lengths, and issues with non-divisible tensor shapes.

## Relationships

- [[risc-v-vector-intrinsic-specification]]: related via shared risc, vector.

- [[riscv-vector-primer]]: related via shared risc, vector.

- [[riscv-vector-intrinsics]]: related via shared risc, vector.

- [[stream-computing-risc-v-matrix-extension]]: related via shared extension, matrix, risc.

- [[risc-v-matrix-project]]: related via shared matrix, risc.

- [[tvm-metaschedule-rvv-integration]]: An existing optimization recipe that integrates RVV into TVM's MetaSchedule autotuning, complementing the codegen-level support discussed in this RFC.
- [[xuantie-c906]]: A RISC-V processor with RVV v0.7.1 support that could benefit from TVM's vector extension support.
- Insufficient context for additional cross-links.

## Sources

- Apache TVM Discuss: "[DISCUSS]Introduce RISC-V Vector/Matrix extension" (https://discuss.tvm.apache.org/t/discuss-introduce-risc-v-vector-matrix-extension/16490)
