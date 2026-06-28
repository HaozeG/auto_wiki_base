---
cold_start: true
created: '2026-07-03'
inbound_links: 1
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/Tencent/ncnn
tags:
- neural network
- inference framework
- Tencent
- mobile
- edge
- RISC-V
- Vulkan
- pnnx
type: entity
updated: '2026-06-28'
---

# ncnn

ncnn is a high-performance neural network inference framework developed by Tencent, designed specifically for mobile, embedded, and desktop deployment with zero third-party runtime dependencies. It supports both CPU and Vulkan GPU backends, enabling efficient execution across Android, iOS, Linux, Windows, macOS, WebAssembly, and various RISC-V platforms such as AllWinner D1 and Loongson 2K1000. The framework includes pnnx, a tool for converting PyTorch and ONNX models into ncnn format, and provides C++ and Python APIs for seamless integration. ncnn is widely used in Tencent's consumer applications including QQ, WeChat, and Qzone, and supports a broad range of neural network architectures from classical CNNs like VGG and ResNet to lightweight models like MobileNet and ShuffleNet, as well as face detection and object detection models. Its lack of external dependencies and careful ARM NEON assembly optimization contribute to its reputation as one of the fastest inference frameworks on mobile CPUs.

## Key Claims

- ncnn has no third-party runtime dependencies (no BLAS, NNPACK, etc.).
- Supports CPU and Vulkan GPU backends.
- Provides pnnx tools for converting PyTorch and ONNX models to ncnn format.
- Cross-platform: Android, iOS, Linux, Windows, macOS, WebAssembly, RISC-V (AllWinner D1, Loongson 2K1000), HarmonyOS, etc.
- Used in Tencent applications: QQ, Qzone, WeChat, Pitu.
- Supports a wide variety of neural network models: CNN, RNN, detection, face recognition.
- ARM NEON assembly optimization for high performance on mobile CPUs.
- Multi-core parallel computing acceleration and ARM big.LITTLE CPU scheduling optimization.
- Low memory footprint through sophisticated memory management and data structure design.

## Relationships

- Insufficient context for additional cross-links to entity pages in the current wiki. The resource is a standalone inference framework; no directly related entity pages are available in the provided wiki context.

## Sources

- [Tencent/ncnn GitHub Repository](https://github.com/Tencent/ncnn)

