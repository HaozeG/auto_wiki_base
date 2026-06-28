---
cold_start: true
created: YYYY-MM-DD
datatypes:
- Q4_K_M
evidence_strength: measured
hardware_targets:
- Apple M4
hardware_versions:
- Apple M4
inbound_links: 1
measurement_method: Benchmarks were run on an Apple M4 system using the llama-cpp-mini
  inference engine built with CMake and Ninja in Release mode. The model file is Llama-3.2-1B-Instruct-Q4_K_M.gguf
  (770MB). Load time measured from invocation to model ready. Prefill and decode speeds
  reported in tokens per second.
metrics:
- load time
- prefill speed
- decode speed
scorecard:
  bridge_score: 0.5
  claim_density: 0.9
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- Llama-3.2-1B-Instruct-Q4_K_M.gguf
sources:
- https://github.com/yiquanlin212/llama-cpp-mini
tags:
- LLM
- inference
- Apple_M4
- GGUF
- benchmark
toolchains:
- C++20
- CMake
- Ninja
type: benchmark_result
updated: '2026-06-28'
workloads:
- LLM inference (Llama 3.2 1B)
------


# llama-cpp-mini Benchmark on Apple M4

This benchmark result documents the performance of the llama-cpp-mini inference engine running the Llama-3.2-1B-Instruct model quantized to Q4_K_M on an Apple M4 system. The measurements include model load time, prefill speed, and decode speed, all measured using the built-in reporting of the engine. The engine is a from-scratch C++20 implementation that loads GGUF weights and performs decoder-only transformer inference. The model file is 770MB. The measured load time is 1056 ms, prefill speed is 4.51 tok/s, and decode speed is 11.50 tok/s. These results provide baseline performance for this lightweight inference engine on Apple Silicon.

## Key Claims

- Model load time: 1056 ms for a 770MB GGUF file.
- Prefill speed: 4.51 tokens per second.
- Decode speed: 11.50 tokens per second.
- All measurements obtained on Apple M4 hardware with the Q4_K_M quantization.

## Measurement Context

- Hardware version: Apple M4.
- Software/toolchain version: llama-cpp-mini (C++20, built with CMake and Ninja, Release mode).
- Workload shape: Llama-3.2-1B-Instruct model with Q4_K_M quantization, sequence generation of 50 tokens after prompt "The capital of France is".
- Metric: Prefill speed (tok/s), decode speed (tok/s), load time (ms).
- Method: Engine reports times directly. Single run reported.
- Evidence strength: measured.

## Relationships

- [[llama-cpp-mini]] – The entity page for the inference engine that produced these results.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Both provide benchmark results for different hardware platforms (Apple M4 vs. RISC-V C910).

## Sources

- [GitHub repository: yiquanlin212/llama-cpp-mini](https://github.com/yiquanlin212/llama-cpp-mini)

