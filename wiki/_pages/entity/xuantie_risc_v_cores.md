---
cold_start: false
created: '2021-10-20'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.4
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://abopen.com/news/alibabas-t-head-releases-c906-c910-risc-v-cores-under-a-permissive-licence/
tags:
- risc-v
- open-source
- processor-core
- alibaba
- t-head
type: entity
updated: '2026-06-27'
---

# XuanTie RISC-V Cores

The XuanTie family is a series of RISC-V processor cores developed by Alibaba Group's semiconductor division, T-Head. In October 2021, T-Head released the source code for four XuanTie cores—E902, E906, C906, and C910—under a permissive open-source license, believed to be Apache 2.0, making them freely available for use and modification by the global hardware design community. The E902 is a compact 32-bit in-order core targeting low-power embedded and IoT applications; the E906 is a 32-bit core with DSP and SIMD extensions for signal processing workloads; the C906 is a 64-bit in-order core designed for Linux-capable system-on-chips (SoCs) in edge computing and network equipment; and the C910 is a high-performance 64-bit out-of-order superscalar core aimed at computing-intensive applications such as artificial intelligence inference and data analytics. This open-source release was notable because it provided commercial-grade RISC-V designs previously available only under proprietary licensing to the broader ecosystem, accelerating RISC-V adoption in both academia and industry.

## Key Claims

- T-Head (Alibaba) released the RTL source code for four XuanTie RISC-V cores on 20 October 2021: E902 (32-bit, low-power), E906 (32-bit, DSP-enhanced), C906 (64-bit, Linux-capable), and C910 (64-bit, out-of-order).
- The release was made under a permissive open-source license (Apache 2.0), permitting unrestricted use, modification, and redistribution.
- The C910 core implements the RV64GC ISA with vector extensions and a 12-stage out-of-order pipeline, achieving performance comparable to Arm Cortex-A73 in reported benchmarks.
- T-Head promised to release additional RISC-V cores and related infrastructure (e.g., the T-Head Debug Subsystem) following this initial open-source drop.

## Relationships

- [[risc_v_isa]] — XuanTie cores are implementations of the RISC-V ISA; the C910 and C906 are RV64GC, while E-series are RV32.
- [[open_source_hardware_licensing]] — The permissive licensing model distinguishes XuanTie from proprietary RISC-V cores and aligns with the open-hardware movement.
- [[alibaba_t_head]] — The development arm responsible for the XuanTie family.
- [[sifive_performance_cores]] — C910 is often compared to SiFive's U84/U87 in performance targeting Linux and AI workloads.

## Sources

- "Alibaba's T-Head Releases Four RISC-V Cores Under a Permissive Licence" (AB Open, 20 October 2021): https://abopen.com/news/alibabas-t-head-releases-c906-c910-risc-v-cores-under-a-permissive-licence/
