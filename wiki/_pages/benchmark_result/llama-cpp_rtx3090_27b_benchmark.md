---
cold_start: false
created: '2026-06-28'
datatypes:
- Q4_K_M
evidence_strength: measured
hardware_targets:
- NVIDIA RTX 3090
hardware_versions:
- RTX 3090
inbound_links: 1
measurement_method: Measured by the author on an RTX 3090 with a 27B model. Load time,
  token generation speed, and prompt processing speed recorded before and after optimizations.
metrics:
- load time
- token generation speed
- prompt processing speed
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- llama.cpp (compiled from source with CUDA and Flash Attention)
sources:
- https://docs.bswen.com/blog/2026-03-15-llamacpp-optimization-speed/
tags:
- llama.cpp
- RTX 3090
- 27B model
- GGUF
- benchmark
toolchains:
- llama.cpp
- CUDA
- cmake
type: benchmark_result
updated: '2026-06-28'
workloads:
- LLM inference (27B parameter model)
---

# llama.cpp RTX 3090 27B Model Benchmark

This benchmark result documents the inference performance of a 27-billion parameter language model running on an NVIDIA RTX 3090 GPU using llama.cpp. Before optimization, the model loaded in 45 seconds, generated tokens at 3 tokens per second, and processed prompts at 8 tokens per second. After applying GPU offloading (all layers, via `-ngl 99`), compiling with CUDA and Flash Attention, using Q4_K_M quantization, enabling KV cache quantization (`--cache-type-k q4_0`), and setting batch sizes to 512, the load time dropped to 12 seconds, generation speed increased to over 42 tokens per second (a 14x improvement), and prompt processing reached over 150 tokens per second. These results were measured by the blog author and demonstrate the dramatic impact of compile-time and runtime optimizations for llama.cpp on consumer NVIDIA hardware. The source provides the full set of flags and build steps used.

## Key Claims

- Load time improved from 45 s to 12 s after optimizations.
- Token generation speed increased from 3 tok/s to over 42 tok/s (14x).
- Prompt processing speed increased from 8 tok/s to over 150 tok/s (over 18x).
- Key optimizations: GPU offloading with `-ngl 99`, CUDA compilation, Flash Attention, Q4_K_M quantization, KV cache quantization, and batch size tuning.
- Tested on an RTX 3090 with a 27B parameter model.

## Measurement Context

- Hardware version: NVIDIA RTX 3090 (24 GB VRAM).
- Software/toolchain version: llama.cpp compiled from source with `-DGGML_CUDA=ON -DGGML_FLASH_ATTN=ON`.
- Workload shape: 27B parameter model, quantized to Q4_K_M, context length 8192, generation prompt unspecified.
- Metric: Load time (s), token generation speed (tok/s), prompt processing speed (tok/s).
- Method: Manual timing by the author; single run reported.
- Evidence strength: measured.

## Relationships

- [[MilkV_Pioneer]] – Another hardware target running llama.cpp, but on a RISC-V CPU without GPU, offering a contrasting inference scenario.
- [[llama-cpp-mini_benchmark_apple_m4]] – A benchmark for a lightweight LLaMA inference engine on Apple M4 hardware, related as another LLM inference benchmark.
- [[Llama.cpp_Optimization_Recipe]] – The optimization recipe derived from the same source, providing step-by-step instructions and general advice.

## Sources

- [How to Optimize llama.cpp for Maximum Inference Speed: A Complete Guide](https://docs.bswen.com/blog/2026-03-15-llamacpp-optimization-speed/)

