---
cold_start: false
created: '2025-06-27'
datatypes:
- FP8
evidence_strength: reported
hardware_targets:
- Wormhole n300
hardware_versions:
- 'TT-LoudBox: 2x Intel Xeon Silver 4309Y'
- 'TT-QuietBox: AMD EPYC 8124P'
inbound_links: 0
measurement_method: Company-reported performance as of April 16, 2025. Tensor Parallel
  (TP=8) for LLMs, Data Parallel (DP=8) for CNNs.
metrics:
- tokens/s/user
- fps
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions: []
sources:
- https://speakerdeck.com/tenstorrent_japan/sw-gai-yao-shuo-ming
tags:
- tenstorrent
- wormhole
- llm
- cnn
- benchmark
toolchains: []
type: benchmark_result
updated: '2026-06-28'
workloads:
- DeepSeek R1 Distill Llama 3.3 70B
- Qwen 2.5 72B
- Falcon 7B
- ResNet-50
---

# TT-LoudBox/TT-QuietBox Performance

The TT-LoudBox and TT-QuietBox are Tenstorrent workstation systems powered by four Wormhole n300 ASICs connected in a 2x4 mesh topology. Each system contains 96 GB of GDDR6 memory and 768 MB of SRAM. Performance numbers reported by Tenstorrent in April 2025 show inference throughput for large language models using Tensor Parallel (TP=8) and for computer vision models using Data Parallel (DP=8). The systems target 20 tokens/s/user for DeepSeek R1 Distill Llama 3.3 70B and 38 tokens/s/user for Qwen 2.5 72B, with achieved values at 15.2 and 32.5 tokens/s/user respectively. ResNet-50 inference reaches 35,800 fps (target 56,000 fps). All measurements are from a company presentation and have not been independently verified.

## Key Claims

- DeepSeek R1 Distill Llama 3.3 70B (TP=8): 15.2 tokens/s/user achieved (target 20 tokens/s/user), batch size 32.
- Qwen 2.5 72B (TP=8): 32.5 tokens/s/user achieved (target 38 tokens/s/user), batch size 32.
- Falcon 7B (DP=8): 15.5 tokens/s/user achieved (target 26 tokens/s/user), batch size 256.
- ResNet-50 224x224 (DP=8): 35,800 fps achieved (target 56,000 fps).

## Measurement Context

- Hardware version: TT-LoudBox (2x Intel Xeon Silver 4309Y, 512 GB DDR5-4800) / TT-QuietBox (AMD EPYC 8124P, 512 GB DDR5-4800) with 4x Wormhole n300 ASICs, 96 GB GDDR6, 768 MB SRAM, connected in 2x4 mesh.
- Software/toolchain version: Not specified; Tenstorrent SDK and TT-NN library implied.
- Workload shape: DeepSeek R1 Distill Llama 3.3 70B (tensor parallel), Qwen 2.5 72B (tensor parallel), Falcon 7B (data parallel), ResNet-50 (data parallel).
- Metric: tokens per second per user (t/s/u) for LLMs; frames per second (fps) for CNNs.
- Method: Company-reported internal benchmarks as of April 16, 2025. Tensor Parallel (TP=8) splits model across 8 ASICs; Data Parallel (DP=8) replicates model across 8 ASICs with batch processing.
- Evidence strength: reported (company presentation, no independent verification).

## Relationships

- [[tenstorrent]] - The parent entity page for Tenstorrent hardware.
- [[risc_v_vector_extension]] - The Wormhole ASICs use RISC-V based Tensix cores.

## Sources

- Tenstorrent HW/SW Overview presentation, Tenstorrent Japan, June 2025. https://speakerdeck.com/tenstorrent_japan/sw-gai-yao-shuo-ming
