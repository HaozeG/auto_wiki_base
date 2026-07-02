---
canonical_name: Windows ML on AMD NPU
aliases:
- Windows ML deployment on AMD Ryzen AI NPU
- AMD NPU Windows ML
subtype: null
tags:
- Windows ML
- AMD NPU
- ONNX Runtime
- AI inference
- AMD Ryzen AI
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/9db0dd2ba99113fa.md
- https://www.amd.com/en/developer/resources/technical-articles/2026/ai-model-deployment-using-windows-ml-on-amd-npu.html
source_url: https://www.amd.com/en/developer/resources/technical-articles/2026/ai-model-deployment-using-windows-ml-on-amd-npu.html
fetched_at: '2026-07-02T07:19:36.347617+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Windows ML on AMD NPU

Windows ML on AMD NPU is a deployment approach that combines Microsoft's Windows Machine Learning runtime with the AMD Ryzen AI Neural Processing Unit to perform high-performance on-device AI inference on Windows devices. Windows ML is part of Microsoft's Windows AI platform and manages ONNX Runtime execution providers across CPU, GPU, and NPU. On AMD hardware, it automatically utilizes the VitisAIExecutionProvider for the NPU, the MIGraphXExecutionProvider for GPU acceleration via ROCm, and a CPU fallback. This setup enables developers to run converted ONNX models from frameworks such as PyTorch, TensorFlow, and scikit-learn with automatic hardware detection, BF16 optimization, and one-time model compilation. The platform also supports language model deployment through the Foundry Local streamlined interface or via Windows ML APIs with ONNX Runtime GenAI for more granular control.

## Key Claims

- Windows ML automatically discovers and registers execution providers (VitisAI for NPU, MIGraphX for GPU, CPU fallback) without manual configuration.
- The runtime automatically converts FP32 ONNX models to BF16 for NPU execution using the VAIML compiler.
- Execution policies PREFER_NPU, PREFER_GPU, and PREFER_CPU allow developers to control which accelerator is used.
- Language model deployment is supported via two paths: Foundry Local (high-level, automatic download of pre-optimized models) and Windows ML APIs with ONNX Runtime GenAI (maximum control).
- Windows ML uses a shared ONNX Runtime across Windows, reducing application size.
- Quantization from FP32 to A8W8 (CNN) or A16W8 (Transformer) can improve performance; conversion is handled by the VS Code AI Toolkit.
- System requirements include Windows 11 24H2, Visual Studio 2022, Python 3.10-3.12, and the latest AMD NPU drivers.

## Relationships

- [[k230]]: A RISC-V-based edge AI SoC with NPU, representing a different hardware ecosystem (RISC-V vs x86) for comparison of NPU deployment approaches.
- [[allwinner_v853]]: Another edge AI SoC with NPU and support for ONNX model deployment, contrastable with the AMD+Windows approach.
- [[onnx_int8_vs_fp16_jetson_orin_nano_latency_benchmark]]: A benchmark of ONNX Runtime on NVIDIA Jetson Orin Nano, illustrating performance tradeoffs on competing hardware that can inform evaluation of AMD NPU inference.

## Sources

- https://www.amd.com/en/developer/resources/technical-articles/2026/ai-model-deployment-using-windows-ml-on-amd-npu.html
