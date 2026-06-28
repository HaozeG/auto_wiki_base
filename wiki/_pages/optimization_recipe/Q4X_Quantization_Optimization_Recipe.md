---
cold_start: true
constraints:
- RISC-V Vector Extension (RVV)
- 8-core CPU
- L2 cache
- 32 scalable vector registers
created: '2025-03-04'
datatypes:
- int4 (codebook Q4X)
evidence_strength: measured
hardware_targets:
- Milk-V Jupiter (8-core RISC-V CPU with RVV)
inbound_links: 1
metrics:
- tokens per second
- perplexity
- model size
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://semiiphub.com/pulse/technical-articles/llm-inference-codebook-based-q4x-quantization-llama-cpp-framework-risc-v-vector-cpu
tags:
- Q4X
- quantization
- LLM
- RISC-V
- codebook
toolchains:
- Clang
- Llama.cpp
type: optimization_recipe
updated: '2026-06-28'
workloads:
- LLM inference (Llama 3.2 1B)
---

# Q4X Quantization Optimization Recipe
The Q4X quantization optimization recipe describes the codebook-based quantization technique designed for efficient LLM inference on RISC-V vector CPUs. The technique leverages a 64-element codebook stored in the CPU register file during dequantization, reducing far-memory accesses. It is integrated into the Llama.cpp framework through hardware-friendly data packing and cache-aware vectorized kernels optimized for the RISC-V Vector Extension (RVV). Measurements on a Milk-V Jupiter board with an 8-core RISC-V CPU show that Q4X (4.28 bits per weight) achieves better token throughput and model size compared to the built-in Q40 and Q4K methods, with a prefill throughput of 8.64 tokens/s and decode throughput of 5.29 tokens/s on Llama 3.2 1B.

## Key Claims

- Q4X uses a 64-element codebook learned from histograms of weight matrices; 4 histograms are reduced to 16 non-uniform samples each, forming 64 centroids.
- For each group of 64 weights, a 2-byte scale, a 2-bit codebook index, and 64 4-bit centroid indices are stored.
- Total BPW is 4.28 (with padding for byte alignment).
- The dequantization kernel is a vectorized dot product with data packing for maximum cache utilization and codebooks stored in vector registers.
- Baseline scalar kernel: 2.93 tokens/s (prefill) and 2.38 tokens/s (decode); optimized vectorized kernel: 8.64 and 5.29 tokens/s respectively.
- Compilation used Clang on an 8-core RISC-V CPU.

## Transformation

- Prerequisites: Target hardware with RISC-V Vector Extension (RVV) and at least 32 vector registers; Llama.cpp framework; Clang compiler; QuantX platform for codebook generation.
- Steps: (1) Generate Q4X codebook using histogram learning on weight matrices per layer. (2) Pack quantized weight matrices, codebooks, and scale factors to enhance spatial locality and cache-line alignment. (3) Implement dequantization kernel as vectorized dot product using RVV intrinsics, with codebook loaded into vector registers. (4) Integrate into Llama.cpp as a new quantization type.
- Expected effect: Improved token throughput and reduced model size compared to Q40 and Q4K, with minimal perplexity increase.
- Failure modes: Performance degradation if vector register file cannot hold all codebooks; increased perplexity if group size too large; lower throughput if data packing does not achieve cache hits.
- Measurements: Prefill throughput 8.64 tokens/s, decode throughput 5.29 tokens/s, perplexity 14.67, file size 702.38 MiB for Llama 3.2 1B.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – The dequantization kernel is similar in structure to vectorized GEMM kernels; both use RVV for performance.
- [[fpga-sdv_RISC-V_Vector_Cluster]] – Demonstrates the relevance of RISC-V vector capabilities for this optimization technique.

## Sources

- [Technical article: LLM Inference with Codebook-based Q4X Quantization using the Llama.cpp Framework on RISC-V Vector CPUs](https://semiiphub.com/pulse/technical-articles/llm-inference-codebook-based-q4x-quantization-llama-cpp-framework-risc-v-vector-cpu)

