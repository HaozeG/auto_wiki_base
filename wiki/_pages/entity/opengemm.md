---
canonical_name: OpenGeMM
aliases:
- OpenGeMM Accelerator Generator
- OpenGeMM platform
subtype: null
tags:
- GeMM accelerator
- RISC-V
- open-source hardware
- Chisel
- accelerator generator
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/1fd2befcfc900c4c.md
- https://arxiv.org/abs/2411.09543
- raw/cache/0186cfe893db769f.md
- https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
source_url: https://arxiv.org/abs/2411.09543
fetched_at: '2026-07-03T15:22:37.924462+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: Both OpenGeMM and the MLIR-xDSL RVV Code Generation Pipeline target efficient
    GEMM execution on RISC-V platforms, but OpenGeMM achieves this through a configurable
    hardware accelerator generator with tight memory coupling, whereas the MLIR-xDSL
    pipeline uses compiler-driven code generation to produce optimized RVV intrinsics-based
    kernels
- target: c908-wino-gemm-optimization
  reason: OpenGeMM and the C908 Winograd and GEMM Optimization both aim to accelerate
    GEMM/convolution on RISC-V; OpenGeMM provides a general-purpose hardware accelerator
    generator, while the C908 recipe is a hand-tuned software library optimization
    specific to the XuanTie C908 core using SHL
---

# OpenGeMM

OpenGeMM is an open-source acceleration platform for deep neural network inference on resource-constrained edge devices, jointly demonstrating high efficiency and high utilization. The platform consists of a parameterized Chisel-coded General Matrix Multiply (GeMM) accelerator, a lightweight RISC-V processor for control, and a tightly coupled multi-banked scratchpad memory for data staging. To boost GeMM core utilization and overall system efficiency, OpenGeMM introduces three mechanisms: configuration pre-loading, which overlaps setup with computation; input pre-fetching with output buffering, which hides memory latency; and programmable strided memory access, which supports arbitrary data layouts. The accelerator is designed to be parameterized and configurable at both design time and runtime, targeting diverse CNN and Transformer workloads. Experimental results report hardware utilization ranging from 81.89% to 99.34% across these workloads; note that specific hardware targets and measurement conditions are not detailed in available excerpts. Compared to the state-of-the-art open-source Gemmini accelerator, OpenGeMM achieves a 3.58x to 16.40x throughput speedup on normalized GeMM workloads and a system efficiency of 4.68 TOPS/W. The project is released as open-source hardware and is intended to be configurable and programmable for a wide range of DNN workloads, suitable for edge AI applications requiring both high performance and programmability.

## Key Claims

- OpenGeMM is an open-source acceleration platform comprising a parameterized Chisel-coded GeMM accelerator, a lightweight RISC-V processor, and a multi-banked scratchpad memory.
- Three mechanisms—configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access—enable high utilization.
- Hardware utilization ranges from 81.89% to 99.34% across CNN and Transformer workloads.
- Compared to the open-source Gemmini accelerator, OpenGeMM yields a 3.58x to 16.40x speedup on normalized GeMM throughput.
- System efficiency reaches 4.68 TOPS/W.
- The design is parameterized and configurable at both design time and runtime, combining high reusability and flexibility with high utilization.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: Both OpenGeMM and the MLIR-xDSL RVV Code Generation Pipeline target efficient GEMM execution on RISC-V platforms, representing a hardware-software design trade-off. OpenGeMM achieves this through a configurable hardware accelerator generator with tight memory coupling, whereas the MLIR-xDSL pipeline uses compiler-driven code generation to produce optimized RVV intrinsics-based kernels.
- [[c908-wino-gemm-optimization]]: OpenGeMM and the C908 Winograd and GEMM Optimization both aim to accelerate GEMM/convolution on RISC-V; OpenGeMM provides a general-purpose hardware accelerator generator, while the C908 recipe is a hand-tuned software library optimization specific to the XuanTie C908 core using SHL.

## Sources

- https://arxiv.org/abs/2411.09543
- https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
