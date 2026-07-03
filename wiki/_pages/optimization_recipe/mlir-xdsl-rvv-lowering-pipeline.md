---
canonical_name: MLIR-xDSL RVV Lowering Pipeline
aliases:
- RISC-V Vector Code Generation in MLIR
- xDSL RVV lowerings
subtype: null
tags: []
hardware_targets:
- Kendryte K230
- BananaPi F3
workloads:
- gemm (General Matrix Multiplication)
datatypes:
- float32
metrics:
- GFLOPS
toolchains:
- MLIR
- xDSL
constraints: []
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/82f7fc54b588bd19.md
- https://arxiv.org/html/2603.17800
source_url: https://arxiv.org/html/2603.17800
fetched_at: '2026-07-02T10:15:07.433844+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 3
---

# MLIR-xDSL RVV Lowering Pipeline

This optimization recipe describes a compilation approach that combines MLIR with xDSL to enable RISC-V Vector (RVV) code generation from high-level abstractions. The transformation uses custom intermediate representations and passes in xDSL to systematically lower operations into hardware-aware C code invoking RVV intrinsics. Prerequisites include an MLIR distribution and the xDSL Python toolkit. Expected effect is portable generation of optimized micro-kernels for RVV targets without hand-tuned intrinsics. Failure modes may occur when RVV semantics or vector-length-agnostic programming are not properly modeled. The approach has been measured on gemm kernels on two RISC-V platforms, achieving performance improvements of 10–35% over OpenBLAS.

## Key Claims

- Combining MLIR with xDSL provides a practical pathway to portable, optimized code generation for RISC-V platforms.
- The approach generates specialized, hardware-aware C micro-kernels for General Matrix Multiplication (gemm) that invoke RVV intrinsics.
- On the Kendryte K230 and BananaPi F3, the generated kernels consistently outperform OpenBLAS, reaching up to 12.2 GFLOPS compared to the baseline's 5.1 GFLOPS, with improvements of 10–35% across evaluated workloads (square-matrix benchmarks and transformer-based workloads from BERT-Large).

## Transformation

- Prerequisites: MLIR framework (or compatible distribution), xDSL Python-native compiler toolkit, RISC-V toolchain with RVV intrinsic support.
- Steps: (1) Define custom dialects in xDSL that model RVV semantics and vector-length-aware transformations. (2) Implement lowering passes that map high-level MLIR operations (e.g., linalg.generic, scf.for) to the custom dialects. (3) Further lower to C code that directly invokes RVV intrinsics (e.g., vfmadd, vfmacc). (4) Emit the resulting micro-kernel as a standalone, portable C function that can be integrated into existing applications without modifying surrounding software stacks.
- Expected effect: Portable generation of optimized RVV kernels that outperform baseline implementations (e.g., OpenBLAS) by 10–35% on supported RISC-V platforms.
- Failure modes: Insufficient modeling of vector-length-agnostic behavior may lead to incorrect code. Missing intrinsic lowerings for specific RVV configurations could result in suboptimal performance or compilation errors. The approach is limited by the expressiveness of xDSL dialects and the completeness of the custom lowering passes.
- Measurements: Up to 12.2 GFLOPS (vs. 5.1 GFLOPS OpenBLAS) on gemm kernels; 10–35% performance improvement on square-matrix and transformer workloads derived from BERT-Large.

## Relationships

- [[xdsl]]: related via shared xdsl.

- [[kendryte-k230-neural-network-benchmarks]]: Related benchmark results for K230 covering different workloads (Resnet50, Mobilenet_v2, YoloV5S) on the KPU, providing additional performance context.
- Insufficient context for additional cross-links.

## Sources

- arXiv:2603.17800 (Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings)
