---
canonical_name: Tile Language
aliases:
- tile-lang
- tilelang
- TileLang
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/73e187183bb4266d.md
- https://github.com/Lyscoria/tilelang-personal
source_url: https://github.com/Lyscoria/tilelang-personal
fetched_at: '2026-07-02T05:34:29.022955+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Tile Language

Tile Language (tile-lang) is a domain-specific language (DSL) designed to streamline the development of high-performance GPU and CPU kernels for AI workloads, including matrix multiplication (GEMM), dequantization GEMM, FlashAttention, and LinearAttention. It employs a Pythonic syntax and is built on top of the Apache TVM compiler infrastructure, enabling developers to write concise kernel code while the underlying compiler handles low-level optimizations such as auto-TMA, WGMMA, and NVRTC backends. Tile-lang supports a range of hardware devices including NVIDIA GPUs (H100, A100, V100, RTX 4090, RTX 3090), AMD GPUs (MI250, MI300X), Apple Metal, and Huawei Ascend NPUs. The project is open source and available on GitHub, with a dedicated puzzle-based learning resource. Tile-lang aims to balance productivity and performance, offering a Pythonic interface to state-of-the-art kernel optimizations.

## Key Claims

- Tile-lang is a concise DSL for developing high-performance GPU/CPU kernels with a Pythonic syntax.
- It compiles through Apache TVM, enabling automatic low-level optimizations (TMA, WGMMA, NVRTC, CuTeDSL).
- Supports multiple backends: CUDA, AMD ROCm, Apple Metal, Huawei Ascend NPU, WebGPU, CuTeDSL.
- Implements a variety of operators: GEMM, Dequant GEMM, FlashAttention, LinearAttention, Flash MLA Decoding, Native Sparse Attention.
- Achieves performance parity with hand-optimized kernels: FlashMLA on AMD MI300X matches Aiter; MLA decoding on H100 matches FlashMLA.
- Integrated Z3 theorem prover for SMT-based symbolic reasoning and automatic correctness verification.
- Tested on NVIDIA H100, A100, V100, RTX 4090, RTX 3090, RTX A6000; AMD MI250, MI300X.
- Version v0.1.0 released February 2025; v0.1.6.post2 is the last Python 3.8 compatible release.

## Relationships

- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A compiler-driven GEMM optimization using MLIR and xDSL for RISC-V, contrasting with tile-lang's TVM-based approach targeting GPUs and CPUs.
- [[xuantie_c908_fp16_gemm_kernel]]: A hand-tuned RISC-V GEMM kernel for a specific CPU, whereas tile-lang uses DSL compilation for cross-platform kernel generation.
- [[grayskull_e75_matmul_benchmark]]: A benchmark result for a different hardware platform, providing complementary performance data for matrix multiplication.
- Note: insufficient context for additional cross-links to entity pages; the wiki does not contain related entity pages that reference tile-lang or similar DSLs.

## Sources

- https://github.com/Lyscoria/tilelang-personal
