---
canonical_name: AraXL
aliases:
- AraXL vector processor
- ETH AraXL
- AraXL RISC-V V processor
subtype: null
tags: []
hardware_targets:
- AraXL
toolchains: []
constraints:
- RISC-V Vector Extension 1.0
- 22nm technology node
- 64 vector lanes
- Max 64 Kibit/vreg VRF
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/389b543e036b0128.md
- https://arxiv.org/html/2501.10301v1
source_url: https://arxiv.org/html/2501.10301v1
fetched_at: '2026-07-02T04:46:11.151365+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: xuantie_c908
  reason: another RISC-V V 1.0 processor core with configurable 128/256-bit VLEN,
    offering a contrast in lane count (2 vs 64) and target market
- target: k230
  reason: an SoC integrating the C908 core, representing a real-world platform for
    RISC-V vector execution
- target: mlir_xdsl_rvv_gemm_codegen_recipe
  reason: an optimization recipe for generating RVV code that could potentially target
    AraXL on software simulation or future implementations
- target: araxl_hpc_ml_benchmark_22nm
  reason: the detailed 22nm peak-performance and energy-efficiency measurements for
    this architecture
---

# AraXL

AraXL is a modular and scalable 64-bit RISC-V V vector processor architecture designed to address the physical scalability challenges of ultra-wide vector processors. It supports up to 64 parallel vector lanes and reaches the maximum Vector Register File size of 64 Kibit per vector register permitted by the RISC-V V 1.0 ISA specification. Implemented in a 22-nm technology node, AraXL achieves a performance peak of 146 GFLOPs on computation-intensive HPC and ML kernels with over 99% FPU utilization, and an energy efficiency of 40.1 GFLOPs/W at 1.15 GHz, TT, 0.8V. The architecture employs a distributed and hierarchical interconnect to overcome wire-dominated scalability limitations seen in designs with more than 8 vector lanes. AraXL is developed by ETH Zürich and the University of Bologna, and targets long-vector applications in HPC and machine learning.

## Key Claims

- 64-bit RISC-V V 1.0 vector architecture with up to 64 vector lanes and 64 Kibit/vreg VRF.
- Distributed hierarchical interconnect enables physical scalability beyond 8 lanes typical of previous designs.
- Implemented in 22-nm technology, achieving 146 GFLOPs peak and 40.1 GFLOPs/W energy efficiency at 1.15 GHz.
- Over 99% FPU utilization on HPC/ML kernels measured.
- Modular design allows instantiation with fewer lanes for smaller area (e.g., 16-lane instance uses 3.8× less area).

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension 1.0 (RVV 1.0).
- Vector/matrix/accelerator support: 64-lane vector unit with FPU for double, single, half precision.
- Memory/cache/TLB/DMA: Distributed interconnect; details not fully disclosed.
- Compiler/toolchain support: Standard RISC-V RVV 1.0 toolchains (GCC, LLVM) presumed compatible.

## Relationships

- [[xuantie_c908]]: another RISC-V V 1.0 processor core with configurable 128/256-bit VLEN, offering a contrast in lane count (2 vs 64) and target market.
- [[k230]]: an SoC integrating the C908 core, representing a real-world platform for RISC-V vector execution.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: an optimization recipe for generating RVV code that could potentially target AraXL on software simulation or future implementations.
- [[araxl_hpc_ml_benchmark_22nm]]: the detailed 22nm peak-performance and energy-efficiency measurements for this architecture.

## Sources

- arXiv:2501.10301v1, "AraXL: A Physically Scalable, Ultra-Wide RISC-V Vector Processor Design for Fast and Efficient Computation on Long Vectors"
