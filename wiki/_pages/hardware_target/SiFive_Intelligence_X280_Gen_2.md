---
cold_start: false
constraints:
- 8-stage dual-issue in-order pipeline
- 512-bit vector register length (256-bit DLEN)
- RVV 1.0 support
- RVA23 support
- SSCI interface
- VCIX interface
- up to 48-bit addressing
- multi-core up to 4 cores per cluster
- multi-cluster configuration
- HW support of BF16
- vector crypto
created: '2025-03-25'
hardware_targets:
- SiFive Intelligence X280 Gen 2
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.7
  self_containedness: 0.7
sources:
- https://www.sifive.com/cores/intelligence-x200-series
tags:
- RISC-V
- SiFive
- AI
- vector
- edge_computing
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# SiFive Intelligence X280 Gen 2

The SiFive Intelligence X280 Gen 2 is a 64-bit RISC-V processor core designed for artificial intelligence and machine learning workloads at the edge. It features an 8-stage dual-issue in-order superscalar pipeline with 512-bit vector register length (256-bit data path width) and implements the RISC-V Vectors v1.0 (RVV 1.0) specification along with SiFive Intelligence Extensions for accelerating AI/ML operations. The second-generation core adds support for the RVA23 profile, an improved memory subsystem with enhanced latency tolerance, hardware support for BF16 datatype, vector crypto instructions, and a new SSCI interface alongside the existing VCIX interface. The core is built on the silicon-proven U7-Series core and supports coherent multi-core configurations up to 4 cores per cluster, with multi-cluster expansion.

## Key Claims

- 512-bit vector register length (256-bit data path width) with decoupled vector pipeline.
- 8-stage dual-issue in-order pipeline.
- Supports RISC-V Vectors v1.0 (RVV 1.0) and SiFive Intelligence Extensions.
- New in second generation: RVA23, improved memory subsystem, BF16 hardware support, vector crypto, SSCI interface.
- Supports integer datatypes INT8 through INT64 and floating-point datatypes BF16, FP16, FP32, FP64.
- Coherent multi-core configuration up to 4 cores per cluster, multi-cluster capable.
- Linux capable with 64-bit RISC-V ISA and up to 48-bit addressing.
- Optimized software stack includes IREE MLIR AI/ML framework and TensorFlow Lite, with hundreds of neural network models ported.
- Core is based on the silicon-proven SiFive U7-Series core.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V with RVA23 profile, RVV 1.0, and SiFive Intelligence Extensions.
- Vector/matrix/accelerator support: 512-bit vector register length (256-bit DLEN), decoupled vector pipeline, VCIX for custom vector instructions, SSCI for scalar-vector communication.
- Memory/cache/TLB/DMA: Improved memory subsystem with memory latency tolerance (specific cache sizes not provided in source).
- Compiler/toolchain support: Not specified at compiler level; software stack includes IREE MLIR and TensorFlow Lite.

## Relationships

- [[SiFive_Intelligence_X390]] – Another SiFive AI core in the X300 series with dual vector ALU and higher vector performance.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A competing high-performance RISC-V core with benchmark results for comparison.

## Sources

- [SiFive Intelligence X200 Series product page](https://www.sifive.com/cores/intelligence-x200-series)

