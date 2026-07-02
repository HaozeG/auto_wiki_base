---
canonical_name: XiangShan Nanhu-vdot
aliases:
- Nanhu-vdot
- XiangShan Nanhu Vector Dot Product
subtype: null
tags: []
hardware_targets:
- XiangShan Nanhu-vdot
toolchains: []
constraints: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/ee9ecdae7041bb64.md
- https://arxiv.org/abs/2409.00661
source_url: https://arxiv.org/abs/2409.00661
fetched_at: '2026-07-02T10:44:29.617156+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# XiangShan Nanhu-vdot

XiangShan Nanhu-vdot is a specialized instruction set processor for edge AI, based on the XiangShan Nanhu high-performance RISC-V core architecture. It extends the RISC-V instruction set with custom vector dot product instructions to accelerate large language model (LLM) inference. The design adds vector dot product calculation units and pipeline processing logic to the baseline XiangShan Nanhu core. Nanhu-vdot targets edge AI applications requiring high performance and low power consumption, addressing digital signal processing needs of edge devices. The processor was validated on FPGA hardware, achieving over four times the speed of scalar methods for vector dot product computations and approximately 30% speedup for GPT-2 model inference through a hardware-software co-design approach, with minimal additional hardware resources and power consumption.

## Key Claims

- Custom RISC-V vector dot product instructions were designed to accelerate LLM inference.
- Implemented on the XiangShan Nanhu open-source RISC-V core architecture.
- FPGA testing showed over 4x speedup for vector dot product computation compared to scalar methods.
- GPT-2 inference achieved approximately 30% speedup via hardware-software co-design over pure software implementation.
- The design incurs almost no additional hardware resource or power consumption (claimed).

## Optimization-Relevant Details

- ISA/profile: RISC-V with custom vector dot product extensions.
- Vector/matrix/accelerator support: specialized vector dot product units added.
- Memory/cache/TLB/DMA: not specified.
- Compiler/toolchain support: not specified.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both are RISC-V-based accelerator optimizations for AI workloads, but target different architectures (Gemmini systolic array vs. XiangShan core).
- Insufficient context for additional cross-links.

## Sources

- [Research on LLM Acceleration Using the High-Performance RISC-V ...](https://arxiv.org/abs/2409.00661)
