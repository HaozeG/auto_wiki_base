---
cold_start: false
created: '2026-06-28'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.4
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://github.com/mlcommons/inference
tags:
- benchmark
- MLPerf
- MLCommons
- inference
- RISC-V AI accelerator
type: entity
updated: '2026-06-29'
---

# MLPerf Inference Benchmarks

The MLPerf Inference benchmark suite is a standard for measuring how fast systems can run machine learning models in a variety of deployment scenarios. The mlcommons/inference GitHub repository hosts the reference implementations of these benchmarks, maintained by MLCommons, an open industry consortium. The suite is described in the MLPerf Inference benchmark paper, which provides a detailed description of the benchmarks along with their motivation and guiding principles. The repository provides reference code for running the benchmarks and is widely used for evaluating inference performance across different hardware platforms.

## Key Claims

- MLPerf Inference is a benchmark suite for measuring how fast systems can run models in a variety of deployment scenarios.
- The mlcommons/inference GitHub repository provides reference implementations of these benchmarks.
- The benchmark suite is described in a dedicated paper with motivation and guiding principles.
- The repository is maintained by MLCommons.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – related benchmark results for a RISC-V AI SoC, likely using MLPerf-style workloads.
- [[Parallel_GEMM_Convolution_on_GAP8]] – an optimization recipe for a workload that could be benchmarked with MLPerf.
- Note: Insufficient context for additional cross-links to entity pages within the available wiki context.

## Sources

- https://github.com/mlcommons/inference

