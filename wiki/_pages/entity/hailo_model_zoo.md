---
cold_start: false
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.4
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/hailo-ai/hailo_model_zoo
tags:
- computer-vision
- deep-learning
- quantization
- hailo
- quantized-neural-networks
- edge-ai
- ai-accelerators
- hailo8
- model-zoo
type: entity
updated: '2026-06-28'
---

# Hailo Model Zoo

The Hailo Model Zoo is an open-source repository maintained by Hailo Technologies that provides pre-trained deep learning models and a complete building and evaluation environment for Hailo's AI accelerator hardware. It supports models in ONNX and TensorFlow formats alongside pre-compiled Hailo Executable Format (HEF) binary files, enabling direct deployment on Hailo devices such as the Hailo-8, Hailo-8L, Hailo-10H, Hailo-15H, and Hailo-15L. The workflow within the Model Zoo includes parsing input models into Hailo's internal representation, profiling for performance estimates, optimization via quantization to compressed integer representations, compilation to HEF, and accuracy evaluation using either the Hailo Emulator or physical hardware. The repository also provides retraining instructions for adapting models to custom datasets. It is released under the MIT license and is the primary software entry point for deploying neural network inference on Hailo accelerators.

## Key Claims

- The Hailo Model Zoo provides pre-trained models in ONNX / TensorFlow formats and pre-compiled HEF (Hailo Executable Format) binary files for execution on Hailo devices.
- Models are divided into public models (trained on publicly available datasets) and Hailo Models (trained in-house on internal datasets, each accompanied by retraining instructions).
- The latest release (v5.3.0, April 2026) aligns with Hailo Dataflow Compiler v5.3.0 and HailoRT v5.3.0, ensuring compatibility and performance improvements.
- Newly supported models include YOLOv11-obb (oriented bounding box detection), YOLO26 (NMS-free object detection and instance segmentation), PaddleOCR-v5 (detection and recognition for Hailo-15L), and YOLOv5-seg-hpp (instance segmentation with HailoRT postprocessing).
- The full workflow comprises parsing, profiling, optimization (quantization to compressed integer representation), compilation to HEF, and evaluation (emulator or device-based accuracy measurement).
- The master branch targets Hailo-10 and Hailo-15 devices; the v2.x branch supports Hailo-8 and Hailo-8L devices in combination with the Hailo Dataflow Compiler v3.x branch.
- The repository includes links to benchmark results hosted at hailo.ai and instructions to reproduce those measurements.

## Relationships

- [[tvm_riscv_backend]]: Both TVM and the Hailo Model Zoo provide end-to-end compilation and optimization pipelines for neural network inference targeting specialized hardware, including quantization and code generation.
- [[gemmini]]: Gemmini and the Hailo Model Zoo both offer model deployment workflows for hardware accelerators; Gemmini uses a RoCC interface and systolic array, while Hailo Model Zoo uses the Dataflow Compiler and HEF for commercial edge AI accelerators.

## Sources

- GitHub repository: https://github.com/hailo-ai/hailo_model_zoo
