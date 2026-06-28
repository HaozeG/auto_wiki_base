---
cold_start: true
constraints:
- 64-core RISC-V
- rv64imafdcv
- 125GB RAM
- NVMe SSD
- Fedora 38
- no GPU
created: '2025-11-10'
hardware_targets:
- MilkV Pioneer
inbound_links: 3
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://bruno.verachten.fr/2025/11/10/running-a-70b-llm-on-pure-risc-v-the-milkv-pioneer-deployment-journey/
tags:
- RISC-V
- workstation
- LLM
- MilkV
- 64-core
toolchains:
- GCC 13.2.1
- CMake
type: hardware_target
updated: '2026-06-28'
---

# MilkV Pioneer

The MilkV Pioneer is a 64-core RISC-V workstation-class machine designed for high-performance computing and AI workloads. It features a 64-core RISC-V CPU with ISA string rv64imafdcv, which includes integer, multiply/divide, atomic, single and double precision floating-point, compressed instructions, and critically, vector extensions (v). The system is equipped with 125GB of RAM (122GB available after OS overhead), an NVMe SSD, and runs Fedora Linux 38. Notably, it has no GPU accelerator; inference relies entirely on CPU execution. The vector extensions (RVV) provide SIMD capabilities analogous to ARM NEON or x86 AVX, enabling efficient parallelisation of matrix multiplications for transformer-based models. The Pioneer's large memory capacity (125GB) allows loading quantized 70-billion parameter language models without swapping. The system's build and deployment process for LLM inference software was documented in a community blog post, demonstrating that llama.cpp and Ollama can be built and run on this hardware with standard toolchains (GCC 13.2.1, CMake) and configuration settings leveraging ARM-optimized code paths via GGML_CPU_AARCH64=ON.

## Key Claims

- 64-core RISC-V CPU with rv64imafdcv (includes vector extension v).
- 125GB RAM, 122GB available after OS overhead.
- No GPU: pure CPU inference.
- Successfully runs llama.cpp built with GGML_CPU_AARCH64=ON.
- Can load a 70B parameter model quantized to Q4_0 (~40GB).
- Fedora Linux 38 riscv64 operating system.
- Vector extensions (v) are critical for LLM inference performance; without them, inference would be 5-10x slower.

## Optimization-Relevant Details

- ISA/profile: rv64imafdcv (RV64GC + vector extension v)
- Vector/matrix/accelerator support: RISC-V Vector Extension (RVV) v1.0 (implied by rv64imafdcv)
- Memory/cache/TLB/DMA: 125GB RAM, NVMe SSD (939GB), no separate GPU memory; memory hierarchy not detailed in source.
- Compiler/toolchain support: GCC 13.2.1 (Red Hat), CMake, ccache; build tested with llama.cpp.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – Another RISC-V hardware target for GEMM, contrasting dedicated accelerator vs. general-purpose CPU inference.
- [[RVV_Autovectorization_Optimization_Insights]] – Optimization insights for RVV, relevant to maximizing vector utilization on the Pioneer's vector extensions.

## Sources

- [Bruno Verachten, "Running a 70B LLM on Pure RISC-V: The MilkV Pioneer Deployment Journey"](https://bruno.verachten.fr/2025/11/10/running-a-70b-llm-on-pure-risc-v-the-milkv-pioneer-deployment-journey/)

