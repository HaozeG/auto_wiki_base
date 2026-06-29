---
cold_start: false
constraints:
- 1+8 RISC-V cores (fabric controller + 8 compute cores)
- four-level memory hierarchy with scratchpad memories instead of caches
- DMA-based data movement
- INT8 dot product support
- heterogeneous architecture
created: '2024-02-19'
hardware_targets:
- GAP8 (PULP platform)
inbound_links: 2
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://link.springer.com/article/10.1007/s11227-024-05927-y
tags:
- RISC-V
- PULP
- GAP8
- IoT
- ultra-low power
- edge AI
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# GAP8 Parallel Ultra-Low Power Platform (PULP)

The GAP8 parallel ultra-low power platform (PULP) is a heterogeneous multi-core RISC-V processor designed for Internet of Things (IoT) edge computing. It integrates a fabric controller (FC) core and a cluster of eight compute cores, all based on the RISC-V instruction set architecture (ISA). Unlike conventional processors with hardware-managed cache hierarchies, the GAP8 features a four-level memory hierarchy built from scratchpad memories, requiring explicit DMA-based data transfers for efficiency. The processor provides special support for 8-bit integer (INT8) dot products, making it suitable for deep learning inference tasks at the edge. The fabric controller coordinates data movement and control, while the compute cluster handles arithmetic operations in a parallel, multi-threaded fashion. This architecture targets low power consumption and computational performance for IoT nodes, enabling inference closer to sensors.

## Key Claims

- Heterogeneous 1+8 core architecture: one fabric controller (FC) plus eight compute cores.
- Four-level memory hierarchy using scratchpads instead of traditional hardware caches.
- DMA-based data transfer orchestration for efficient memory access.
- INT8 dot product support for quantized deep learning workloads.
- Designed for ultra-low-power IoT applications with privacy and latency benefits.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific extensions not detailed in source).
- Vector/matrix/accelerator support: No explicit vector extension; relies on scalar dot product and DMA-assisted parallelization.
- Memory/cache/TLB/DMA: Four-level scratchpad hierarchy; DMA transfers managed by fabric controller.
- Compiler/toolchain support: Not specified in available resource.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – Both are RISC-V platforms used for GEMM-based computation, though GAP8 lacks vector extensions and uses scratchpad memory.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another RISC-V platform with GEMM optimization; comparison highlights alternative memory and instruction set approaches.

## Sources

- [Parallel GEMM-based convolution for deep learning on multicore RISC-V processors – Springer](https://link.springer.com/article/10.1007/s11227-024-05927-y)

