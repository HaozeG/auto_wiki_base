---
canonical_name: HTVM
aliases:
- HTVM compiler
- Hybrid TVM
subtype: null
tags:
- compiler
- TinyML
- heterogeneous
- TVM
- DORY
- DIANA
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/f42e80928cf6b057.md
- https://arxiv.org/html/2406.07453
source_url: https://arxiv.org/html/2406.07453
fetched_at: '2026-07-06T02:44:00.911548+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# HTVM

HTVM is a hybrid compiler toolchain for efficient deployment of deep neural networks (DNNs) on heterogeneous TinyML platforms. It merges the TVM compiler framework with the DORY memory planning backend to maximize utilization of multiple accelerator cores and minimize data movements. HTVM targets systems-on-chips (SoCs) that contain a microcontroller CPU, digital and analog compute-in-memory AI accelerators, and limited programmer-managed memory. The toolchain operates completely ahead-of-time, generating code that dispatches kernels across heterogeneous cores with hardware-aware layer tiling. HTVM achieves up to 120x improved performance over plain TVM when deploying the MLPerf Tiny suite on the DIANA SoC, a platform with a RISC-V host, a 500k MAC/cycle analog-in-memory-compute accelerator, and a digital DNN accelerator with a two-level memory system.

## Key Claims

- HTVM extends TVM with the DORY memory-planning backend for automatic code generation and data movement optimization.
- HTVM enables tiled execution of DNN layers on memory-constrained heterogeneous accelerators.
- On the DIANA SoC, HTVM achieves up to 6.2× speedup using hardware-aware tiling over hardware-agnostic tiling.
- HTVM achieves performance within 15.52% (digital accelerator) and 5.19% (analog accelerator) of theoretical peak for convolutional layers.
- End-to-end MLPerf Tiny networks deployed with HTVM reduce binary size by up to 12.3% compared to plain TVM at equal bit precision.
- HTVM combined multi-accelerator usage reduces total latency by up to 8× over single-accelerator solutions.
- HTVM achieves 120x improved performance over plain TVM deployment on DIANA.

## Relationships

No specific relationships to visible context pages.

## Sources

- https://arxiv.org/html/2406.07453
