---
canonical_name: BananaPi BPI-F3 LLM Inference (RVV optimized)
aliases:
- BPI-F3 RVV LLM benchmark
- Gemma-2-2B Llama-3.1-8B RVV BPI-F3
- BPI-F3 RVV llama.cpp
subtype: null
tags: []
hardware_targets:
- SpacemiT K1
workloads:
- LLM prefill (Gemma-2-2B)
- LLM decode (Gemma-2-2B)
- LLM prefill (Llama-3.1-8B)
- LLM decode (Llama-3.1-8B)
datatypes:
- FP16 (via zvfh)
metrics:
- speedup (prefill prompt processing)
- speedup (token generation)
toolchains:
- llama.cpp (RVV-optimized)
hardware_versions:
- BananaPi BPI-F3 (SpacemiT K1, RVV 1.0, zvfh extension, 16GB LPDDR4X-3200)
software_versions:
- Llama.cpp with RVV vector instructions (zvfh half-precision)
measurement_method: Profiling of prefill and decode phases on BPI-F3 board, comparing
  baseline unoptimized llama.cpp against RVV-optimized version
evidence_strength: measured
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.3
sources:
- raw/cache/cacf8ab28479ed85.md
- https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
source_url: https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
fetched_at: '2026-07-03T15:36:41.928584+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# BananaPi BPI-F3 LLM Inference (RVV optimized)

This benchmark result captures the measured speedups achieved by optimizing critical operators in the llama.cpp framework using RISC-V Vector Extension (RVV) instructions, specifically targeting half-precision floating-point via the Zvfh extension on the BananaPi BPI-F3 platform. The BPI-F3 is built around the SpacemiT K1 SoC, which provides an 8-core CPU with RVV 1.0, a VLEN of 256 bits, and 16 GB of LPDDR4X-3200 memory delivering approximately 25.6 GB/s of theoretical bandwidth. Runtime profiling identified the f16 vector dot product and layer normalization as performance bottlenecks; these operators were redesigned with RVV SIMD primitives to maximize parallel computation. The results, reported in a conference paper (ICIC 2025), show speedups on two LLMs: Gemma-2-2B and Llama-3.1-8B, measured during prefill prompt processing and token generation during decoding.

## Key Claims

- Gemma-2-2B prefill prompt processing achieves a 1.7x speedup over the unoptimized llama.cpp baseline on the BPI-F3.
- Gemma-2-2B token generation during decoding sees a 53% acceleration (1.53x speedup).
- Llama-3.1-8B prefill shows a 36% improvement (1.36x speedup).
- Llama-3.1-8B decode shows a 19% improvement (1.19x speedup).
- The optimizations leverage RVV 1.0 with the Zvfh extension for half-precision floating-point vector operations.

## Measurement Context

- Hardware version: BananaPi BPI-F3 (SpacemiT K1, 8-core X60, RVV 1.0 zve64d/f/x, VLEN=256, 16 GB LPDDR4X-3200, Linux 6.6.63)
- Software/toolchain version: llama.cpp with hand-tuned RVV instructions (Zvfh extension for FP16), glibc 2.39
- Workload shape: Full prompt processing and autoregressive decode for Gemma-2-2B and Llama-3.1-8B
- Metric: Speedup factor (ratio of optimized prefill/decode time over baseline unoptimized llama.cpp)
- Method: Profiling on physical BPI-F3 hardware; baseline and optimized variants compared under identical conditions
- Evidence strength: measured (reported in peer-reviewed conference paper)

## Relationships

- Shares the SpacemiT K1 hardware platform documented in [[spacemit-k1]] and provides the first LLM inference speedup measurements specifically optimizing llama.cpp with RVV Zvfh on that platform.

## Sources

- https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
