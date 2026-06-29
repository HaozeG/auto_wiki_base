---
cold_start: false
constraints:
- asymmetric GPU VRAM (24 GB vs 6 GB)
- context size target 32K tokens
- Qwen3-30B-A3B model size ~16 GB in Q4_K_XL
created: '2025-05-09'
datatypes:
- Q4_K_XL
evidence_strength: measured
hardware_targets:
- RTX 3090 (24 GB VRAM)
- RTX 2060 (6 GB VRAM)
- AMD Ryzen 9 7950X3D
inbound_links: 0
metrics:
- tokens per second (prompt processing)
- tokens per second (generation)
- GPU utilization
- VRAM usage
needs_summary_revision: true
scorecard:
  bridge_score: 0.4
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.95
  self_containedness: 0.85
sources:
- https://pauleasterbrooks.com/articles/technology/agentic-llamacpp-optimization
tags:
- llama.cpp
- LLM inference optimization
- AI-assisted tuning
- Claude Sonnet 3.7
- tensor-split
- flash attention
- continuous batching
- asymmetric GPU
- Qwen3
toolchains:
- llama.cpp
- Claude Sonnet 3.7
type: optimization_recipe
updated: '2026-06-28'
workloads:
- LLM inference (Qwen3-30B-A3B, Q4_K_XL)
---

# AI-Assisted Llama.cpp Optimization Recipe

This optimization recipe describes an iterative tuning process for llama.cpp inference on a dual-GPU workstation with asymmetric VRAM (RTX 3090 24 GB + RTX 2060 6 GB). Claude Sonnet 3.7, a frontier AI assistant, analyzed performance metrics from llama-server and nvtop, then suggested parameter adjustments across four optimization steps. The final configuration achieved a 24.7% generation speed improvement and 96% prompt processing improvement while enabling an 8x larger context window. Key optimizations included reducing CPU threads to 2, setting tensor-split to 0.97/0.03 to match GPU capabilities, enabling flash attention for large context windows, and using layer-based splitting. The recipe is grounded in measured results on real hardware and demonstrates the value of AI-assisted tuning for LLM inference.

## Key Claims

- Reducing threads from 32 to 2 (counter-intuitive for GPU-accelerated inference) improved prompt processing by 43.7%.
- Tensor-split ratio 0.97/0.03 optimally distributed model layers across asymmetric GPUs.
- Flash attention was essential for efficient 32K token context; row splitting caused a VRAM bottleneck on the smaller GPU.
- Switching from row-based to layer-based splitting resolved the bottleneck and restored performance.
- Continuous batching and memory locking (mlock) contributed to throughput improvements.
- AI assistant identified VRAM bottleneck and corrected tensor-split ratio autonomously.

## Transformation

- Prerequisites: Workstation with asymmetric NVIDIA GPUs, llama.cpp compiled from source (main branch), a 4-bit quantized LLM (tested with Qwen3-30B-A3B Q4_K_XL), and an AI assistant capable of analyzing performance metrics and suggesting parameters (Claude Sonnet 3.7 with web search MCP servers for live documentation).
- Steps:
  1. Establish baseline: run llama-server with default Unsloth recommendations (--n-gpu-layers 99, --ctx-size 4096, --threads 32). Capture metrics from llama-server output (prompt processing tok/s, generation tok/s) and nvtop (GPU utilization, VRAM).
  2. Optimization Step 1: Reduce threads to 2, add tensor-split (0.8/0.2) proportional to GPU VRAM, set batch-size 512, ubatch-size 512, enable continuous batching and mlock, use layer-based splitting. This improves prompt processing 43.7%.
  3. Optimization Step 2: Increase context size to 32768, enable flash attention, adjust tensor-split to 0.75/0.25, switch to row-based splitting. Generation speed drops due to VRAM pressure on RTX 2060.
  4. Optimization Step 3: Revert to layer-based splitting, adjust tensor-split to 0.9/0.1 to relieve VRAM pressure on the smaller GPU. Generation recovers to 82.69 tok/s (+74% from step 2).
  5. Optimization Step 4: Fine-tune tensor-split to 0.97/0.03 to maximize RTX 3090 contribution while keeping RTX 2060 lightly loaded. Final generation 96.68 tok/s.
- Expected effect: Up to 24.7% generation speedup and 96% prompt processing speedup over baseline, with ability to use 8x larger context windows.
- Failure modes: If tensor-split assigns too many layers to the smaller GPU, VRAM bottleneck degrades performance (observed in step 2). Row-based splitting with asymmetric GPUs can cause load imbalance. Hallucinated llama-server arguments can be resolved by using live documentation (MCP servers).
- Measurements: Baseline: prompt 128.71 tok/s, generation 77.51 tok/s. Final: prompt 252.36 tok/s, generation 96.68 tok/s. All measurements from single runs on the described hardware (see benchmark page for details).

## Relationships

- [[AI-Assisted_Llama.cpp_Optimization_Benchmark]] – The benchmark results page that grounds the claims with specific numeric data.
- Insufficient context for additional cross-links; existing wiki pages are focused on RISC-V / edge AI and not directly related to this NVIDIA GPU LLM inference domain.

## Sources

- [Paul Easterbrooks – AI-Assisted Llama.cpp Optimization](https://pauleasterbrooks.com/articles/technology/agentic-llamacpp-optimization)

