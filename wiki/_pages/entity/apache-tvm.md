---
canonical_name: Apache TVM
aliases:
- TVM
- Apache TVM
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.2
  self_containedness: 0.7
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/2842c157ecb13311.md
- https://tvm.apache.org/docs/
source_url: https://tvm.apache.org/docs/
fetched_at: '2026-07-02T11:39:51.936692+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Apache TVM

Apache TVM is an open-source deep learning compiler that enables access to high-performance machine learning across diverse hardware backends. It provides a unified, programmable software stack that brings together hardware vendors, compiler engineers, and ML researchers to optimize and deploy models efficiently. In the context of RISC-V AI acceleration, TVM serves as a foundational toolchain: the XuanTie C906 uses HHB, a TVM-based deployment tool, and the Kendryte K230 supports TVM for model compilation. The project encompasses several subcomponents including TensorIR for low-level tensor program optimization, Relax for high-level graph abstraction, TIRx for native-level kernel authoring, DLight for rule-based GPU scheduling, and MetaSchedule for search-based auto-tuning. TVM supports import from major frameworks such as PyTorch, TensorFlow, and ONNX, and can target a variety of backends including CUDA, PTX, and RISC-V vector extensions.

## Key Claims

- Apache TVM is an open-source deep learning compiler.
- It provides a unified software stack for ML optimization across hardware platforms.
- Supports toolchains and frameworks including PyTorch, TensorFlow, ONNX, CUDA, and RISC-V vector extensions.
- Subcomponents include TensorIR, Relax, TIRx, DLight, and MetaSchedule.
- Used as a toolchain in RISC-V AI accelerators such as the XuanTie C906 and Kendryte K230.
- Community-driven project with contributions from hardware vendors, compiler engineers, and ML researchers.

## Relationships

- [[xuantie-c906]]: The XuanTie C906 uses HHB, a deployment toolchain based on Apache TVM, for quantized neural network inference.
- [[kendryte-k230-neural-network-benchmarks]]: The Kendryte K230 benchmarks report TVM as a supported toolchain for converting models from TensorFlow, PyTorch, and ONNX.

## Sources

- https://tvm.apache.org/docs/
