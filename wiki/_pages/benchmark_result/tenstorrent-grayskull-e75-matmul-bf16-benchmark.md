---
canonical_name: Tenstorrent Grayskull e75 MatMul BF16 Peak Efficiency
aliases:
- Grayskull MatMul BF16 1.55 TFLOPs/Watt
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e75
workloads:
- MatMul
datatypes:
- BF16
metrics:
- TFLOPs per Watt
toolchains: []
hardware_versions: []
software_versions: []
measurement_method: Detailed characterization of execution model, grid size, matrix
  dimensions, data formats, and numerical precision impact on computational efficiency,
  as described in the conference paper.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/0f397fff796e4aa1.md
- https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10
source_url: https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10
fetched_at: '2026-07-02T10:04:18.333789+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Tenstorrent Grayskull e75 MatMul BF16 Peak Efficiency

The Tenstorrent Grayskull e75 RISC-V accelerator achieves a peak efficiency of 1.55 TFLOPs per Watt on matrix multiplication (MatMul) workloads at BF16 numerical precision, as reported in a 2025 conference paper by Pizzini Cavagna et al. presented at ISC High Performance 2025. This result was obtained through a detailed characterization of the accelerator's execution model, including grid size, matrix dimensions, data format, and numerical precision settings. The measurement context includes comparisons against Intel Sapphire Rapids processors and NVIDIA V100 and A100 GPUs, with the Grayskull e75 demonstrating a competitive power-performance trade-off despite lower absolute raw throughput than NVIDIA GPUs. The benchmark is representative of fundamental operations in large language model (LLM) computations, where reduced numerical precision (BF16) is commonly employed.

## Key Claims

- Peak matrix multiplication efficiency: 1.55 TFLOPs/Watt with BF16 precision on Tenstorrent Grayskull e75.
- Efficiency measured via detailed characterization of execution parameters (grid size, matrix dimensions, data formats, precision).
- Comparison against Intel Sapphire Rapids and NVIDIA V100/A100 shows Grayskull e75 offers competitive power efficiency.

## Measurement Context

- Hardware version: Tenstorrent Grayskull e75 (no specific hardware revision provided)
- Software/toolchain version: Not specified; paper references GitHub repository for software
- Workload shape: Matrix multiplication (MatMul); shapes not specified beyond grid and dimension parameters
- Metric: TFLOPs per Watt
- Method: Detailed characterization of execution model, grid size, matrix dimensions, data formats, and numerical precision impact
- Evidence strength: reported (conference paper)

## Relationships

- [[tenstorrent-grayskull-e75]]: Hardware target page for the Grayskull e75 accelerator.
- [[cpa-factored-gemmini-systolic-array]]: Related optimization recipe for systolic array acceleration; both pages address ML acceleration in the RISC-V ecosystem.

## Sources

- [Assessing Tenstorrent’s RISC-V MatMul Acceleration Capabilities](https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10)
