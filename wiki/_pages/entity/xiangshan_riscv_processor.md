---
cold_start: false
created: '2025-04-04'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.8
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://openxiangshan.github.io/index.html
tags:
- risc-v
- open-source
- processor
- research-infrastructure
type: entity
updated: '2026-06-27'
---

# XiangShan: An Open-Source High-Performance RISC-V Processor

XiangShan is an open-source, high-performance RISC-V processor project initially launched in June 2020, developed by the Institute of Computing Technology (ICT) at the Chinese Academy of Sciences. It aims to provide an industry-competitive, publicly accessible processor design that raises the performance ceiling for open-source hardware and serves as a platform for computer architecture research. The project has produced two major generations, codenamed YQH and NH, with the latest version achieving the highest performance among open-source RISC-V processors to date. XiangShan is written in Chisel, a high-level hardware description language, which enhances readability and maintainability. The processor implements a superscalar, out-of-order execution pipeline supporting the RV64GCBK ISA, featuring a high-throughput frontend with advanced branch prediction, a six-width aggressive execution engine, a high-bandwidth load/store unit, and a highly configurable cache system. Beyond the processor itself, the project includes the Minjie agile development platform, a set of open-source tools for hardware development, functional verification, and performance evaluation, enabling researchers to rapidly implement and test architectural innovations.

## Key Claims

- XiangShan was launched in June 2020 and has produced two major generations: YQH and NH.
- The latest XiangShan processor achieves the highest performance of any open-source RISC-V processor as of 2023.
- It is a superscalar, out-of-order RISC-V processor supporting the RV64GCBK ISA (which includes base integer, multiply/divide, atomic, single/double float, compressed, and bit manipulation extensions).
- Microarchitecture features: high-throughput frontend with advanced branch predictor, six-width out-of-order execution engine, high-bandwidth load/store unit, and highly configurable cache hierarchy.
- Written in Chisel, a high-level hardware description language, for improved readability and maintainability.
- The Minjie platform is an open-source agile development infrastructure that accelerates hardware development, verification, and evaluation.
- The project has tape-out status, performance evaluation results, and a future roadmap.
- The tutorial at ASPLOS 2023 covered simulation flows and FPGA prototyping.

## Relationships

(No existing wiki pages to link. Potential future links include [[risc_v_isa]], [[chisel_hdl]], and [[minjie_platform]].)

## Sources

- [XiangShan Tutorial Page (Deprecated)](https://openxiangshan.github.io/index.html)
