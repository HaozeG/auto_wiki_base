---
cold_start: true
created: '2025-04-10'
inbound_links: 1
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 1.0
  self_containedness: 1.0
sources:
- https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
tags:
- RISC-V
- T-Head
- XuanTie
- AIoT
- processor
type: entity
updated: '2026-06-28'
---

# XuanTie C908

XuanTie C908 is a RISC-V processor core designed by T-Head Semiconductor, a subsidiary of Alibaba Group, targeting mid-range AIoT applications such as intelligent interaction, augmented and virtual reality (AR/VR), and image/video processing. Released in 2022, it implements the RV64GCB[V] instruction set architecture and is compatible with the RVA22 profile. The core features a high-efficiency, dual-issued, 9-stage in-order pipeline and includes an optional vector processing unit supporting RISC-V Vector Extension 1.0, BF16 operations, and INT4 datatype for AI acceleration. It supports a multi-cluster architecture with each cluster containing 1 to 4 cores, two-level cache with hardware cache coherence and optional ECC, and full RISC-V privileged architecture (Machine, Supervisor, User modes). It can run at frequencies up to 2 GHz and has a dynamic power consumption of 52.8 mW/GHz per core under TSMC’s 12nm process, achieving an energy efficiency ratio improvement of over 20% compared to the earlier XuanTie C906.

## Key Claims

- C908 is a 9-stage dual-issue in-order pipeline processor.
- Supports RV64GCB[V] and RV32 COMPAT mode (first in industry).
- Compatible with RVA22 profile.
- Includes optional Vector Processing Unit (RVV 1.0) with INT4 and vector dot product extension.
- Uses two-level cache system with hardware cache coherency and optional ECC.
- Max frequency: 2 GHz.
- Dynamic power: 52.8 mW/GHz per core under TSMC 12nm.
- Energy efficiency >20% better than C906 in typical scenarios.
- MLPerf tiny V0.7 inference performance up to 3.5 times that of C906.
- Supports Bitmanip 1.0 (zbc), CMO Base extension, Svinval extension.
- Bus interface: AXI4/ACE, Device Coherence Port (DCP), Low Latency Port (LLP).
- ePMP with up to 64 regions, PLIC with up to 1023 interrupt sources.
- Merged into Linux mainline from version 5.19 (RV32 COMPAT support).
- Custom XuanTie extensions: Instruction Memory Attributes Extension (XMAE).

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Benchmark results for the predecessor C910 core.
- [[Sipeed_MAIX_series]] – Another RISC-V AIoT development platform for comparison.
- (Insufficient context for additional cross-links.)

## Sources

- [RISC-V International Blog: XuanTie C908 High-performance RISC-V Processor Catered to AIoT Industry](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
