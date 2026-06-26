---
type: entity
tags: [sparsity, pruning, ampere, hopper, inference, compression, structured-sparsity]
sources:
  - https://arxiv.org/abs/2104.08378
  - https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/
  - https://arxiv.org/abs/2009.14053
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

# NVIDIA 2:4 Structured Sparsity

NVIDIA 2:4 structured sparsity is a hardware-enforced weight pruning format introduced with the Ampere GPU architecture (A100, 2020) in which exactly 2 out of every 4 consecutive values in a weight matrix are forced to zero. This fixed pattern allows the sparse weights to be stored in a compressed representation — two non-zero values and a 2-bit metadata index per group of 4 — halving the effective memory footprint and enabling the Sparse Tensor Core units on Ampere and Hopper GPUs to skip computation on zero elements. The result is a peak throughput of 2× relative to the dense INT8 or FP16 Tensor Core path: an A100 delivers 312 TFLOPS for dense FP16 but 624 TFLOPS for FP16 with 2:4 sparsity. The standard deployment workflow — prune to the 2:4 pattern, then fine-tune on the original training data — typically recovers most of the accuracy lost to pruning: BERT-Large and ResNet-50 both recover to within 1% of dense accuracy after fine-tuning for a few thousand steps. Because the pattern is structural (positional, not value-based), the hardware encoding is deterministic and requires no runtime index lookup beyond reading the fixed 2-bit metadata, keeping the memory access pattern predictable and latency low. The technique is orthogonal to quantization: combining 2:4 sparsity with INT8 quantization can yield up to 4× throughput improvement over dense FP16 on supported hardware.

## Key Claims

- The 2:4 sparsity format stores each group of 4 elements as 2 non-zero values plus a 2-bit selector per non-zero value (4 bits total metadata per group), compressing weights to 50% of their original size with no runtime decompression overhead during matrix multiply.
- NVIDIA A100 Sparse Tensor Core throughput: 624 TFLOPS (FP16 with 2:4 sparsity) vs. 312 TFLOPS (FP16 dense) — exactly 2× as stated in the A100 datasheet; H100 SXM5 delivers 3,958 TFLOPS sparse FP8 vs. 1,979 TFLOPS dense FP8.
- Mishra et al. (2021) showed that a prune-then-fine-tune pipeline on BERT-Large achieves 90.9% F1 on SQuAD v1.1 with 2:4 sparsity, compared to 91.1% for the dense baseline — a degradation of only 0.2 points at 50% sparsity.
- GPT-2 (117 M parameters) pruned to 2:4 sparsity and fine-tuned for 10K steps recovers to within 0.5 perplexity points of its dense counterpart on WikiText-103, as reported in NVIDIA's Apex library benchmarks.
- The pruning criterion most commonly used to select which 2 of 4 weights to zero is magnitude-based (smallest absolute value zeroed), but activation-weighted magnitude (multiplying weight magnitude by the running mean absolute activation) reduces accuracy loss by an additional 0.3–0.7% on transformer models, as shown by Pool & Yu (2021).
- TensorRT supports automated 2:4 sparsity through its `sparsify_weights` API, which applies the pruning pattern and exports a sparse weight tensor compatible with cuSPARSELt for deployment without manual model surgery.
- The 2:4 constraint applies only to weight matrices, not activations; activation sparsity (ReLU zeros) is a separate phenomenon and is not exploited by Sparse Tensor Cores in the standard 2:4 path.

## Relationships

- [[nvidia_tensor_cores]] — Sparse Tensor Cores introduced in Ampere implement the 2:4 decode-and-skip mechanism; the 2:4 format was co-designed with the Tensor Core microarchitecture to guarantee 2× throughput.
- [[nvidia_hopper_h100]] — H100 inherits Sparse Tensor Core support and extends it to FP8 precision, making 2:4 sparsity composable with FP8 quantization for up to 4× over dense FP16.
- [[int8_fp8_quantization_llm_inference]] — Quantization and 2:4 sparsity are independently applicable and composable; the combination is the primary path to 4× inference throughput improvement on Ampere/Hopper without architectural changes.
- [[nvidia_ampere_a100]] — A100 is the first GPU to expose Sparse Tensor Core throughput to users; all subsequent NVIDIA data-center GPUs inherit the feature.

## Sources

- Mishra et al. (2021). "Accelerating Sparse Deep Neural Networks." NVIDIA Technical Report. https://arxiv.org/abs/2104.08378
- Pool, J. & Yu, C. (2021). "Channel Permutations for N:M Sparsity." NeurIPS 2021. https://arxiv.org/abs/2112.02086
- NVIDIA A100 Tensor Core GPU Architecture Whitepaper, 2020. https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet.pdf
- NVIDIA Developer Blog: "Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT." https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/
- Hubara et al. (2021). "Accelerated Sparse Neural Training: A Provable and Efficient Method to Find N:M Transposable Masks." https://arxiv.org/abs/2102.08124
