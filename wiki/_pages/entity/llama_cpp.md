---
canonical_name: llama.cpp
aliases:
- llama-cpp
- LLM inference in C/C++
- ggml-org/llama.cpp
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.9
sources:
- raw/cache/d4041c87a3b8b19a.md
- https://github.com/ggml-org/llama.cpp
source_url: https://github.com/ggml-org/llama.cpp
fetched_at: '2026-07-02T04:13:23.037775+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
---

# llama.cpp

llama.cpp is a high-performance C/C++ library and suite of tools for running large language model (LLM) inference locally with minimal setup. Developed by the GGML organization, it serves as the primary development environment for the GGML tensor library. The project supports a wide range of integer quantization formats from 1.5-bit to 8-bit, reducing memory usage and accelerating inference. It includes explicit support for RISC-V architectures through the RVV, ZVFH, ZFH, ZICBOP, and ZIHINTPAUSE extensions, enabling efficient execution on RISC-V hardware. The library is dependency-free, implemented in plain C/C++, and designed to deliver state-of-the-art performance across diverse hardware platforms, from local computers to cloud instances.

## Key Claims

- Enables LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware, locally and in the cloud.
- Provides 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization formats for faster inference and reduced memory use.
- Supports RISC-V architectures with RVV, ZVFH, ZFH, ZICBOP, and ZIHINTPAUSE extensions.
- Is dependency-free, implemented in plain C/C++.
- Is the primary development environment for the GGML tensor library.

## Relationships

- Hardware target: [[xuantie_c908]] – the XuanTie C908 RISC-V processor is one of the hardware targets that can execute llama.cpp inference workloads, benefiting from the RVV support in the library.
- Compiler target: [[llvm_riscv_target]] – the LLVM RISC-V target provides the compiler infrastructure needed to build llama.cpp for RISC-V platforms, including support for the vector extensions that llama.cpp exploits.

## Sources

- https://github.com/ggml-org/llama.cpp
