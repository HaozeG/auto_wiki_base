---
canonical_name: TinyLlama 1.1B Inference on Banana Pi F3 (llama.cpp)
aliases:
- llama.cpp TinyLlama Banana Pi F3
- TinyLlama on RISC-V board
subtype: null
tags: []
hardware_targets:
- Banana Pi F3
- SpacemiT K1
workloads:
- TinyLlama 1.1B text generation
datatypes: []
metrics:
- tokens/second
toolchains:
- llama.cpp (git clone --depth 1, built from source)
- GCC 14.2.0
- cmake 3.31.6
hardware_versions:
- Banana Pi F3 (SpacemiT K1, 8 cores @ 1.6 GHz, 16 GB RAM)
software_versions:
- llama.cpp (commit from February 2026)
- Armbian 25.11.2 (Debian 13 trixie)
- Kernel 6.6.99-current-spacemit
measurement_method: OpenAI-compatible API server built into llama.cpp server binary.
  Short query, batch-1 inference. Benchmarks recorded as 8.29 tokens/second in benchmark
  mode, 8.76 tokens/second on short queries.
evidence_strength: measured
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/1edc7a10481145b4.md
- https://dev.to/gounthar/running-a-local-llm-on-risc-v-building-llamacpp-on-a-banana-pi-f3-part-1-4d5g
source_url: https://dev.to/gounthar/running-a-local-llm-on-risc-v-building-llamacpp-on-a-banana-pi-f3-part-1-4d5g
fetched_at: '2026-07-02T10:34:55.066018+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# TinyLlama 1.1B Inference on Banana Pi F3 (llama.cpp)

On a Banana Pi F3 single-board computer (SpacemiT K1 SoC, 8-core 1.6 GHz RISC-V X60 processor, 16 GB RAM) running Armbian 25.11.2 with kernel 6.6.99-current-spacemit, llama.cpp was built from source using GCC 14.2.0 and cmake 3.31.6. An OpenAI-compatible API server was deployed and used to run inference with TinyLlama 1.1B. The measured throughput was approximately 8.5 tokens/second, with benchmark mode yielding 8.29 tokens/second and short queries achieving up to 8.76 tokens/second. This benchmark demonstrates the feasibility of running local LLM inference on RISC-V hardware without cloud API dependencies, using the llama.cpp inference engine.

## Key Claims

- TinyLlama 1.1B inference at ~8.5 tokens/second on Banana Pi F3.
- Benchmark mode: 8.29 tokens/second.
- Short query throughput: 8.76 tokens/second.
- Inference performed using a locally built llama.cpp server, fully offline.
- The build required handling of RISC-V vector extensions (zvfh for float16 support).

## Measurement Context

- Hardware version: Banana Pi F3 with SpacemiT K1 (X60), 8 cores @ 1.6 GHz, 16 GB RAM (14 GB usable).
- Software/toolchain version: llama.cpp (February 2026 snapshot), GCC 14.2.0, cmake 3.31.6, Armbian 25.11.2, kernel 6.6.99-current-spacemit.
- Workload shape: TinyLlama 1.1B text generation, batch size 1.
- Metric: tokens/second (output generation rate).
- Method: llama.cpp server binary serving OpenAI-compatible API; measurements from author's blog including benchmark mode and short query.
- Evidence strength: measured (real-world execution on physical hardware).

## Relationships

- [[mlperf-inference-tiny-benchmark]]: related via shared inference.

- [[llama.cpp]]: related via shared cpp, llama.

- [[banana-pi-bpi-f3]]: related via shared banana.

- [[spacemit-x60-processor]]: The benchmark runs on the SpacemiT X60 processor integrated in the K1 SoC.
- [[llvm-risc-v-fptrunc-narrowing-optimization]]: Compiler optimizations for RISC-V floating-point operations may affect inference performance on this hardware.
- Insufficient context for additional cross-links.

## Sources

- [Running a Local LLM on RISC-V: Building llama.cpp on a Banana Pi F3 (Part 1) - DEV Community](https://dev.to/gounthar/running-a-local-llm-on-risc-v-building-llamacpp-on-a-banana-pi-f3-part-1-4d5g)
