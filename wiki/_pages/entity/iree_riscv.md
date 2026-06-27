---
type: entity
tags: [risc-v, mlir, compiler-runtime, google, ml-deployment, software-stack]
sources:
  - https://arxiv.org/abs/2508.14899
  - https://arxiv.org/html/2405.15380v1
  - https://iree.dev/building-from-source/riscv/
  - https://github.com/iree-org/iree
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# IREE Runtime on RISC-V

IREE (Intermediate Representation Execution Environment) is a retargetable MLIR-based machine learning compiler and runtime toolkit originally developed by Google, now maintained as an open-source project. On RISC-V, IREE compiles ML models (from TensorFlow, JAX, PyTorch via torch-mlir) into hardware-specific executables by lowering through MLIR's Linalg dialect to RVV intrinsics. IREE on RISC-V is significant because it provides the only fully end-to-end open-source ML deployment pipeline from framework-level model to bare-metal or Linux-based RISC-V execution, without requiring proprietary vendor SDKs.

## Key Claims

- IREE supports RISC-V 64-bit Linux cross-compilation and bare-metal deployment targets, with QEMU-based emulation for testing without physical hardware.
- As of 2024, IREE lacked optimized microkernels for RISC-V despite having them for x86 and ARM (NEON/SVE), causing poor GenAI model performance on RISC-V platforms.
- A 2025 paper (arXiv:2508.14899) added RISC-V microkernel support by lowering linalg.mmt4d operations for RV64 targets within the IREE pass pipeline, directly improving transformer and GenAI workload throughput.
- IREE's compilation path for RISC-V: model → MLIR Linalg → linalg.mmt4d → RVV microkernels → RISC-V binary; this is the same lowering strategy used for ARM NEON/SVE microkernels.
- Google's Coral NPU (a unified open ML hardware platform) uses IREE as its primary compiler stack, with RISC-V as the host control core.
- TinyIREE (arXiv:2205.14479) demonstrated IREE targeting embedded RISC-V bare-metal systems, achieving ML inference on microcontroller-class hardware.
- A 2024 full-stack evaluation (arXiv:2405.15380) benchmarked IREE against TVM and other runtimes on RISC-V systems, finding that kernel optimization (not compiler IR quality) is the dominant performance factor.

## Relationships

- [[mlir_riscv_backend]]: IREE relies on MLIR's vector dialect and LLVM RISC-V backend as its core compilation infrastructure.
- [[tvm_riscv_backend]]: TVM and IREE are the two primary open-source ML compilers with RISC-V support; 2024 benchmarks show performance parity after kernel tuning.
- [[risc_v_vector_extension]]: IREE generates RVV 1.0 code; performance is contingent on hardware VLEN and LMUL configuration matching compiler assumptions.
- [[gemmini]]: IREE targets software-defined vector pipelines; Gemmini is a hardware-defined systolic alternative within the same Chipyard ecosystem.

## Sources

- RISC-V microkernel paper: arXiv:2508.14899
- Full-stack evaluation: arXiv:2405.15380
- IREE RISC-V cross-compilation docs: https://iree.dev/building-from-source/riscv/
- GitHub: https://github.com/iree-org/iree
