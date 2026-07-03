---
canonical_name: LLVM RISC-V Vector Extension IR Representation
aliases:
- RISC-V Vector Extension in LLVM
- RVV LLVM IR types
- LLVM RVV scalable vectors
- LLVM RVV intrinsics
subtype: null
tags:
- LLVM
- RISC-V
- RVV
- compiler IR
- scalable vectors
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.95
  bridge_score: 0.8
  hub_potential: 0.5
sources:
- raw/cache/915ca891a1497a12.md
- https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst
source_url: https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst
fetched_at: '2026-07-02T04:35:06.928877+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: llvm_riscv_target
  reason: The broader LLVM RISC-V target backend that includes this vector extension
    support as a key component, providing code generation for the full set of RISC-V
    extensions
- target: mlir_xdsl_rvv_gemm_codegen_recipe
  reason: An optimization recipe that uses LLVM RVV intrinsic code generation for
    GEMM micro-kernels, relying on the type mapping and intrinsic representation documented
    here
- target: spacemit_x60
  reason: A RISC-V hardware target implementing RVV 1.0 with 256-bit vectors; the
    LLVM RVV IR model is the compilation path for generating code for this and similar
    platforms
---

# LLVM RISC-V Vector Extension IR Representation

LLVM RISC-V Vector Extension IR Representation is the LLVM compiler infrastructure's formal model for the 1.0 version of the RISC-V Vector Extension (RVV). It maps RVV's VLEN-sized vector registers to LLVM IR scalable vector types of the form `<vscale x n x ty>`, where the multiplicity `n` and element type `ty` encode the vector length multiplier (LMUL) and standard element width (SEW). The mapping covers integer types i8 through i64, floating-point types half, float, double, and bfloat, across LMUL values from ⅛ to 8, with explicit N/A entries for infeasible combinations. Mask vectors are represented as scalable vector types of i1 elements (`<vscale x 1 x i1>` through `<vscale x 64 x i1>`), where types sharing the same SEW/LMUL ratio map to identical mask types. RVV instructions are represented in LLVM IR in two distinct forms: direct use of scalable vector types in standard IR operations (e.g., `add`), and explicit RVV intrinsics (`@llvm.riscv.vadd.*`) that mirror the C intrinsics specification. Both unmasked and masked intrinsic variants provide operands for the application vector length (AVL), passthru values for inactive/tail element management, and policy bits. The representation supports ELEN=32 or ELEN=64 only, requiring VLEN to be at least 64 bits. This reference serves as the authoritative guide for how the LLVM backend interprets and lowers RVV vector code.

## Key Claims

- LLVM supports the 1.0 RISC-V Vector Extension (RVV) specification.
- RVV VLEN-sized registers are modeled using scalable vector types `<vscale x n x ty>`, where `n` and `ty` control LMUL and SEW.
- The mapping table covers LMUL=⅛, ¼, ½, 1, 2, 4, 8 for element types i8, i16, i32, i64 (ELEN=64), half, float, double, bfloat; infeasible combinations are marked N/A.
- Mask vector types are `<vscale x 1/2/4/8/16/32/64 x i1>`; types with the same SEW/LMUL ratio share the same mask type.
- LLVM supports ELEN=32 or ELEN=64; VLEN must be at least 64 bits (VLEN=32 not supported).
- `vscale` is defined as VLEN/64 (constant `RISCV::RVVBitsPerBlock`).
- RVV instructions can be represented as regular LLVM instructions on scalable vector types or as explicit RVV intrinsics.
- RVV intrinsics (`@llvm.riscv.*`) provide unmasked and masked variants with operands for AVL, passthru, mask, and policy immediates.
- Only scalable vector types are valid for RVV intrinsics; fixed-length vector types are not supported.

## Relationships

- [[llvm_riscv_target]]: The broader LLVM RISC-V target backend that includes this vector extension support as a key component, providing code generation for the full set of RISC-V extensions.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe that uses LLVM RVV intrinsic code generation for GEMM micro-kernels, relying on the type mapping and intrinsic representation documented here.
- [[spacemit_x60]]: A RISC-V hardware target implementing RVV 1.0 with 256-bit vectors; the LLVM RVV IR model is the compilation path for generating code for this and similar platforms.

## Sources

- https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst
