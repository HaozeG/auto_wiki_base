---
canonical_name: SiFive Intelligence X390
aliases:
- X390
- SiFive X390
subtype: null
tags:
- RISC-V
- SiFive
- AI
- ML
- vector
hardware_targets:
- SiFive Intelligence X390
toolchains:
- RISC-V GNU toolchain
- LLVM
constraints:
- RISC-V Vector Extension
- 1024-bit VLEN
- 512-bit DLEN
- dual vector ALU option
- VCIX
- data types: Int8, Int16, Int32, FP16, FP32, FP64, Q8.8, Q15
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.85
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/29110787b8f23bbd.md
- https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
source_url: https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
fetched_at: '2026-07-02T04:25:16.741148+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# SiFive Intelligence X390

The SiFive Intelligence X390 is a RISC-V vector-optimized processor core designed for artificial intelligence and machine learning workloads. It is the successor to the X280 core and belongs to SiFive's Intelligence series, which specializes in accelerating large-vector instructions. The X390 delivers a fourfold improvement in vector performance over its predecessor, primarily achieved by doubling the vector length. It supports a maximum vector register length (VLEN) of 1024 bits with a data path width (DLEN) of 512 bits. The core can be configured with either single or dual vector arithmetic logic units. It integrates SiFive's Vector Coprocessor Interface Extension (VCIX), enabling developers to implement custom vector instructions and acceleration hardware. The X390 supports a broad range of data types suitable for AI and ML, including Int8, Int16, Int32, FP16, FP32, FP64, and Q8.8 to Q15 fixed-point formats. The core is designed for deployment in heterogeneous SoC configurations, often paired with SiFive's Performance series cores like the P870.

## Key Claims

- Quadruple vector performance compared to X280.
- 1024-bit VLEN with 512-bit DLEN.
- Supports single or dual vector ALUs.
- VCIX for custom vector instructions and hardware acceleration.
- Data type support: Int8, Int16, Int32, FP16, FP32, FP64, Q8.8, Q15.
- Targets AI/ML workloads with large-vector operations.

## Optimization-Relevant Details

- ISA/profile: RISC-V with Vector Extension.
- Vector/matrix/accelerator support: Configurable 1- or 2-vector ALU; VCIX interface.
- Memory/cache/TLB/DMA: Not specified in source.
- Compiler/toolchain support: Standard RISC-V toolchains (GCC, LLVM) with vector intrinsic support.

## Relationships

- Related RISC-V AI accelerator core: [[xuantie_c908]]
- SoC integrating RISC-V core with AI acceleration: [[k230]]
- SiFive Performance core for heterogeneous pairing: [[sifive_performance_p870]]
- [[xuantie_c907]]: Another RISC-V core with matrix extension for AI workloads.

## Sources

- https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
