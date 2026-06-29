---
cold_start: false
constraints:
- four-issue out-of-order pipeline
- RVA22 profile
- Vector 1.0
- Vector Crypto
- up to 16 cores
- non-inclusive L3 cache
- IOMMU
- AIA
- WorldGuard security
- private L2 caches
- streaming prefetcher
created: YYYY-MM-DD
hardware_targets:
- SiFive Performance P870
inbound_links: 2
needs_summary_revision: true
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
- HPC
- data center
- out-of-order
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# SiFive Performance P870

The SiFive Performance P870 is a high-performance RISC-V processor core targeting data center and high-performance computing applications. It fully supports the RVA22 profile specification, the Vector 1.0 and Vector Crypto extensions, and implements a four-issue out-of-order pipeline tuned for scalable performance. The core achieves a reported 12 SpecINT2k6/GHz, making it the highest performing commercially licensable RISC-V processor. It features private L2 caches with a streaming prefetcher, a non-inclusive L3 cache, and support for IOMMU and AIA extensions. Security is provided by RISC-V WorldGuard technology. The P870 supports coherent multi-cluster configurations of up to 16 cores.

## Key Claims

- Four-issue out-of-order pipeline for scalable performance.
- Full support for RVA22, Vector 1.0, and Vector Crypto.
- Reported performance: 12 SpecINT2k6/GHz.
- Supports up to 16 cores in coherent multi-cluster configurations.
- Private L2 caches, streaming prefetcher, non-inclusive L3 cache.
- Includes IOMMU, AIA, and WorldGuard security.
- Designed for feature-rich OS stacks such as Linux and Android.

## Optimization-Relevant Details

- ISA/profile: RVA22 profile, RISC-V Vector 1.0, Vector Crypto.
- Vector/matrix/accelerator support: 2x 128-bit vector length (VLEN) implementing RVV 1.0.
- Memory/cache/TLB/DMA: Private L2 caches, streaming prefetcher, non-inclusive L3 cache.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[SiFive_Intelligence_X390]] – A sibling SiFive processor focused on edge AI and ML.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A competing high-performance RISC-V core.
- [[Sipeed_MAIX_series]] – Edge AI platform using a different RISC-V processor.

## Sources

- [DFRobot Blog: Top 6 RISC-V Chips with Multi-core Design and AI Accelerator for AI and ML](https://www.dfrobot.com/blog-13462.html)
