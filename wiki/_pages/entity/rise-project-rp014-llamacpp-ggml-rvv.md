---
canonical_name: RP014 - Optimizing Llama.cpp and GGML for RVV
aliases:
- RP014
- Project RP014
- Llama.cpp GGML RVV Optimization
- RISE RP014
subtype: null
tags:
- llama.cpp
- GGML
- RVV
- RISC-V
- quantization
- optimization
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.6
sources:
- raw/cache/d3ef38e3fe1fb8b8.md
- https://lf-rise.atlassian.net/wiki/spaces/HOME/pages/628817924/Project+RP014+Optimizing+Llama.cpp+and+GGML+for+RVV
source_url: https://lf-rise.atlassian.net/wiki/spaces/HOME/pages/628817924/Project+RP014+Optimizing+Llama.cpp+and+GGML+for+RVV
fetched_at: '2026-07-03T15:35:38.731344+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: Both RP014 and the MLIR-xDSL RVV Code Generation Pipeline target RVV 1.0
    for performance acceleration, but RP014 focuses on hand-optimized kernel implementations
    within the GGML framework, while the MLIR-xDSL pipeline uses compiler-generated
    code for GEMM. The two approaches represent complementary strategies for achieving
    RVV performance on RISC-V platforms
- target: mlir-xdsl-gemm-benchmark-k230-banana-pi
  reason: Benchmarks on the BananaPi F3 from the MLIR-xDSL pipeline establish a performance
    baseline (up to 12.2 GFLOPS for GEMM) that RP014's optimized GGML kernels may
    later be compared against, as both use the same BPI-F3 hardware
---

# RP014 - Optimizing Llama.cpp and GGML for RVV

RISE Project RP014 is a request for proposals (RFP) initiated by the RISE consortium to bring RISC-V Vector (RVV) support within the Llama.cpp and GGML ecosystem on par with established architectures such as x86 and ARM. The project focuses on comprehensive support for the RVV 1.0 extension with optimized VLEN-agnostic implementations, targeting the BananaPi BPI-F3 board. It aims to address identified gaps including incomplete 128-bit RVV support across diverse quantization types and the absence of mature VLEN-agnostic support for wider vector hardware. The scope covers quantization/dequantization kernels, vector dot products, GEMV, GEMM, activation functions, and utilities. Contractors are required to use only ratified RISC-V extensions and to upstream contributions to the Llama.cpp community.

## Key Claims

- Current RVV support in Llama.cpp/GGML is incremental and kernel-specific, primarily focused on 128-bit VLEN for a subset of quantization kernels.
- Key gaps identified: incomplete 128-bit RVV support across quantization types (Q2_K, Q3_K, Q5_K, Q6_K, Q8_0, FP16, FP32) and absence of mature VLEN-agnostic support for VLEN >128-bit.
- The scope includes implementing VLEN-agnostic RVV versions for performance-critical GGML functions, extending work from PR #12530 and PR #13892.
- A dynamic dispatch mechanism (similar to ifunc in glibc) based on the hardware VLEN is planned to select optimized intrinsics for specific VLEN values.
- Target hardware is the BananaPi BPI-F3 board; only ratified RVA23 mandatory extensions may be used (no AME/IME).
- Functional testing will use QEMU syscall-emulation with multiple VLEN configurations (128, 256, 512, 1024).
- Success criteria include demonstrating performance improvements on TinyLlama and BERT-Large-uncased models with FP32, FP16, INT8, and Q4_K_M datatypes on the BPI-F3.
- Deliverables include a benchmarking and test harness as open source software, integrated into mainline Llama.cpp.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: Both RP014 and the MLIR-xDSL RVV Code Generation Pipeline target RVV 1.0 for performance acceleration, but RP014 focuses on hand-optimized kernel implementations within the GGML framework, while the MLIR-xDSL pipeline uses compiler-generated code for GEMM. The two approaches represent complementary strategies for achieving RVV performance on RISC-V platforms.
- [[mlir-xdsl-gemm-benchmark-k230-banana-pi]]: Benchmarks on the BananaPi F3 from the MLIR-xDSL pipeline establish a performance baseline (up to 12.2 GFLOPS for GEMM) that RP014's optimized GGML kernels may later be compared against, as both use the same BPI-F3 hardware.

## Sources

- https://lf-rise.atlassian.net/wiki/spaces/HOME/pages/628817924/Project+RP014+Optimizing+Llama.cpp+and+GGML+for+RVV
