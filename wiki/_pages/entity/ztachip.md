---
cold_start: false
created: '2026-07-05'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/ztachip/ztachip
tags:
- risc-v
- fpga
- ai-accelerator
- open-source
- tensor-processor
- edge-ai
type: entity
updated: '2026-06-27'
---

# Ztachip

Ztachip is an open-source multicore, data-aware, embedded RISC-V AI accelerator designed for edge inferencing on low-end FPGA devices or custom ASICs. It combines a VexRiscv CPU with a custom tensor processor comprising 28 Pcores, each containing scalar and vector ALUs with 16 hardware threads, to accelerate a broad range of vision and AI tasks. The platform provides up to 20–50× acceleration over non-accelerated RISC-V implementations, and also outperforms RISC-V cores with vector extensions on many workloads. A key differentiator is its tensor programming paradigm, which enables developers to leverage massive data parallelism through a C-like DSL compiler, AI vision libraries, and MicroPython support. Ztachip's tensor processor can handle tasks from classical computer vision (edge detection, optical flow, motion detection) to executing TensorFlow AI models, distinguishing it from accelerators that only accelerate narrow application domains.

## Key Claims

- Ztachip achieves up to 20–50× speedup on vision/AI tasks compared to a non-accelerated RISC-V implementation, and performs better than RISC-V with vector extensions.
- The tensor processor contains 28 Pcores, each with a Scalar and Vector ALU and 16 threads of execution, configurable as a systolic array for in-memory compute.
- Hardware architecture includes a Scheduling Processor (Mcore), Dataplane, Scratch-Pad Memory, Stream Processor, and Tensor Engine, tied via an AXI bus to a VexRiscv CPU and DRAM.
- Software stack comprises a C-like DSL compiler, prebuilt AI vision libraries (e.g., edge detection, Harris corner, optical flow, neural nets), and a MicroPython port with examples.
- The platform targets low-end FPGAs (e.g., ArtyA7-100T) and includes a generic platform wrapper for custom ASIC implementation.
- Demos include multi-tasking with ObjectDetection, edge detection, Harris-Corner, and Motion Detection running concurrently.

## Relationships

- [[risc_v_vector_extension]] — Ztachip claims superior performance to RISC-V cores equipped with the Vector Extension on many vision and AI tasks, making it a competing acceleration approach.
- [[gemmini]] — Both are open-source RISC-V AI accelerators, but Ztachip's tensor processor targets a wider range of tasks beyond DNN convolution, including classical vision algorithms.

## Sources

- GitHub README: https://github.com/ztachip/ztachip

