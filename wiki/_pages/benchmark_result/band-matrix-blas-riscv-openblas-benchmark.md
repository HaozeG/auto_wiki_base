---
canonical_name: Band Matrix BLAS OpenBLAS RISC-V Benchmark
aliases:
- BLAS band matrix optimization on RISC-V
- OpenBLAS band matrix RISC-V speedup
- RVV 0.7.1 BLAS band matrix
- RVV 1.0 BLAS band matrix
subtype: null
tags: []
hardware_targets:
- Lichee Pi 4A (TH1520 SoC, XuanTie C910 cores, RVV 0.7.1)
- Banana Pi BPI-F3 (SpacemiT K1, RVV 1.0)
workloads:
- Band matrix BLAS operations (four algorithms from OpenBLAS)
datatypes: []
metrics:
- Speedup factor relative to OpenBLAS baseline (1.5x to 10x)
toolchains:
- OpenBLAS (baseline and optimized implementations)
hardware_versions:
- RVV 0.7.1 (Lichee Pi 4A)
- RVV 1.0 (Banana Pi BPI-F3)
software_versions: []
measurement_method: Comparison of optimized OpenBLAS implementations against unmodified
  OpenBLAS baseline on two RISC-V development boards, using RISC-V Vector instructions
  for vectorization.
evidence_strength: reported
scorecard:
  novelty_delta: 0.6
  claim_density: 0.4
  self_containedness: 0.7
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/a3aa0c10af15dafa.md
- https://arxiv.org/html/2502.13839
source_url: https://arxiv.org/html/2502.13839
fetched_at: '2026-07-06T02:10:36.873389+00:00'
type: benchmark_result
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# Band Matrix BLAS OpenBLAS RISC-V Benchmark

The Band Matrix BLAS OpenBLAS RISC-V Benchmark reports performance improvements from optimizing BLAS algorithms for band matrix operations on RISC-V processors using RISC-V Vector (RVV) extensions. The study evaluates four band matrix BLAS algorithms from the OpenBLAS library, optimized through improved vectorization of computationally intensive loops, including the use of vector register grouping. Experiments were conducted on two RISC-V development boards: Lichee Pi 4A, featuring the TH1520 SoC with XuanTie C910 cores supporting RVV 0.7.1, and Banana Pi BPI-F3, featuring the SpacemiT K1 SoC supporting RVV 1.0. The optimized implementations achieved speedups ranging from 1.5x to 10x compared to the unmodified OpenBLAS baseline, depending on the specific band matrix operation. The results demonstrate that targeted vectorization, especially leveraging RVV register grouping, can significantly improve the performance of dense linear algebra kernels on RISC-V hardware, even with the older RVV 0.7.1 specification.

## Key Claims

- Four band matrix BLAS algorithms from OpenBLAS were optimized using improved vectorization of computationally intensive loops.
- Vector register grouping with RVV was successfully used to achieve significant performance gains.
- Speedups of 1.5x to 10x were observed on Lichee Pi 4A (RVV 0.7.1) and Banana Pi BPI-F3 (RVV 1.0) compared to the OpenBLAS baseline.
- The speedup depends on the specific band matrix operation.

## Measurement Context

- Hardware version: Lichee Pi 4A with TH1520 SoC (XuanTie C910 cores, RVV 0.7.1); Banana Pi BPI-F3 with SpacemiT K1 (RVV 1.0).
- Software/toolchain version: OpenBLAS baseline; optimized versions use intrinsics/assembly for RVV.
- Workload shape: Band matrix operations (four BLAS algorithms); specific matrix dimensions not disclosed in the abstract.
- Metric: Speedup factor (1.5x–10x) relative to the original OpenBLAS implementation.
- Method: Benchmarks comparing the time of optimized vs. baseline OpenBLAS implementations on the two target boards.
- Evidence strength: reported (claims from a peer-reviewed paper, not independently verified).

## Relationships

No specific relationship to visible context pages. The hardware targets (Lichee Pi 4A / Banana Pi BPI-F3) differ from [[andes-ax45mpv-hardware-target]], which is an Andes Technology IP core not used in these experiments.

## Sources

- arXiv preprint: https://arxiv.org/html/2502.13839
