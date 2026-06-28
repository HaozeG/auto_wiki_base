---
cold_start: true
created: '2025-05-09'
datatypes:
- Q4_K_XL
evidence_strength: measured
hardware_targets:
- RTX 3090 (24 GB VRAM)
- RTX 2060 (6 GB VRAM)
- AMD Ryzen 9 7950X3D
hardware_versions:
- RTX 3090 @ unspecified clock
- RTX 2060 @ unspecified clock
- AMD Ryzen 9 7950X3D @ stock
inbound_links: 1
measurement_method: Baseline and iterative optimization of llama.cpp inference parameters
  performed on a workstation. Metrics were collected from llama-server output (prompt
  processing tok/s, generation tok/s) and nvtop (GPU utilization, VRAM usage). AI
  assistant (Claude Sonnet 3.7) analyzed performance data and suggested configuration
  changes across four optimization steps.
metrics:
- tokens per second (prompt processing)
- tokens per second (generation)
- GPU utilization
- VRAM usage
scorecard:
  bridge_score: 0.4
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.95
  self_containedness: 0.85
software_versions:
- llama.cpp main branch (as of May 2025)
- Qwen3-30B-A3B-UD-Q4_K_XL.gguf
- Claude Sonnet 3.7 (frontier LLM)
sources:
- https://pauleasterbrooks.com/articles/technology/agentic-llamacpp-optimization
tags:
- llama.cpp
- LLM inference
- Qwen3
- RTX 3090
- RTX 2060
- AI-assisted optimization
- Claude Sonnet 3.7
- tensor-split
- flash attention
toolchains:
- llama.cpp (main branch)
- Claude Sonnet 3.7
type: benchmark_result
updated: '2026-06-28'
workloads:
- LLM inference (Qwen3-30B-A3B 4-bit quantized)
------

# AI-Assisted Llama.cpp Optimization Benchmark

This page documents the measured inference performance of the Qwen3-30B-A3B large language model (4-bit Q4_K_XL quantized) running on llama.cpp on a workstation with dual NVIDIA GPUs (RTX 3090 with 24 GB VRAM and RTX 2060 with 6 GB VRAM) and an AMD Ryzen 9 7950X3D CPU with 128 GB DDR5-5200 RAM. The experiment was conducted by Paul Easterbrooks and published in May 2025. It demonstrates an iterative tuning process where Claude Sonnet 3.7 analyzed initial baseline metrics and suggested parameter adjustments across four optimization steps, achieving a final generation speed of 96.68 tokens per second (a 24.7% improvement over baseline) and prompt processing speed of 252.36 tokens per second (a 96% improvement) while increasing context window size eightfold from 4096 to 32768 tokens. The final configuration used tensor-split 0.97/0.03, layer-based splitting, flash attention, batch size 1024, and two CPU threads.

## Key Claims

- Baseline prompt processing: 128.71 tokens per second; generation: 77.51 tokens per second.
- After Step 1 (threads reduced, tensor-split 0.8/0.2, batch-size 512, mlock): prompt processing 185.00 tok/s (+43.7%), generation 78.33 tok/s (+1.1%).
- After Step 2 (context increased to 32K, flash attention, tensor-split 0.75/0.25, row split): generation dropped to 47.52 tok/s due to RTX 2060 VRAM bottleneck.
- After Step 3 (tensor-split 0.9/0.1, layer split): generation recovered to 82.69 tok/s (+74% from step 2).
- After Step 4 (tensor-split 0.97/0.03): final generation 96.68 tok/s, prompt processing 252.36 tok/s.
- RTX 3090 utilized 80% GPU and 20.3 GB VRAM; RTX 2060 used 14% GPU and 1 GB VRAM in final configuration.
- Overall improvement from baseline to final: 24.7% faster generation, 96% faster prompt processing, 8x larger context window.

## Measurement Context

- Hardware version: RTX 3090 (24 GB VRAM, GA102), RTX 2060 (6 GB VRAM, TU106), AMD Ryzen 9 7950X3D (16 cores, 128 GB DDR5-5200).
- Software/toolchain version: llama.cpp main branch (compiled from source), model: unsloth/Qwen3-30B-A3B-GGUF/Qwen3-30B-A3B-UD-Q4_K_XL.gguf, AI assistant: Claude Sonnet 3.7 using web search MCP servers.
- Workload shape: LLM inference with prompt processing and autoregressive generation; default prompt not specified; context sizes 4096 and 32768 tokens.
- Metric: Prompt processing throughput (tokens per second), generation throughput (tokens per second), GPU utilization (%), VRAM usage (GB).
- Method: Baseline server command: `./build/bin/llama-server --model ... --n-gpu-layers 99 --ctx-size 4096 --threads 32`. Iterative modifications suggested by Claude based on observed metrics from llama-server output and nvtop. All measurements from a single run per configuration; averages not specified.
- Evidence strength: measured (real hardware, reported metrics from tool output).

## Relationships

- [[AI-Assisted_Llama.cpp_Optimization_Recipe]] – The detailed optimization process derived from the same experiment.
- Insufficient context for additional cross-links to existing RISC-V/edge AI pages; this benchmark is in a different domain (x86 GPU LLM inference).

## Sources

- [Paul Easterbrooks – AI-Assisted Llama.cpp Optimization](https://pauleasterbrooks.com/articles/technology/agentic-llamacpp-optimization)

