---
type: entity
tags: [compiler, IR, mlir, llvm, xla, tensorflow, jax, pytorch]
sources:
  - https://mlir.llvm.org/
  - https://arxiv.org/abs/2002.11054
  - https://iree.dev/
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

# MLIR / LLVM for AI

MLIR (Multi-Level Intermediate Representation) is a reusable compiler infrastructure project inside the LLVM umbrella, designed to express machine learning computations at multiple abstraction levels simultaneously. Introduced by Google in 2019 and open-sourced in 2020, MLIR solves the "N×M compiler problem" where N ML frameworks and M hardware targets each required bespoke translation layers. The central mechanism is the dialect system: each dialect is a self-contained IR namespace with custom operations, types, and lowering passes. Common AI-relevant dialects include `linalg` (named-axis tensor contractions), `affine` (polyhedral loop transforms), `vector` (SIMD abstraction), `tosa` (Tensor Operator Set Architecture for edge), `mhlo`/`stablehlo` (XLA's HLO as an MLIR dialect), and `nvgpu`/`amdgpu` for vendor-specific GPU instructions. A computation begins at a high-level dialect (e.g., `torch` or `tosa`) and is progressively lowered through a configurable pass pipeline to `llvm` dialect, then to LLVM IR, and finally to machine code or PTX. All major ML frameworks — TensorFlow (via XLA), JAX (via XLA), and PyTorch (via torch-mlir and TorchInductor) — now have MLIR-based compilation paths, making MLIR the de-facto common substrate for AI compiler research and production deployment.

## Key Claims

- MLIR was published by Lattner et al. (Google Brain / LLVM) in 2020 (arXiv:2002.11054) and upstreamed into the LLVM monorepo; it is now the primary IR used inside XLA, TensorFlow, JAX, and (partially) PyTorch compilation pipelines.
- The XLA HLO lowering pipeline was rewritten to use MLIR dialects (`mhlo` → `linalg` → `llvm`), enabling XLA to target CPUs, NVIDIA GPUs, AMD GPUs, and Google TPUs from a single IR without per-backend code duplication.
- torch-mlir is an open-source project that imports PyTorch's `torch.fx` graphs into MLIR's `torch` dialect, enabling hardware vendors (Arm, Qualcomm, AMD) to write MLIR backends rather than PyTorch-specific integrations.
- IREE (Intermediate Representation Execution Environment), developed by Google, uses MLIR to compile ML models for mobile and embedded targets (Android, iOS, bare-metal); it achieves within 10–30% of hand-optimized TFLite performance while supporting a broader model set.
- The `linalg` dialect's named-axis named-tensor operations enable polyhedral loop transformations (tiling, fusion, interchange) to be expressed as generic rewrite rules, replacing hand-written pattern matchers in legacy compilers.
- MLIR's progressive lowering model allows vendor-specific dialects (`nvgpu` for Hopper tensor memory accelerator, `amdgpu` for matrix core instructions) to be inserted at any level without modifying upstream dialects, enabling hardware vendors to contribute optimizations without forking the framework.

## Relationships

- [[openai_triton]] — Triton's compiler backend is implemented as an MLIR dialect (`triton`, `triton_gpu`) lowered through the MLIR pass pipeline to PTX.
- [[google_tpu]] — XLA, the primary compiler for Google TPUs, uses MLIR dialects (`mhlo`, `linalg`) in its lowering pipeline; Google contributed mhlo to the MLIR project.
- [[nvidia_hopper_h100]] — MLIR's `nvgpu` dialect exposes Hopper-specific instructions (wgmma, TMA) to higher-level dialects without requiring direct PTX intrinsic programming.
- [[onnx_tensorrt]] — TensorRT can ingest ONNX graphs that themselves may have been exported from MLIR-compiled frontends; MLIR-to-ONNX export paths exist in torch-mlir.
- [[intel_amx]] — Intel's AMX matrix extension is targeted from MLIR's `x86vector` and `amx` dialects, allowing JAX/TensorFlow kernels to emit AMX instructions.

## Sources

- Lattner, C. et al. "MLIR: Scaling Compiler Infrastructure for Domain Specific Computation." CGO 2021. https://arxiv.org/abs/2002.11054
- MLIR project documentation: https://mlir.llvm.org/
- torch-mlir project: https://github.com/llvm/torch-mlir
- IREE project: https://iree.dev/
- StableHLO (portable XLA dialect): https://github.com/openxla/stablehlo
