---
canonical_name: OpenGeMM Benchmark Results
aliases:
- OpenGeMM throughput and efficiency measurements
subtype: null
tags: []
hardware_targets:
- OpenGeMM
- Gemmini
workloads:
- GeMM (various computational matrix sizes from CNN and Transformer workloads)
datatypes:
- unspecified (likely fixed-point or integer GeMM)
metrics:
- normalized throughput (GOPS/µm²)
- speedup factor (3.58x to 16.40x)
- system efficiency (TOPS/W)
toolchains:
- Chisel (for accelerator generation)
- unspecified RISC-V toolchain
hardware_versions:
- OpenGeMM (parameterized, Chisel-coded, 2024)
- Gemmini (output stationary and weight stationary modes)
software_versions: []
measurement_method: Simulation-based evaluation reported in the arXiv preprint. Comparison
  against Gemmini in both output-stationary (OS) and weight-stationary (WS) modes
  across a wide variety of GeMM workload matrix sizes.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/139c70528d55cca1.md
- https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
source_url: https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
fetched_at: '2026-07-02T11:29:00.701437+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# OpenGeMM Benchmark Results

The OpenGeMM benchmark result reports normalized throughput and system efficiency measurements for the OpenGeMM accelerator platform compared to the Gemmini open-source accelerator. The data originates from the preprint "OpenGeMM: A High-Utilization GeMM Accelerator Generator with Lightweight RISC-V Control and Tight Memory Coupling" (arXiv:2411.09543, November 2024). The evaluation covers a wide variety of GeMM workloads representative of CNN and Transformer inference tasks. OpenGeMM achieves hardware utilization between 81.89% and 99.34% across these workloads. On normalized throughput (GOPS/µm²), OpenGeMM demonstrates a 3.58x to 16.40x speedup over Gemmini in both output-stationary and weight-stationary configurations. The measured system efficiency is 4.68 TOPS/W. These results indicate that the platform's three optimization mechanisms—configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access—effectively reduce overhead and improve data movement efficiency.

## Key Claims

- Hardware utilization of 81.89% to 99.34% across diverse CNN and Transformer workloads.
- Normalized throughput speedup of 3.58x to 16.40x over Gemmini (OS and WS modes).
- System efficiency of 4.68 TOPS/W.
- Speedup and efficiency gains are attributed to three hardware mechanisms.

## Measurement Context

- Hardware version: OpenGeMM (parameterized, Chisel-coded, 2024), Gemmini (reference, modes: OS and WS)
- Software/toolchain version: Not explicitly specified; accelerator generated via Chisel, comparison from original Gemmini implementation.
- Workload shape: Various GeMM matrix sizes extracted from CNN and Transformer neural network models.
- Metric: Normalized throughput (GOPS/µm²), system efficiency (TOPS/W)
- Method: Simulation-based measurement; comparison against published Gemmini baseline.
- Evidence strength: reported (from preprint, not independently reproduced).

## Relationships

- [[opengemm]]: This benchmark is the primary performance characterization of the OpenGeMM platform.
- [[cpa-factored-gemmini-systolic-array]]: Both involve performance comparisons to Gemmini; the CPA factoring is an orthogonal optimization applicable to Gemmini architecture.
- [[earth-shifting-based-vector-memory-access]]: Both benchmarks evaluate hardware optimizations for memory access efficiency in RISC-V based designs.

## Sources

- [OpenGeMM arXiv preprint](https://arxiv.org/abs/2411.09543)
- [ResearchGate entry](https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling)
