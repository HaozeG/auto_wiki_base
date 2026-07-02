---
canonical_name: XpulpNN
aliases: []
subtype: null
tags: []
hardware_targets:
- PULP Cluster (8 cores, GF22FDX)
workloads:
- QNN convolution
datatypes:
- int2
- int4
metrics:
- speedup
- energy efficiency (TOPs/s/W)
toolchains: []
hardware_versions:
- GF22FDX 8-core cluster
software_versions: []
measurement_method: Comparison of QNN convolution kernels on a parallel cluster implementing
  the proposed extensions vs a baseline cluster supporting only 8-bit SIMD instructions.
  The cluster is fully implemented in GF22FDX technology.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/26a782f184814ce6.md
- https://arxiv.org/abs/2011.14325
source_url: https://arxiv.org/abs/2011.14325
fetched_at: '2026-07-02T12:04:14.015493+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# XpulpNN: Benchmark Results on Parallel Cluster in GF22FDX

XpulpNN is a set of lightweight ISA extensions to the RISC-V architecture introduced in a 2020 paper to accelerate heavily quantized neural network (QNN) inference on microcontroller-class cores. The extensions add nibble (4-bit) and crumb (2-bit) SIMD instructions for sum-of-dot-product operations, along with a fused load-dot-product execution paradigm that improves peak MAC/cycle by up to 1.64x. The proposed design is evaluated on a parallel cluster of 8 RISC-V processors synthesized in GF22FDX technology. Compared to a baseline supporting only 8-bit SIMD instructions, QNN convolution kernels using 4-bit operands achieve a 6x speedup, and kernels using 2-bit operands achieve an 8x speedup. The cluster attains a peak system efficiency of 2.22 TOPs/s/W, which is comparable to dedicated DNN inference accelerators and up to three orders of magnitude better than state-of-the-art ARM Cortex-M based microcontroller systems such as the STM32L4 and STM32H7.

## Key Claims

- Nibble (4-bit) and crumb (2-bit) SIMD instructions provide near-linear speedup over 8-bit SIMD for QNN convolution kernels, achieving 6x and 8x speedup respectively on a parallel cluster.
- Fusing the dot product with a load operation improves peak MAC/cycle by up to 1.64x compared to a standard execution scenario.
- The cluster reaches a peak efficiency of 2.22 TOPs/s/W, demonstrating energy efficiency comparable to dedicated DNN accelerators.
- The parallel cluster of 8 processors scales with near-linear performance improvement over a single core.

## Measurement Context

- **Hardware version:** Parallel cluster of 8 RISC-V processors with XpulpNN extensions, implemented in GF22FDX technology.
- **Software/toolchain version:** Not specified in the source.
- **Workload shape:** QNN convolution kernels (exact dimensions not specified; assumed representative of typical microcontroller inference).
- **Metric:** Speedup (ratio of execution time vs. baseline) and energy efficiency (peak TOPs/s/W).
- **Method:** RTL implementation of the cluster; measurements are compared against a baseline cluster that only supports 8-bit SIMD instructions. The numbers are from synthesis results.
- **Evidence strength:** Measured (based on RTL implementation in GF22FDX).

## Relationships

- [[pulp-nn-optimization-recipe]]: PULP-NN is a software library that optimizes quantized neural network inference on PULP clusters using the Xpulp ISA extension (including dot-product instructions). The benchmark results reported for XpulpNN provide the hardware-level performance foundation for the library's measured improvements.

Insufficient context for additional cross-links; only one directly related wiki page is available.

## Sources

- arXiv:2011.14325 - XpulpNN: Enabling Energy Efficient and Flexible Quantized Neural Network Inference for RISC-V (2020)
