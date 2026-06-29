---
cold_start: true
constraints:
- integer-only arithmetic units required
- no dedicated floating-point units on target edge processors
created: '2026-06-29'
datatypes:
- INT4
- INT8
evidence_strength: reported
hardware_targets:
- ARM Cortex-M
- GreenWaves GAP-9
- Google Edge TPU
- Turing Tensor Cores
inbound_links: 0
metrics:
- accuracy
- perplexity
- latency
- speedup
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/html/2405.17849v2
tags:
- LLM
- integer-only
- quantization
- PTQ
- edge
- FPGA
- GPU
toolchains: []
type: optimization_recipe
updated: '2026-06-29'
workloads:
- LLM inference (LLaMA-7b, LLaMA-13b)
---

# I-LLM: Integer-Only Inference Optimization for LLMs

I-LLM is a post-training quantization (PTQ) framework that enables fully integer-only inference for large language models (LLMs), eliminating all floating-point operations during deployment. The framework addresses the key obstacle of large activation fluctuations across channels and tokens in both linear and non-linear operations. I-LLM introduces three core techniques: Fully-Smooth Block-Reconstruction (FSBR) to smooth inter-channel variations, Dynamic Integer-only MatMul (DI-MatMul) for dynamic quantization in matrix multiplication, and integer-only operators (DI-ClippedSoftmax, DI-Exp, DI-Norm) that use bit shifting to replace complex math. This optimization targets edge devices (e.g., ARM Cortex-M, GreenWaves GAP-9, Google Edge TPU) and GPU Tensor Cores that lack floating-point capability, enabling efficient low-bit (e.g., W4A4) LLM inference. The paper reports that I-LLM achieves accuracy comparable to the floating-point baseline while outperforming non-integer quantization methods, such as a 20% perplexity reduction on LLaMA-13b relative to existing non-integer techniques.

## Key Claims

- I-LLM is the first framework to enable integer-only quantization for LLMs, bridging the gap between integer arithmetic and LLM inference.
- FSBR reduces inter-channel activation variations across all suitable activation-activation and activation-weight pairs, including within non-linear operators like SwiGLU, by decomposing the operation and applying smoothing.
- DI-MatMul dynamically quantizes inputs and outputs using integer-only operations, adapting to varying token ranges and minimizing quantization errors compared to static methods.
- DI-ClippedSoftmax, DI-Exp, and DI-Norm replace floating-point nonlinear operations with bit-shifting integer equivalents, maintaining accuracy.
- I-LLM achieves W4A4 quantization with negligible accuracy loss relative to the FP baseline.
- On LLaMA-13b, I-LLM yields an approximate 20% reduction in perplexity over state-of-the-art non-integer quantization techniques.
- The method is applicable to edge processors lacking FP units and to server-class GPU Tensor Cores that support integer logical units with lower latency.

## Transformation

- Prerequisites: A target LLM (e.g., LLaMA-7b, LLaMA-13b) and a hardware platform with integer arithmetic support (ARM Cortex-M, GAP-9, Edge TPU, or Turing Tensor Cores with integer logical units). No floating-point units required.
- Steps:
  1. Apply Fully-Smooth Block-Reconstruction (FSBR) to smooth inter-channel variations for all activation-activation and activation-weight pairs. This includes decomposing non-linear operators (e.g., SiLU into x * σ(x)) to enable smoothing.
  2. Use Dynamic Integer-only MatMul (DI-MatMul) for matrix multiplications. This dynamically quantizes inputs and outputs using integer-only operations, adapting to per-token variation.
  3. Replace Softmax, exponential functions, and normalization (RMSNorm) with DI-ClippedSoftmax, DI-Exp, and DI-Norm, respectively. These use bit-shifting to compute in integers.
  4. Quantize all weights and activations to low-bit integers (e.g., W4A4) using the smoothed and dynamically quantized framework.
- Expected effect: Fully integer-only inference with accuracy comparable to FP baseline. Speedup from using integer arithmetic units and reduced data movement due to lower bit-width. Enables deployment on resource-constrained devices.
- Failure modes: Not explicitly discussed in the available resource. Potential failure includes degradation if activation variations are not fully smoothed, or if dynamic quantization introduces overhead on certain hardware without integer logical unit support.
- Measurements: The paper reports that I-LLM achieves FP-comparable accuracy at W4A4 and a 20% perplexity reduction on LLaMA-13b over non-integer PTQ methods. Specific latency/speedup numbers are not provided in the extracted content but are claimed to result from integer-only arithmetic. Evidence strength is classified as reported based on the paper's claims.

## Relationships

- [[T-SAR_Benchmark_Results]] – Another optimization targeting LLM inference on edge hardware (ternary quantization on AVX2), providing a contrasting approach to I-LLM's integer-only method.
- [[Parallel_GEMM_Convolution_on_GAP8]] – An optimization recipe for edge AI on RISC-V using INT8 arithmetic; both target low-bit integer inference on constrained platforms.

## Sources

- [I-LLM paper on arXiv](https://arxiv.org/html/2405.17849v2)

