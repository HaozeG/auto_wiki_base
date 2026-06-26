---
type: entity
tags: [performance-analysis, hardware, memory-bandwidth, compute-bound, memory-bound]
sources:
  - "Williams, S., Waterman, A., Patterson, D. (2009). Roofline: An Insightful Visual Performance Model for Multicore Architectures. CACM 52(4):65-76."
  - "https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html"
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

# Roofline Model / Arithmetic Intensity

The Roofline model is a visual performance analysis framework introduced by Williams, Waterman, and Patterson in 2009 that characterizes whether a computational kernel is limited by peak floating-point throughput (compute-bound) or by memory bandwidth (memory-bound). The central metric is **arithmetic intensity** (also called operational intensity), defined as the ratio of floating-point operations performed to bytes transferred from memory: measured in FLOP/byte. A kernel with low arithmetic intensity transfers large amounts of data relative to its computation, causing performance to be capped by memory bandwidth; a kernel with high arithmetic intensity is instead capped by the processor's peak FLOP/s. The boundary between these regimes is the **ridge point**: arithmetic intensity (FLOP/byte) = peak FLOP/s ÷ peak memory bandwidth (bytes/s). On NVIDIA's H100 SXM5 GPU, peak FP16 Tensor Core throughput is approximately 989 TFLOP/s and HBM3 bandwidth is approximately 3.35 TB/s, yielding a ridge point near 295 FLOP/byte. For FP8 (1,979 TFLOP/s peak) the ridge point doubles to roughly 590 FLOP/byte. Any kernel whose arithmetic intensity falls below the ridge point is memory-bound; above it is compute-bound. The Roofline model provides a ceiling that no implementation can exceed regardless of software optimization, making it a hardware-grounded baseline for performance engineers.

## Key Claims

- The ridge point for H100 SXM5 at FP16 precision is approximately 295 FLOP/byte (989 TFLOP/s ÷ 3.35 TB/s); at FP8 it is approximately 590 FLOP/byte.
- LLM autoregressive decoding (single-token generation with batch size 1) has arithmetic intensity well below 10 FLOP/byte because each forward pass reads the full model weight matrix (~tens of GB) to produce a single output vector, making decoding memory-bound on every current GPU generation.
- LLM prefill (processing an entire prompt in parallel) achieves arithmetic intensity proportional to sequence length × hidden dimension / bytes-per-weight; for sequence lengths in the hundreds to thousands, prefill is typically compute-bound on H100.
- Matrix multiplication of shape M×K × K×N has arithmetic intensity 2MKN / (2(MK + KN + MN) bytes) ≈ M/2 FLOP/byte for square matrices at FP16, meaning a 4096×4096 GEMM reaches ~2048 FLOP/byte, far above the H100 ridge point.
- The Williams et al. 2009 paper applied the Roofline model to 14 Berkeley dwarfs on multicore CPUs, demonstrating that memory bandwidth limits dominated for graph traversal and stencil operations while dense linear algebra was compute-bound.
- Flash Attention reformulates attention computation to reuse tiles of Q, K, V matrices in on-chip SRAM, raising effective arithmetic intensity from ~1-2 FLOP/byte (naive HBM-backed attention) to tens of FLOP/byte, moving attention from memory-bound to near-compute-bound operation.

## Relationships

- [[nvidia_hopper_h100]] — H100 SXM5 provides the concrete hardware parameters (989 TFLOP/s FP16, 3.35 TB/s HBM3) used to calculate the H100 ridge point of ~295 FLOP/byte.
- [[hbm_high_bandwidth_memory]] — HBM bandwidth is the denominator of the memory roof in the Roofline model; higher HBM bandwidth raises the memory roof and shifts the ridge point rightward.
- [[kv_cache_llm_inference]] — KV cache management during autoregressive decoding increases memory traffic (reading cached K/V tensors each token), worsening arithmetic intensity and deepening memory-bound behavior.
- [[flash_attention]] — Flash Attention's tiled SRAM reuse strategy directly improves arithmetic intensity for the attention kernel, a concrete application of Roofline-guided optimization.
- [[openai_triton]] — Triton kernels are commonly evaluated against the Roofline ceiling to verify that custom implementations approach hardware-attainable FLOP/s given their arithmetic intensity.

## Sources

- Williams, S., Waterman, A., Patterson, D. (2009). "Roofline: An Insightful Visual Performance Model for Multicore Architectures." *Communications of the ACM*, 52(4), 65–76. https://doi.org/10.1145/1498765.1498785
- NVIDIA H100 Tensor Core GPU Architecture Whitepaper (2022). https://resources.nvidia.com/en-us-tensor-core
- NVIDIA Deep Learning Performance Guide: GPU Background. https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html
- Dao, T. et al. (2022). "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness." NeurIPS 2022. (arithmetic intensity analysis of attention, Section 2)
