---
type: entity
tags: [risc-v, tinyML, inference-library, RVV, embedded, CMSIS-NN, quantization]
sources:
  - https://dl.acm.org/doi/10.1145/3637543.3652878
  - https://mediatum.ub.tum.de/doc/1759366/1759366.pdf
  - https://www.semanticscholar.org/paper/From-Simulation-to-RVV-Hardware:-Evaluating-the-on-Witteler-Prof/73bf048b066607e3a3ddda5000db4322169aa4c9
  - https://www.researchgate.net/publication/381895543_muRISCV-NN_Challenging_Zve32x_Autovectorization_with_TinyML_Inference_Library_for_RISC-V_Vector_Extension
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# muRISCV-NN

muRISCV-NN is an open-source library of optimized deep learning inference kernels for RISC-V processors, targeting embedded and microcontroller-class devices. It is derived from ARM's CMSIS-NN library but reimplemented using RISC-V Vector (RVV) intrinsics, maintaining bit-exact numerical compatibility with CMSIS-NN so it can serve as a drop-in replacement in existing TinyML deployment pipelines. The library integrates directly with TensorFlow Lite for Microcontrollers (TFLM) and microTVM, enabling standard ML model deployment on RISC-V MCUs without changing the compilation front-end. muRISCV-NN targets the Zve32x embedded vector sub-extension (32-bit ELEN, no FPU) as its minimum hardware requirement, making it applicable to area-constrained silicon. Performance benchmarks published at ACM Computing Frontiers (May 2024) demonstrate: a 3.85× cycle-count reduction for ResNet inference versus scalar code, 1.8–2.8× speedup of unvectorized kernels over TFLM reference kernels, and up to 60% runtime improvement for convolutional models versus LLVM's auto-vectorization of the same source code. The library was validated on the Canaan Kendryte K230 — the first commercial RISC-V silicon implementing ratified RVV 1.0 — bridging simulation-only evaluation to real hardware. These results demonstrate that hand-tuned vector intrinsics outperform compiler auto-vectorization for structured convolution patterns at this scale.

## Key Claims

- Bit-exact drop-in replacement for ARM CMSIS-NN; integrates with TFLM and microTVM on RISC-V.
- Targets Zve32x minimum (32-bit ELEN, no FPU) for maximum MCU-class coverage.
- 3.85× cycle-count reduction on ResNet inference via manual RVV vectorization vs. scalar baseline.
- Unvectorized muRISCV-NN kernels beat TFLM reference kernels by 1.8–2.8× on RISC-V.
- Up to 60% runtime improvement over LLVM's auto-vectorization for convolutional layers.
- Validated on Canaan K230 (first commercial RVV 1.0 hardware); published ACM Computing Frontiers May 2024.

## Relationships

- [[risc_v_zve_embedded_vector]]: muRISCV-NN targets Zve32x as minimum; demonstrates practical utility of embedded vector sub-extensions for TinyML.
- [[risc_v_vector_extension]]: Full RVV 1.0 (as in K230) enables the best muRISCV-NN performance; Zve32x is the lower-bound target.
- [[canaan_kendryte_k510_k230]]: K230 was the primary real-hardware validation platform for muRISCV-NN evaluation.
- [[gnu_toolchain_riscv_vector]]: muRISCV-NN uses RVV intrinsics rather than relying on GCC/LLVM auto-vectorization, outperforming the compiler by up to 60%.
- [[tvm_riscv_backend]]: TVM microTVM is one of the deployment frameworks muRISCV-NN integrates with for RISC-V MCU inference.

## Sources

- https://dl.acm.org/doi/10.1145/3637543.3652878
- https://mediatum.ub.tum.de/doc/1759366/1759366.pdf
- https://www.semanticscholar.org/paper/From-Simulation-to-RVV-Hardware:-Evaluating-the-on-Witteler-Prof/73bf048b066607e3a3ddda5000db4322169aa4c9
