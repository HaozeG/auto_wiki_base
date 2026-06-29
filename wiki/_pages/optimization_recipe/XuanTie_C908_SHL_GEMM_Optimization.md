---
cold_start: false
constraints:
- VLEN128/256
- instruction fusion
- 16×12 register blocking
- outer product matrix operations
created: '2025-03-04'
datatypes:
- fp16
- fp32
- int8
evidence_strength: reported
hardware_targets:
- XuanTie C908
inbound_links: 8
metrics:
- speedup
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
tags:
- XuanTie
- C908
- GEMM
- SHL
- optimization
toolchains:
- SHL
type: optimization_recipe
updated: '2026-06-28'
workloads:
- GEMM
- Convolution (im2col+GEMM, Winograd)
---

# XuanTie C908 SHL GEMM Optimization
The Structure of Heterogeneous Library (SHL) provides an assembly-optimized GEMM implementation for the XuanTie C908 processor. The optimization targets convolution operators in neural networks using im2col+GEMM and Winograd algorithms. The core GEMM computation uses an outer product approach with 16×12 register blocks. Input data is loaded via scalar loads (flh) and weight data via vector loads (vle). Data dependencies (read-after-write, write-after-write) are manually eliminated to adjust instruction flow, and instruction fusion technology is applied to further improve performance. The recipe is described in a T-Head engineering blog post with reported speedup results.

## Key Claims

- GEMM implementation uses outer product with 16×12 register blocking.
- Scalar load for input data, vector load for weight data.
- Manual dependency removal (RAW, WAW) to optimize instruction scheduling.
- Instruction fusion technology integrated for additional throughput gains.
- Supports im2col+GEMM and Winograd convolution acceleration.

## Transformation

- Prerequisites: XuanTie C908 processor with RVV 1.0 support; SHL library; compiler with assembly-level optimization.
- Steps:
  1. Input padding and transformation (Winograd).
  2. Input reordering.
  3. Batch GEMM operations using outer product with register blocking.
  4. Output transformation and cropping.
- Expected effect: Accelerated convolution operator performance, especially for CNN inference. Reported speedups include 3.35× on MobileNet when combined with int8 dot product.
- Failure modes: Not specified.
- Measurements: Refer to [[XuanTie_C908_AI_Inference_Performance]] for reported speedups.

## Relationships

- [[XuanTie_C908]] – The hardware target for which the optimization is designed.
- [[XuanTie_C908_AI_Inference_Performance]] – Benchmark results demonstrating the effectiveness of this recipe.
- [[GEMM_with_RISC-V_Vector_Extension]] – General RISC-V vector GEMM kernel; the C908 optimization is a vendor-specific variant.

## Sources

- [XuanTie C908 Accelerates AI with Software and Hardware Fusion - RISC-V International](https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/)
