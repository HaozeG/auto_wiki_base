---
canonical_name: XuanTie C908 AI Inference Performance
aliases:
- C908 AI benchmarks
- C908 inference speedup
subtype: null
tags:
- XuanTie C908
- AI inference
- HHB
- SHL
- MobileNet
- int8 quantization
- RVV
hardware_targets:
- XuanTie C908 (VLEN128)
- XuanTie C908 (VLEN256)
workloads:
- mobilenettoolchains: null
- HHB
- SHL
datatypes:
- int8
- fp16
metrics:
- speedup factor: 3.35x (with int8 dot product)
- speedup factor: 1.55-1.68x (VLEN128 to VLEN256)
- speedup factor: 3.75-4.57x (vs XuanTie C906)
hardware_versions:
- XuanTie C908 with VLEN128
- XuanTie C908 with VLEN256
software_versions:
- HHB with int8_asym_w_sym quantization
- SHL
measurement_method: AI inference performance tested on common CNN models (MobileNet
  specified) using HHB and SHL. Performance improvements calculated relative to baseline
  (no int8 dot product extension) and relative to XuanTie C906.
evidence_strength: reported
scorecard:
  novelty_delta: 0.6
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
source_url: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
fetched_at: '2026-07-02T06:17:44.111323+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# XuanTie C908 AI Inference Performance

This page summarizes the AI inference benchmark results reported for the XuanTie C908 processor using the HHB and SHL software stack. The benchmarks measure the relative performance improvement from the int8 vector dot product extension (3.35× on MobileNet), the speedup from expanding vector length from 128 to 256 bits (1.55–1.68×), and the overall improvement over the predecessor XuanTie C906 (3.75–4.57×). The results are based on tests conducted by T-Head and published in a RISC-V International blog post. Measurements use the MobileNet CNN model with int8 quantization and the SHL high-performance inference library. These results highlight the effectiveness of combining RISC-V vector extensions with software optimization for edge AI.

## Key Claims

- Adding INT8 vector dot product instructions improves XuanTie C908 inference performance on MobileNet by 3.35× (C908 VLEN128 compared to C908 without dot product extension).
- Increasing vector length from 128 to 256 bits yields an additional speedup factor of 1.55–1.68×.
- The XuanTie C908 at VLEN128 delivers 3.75–4.57× the AI inference performance of the predecessor XuanTie C906.

## Measurement Context

- Hardware version: XuanTie C908 with VLEN128 configuration; XuanTie C908 with VLEN256 configuration; XuanTie C906 for comparison.
- Software/toolchain version: HHB (Heterogeneous Honey Badger) with int8 asymmetric weight-symmetric activation quantization; SHL (Structure of Heterogeneous Library) optimized operators.
- Workload shape: MobileNet CNN model (exact input dimensions not specified).
- Metric: Speedup factor (ratio of inference performance relative to baseline).
- Method: Inference performance tested using HHB-generated C code calling SHL optimized operators on the target hardware. Baseline uses the same setup without the int8 dot product extension. Comparative measurement against C906 is performed on the same workload.
- Evidence strength: reported (source: T-Head blog post, no independent verification).

## Relationships

- The benchmarked hardware target is [[xuantie_c908]], which supports the described optimizations.
- The SHL GEMM outer product kernel [[xuantie_c908_fp16_gemm_kernel]] is a key component enabling the convolution acceleration used in these benchmarks.
- The MLIR+xDSL code generation recipe [[mlir_xdsl_rvv_gemm_codegen_recipe]] demonstrates alternative optimization approaches for similar RISC-V vector hardware.
- Comparison baseline: [[xuantie_c906]] (performance improvement factor reported).

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
