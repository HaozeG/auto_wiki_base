---
cold_start: false
created: '2025-05-09'
datatypes:
- BF16
evidence_strength: measured
hardware_targets:
- Tenstorrent Grayskull e75
hardware_versions:
- Grayskull e75 (96 Tensix cores, 1 GHz, 12 nm GF)
inbound_links: 10
measurement_method: Independent assessment analyzing Tenstorrent's MatMul acceleration
  capabilities; specific methodology not detailed in available snippets.
metrics:
- throughput
- power
- efficiency
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://news.ycombinator.com/item?id=39658787
- Assessing Tenstorrent's RISC-V MatMul Acceleration Capabilities (May 9, 2025)
tags:
- RISC-V
- Tenstorrent
- Grayskull
- MatMul
- efficiency
toolchains:
- TT-Metalium
type: benchmark_result
updated: '2026-06-29'
workloads:
- Matrix multiplication (MatMul)
---

# Tenstorrent Grayskull MatMul Efficiency

Benchmark results for Tenstorrent Grayskull's matrix multiplication (MatMul) efficiency are reported in an independent assessment published May 9, 2025. The Grayskull e75 DevKit, with 96 Tensix cores, 1 GHz clock, and 75 W TDP, achieves a peak of 1.55 TFLOPs per Watt using BF16 datatype. This efficiency metric positions Grayskull competitively against NVIDIA GPUs in terms of computational throughput per watt, though NVIDIA GPUs still dominate raw throughput. The measurement likely involves dense matrix multiplication workloads typical of deep learning inference, using the TT-Metalium software stack. This benchmark fills a gap in understanding the real-world efficiency of RISC-V-based AI accelerators for compute-heavy tensor operations.

## Key Claims

- Peak efficiency of 1.55 TFLOPs/Watt with BF16 on Grayskull e75.
- Competitive power efficiency relative to NVIDIA GPUs (which have higher absolute throughput but lower TFLOPs/Watt).
- Grayskull demonstrates a trade-off between power consumption and computational throughput.

## Measurement Context

- **Hardware version:** Tenstorrent Grayskull e75 (96 Tensix cores, 1 GHz clock, 12 nm GF process, 75 W TDP, 96 MB SRAM, 8 GB LPDDR4).
- **Software/toolchain version:** Not specified; likely TT-Metalium or custom benchmarking harness.
- **Workload shape:** Matrix multiplication (dense MatMul). Specific dimensions (M, N, K) not available.
- **Metric:** TFLOPs/Watt (efficiency derived from throughput and power).
- **Method:** Independent assessment; methodology details not provided in available snippets. Evidence strength is classified as measured based on the source's analytical nature.
- **Evidence strength:** measured (independent analysis of benchmark results).

## Relationships

- [[Tenstorrent_Grayskull]] – The hardware target on which this benchmark is measured.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another RISC-V AI accelerator benchmark providing a comparison point for efficiency.

## Sources

- [Assessing Tenstorrent's RISC-V MatMul Acceleration Capabilities (May 9, 2025)](https://example.com/arxiv/abstract) (URL not provided in resource; source identified by snippet)
- [TechRadar: Tenstorrent unveils Grayskull](https://www.techradar.com/) (background hardware specs)
