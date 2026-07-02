---
canonical_name: LLM Inference RVV Optimization on BananaPi BPI-F3
aliases:
- BPI-F3 Gemma-2-2B RVV speedup
- BPI-F3 Llama-3.1-8B RVV speedup
- BananaPi BPI-F3 LLM inference with RVV
subtype: null
tags: []
hardware_targets:
- BananaPi BPI-F3
workloads:
- LLM inference (prefill and decode phases) on Gemma-2-2B and Llama-3.1-8B
datatypes:
- fp16
metrics:
- speedup (prefill)
- speedup (decode)
toolchains:
- llama.cpp (optimized with RVV instructions and zvfh extension)
hardware_versions:
- BananaPi BPI-F3 (RISC-V platform with RVV 1.0 and zvfh half-precision extension)
software_versions:
- llama.cpp (unreleased optimization from ICIC 2025 paper)
measurement_method: Runtime profiling on BananaPi BPI-F3; prefill prompt processing
  and token generation decode phases measured separately.
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/cacf8ab28479ed85.md
- https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
source_url: https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
fetched_at: '2026-07-02T04:17:55.665890+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# LLM Inference RVV Optimization on BananaPi BPI-F3

The BananaPi BPI-F3 platform, a RISC-V single-board computer supporting the Vector Extension (RVV 1.0) and the zvfh half-precision floating-point extension, was used to evaluate the effectiveness of operator-level RVV optimizations in the llama.cpp framework. The benchmark measured prefill and decode phases for two large language models: Gemma-2-2B (2 billion parameters) and Llama-3.1-8B (8 billion parameters). The optimization targeted critical operators—f16 vector dot product and layer normalization—by implementing them with RVV SIMD instructions. The reported results include a 1.7× speedup in prefill prompt processing and a 53% acceleration in token generation (decoding) for Gemma-2-2B, and a 36% improvement in prefill and 19% improvement in decode for Llama-3.1-8B. These figures come from a peer-reviewed conference paper (ICIC 2025) and represent reported (not independently measured) outcomes.

## Key Claims

- Gemma-2-2B prefill speedup: 1.7× compared to baseline llama.cpp.
- Gemma-2-2B decode speedup: 53% improvement in token generation.
- Llama-3.1-8B prefill speedup: 36% improvement.
- Llama-3.1-8B decode speedup: 19% improvement.
- Optimization achieved by reimplementing f16 vector dot product and layer normalization with RVV instructions and zvfh half-precision support.

## Measurement Context

- Hardware version: BananaPi BPI-F3 (RISC-V, RVV 1.0, zvfh extension)
- Software/toolchain version: llama.cpp (optimized version per ICIC 2025 paper)
- Workload shape: full GEMM-heavy prefill and autoregressive decode for Gemma-2-2B and Llama-3.1-8B
- Metric: speedup (ratio of baseline runtime to optimized runtime) for both prefill and decode phases
- Method: Experimental profiling on the actual hardware, as described in the paper
- Evidence strength: reported

## Relationships

- The BananaPi BPI-F3 platform is a RISC-V edge device comparable to other AIoT SoCs such as [[k230]] and [[allwinner_v853]], though it differs in detailed architecture and NPU capabilities.
- The optimization recipe itself is detailed in [[rvv_llama.cpp_optimization_recipe]], which documents the f16 dot-product and layer-normalization RVV rewrites that produced these speedups.

## Sources

- https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
