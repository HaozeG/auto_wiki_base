---
canonical_name: SpacemiT K3
aliases:
- K3
- SpacemiT K3 SoC
- Bianbu K3
- MilkV Jupiter 2
- Milk-V Jupiter 2
- llama.cpp inference on SpacemiT K3
- SpacemiT K3 LLM benchmark
- llama.cpp K3 benchmark
- Llama.cpp SpaceMIT K3 Gemma 4 QAT MTP Benchmarks
- llama-cpp-spacemit-k3
- SpaceMIT K3 Gemma 4 benchmarks
- Milk-V Jupiter 2 Gemma 4 benchmarks
subtype: null
tags:
- RISC-V
- SpacemiT
- AI CPU
- big.LITTLE
- RVV 1.0
hardware_targets:
- SpacemiT K3
- SpacemiT X100
- SpacemiT A100
toolchains:
- GCC 15.2.0
- cmake
- llama.cpp
constraints:
- 16 cores: 8 X100 (general-purpose) + 8 A100 (AI acceleration)
- X100: 2.4 GHz, vlen 256 bits, ISA rv64imafdcvh
- A100: 2.0 GHz, vlen 1024 bits, ISA rv64imafdcv (no hypervisor)
- shared extensions: zicbop, zicond, zfa, zawrs, vector crypto, zvfh
- 32 GB shared RAM
- Linux kernel 6.18.3
- GCC 15.2.0 compiler
- IME2 matrix instructions (vendor-only, not public)
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/c87de398f6c8a898.md
- https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
- raw/cache/673f92af34a7ba79.md
- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
- raw/cache/cc037e7fa5f7e3f8.md
- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
source_url: https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
fetched_at: '2026-07-03T16:13:21.390248+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
outbound_links:
- target: spacemit-x60-hardware-target
  reason: The X100 general-purpose core in the K3 is the successor to the X60 core
    in the SpacemiT K1 SoC, sharing the same 256-bit vector width but operating at
    a 50% higher clock (2.4 GHz vs 1.6 GHz) and achieving 2.3x faster token generation
    throughput on TinyLlama 1.1B Q4_0
---

# SpacemiT K3

SpacemiT K3 is a 16-core RISC-V AI CPU designed by SpacemiT Technology, featuring a big.LITTLE architecture with two core types on the same die: eight X100 general-purpose cores (2.4 GHz, 256-bit vector length) and eight A100 AI accelerator cores (2.0 GHz, 1024-bit vector length). Both core types share the RV64IMAFDCV base ISA and common extensions including zicbop, zicond, zfa, zawrs, vector crypto, and half-precision float support (zvfh). The X100 cores additionally implement the hypervisor extension (rv64imafdcvh), while the A100 cores omit virtualization support. The K3 runs Linux kernel 6.18.3 with 32 GB of shared RAM and uses GCC 15.2.0 as the default toolchain. The chip is accessible via SpacemiT's BianbuCloud platform for remote evaluation. The A100 cores include proprietary IME2 matrix instructions that are not yet supported by public compiler toolchains, requiring a vendor-specific build of llama.cpp to achieve optimal AI inference performance.

## Key Claims

- The K3 has two core types: X100 (general-purpose, vlen 256) and A100 (AI acceleration, vlen 1024), identical ISA extensions except the hypervisor extension (X100 only).
- X100 cores run at 2.4 GHz, A100 cores at 2.0 GHz.
- Total system memory is 32 GB shared across both core types.
- The A100 cores support proprietary IME2 matrix instructions for AI acceleration, which are not publicly compiled in standard toolchains.
- The K3 was accessed via the BianbuCloud platform, which uses Chinese-locale web terminals and requires ssh-rsa for access.
- Standard llama.cpp built with GGML_NATIVE=ON runs 2.3x faster on X100 cores than the K1's X60 cores, but 34x slower on A100 cores than X100 at single-thread prompt processing.
- SpacemiT's custom build using IME2 instructions achieves 111 t/s prompt processing on A100, making A100 the fastest core type.

## Optimization-Relevant Details

- ISA/profile: X100: rv64imafdcvh; A100: rv64imafdcv; shared: zicbop, zicond, zfa, zawrs, vector crypto, zvfh
- Vector/matrix/accelerator support: X100: RVV 1.0, vlen 256 bits; A100: RVV 1.0, vlen 1024 bits, plus IME2 matrix instructions
- Memory/cache/TLB/DMA: 32 GB shared RAM; no further cache details in source
- Compiler/toolchain support: GCC 15.2.0 (standard); vendor toolchain for IME2 not public

## Relationships

- [[spacemit-x60-hardware-target]]: The X100 general-purpose core in the K3 is the successor to the X60 core in the SpacemiT K1 SoC, sharing the same 256-bit vector width but operating at a 50% higher clock (2.4 GHz vs 1.6 GHz) and achieving 2.3x faster token generation throughput on TinyLlama 1.1B Q4_0.

## Sources

- https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
