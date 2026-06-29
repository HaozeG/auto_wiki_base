---
cold_start: true
constraints:
- fixed-function accelerator
- supports convolution, deconvolution, fully connected, activation, pooling, batch
  normalization
- first-generation DLA (Xavier), second-generation DLA (Orin)
- up to two DLAs per SoC
- offline compilation through TensorRT
- GPU fallback supported
- INT8 and FP16 support
created: '2025-05-26'
hardware_targets:
- NVIDIA Orin
- NVIDIA Xavier
- NVIDIA Jetson
- NVIDIA DRIVE
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://developer.nvidia.com/deep-learning-accelerator
tags:
- NVIDIA
- DLA
- deep learning accelerator
- fixed-function
- Jetson
- DRIVE
- Orin
- Xavier
toolchains:
- TensorRT
- CUDA
- cuDLA
- JetPack SDK
- DLA compiler
- DLA runtime stack
- DLA firmware
type: hardware_target
updated: '2026-06-29'
---

# NVIDIA Deep Learning Accelerator (DLA)

The NVIDIA Deep Learning Accelerator (DLA) is a fixed-function hardware accelerator integrated into NVIDIA's edge AI platforms, including the Jetson and DRIVE families of system-on-chips (SoCs). It is designed to offload deep learning inference workloads from the GPU and CPU, providing power-efficient acceleration for convolutional neural networks and other deep learning operations. The DLA is available in two generations: first-generation DLA on Xavier SoCs and second-generation DLA on Orin SoCs, with Orin featuring up to two second-generation DLA cores. The DLA is complemented by a software stack that includes an offline compiler (invoked via TensorRT) and a runtime stack consisting of firmware, a kernel-mode driver, and a user-mode driver. NVIDIA's cuDLA extension further integrates DLA programming under the CUDA model, enabling seamless hybrid GPU+DLA execution. The DLA targets applications such as autonomous driving, robotics, and edge AI where power efficiency and real-time performance are critical.

## Key Claims

- DLA is a fixed-function accelerator for deep learning operations, supporting layers such as convolution, deconvolution, fully connected, activation, pooling, and batch normalization.
- Orin SoCs feature up to two second-generation DLA cores, offering up to 9X the performance of the two first-generation DLAs on Xavier.
- The DLA delivers almost 2.5X the power efficiency of a GPU for AI workloads.
- Combined FP16 half-precision and NVDLA on Xavier achieved a reported 40x speedup over baseline (Postmates X case study).
- DLA software performs fusions to reduce memory passes, and TensorRT provides a unified interface for GPU, DLA, or hybrid deployment.
- Offloading inference to DLA frees GPU/CPU for other tasks, enabling parallel workload execution and improved overall system throughput.

## Optimization-Relevant Details

- **ISA/profile:** Fixed-function accelerator (not general-purpose RISC-V); operates as a hardware accelerator alongside GPU and CPU in NVIDIA SoCs.
- **Vector/matrix/accelerator support:** Dedicated hardware for deep learning operations; does not execute arbitrary vector instructions but accelerates specific tensor operations.
- **Memory/cache/TLB/DMA:** DLA has its own memory subsystem (details not publicly documented in the resource); data movement is managed through the DLA runtime stack and DMA transfers orchestrated by firmware and drivers.
- **Compiler/toolchain support:** TensorRT serves as the primary compilation interface, converting neural network graphs into DLA loadable binaries. The DLA offline compiler is invoked through TensorRT's builder API. CUDA and cuDLA provide a unified programming model for GPU and DLA. Support is available via JetPack SDK on Jetson platforms.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – An alternative AI accelerator benchmark on a RISC-V chiplet architecture, providing a contrast with the NVIDIA DLA approach.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – A RISC-V-based AI accelerator benchmark (Grayskull) that competes with NVIDIA hardware in power-efficiency metrics.

## Sources

- [NVIDIA Deep Learning Accelerator (DLA) – Developer Page](https://developer.nvidia.com/deep-learning-accelerator)

