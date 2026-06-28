---
cold_start: true
created: '2025-03-04'
datatypes:
- int4 (codebook Q4X)
evidence_strength: measured
hardware_targets:
- Milk-V Jupiter (8-core RISC-V CPU)
hardware_versions:
- Milk-V Jupiter board
inbound_links: 4
measurement_method: Benchmark conducted on Milk-V Jupiter board with 8-core RISC-V
  CPU, using Clang compiler. Tokens per second measured for prefill and decode phases.
  Perplexity computed on Wikitext v2 test subset with context length 2048.
metrics:
- tokens per second (prefill)
- tokens per second (decode)
- perplexity
- file size
- bits per weight (BPW)
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- Llama.cpp (private fork with Q4X)
- Llama 3.2 1B
- Wikitext v2 test subset
- nctx=2048
sources:
- https://semiiphub.com/pulse/technical-articles/llm-inference-codebook-based-q4x-quantization-llama-cpp-framework-risc-v-vector-cpu
tags:
- Q4X
- quantization
- LLM
- RISC-V
- Milk-V Jupiter
toolchains:
- Clang
type: benchmark_result
updated: '2026-06-28'
workloads:
- LLM inference (Llama 3.2 1B)
---

# Q4X Quantization LLM Inference Milk-V Jupiter Benchmark

The Q4X Quantization LLM Inference Milk-V Jupiter Benchmark documents measured performance of the codebook-based Q4X quantization technique integrated into a private fork of the Llama.cpp framework and evaluated on a Milk-V Jupiter RISC-V board with an 8-core CPU. Measurements were collected for the Llama 3.2 1B instruction-tuned model using the Wikitext v2 test subset with a context length of 2048 tokens. The benchmark compares Q4X against the built-in Llama.cpp quantization methods Q40 and Q4K across metrics including tokens per second (prefill and decode), perplexity, and model file size. All tests used the Clang compiler. The Q4X method achieves a bits-per-weight (BPW) of 4.28, and delivers prefill throughput of 8.64 tokens/s and decode throughput of 5.29 tokens/s with a perplexity of 14.67, outperforming Q40 in throughput and model size, and matching Q4K in throughput with a reduced file size.

## Key Claims

- Q4X achieves 4.28 BPW, 702.38 MiB file size for Llama 3.2 1B quantized model.
- Q4X prefill throughput: 8.64 tokens/s (vs Q40 6.03, Q4K 7.77).
- Q4X decode throughput: 5.29 tokens/s (vs Q40 4.28, Q4K 5.06).
- Q4X perplexity on Wikitext v2: 14.67 (vs Q40 15.22, Q4K 14.45).
- Baseline FP16 model: 16 BPW, ~2300 MiB, prefill 0.12 tokens/s, decode 0.06 tokens/s, perplexity 13.16.
- Q4X outperforms Q40 on all three metrics (throughput, file size, perplexity).
- Q4X has better file size and decode throughput than Q4K, but Q4K achieves lower perplexity due to two-level scaling and smaller subgroup size.

## Measurement Context

- Hardware version: Milk-V Jupiter board (8-core RISC-V CPU).
- Software/toolchain version: Clang compiler; private fork of Llama.cpp with Q4X integration; Llama 3.2 1B instruction-tuned model.
- Workload shape: LLM inference on Wikitext v2 test subset, context length (nctx) = 2048.
- Metric: tokens per second (prefill and decode), perplexity, file size (MiB), bits per weight (BPW).
- Method: Models quantized and run on the board; tok/s measured for prefill and decode phases; perplexity computed using Wikitext v2 without training interference.
- Evidence strength: measured.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – Both involve RISC-V vector kernels; the Q4X dequantization kernel is a vectorized dot product similar in nature.
- [[fpga-sdv_RISC-V_Vector_Cluster]] – Another RISC-V vector platform where similar vectorized performance could be evaluated.

## Sources

- [Technical article: LLM Inference with Codebook-based Q4X Quantization using the Llama.cpp Framework on RISC-V Vector CPUs](https://semiiphub.com/pulse/technical-articles/llm-inference-codebook-based-q4x-quantization-llama-cpp-framework-risc-v-vector-cpu)

