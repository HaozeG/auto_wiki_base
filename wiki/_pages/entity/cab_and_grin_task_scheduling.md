---
canonical_name: CAB and GrIn Task Scheduling
aliases:
- CAB
- GrIn
- Choose-between-Accelerate-the-fastest-and-Best-fit
- Greedy-Increase
subtype: null
tags:
- scheduling
- heterogeneous
- optimal policy
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.3
sources:
- raw/cache/00c65ffce189cd51.md
- https://www.researchgate.net/publication/321718938_Task_Scheduling_for_Heterogeneous_Multicore_Systems
source_url: https://www.researchgate.net/publication/321718938_Task_Scheduling_for_Heterogeneous_Multicore_Systems
fetched_at: '2026-07-02T04:56:05.290847+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# CAB and GrIn Task Scheduling

CAB (Choose-between-Accelerate-the-fastest-and-Best-fit) and GrIn (Greedy-Increase) are task scheduling policies proposed by Chen and Marculescu (2017) for heterogeneous multicore systems. CAB is an optimal scheduling policy derived from queueing theory for systems with two processor types, such as CPU+GPU combinations, while GrIn is a near-optimal heuristic that extends to any number of processor types, achieving performance within 1.6% of the optimal bound. Both policies are designed to work with any task size distribution and processing order, making them applicable to a wide range of heterogeneous computing environments. The policies are validated through extensive simulations and real-platform experiments on a CPU-GPU system, where they demonstrate significant improvements over classic load-balancing approaches: 1.08x to 2.24x better performance and 1.08x to 2.26x better energy efficiency in simulation, and 2.37x to 9.07x better performance in experimental tests. These scheduling techniques are particularly relevant for modern heterogeneous architectures such as those found in RISC-V AI accelerators, where efficient task mapping across different core types (e.g., CPU with vector extension and NPU) can dramatically affect throughput and power consumption.

## Key Claims

- CAB provides an optimal scheduling policy for two-processor-type heterogeneous systems, mathematically formulated using queueing theory.
- GrIn solves the near-optimal policy for any number of processor types with a performance guarantee within 1.6% of the optimal.
- Both policies are general and practical, handling any task size distribution and processing order.
- Compared to classic load-balancing, CAB/GrIn achieve 1.08x~2.24x better performance and 1.08x~2.26x better energy efficiency in simulation.
- Experimental implementation on a real CPU-GPU platform yields 2.37x~9.07x better performance.

## Relationships

- The scheduling policies can be applied to heterogeneous RISC-V platforms like [[xuantie_c908]], which combines different core configurations (RVV-capable and scalar) for AI workloads.
- The dual-core architecture of [[k230]] (one core at 800 MHz with 64GCB, another at 1.6 GHz with RVV 1.0) exemplifies a heterogeneous system where CAB/GrIn could optimize task allocation.
- The policies complement optimization recipes such as [[mlir_xdsl_rvv_gemm_codegen_recipe]], which focuses on kernel-level code generation for specific hardware, by providing a higher-level scheduling layer for multiple kernels.

## Sources

- Chen, Z., & Marculescu, D. (2017). Task Scheduling for Heterogeneous Multicore Systems. arXiv:1712.03209.
