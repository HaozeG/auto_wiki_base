---
canonical_name: Q4X
aliases:
- Q4X quantization
- Codebook-based Q4X
subtype: null
tags:
- quantization
- codebook
- llama.cpp
- RVV
hardware_targets:
- MILK-V Jupiter
workloads:
- LLM inference
datatypes:
- Q4X (4-bit codebook)
metrics:
- latency
toolchains:
- llama.cpp
- QuantX
constraints:
- RISC-V vector extension (RVV) CPU
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/902250618af91597.md
- https://10xengineers.ai/llm-inference-with-codebook-based-q4x-quantization-using-the-llama-cpp-framework-on-risc-v-vector-cpus/
source_url: https://10xengineers.ai/llm-inference-with-codebook-based-q4x-quantization-using-the-llama-cpp-framework-on-risc-v-vector-cpus/
fetched_at: '2026-07-03T16:45:06.021616+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 1
---

# Q4X Quantization for LLM Inference on RISC‑V Vector CPUs

Q4X is a codebook-based quantization technique designed for efficient LLM inference on RISC‑V vector (RVV) CPUs. Developed using QuantX, a hardware-aware quantization platform, Q4X proposes a new 'Q4X' quantization strategy that improves upon built-in llama.cpp strategies such as Q40 and Q4K_S. The technique employs learned codebooks rather than fixed block sizes to achieve better accuracy-efficiency trade-offs. A custom dequantization kernel optimized for RVV was integrated into a private fork of the llama.cpp framework, and validation was performed on the Milk‑V Jupiter RISC‑V board. Prerequisites include a RVV-capable CPU (e.g., Milk‑V Jupiter) and access to the QuantX platform for codebook generation. The expected effect is reduced inference latency with minimal accuracy loss compared to Q40 or Q4K_S. Failure modes may include increased memory footprint from codebook storage if not carefully tuned. Measurements reported are qualitative; no numerical latency figures are provided in the source.

## Key Claims

- Q4X is a codebook-based quantization technique using learned codebooks (vs. fixed block sizes in Q40, Q4K_S).
- Designed for RVV CPUs and integrated into a private fork of llama.cpp via a custom dequantization kernel.
- Validated on the Milk‑V Jupiter RISC‑V board (RVV-capable platform).
- Aims to improve inference latency over existing llama.cpp quantization strategies while maintaining accuracy.

## Transformation

- Prerequisites:
  - RISC‑V vector (RVV) CPU (validated on Milk‑V Jupiter).
  - QuantX platform for generating CPU-friendly codebook quantization.
  - Private fork of llama.cpp with the Q4X integration.
- Steps:
  1. Use QuantX to produce a Q4X codebook for the target LLM and RVV hardware.
  2. Load the quantized model into the Q4X-enabled llama.cpp fork.
  3. The custom dequantization kernel runs on RVV, converting codebook indices on the fly during inference.
- Expected effect:
  - Reduced inference latency compared to built-in quantization strategies (Q40, Q4K_S) with minimal accuracy degradation.
- Failure modes:
  - Codebook storage may increase memory usage; may offset benefits on memory-constrained devices.
  - The private fork is not upstreamed to mainline llama.cpp, limiting reproducibility.
- Measurements:
  - No numeric benchmark results disclosed; only qualitative validation reported.

## Relationships

(This page is the first documentation of Q4X; no specific relationships to existing wiki pages are established from the source material. The technique has not been validated on documented hardware targets such as AndesCore AX45MPV, though RVV compatibility suggests potential applicability.)

## Sources

- https://10xengineers.ai/llm-inference-with-codebook-based-q4x-quantization-using-the-llama-cpp-framework-on-risc-v-vector-cpus/
