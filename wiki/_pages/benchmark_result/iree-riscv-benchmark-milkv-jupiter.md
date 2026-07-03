---
canonical_name: IREE RISC-V Microkernel Benchmark on MILK-V Jupiter
aliases:
- 10x-IREE Llama-3.2-1B Benchmark
- IREE RISC-V Llama Benchmark on MILK-V Jupiter
subtype: null
tags: []
hardware_targets:
- MILK-V Jupiter
workloads:
- LLM (Llama-3.2-1B-Instruct)
datatypes:
- f16
- f32
metrics:
- tokens per second
- accuracy
toolchains:
- IREE (10x-IREE)
- LM-Evaluation-Harness
- llama.cpp (for comparison)
hardware_versions:
- 1.66GHz × 8 RISC-V vector cores, RVV 1.0, VLEN=256, RVA22 profile
software_versions:
- IREE (10x-IREE, version not specified)
- llama.cpp (version not specified)
measurement_method: Evaluated Llama-3.2-1B-Instruct model compiled with 10x-IREE (IREE
  with RISC-V microkernels) on MILK-V Jupiter; recorded tokens per second for prefill
  and decode phases under single-threaded and 8-thread configurations. Accuracy verified
  against HuggingFace reference using LM-Evaluation-Harness on ARC_c and GPQA benchmarks.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/bfa9d98ae6a1aa49.md
- https://arxiv.org/html/2508.14899v1
source_url: https://arxiv.org/html/2508.14899v1
fetched_at: '2026-07-03T15:26:45.626424+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: iree-riscv-microkernel-support
  reason: This benchmark evaluates the optimization recipe described on that page,
    providing the measured performance results
- target: mlir-xdsl-gemm-benchmark-k230-banana-pi
  reason: Both benchmarks evaluate RISC-V AI inference performance, but this benchmark
    uses IREE with microkernels on MILK-V Jupiter for LLM inference, while the MLIR-xDSL
    benchmark uses a compiler-generated GEMM pipeline on K230 and BananaPi F3 for
    transformer-based workloads
---

# IREE RISC-V Microkernel Benchmark on MILK-V Jupiter

The IREE RISC-V Microkernel Benchmark on MILK-V Jupiter evaluates the performance of the Llama-3.2-1B-Instruct large language model compiled with the 10x-IREE framework (IREE with added RISC-V microkernels) on a MILK-V Jupiter single-board computer featuring eight 1.66 GHz RISC-V vector cores with RVV 1.0, VLEN=256, and the RVA22 profile. The benchmark measures tokens per second for prefill and decode phases under single-threaded and multi-threaded (8-thread) configurations. Accuracy is verified against the HuggingFace reference using LM-Evaluation-Harness on ARC_c and GPQA benchmarks. The results show that 10x-IREE achieves up to 50x single-threaded decode improvement and 17x multi-threaded decode improvement over upstream IREE, with prefill gains of 2x (8-thread). Compared to llama.cpp, 10x-IREE also shows substantial advantages in both prefill and decode phases.

## Key Claims

- Llama-3.2-1B-Instruct on MILK-V Jupiter with 10x-IREE achieves:
  - Prefill single-threaded: 0.18 tokens/s (vs IREE 0.14, llama.cpp 0.04)
  - Prefill 8-thread: 1.89 tokens/s (vs IREE 0.91, llama.cpp 0.11)
  - Decode single-threaded: 0.99 tokens/s (vs IREE 0.02, llama.cpp 0.03)
  - Decode 8-thread: 2.12 tokens/s (vs IREE 0.12, llama.cpp 0.07)
- 10x-IREE matches HuggingFace reference accuracy exactly (ARC_c: 59.4%, GPQA: 27.2%)
- Performance gains over upstream IREE: 50x decode single-thread, 17x decode multi-thread, 2x prefill multi-thread.
- Performance gains over llama.cpp: significant across all configurations (e.g., 33x decode single-thread, 30x decode multi-thread).

## Measurement Context

- Hardware version: MILK-V Jupiter with 1.66 GHz × 8 RISC-V vector cores, RVV 1.0, VLEN=256, RVA22 profile.
- Software/toolchain version: 10x-IREE (version not specified), llama.cpp (version not specified), LM-Evaluation-Harness (version not specified).
- Workload shape: Llama-3.2-1B-Instruct model, prefill and decode phases.
- Metric: tokens per second (throughput) and accuracy (ARC_c, GPQA).
- Method: Models were compiled and run on the target hardware; throughput measured during inference; accuracy evaluated using the LM-Evaluation-Harness framework.
- Evidence strength: measured (results are reported from experimental evaluation by the authors).

## Relationships

- [[iree-riscv-microkernel-support]]: This benchmark evaluates the optimization recipe described on that page, providing the measured performance results.
- [[mlir-xdsl-gemm-benchmark-k230-banana-pi]]: Both benchmarks evaluate RISC-V AI inference performance, but this benchmark uses IREE with microkernels on MILK-V Jupiter for LLM inference, while the MLIR-xDSL benchmark uses a compiler-generated GEMM pipeline on K230 and BananaPi F3 for transformer-based workloads.

## Sources

- https://arxiv.org/html/2508.14899v1
