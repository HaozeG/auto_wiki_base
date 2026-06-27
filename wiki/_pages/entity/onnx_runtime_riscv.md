---
type: entity
tags: [risc-v, ONNX, ML-runtime, inference, software-stack, benchmark]
sources:
  - https://github.com/ucb-bar/onnxruntime-riscv
  - https://arxiv.org/html/2504.03774v1
  - https://onnxruntime.ai/docs/reference/compatibility.html
  - https://openbenchmarking.org/test/pts/onnx
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

# ONNX Runtime RISC-V Backend

ONNX Runtime (ORT) is Microsoft's cross-platform ML inference engine for executing ONNX-format models; its RISC-V support is community-driven and consists of two tracks: an upstream track in the main onnxruntime repository and a specialized UC Berkeley fork. The upstream ORT gained initial RISC-V RV64 build support (--rv64, --riscv_toolchain_root, --riscv_qemu_path build flags) and subsequently added RISC-V Vector (RVV) acceleration for the CPU Execution Provider (CPU EP). The UCB fork (github.com/ucb-bar/onnxruntime-riscv) is specifically adapted for RISC-V accelerator research, providing integration hooks for Gemmini-class attached accelerators. A 2024–2025 benchmark study on the 64-core SOPHON SG2042 RISC-V server CPU compared PyTorch, ONNX Runtime, and TensorFlow energy consumption: ORT (using the XNNPACK backend) was among the most energy-efficient frameworks on RISC-V, outperforming PyTorch compiled with OpenBLAS in energy per inference. ONNX Runtime version 1.24.1 benchmark data was published in February 2026. Supported operations via CPU EP on RISC-V cover the standard ONNX opset for dense linear algebra (GEMM, Conv, ReLU, etc.); RVV-accelerated paths depend on XNNPACK or custom microkernel backends rather than native ORT kernel implementations.

## Key Claims

- Upstream ONNX Runtime added RISC-V RV64 build support with --rv64 and QEMU integration flags.
- RVV (RISC-V Vector) acceleration added to ORT CPU Execution Provider for RISC-V targets.
- UC Berkeley maintains a specialized onnxruntime-riscv fork for Gemmini-class accelerator integration.
- On SOPHON SG2042 (64-core RV64), ORT with XNNPACK backend is more energy-efficient than PyTorch+OpenBLAS.
- ORT version 1.24.1 benchmark data published February 2026.
- Supported ONNX ops on RISC-V CPU EP cover standard opset (GEMM, Conv, activation functions).

## Relationships

- [[gemmini]]: UCB onnxruntime-riscv fork integrates with Gemmini as an attached accelerator backend.
- [[iree_riscv]]: IREE and ONNX Runtime are competing ML runtimes targeting RISC-V; IREE uses MLIR, ORT uses XNNPACK/custom kernels.
- [[tvm_riscv_backend]]: TVM and ONNX Runtime occupy overlapping space for RISC-V model deployment; TVM offers more compiler optimization.
- [[risc_v_vector_extension]]: ORT's RVV-accelerated CPU EP depends on RVV 1.0 hardware for performance gains.

## Sources

- https://github.com/ucb-bar/onnxruntime-riscv
- https://arxiv.org/html/2504.03774v1
- https://onnxruntime.ai/docs/reference/compatibility.html
