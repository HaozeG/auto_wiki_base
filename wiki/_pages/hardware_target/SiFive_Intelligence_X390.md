---
cold_start: true
constraints:
- 8-stage dual-issue in-order pipeline
- 512-bit vector register length
- dual vector ALU
- VCIX technology
- up to 48-bit addressing
- multi-cluster up to 8 cores
- single-core configuration
created: YYYY-MM-DD
hardware_targets:
- SiFive Intelligence X390
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.5
  hub_potential: 0.4
  novelty_delta: 0.6
  self_containedness: 0.4
sources:
- https://www.dfrobot.com/blog-13462.html
tags:
- RISC-V
- SiFive
- AI
- machine learning
- vector
toolchains: []
type: hardware_target
updated: '2026-06-28'
------

# SiFive Intelligence X390

The SiFive Intelligence X390 is a single-core RISC-V processor designed for artificial intelligence and machine learning workloads. It features a 512-bit vector register length, dual vector arithmetic logic units (ALUs) for fourfold improvement in vector computation, and SiFive's VCIX technology enabling customers to incorporate custom vector instructions or acceleration hardware. The core implements an 8-stage dual-issue in-order pipeline, supports up to 48-bit addressing, and can be configured in multi-cluster arrangements of up to 8 cores. The X390 is built on the silicon-proven U7-Series core and includes SiFive Intelligence Extensions for ML workloads. Performance benchmarks report 5.75 CoreMarks/MHz, 3.25 DMIPS/MHz, and 4.6 SpecINT2k6/GHz.

## Key Claims

- Single-core configuration with 512-bit vector register length and dual vector ALU.
- VCIX technology for custom vector instructions or acceleration hardware.
- 8-stage dual-issue in-order pipeline.
- Up to 48-bit addressing and multi-cluster support up to 8 cores.
- Performance benchmarks: 5.75 CoreMarks/MHz, 3.25 DMIPS/MHz, 4.6 SpecINT2k6/GHz.
- SiFive Intelligence Extensions for machine learning workloads.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V ISA with SiFive Intelligence Extensions.
- Vector/matrix/accelerator support: 512-bit vector register length, dual vector ALU, VCIX for custom acceleration.
- Memory/cache/TLB/DMA: High performance vector memory subsystem (details not specified in source).
- Compiler/toolchain support: Not specified.

## Relationships

- [[SiFive_Performance_P870]] – Another SiFive processor targeting HPC and data center.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A competing high-performance RISC-V core.
- [[Sipeed_MAIX_series]] – Edge AI development platform using a different RISC-V processor (Kendryte K210).

## Sources

- [DFRobot Blog: Top 6 RISC-V Chips with Multi-core Design and AI Accelerator for AI and ML](https://www.dfrobot.com/blog-13462.html)
