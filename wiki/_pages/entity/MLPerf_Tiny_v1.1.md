---
cold_start: true
created: '2025-09-18'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.4
  claim_density: 0.3
  hub_potential: 0.5
  novelty_delta: 0.5
  self_containedness: 0.9
sources:
- https://github.com/mlcommons/tiny_results_v1.1
- https://mlcommons.org/en/inference-tiny-11/
tags:
- MLPerf
- TinyML
- benchmark
- v1.1
type: entity
updated: '2026-06-28'
---

# MLPerf Tiny v1.1

MLPerf Tiny v1.1 is a version of the MLPerf Tiny benchmark suite, which provides a standardized set of deep neural network workloads and benchmarking code to compare inference performance on ultra-low-power embedded devices such as microcontrollers, DSPs, and tiny NN accelerators operating between 10 MHz and 250 MHz with power budgets under 50 mW. The v1.1 results repository on GitHub contains the official submission results and code for this benchmark version, following a structured directory format with closed and open divisions, submitting organization folders, system description JSON files, and separate performance, accuracy, and optional energy results. Final certified results are also published on the MLCommons website. The suite includes four benchmarks: visual wake words (vww), image classification (ic), keyword spotting (kws), and anomaly detection (ad). This version is part of an ongoing series that includes v0.5, v0.7, v1.0, and v1.1, providing a consistent framework for evaluating TinyML systems.

## Key Claims

- MLPerf Tiny v1.1 results are hosted on GitHub at mlcommons/tiny_results_v1.1 with code and results.
- Official results table is available at mlcommons.org/en/inference-tiny-11/.
- Benchmark code and rules are maintained in the mlcommons/tiny repository.
- Submissions follow a required directory structure: division (closed/open) → submitting organization → systems (with system_desc_id.json, Submission Checklist, Energy-Hookup.pdf), code (benchmark_name → implementation_id), and results (system_desc_id → benchmark → performance, accuracy, energy).
- The four benchmark workloads are visual wake words (vww), image classification (ic), keyword spotting (kws), and anomaly detection (ad).
- Previous versions include v1.0, v0.7, and v0.5, each with separate results tables and repositories.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another benchmark result for a RISC-V AI SoC, showing a different benchmark class (not TinyML) but relevant for comparison of AI inference performance.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Benchmark results for a TinyML accelerator on RISC-V, directly relevant to the TinyML domain that MLPerf Tiny covers.
- Insufficient context for additional cross-links to entity pages in the current wiki state.

## Sources

- [GitHub README: mlcommons/tiny_results_v1.1](https://github.com/mlcommons/tiny_results_v1.1)
- [MLPerf Tiny v1.1 official results](https://mlcommons.org/en/inference-tiny-11/)
- [MLPerf Tiny benchmark repository](https://github.com/mlcommons/tiny)
