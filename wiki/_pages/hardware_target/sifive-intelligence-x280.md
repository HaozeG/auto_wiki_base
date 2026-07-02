---
canonical_name: SiFive Intelligence X280
aliases:
- SiFive X280
- X280
- SiFive Intelligence X280 CPU
- SiFive Intelligence X280 processor
- SiFive Intelligence X280 Gen 2
- SiFive X280 Gen 2
- X280 Gen 2
subtype: null
tags: []
hardware_targets:
- SiFive Intelligence X280
toolchains:
- TensorFlow Lite (optimized implementation)
constraints:
- 64-bit RISC-V ISA
- 512-bit vector length (VLEN)
- 8-stage dual-issue in-order scalar pipeline
- Multi-core capable
- SiFive Intelligence Extensions for ML workloads
scorecard:
  novelty_delta: 0.5
  claim_density: 0.6
  self_containedness: 0.5
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/c5c394256e12c188.md
- https://ueno-staging.scs-test.sifive.com/cores/intelligence-x280
- raw/cache/5074cb278ce52a88.md
- https://www.cnx-software.com/2021/04/27/sifive-intelligence-x280-64-bit-risc-v-processor-integrates-ai-extensions/
- raw/cache/c53bc4be49df185e.md
- https://semiiphub.com/ip/multi-core-capable-risc-v-processor-ip-with-vector-extensions-ip-23509
- raw/cache/6f90249d1ea76f58.md
- https://riscv.org/blog/sifive-enhances-popular-x280-processor-ip-to-meet-accelerated-demand-for-vector-processing-sifive/
source_url: https://ueno-staging.scs-test.sifive.com/cores/intelligence-x280
fetched_at: '2026-07-02T09:49:04.007724+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# SiFive Intelligence X280

The SiFive Intelligence X280 is a 64-bit multi-core RISC-V processor core introduced in 2021 as part of SiFive's Intelligence X200 Series. It features a powerful combination of the RISC-V Vector Extension with a 512-bit vector length (VLEN) and the proprietary SiFive Intelligence Extensions, tightly integrated with an 8-stage dual-issue in-order scalar pipeline. The X280 is optimized for AI/ML compute at the edge, offering a balance of performance and power efficiency for neural network inference and other machine learning workloads. It includes an optimized TensorFlow Lite implementation, enabling efficient deployment of ML models on embedded and edge devices. The core is designed to be multi-core capable, allowing scalable performance in system-on-chip designs for applications such as computer vision, natural language processing, and intelligent sensors.

## Key Claims

- 64-bit RISC-V ISA with Vector Extension (512-bit VLEN) and SiFive Intelligence Extensions.
- 8-stage dual-issue in-order scalar pipeline.
- Multi-core capable architecture.
- Optimized TensorFlow Lite implementation for ML workloads.
- AI/ML compute optimization targeting edge applications.
- Part of the SiFive Intelligence X200 Series (second generation).

## Optimization-Relevant Details

- ISA/profile: RISC-V (64-bit) with Vector Extension (RVV, version not specified in source) and SiFive Intelligence Extensions.
- Vector/matrix/accelerator support: 512-bit vector length; SiFive Intelligence Extensions for custom ML instructions; VCIX (Vector Coprocessor Interface eXtension) likely available based on family-wide features.
- Memory/cache/TLB/DMA: Not specified in the available documentation.
- Compiler/toolchain support: Optimized TensorFlow Lite implementation; expected support from RISC-V GCC/LLVM with vector extension support.

## Relationships

- [[sifive-intelligence-x160-gen-2]]: A 32-bit sibling core in the same SiFive Intelligence family, targeting similar AIoT workloads with narrower vector width.
- [[gemmini]]: An open-source systolic array generator for RISC-V-based AI accelerators, representing a complementary approach to the X280's vector-based compute.

## Sources

- [SiFive Intelligence X280 - SiFive](https://ueno-staging.scs-test.sifive.com/cores/intelligence-x280)
- [Introduction To The SiFive Intelligence X280 (CNX Software, 2022)](https://www.cnx-software.com/2022/06/01/sifive-intelligence-x280-risc-v-processor-ai-ml-compute/)
