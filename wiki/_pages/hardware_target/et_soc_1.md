---
canonical_name: ET-SoC-1
aliases:
- Esperanto ET-SoC-1
- Esperanto Technologies ET-SoC-1
subtype: null
hardware_targets:
- ET-SoC-1
toolchains: []
constraints:
- RISC-V 64-bit
- TSMC 7nm
- vector/tensor unit per ET-Minion core
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/c4008bd42a8db9c8.md
- https://www.readkong.com/page/accelerating-ml-recommendation-with-over-a-thousand-3873022
source_url: https://www.readkong.com/page/accelerating-ml-recommendation-with-over-a-thousand-3873022
fetched_at: '2026-07-02T05:11:19.976172+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# ET-SoC-1

The ET-SoC-1 is a custom chip designed by Esperanto Technologies for accelerating machine learning recommendation workloads. It integrates over one thousand low-power RISC-V processors on a single TSMC 7nm die, along with a distributed on-die memory system. The chip includes 1088 energy-efficient ET-Minion 64-bit in-order cores, each equipped with a vector/tensor unit, and 4 high-performance ET-Maxion 64-bit out-of-order cores for general-purpose tasks. The on-chip SRAM exceeds 160 million bytes, and external memory interfaces support low-power LPDDR4x DRAM and eMMC FLASH. A PCIe Gen4 x8 interface enables host connectivity. The chip targets ML recommendation, which traditionally runs on x86 servers, aiming to provide a more power-efficient alternative using many RISC-V cores with tensor acceleration.

## Key Claims

- Incorporates 1088 ET-Minion 64-bit in-order RISC-V cores with vector/tensor units.
- Includes 4 ET-Maxion 64-bit out-of-order RISC-V cores for general-purpose control.
- Over 160 million bytes of on-chip SRAM for distributed memory system.
- Supports low-power LPDDR4x DRAM and eMMC FLASH external memory.
- Interfaces via PCIe Gen4 x8.
- Fabricated on TSMC 7nm process.
- Performance estimated through internal ML Recommendation benchmark on a full-chip emulation platform (Synopsys Zebu) with clock-level accuracy.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, in-order (ET-Minion) and out-of-order (ET-Maxion) cores; ET-Minion includes vector/tensor unit.
- Vector/matrix/accelerator support: each ET-Minion core has a vector/tensor unit; instruction fetch bandwidth reduction and power reduction features; integer pipeline sleep during tensor instructions; vector transcendental instructions optimized for low-voltage operation.
- Memory/cache/TLB/DMA: distributed on-die SRAM >160 MB; external memory interfaces LPDDR4x and eMMC FLASH; PCIe Gen4 x8 for host communication.
- Compiler/toolchain support: not detailed in available source.

## Relationships

- [[xuantie_c908]]: another RISC-V processor for AI workloads, though using a smaller number of cores with vector extensions.
- [[k230]]: a dual-core RISC-V SoC for AIoT, representing a different approach (fewer cores with dedicated NPU) compared to the many-core design of ET-SoC-1.

## Sources

- https://www.readkong.com/page/accelerating-ml-recommendation-with-over-a-thousand-risc-v/tensor-3873022
