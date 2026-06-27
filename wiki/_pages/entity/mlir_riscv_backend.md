---
cold_start: true
created: 2026-06-27
inbound_links: 6
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/02-Zhang-RISC-V-VectorExtensionSupport-in-MLIR.pdf
- https://discourse.llvm.org/t/rfc-add-risc-v-vector-extension-rvv-dialect/4146
- https://arxiv.org/html/2603.17800v1
- https://llvm.org/docs/RISCV/RISCVVectorExtension.html
tags:
- mlir
- risc-v
- compiler
- rvv
- llvm
- software-stack
type: entity
updated: 2026-06-27
---

# MLIR RISC-V Backend

The MLIR (Multi-Level Intermediate Representation) RISC-V backend is the compilation infrastructure within the LLVM/MLIR project that lowers ML and linear algebra computations to RISC-V Vector Extension (RVV) code. MLIR provides a dialect-based progressive lowering pipeline: high-level models expressed in Linalg or tensor dialects are converted through the vector dialect and ultimately to LLVM IR, from which the LLVM RISC-V backend generates RVV-intrinsic machine code. This infrastructure allows ML frameworks like TensorFlow, PyTorch, and IREE to target RISC-V vector hardware without custom per-framework backend work.

## Key Claims

- MLIR implements a dedicated RVV dialect with operations, scalable vector types, RVV intrinsic wrappers, and conversion passes from RVV dialect → LLVM dialect → LLVM IR.
- The standard lowering path for ML operators is: Linalg dialect → vector dialect → LLVM dialect → RISC-V backend with RVV intrinsics; each step is a separate, composable MLIR pass.
- LLVM RISC-V backend supports RVV 1.0 (ratified), modeling scalable vector types (`<vscale x N x T>`) that abstract over hardware-defined VLEN at compile time.
- A 2023 proposal (RFC) to add an explicit RISC-V Vector dialect was accepted; the dialect bridges generic MLIR vector ops and RVV-specific semantics (mask handling, vl/vtype configuration).
- A 2025 paper (arXiv:2603.17800) demonstrates generating portable C code with native RVV 1.0 intrinsics via MLIR's emitc dialect, enabling deployment on systems without full LLVM toolchain availability.
- Hardware-per-target vector operations are implemented as one dialect per target (RVV, ARM SVE, x86 AVX-512), enabling shared middle-end optimization passes across all vector ISAs.
- MLIR's auto-vectorization for RISC-V relies on the same loop-vectorizer infrastructure as LLVM, extended with scalable-vector (SVE/RVV) support added to GCC 14 and LLVM 17+.

## Relationships

- [[risc_v_vector_extension]]: MLIR backend generates RVV 1.0 intrinsics; correctness depends on accurate VLEN/LMUL modeling in the compiler.
- [[iree_riscv]]: IREE uses MLIR's Linalg-to-LLVM lowering pipeline as its primary compilation path for RISC-V targets.
- [[tvm_riscv_backend]]: TVM and MLIR/IREE represent competing ML compilation stacks for RISC-V; MLIR focuses on progressive lowering while TVM uses a tensor expression language.
- [[ara_vector_processor]]: Ara and Ara2 are primary open-source hardware targets for validating MLIR RVV code generation.

## Sources

- LLVM Dev Meeting 2023 slides: https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/02-Zhang-RISC-V-VectorExtensionSupport-in-MLIR.pdf
- LLVM Discourse RFC: https://discourse.llvm.org/t/rfc-add-risc-v-vector-extension-rvv-dialect/4146
- xDSL/emitc paper: arXiv:2603.17800
- LLVM RVV docs: https://llvm.org/docs/RISCV/RISCVVectorExtension.html
