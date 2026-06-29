---
cold_start: true
constraints:
- RISC-V V 1.0
- 64-bit
- 22nm technology
- 64 vector lanes
- 8192 double-precision elements per vector register
- 64 Kibit VRF per vreg
- 1.15 GHz
- TT 0.8V 25C
created: '2025-07-15'
hardware_targets:
- AraXL
inbound_links: 1
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/html/2501.10301v1
tags:
- RISC-V
- vector processor
- long vectors
- HPC
- ML
- 22nm
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# AraXL

AraXL is a modular and scalable 64-bit RISC-V V vector processor design targeting long-vector applications for HPC and ML. It is the first RISC-V vector processor architecture able to scale up to 64 double-precision floating-point vector lanes, achieving the maximum Vector Register File (VRF) size of 64 Kibit per vector register permitted by the RISC-V V 1.0 ISA specification. AraXL addresses physical scalability challenges of state-of-the-art vector processors with a distributed and hierarchical interconnect, implemented in a 22-nm technology node. The architecture supports up to 64 parallel vector lanes, each with a double-precision FPU, and reaches a maximum frequency of 1.15 GHz at TT 0.8V 25C.

## Key Claims

- First RISC-V vector processor to scale to 64 lanes with 8192 double-precision elements per vector register.
- Achieves maximum VRF size of 64 Kibit/vreg as permitted by RISC-V V 1.0.
- Uses a distributed and hierarchical interconnect to overcome physical scalability limitations.
- Implemented in 22-nm technology; 64-lane instance has 3.8x the area of a 16-lane instance.
- Peak performance: 146 GFLOPs on HPC/ML kernels with >99% FPU utilization.
- Energy efficiency: 40.1 GFLOPs/W at 1.15 GHz (TT, 0.8V, 25C).

## Optimization-Relevant Details

- ISA/profile: RISC-V V 1.0 (64-bit)
- Vector/matrix/accelerator support: 64 double-precision FPUs per lane, up to 64 lanes
- Memory/cache/TLB/DMA: Not detailed in available resource; VRF is distributed across lanes
- Compiler/toolchain support: Not specified

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another RISC-V accelerator benchmark providing a comparison point.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – A benchmark for a different RISC-V-based accelerator.

## Sources

- [AraXL paper (arXiv)](https://arxiv.org/html/2501.10301v1)

