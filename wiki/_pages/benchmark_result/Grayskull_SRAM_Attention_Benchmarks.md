---
cold_start: true
created: '2025-04-09'
datatypes:
- Bfloat16
evidence_strength: reported
hardware_targets:
- Tenstorrent Grayskull e150
hardware_versions:
- Tenstorrent Grayskull e150
- Nvidia H100 PCIe (for cost/SRAM comparison)
inbound_links: 0
measurement_method: 'Dedicated Softmax kernel benchmark: compared against a CPU baseline
  implementation (unspecified CPU). Fused kernel benchmark: compared against the dedicated
  Softmax kernel on the same Grayskull e150 hardware.'
metrics:
- speedup
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/abs/2407.13885
tags:
- Tenstorrent
- Grayskull
- attention
- Softmax
- SRAM
- speedup
toolchains:
- TT-Metalium
- TT-Buda
type: benchmark_result
updated: '2026-06-29'
workloads:
- Self-attention Softmax
---

# Grayskull SRAM Attention Benchmarks

Benchmark results for the SRAM-based self-attention implementation on the Tenstorrent Grayskull e150 are reported in the paper "Attention in SRAM on Tenstorrent Grayskull" (arXiv:2407.13885). The dedicated Softmax kernel, which runs entirely in the 120 MB distributed SRAM, achieves a speedup of up to 10× compared to a CPU baseline implementation. The fused kernel that combines matrix multiplication (QK^T), attention score scaling, and Softmax operations in a single SRAM-resident kernel achieves an additional 1.8× speedup over the dedicated Softmax kernel alone. The measurements were performed on the Grayskull e150 card using Bfloat16 data format with 32×32 tile processing. The paper also provides a cost comparison: the Grayskull e150 is approximately 30× cheaper for the general public than an Nvidia H100 PCIe and offers 1.5× more SRAM (120 MB vs. 80 MB). The benchmarks demonstrate that SRAM-only attention execution can yield significant speedups on this dataflow architecture, though the time and memory complexity remain quadratic in sequence length.

## Key Claims

- Dedicated Softmax kernel on Grayskull e150: up to 10× speedup over CPU implementation.
- Fused kernel (matmul + scaling + Softmax) on Grayskull e150: approximately 1.8× faster than the dedicated Softmax kernel.
- Grayskull e150 SRAM: 120 MB vs. 80 MB on Nvidia H100 PCIe.
- Cost: Grayskull e150 is approximately 30× cheaper than Nvidia H100 PCIe.

## Measurement Context

- Hardware version: Tenstorrent Grayskull e150 (120 Tensix cores, 1.2 GHz, 200 W, 120 MB SRAM, 8 GB LPDDR4).
- Software/toolchain version: Not specified; likely TT-Metalium or TT-Buda.
- Workload shape: Self-attention Softmax; sequence length not specified but time complexity quadratic in length.
- Metric: Speedup factor (dedicated Softmax vs. CPU; fused kernel vs. dedicated kernel).
- Method: Benchmarks are reported from the paper. The CPU baseline is described as a "CPU implementation serving as a baseline" without further specification. The fused kernel's performance is measured relative to the dedicated Softmax kernel on the same hardware.
- Evidence strength: reported (claims from an academic paper, not independently verified).

## Relationships

- [[Tenstorrent_Grayskull_e150]] – The hardware target that enables these benchmarks.
- [[Grayskull_SRAM_Fused_Attention_Kernel]] – The optimization recipe that these benchmarks evaluate.

## Sources

- arXiv:2407.13885 – Attention in SRAM on Tenstorrent Grayskull
