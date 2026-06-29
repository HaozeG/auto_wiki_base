---
cold_start: false
constraints:
- 9-stage dual-issue in-order pipeline
- RV64GCB[V]
- RVA22 profile
- RVV 1.0
- up to 2 GHz
- cluster of 1 to 4 cores
- two-level cache with ECC
- AXI4/ACE bus
- ePMP up to 64 regions
- PLIC up to 1023 sources
created: '2025-03-05'
hardware_targets:
- XuanTie C908
inbound_links: 2
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
tags:
- RISC-V
- T-Head
- XuanTie
- vector
- AIoT
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# XuanTie C908

The XuanTie C908 is a 64-bit RISC-V processor core designed by T-Head Semiconductor, a subsidiary of Alibaba, targeting mid-range AIoT (Artificial Intelligence of Things) applications. Announced in November 2022, the C908 features a 9-stage dual-issue in-order pipeline and supports the RISC-V Vector Extension 1.0 for AI workload acceleration. It adopts the RV64GCB[V] instruction set with bit manipulation and optional vector operations, and complies with the RVA22 profile for compatibility with Android and other rich operating systems. The core can be configured in clusters of 1 to 4 cores and includes a two-level cache system supporting hardware cache coherency with optional ECC. The bus interface uses AXI4/ACE protocol with optional Device Coherence Port (DCP) and Low Latency Port (LLP). It also includes enhanced physical memory protection (ePMP) with up to 64 regions and a configurable PLIC with up to 1023 interrupt sources. According to T-Head, the C908 delivers 24 to 64% performance improvement over the earlier C906 core based on synthetic benchmarks, and achieves a dynamic power consumption as low as 52.8 mW/GHz per core on TSMC's 12nm process, with an energy efficiency improvement of over 20% compared to the C906 under the same frequency and process constraints. The core supports RV32 COMPAT mode for running 32-bit binaries on 64-bit CPUs and includes XuanTie extensions such as Instruction Memory Attributes Extension (XMAE).

## Key Claims

- 9-stage dual-issue in-order pipeline with RV64GCB[V] ISA and optional vector extensions.
- Compliant with RVA22 profile for Android and rich OS compatibility.
- Cluster of 1 to 4 cores with two-level cache and hardware cache coherency.
- Performance improvement of 24–64% over XuanTie C906 in synthetic benchmarks (Linkpacks, Coremark, Whetstone, Dhrystone).
- Dynamic power consumption of 52.8 mW/GHz per core on TSMC 12nm process.
- Energy efficiency improvement >20% over C906 under same frequency and process.
- RISC-V Vector Extension 1.0 acceleration yields 2–3.5x speedup over C906 for AI workloads (wake word detection, image classification, keyword spotting, anomaly detection) using INT4 data type in MLPerf Tiny v0.7.
- Supports RV32 COMPAT mode for 32-bit binary execution on 64-bit cores (first in industry per T-Head; merged into Linux mainline from v5.19).
- Bus interface: AXI4/ACE with optional DCP and LLP interfaces.
- ePMP with up to 64 regions; PLIC configurable up to 1023 interrupt sources.
- Optional vector unit supports BF16 operations in addition to RVV 1.0 and INT4; released 2022 targeting AIoT applications including AR/VR, intelligent interaction, and image/video processing.
- T-Head Semiconductor is a subsidiary of Alibaba Group.

## Optimization-Relevant Details

- ISA/profile: RV64GCB[V], RVA22 profile, RVV 1.0, XuanTie XMAE extension.
- Vector/matrix/accelerator support: RISC-V Vector Extension 1.0, INT4 data type support for AI workloads.
- Memory/cache/TLB/DMA: Two-level cache with hardware coherency and optional ECC; Sv39/Sv48 virtual address system.
- Compiler/toolchain support: Not specified in source; vendor toolchain presumed.

## Relationships

- [[XuanTie_C906]] – The predecessor core that the C908 outperforms by 24–64% in benchmarks.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – GEMM optimization recipe targeting this core using the SHL library.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – The higher-end XuanTie C910 core with out-of-order pipeline, for comparison.
- [[SiFive_Intelligence_X390]] – A competing RISC-V AI core with vector extensions and similar target applications.

## Sources

- [CNX Software: T-Head XuanTie C908 RISC-V core targets AIoT applications](https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/)
- [RISC-V International Blog: XuanTie C908 High-performance RISC-V Processor Catered to AIoT Industry](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
