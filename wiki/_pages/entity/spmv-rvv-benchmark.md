---
canonical_name: SpMV-RVV
aliases:
- laspp/SpMV-RVV
- SpMV-RVV benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.5
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/05303857aee34bfe.md
- https://github.com/laspp/SpMV-RVV/
source_url: https://github.com/laspp/SpMV-RVV/
fetched_at: '2026-07-03T18:12:07.325683+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-x60-hardware-target
  reason: SpMV-RVV's vectorised formats use RVV intrinsics, making the benchmark directly
    applicable to RISC-V cores with RVV support such as the SpacemiT X60, which implements
    RVV 1.0 with a 256-bit vector unit. The benchmark can evaluate SpMV performance
    on the X60 and identify optimization opportunities for sparse linear algebra
- target: xuantie-c906-hardware-target
  reason: The XuanTie C906 core uses a custom 128-bit SIMD unit that is not RVV-compatible;
    therefore SpMV-RVV's RVV vectorised formats cannot be compiled for the C906 without
    modification. The scalar formats, however, can be used to benchmark SpMV performance
    on the C906's in-order pipeline
- target: sophon-sg2044-hardware-target
  reason: The Sophon SG2044 incorporates T-Head XuanTie C920v2 cores with 128-bit
    RVV 1.0 vector units, making it a suitable target for SpMV-RVV's RVV formats.
    The benchmark can provide cycle-level measurements of SpMV kernels on this high-performance
    RISC-V server processor
---

# SpMV-RVV

SpMV-RVV is an open-source benchmark suite for sparse matrix-vector multiplication (SpMV) that implements both scalar and RISC-V Vector Extension (RVV) variants. The project targets EPAC and Orange Pi RV2 RISC-V hardware platforms, with x86 support for development and correctness testing. It iterates SpMV and reports timing, cycle counts via the rdcycle instruction, memory footprint, and FLOP counts for each sparse format. Supported scalar formats include COO, CSR, ELLPACK, and DIA. Vectorised formats include multiple CSR, ELL, and DIA variants implemented using RVV intrinsics, such as vCSRVG (vector-permute), vCSRMG (index-load), vELLVG, and vDIAVG. The benchmark also supports group format aliases, blocking, and binary matrix caching to accelerate repeated runs. Build profiles are pre-configured for GCC and clang on Orange Pi, EPAC, and the Spike simulator, with configurable floating-point precision (float/double) and march string.

## Key Claims

- SpMV-RVV provides both scalar (COO, CSR, ELL, DIA) and vectorised (CSR, ELL, DIA) SpMV implementations, with multiple variants per format.
- Benchmark output includes per-format metrics: rows, columns, blocks, total elements, nonzeros, memory footprint (MB), flops, iteration count, average time, hardware cycle count (rdcycle), and output result mean.
- Pre-configured build profiles exist for Orange Pi (gcc/clang), EPAC (clang), and Spike simulator, enabling easy compilation across targets.
- The tool supports binary matrix caching to skip parsing on repeated runs with the same block size and precision.
- Floating-point precision (float or double) can be selected at build time without editing the Makefile.
- A six-step checklist in the source code guides developers adding new SpMV formats.

## Relationships

- [[spacemit-x60-hardware-target]]: SpMV-RVV's vectorised formats use RVV intrinsics, making the benchmark directly applicable to RISC-V cores with RVV support such as the SpacemiT X60, which implements RVV 1.0 with a 256-bit vector unit. The benchmark can evaluate SpMV performance on the X60 and identify optimization opportunities for sparse linear algebra.
- [[xuantie-c906-hardware-target]]: The XuanTie C906 core uses a custom 128-bit SIMD unit that is not RVV-compatible; therefore SpMV-RVV's RVV vectorised formats cannot be compiled for the C906 without modification. The scalar formats, however, can be used to benchmark SpMV performance on the C906's in-order pipeline.
- [[sophon-sg2044-hardware-target]]: The Sophon SG2044 incorporates T-Head XuanTie C920v2 cores with 128-bit RVV 1.0 vector units, making it a suitable target for SpMV-RVV's RVV formats. The benchmark can provide cycle-level measurements of SpMV kernels on this high-performance RISC-V server processor.

## Sources

- https://github.com/laspp/SpMV-RVV/
