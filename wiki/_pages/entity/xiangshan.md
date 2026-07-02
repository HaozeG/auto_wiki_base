---
canonical_name: XiangShan
aliases:
- OpenXiangShan
- 香山
- XiangShan processor
- Open XiangShan
- XiangShan RISC-V
- XiangShan RISC-V CPU
- XiangShan project
- XiangShan high-performance RISC-V
- XiangShan (香山)
subtype: null
tags:
- RISC-V
- open-source processor
- agile development
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.8
sources:
- raw/cache/25f743aa9dc9aa37.md
- https://github.com/OpenXiangShan/XiangShan
- raw/cache/8f18060118756a81.md
- https://openxiangshan.github.io/
- raw/cache/478606518fc3ba24.md
- https://www.servethehome.com/xiangshan-high-performance-risc-v-processors-at-hot-chips-2024/
- raw/cache/ff059b90f8734be6.md
- https://github.com/SigmaOfTy/XiangShan_ty
source_url: https://github.com/OpenXiangShan/XiangShan
fetched_at: '2026-07-02T06:41:53.817293+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# XiangShan

XiangShan (香山) is an open-source high-performance RISC-V processor project developed by the Institute of Computing Technology, Chinese Academy of Sciences. The project aims to demonstrate agile hardware development methodology for high-performance RISC-V processors. XiangShan has produced three stable micro-architectures: Yanqihu (雁栖湖), Nanhu (南湖), and the current Kunminghu (昆明湖) which is under active development. The processor supports the RISC-V instruction set and is designed using the Chisel hardware construction language, with simulation and verification tools including NEMU and difftest. Documentation and user guides are available at docs.xiangshan.cc.

## Key Claims

- Open-source high-performance RISC-V processor project.
- Three stable micro-architectures: Yanqihu (stable since June 2020), Nanhu, and Kunminghu (current development).
- Developed using agile methodology, published at MICRO 2022 with all three artifact evaluation badges (Available, Functional, Reproduced).
- Supports Verilog generation from Chisel source and simulation with Verilator.
- Provides a difftest co-simulation framework for functional verification.
- All documentation licensed under CC-BY-4.0.

## Relationships

- [[k230]]: a RISC-V SoC that integrates a different core (XuanTie C908), contrasting with XiangShan's in-house processor design.
- [[xuantie_c908]]: another open-source RISC-V processor core, representing a different design philosophy (commercial IP vs academic open-source) and target application space.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a compiler optimization recipe for RVV that could potentially target XiangShan's Kunminghu micro-architecture if it supports the RISC-V Vector Extension.
- [[xiangshan_kunminghu]]: the current-generation micro-architecture under active development within this project, implementing the RV64GCBSUHV ISA with vector and hypervisor extensions.

## Sources

- https://github.com/OpenXiangShan/XiangShan
