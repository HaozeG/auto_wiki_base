---
cold_start: true
constraints:
- 1024 RISC-V cores
- Non-uniform memory access (NUMA)
- 4MB shared L1 data memory
created: '2025-07-07'
hardware_targets:
- TeraPool (1024 RISC-V cores)
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.5
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.research-collection.ethz.ch/handle/20.500.11850/648454
tags:
- RISC-V
- many-core
- barrier synchronization
- TeraPool
- shared memory
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# TeraPool 1024-Core Cluster

TeraPool is a many-core cluster consisting of 1024 RISC-V processors with non-uniform memory access (NUMA) to a tightly coupled 4 MB shared L1 data memory. Designed for scalable shared-memory parallel processing, TeraPool targets barrier synchronization as a critical performance challenge. The cluster architecture allows different processors to access the shared memory with varying latencies due to its NUMA nature. Research on this platform focuses on implementing efficient barrier synchronization algorithms for large-scale many-core systems, exploring tree-based barriers with tunable radix and partial synchronization techniques to improve performance and energy efficiency. This hardware target provides a testbed for evaluating synchronization overheads in massively parallel RISC-V clusters.

## Key Claims

- TeraPool integrates 1024 RISC-V processors with non-uniform memory access to a tightly coupled 4 MB shared L1 data memory.
- Barrier synchronization is identified as a critical performance and energy overhead source for shared-memory parallel programs on this cluster.
- Performance improvements can be achieved by tuning the radix of tree barriers and introducing partial synchronization mechanisms.
- The architecture is designed as a scalable many-core platform for studying synchronization in RISC-V systems.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific extension set not detailed in available resource).
- Vector/matrix/accelerator support: Not explicitly mentioned; focus is on general-purpose cores with shared memory.
- Memory/cache/TLB/DMA: 4 MB shared L1 data memory with NUMA characteristics; tightly coupled memory architecture.
- Compiler/toolchain support: Not specified in the available resource.

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – A related many-core RISC-V platform (GAP8) with a different memory hierarchy, offering a comparison for synchronization and optimization techniques.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark for a chiplet-based RISC-V AI SoC, providing context for evaluating many-core RISC-V systems.
- Insufficient context for additional cross-links to entity pages.

## Sources

- [Fast Shared-Memory Barrier Synchronization for a 1024-Cores RISC-V Cluster](https://www.research-collection.ethz.ch/handle/20.500.11850/648454)

