---
cold_start: false
constraints:
- 16 big RISC-V cores (run Linux)
- 752 baby RISC-V cores (programmable with C kernels, no OS)
- 5 baby RISC-V cores per Tensix core
- 10x 400Gbps Ethernet ports
- 512 GB/s aggregate Ethernet bandwidth
- Statically scheduled Network-on-Chip (NoC)
- Tile math engine (32x32 tiles)
- Vector math engine
- Off-chip DRAM support (inferred)
- Ethernet-based scale-out with mesh topologies
created: '2026-06-28'
hardware_targets:
- Tenstorrent Blackhole
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.8
sources:
- https://www.servethehome.com/tenstorrent-blackhole-and-metalium-for-standalone-ai-processing/
tags:
- Tenstorrent
- RISC-V
- AI accelerator
- Ethernet
toolchains:
- TT-Metalium
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Blackhole

Tenstorrent Blackhole is a standalone AI computer chip designed for AI inference and compute workloads, featuring a RISC-V-based architecture with 16 big RISC-V cores capable of running Linux and 752 smaller programmable "baby" RISC-V cores that execute C kernels without an operating system. The chip includes Tensix cores, each containing five baby RISC-V cores, a tile math engine for 32x32 matrix operations, and a vector math engine. Blackhole is built for Ethernet-based scale-out, integrating ten 400Gbps Ethernet ports providing 512GB/s of aggregate bandwidth, and uses a statically scheduled network-on-chip for intra-chip communication. The chip is programmed using Tenstorrent's low-level software stack, TT-Metalium, which is open source and exposes the hardware directly to developers for custom compute and data movement kernels.

## Key Claims

- The chip contains 16 big RISC-V cores that can run a full Linux operating system.
- There are 752 baby RISC-V cores, programmable using C kernels but not running an OS.
- Each Tensix core includes five baby RISC-V cores, a tile math engine, and a vector math engine.
- The tile math engine operates on 32x32 tiles for matrix operations.
- Ten 400Gbps Ethernet ports provide 512 GB/s total bandwidth for scale-out networking.
- Ethernet-based scale-out supports 2x2 and 4x8 mesh topologies (Galaxy configuration).
- The network-on-chip is statically scheduled.
- TT-Metalium is the low-level, open-source programming model for compute and data movement kernels.
- A single user compute kernel is automatically compiled to three RISC-V threads.
- Hardware-enabled flow control synchronizes kernels.

## Optimization-Relevant Details

- ISA/profile: RISC-V (big cores run Linux; baby cores are proprietary RISC-V implementations programmable in C).
- Vector/matrix/accelerator support: Tile math engine (32x32 tiles), vector math engine, baby RISC-V cores for data movement and compute.
- Memory/cache/TLB/DMA: Off-chip DRAM support with emphasis on keeping data local in SRAM; memory access via DMA and statically scheduled NoC.
- Compiler/toolchain support: TT-Metalium SDK for custom kernel development; automatic compilation to three RISC-V threads.

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] \- A different RISC-V-based AI accelerator benchmark, highlighting contrasting architecture and measurement methods.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] \- A chiplet-based RISC-V AI SoC benchmark, showing an alternative approach to AI acceleration.

Note: Insufficient entity pages are present in the wiki context for additional cross-links; the two linked pages are benchmark result pages rather than entity pages.

## Sources

- [ServeTheHome: Tenstorrent Blackhole and Metalium For Standalone AI Processing](https://www.servethehome.com/tenstorrent-blackhole-and-metalium-for-standalone-ai-processing/)
