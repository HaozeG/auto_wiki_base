---
type: entity
tags:
  - RISC-V
  - matrix extension
  - coprocessor
  - systolic array
  - edge AI
  - open-source
  - low-power
sources:
  - https://arxiv.org/abs/2504.07565
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.85
  hub_potential: 0.75
---

# Quadrilatero RISC-V Matrix Coprocessor

Quadrilatero is an open-source RISC-V programmable systolic array coprocessor for low-power edge AI applications, designed at ETH Zurich and University of Bologna. It implements a streamlined matrix ISA extension atop a RISC-V scalar core, targeting the sub-milliwatt edge inference regime. Post-synthesis results in 65 nm technology show Quadrilatero requires only 0.65 mm² while achieving up to 99.4% FPU utilization on MatMul workloads. Compared to Spatz (a RISC-V vector processor) and Spatz MX (a hybrid vector-matrix processor), Quadrilatero improves area efficiency and energy efficiency for matrix-dominated workloads by eliminating vector register file access overhead. The architecture sits in the design space between pure SIMD vector processors (one dimension of parallelism) and dedicated NPU systolic arrays (inflexible dataflows), offering programmable systolic dataflow with a compact hardware footprint.

## Key Claims

- Post-synthesis area: 0.65 mm² in 65 nm technology (worst-case corner).
- FPU utilization: up to 99.4% on MatMul benchmarks, compared to <80% for vector processor baselines at equivalent tile dimensions.
- Architecture: programmable systolic array coprocessor tightly coupled to a RISC-V scalar host; implements a streamlined matrix ISA extension (not full XuanTie AME or community RVM v0.6.0 — a custom minimalist subset for edge).
- Target workloads: AI/IoT edge inference; matrix multiply is the primary compute kernel.
- Comparison baseline: Spatz (RISC-V vector processor, 65 nm) and Spatz MX (Spatz + MX matrix extension by Perotti et al., 2024); Quadrilatero achieves better area efficiency because systolic dataflow avoids the wide VRF bus required by vector loads.
- Open-source: hardware RTL and ISA definition available (university research project, arXiv 2504.07565, April 2025).
- Design philosophy: vector processors exploit one dimension of parallelism per cycle; systolic arrays exploit two (row × column); Quadrilatero achieves the second without a separate large register file.

## Relationships

- [[RISC-V_Matrix_Extension]] — Quadrilatero implements a custom streamlined matrix ISA; the community RVM/AME spec is the standardization target but not what this paper implements.
- [[XuanTie_AME_ISA]] — XuanTie AME is T-Head's industrial matrix extension for C908/C930/C950; Quadrilatero is an academic edge alternative with smaller area.
- [[RVME_Matrix_Engine]] — another academic RISC-V matrix engine (28 nm, OPA architecture); RVME uses outer-product arrays vs. Quadrilatero's systolic arrays.
- [[Ara_Vector_Processor]] — Ara is a RISC-V vector processor in the same design space; Quadrilatero is an alternative for matrix-dominated workloads where Ara's VRF access overhead is too costly.
- [[Kernel_Dispatch_Decision_Tree_RVV_AME]] — Quadrilatero's 99.4% utilization data point informs the AME vs. RVV dispatch decision: systolic/matrix dataflow reaches near-ideal utilization for GEMM but not GEMV.

## Sources

- Quadrilatero: A RISC-V Programmable Matrix Coprocessor for Low-Power Edge Applications. arXiv:2504.07565 (April 2025).
