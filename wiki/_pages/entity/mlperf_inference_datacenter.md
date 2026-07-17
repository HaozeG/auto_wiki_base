---
canonical_name: MLPerf Inference Datacenter
aliases:
- 'MLPerf Inference: Datacenter'
- MLPerf Datacenter
- Inference Datacenter benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.3
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.7
sources:
- raw/cache/d9f41725d58b14f3.md
- https://mlcommons.org/benchmarks/inference-datacenter/
source_url: https://mlcommons.org/benchmarks/inference-datacenter/
fetched_at: '2026-07-17T09:50:40.662997+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# MLPerf Inference Datacenter

MLPerf Inference Datacenter is a benchmark suite developed by MLCommons to measure how fast systems can process inputs and produce results using a trained model in datacenter environments. The suite defines four test scenarios for representative testing of inference platforms and uses metrics such as latency and throughput. Submissions are divided into Closed and Open divisions, and results are categorized by system availability into Available, Preview, and Research/Development/Internal (RDI) categories. The benchmark also supports power measurement at the wall for the entire system during performance runs. Version 3.1 provides the official set of results from MLCommons.

## Key Claims

- MLPerf Inference Datacenter measures inference performance using trained models with datasets and quality targets.
- Four different test scenarios are defined to cover a variety of inference platforms and use cases.
- Metrics recorded include latency, throughput, and power (energy).
- Closed division requires the same model as the reference implementation for apples-to-apples comparison.
- Open division allows different models or retraining to encourage innovation.
- Results are grouped into Available, Preview, and RDI categories based on component availability.
- Power measurements are taken at the AC wall for the full system duration; references to TDP or power supply ratings are not measured or validated by MLCommons.

## Relationships

No specific relationships to other pages are documented in this source.

## Sources

- [Benchmark MLPerf Inference: Datacenter | MLCommons V3.1](raw/cache/d9f41725d58b14f3.md)
