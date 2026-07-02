---
canonical_name: Tenstorrent Wormhole Galaxy Llama 70B Benchmark
aliases: []
subtype: null
tags: []
sources:
- raw/cache/7a559880560aa975.md
- https://www.spheron.network/blog/tenstorrent-vs-nvidia-open-source-ai-hardware/
hardware_targets:
- Tenstorrent Wormhole Galaxy
- Tenstorrent Wormhole processor
workloads:
- Llama 70B inference (batch 32)
datatypes: []
metrics:
- token throughput (tokens/sec)
toolchains:
- TT-Forge
- PyTorch
- JAX
- ONNX
hardware_versions: []
software_versions: []
measurement_method: Controlled single-model benchmark runs by Tenstorrent; results
  reported but not independently verified.
evidence_strength: reported
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
type: benchmark_result
---

# Tenstorrent Wormhole Galaxy Llama 70B Benchmark

Tenstorrent's Wormhole Galaxy system, comprising 32 Wormhole processors, achieves approximately 4000-5000 tokens per second on Llama 70B inference at batch size 32. These figures originate from Tenstorrent's own controlled single-model benchmark runs, and have not been independently verified. The workload involves generating tokens from a Llama 70B language model, though details on prefill versus decode phases, input sequence lengths, and exact software versions are not disclosed. The TT-Forge compiler stack is used to compile the model from PyTorch, JAX, or ONNX onto the Wormhole hardware.

## Key Claims

- Wormhole Galaxy (32 processors): 4000-5000 tokens/sec on Llama 70B (batch 32).
- Results are vendor-reported; evidence strength is classified as reported.
- Toolchain: TT-Forge, supporting PyTorch, JAX, ONNX.

## Measurement Context

- Hardware version: Tenstorrent Wormhole Galaxy (32 Wormhole processors).
- Software/toolchain version: Not specified.
- Workload shape: Llama 70B inference, batch size 32.
- Metric: Token throughput (tokens/sec).
- Method: Controlled single-model benchmark runs by Tenstorrent, not independently verified.
- Evidence strength: reported.

## Relationships

- [[kendryte-k230-neural-network-benchmarks]]: Another RISC-V AI acceleration benchmark; provides a contrasting point for throughput on a smaller SoC.

Insufficient context for additional cross-links.

## Sources

- https://www.spheron.network/blog/tenstorrent-vs-nvidia-open-source-ai-hardware/
