---
canonical_name: Andes QiLai
aliases:
- QiLai
- Andes QiLai SoC
subtype: null
tags: []
hardware_targets:
- Andes QiLai
toolchains:
- AndeSight
- AndesAIRE NN SDK
- OpenSUSE Linux
constraints:
- RV64GC (ISA)
- RISC-V Vector Extension (RVV) with VLEN=512
- 7nm TSMC process
- MESI cache coherence protocol
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
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Andes QiLai

The Andes QiLai is a RISC-V AI system-on-chip developed by Andes Technology, integrating a quad-core AX45MP cluster and an NX27V vector processor. The AX45MP cores are 64-bit RV64GC 8-stage superscalar processors clocked at 1.6 GHz (worst-case) to 2.1 GHz (typical), with 32KB L1 instruction and data caches per core and a shared 2MB L2 cache. The NX27V vector processor operates at 1.1 to 1.4 GHz with 512-bit vector registers and supports the RISC-V Vector Extension for AI workloads. The SoC is fabricated on a 7nm TSMC process and has a maximum power consumption of 5W. It includes interfaces such as PCIe Gen4, I2C, UART, GPIO, and memory controllers for DDR4 up to 3200MHz and on-chip SRAM. The QiLai SoC is designed to serve as a heterogeneous software development platform where a Linux SMP system and an RTOS or bare-metal system can run simultaneously, with the NX27V core cooperating with the AX45MP cluster.

## Key Claims

- Quad-core AX45MP RISC-V cluster with 1.6 GHz (worst) / 2.1 GHz (typical) clock speeds.
- NX27V vector processor with 512-bit VLEN, clocked at 1.1 GHz (worst) / 1.4 GHz (typical).
- 5W power consumption under maximum load.
- 7nm TSMC fabrication process.
- Supports up to 16GB DDR4-3200 memory via 64-bit DRAM interface.
- Peripherals: PCIe Gen4 (x4 and x2), I2C, UART, GPIO, PWM, I2S, QSPI, SD.
- Software support: OpenSUSE Linux, AndeSight toolchains, AndesAIRE NN SDK.
- Heterogeneous architecture supports concurrent Linux SMP and RTOS/bare-metal operation.

## Optimization-Relevant Details

- ISA/profile: RV64GC with RISC-V Vector Extension (RVV) VLEN=512, ELEN=64.
- Vector/matrix/accelerator support: NX27V vector processor with 512-bit SIMD width, 512KiB D-cache, 32KiB I-cache.
- Memory/cache/TLB/DMA: 32KB L1 I-cache and D-cache per AX45MP core, 2MB shared L2 cache, 4×512KB SRAM. I/O Coherence Port (IOCP) with synchronous AXI4 (256-bit data width).
- Compiler/toolchain support: AndeSight (IDE and toolchain), AndesAIRE NN SDK (model conversion from PyTorch, ONNX, TensorFlow Lite), OpenSUSE Linux.

## Relationships

- [[voyager-development-platform]]: The micro-ATX development board based on the QiLai SoC.
- [[kendryte-k230-neural-network-benchmarks]]: Another RISC-V AI SoC benchmark page, providing a reference for comparing AI inference performance.
- [[earth-shifting-based-vector-memory-access]]: A vector memory access optimization relevant to the NX27V vector processor's memory subsystem.

## Sources

- [Andes QiLai SoC and Voyager Development Platform - CNX Software](https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/)
