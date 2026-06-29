---
cold_start: false
created: '2026-07-11'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.4
  claim_density: 0.5
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2106.07597
- https://github.com/mlcommons/tiny
- https://github.com/mlcommons/tiny_results_v1.1
- https://mlcommons.org/en/inference-tiny-11/
tags:
- TinyML
- benchmark
- machine_learning
- ultra-low-power
- MLPerf
- v1.1
type: entity
updated: '2026-06-29'
---

# MLPerf Tiny Benchmark

MLPerf Tiny is the first industry-standard benchmark suite for ultra-low-power tiny machine learning (TinyML) systems, developed through a collaborative effort of more than 50 organizations from industry and academia. The suite addresses the lack of a widely accepted and easily reproducible benchmark for these systems, providing standardized measurements for accuracy, latency, and energy of machine learning inference. It features a modular design that allows submitters to showcase the benefits of their products across the ML deployment stack in a fair and reproducible manner. The benchmark suite includes four representative workloads: keyword spotting, visual wake words, image classification, and anomaly detection, enabling comprehensive evaluation of TinyML system trade-offs.

## Key Claims

- MLPerf Tiny is the first industry-standard benchmark for ultra-low-power TinyML systems.
- The benchmark suite resulted from collaboration of more than 50 organizations from industry and academia.
- Measurements cover accuracy, latency, and energy of machine learning inference.
- The modular design ensures fair and reproducible submissions regardless of where a product falls on the ML deployment stack.
- Four specific benchmarks are included: keyword spotting, visual wake words, image classification, and anomaly detection.

## Version History

The benchmark suite has been released across multiple versions: v0.5, v0.7, v1.0, and v1.1. For v1.1, results are hosted on GitHub at `mlcommons/tiny_results_v1.1` following a structured directory format: `division (closed/open) → submitting organization → systems` (with `system_desc_id.json`, Submission Checklist, Energy-Hookup.pdf), `code (benchmark_name → implementation_id)`, and `results (system_desc_id → benchmark → performance, accuracy, energy)`. Official certified results are published at mlcommons.org/en/inference-tiny-11/.

## Relationships

- [[Sipeed_MAIX_series]] – A development board for TinyML that could be evaluated using MLPerf Tiny.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A RISC-V AI SoC benchmark, providing contrast with the TinyML target class of MLPerf Tiny.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Benchmark results for a TinyML accelerator on RISC-V directly relevant to the MLPerf Tiny workload domain.

## Sources

- [arXiv: MLPerf Tiny Benchmark](https://arxiv.org/abs/2106.07597)
- [MLPerf Tiny GitHub Repository](https://github.com/mlcommons/tiny)
- [GitHub: mlcommons/tiny_results_v1.1](https://github.com/mlcommons/tiny_results_v1.1)
- [MLPerf Tiny v1.1 official results](https://mlcommons.org/en/inference-tiny-11/)
