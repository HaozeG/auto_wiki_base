---
type: entity
tags: [compiler, gpu, kernel, python, pytorch]
sources:
  - https://triton-lang.org/main/index.html
  - https://arxiv.org/abs/2111.01472
  - https://pytorch.org/docs/stable/torch.compile.html
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

# OpenAI Triton

OpenAI Triton is an open-source domain-specific language and compiler for writing GPU kernels in Python, targeting NVIDIA PTX and AMD GCN/RDNA ISAs. Released in 2021 and open-sourced under the MIT license, Triton allows researchers and engineers to write high-performance GPU programs without resorting to hand-written CUDA C++. The core abstraction is a tile-based programming model: instead of reasoning about individual SIMT threads, the programmer operates on tiles (contiguous blocks of memory), and the Triton compiler handles thread-level parallelism, shared-memory allocation, and vectorization automatically. Triton compiles Python-annotated functions through an MLIR-based intermediate representation to PTX, applying auto-tuning passes that select optimal tile sizes, pipeline depths, and memory access strategies at compile time. The resulting kernels routinely match or exceed hand-written CUDA performance for memory-bandwidth-bound and compute-bound workloads. Triton became a first-class component in PyTorch 2.0's `torch.compile` path, where the Inductor backend emits Triton kernels for GPU execution, replacing the need for manually-maintained fused operator libraries in many common cases.

## Key Claims

- Triton's tile abstraction lets a single Python function body generate kernels that match cuDNN-level performance on matrix multiply and attention without manual CUDA; benchmarks published by the Triton team show FlashAttention implemented in ~50 lines of Triton matching hand-written CUDA throughput on A100.
- PyTorch 2.0 `torch.compile` uses Triton as the default GPU backend via TorchInductor; as of PyTorch 2.1, roughly 80% of benchmark models see ≥10% speedup over eager mode on NVIDIA GPUs, driven largely by Triton-generated fused kernels.
- Triton auto-tuner performs exhaustive or heuristic search over tile size, number of warps, and pipeline stages; the winning configuration is cached so subsequent runs incur zero search overhead.
- Flash Attention 2 and Flash Attention 3 reference implementations are written in Triton, demonstrating that the language is sufficient to implement memory-IO-optimal attention algorithms that outperform PyTorch's `scaled_dot_product_attention` eager path by 2–4× on A100 for typical LLM sequence lengths.
- Triton supports AMD GPUs (via ROCm/HIP) and work is ongoing for Intel GPU targets through the MLIR SPIR-V backend, extending its reach beyond NVIDIA hardware.
- The Triton compiler IR sits above LLVM and is lowered through MLIR dialects (arith, scf, gpu, nvgpu) to PTX; this contrasts with hand-tuned CUDA, which requires vendor-specific intrinsics and architecture-specific tuning by the developer.

## Relationships

- [[flash_attention]] — Flash Attention and Flash Attention 2 are prototypically implemented in Triton, validating the language as capable of expressing IO-optimal attention algorithms.
- [[nvidia_hopper_h100]] — Triton targets NVIDIA PTX and uses H100-specific features (tensor memory accelerator, wgmma instructions) in the Triton-lang CUDA backend.
- [[groq_lpu]] — Groq's static compiler philosophy contrasts with Triton's JIT auto-tuning model; both aim to eliminate hand-tuning but through orthogonal mechanisms.
- [[mlir_llvm_ai]] — Triton's compiler backend is built on MLIR; Triton IR is an MLIR dialect lowered through the MLIR pass pipeline to target ISAs.

## Sources

- Tillet, P. et al. "Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations." MLSys 2019; updated open-source release 2021. https://arxiv.org/abs/2111.01472
- OpenAI Triton documentation: https://triton-lang.org/main/index.html
- PyTorch 2.0 blog: "Introducing PyTorch 2.0" — describes TorchInductor + Triton backend. https://pytorch.org/blog/pytorch-2.0-release/
- Flash Attention 2 Triton implementation: https://github.com/Dao-AILab/flash-attention
