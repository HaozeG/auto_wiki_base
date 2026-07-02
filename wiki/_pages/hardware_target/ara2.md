---
canonical_name: Ara2
aliases:
- Ara2 processor
- ETH Zurich Ara2
- Ara2 vector processor
subtype: null
tags: []
hardware_targets:
- Ara2
toolchains: []
constraints:
- RISC-V Vector Extension 1.0 (RVV 1.0)
- 22nm CMOS process
- Configurable 2-16 lanes
- 1.35 GHz maximum frequency
- ~40 FO4 gate critical path
scorecard:
  novelty_delta: 0.95
  claim_density: 0.9
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/8ed2ac43e51297ac.md
- https://arxiv.org/html/2311.07493v2
source_url: https://arxiv.org/html/2311.07493v2
fetched_at: '2026-07-02T04:47:09.593485+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Ara2

Ara2 is an open-source vector processor compliant with the RISC-V V (RVV) 1.0 frozen ISA, developed at ETH Zurich in collaboration with Huawei Zurich Research Center and Stanford University. It is the first fully open-source processor to support the final RVV 1.0 specification. Ara2 implements a multi-lane vector architecture configurable from 2 to 16 lanes, achieving a clock frequency of 1.35 GHz in 22nm technology. The design is characterized by high functional-unit utilization (average 95% on intensive kernels) and state-of-the-art energy efficiency of 37.8 DP-GFLOPS/W at 0.8V. The processor targets data-parallel workloads and includes a scalar core, vector register file, and memory hierarchy typical of vector processors. The open-source nature of Ara2 allows detailed microarchitectural analysis, including critical path analysis (~40 FO4 gates) and PPA characterization across configurations. The processor also supports multi-core clustering, overcoming scalar core issue-rate bottlenecks for short-vector workloads.

## Key Claims

- First fully open-source processor implementing RISC-V V 1.0 frozen ISA.
- Configurable vector width via 2–16 lanes with 1.35 GHz clock frequency in 22nm.
- Average functional-unit utilization of 95% on computationally intensive data-parallel kernels.
- Energy efficiency of 37.8 DP-GFLOPS/W at 0.8V supply.
- Critical path of approximately 40 FO4 gates.
- Multi-core cluster (eight 2-lane Ara2 cores) achieves >3× performance improvement over a 16-lane single-core on 32×32×32 matrix multiplication, with 1.5× better energy efficiency.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension 1.0 (RVV 1.0)
- Vector/matrix/accelerator support: Multi-lane vector architecture (2–16 lanes), vector register file for data reuse.
- Memory/cache/TLB/DMA: Not publicly detailed; general vector processor memory hierarchy.
- Compiler/toolchain support: Standard RISC-V GCC/LLVM toolchains with RVV 1.0 support.

## Relationships

- [[xuantie_c908]]: Another open-source processor implementing RVV 1.0, but with a different microarchitecture and target application domain.
- [[k230]]: A RISC-V SoC integrating a C908 core with RVV 1.0, serving as a comparison point for open-source vector implementations.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe for generating RVV code that could be validated on Ara2 hardware.
- [[ara2_22nm_vector_benchmarks]]: the detailed 22nm measurement results (utilization, energy efficiency, multi-core scaling) for this processor.

## Sources

- arXiv:2311.07493v2, "Ara2: Exploring Single- and Multi-Core Vector Processing with an Efficient RVV 1.0 Compliant Open-Source Processor"
- DOI: 10.1109/TC.2024.3388896
