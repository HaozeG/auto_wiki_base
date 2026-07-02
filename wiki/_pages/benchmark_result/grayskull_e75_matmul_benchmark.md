---
canonical_name: Tenstorrent Grayskull e75 MatMul Benchmark (arXiv:2505.06085)
aliases:
- Grayskull e75 MatMul efficiency
- Grayskull BF16 benchmark
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e75
- Intel Sapphire Rapids
- NVIDIA V100
- NVIDIA A100
workloads:
- MatMul
datatypes:
- BF16
- FP16
metrics:
- TFLOPs/Watt
- TFLOPs
toolchains: []
hardware_versions:
- Grayskull e75 (12nm, 1 GHz, 96 cores, 8 GB LPDDR4)
- Intel Sapphire Rapids (model unspecified)
- NVIDIA V100
- NVIDIA A100
software_versions: []
measurement_method: Academic benchmark paper. MatMul performance measured across different
  grid sizes, matrix dimensions, and data formats on Grayskull e75 using custom kernel
  implementations. Power consumption measured at system level. Comparison data for
  Intel Sapphire Rapids and NVIDIA GPUs sourced from literature or vendor specifications.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/2bb619b763be17f7.md
- https://arxiv.org/html/2505.06085v1
source_url: https://arxiv.org/html/2505.06085v1
fetched_at: '2026-07-02T05:05:34.906383+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Tenstorrent Grayskull e75 MatMul Benchmark (arXiv:2505.06085)

The Tenstorrent Grayskull e75 was characterized for matrix multiplication (MatMul) performance and energy efficiency in a study published at arXiv:2505.06085v1 by researchers from University of Bologna and Cineca. The paper reports a peak computational efficiency of 1.55 TFLOPs/Watt when using BF16 data format, highlighting the accelerator's competitive energy efficiency against Intel Sapphire Rapids processors and NVIDIA V100 and A100 GPUs. The study also analyzes the execution time breakdown: on the first run, matrix tiling accounts for 31% of the time and kernel compilation for 66%, while subsequent runs are dominated by data transfer (62%). The Grayskull e75, with 96 Tensix cores at 1 GHz, achieves a peak raw throughput of 55 TFLOPs for FP16.

## Key Claims

- Peak MatMul efficiency on Grayskull e75: 1.55 TFLOPs/Watt with BF16.
- Peak FP16 throughput: 55 TFLOPs.
- First-run execution: 31% tiling, 66% kernel compilation.
- Subsequent runs: 62% data transfer.
- Grayskull e75 offers competitive energy efficiency vs NVIDIA V100/A100 and Intel Sapphire Rapids.

## Measurement Context

- Hardware version: Tenstorrent Grayskull e75 (12nm, 1 GHz, 96 cores, 8 GB LPDDR4)
- Software/toolchain version: Not specified; custom kernels
- Workload shape: MatMul with varying grid sizes and matrix dimensions
- Metric: TFLOPs/Watt (energy efficiency), TFLOPs (throughput)
- Method: Academic benchmark; power measured at system level; kernel execution timed separately.
- Evidence strength: reported

## Relationships

- [[tenstorrent_grayskull_e75]]: The hardware target under test.
- [[k230]]: Another RISC-V AI accelerator with benchmark data (if any exists in wiki; but we only have the hardware_target page for k230, not a benchmark). We can still link as a comparable hardware target.

## Sources

- https://arxiv.org/html/2505.06085v1
