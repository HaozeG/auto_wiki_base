---
canonical_name: llama.cpp
aliases:
- llama.cpp
- LLM inference in C/C++
- ggml-org/llama.cpp
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.6
sources:
- raw/cache/6d386c7dca8e34a3.md
- https://github.com/ggml-org/llama.cpp
source_url: https://github.com/ggml-org/llama.cpp
fetched_at: '2026-07-02T11:33:55.835431+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# llama.cpp

llama.cpp is an open source software library that performs inference on various large language models (LLMs) such as Llama. It is co-developed alongside the GGML tensor library and is written in plain C/C++ without external dependencies. The main goal of llama.cpp is to enable LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware, including both local and cloud environments. Apple silicon is treated as a first-class citizen, with optimizations through ARM NEON, Accelerate, and Metal frameworks. The library also supports x86 architectures via AVX, AVX2, AVX512, and AMX, and RISC-V systems through RVV, ZVFH, ZFH, and ZICBOP extensions. This broad hardware support makes llama.cpp a versatile tool for running LLMs efficiently across different platforms.

## Key Claims

- Enables LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware.
- Written in plain C/C++ without dependencies.
- Optimized for Apple silicon architectures (ARM NEON, Accelerate, Metal).
- Provides support for x86 architectures (AVX, AVX2, AVX512, AMX).
- Supports RISC-V vector extensions (RVV, ZVFH, ZFH, ZICBOP).
- Runs on both local and cloud environments.

## Relationships

- [[gemmini]]: Both llama.cpp and Gemmini are tools for AI acceleration, though Gemmini is a hardware generator while llama.cpp is a software inference library.
- [[nncase]]: Both are open-source software projects for AI inference, with nncase targeting RISC-V accelerators and llama.cpp providing general LLM inference.

## Sources

- GitHub repository: https://github.com/ggml-org/llama.cpp
