---
canonical_name: RISC-V Vector (RVV) C Intrinsic Specification
aliases:
- RVV intrinsics
- riscv_vector.h
- RVV C API
- RISC-V V extension intrinsics
- __riscv_v_intrinsic
subtype: null
tags:
- RISC-V
- RVV
- intrinsics
- specification
- API
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.8
  hub_potential: 0.85
sources:
- raw/cache/c6fd44b003a42be6.md
- https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc
source_url: https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc
fetched_at: '2026-07-02T05:22:29.711992+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# RISC-V Vector (RVV) C Intrinsic Specification

The RISC-V Vector (RVV) C Intrinsic Specification defines the C language interface for directly leveraging the RISC-V V extension through compiler intrinsics. It provides a strongly-typed API for controlling vector length, effective element width (EEW), effective LMUL (EMUL), vector masking, and policy behavior (tail/mask agnostic). The specification includes a version test macro (`__riscv_v_intrinsic`), a required header file (`<riscv_vector.h>`), and a naming scheme that encodes the EEW and EMUL of the destination vector register into the function name suffix. It targets high-performance cores and defaults to tail-agnostic (`vta=1`) and mask-agnostic (`vma=1`) policies to avoid performance penalties from undisturbed behavior on out-of-order cores. The API abstracts the `vl` control register, requiring programmers to specify an application vector length (AVL) as a `size_t` parameter, with the actual `vl` value being implementation-defined and typically resolved at runtime following the rules of the RVV specification.

## Key Claims

- The `__riscv_v_intrinsic` macro is defined even when the vector extension is not enabled, and its value encodes the specification version as `MAJOR_VERSION * 1,000,000 + MINOR_VERSION * 1,000 + REVISION_VERSION` (identical to the RISC-V C API specification).
- The header `<riscv_vector.h>` must be included to use the intrinsics, and its inclusion should be guarded by the test macro.
- Availability of specific intrinsic variants depends on the architecture specified via the `-march` option; for example, `vint64m1_t` and `__riscv_vle64_v_i64m1` are not available under `rv64gc_zve32x`.
- Data types are strongly-typed and encode the EEW and EMUL in the function name: e.g., `vint32m1_t __riscv_vadd_vv_i32m1` implies EEW=32, EMUL=1 on all operands.
- Widening operations encode different EEW/EMUL for sources vs destination: e.g., `vint32m1_t __riscv_vwadd_vv_i32m1(vint16mf2_t vs2, vint16mf2_t vs1, size_t vl)` uses source EEW=16, EMUL=1/2 and destination EEW=32, EMUL=1.
- The `vl` argument specifies the application vector length (AVL); the actual `vl` control register value is set by the implementation and can be queried via the `__riscv_vsetvl_*` intrinsics.
- Instructions that support masking have masked variant intrinsics; the control of vector masking and policy behavior (`vta`, `vma`) is fused into the same suffix.
- The default policy scheme is tail-agnostic and mask-agnostic (`vta=1`, `vma=1`), optimized for high-performance out-of-order cores.

## Relationships

- [[llvm_riscv_target]] - The LLVM RISC-V target provides the compiler backend that implements the RVV intrinsic API described in this specification.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]] - This optimization recipe generates C code with RVV intrinsics, relying on the interface defined in the specification.
- [[sifive_performance_p570_gen3]] - This hardware target supports the RISC-V V extension (RVV 1.0) and is capable of executing code compiled using these intrinsics.

## Sources

- https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc
