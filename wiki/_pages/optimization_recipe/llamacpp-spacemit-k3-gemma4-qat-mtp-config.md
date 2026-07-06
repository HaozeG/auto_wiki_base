---
canonical_name: SpaceMIT K3 Gemma 4 QAT MTP Configuration
aliases:
- llama.cpp Gemma 4 QAT MTP on SpaceMIT K3
- Milk-V Jupiter 2 Gemma 4 server config
- Spacemit K3 llama.cpp tuning
subtype: null
tags: []
hardware_targets:
- SpacemiT K3
workloads:
- LLM inference (Gemma 4 E2B QAT)
- LLM inference (Gemma 4 26B A4B QAT)
datatypes:
- Q4_K_XL (model)
- Q4_0 (draft model)
- f16 KV cache
- q8_0 KV cache
metrics:
- generation throughput (tok/s)
- prefill throughput (tok/s)
- MTP acceptance rate
- memory usage (MiB)
toolchains:
- llama.cpp (SpaceMIT K3 fork with -DGGML_CPU_RISCV64_SPACEMIT=ON -DGGML_RV_ZBA=ON
  -DGGML_RV_ZFH=ON -DGGML_RV_ZVFH=ON)
- llama-server
constraints:
- 8 performance cores (A100/IME2)
- TCM block size: 393216
- f16 KV cache
- thread count 8 (not more)
- context size limited to 32K (E2B) or 16K (26B A4B)
- ubatch size 256 (prefill) or 512 (generation for E2B)
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.4
sources:
- raw/cache/cc037e7fa5f7e3f8.md
- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
source_url: https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
fetched_at: '2026-07-06T02:19:19.351286+00:00'
type: optimization_recipe
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# SpaceMIT K3 Gemma 4 QAT MTP Configuration

Optimization recipe for running Gemma 4 QAT models (E2B 2B and 26B A4B) with Multi-Token Prediction (MTP) on the SpacemiT K3 board (Milk-V Jupiter 2). The transformation applies to llama.cpp server configuration, targeting maximum generation throughput with practical memory constraints. Prerequisites include the llama.cpp SpaceMIT fork built with CPU and RISC-V vector extension flags, and a Gemma 4 QAT model quantized to Q4_K_XL along with a Q4_0 draft model for MTP. The recipe recommends 8 threads (matching the 8 A100/IME2 performance cores), f16 KV cache (consistently outperforms q8_0 by ~1.8 tok/s), and specific context sizes: 32768 for the E2B model (interactive ceiling) and 16384 for the 26B model (sweet spot before OOM). ubatch size 256 is best for prefill; 512 improves generation on E2B. MTP is enabled with draft-mtp and n_max=4, but cache-reuse is auto-disabled by llama-server under draft-mtp. Prompt cache with 8 GiB budget is enabled for the E2B server. Failure modes include TCM contention with t>=12, OOM at context sizes above 16K for the 26B model, and channel-thought leakage if reasoning-format is not set to deepseek. Measurements from a 96-run llama-bench sweep and server benchmarks confirm the settings produce the highest throughput on this hardware.

## Key Claims

- Thread count must be exactly 8; t<8 segfaults, t>=12 causes TCM contention.
- f16 KV cache yields higher generation throughput than q8_0 across all tested contexts.
- For Gemma 4 E2B: ctx=32768, threads=8, ubatch=256/512, f16 KV, MTP enabled, prompt cache 8GiB.
- For Gemma 4 26B A4B: ctx=16384, threads=8, ubatch=256, f16 KV, MTP enabled, reasoning-format deepseek to prevent output leaks.
- 26B A4B memory usage at 16K ctx: ~1066 MiB with f16 KV; OOM at 64K.
- Cold server benchmark (E2B): +82 tok/s prefill, +12.93 tok/s generation, MTP acceptance 0.306.
- Warm request with prompt-cache hit: ~1 second round trip.

## Transformation

- Prerequisites:
  - SpacemiT K3 board (Milk-V Jupiter 2) with A100/IME2 cores and TCM enabled.
  - llama.cpp fork built with -DGGML_CPU_RISCV64_SPACEMIT=ON -DGGML_RV_ZBA=ON -DGGML_RV_ZFH=ON -DGGML_RV_ZVFH=ON.
  - Gemma 4 QAT model in Q4_K_XL format and corresponding Q4_0 draft MTP model.
  - tcm-cleanup before each run to clear TCM memory.
- Steps:
  1. For Gemma 4 E2B: use the provided run-gemma-e2b-qat-server.sh script or equivalent llama-server invocation with flags:
     --threads 8 --ubatch-size 256 (or 512 for gen) --ctx-size 32768 --cache-type-k f16 --cache-type-v f16
     --model gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf --model-draft mtp-gemma-4-E2B-it-qat-Q4_0.gguf
     --spec-type draft-mtp --spec-draft-n-max 4
     Optionally: enable prompt cache with --prompt-cache and 8 GiB budget.
  2. For Gemma 4 26B A4B: use similar invocation but with ctx-size 16384 and --reasoning-format deepseek.
- Expected effect:
  - E2B: ~12.9 tok/s generation, ~82 tok/s prefill (cold), ~1s warm round trip, MTP acceptance ~0.31.
  - 26B A4B: ~8.4 tok/s generation at 16K ctx, prefill not specified but likely lower; practical for 10-15 source files or full function-level code context.
- Failure modes:
  - t>=12 causes TCM contention leading to SIGABRT.
  - 26B model at ctx=32768 risks OOM; at ctx=65536 OOM kills the machine.
  - Without --reasoning-format deepseek, the 26B model may leak <|channel>thought tags into response body.
  - cache-reuse (KV shifting) is auto-disabled under draft-mtp, so omission is correct.
- Measurements:
  - Swaptable for E2B: cold prefill 93.14 tok/s, gen 12.93 tok/s, MTP acc 0.306 (complex agent prompt); warm request ~1s.
  - Llama-bench best: E2B prefill 120.90 tok/s (t=8 ub=256 f16), generation 13.36 tok/s (t=8 ub=512 f16).
  - 26B A4B context scaling table shows generation throughput flat from 4K to 16K (~8.46 to 8.36 tok/s) then drops at 32K (~6.1) and OOM at 64K.

## Relationships

No specific relationship to the visible context pages ([[q4x-quantization-llamacpp-rvv]], [[v-seek-llm-inference-optimization-sg2042]]) is established from the source material. The optimization is specific to the SpaceMIT K3 platform and Gemma 4 QAT models, which are not covered by existing pages. Future pages on SpaceMIT K3 hardware details or Gemma model performance could provide meaningful cross-links.

## Sources

- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
