---
cold_start: false
created: '2025-03-05'
datatypes: []
evidence_strength: measured
hardware_targets:
- Allwinner D1 (XuanTie C906)
hardware_versions:
- Allwinner D1 with XuanTie C906 at unknown frequency
inbound_links: 0
measurement_method: Benchmarks executed on the Allwinner D1 board using vendor-provided
  compiler, comparing vectorised vs. scalar execution to measure speedup.
metrics:
- vectorisation speedup
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.7
software_versions:
- Xuantie-900-gcc (modified GCC 8.4 for RVV v0.7.1)
sources:
- https://ar5iv.labs.arxiv.org/html/2304.10319
tags:
- RISC-V
- RVV
- Allwinner D1
- XuanTie C906
- RAJA Performance Suite
toolchains:
- Xuantie-900-gcc (vendor-provided)
type: benchmark_result
updated: '2026-06-28'
workloads:
- RAJA Performance Suite (various kernels)
---

# RAJA Performance Suite on Allwinner D1

The RAJA Performance Suite benchmark results on the Allwinner D1 platform, featuring the T-Head XuanTie C906 core with RVV v0.7.1, were reported in Lee et al. (2023) as part of a survey on RISC-V vectorisation for HPC. The suite, which includes multiple computational kernels typical of HPC workloads, was run using the vendor-provided Xuantie-900-gcc compiler. The key finding was that vectorisation provided a reasonable speedup compared to scalar execution, though specific numeric speedup factors are not publicly detailed in the abstract or introduction. The Allwinner D1 also showed favourable performance relative to the StarFive VisionFive V2 board, which uses the SiFive U74 processor without RVV, highlighting the benefit of vector hardware even with a pre-ratification vector extension. This benchmark result is one of the first published measurements on commercially available RVV hardware and serves as a reference for evaluating vectorisation efficiency on early RISC-V vector platforms.

## Key Claims

- RAJA Performance Suite on Allwinner D1 demonstrated reasonable vectorisation speedup using vendor-provided compiler.
- Allwinner D1 performed favourably compared to StarFive VisionFive V2 (SiFive U74, no RVV).
- Benchmarks were run as part of the EPCC RISC-V testbed setup.
- Specific speedup values are not provided in the public abstract but are available in the full paper.

## Measurement Context

- Hardware version: Allwinner D1 SoC with XuanTie C906 core, RVV v0.7.1, clock frequency not specified.
- Software/toolchain version: Xuantie-900-gcc (modified GCC 8.4), Linux kernel (version not specified in source).
- Workload shape: RAJA Performance Suite – a set of HPC-oriented kernels (e.g., matrix operations, stencil, etc.).
- Metric: Vectorisation speedup (ratio of vectorised execution time to scalar execution time).
- Method: Benchmarks executed on the Allwinner D1 board using vendor-provided compiler, with results reported as speedup factors. Comparison against StarFive VisionFive V2 with SiFive U74 (no RVV).
- Evidence strength: measured

## Relationships

- [[XuanTie_C906]] – The processor core used in the Allwinner D1, providing RVV v0.7.1 vector capability.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A SPEC CPU benchmark on a related T-Head core (C910) with RVV v1.0, offering a reference for higher-end RISC-V vector performance.
- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel that could be part of the RAJA suite, demonstrating vectorisation on a different RISC-V vector platform.

## Sources

- [arXiv:2304.10319 Test-driving RISC-V Vector hardware for HPC](https://ar5iv.labs.arxiv.org/html/2304.10319)

