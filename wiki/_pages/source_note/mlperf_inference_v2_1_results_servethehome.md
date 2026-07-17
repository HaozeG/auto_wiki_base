---
canonical_name: MLPerf Inference v2.1 Results (ServeTheHome)
aliases:
- MLPerf Inference v2.1 ServeTheHome
- STH MLPerf Inference v2.1
subtype: null
tags:
- mlperf
- inference
- benchmark
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.6
sources:
- raw/cache/e6ae6ea33d1bf6bc.md
- https://www.servethehome.com/mlperf-inference-v2-1-results-ai-nvidia-inspur-moffett-biren-qualcomm-intel-sk-hynix/
source_url: https://www.servethehome.com/mlperf-inference-v2-1-results-ai-nvidia-inspur-moffett-biren-qualcomm-intel-sk-hynix/
fetched_at: '2026-07-17T11:58:19.568673+00:00'
type: source_note
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# MLPerf Inference v2.1 Results (ServeTheHome)

MLPerf Inference v2.1 is the July 2022 benchmark round published by MLCommons, covering AI inference performance of both closed- and open-category systems across datacenter and edge workloads. The ServeTheHome article summarizes notable submissions including NVIDIA H100 on dual-socket Xeon Silver 4314 and EPYC 7252 platforms, Intel Sapphire Rapids with integrated inference acceleration outperforming the NVIDIA A2 in some tests, the Biren BR104-300W PCIe card (half the BR100 GPU) delivering performance between the A100 and H100, and the Moffett S4/S10/S30 accelerators leveraging sparsity. Additional entries included Qualcomm Cloud AI 100, SK Hynix Sapeon X220, and Alibaba Yitian 710 Arm CPUs. NVIDIA's Jetson AGX Orin edge module demonstrated a 50% performance-per-watt improvement over earlier results.

## Key Claims

- The Biren BR100 (via the BR104-300W PCIe variant in an Inspur NF5468M6) showed inference performance in ResNet and BERT 99.9 benchmarks that falls between the NVIDIA A100 and H100, a strong showing for a first-generation GPU-class accelerator.
- Intel Sapphire Rapids 2-socket systems with PyTorch achieved inference performance comparable to an NVIDIA A2 or higher, suggesting that future CPUs with built-in acceleration could reduce the need for low-power PCIe inference add-in cards.
- Moffett's S4, S10, and S30 accelerators exploit sparsity and were submitted in the open datacenter category, giving them flexibility in mathematical precision.
- NVIDIA Jetson AGX Orin saw a 50% improvement in performance per watt between the first MLPerf submission and v2.1, attributed to software maturation.
- SK Hynix Sapeon X220, an older-generation accelerator, was tested in Supermicro servers, marking its first MLPerf appearance.

## Relationships

- The [[amd_instinct_mi100]] page describes an HPC accelerator from AMD that targets similar AI training and inference workloads; both are contemporary (2020-2022) accelerators used in datacenter AI inference, though the MI100 was not submitted to MLPerf Inference v2.1.
- No additional specific relationships to the visible context pages can be stated; this source note primarily collects first-benchmark results for several new chips that currently lack individual pages.

## Sources

- [MLPerf Inference v2.1 Results with Lots of New AI Hardware](raw/cache/e6ae6ea33d1bf6bc.md)
