---
cold_start: true
created: '2025-07-25'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/html/2507.22451v1
tags:
- RISC-V
- PMU
- Roofline
- LLVM
- performance analysis
- SpacemiT X60
type: entity
updated: '2026-06-29'
---

# LLVM Roofline and PMU Tooling on RISC-V

This entity describes a practical methodology for performance analysis on RISC-V systems, combining a workaround for hardware PMU sampling bugs with a compiler-driven Roofline modeling approach that bypasses PMU dependencies. The methodology targets the SpacemiT X60 processor, where standard event sampling fails due to hardware limitations, and provides an open-source toolchain (miniperf) that automates PMU data correction and LLVM-based instrumentation for deriving operational intensity and throughput metrics. The compiler-driven Roofline tool uses LLVM Intermediate Representation (IR) to compute arithmetic intensity without relying on hardware counters, making it applicable across diverse RISC-V platforms with limited or faulty monitoring capabilities. This integrated toolchain lowers the barrier for effective performance bottleneck analysis on emerging RISC-V hardware, addressing persistent challenges of fragmented tooling and immature hardware features in the RISC-V ecosystem.

## Key Claims

- Identifies a hardware bug in the SpacemiT X60 that prevents standard PMU event sampling for cycles and instructions under Linux perf_event.
- Presents a workaround leveraging observed interactions within the Linux perf_event subsystem to enable reliable sampling for cycles and instructions on the SpacemiT X60.
- Introduces a hardware-agnostic Roofline modeling approach using LLVM instrumentation that derives operational intensity and throughput from application IR, eliminating dependency on hardware PMU counters.
- Provides an open-source toolset (miniperf) that automates the PMU sampling workaround and the compiler-guided Roofline construction into a single workflow.
- The toolchain is designed for practical performance analysis on RISC-V systems with constrained or unreliable hardware monitoring capabilities.

## Relationships

- [[RVV_Autovectorization_Optimization_Insights]] – Related optimization methodology for RISC-V vectorization, showing another approach to performance analysis on RISC-V hardware.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Another RISC-V optimization approach on GAP8 hardware, illustrating the diversity of performance tuning techniques in the ecosystem.
- Insufficient context for additional cross-links; only these two related pages are available in the current wiki context.

## Sources

- [Dissecting RISC-V Performance: Practical PMU Profiling and Hardware-Agnostic Roofline Analysis on Emerging Platforms – arXiv](https://arxiv.org/html/2507.22451v1)
