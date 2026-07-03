---
canonical_name: XuanTie C908
aliases:
- C908
- T-Head XuanTie C908
- Alibaba XuanTie C908
- XuanTie C908 MLPerf tiny inference vs C906
- C908 MLPerf performance
- C908 inference benchmark
subtype: null
tags: []
hardware_targets:
- XuanTie C908
toolchains:
- GCC (RISC-V toolchain, Linux 5.19+)
- HHB (neural network inference deployment tool)
- SHL (heterogeneous computing library)
constraints:
- RV64GCB[V] instruction set
- Compatible with RVA22 profile
- TSMC 12nm process
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.2
sources:
- raw/cache/f47a619a7b5e17eb.md
- https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
source_url: https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
fetched_at: '2026-07-02T09:40:51.877295+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# XuanTie C908

The XuanTie C908 is a mid-range RISC-V processor core from T-Head Semiconductor (Alibaba Cloud) launched in November 2022. It implements the RV64GCB[V] instruction set and is compatible with the RVA22 profile. The core features a 9-stage dual-issue in-order pipeline with a maximum frequency of 2 GHz and dynamic power consumption of 52.8 mW/GHz per core on a 12nm TSMC process. It includes an optional Vector Processing Unit (VPU) supporting the RISC-V Vector Extension 1.0, IEEE-754 half-precision floating point, BF16 operations, and the Bitmanip 1.0 extension. The C908 is designed for AIoT applications such as intelligent interaction and AR/VR, and it fills the product gap between the high-performance out-of-order C910 and the low-cost single-issue C906.

## Key Claims

- Implements RV64GCB[V] and is compatible with RVA22 profile.
- 9-stage dual-issue in-order pipeline, up to 2 GHz on TSMC 12nm.
- Dynamic power consumption: 52.8 mW/GHz per core.
- Supports RV32 COMPAT mode for 32-bit application porting (merged in Linux 5.19).
- Optional VPU compatible with RISC-V Vector 1.0, including INT4 and vector dot product extensions.
- Multi-cluster architecture with up to 4 cores per cluster, AXI4/ACE bus, DCP and LLP ports.
- Energy efficiency ratio improved more than 20% over C906 at same frequency and process.
- MLPerf Tiny v0.7 inference performance up to 3.5× that of C906.

## Optimization-Relevant Details

- ISA/profile: RV64GCB[V], RVA22, Bitmanip 1.0, Vector 1.0, CMO Base, Svinval, Sv39/Sv48.
- Vector/matrix/accelerator support: Optional VPU with INT4 and dot product extensions; XuanTie proprietary extensions (XMAE).
- Memory/cache/TLB/DMA: Two-level cache system with hardware cache coherency and optional ECC.
- Compiler/toolchain support: Linux mainline 5.19, HHB inference deployment tool, SHL computing library.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: The Gemmini systolic array is a separate accelerator design; no direct architectural overlap but both target RISC-V AI acceleration.
- Insufficient context for additional cross-links; no other RISC-V hardware target pages exist in the wiki.

## Sources

- [XuanTie C908 blog post on RISC-V International](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
