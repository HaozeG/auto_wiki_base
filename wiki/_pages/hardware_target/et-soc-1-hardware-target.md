---
canonical_name: ET-SoC-1
aliases:
- Esperanto Technologies Supercomputer-on-Chip 1
- ET-SOC-1
subtype: null
type: hardware_target
tags: []
sources:
- raw/cache/092a8c8ab5f91b30.md
- https://fuse.wikichip.org/news/4911/a-look-at-the-et-soc-1-esperantos-massively-multi-core-risc-v-approach-to-ai/
hardware_targets:
- ET-SoC-1
toolchains: []
constraints:
- TSMC 7nm
- Over 1000 RISC-V cores
- Targets hyperscaler datacenter
- Ultra-low power consumption
- Designed for AI inference acceleration
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.4
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.3
source_url: https://fuse.wikichip.org/news/4911/a-look-at-the-et-soc-1-esperantos-massively-multi-core-risc-v-approach-to-ai/
fetched_at: '2026-07-03T16:08:21.096382+00:00'
---

# ET-SoC-1

The ET-SoC-1 (Esperanto Technologies Supercomputer-on-Chip 1) is a RISC-V AI inference accelerator chip fabricated on TSMC's 7nm process, integrating 1088 energy-efficient ET-Minion 64-bit in-order RISC-V cores each with a vector/tensor unit, 4 high-performance ET-Maxion 64-bit out-of-order RISC-V cores, and 1 RISC-V service processor. With 24 billion transistors on a 570 mm² die, it delivers peak compute rates of 100 to 200 TOPS while consuming typically less than 20 watts. It is designed for energy-efficient ML recommendation inference in large data centers and is packaged on a Glacier Point v2 accelerator card that houses up to six chips, providing up to 192 GB of DRAM with 822 GB/s bandwidth.

## Key Claims

- Integrates 1,093 RISC-V cores: 1,088 ET-Minion 64-bit dual-threaded in-order scalar cores with custom vector/tensor units, 4 ET-Maxion 64-bit single-threaded superscalar out-of-order cores, and 1 ET-Minion-based Service Processor.
- Fabricated on TSMC 7nm process.
- Targets hyperscaler datacenter inference market.
- Claims to be the world's most efficient commercial RISC-V chip for inference.
- Ultra-low power consumption design for high efficiency.
- Massively parallel, flexible architecture.
- First product from the Esperanto Technologies AI accelerator family.

## Optimization-Relevant Details

- **ISA/profile:** RISC-V with custom vector/tensor extensions; specific ISA-level details not fully public.
- **Vector/matrix/accelerator support:** Custom vector/tensor units integrated into each ET-Minion core.
- **Memory/cache/TLB/DMA:** 140 MB on-die SRAM distributed across the chip. Each 1 MB block is configurable as local L2 cache, part of a chip-wide L3, or globally accessible scratchpad.
- **Memory controllers:** Sixteen 16-bit LPDDR4X controllers at 4,266 MT/s providing 133 GB/s aggregate bandwidth.
- **PCIe interface:** PCI Express Gen4 x8 delivering peak throughput 128 Gbps.
- **SoC hierarchy:**
  - **Neighborhood:** 8 ET-Minion cores + 32 KB shared I-cache.
  - **Shire:** 4 Neighborhoods, 4 MB shared L2/L3 cache, mesh stop interface.
  - **Total:** 34 Minion Shires (1,088 cores) plus PCI Shire and I/O Shire (ET-Maxion cores, Service Processor, Root of Trust, USB, I2C, SPI, UARTs).
- **ET-Minion privileged architecture deviations:** Performance counters moved to shared PMU; `minstret`/`mcycle` always return 0; `satp` CSR shared between harts; `mtvec`/`stvec` alignment to 4 KB; WFI behavior.

## Relationships

No specific relationships to pages in the current context.

## Sources

- https://fuse.wikichip.org/news/4911/a-look-at-the-et-soc-1-esperantos-massively-multi-core-risc-v-approach-to-ai/
- https://github.com/10x-Engineers/et-soc1-docs/blob/main/01_esperanto_soc_overview.md
