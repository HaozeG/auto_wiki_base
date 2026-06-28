---
cold_start: true
constraints: []
created: YYYY-MM-DD
hardware_targets:
- Kendryte K210
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.8
  hub_potential: 0.3
  novelty_delta: 1.0
  self_containedness: 1.0
sources:
- https://grokipedia.com/page/Sipeed_MAIX_series
tags:
- RISC-V
- SoC
- NPU
- edge_AI
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# Kendryte K210

The Kendryte K210 is a dual-core 64-bit RISC-V system-on-chip (SoC) designed for edge AI applications, implementing the RV64GC instruction set architecture with base integer, multiplication/division, atomic operations, single- and double-precision floating-point, and compressed instructions extensions. Each core operates at up to 400 MHz via PLL configuration and includes independent floating-point units. The SoC integrates an Neural Processing Unit (KPU) for convolutional neural network acceleration, 8 MB of on-chip SRAM, and support for up to 128 MB external flash storage. It is manufactured on TSMC's 28nm process and provides interfaces for cameras, displays, and audio, making it suitable for machine vision and hearing tasks in low-power edge devices.

## Key Claims

- Dual-core RV64GC RISC-V CPU at 400 MHz.
- Integrated NPU (KPU) for CNN acceleration.
- 8 MB on-chip SRAM, up to 128 MB external flash.
- Manufactured on TSMC 28nm process.
- Used as the core of the Sipeed MAIX series.
- Includes FPU per core for floating-point operations.

## Optimization-Relevant Details

- ISA/profile: RV64GC (IMAFDC).
- Vector/matrix/accelerator support: KPU for convolution neural networks.
- Memory/cache/TLB/DMA: 8 MB SRAM, external flash up to 128 MB.
- Compiler/toolchain support: Standard RISC-V toolchains (GCC, LLVM) should be compatible; specific SDKs like MaixPy (MicroPython) available.

## Relationships

- [[Sipeed_MAIX_series]] – Development boards based on the K210.

## Sources

- [Grokipedia: Sipeed MAIX series](https://grokipedia.com/page/Sipeed_MAIX_series)
