---
canonical_name: Tenstorrent
aliases: []
subtype: null
tags: []
sources:
- raw/cache/7a559880560aa975.md
- https://www.spheron.network/blog/tenstorrent-vs-nvidia-open-source-ai-hardware/
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.5
  bridge_score: 0.2
  hub_potential: 0.4
source_url: https://www.spheron.network/blog/tenstorrent-vs-nvidia-open-source-ai-hardware/
fetched_at: '2026-07-02T10:07:30.477282+00:00'
type: entity
---

# Tenstorrent

Tenstorrent is a company developing artificial intelligence accelerators that utilize RISC-V cores and a fully open instruction set architecture. Its product lineup includes the Wormhole and Blackhole chip families, designed for AI inference and training workloads. Tenstorrent provides the TT-Forge compiler, an MLIR-based open-source software stack that supports compiling models from PyTorch, JAX, and ONNX for execution on its hardware. The company positions its offerings as an open-source alternative to proprietary solutions like NVIDIA's CUDA ecosystem. The Wormhole Galaxy system, combining 32 Wormhole processors, has been benchmarked at 4000-5000 tokens per second on Llama 70B inference at batch 32, according to vendor-reported results.

## Key Claims

- Tenstorrent's Wormhole and Blackhole chips use RISC-V cores with a fully open ISA.
- TT-Forge is an MLIR-based open-source compiler supporting PyTorch, JAX, ONNX.
- The Wormhole Galaxy (32 Wormhole processors) achieves 4000-5000 tokens/sec on Llama 70B at batch 32 (vendor-reported).

## Relationships

- [[kendryte-k230-neural-network-benchmarks]]: Another RISC-V AI accelerator benchmark page; Tenstorrent serves as a comparison point for open-source vs. proprietary AI hardware strategies.

Insufficient context for additional cross-links.

## Sources

- https://www.spheron.network/blog/tenstorrent-vs-nvidia-open-source-ai-hardware/
