---
canonical_name: GCC 15 vs Clang 21 Auto-vectorization on SpacemiT X60
aliases:
- RVV compiler auto-vectorization comparison
- GCC15 Clang21 RVV benchmark
subtype: null
tags:
- SpacemiT X60
- GCC 15
- Clang 21
- LLVM 21
- RVV 1.0
hardware_targets:
- SpacemiT X60
workloads:
- SGEMM
- DGEMM
- Qsim (quantum circuit simulator)
- four additional HPC/ML proxy applications (not individually named)
datatypes:
- FP32
- FP64
metrics:
- outperformance count (4/6)
- predication overhead percentage
- stride load cost multiplier
toolchains:
- GCC 15
- Clang 21 (LLVM 21)
hardware_versions:
- Banana Pi BPI-F3 board (SpacemiT K1 SoC)
- SpacemiT X60 core
software_versions:
- GCC 15
- LLVM 21 / Clang 21
measurement_method: Assembly microbenchmarks for performance ceiling calibration and
  perf counter validation; proxy applications executed with hardware performance counter
  monitoring on Banana Pi BPI-F3.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/53f948c53967f26e.md
- https://arxiv.org/abs/2605.10860
source_url: https://arxiv.org/abs/2605.10860
fetched_at: '2026-07-03T17:26:56.722855+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-x60-hardware-target
  reason: This benchmark result is the first published compiler auto-vectorization
    comparison on the SpacemiT X60 core, using the Banana Pi BPI-F3 platform; the
    predication overhead and stride load findings inform optimization details for
    this hardware target
- target: sophon-sg2044-hardware-target
  reason: Both the SpacemiT X60 and the Sophon SG2044 (via C920v2) implement RVV 1.0;
    this benchmark provides data points for compiler performance on an in-order RVV
    implementation, complementing the SG2044's vector processing capabilities
---

# GCC 15 vs Clang 21 Auto-vectorization on SpacemiT X60

This benchmark result compares the auto-vectorization performance of GCC 15 and Clang/LLVM 21 on the RISC-V Vector Extension (RVV) 1.0 hardware of the SpacemiT X60 core, as found in the Banana Pi BPI-F3 development board. The evaluation was conducted by Shi et al. (arXiv:2605.10860) using a suite of assembly microbenchmarks to calibrate performance counters and then measuring six scientific and machine learning proxy applications, including SGEMM, DGEMM, and the Google Qsim quantum circuit simulator. The paper reports that GCC 15 outperforms Clang 21 in four of the six applications, while Clang 21 achieves superior performance only in SGEMM and DGEMM due to more aggressive instruction reduction confirmed through validated perf counters. The study also finds that predication overhead and stride loads pose performance challenges that current compiler cost models do not fully address, and that default LMUL selection is near-optimal, though GCC 15 shows greater potential for gains from larger LMUL tuning.

## Key Claims

- GCC 15 outperformed Clang/LLVM 21 in four out of six RVV auto-vectorized proxy applications on SpacemiT X60 (Banana Pi BPI-F3).
- Clang 21 outperformed GCC 15 only in SGEMM and DGEMM, attributed to more aggressive instruction reduction verified by hardware perf counters.
- Predication overhead and stride loads were identified as performance bottlenecks not yet fully captured by current compiler cost models.
- Default LMUL selection by the compiler is near-optimal on this in-order RVV 1.0 implementation.
- GCC 15 shows greater potential for additional performance improvement through larger LMUL tuning compared to Clang 21.
- This work provides the first evaluation of GCC 15 and LLVM 21 auto-vectorization on real RVV 1.0 hardware.

## Measurement Context

- Hardware version: SpacemiT X60 core (Banana Pi BPI-F3 board, SpacemiT K1 SoC)
- Software/toolchain version: GCC 15, Clang/LLVM 21
- Workload shape: Six proxy applications (SGEMM, DGEMM, Qsim quantum circuit simulator, plus three additional HPC/ML proxy applications not individually named in the source)
- Metric: Comparative performance (GCC outperforms in 4/6, Clang in 2/6); also predication overhead and stride load costs (not numerically quantified in abstract)
- Method: Assembly microbenchmarks for ceiling calibration; proxy application runs with validated hardware performance counters
- Evidence strength: measured

## Relationships

- [[spacemit-x60-hardware-target]]: This benchmark result is the first published compiler auto-vectorization comparison on the SpacemiT X60 core, using the Banana Pi BPI-F3 platform; the predication overhead and stride load findings inform optimization details for this hardware target.
- [[sophon-sg2044-hardware-target]]: Both the SpacemiT X60 and the Sophon SG2044 (via C920v2) implement RVV 1.0; this benchmark provides data points for compiler performance on an in-order RVV implementation, complementing the SG2044's vector processing capabilities.

## Sources

- https://arxiv.org/abs/2605.10860
