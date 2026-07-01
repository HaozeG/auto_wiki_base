---
canonical_name: 'MLPerf Inference: Tiny'
aliases:
- MLPerf Tiny
- MLPerf Inference Tiny benchmark suite
- MLPerf Tiny Benchmark
- MLPerf Tiny inference benchmark suite
- MLPerf Tiny Benchmark (PDF)
subtype: null
tags:
- benchmark
- MLPerf
- TinyML
scorecard:
  novelty_delta: 0.5
  claim_density: 0.3
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/ebc35cb1d94b1e30.md
- https://mlcommons.org/benchmarks/inference-tiny/
- raw/cache/e269be0c87247b59.md
- https://www.researchgate.net/publication/352397004_MLPerf_Tiny_Benchmark
source_url: https://mlcommons.org/benchmarks/inference-tiny/
fetched_at: '2026-07-01T06:28:15.325426+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 0
needs_summary_revision: false
---

# MLPerf Inference: Tiny

MLPerf Inference: Tiny is a benchmark suite developed by MLCommons that measures how fast systems can process inputs and produce results using a trained model on small embedded devices. The suite includes five benchmarks: Image Classification (CIFAR-10, ResNet, Single-stream, 85% Top-1), Person Detection (COCO, MobileNet, Single-stream, 80% Top-1), Keyword Spotting (Speech Commands, DS-CNN, Single-stream and Offline, 90% Top-1), Anomaly Detection (ADMOS Toy Car, Dense, Single-stream, 0.85 AUC), and Streaming Wakeword (Custom Speech Commands + MUSAN, 1D DS-CNN, Streaming, ≤8 false positives and ≤8 false negatives). All benchmarks are single-stream except Keyword Spotting which also offers an Offline mode. Submissions are divided into Closed (apples-to-apples hardware/software comparison) and Open (innovation with any model) divisions. Results are categorized by availability: Available systems contain only purchasable components, Preview systems must be submittable as Available in the next round, and Research/Development/Internal (RDI) systems are experimental or internal-use. The suite also supports optional energy benchmarking, measuring system power or energy per stream per scenario.

## Key Claims

- Defines five standard TinyML benchmarks with specific datasets, models, modes, and quality targets: Image Classification (CIFAR-10, ResNet, 85% Top-1), Person Detection (COCO, MobileNet, 80% Top-1), Keyword Spotting (Speech Commands, DS-CNN, 90% Top-1), Anomaly Detection (ADMOS Toy Car, Dense, 0.85 AUC), and Streaming Wakeword (Custom Speech Commands + MUSAN, 1D DS-CNN, ≤8 false positives and ≤8 false negatives).
- All benchmarks use single-stream mode; Keyword Spotting additionally supports Offline mode.
- Two submission divisions: Closed requires the reference model; Open allows any model or retraining.
- Result categories by availability: Available, Preview, RDI.
- Optional energy benchmarking is supported.

## Relationships

- [[xuantie_c908]] — Potential hardware target for running MLPerf Inference: Tiny benchmarks on a RISC-V platform with RVV support.
- [[rvme]] — Potential hardware target for accelerating GEMM kernels required by the benchmark models.
- [[xuantie_c908_fp16_gemm_kernel]] — Related workload kernel that could be evaluated under the MLPerf Tiny framework.

## Sources

- https://mlcommons.org/benchmarks/inference-tiny/
