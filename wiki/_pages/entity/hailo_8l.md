---
cold_start: true
created: '2026-07-02'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 1.0
  hub_potential: 0.3
  novelty_delta: 1.0
  self_containedness: 0.9
sources:
- https://danieldubinsky.github.io/personal-site/case-studies/yolo26n-hailo-L8/
tags:
- ai-accelerator
- edge-inference
- npu
- intel-hailo
type: entity
updated: '2026-06-28'
---

# Hailo-8L

The Hailo-8L is an edge AI accelerator NPU produced by Hailo, designed for low-power inference on vision and object detection models. It offers a theoretical peak performance of 13 TOPS (tera-operations per second) at INT8 precision and is typically deployed via PCIe on embedded platforms such as the Raspberry Pi 5. The Hailo-8L is programmed using the Hailo Dataflow Compiler (DFC), which parses ONNX models and partitions them into execution contexts constrained by on-chip SRAM. In the YOLO26n port documented by Dubinsky, the backbone was split into five execution contexts due to SRAM limits, introducing fixed PCIe overhead per frame. A hybrid architecture is required because detection head operators (e.g., GatherElements, TopK) are unsupported on the NPU and must be offloaded to the host CPU. The Hailo-8L supports INT8 quantization via the DFC calibration pipeline and is used with the Hailo Executable Format (HEF).

## Key Claims

- The Hailo-8L provides 13 TOPS theoretical compute at INT8, with a theoretical compute floor of ~0.41 ms for YOLO26n.
- The DFC automatically partitions models into execution contexts; for YOLO26n, five contexts were generated, indicating tight SRAM constraints.
- End-to-end inference of YOLO26n on a Hailo-8L + Raspberry Pi 5 reaches 86.5 FPS (C++ implementation) and a 13× speedup over CPU-only ONNX runtime.
- The NPU does not natively support detection head operations like GatherElements, ReduceMax, TopK, Mod, or Gather, requiring offload to the CPU.
- Calibration for INT8 quantization uses the COCO dataset; the quantized model achieved an mAP of 0.371 after letterbox preprocessing.

## Relationships

- [[gemmini]] — Another edge-oriented AI accelerator, but based on a systolic array architecture and tightly coupled with RISC-V CPUs via RoCC.
- [[yolo26n_hailo_8l_benchmark]] — Benchmark results for YOLO26n on the Hailo-8L, including detailed latency breakdowns and accuracy measurements.
- Insufficient context for additional cross-links; the wiki currently lacks pages for other Hailo products or comparator edge NPUs.

## Sources

- https://danieldubinsky.github.io/personal-site/case-studies/yolo26n-hailo-L8/
