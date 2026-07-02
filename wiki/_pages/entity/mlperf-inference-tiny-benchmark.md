---
canonical_name: 'MLPerf Inference: Tiny'
aliases:
- MLPerf Tiny
- MLCommons MLPerf Tiny
- MLPerf Inference Tiny Benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/ebc35cb1d94b1e30.md
- https://mlcommons.org/benchmarks/inference-tiny/
source_url: https://mlcommons.org/benchmarks/inference-tiny/
fetched_at: '2026-07-02T11:02:49.881922+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# MLPerf Inference: Tiny

The MLPerf Inference: Tiny benchmark suite is a standardized benchmarking framework developed by MLCommons for measuring the performance of machine learning inference on small embedded systems and microcontrollers. It defines a set of tasks including image classification on CIFAR-10 using ResNet, person detection on COCO using MobileNet, keyword spotting on Speech Commands using DS-CNN, anomaly detection on ADMOS Toy Car, and streaming wake-word detection. Benchmarks are primarily single-stream, measuring inference latency, and also evaluate model quality metrics such as accuracy or AUC. The suite supports optional energy benchmarking. Submissions are organized into Closed and Open divisions to compare hardware/software platforms while allowing innovation. Results are categorized by availability into Available, Preview, and Research/Development/Internal (RDI).

## Key Claims

- The suite measures latency and model quality for tinyML inference tasks.
- Five benchmark tasks are defined: image classification, person detection, keyword spotting, anomaly detection, and streaming wake-word.
- All benchmarks are single-stream, with optional energy measurement.
- Two divisions: Closed (apples-to-apples) and Open (innovation allowed).
- Three availability categories: Available, Preview, RDI.

## Relationships

- [[gap9-vs-stm32f7-odtl-benchmark]]: This benchmark result compares MCU-level platforms on on-device training; MLPerf Tiny provides a complementary inference-focused benchmark standard for similar edge devices.
- [[earth-shifting-based-vector-memory-access]]: While this optimization targets memory access on vector units, MLPerf Tiny benchmarks measure inference latency on systems that may incorporate similar optimizations.

Insufficient context for additional cross-links; no entity pages exist yet in the wiki that are directly related.

## Sources

- [MLPerf Inference: Tiny benchmark suite](https://mlcommons.org/benchmarks/inference-tiny/)
