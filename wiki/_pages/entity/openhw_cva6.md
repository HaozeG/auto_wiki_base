---
cold_start: true
created: 2026-06-27
inbound_links: 3
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://docs.openhwgroup.org/projects/cva6-user-manual/
- https://github.com/openhwgroup/cva6
- https://open-src-soc.org/2022-05/media/slides/4th-RISC-V-Meeting-2022-05-04-14h55-Jerome-Quevremont.pdf
- https://arxiv.org/pdf/2202.03749
tags:
- risc-v
- open-source
- processor
- application-class
- OpenHW
- Linux-capable
type: entity
updated: 2026-06-27
---

# OpenHW Group CVA6 (Ariane)

CVA6 is an open-source, application-class RISC-V processor core maintained by the OpenHW Group, originally developed as "Ariane" by ETH Zürich and the University of Bologna. It implements a 6-stage, single-issue, in-order pipeline supporting the RV64IMACF ISA (with optional RV32 configuration), full M/S/U privilege levels, and sv39 virtual memory — making it capable of booting Linux. Written in SystemVerilog and released under the permissive Solderpad Hardware Licence, CVA6 is designed to be highly configurable: an optional FPU, optional MMU, optional Physical Memory Protection (PMP), separate instruction and data TLBs, a hardware page-table walker (PTW), a branch target buffer (BTB), and a branch history table (BHT) can all be included or excluded. On GlobalFoundries 22 nm FDX silicon CVA6 achieves up to 1.7 GHz clock and up to 40 GOp/s·W peak energy efficiency. Its CoreMark score is approximately 4.0 CoreMarks/MHz. CVA6 has been validated booting buildroot and Yocto Linux, FreeRTOS, and Zephyr. The OpenHW Group positions it as a verified, Linux-capable open-source alternative to proprietary IP for industrial SoC designers, and it has been taped out on GF22FDX and other process nodes. Notably, Ara — ETH Zürich's RVV 1.0 vector processor — uses a CVA6-derived scalar core as its host processor.

## Key Claims

- 6-stage in-order single-issue pipeline; RV64IMACF ISA (also configurable to RV32).
- Supports M/S/U privilege levels and sv39 virtual memory for full Linux boot capability.
- Achieves up to 1.7 GHz on GlobalFoundries 22 nm FDX process.
- Peak energy efficiency up to 40 GOp/s·W on GF 22FDX.
- Approximately 4.0 CoreMarks/MHz performance.
- Includes configurable BTB + BHT branch predictors, separate iTLB/dTLB, and hardware PTW.
- Originally created at ETH Zürich as "Ariane"; transferred to and maintained by OpenHW Group under Solderpad license.

## Relationships

- [[boom_riscv]]: Both are open-source application-class RISC-V cores; BOOM is out-of-order while CVA6 is in-order.
- [[xiangshan_riscv]]: CVA6 and XiangShan represent different points on the open-source RISC-V performance spectrum.
- [[ara_vector_processor]]: Ara's lane controller attaches to a CVA6-derived scalar core as its host processor.
- [[pulp_platform]]: Both originate from ETH Zürich RISC-V research; CVA6 targets application-class workloads while PULP targets ultra-low-power IoT.

## Sources

- https://docs.openhwgroup.org/projects/cva6-user-manual/
- https://github.com/openhwgroup/cva6
- https://arxiv.org/pdf/2202.03749
