---
type: entity
tags: [ml-algorithm, attention, memory-optimization, gpu-optimization]
sources:
  - "Dao et al. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. NeurIPS 2022. https://arxiv.org/abs/2205.14135"
  - "Dao (2023). FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. ICLR 2024. https://arxiv.org/abs/2307.08691"
  - "Shah et al. (2024). FlashAttention-3: Fast and Accurate Attention for H100 GPUs. https://arxiv.org/abs/2407.08608"
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

# Flash Attention

FlashAttention is an IO-aware exact attention algorithm developed by Tri Dao et al. (Stanford, 2022) that computes the standard scaled dot-product attention result while avoiding the O(n²) memory materialization that makes vanilla attention prohibitively expensive for long sequences. The key insight is that modern GPU memory is hierarchical: on-chip SRAM is orders of magnitude faster than off-chip HBM (High Bandwidth Memory) but is limited in capacity (tens of MB vs. tens of GB). Standard attention implementations write the full n×n attention matrix to HBM and read it back for the softmax and output computation, incurring O(n²) HBM reads and writes. FlashAttention avoids this by tiling the computation: it loads blocks of Q, K, and V into SRAM, computes partial softmax outputs using the online softmax trick (Milakov & Gimelshein 2018), and accumulates the result without ever materializing the full attention matrix in HBM. The algorithm is mathematically equivalent to standard attention—it produces bit-identical outputs—while reducing HBM memory footprint from O(n²) to O(n) and cutting the number of HBM read/write operations by a factor proportional to the SRAM block size. On an A100 GPU, FlashAttention achieves 2–4× wall-clock speedup over a PyTorch baseline for typical sequence lengths (512–8192 tokens) and reduces peak memory by 5–20× for long sequences, enabling training at context lengths that would otherwise exceed GPU memory.

## Key Claims

- FlashAttention (v1, 2022) reduces attention HBM memory complexity from O(n²) to O(n) by tiling computation within SRAM, while computing mathematically exact (not approximate) attention.
- On an A100 80GB SXM GPU, FlashAttention achieves 2–4× speedup over standard PyTorch attention for sequence lengths of 512 to 8192 tokens and reaches up to 72% of A100 peak FLOP/s throughput.
- FlashAttention-2 (Dao 2023) improves parallelism by partitioning work across sequence length dimension and reduces non-matrix operations, achieving approximately 2× the throughput of FlashAttention-1 and up to 230 TFLOPS on A100.
- FlashAttention-3 (Shah et al. 2024) targets H100 specifically, exploiting asynchronous memory copies (TMA) and the wgmma instruction to overlap GEMM and softmax computation, reaching 740–760 TFLOPS on H100 SXM5 (75% of theoretical peak).
- The online softmax trick allows incremental computation of softmax across tiles by maintaining a running maximum and sum, enabling single-pass accumulation without storing the full score matrix.
- FlashAttention is the default attention kernel in PyTorch 2.0+ (via `torch.nn.functional.scaled_dot_product_attention`), Hugging Face Transformers, and all major LLM training frameworks including Megatron-LM and NanoGPT.
- For a sequence length of 64K tokens with d_head=128 in FP16, standard attention requires ~64 GB for the attention matrix alone; FlashAttention reduces this to ~2 MB of SRAM working memory.

## Relationships

- [[transformer_architecture]] — FlashAttention accelerates the self-attention sublayer of Transformer models without changing the mathematical output.
- [[nvidia_hopper_h100]] — FlashAttention-3 is explicitly optimized for H100's asynchronous execution pipeline (wgmma + TMA), achieving 75% of H100 theoretical peak FLOP/s.
- [[nvidia_blackwell_b200]] — Blackwell's FP8 Tensor Cores and increased SRAM per SM continue the hardware trend that makes IO-aware tiling algorithms like FlashAttention increasingly critical.
- [[hbm_high_bandwidth_memory]] — FlashAttention's primary optimization is minimizing round-trips to HBM; HBM bandwidth and latency directly determine the benefit of the algorithm.
- [[int8_fp8_quantization_llm_inference]] — FlashAttention-3 supports FP8 attention computation on H100, combining quantization with IO-aware tiling to further increase throughput.

## Sources

- Dao, T., Fu, D.Y., Ermon, S., Rudra, A., Ré, C. (2022). "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness." NeurIPS 2022. https://arxiv.org/abs/2205.14135
- Dao, T. (2023). "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning." ICLR 2024. https://arxiv.org/abs/2307.08691
- Shah, J. et al. (2024). "FlashAttention-3: Fast and Accurate Attention for H100 GPUs." https://arxiv.org/abs/2407.08608
- Milakov, M., Gimelshein, N. (2018). "Online normalizer calculation for softmax." https://arxiv.org/abs/1805.02867
