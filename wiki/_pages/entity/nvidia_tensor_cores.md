---
type: entity
tags: [nvidia, gpu, hardware, ai-accelerator, matrix-multiply]
sources:
  - https://developer.nvidia.com/blog/programming-tensor-cores-cuda-9/
  - https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf
  - https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf
  - https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
  - https://newsletter.semianalysis.com/p/nvidia-tensor-core-evolution-from-volta-to-blackwell
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# NVIDIA Tensor Cores

NVIDIA Tensor Cores are specialized fixed-function matrix-multiply-accumulate (MMA) units integrated into NVIDIA GPU streaming multiprocessors (SMs), first introduced in the Volta microarchitecture (V100, 2017). Unlike general-purpose CUDA cores that perform scalar or vector operations, Tensor Cores execute a fused D = A×B + C matrix operation in a single clock cycle at the warp level. Each Volta Tensor Core performs a 4×4×4 matrix multiply-accumulate in one clock step; 32 threads in a warp cooperate via the WMMA (warp matrix multiply-accumulate) API to expose a 16×16×16 tile operation to CUDA programmers through the `nvcuda::wmma` namespace introduced in CUDA 9.0. Tensor Cores deliver dramatically higher throughput than CUDA cores for the dense matrix multiplications that dominate deep learning training and inference workloads, including transformers, CNNs, and RNNs, because the hardware pipelines MMA operations without per-element memory traffic. Each generation since Volta has expanded supported data types downward (lower precision, higher throughput) and upward (FP64 for HPC), while doubling or quadrupling peak throughput per SM per generation.

## Key Claims

- **Volta V100 (2017):** 640 Tensor Cores per GPU; each performs 64 FMA operations per clock; peak throughput 125 TFLOPS FP16 with FP32 accumulation; WMMA API tile shape is 16×16×16.
- **Turing (T4, 2018):** Second-generation Tensor Cores added INT8 (up to 261 TOPS) and INT4 precision support alongside FP16, enabling quantized inference at lower precision than Volta.
- **Ampere A100 (2020):** Third-generation Tensor Cores introduced TF32 (TensorFloat-32) — a 19-bit format with 8-bit exponent and 10-bit mantissa — providing 10× the FP32 throughput of V100; also added BF16 support; structured 2:4 sparsity doubles effective throughput for all data types.
- **Hopper H100 (2022):** Fourth-generation Tensor Cores support FP8, FP16, BF16, TF32, FP64, and INT8 MMA; deliver double the dense/sparse math throughput per SM per clock versus A100; H100 SXM5 peaks at 3,958 TFLOPS FP8 (with sparsity) and 1,979 TFLOPS FP16 (with sparsity).
- **Hopper Transformer Engine:** Automatically selects between FP8 and FP16 precision per operation during training with no manual tuning; enables up to 4× faster training on GPT-3 (175B parameter) models compared to A100.
- **Programming model:** Tensor Core access requires warp-level cooperation — all 32 threads in a warp must participate collectively; higher-level abstractions include CUTLASS, cuBLAS, and (on Hopper) the WGMMA (warpgroup MMA) PTX instruction targeting groups of 4 warps (128 threads) for larger tiles.

## Relationships

- [[nvidia_hopper_h100]] — H100 GPU that contains fourth-generation Tensor Cores and the Transformer Engine built around FP8 Tensor Core operations
- [[google_tpu]] — Google's TPU systolic array pursues the same dense MMA workloads as Tensor Cores but via a dedicated off-die accelerator rather than SM-integrated units
- [[intel_amx]] — Intel Advanced Matrix Extensions provide CPU-side matrix tiles (AMX TMUL) analogous in purpose to Tensor Cores, targeting BF16 and INT8 at the socket level
- [[arm_sme]] — ARM Scalable Matrix Extension adds outer-product MMA to general-purpose CPUs, addressing the same GEMM bottleneck Tensor Cores solve in GPUs
- [[gemmini]] — Gemmini is an open-source systolic array generator inspired by the same GEMM acceleration principles as Tensor Cores, targeting RISC-V SoCs

## Sources

- NVIDIA Volta Architecture Whitepaper (2017): 640 Tensor Cores, 125 TFLOPS FP16, 4×4×4 MMA — https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf
- NVIDIA blog "Programming Tensor Cores in CUDA 9" (2017): WMMA API, 16×16×16 tile, nvcuda::wmma namespace — https://developer.nvidia.com/blog/programming-tensor-cores-cuda-9/
- NVIDIA Ampere A100 Architecture Whitepaper (2020): TF32, BF16, 2:4 sparsity, 10× FP32 vs V100 — https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf
- NVIDIA Hopper Architecture In-Depth (2022): fourth-gen Tensor Cores, FP8, Transformer Engine, 4× GPT-3 speedup — https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- SemiAnalysis "NVIDIA Tensor Core Evolution: From Volta to Blackwell": cross-generation throughput comparison — https://newsletter.semianalysis.com/p/nvidia-tensor-core-evolution-from-volta-to-blackwell
