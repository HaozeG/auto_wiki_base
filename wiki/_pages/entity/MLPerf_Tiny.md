---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
scorecard:
  bridge_score: 0.4
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/mlcommons/tiny
tags:
- benchmark
- tinyML
- MLPerf
type: entity
updated: '2026-06-28'
---

# MLPerf Tiny

MLPerf Tiny is an open-source benchmark suite developed by MLCommons for evaluating the performance of machine learning inference on extremely low-power embedded systems, including microcontrollers, digital signal processors (DSPs), and tiny neural network accelerators. These devices typically operate at clock speeds between 10 MHz and 250 MHz and perform inference using less than 50 mW of power. The benchmark provides a representative set of deep neural network models and standardized benchmarking code to measure energy consumption, latency, and accuracy, enabling device makers and researchers to compare the capabilities of different TinyML hardware, models, and runtimes.

## Key Claims

- MLPerf Tiny is a benchmark suite for extremely low-power systems such as microcontrollers.
- Its goal is to provide a representative set of deep neural nets and benchmarking code to compare performance between embedded devices.
- Targeted devices include microcontrollers, DSPs, and tiny NN accelerators, operating at 10 MHz to 250 MHz and using less than 50 mW for inference.
- Metrics measured include energy, latency, and accuracy.
- Submissions allow device makers and researchers to evaluate TinyML hardware, models, and runtimes.
- The benchmark is open source and available on GitHub at https://github.com/mlcommons/tiny.

## Relationships

- [[Sipeed_MAIX_series]] – Potential hardware platform for running MLPerf Tiny benchmarks.
- Insufficient context for additional cross-links.

## Sources

- [MLPerf Tiny GitHub Repository](https://github.com/mlcommons/tiny)
