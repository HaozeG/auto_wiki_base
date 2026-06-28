---
cold_start: true
constraints:
- Local scratchpad memories per core
- Static compile-time schedule for shared memory access
- Central management core for external memory access
- Vicuna vector co-processor integration
created: YYYY-MM-DD
hardware_targets:
- Custom RISC-V multicore vector processor with Vicuna co-processor
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://arxiv.org/html/2410.10340v1
tags:
- RISC-V
- vector processor
- real-time
- neural network
- predictable execution
- Vicuna
toolchains:
- Compiler-based deployment toolchain (described in paper)
type: hardware_target
updated: '2026-06-28'
---

# RISC-V Predictable Multicore Vector Processor

The Custom RISC-V Multicore Vector Processor for Real-Time Neural Network Inference is a proposed hardware architecture designed to enable timing-predictable execution of neural network workloads on RISC-V systems. The architecture integrates multiple predictable scalar cores, each augmented with a Vicuna vector co-processor for SIMD operations, and each equipped with its own local scratchpad memory to avoid contention. A central management core orchestrates access to a shared external memory using a static schedule computed at compile-time, eliminating runtime interference. The accompanying compiler exploits the fixed data flow of neural networks and worst-case execution time (WCET) estimates of subtasks to compute this schedule, enabling a composable WCET analysis from subtask estimates, data transfer times, and shared memory access latencies. This work-in-progress targets real-time systems such as automated driving where both high performance and predictability are required.

## Key Claims

- The architecture consists of multiple predictable vector processors with local scratchpad memories.
- A central management core facilitates access to shared external memory through a static schedule calculated at compile-time.
- The compiler exploits fixed data flow of neural networks and WCET estimates of subtasks to compute the schedule.
- The Vicuna vector co-processor is an integral component of the implementation.
- The approach aims to close the gap between performance and predictability in real-time neural network inference.
- The overall WCET estimate can be obtained from subtask WCET estimates, data transfer times, and access times of shared memory.

## Optimization-Relevant Details

- ISA/profile: RISC-V scalar core with Vicuna vector co-processor (timing-predictable vector unit).
- Vector/matrix/accelerator support: Vicuna co-processor supporting vector operations; no specific VLEN or element width reported in source.
- Memory/cache/TLB/DMA: Local scratchpad memories per core; shared external memory accessed via central management core with static schedule; no caches or TLBs mentioned.
- Compiler/toolchain support: Custom compiler for static schedule generation based on neural network data flow and WCET estimates.

## Relationships

- [[fpga-sdv_RISC-V_Vector_Cluster]] – Both are RISC-V vector processing platforms with a focus on timing predictability.
- [[GEMM_with_RISC-V_Vector_Extension]] – Neural network inference kernels (such as GEMM) are relevant workloads for this architecture.
- [[SiFive_Intelligence_X390]] – Another RISC-V processor with vector extensions for AI workloads, though optimized for average-case performance rather than predictability.
- [[Sipeed_MAIX_series]] – Edge AI platform using a different RISC-V processor with integrated NPU, contrasting with the predictable design approach.

## Sources

- [arXiv paper: Work-in-Progress: Real-Time Neural Network Inference on a Custom RISC-V Multicore Vector Processor](https://arxiv.org/html/2410.10340v1)

