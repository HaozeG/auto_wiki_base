---
canonical_name: Voyager Development Platform
aliases:
- Andes Voyager
- Voyager board
- Voyager micro-ATX
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/b71d020937eafbcc.md
- https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/
source_url: https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/
fetched_at: '2026-07-02T11:46:38.276939+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Voyager Development Platform

The Voyager Development Platform is a micro-ATX motherboard developed by Andes Technology, based on the QiLai SoC. The board features an Andes QiLai SoC with four AX45MP 64-bit RISC-V cores clocked up to 2.1 GHz and an NX27V vector processor clocked up to 1.4 GHz. It supports up to 16GB DDR4 via a 288-pin UDIMM socket at speeds of DDR4-1600/2400/3200. Storage options include a 256GB/512GB M.2 2280 NVMe SSD via a PCIe Gen4 x2 slot, a microSD card socket (push/pull type), and 2MB SPI flash. The board provides three PCIe Gen4 expansion slots: one x16 slot (x4 electrical) for a graphics card, and two x4 slots (each x2 electrical) for USB 3.0, Ethernet, or additional storage. Debugging and connectivity include a USB Type-C port for AICE-MICRO JTAG debugging and another USB Type-C port for UART. Power is supplied via a 24-pin ATX connector requiring a 300+ Watt power supply. The board measures 244×244mm in a micro-ATX form factor with a 14-layer PCB. A CR2032 battery is included for RTC, and 10-position DIP switches are used for SoC strap configuration. The platform is supported by OpenSUSE Linux, AndeSight toolchains, and AndesAIRE NN SDK for AI model deployment.

## Key Claims

- Micro-ATX form factor (244×244mm, 14-layer PCB).
- Supports up to 16GB DDR4-3200 via UDIMM socket.
- Three PCIe Gen4 slots: one x16 (x4 electrical) and two x4 (each x2 electrical).
- Storage: M.2 NVMe SSD (up to 512GB), microSD card, 2MB SPI flash.
- Debug interfaces: USB Type-C JTAG and USB Type-C UART.
- Power: 24-pin ATX, 300+ Watt requirement.
- Software: OpenSUSE Linux, AndeSight tools, AndesAIRE NN SDK.

## Relationships

- [[pulp-platform]]: related via shared platform.

- [[andes-qilai]]: The SoC that powers the Voyager platform.
- [[kendryte-k230-neural-network-benchmarks]]: A benchmark page for a different RISC-V AI SoC, provides performance comparison context for AI workloads on development boards.
- [[earth-shifting-based-vector-memory-access]]: An optimization recipe for vector memory access that could be relevant to optimizing workloads on the NX27V vector processor.

## Sources

- [Andes QiLai SoC and Voyager Development Platform - CNX Software](https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/)
