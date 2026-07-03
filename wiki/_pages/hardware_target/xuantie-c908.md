---
canonical_name: XuanTie C908
aliases:
- C908
- T-Head XuanTie C908
- Xuantie C908
- T-HEAD XuanTie C908
- xuantie-c908
- xt-c908
- C908V
- T-Head C908
- GCC Tuning for XuanTie C908 (CanMV-K230)
- XuanTie C908 tuning
- C908 scheduler model
- GCC XuanTie C908 scheduler model
subtype: null
type: hardware_target
tags: []
sources:
- raw/cache/f47a619a7b5e17eb.md
- https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
- raw/cache/d97272025503b0a2.md
- https://csi-nn2.opensource.alibaba.com/zh/blog/C908+accelerates+AI
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
- raw/cache/84a65460eb9d8421.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- raw/cache/17dddb797b6e11ae.md
- https://github.com/FreeRTOS/FreeRTOS-Community-Supported-Demos/blob/main/RISC-V_XUANTIE_C908_GCC/README.md
- raw/cache/25ef1a75fb2012c6.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719234.html
- raw/cache/97c99da680dadacf.md
- https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
hardware_targets:
- XuanTie C908
toolchains:
- HHB
- SHL
constraints:
- TSMC 12nm
- 2 GHz
- 52.8 mW/GHz per core
created: '2022-11-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
source_url: https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
fetched_at: '2026-07-03T13:14:57.990457+00:00'
---

# XuanTie C908

The XuanTie C908 is a mid-range RISC-V processor core developed by T-Head Semiconductor (Alibaba Cloud). It implements the RV64GCB[V] instruction set and is compatible with the RVA22 profile. The core features a 9-stage dual-issue in-order pipeline with branch prediction technologies including a state-of-the-art Branch History Table, Branch Target Buffer, and Return Address Stack, and it utilizes instruction fusion technology to fuse multiple instructions into a single execution. Designed for AIoT applications such as intelligent interaction and AR/VR, the C908 includes an optional Vector Processing Unit (VPU) supporting the RISC-V Vector Extension 1.0 specification. The VPU handles various vector floating-point and integer data formats including INT4, BF16, and half-precision IEEE-754 floating-point. The core uses a two-level cache system with hardware cache coherency and optional ECC, supporting multi-cluster configurations (1 to 4 cores per cluster). The bus interface supports AXI4/ACE protocol with a Device Coherence Port (DCP) and a Low Latency Port (LLP). The C908 can run at up to 2 GHz TSMC 12nm process with dynamic power consumption of 52.8 mW/GHz per core. It also supports the RV32 COMPAT mode for running 32-bit applications.

## Key Claims

- Implements RV64GCB[V] instruction set and is compatible with the RVA22 profile.
- 9-stage dual-issue in-order pipeline with instruction fusion.
- Optional VPU compliant with RISC-V Vector 1.0, supporting INT4, BF16, and half-precision.
- Supports RISC-V Bitmanip 1.0, CMO Base, Svinval, Svnapot, Svpbmt, and XMAE extensions.
- Two-level cache with hardware cache coherency and optional ECC.
- Maximum frequency of 2 GHz under TSMC 12nm; dynamic power 52.8 mW/GHz per core.
- Enhanced Physical Memory Protection (ePMP) with up to 64 regions.
- Platform-Level Interrupt Controller (PLIC) configurable up to 1023 interrupt sources.
- AI software tools: HHB neural network inference deployment tool and SHL high-performance heterogeneous computing library.

## Optimization-Relevant Details

- ISA/profile: RV64GCB[V] (compatible with RVA22); RV32GCB[V] for User mode; extends with Vector 1.0, Bitmanip 1.0, CMO, Svinval.
- Vector/matrix/accelerator support: Optional VPU with RVV 1.0, vector dot product instruction extension, INT4 data type.
- Memory/cache/TLB/DMA: Two-level cache with hardware coherency, Sv39/Sv48 virtual address, AXI4/ACE bus with DCP and LLP interfaces.
- Compiler/toolchain support: HHB deployment tool, SHL library for optimized kernel implementations.

## Relationships

No specific relationship to visible context pages.

## Sources

- [XuanTie C908 Blog Post](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
