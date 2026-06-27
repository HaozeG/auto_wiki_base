---
type: entity
tags: [risc-v, AI-accelerator, many-core, inference, hardware]
sources:
  - https://www.servethehome.com/esperanto-et-soc-1-1092-risc-v-ai-accelerator-solution-at-hot-chips-33/
  - https://fuse.wikichip.org/news/4911/a-look-at-the-et-soc-1-esperantos-massively-multi-core-risc-v-approach-to-ai/
  - https://www.hpcwire.com/2021/08/27/esperanto-silicon-in-hand-champions-the-efficiency-of-its-1092-core-risc-v-chip/
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Esperanto ET-SoC-1

The Esperanto ET-SoC-1 is a massively parallel AI inference accelerator chip developed by Esperanto Technologies, containing 1,092 RISC-V processor cores on a single 7nm die. Rather than using a GPU or dedicated matrix accelerator, the ET-SoC-1 employs a heterogeneous RISC-V core design: 1,088 low-power "ET-Minion" in-order cores, each equipped with its own custom vector/tensor unit, plus four high-performance out-of-order "ET-Maxion" cores for control and scheduling. The chip integrates over 160 Mb of on-chip SRAM and is designed to run at under 20W, making it one of the earliest production demonstrations of RISC-V custom extensions applied to commercial AI inference at scale.

## Key Claims

- The ET-SoC-1 contains 1,088 ET-Minion cores (each with a custom vector/tensor unit) and 4 ET-Maxion out-of-order cores on a single TSMC 7nm die with over 160 Mb of on-chip SRAM, targeting operation at under 20W per chip.
- Six ET-SoC-1 chips assembled on a Glacier Point V2 PCIe card yield 6,552 RISC-V cores total, 192 GB of DRAM, at approximately 120W total card power.
- Peak card performance is rated at 835.6 TOPS (INT8) or approximately 210 teraFLOPS at half precision, establishing it as an early high-density RISC-V inference accelerator.
- Compared to Intel Xeon as a baseline, Esperanto claimed 59× performance and 123× performance-per-watt on recommendation network workloads, representing a fundamental power-efficiency argument for many-core RISC-V over general-purpose CPUs.
- Esperanto reported up to 50× improvement on recommendation networks and up to 30× for image classification versus Intel Xeon, based on gate-level simulation and hardware emulation prior to full silicon validation.

## Relationships

- [[risc_v_vector_extension]] — ET-Minion cores use custom RISC-V vector/tensor extensions, demonstrating the extensibility model at scale
- [[riscv_open_ai_acceleration]] — ET-SoC-1 is a key reference point for the many-core RISC-V inference accelerator design paradigm

## Sources

- ServeTheHome Hot Chips 33 coverage: https://www.servethehome.com/esperanto-et-soc-1-1092-risc-v-ai-accelerator-solution-at-hot-chips-33/
- WikiChip architectural deep-dive: https://fuse.wikichip.org/news/4911/a-look-at-the-et-soc-1-esperantos-massively-multi-core-risc-v-approach-to-ai/
- HPCwire silicon validation report: https://www.hpcwire.com/2021/08/27/esperanto-silicon-in-hand-champions-the-efficiency-of-its-1092-core-risc-v-chip/
