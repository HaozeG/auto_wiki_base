---
type: entity
canonical_name: RISC-V Matrix Specification Proposal
aliases:
- RISC-V Matrix Extension Proposal
- RISC-V Matrix ISA Proposal
tags:
- risc-v
- matrix-extension
- isa
- accelerator
sources:
- raw/sources/riscv_matrix_extension_proposal.pdf
created: 2026-07-01
updated: 2026-07-01
cold_start: true
inbound_links: 2
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.7
needs_summary_revision: true
---

# RISC-V Matrix Specification Proposal

The RISC-V Matrix Specification Proposal is a draft RISC-V ISA extension (version v0.6.0, dated 2024-12-11) that adds native matrix-multiply-accumulate capability to RISC-V harts through a decoupled architecture separate from the existing RISC-V Vector ("V") extension. It defines four architectural Tile Registers (tr0-tr3) for input matrices and four Accumulation Registers (acc0-acc3) for output matrices, plus eight new control-and-status registers, giving compilers and hand-written kernels direct hardware support for `C += A x B^T` style matrix multiplication, matrix load/store, element-wise, and miscellaneous matrix operations. The extension is parameterized per hart by three implementation-defined constants — ELEN (max element bit-width, >=8), TLEN (bits per tile register, a power of 2, <=2^32), and TRLEN (bits per tile-register row, a power of 2, <=2^16) — from which ROWNUM, ARLEN, and ALEN for the accumulation registers are derived, letting implementations trade tile shape against register width (e.g. a 512-bit TLEN with 128-bit TRLEN yields a 4x4 tile at 32-bit elements). Because the tile/accumulator geometry and datatype support are all implementation-defined and self-describing via CSRs, the same instruction encoding can target very different hardware matrix-engine sizes.

## Key Claims

- The extension defines exactly 4 Tile Registers (tr0-tr3) and 4 Accumulation Registers (acc0-acc3), plus 8 CSRs including xmcsr, mtilem/mtilen/mtilek, xmisa, xtlenb, xtrlenb, and xalenb.
- Three implementation-defined constants govern register geometry: ELEN (>=8 bits, power of 2), TLEN (<=2^32 bits, power of 2), and TRLEN (<=2^16 bits, power of 2); ROWNUM = TLEN/TRLEN, ARLEN = ROWNUM*ELEN, ALEN = ARLEN*ROWNUM.
- Example configuration: with TLEN=512 bits and TRLEN=128 bits, ROWNUM=4, and at 32-bit elements this yields a 4x4 tile register and a 4x4 (128-bit-row) accumulation register.
- The read-only `misa`-style CSR `xmisa` exposes a compulsory/optional feature bitmap covering integer matrix multiply (mmi4i32, mmi8i32) and floating-point matrix multiply at multiple precisions (mmf16f16, mmf32f32, mmf64f64, mmf8f16, mmf16f32, mmbf16f32, mmf32f64, mmf8f32, mmf8bf16), where int8xint8->int32 (mmi8i32) and several fp16/bf16-widening modes are compulsory for any conforming implementation.
- Instructions are encoded under the custom-1 (0101011) major opcode with three 32-bit instruction formats (matrix-register-only, matrix-with-GPR, matrix-with-10-bit-immediate) and a distinct 64-bit instruction encoding; d_size/s_size fields select 8/16/32/64-bit element widths.
- The matrix context status field MS (2 bits, mirrored in mstatus/sstatus analogous to the vector context field VS) has four states (All Off, Initial, Clean, Dirty); executing a matrix instruction while MS=Off raises an illegal instruction exception.
- Fixed-point arithmetic supports four rounding modes (RNU, RNE, RDN, ROD) via the xmxrm CSR, and floating-point arithmetic supports five rounding modes (RNE, RTZ, RDN, RUP, RMM) via xmfrm, with an xmsaten CSR selecting saturating vs. wraparound/NaN behavior on fp8 and integer matrix-multiply overflow.

## Relationships

- [[xuantie_c908]]: XuanTie C908 implements the standard RISC-V Vector Extension 1.0 rather than this decoupled matrix extension, illustrating an alternative vector-only approach to matrix acceleration on RISC-V.
- Insufficient context for additional cross-links; a synthesis page comparing decoupled matrix-register extensions (this proposal) against vector-register-based matrix acceleration (e.g. XuanTie IME-style outer-product approaches) would be a natural follow-up once more hardware_target pages exist.

## Sources

- RISC-V Matrix Specification Proposal, Version v0.6.0, 2024-12-11 (Draft). raw/sources/riscv_matrix_extension_proposal.pdf, pages 1-20 (Preamble, Chapters 1-4 through Matrix Multiplication Instruction Format).
