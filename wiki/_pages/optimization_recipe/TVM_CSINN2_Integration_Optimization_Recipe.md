---
cold_start: true
constraints:
- RISC-V Vector Extension v0.7.1/v1.0
- BYOC infrastructure
- CSourceModule
created: '2025-01-29'
datatypes:
- FP32
evidence_strength: reported
hardware_targets:
- XuanTie C906
inbound_links: 1
metrics: []
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://discuss.tvm.apache.org/t/pre-rfc-byoc-risc-v-csi-nn2-compute-library-integration/12610
tags:
- TVM
- CSI-NN2
- CSINN2
- BYOC
- RISC-V
- XuanTie C906
- vector extension
toolchains:
- TVM
- CMake
- QEMU
type: optimization_recipe
updated: '2026-06-29'
workloads:
- conv2d
- relu
- maxpool2d
- softmax
---

# TVM CSI-NN2 Integration Optimization Recipe

This optimization recipe describes the integration of the open-source CSI-NN2 Compute Library (CSINN2) into Apache TVM to accelerate inference on RISC-V CPUs with Vector Extension, specifically targeting the Alibaba T-Head XuanTie C906 processor. The integration uses TVM's Bring Your Own Codegen (BYOC) framework with CSourceModule to offload Relay operators to CSINN2 hand-crafted assembler routines, generating a model.c and model.params file that are compiled into a shared library. A runtime module loads the library and input/output buffers, enabling execution on both QEMU (for simulation) and real RISC-V devices. The initial implementation supports FP32 precision for operators including conv2d, relu, maxpool2d, and softmax, with approximately 50 operators implemented in total. No performance measurements are yet available as the integration is at the pre-RFC stage; testing is performed via QEMU simulation with random data and known network results.

## Key Claims

- CSI-NN2 provides hand-crafted assembler routines for RISC-V CPUs with vector extension, compatible with RISC-V v0.7.1 and v1.0 vector standards.
- The integration converts Relay operators to CSINN2 calls via BYOC infrastructure, generating model.c (layer attributions and graph representation) and model.params (constant tensors and quantization info).
- Approximately 50 operators are implemented, including FP32/FP16/quantized; initial supported operators are conv2d, relu, maxpool2d, and softmax.
- Build system support is provided via a CMake option (USE_CSINN2) and a Docker script (docker/ubuntu_install_csinn2.sh) for cross-compilation.
- Testing uses QEMU simulation on x86, with end-to-end network tests (MobileNetV1) and unit tests for individual operators.
- Future improvements include wider FP32/FP16 operator support and quantized operator support.

## Transformation

- Prerequisites: TVM with BYOC support, CMake, QEMU user-mode emulator for RISC-V, cross-compilation toolchain for RISC-V vector extension.
- Steps:
  1. Enable CSINN2 support in TVM build with `USE_CSINN2=ON`.
  2. Run the provided Docker script to install CSINN2 cross-compiled for RISC-V.
  3. Compile a Relay graph using the CSINN2 codegen: the graph is pre-processed with passes like FoldConstant, then operators are checked for CSINN2 support and converted to CSINN2 graph representation, outputting model.c and model.params.
  4. Compile model.c into model.so using the RISC-V cross-compiler.
  5. At runtime, load model.so and model.params, supply input/output buffers, and execute inference.
- Expected effect: Faster inference on RISC-V CPUs with vector extension by leveraging hand-crafted assembly routines in CSINN2, compared to generic TVM code generation.
- Failure modes: Not documented; relies on correct cross-compilation setup and operator coverage. Operators not supported by CSINN2 must fall back to TVM.
- Measurements: None reported; the RFC is a pre-RFC proposal.

## Relationships

- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – Benchmark results from another TVM integration with a RISC-V hardware accelerator (Gemmini), providing a comparison for TVM-based acceleration on RISC-V.
- [[MilkV_Pioneer]] – A RISC-V workstation with vector extensions (RVV) similar to the XuanTie C906 target; this recipe's techniques are potentially applicable to MilkV Pioneer.

## Sources

- [pre-RFC: BYOC RISC-V CSI-NN2 Compute Library integration – Apache TVM Discuss](https://discuss.tvm.apache.org/t/pre-rfc-byoc-risc-v-csi-nn2-compute-library-integration/12610)
