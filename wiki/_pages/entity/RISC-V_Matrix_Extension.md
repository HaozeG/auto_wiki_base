---
type: entity
tags:
  - RISC-V
  - matrix extension
  - ISA
  - GEMM
  - AI accelerator
  - RVM
sources:
  - raw/sources/riscv_matrix_extension_proposal.pdf
created: 2026-06-29
updated: 2026-06-29
cold_start: true
inbound_links: 3
scorecard:
  novelty_delta: 0.95
  claim_density: 0.9
  self_containedness: 0.95
  bridge_score: 0.85
  hub_potential: 0.85
---

# RISC-V Matrix Extension

The RISC-V Matrix Extension (RVM) is a draft ISA proposal (v0.6.0, 2024-12-11) that adds hardware-accelerated matrix multiply-accumulate (GEMM) capability to RISC-V. It uses a decoupled architecture from the RISC-V Vector Extension (RVV), introducing separate matrix tile registers, accumulation registers, and a dedicated CSR bank. The core operation is `C += A × BT`, where A and B are loaded into tile registers and C accumulates into a wider accumulation register. The extension is designed for tiled GEMM loops common in deep learning workloads, with direct ISA support for tail-handling in the M, N, and K dimensions.

## Key Claims

- Adds 4 tile registers (tr0–tr3) for input matrices and 4 accumulation registers (acc0–acc3) for output; registers are two-dimensional, not flat vectors.
- Three implementation-defined parameters govern all register geometry: ELEN (element bit width, ≥8, power of 2), TLEN (tile register bits, ≤2^32), and TRLEN (tile row bits, ≤2^16); derived ROWNUM = TLEN/TRLEN, ARLEN = TLEN/TRLEN × ELEN, ALEN = ARLEN × ROWNUM.
- At TLEN=512, TRLEN=128, ELEN=32: mfmacc.s (fp32) achieves a 4×4 A tile, 4×4 BT tile, 4×4 C tile; mmacc.w.b (int8→int32) achieves 4×16 × 16×4 → 4×4; at TLEN=8192 the same parameters scale to 16×32 × 32×16 → 16×16.
- Compulsory data types in misa: mmi8i32 (int8→int32 quad-widen), mmf16f16 (fp16 non-widen), mmf8f16/mmf8bf16 (fp8 double-widen to fp16/bf16), mmf16f32/mmbf16f32 (fp16/bf16 double-widen to fp32), mmf8f32 (fp8 quad-widen to fp32); optional types include mmf32f32, mmf64f64, mmi4i32.
- The Zmint4 sub-extension adds 4-bit integer matrix multiplication (INT4 × INT4 → INT32 oct-widen), requires ELEN ≥ 32; two INT4 values are packed into one 8-bit element and mtilek must be even.
- 32-bit instruction encoding fits under the custom-1 opcode (0101011); a 64-bit variant adds per-instruction frm (float rounding mode) and se (saturation enable) fields in bits [42:39].
- `msettile{m|k|n}[i]` configuration instructions update the mtilem/mtilek/mtilen CSRs directly, providing hardware-managed tiling support for M/K/N loop tails without software branch logic.
- The `mrelease` instruction sets the MS context field in mstatus to Initial (01), signaling that tile register state can be discarded; analogous to RVV's VS field and enables low-cost context switching.
- Matrix memory instructions follow RVWMO at the instruction level; element access order within a single instruction is unordered.
- Load/store distinguishes three operand roles: A (left matrix, shape mtilem × mtilek), B (right matrix, transposed, shape mtilen × mtilek), C (accumulation, shape mtilem × mtilen); both non-transposed (mlae*/mlbe*/mlce*) and transposed (mlate*/mlbte*/mlcte*) variants exist for 8/16/32/64-bit element widths.
- Element-wise instruction category covers integer arithmetic, float arithmetic, and type-conversion (fp↔fp, int↔float, fixed-point clip); requires optional miew/mfew/mfic misa bits.

## Relationships

- [[RISC-V_Vector_Extension]] — Matrix Extension is explicitly decoupled from RVV; separate register file, separate CSR space, separate context status bit in mstatus (MS vs VS). Both can coexist in the same hart.
- [[GEMM_with_RISC-V_Vector_Extension]] — RVV implements GEMM via VLMUL-based tiling; RVM replaces that with dedicated `mfmacc`/`mmacc` instructions and accumulation registers, reducing instruction count and loop overhead.
- [[QiMeng_TensorOp]] — QiMeng-TensorOp auto-generates tensor operator kernels; RVM's native GEMM instructions are a candidate target backend for such generation frameworks.
- [[Seal5]] — Seal5 automates LLVM backend generation for custom RISC-V extensions; RVM is a complex extension that would require Seal5-style toolchain integration for compiler support.
- [[XuanTie_GNU_Toolchain]] — RVM needs toolchain support (assembler, compiler intrinsics) not yet present in mainline; vendor toolchains like XuanTie's are likely first adopters.

## Sources

- RISC-V Matrix Specification Proposal v0.6.0 (2024-12-11, draft): `raw/sources/riscv_matrix_extension_proposal.pdf`
  - Ch. 2 (pp. 5–6): implementation parameters ELEN/TLEN/TRLEN, register geometry
  - Ch. 3 (pp. 7–14): programmer's model — register file, CSR table, rounding modes, saturation, context status
  - Ch. 4 (pp. 15–22): instruction encoding formats (32-bit and 64-bit)
  - Ch. 5 (pp. 23–53): full instruction set (configuration, multiply, load/store, misc, element-wise)
  - Ch. 6 (p. 54): Zmint4 INT4 extension
  - Ch. 7 (p. 55): matrix memory model
