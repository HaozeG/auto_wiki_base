---
canonical_name: GAP9 vs STM32F7 On-Device Training Benchmark
aliases:
- GAP9 ODTL performance
- GAP9 vs STM32F756ZG benchmark
subtype: null
tags: []
hardware_targets:
- GAP9
- STM32F756ZG
workloads:
- Human Activity Recognition (HAR) - body capacitance-based gym activity recognition
- Human Activity Recognition (HAR) - QVAR-based hand gesture recognition
- Human Activity Recognition (HAR) - ultrasonic-based hand gesture recognition
datatypes: []
metrics:
- latency
- power consumption
- accuracy
toolchains: []
hardware_versions: []
software_versions: []
measurement_method: Experimental deployment of on-device transfer learning (ODTL)
  on two MCU platforms; latency and power measured during training task
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/1259d3b22900ba3e.md
- https://arxiv.org/html/2407.03644v1
source_url: https://arxiv.org/html/2407.03644v1
fetched_at: '2026-07-02T11:01:08.816668+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
---

# GAP9 vs STM32F7 On-Device Training Benchmark

This benchmark compares the performance of two MCU-level edge computing platforms — the GreenWaves GAP9 (a RISC-V based ultra-low-power parallel processor) and the STM32F756ZG (ARM Cortex-M7) — when executing an on-device transfer learning (ODTL) scheme for human activity recognition (HAR). The workload consists of three HAR scenarios: body capacitance-based gym activity recognition, QVAR-based hand gesture recognition, and ultrasonic-based hand gesture recognition. Measured metrics include latency during training (absolute and relative), power consumption during training, and the accuracy improvement over a baseline model without transfer learning. The measurements are reported in the research paper "On-Device Training Empowered Transfer Learning For Human Activity Recognition" (arXiv:2407.03644).

## Key Claims

- GAP9 achieves 20× lower latency than STM32F756ZG during ODTL deployment.
- GAP9 achieves 280× lower power consumption than STM32F756ZG during ODTL deployment.
- ODTL improves recognition accuracy by 3.73% for body capacitance-based gym activity recognition.
- ODTL improves recognition accuracy by 17.38% for QVAR- and ultrasonic-based hand gesture recognition.
- ODTL improves recognition accuracy by 3.70% for a combined hand gesture recognition scenario.

## Measurement Context

- Hardware version: GreenWaves GAP9 (RISC-V based, low-power parallel computing device), STM32F756ZG (ARM Cortex-M7)
- Software/toolchain version: Not specified; assumed vendor toolchains for GAP9 (GAP SDK) and STM32 (STM32CubeIDE)
- Workload shape: Three distinct HAR scenarios using body capacitance, QVAR, and ultrasonic sensing; specific sensor data not detailed
- Metric: Latency (absolute and ratio), power consumption (absolute and ratio), recognition accuracy (percentage improvement)
- Method: The ODTL scheme was deployed on both platforms; latency and power were measured during the training task. Accuracy improvements were computed relative to a baseline without transfer learning.
- Evidence strength: reported

## Relationships

- [[earth-shifting-based-vector-memory-access]]: This optimization recipe targets RISC-V vector memory access, which may be applicable to the GAP9's vector processing unit; the benchmark highlights GAP9's efficiency for edge ML tasks.
- Insufficient context for additional cross-links; no existing entity pages for GAP9 or STM32F7 are present in the wiki.

## Sources

- [On-Device Training Empowered Transfer Learning For Human Activity Recognition](https://arxiv.org/html/2407.03644v1)
