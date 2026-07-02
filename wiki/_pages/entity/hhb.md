---
canonical_name: HHB
aliases:
- Heterogeneous Honey Badger
- T-Head HHB
subtype: null
tags:
- toolchain
- neural network deployment
- T-Head
- Xuantie
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/1b8d62580955e804.md
- https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
source_url: https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
fetched_at: '2026-07-02T06:12:25.049872+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# HHB

HHB (Heterogeneous Honey Badger) is a neural network model deployment toolset developed by T-Head specifically for the Xuantie chip platform, including the RISC-V based C906, C908, and associated SoCs such as the Canaan Kendryte K230. Built upon the open-source TVM framework, HHB provides a comprehensive set of tools for compilation optimization, performance analysis, process debugging, and result simulation. It supports importing models from popular training frameworks including TensorFlow, PyTorch, Caffe, ONNX, and TFLite, and can output either C code that calls the SHL (Simple Heterogeneous Library) or directly executable binaries optimized for the Wujian SoC platform. The toolset offers dual interfaces—traditional Unix command line and Python—to facilitate secondary development and automation. HHB also handles data type conversion, supporting 8/16-bit fixed-point and 16/32-bit floating-point formats, symmetric and asymmetric quantization, and channel quantization. It is a key enabler for deploying AI models on RISC-V edge devices, bridging the gap between training frameworks and the constrained hardware of AIoT platforms.

## Key Claims

- Developed by T-Head for the Xuantie chip platform (C906, C908, K230).
- Based on the open-source TVM framework with additional command-line options and quantization algorithms.
- Supports model formats from TensorFlow, PyTorch, Caffe, ONNX, TFLite.
- Supports data types: 8/16-bit fixed-point, 16/32-bit floating-point, symmetric and asymmetric quantization.
- Performs network structure optimization before deployment.
- Outputs C code (using SHL) or directly executable binaries.
- Provides behavior simulation on the host (x86 PC).
- Offers both Unix command-line and Python interfaces.
- Used in the K230 AI deployment workflow, requiring Docker environment and cross-compilation with the RTT toolchain.

## Relationships

- HHB is the primary model deployment tool for the [[k230]] SoC, which integrates dual Xuantie C908 cores and a KPU accelerator, as documented in the official K230 SDK.
- HHB's reliance on TVM connects it to the broader TVM compilation ecosystem, though no dedicated TVM page exists in this wiki yet.
- The [[allwinner_v853]] SoC also targets AIoT applications with an NPU, but uses a different vendor toolchain rather than HHB, making it a contrasting reference point in the RISC-V AI accelerator landscape.
- HHB integrates with SHL (Simple Heterogeneous Library), an optimized neural network library for Xuantie CPUs, which provides assembly-optimized implementations.

## Sources

- https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
