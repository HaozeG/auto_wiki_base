---
cold_start: true
constraints:
- RV64GC
- 12-stage pipeline
- up to 2.5 GHz
- Sv39 MMU
- XIE extensions
- XMAE extensions
- up to 8 MB L2 cache
- PLIC up to 1023 sources
- JTAG debug
created: '2025-03-10'
hardware_targets:
- XuanTie C910
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/
tags:
- RISC-V
- T-Head
- XuanTie
- high-performance
- out-of-order
toolchains:
- GNU toolchain
type: hardware_target
updated: '2026-06-28'
---

# T-HEAD XuanTie C910

The C910 is a RISC-V compatible 64-bit high performance processor developed by T-Head Semiconductor Co., Ltd. It delivers industry-leading performance in control flow, computing and frequency through architecture and micro-architecture innovations. The C910 processor is based on the RV64GC instruction set and implements the XIE (XuanTie Instruction Extension) technology. C910 adopts a state of the art 12-stage out-of-order multiple issue superscalar pipeline with high frequency, IPC, and power efficiency. C910 supports hardware cache coherency with clusters of 1-4 cores, the AXI4 bus interface, a device coherence port, Sv39 virtual address system with XMAE (XuanTie Memory Attributes Extension), standard CLINT and PLIC interrupt controllers, and RV-compatible debug interface and performance monitors.

## Key Claims

- Based on RV64GC ISA with custom XIE and XMAE extensions.
- 12-stage out-of-order multiple-issue superscalar pipeline.
- Supports up to 4 cores per cluster with hardware cache coherency (MOESI protocol).
- L1 instruction cache: up to 64 KB, 2-way set-associative, VIPT.
- L1 data cache: up to 64 KB, 2-way set-associative, PIPT.
- L2 cache: configurable 256 KB to 8 MB, 16-way, PIPT, with optional ECC.
- Frequency range: 2 – 2.5 GHz.
- Performance: 6 DMIPS/MHz (O2), 7 Coremark/MHz (O3).
- Power: 200 µW/MHz.
- Area: 1.137 mm² (MP2) / 0.398 mm² (core).
- FPU supporting RISC-V F and D extensions, IEEE 754-2008 compliant.
- MMU: Sv39 with 2048-entry TLB, hardware page table walker.
- PLIC: up to 1023 interrupt sources, 32 priority levels, 8 targets.
- JTAG debug: multi-core, software breakpoints, register access.
- Official software ecosystem: GNU toolchain, Linux kernel, QEMU.
- Custom extensions: XIE (instruction extension) and XMAE (memory attributes extension) for PTE-level attributes.

## Optimization-Relevant Details

- ISA/profile: RV64GC plus XuanTie custom extensions (XIE, XMAE). No standard vector extension (RVV) support.
- Vector/matrix/accelerator support: None beyond FPU; custom XIE may include specialized instructions.
- Memory/cache/TLB/DMA:
  - L1 I-cache: VIPT, 2-way, 64 B line, 128-bit read from L2.
  - L1 D-cache: PIPT, 2-way, 64 B line, 128-bit read/write paths.
  - L2: PIPT, 16-way, configurable size, ECC optional, data prefetch.
  - uTLB: 32-entry I-uTLB, 17-entry D-uTLB.
  - Shared TLB: 2048-entry, 4-way.
  - Hardware page table walker for Sv39.
  - Device coherence port (DCP) for external coherent masters.
- Compiler/toolchain support: GNU toolchain (officially contributed), CDS IDE (Eclipse-based), ICE and CK-Link Pro debug hardware.

## Relationships

- [[fpga-sdv_RISC-V_Vector_Cluster]] – Both are RISC-V hardware targets, though the fpga-sdv cluster targets vector workloads with a different microarchitecture.
- [[GEMM_with_RISC-V_Vector_Extension]] – The GEMM workload kernel implemented with the RISC-V Vector Extension may be adaptable to the C910's custom ISA, though the C910 lacks standard RVV support.

## Sources

- [T-HEAD XuanTie C910 RISC-V – RISC-V School](https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/)
