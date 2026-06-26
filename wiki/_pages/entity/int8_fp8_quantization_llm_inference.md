---
type: entity
tags: [quantization, inference, llm, int8, fp8, ptq, compression]
sources:
  - https://arxiv.org/abs/2206.09557
  - https://arxiv.org/abs/2208.09491
  - https://arxiv.org/abs/2211.10438
  - https://arxiv.org/abs/2306.00978
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# INT8/FP8 Quantization for LLM Inference

Post-training quantization (PTQ) for large language models reduces weight and activation numerical precision from 32-bit or 16-bit floating point to 8-bit integer (INT8) or 8-bit floating point (FP8) formats without requiring full retraining. This technique is critical for LLM deployment because memory bandwidth is the primary inference bottleneck: a 70-billion-parameter model stored in FP16 requires approximately 140 GB of memory, while INT8 halves that footprint to 70 GB and FP8 matches it while preserving a floating-point dynamic range. The practical throughput gain from 8-bit formats on modern accelerators stems from two effects: fewer bytes transferred from HBM per token generated (directly reducing memory-bandwidth-bound latency), and access to wider SIMD datapaths — NVIDIA Tensor Cores, Intel AMX, and ARM SME2 all expose INT8 or FP8 matrix-multiply units that deliver roughly 2× the peak TFLOPS relative to their FP16 counterparts. Quantization error is controlled through calibration: a small representative dataset (typically 128–512 samples) is used to measure activation ranges, which are then encoded as per-tensor or per-channel scale factors. The dominant accuracy risk is the emergence of large-magnitude "outlier" activations in transformer hidden states beyond roughly 6.7 billion parameters, which can widen the quantization range and degrade perplexity by 1–5 points on standard benchmarks if not specifically handled.

## Key Claims

- **GPTQ** (Frantar et al., 2022) quantizes LLM weights to INT4 or INT8 using an approximate second-order (Hessian-based) update, compressing a 175 B OPT model in under 4 GPU-hours with less than 1 point of WikiText-2 perplexity degradation at INT4.
- **SmoothQuant** (Xiao et al., 2022) migrates quantization difficulty from activations to weights by multiplying activations by a per-channel smoothing factor α and dividing weights by the same factor, enabling accurate INT8 weight-and-activation quantization for GPT-3-scale models with <1% accuracy loss on zero-shot benchmarks.
- **AWQ** (Lin et al., 2023) identifies the 1% of weight channels that are most salient (correlated with large activation magnitudes) and applies per-group scaling only to those channels, achieving INT4 quantization of LLaMA-2 70B with 5.68 WikiText-2 perplexity versus 3.32 for FP16 — a gap of 2.36 points preserved across a 4× memory reduction.
- **Absmax scaling** maps the maximum absolute value of a tensor to 127 (INT8) or the FP8 max (448 for E4M3), producing a single per-tensor scale; **zero-point scaling** adds an integer offset to handle asymmetric distributions, reducing quantization error for ReLU-activated layers by up to 40% over absmax alone.
- NVIDIA H100 FP8 Tensor Cores (E4M3 and E5M2 formats) deliver 3,958 TFLOPS peak for FP8 matrix multiply, versus 1,979 TFLOPS for FP16 — exactly 2× — as specified in the H100 datasheet.
- Intel AMX TMUL instructions operate on INT8 tiles and deliver up to 16× throughput improvement over scalar INT8 on Sapphire Rapids CPUs for matrix multiply workloads, as measured by Intel in MLPerf submissions.
- Activation quantization is substantially harder than weight quantization: weights are static and can be calibrated offline, while activations vary per input; this asymmetry motivated weight-only quantization schemes (GPTQ, AWQ) that keep activations in FP16 at inference time.

## Relationships

- [[nvidia_hopper_h100]] — H100 introduces native FP8 Tensor Core support (E4M3/E5M2 formats) that FP8 PTQ methods are specifically designed to target.
- [[nvidia_tensor_cores]] — INT8 Tensor Cores (Turing/Ampere/Hopper) provide the 2× throughput gain that makes INT8 quantization practically impactful; GPTQ and SmoothQuant map directly to these units.
- [[intel_amx]] — AMX TMUL tiles support INT8 matrix multiply; SmoothQuant and GPTQ have been validated on AMX-equipped Sapphire Rapids CPUs for CPU-based LLM inference.
- [[arm_sme2]] — SME2 outer-product instructions support INT8 and FP8 accumulation, enabling the same PTQ techniques on Arm server and edge SoCs.
- [[nvidia_2_4_structured_sparsity]] — Sparsity and quantization are orthogonal and composable: 2:4 sparsity applied before INT8 quantization can yield up to 4× combined throughput improvement on Ampere/Hopper hardware.

## Sources

- Frantar et al. (2022). "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers." https://arxiv.org/abs/2210.17323
- Xiao et al. (2022). "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models." https://arxiv.org/abs/2211.10438
- Lin et al. (2023). "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration." https://arxiv.org/abs/2306.00978
- NVIDIA H100 Tensor Core GPU Architecture Whitepaper, 2022. https://resources.nvidia.com/en-us-tensor-core
- Dettmers et al. (2022). "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale." https://arxiv.org/abs/2208.07339
