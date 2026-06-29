---
cold_start: false
constraints:
- RVV v0.7.1
- minimum VLEN 128 bits (per RVV v0.7.1)
created: '2025-03-05'
hardware_targets:
- XuanTie C906
- Allwinner D1
inbound_links: 4
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://ar5iv.labs.arxiv.org/html/2304.10319
tags:
- RISC-V
- T-Head
- vector
- RVV
- Allwinner D1
toolchains:
- Xuantie-900-gcc (vendor-provided)
type: hardware_target
updated: '2026-06-28'
---

# XuanTie C906

The XuanTie C906 is a RISC-V processor core designed by T-Head Semiconductor that implements the RISC-V Vector Extension (RVV) version 0.7.1, a pre-ratification beta version of the vector standard. As of April 2023, the C906 is the only commercially mass-produced and available hardware supporting RVV, embedded in the Allwinner D1 System-on-Chip. The vector extension provides a minimum vector register length of 128 bits and supports variable vector lengths through LMUL grouping, though it lacks fractional LMUL support present in RVV v1.0. The core has been used in production for edge AI inference workloads, including an MLPerf Tiny Inference submission. Open-source software support for vectorisation on this core relies on vendor-provided toolchains, specifically a modified GCC 8.4 compiler from the Xuantie 900 series, as mainline compilers did not support RVV v0.7.1 at the time of writing.

## Key Claims

- Implements RVV v0.7.1 (beta version, incompatible with v1.0).
- Embedded in the Allwinner D1 SoC, the only mass-produced RVV-capable hardware as of April 2023.
- Vendor-provided Xuantie 900 series GCC 8.4 compiler supports custom intrinsics for v0.7.1.
- Submitted for MLPerf Tiny Inference benchmark.
- Demonstrated reasonable vectorisation speedup on the RAJA Performance Suite using vendor compiler.

## Optimization-Relevant Details

- ISA/profile: RV64GCV (with RVV v0.7.1, not v1.0)
- Vector/matrix/accelerator support: RVV v0.7.1, minimum 128-bit vector registers, LMUL grouping (no fractional LMUL)
- Memory/cache/TLB/DMA: Not specified in source (Allwinner D1 memory hierarchy unknown)
- Compiler/toolchain support: Xuantie-900-gcc (modified GCC 8.4) with custom intrinsics; no mainline GCC/LLVM support for v0.7.1 at time of publication

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Another T-Head core (C910) with RVV v1.0, comparable vector capability but different ISA revision.
- [[fpga-sdv_RISC-V_Vector_Cluster]] – An FPGA-based RVV v0.7 platform, similar vector extension version.
- [[Sipeed_MAIX_series]] – RISC-V edge AI board using a different processor (Kendryte K210) with no vector extension.

## Sources

- [arXiv:2304.10319 Test-driving RISC-V Vector hardware for HPC](https://ar5iv.labs.arxiv.org/html/2304.10319)

