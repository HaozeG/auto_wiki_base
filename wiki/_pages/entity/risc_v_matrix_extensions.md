---
cold_start: false
created: '2026-06-26'
inbound_links: 2
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://cfp.riscv-europe.org/eu-summit-2026/talk/BLF3DX/
- https://www.securerisc.org/RISCVIME/
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec
- https://github.com/riscv-stc/riscv-matrix-spec
tags:
- risc-v
- isa-extension
- matrix
- ai-acceleration
type: entity
updated: '2026-06-26'
---

# RISC-V Matrix Extensions (IME, VME, AME)

RISC-V Matrix Extensions are a family of proposed ISA extensions for the RISC-V architecture that provide hardware acceleration for matrix operations, primarily targeting artificial intelligence and machine learning workloads. The family includes the Integrated Matrix Extension (IME), which leverages existing vector registers without adding new architected state; the Vector Matrix Extension (VME), which extends vector operations for matrix multiplication; and the Attached Matrix Extension (AME), which introduces dedicated matrix tile registers and operations executing as part of the program instruction stream. A fourth related extension, XuanTie's custom Matrix-Multiply Extension (MME), is an open-source implementation that served as a precursor to the AME task group. The AME design is based on the Outer Product Accumulator (OPA) concept, which efficiently computes outer products of vectors to build matrix products. The proposal document (version 0.2-draft-20241016) is maintained on SecureRISC.org. As of 2026, IME and VME are converging on specification freeze.

## Key Claims

- IME and VME are converging on specification freeze as of the 2026 RISC-V EU Summit; AME is at an earlier stage.
- IME uses only existing vector registers and introduces no new architected state for matrix data.
- VME extends vector operations for matrix multiply-accumulate (MMAC), building directly on RVV register file and instruction encoding space.
- AME introduces its own matrix (tile) registers and is based on the Outer Product Accumulator (OPA) concept; it targets scalability across application classes.
- The XuanTie MME (open-source: XUANTIE-RV/riscv-matrix-extension-spec) is a working implementation that preceded and informed the AME task group.
- The proposal is versioned 0.2-draft-20241016 and licensed Creative Commons Attribution 4.0 International.
- Alternative proposals store matrices A, B, C directly in the Vector Register File with a fused matrix multiply-add instruction, avoiding new register state entirely.

## Relationships

- [[risc_v_vector_extension]]: IME and VME explicitly build on RVV; matrix extensions are the natural successor to vector extensions for AI matrix workloads.
- [[risc_v_vme]]: Dedicated page for the VME specification and its GitHub repository.
- [[rva23_profile]]: Matrix extensions are candidates for inclusion in future RISC-V profiles beyond RVA23.
- [[fpga_riscv_isa_extension_nn_inference]]: FPGA prototypes implement ad hoc matrix extensions; the RISC-V Matrix Extensions standardize this at the ISA level.
- [[sifive_intelligence_x280]]: SiFive 2nd Gen adds FP4/FP8 vector support; matrix extension ratification would enable dedicated matrix tiling on future SiFive cores.

## Sources

- EU Summit 2026 talk (BLF3DX): IME/VME specification freeze status, family overview.
- SecureRISC.org proposal (v0.2-draft-20241016): IME/AME design options, OPA concept, licensing.
- XUANTIE-RV/riscv-matrix-extension-spec: XuanTie MME open-source implementation.
- riscv-stc/riscv-matrix-spec: RISC-V STC group matrix specification repository.
