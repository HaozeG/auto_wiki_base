---
cold_start: false
created: '2026-06-26'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.4
  claim_density: 0.75
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.6
sources:
- https://www.embedded.com/first-risc-v-laptop-uses-alibaba-th1520-soc/
tags:
- risc-v
- soc
- alibaba
- t-head
- edge-ai
- china
type: entity
updated: '2026-06-27'
------

# Alibaba TH1520 SoC

The Alibaba TH1520 is a system-on-chip (SoC) developed by Alibaba Group's T-Head business unit, based on the Wujian 600 chip development platform. It integrates a quad-core Xuantie C910 64-bit RISC-V CPU cluster running at up to 2.5 GHz, a neural processing unit (NPU) delivering 4 tera-operations per second (TOPS), and support for 64-bit DDR memory at 4266 MT/s. The TH1520 is designed for edge computing applications including embedded AI inference and was selected as the processor for the ROMA, claimed to be the world's first native RISC-V development laptop. Its announcement in October 2022 marked a notable step for the RISC-V open instruction set architecture, moving it from microcontrollers and development boards into a consumer laptop form factor. The SoC represents a significant example of Chinese domestic chip design in the RISC-V ecosystem, combining general-purpose CPU cores with an on-chip AI accelerator.

## Key Claims

- The TH1520 integrates a **quad-core Xuantie C910 CPU** clocked at up to **2.5 GHz** with 64-bit RISC-V architecture.
- It includes an **NPU rated at 4 TOPS** for edge AI inference workloads.
- Memory interface supports **64-bit DDR at 4266 MT/s**.
- The SoC is built on Alibaba's **Wujian 600 platform**, a development framework tailored for edge SoCs.
- It powers the **ROMA laptop**, which was introduced in October 2022 as the first native RISC-V development laptop.
- The first 100 premium ROMA units were scheduled for delivery in 2022, with production planned to reach **1,000 units in Q1 2023**.

## Relationships

- [[ai_chip_export_controls]] – The TH1520 is a Chinese-manufactured SoC that, while not directly subject to US export controls on high-performance AI chips, represents the type of domestic alternative that has emerged in response to restrictions on importing NVIDIA and AMD accelerators. Its edge AI capabilities (4 TOPS) are far below the performance thresholds of controlled chips, but it illustrates China's parallel path in RISC-V-based computing.
- [[riscv]] – The TH1520 is a high-profile RISC-V application processor demonstrating the ISA's feasibility in portable computing.

## Sources

- https://www.embedded.com/first-risc-v-laptop-uses-alibaba-th1520-soc/
