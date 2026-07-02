---
canonical_name: PULP-NN GAP-8 CIFAR-10 Benchmark
aliases:
- GAP-8 PULP-NN benchmark
- PULP-NN vs CMSIS-NN CIFAR-10
subtype: null
tags: []
hardware_targets:
- GAP-8
- STM32L4
- STM32H7
workloads:
- CIFAR-10 inference
datatypes:
- INT-8
metrics:
- MACs/cycle
- clock cycle reduction
- energy efficiency
toolchains:
- PULP-NN
- CMSIS-NN
hardware_versions:
- GAP-8
- STM32L4
- STM32H7
software_versions:
- PULP-NN
- CMSIS-NN
measurement_method: Execution clock cycle comparison between PULP-NN on GAP-8 and
  CMSIS-NN on STM32L4/STM32H7 at maximum frequency and at maximum efficiency point.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/4b0071cc05f9850c.md
- https://arxiv.org/abs/1908.11263
source_url: https://arxiv.org/abs/1908.11263
fetched_at: '2026-07-02T04:53:43.278716+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# PULP-NN GAP-8 CIFAR-10 Benchmark

This benchmark measures the performance of PULP-NN, an optimized quantized neural network inference library, on the GAP-8 processor running a CIFAR-10 network. Measurements compare execution clock cycles against the ARM CMSIS-NN library on STM32L4 and STM32H7 microcontrollers. At maximum frequency, PULP-NN on GAP-8 achieves 36.8x fewer clock cycles than STM32L4 and 7.45x fewer than STM32H7. At the maximum efficiency point, PULP-NN on GAP-8 achieves 14.1x higher energy efficiency than STM32L4 and 39.5x higher than STM32H7. The library also achieves up to 15.5 MACs/cycle on INT-8 and improves performance by up to 63x relative to a sequential single-core RISC-V baseline implementing the RV32IMC ISA. These results demonstrate the effectiveness of PULP-NN's DSP-extensions-aware kernels and cluster parallelism exploitation.

## Key Claims

- At maximum frequency, PULP-NN on GAP-8 outperforms CMSIS-NN on STM32L4 by 36.8x and on STM32H7 by 7.45x in terms of clock cycles.
- At the maximum efficiency point, PULP-NN on GAP-8 provides 14.1x energy efficiency improvement over STM32L4 and 39.5x over STM32H7.
- PULP-NN achieves up to 15.5 MACs/cycle on INT-8.
- Performance improves up to 63x over a sequential single-core RV32IMC baseline.

## Measurement Context

- Hardware version: GAP-8 (PULP-based processor); comparison targets STM32L4 and STM32H7.
- Software/toolchain version: PULP-NN library; CMSIS-NN library for ARM targets.
- Workload shape: CIFAR-10 network (full inference pass).
- Metric: Clock cycle count for inference; energy efficiency (relative).
- Method: Measured execution cycles on real hardware; comparison reported as ratios.
- Evidence strength: measured

## Relationships

- [[pulp_nn]]: The library that produced these benchmark results.
- [[k230]]: A RISC-V AI SoC that could serve as an alternative target for similar quantized neural network benchmarks.
- [[xuantie_c908]]: Another RISC-V core with vector extensions, relevant for comparison of RISC-V AI inference performance.

## Sources

- https://arxiv.org/abs/1908.11263
