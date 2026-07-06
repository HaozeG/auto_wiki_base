---
canonical_name: XiangShan
aliases:
- XiangShan processor
- XiangShan project
- 香山
- OpenXiangShan
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.6
sources:
- raw/cache/8f18060118756a81.md
- https://openxiangshan.github.io/
- raw/cache/db4e85bfe4899e39.md
- https://github.com/Ergou-ren/XiangShan_docs
- raw/cache/27eb7ecc2a210a77.md
- https://deepwiki.com/OpenXiangShan/XiangShan
source_url: https://openxiangshan.github.io/
fetched_at: '2026-07-03T14:36:35.508614+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# XiangShan

XiangShan (香山) is an open-source, high-performance RISC-V processor designed to be industry-competitive and serve as infrastructure for architecture research. The project is developed by the Institute of Computing Technology, Chinese Academy of Sciences, and employs agile development methodology to accelerate chip design, as documented in a MICRO 2022 publication. Launched in June 2020, XiangShan has produced three major micro-architectures codenamed Yanqihu (YQH, first stable version), Nanhu (NH, second stable version), and Kunminghu (current version under development on the master branch). The processor implements the RV64GCBK ISA extension set and is a superscalar out-of-order design featuring a high-throughput frontend with an advanced branch predictor, a six-width aggressive out-of-order execution engine, a high-bandwidth load/store unit, and a highly configurable cache system. It is written in Chisel, a high-level hardware description language that improves readability and maintainability, and can generate Verilog code for simulation and synthesis. The repository includes submodules for a floating-point unit (fudian), an L2/L3 cache subsystem (huancun), and a difftest co-simulation framework (difftest). According to the project, the latest version of XiangShan achieves the highest performance of any open-source RISC-V processor. The development process is supported by the Minjie platform, an open-source agile development infrastructure that integrates tools for functional verification, performance evaluation, and simulation flow. The processor has been taped out and has a demonstrated FPGA prototype. XiangShan provides official documentation at docs.xiangshan.cc, including a design document for Kunminghu V2R2 and a user guide, all licensed under CC-BY-4.0. Simulation is supported via Verilator with pre-built images for running programs such as CoreMark. The project also offers IDE support (bsp, IDEA) and a troubleshooting guide.

## Key Claims

- XiangShan is an open-source RISC-V processor with three micro-architectures: Yanqihu (YQH), Nanhu (NH), and Kunminghu.
- It implements the RV64GCBK ISA.
- It is a superscalar out-of-order design with a six-width execution engine.
- Features a high-bandwidth load/store unit and configurable cache system.
- Written in Chisel for high readability and maintainability; generates Verilog.
- Achieves the highest reported performance among open-source RISC-V processors.
- The Minjie platform provides agile development infrastructure including functional verification and performance evaluation.
- The project uses agile development methodology (documented in a MICRO 2022 paper).
- Submodules include fudian (floating-point unit), huancun (L2/L3 cache), and difftest (co-simulation framework).
- Documentation is available at docs.xiangshan.cc, licensed under CC-BY-4.0.
- Simulation can be performed with Verilator using pre-built images (e.g., CoreMark).
- IDE support for bsp and IDEA is available.

## Relationships

No specific relationship to visible context pages.

## Sources

- ASPLOS 2023 tutorial abstract, https://openxiangshan.github.io/ (deprecated; redirects to https://xiangshan-doc.readthedocs.io/zh_CN/latest/tutorials/asplos23/).
- https://github.com/Ergou-ren/XiangShan_docs
