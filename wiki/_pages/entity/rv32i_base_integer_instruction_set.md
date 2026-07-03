---
canonical_name: RV32I
aliases:
- RV32I base integer instruction set
- RISC-V RV32I
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.8
sources:
- raw/cache/087e1d9716d3ad61.md
- https://varshaaks.wordpress.com/2021/07/19/rv32i-base-integer-instruction-set/
source_url: https://varshaaks.wordpress.com/2021/07/19/rv32i-base-integer-instruction-set/
fetched_at: '2026-07-02T05:12:03.953388+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: mos2_risc_v_prototype
  reason: a 2D-material (MoS2) 32-bit microprocessor that implements this full RV32I
    instruction set as its target ISA
---

# RV32I Base Integer Instruction Set

RV32I is the base integer instruction set of the RISC-V architecture, designed to provide a minimal yet sufficient foundation for modern operating systems with only 47 instructions. It defines 32 general-purpose registers, each 32 bits wide, with register x0 hardwired to the constant zero. The instruction set features four core instruction formats (R, I, S, U) and two variant formats (B for branches and J for jumps), all aligned on 32-bit boundaries. Immediate values in B and J types are jumbled to simplify decoding and reduce hardware complexity. Key arithmetic and logical instructions include ADD, SUB, AND, OR, XOR, and their immediate variants, while control flow is handled by BEQ, BNE, BLT, BGE, JAL, and JALR. RV32I serves as the mandatory base for all RISC-V implementations, enabling emulation of other extensions except the 'A' atomic extension.

## Key Claims

- RV32I consists of 47 instructions.
- 32 general-purpose registers, each 32-bit, with x0 hardwired to zero.
- Four core instruction formats: R, I, S, U; two additional variants: B and J.
- Branch and jump immediate values are jumbled to simplify decoding and reduce mux costs.
- Shift instructions (SLL, SRL, SRA) and set-less-than operations (SLT, SLTU) are included.
- Load and store instructions are I-type and S-type respectively.
- JALR stores return address in rd; if not needed, rd can be x0.

## Relationships

- The [[xuantie_c908]] implements the RV32GCB variant, which builds upon RV32I with compressed instructions and the vector extension.
- The [[k230]] SoC integrates a core that uses the RISC-V 64GCB profile, extending the 64-bit variant RV64I which is itself an extension of the RV32I base.
- The [[mlir_xdsl_rvv_gemm_codegen_recipe]] generates code for RISC-V vector extensions that require the base RV32I or RV64I instruction set.
- [[mos2_risc_v_prototype]]: a 2D-material (MoS2) 32-bit microprocessor that implements this full RV32I instruction set as its target ISA.

## Sources

- https://varshaaks.wordpress.com/2021/07/19/rv32i-base-integer-instruction-set/
