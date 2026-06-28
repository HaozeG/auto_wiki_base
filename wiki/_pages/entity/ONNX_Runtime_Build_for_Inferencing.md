---
cold_start: true
created: '2025-07-10'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.5
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://onnxruntime.ai/docs/build/inferencing.html
tags:
- ONNX Runtime
- inference
- build
- cross-compilation
- RISC-V
type: entity
updated: '2026-06-28'
---

# ONNX Runtime (Build for Inferencing)

ONNX Runtime is a cross-platform inference engine for machine learning models developed by Microsoft. It supports a wide range of hardware architectures including x86_64, ARM32v7, ARM64, PPC64LE, RISCV64, and more, with build instructions for Windows, Linux, macOS, AIX, and embedded platforms. For RISC-V, ONNX Runtime can be cross-compiled on Linux using the provided build script and cmake configuration. The build process requires Python 3.10+, cmake 3.28+, and a supported compiler such as GCC 8+ or Clang. The inference engine supports both CPU and GPU backends, with shared library and training options available via build flags. This page documents the build steps for inferencing, with a focus on RISC-V cross-compilation.

## Key Claims

- ONNX Runtime supports inference on x86_32, x86_64, ARM32v7, ARM64, PPC64LE, RISCV64, PPC64BE, and S390X architectures.
- Supported host operating systems include Windows 10, Ubuntu 20.x/22.x, CentOS 7/8/9, macOS, and AIX 7.2+.
- Build prerequisites: Python 3.10+, cmake 3.28+, git, and a compatible compiler (GCC 8+ or Clang).
- Windows builds use `.\build.bat` with Visual Studio 2022; Linux and macOS use `./build.sh`.
- RISC-V cross-compilation on Linux is possible using the build script with appropriate toolchain settings.
- Default build configuration is RelWithDebInfo; other valid values are Release, Debug, and MinSizeRel.
- Unit tests run by default for native builds and are skipped for cross-compiled builds.
- Parallel building is strongly recommended with the `--parallel` flag.
- Minimum target OS versions: Windows 10, macOS 13.3, CentOS 7, and Ubuntu 16.04.

## Relationships

- [[HAL_riscv_rvv_OpenCV_Optimization_Recipe]] \- Another open-source library (OpenCV) with RVV optimization for RISC-V, similar in that both provide accelerated inference/processing on RISC-V platforms.
- [[Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark]] \- A benchmark of LLM inference on a RISC-V board, demonstrating a use case for ONNX Runtime as an inference engine.

## Sources

- [Build for inferencing | onnxruntime](https://onnxruntime.ai/docs/build/inferencing.html)

