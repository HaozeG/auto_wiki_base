---
type: entity
tags: [risc-v, commercial-ip, dsp, vector, ai-edge, andes-technology]
sources:
  - https://www.andestech.com/en/2021/12/02/andes-risc-v-superscalar-multicore-ax45mp-and-vector-processor-nx27v-upgrade-their-spec-and-performance/
  - https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/
  - https://www.globenewswire.com/en/news-release/2021/12/02/2345341/0/en/Andes-RISC-V-Superscalar-Multicore-A-X-45MP-and-Vector-Processor-NX27V-Upgrade-Their-Spec-and-Performance.html
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

# Andes AX45MP and NX27V

The Andes AX45MP and NX27V form a paired RISC-V processor IP solution from Andes Technology Corporation targeting AI-edge and embedded Linux SoC designs. The AX45MP is a 64-bit superscalar multicore application processor, while the NX27V is a companion vector processing unit (VPU) compliant with RVV 1.0. Together they appear in Andes's QiLai SoC, which powers the Voyager micro-ATX development platform. Andes Technology is a founding RISC-V International member and contributed the P-extension packed-SIMD specification to the RISC-V standard.

## Key Claims

- AX45MP is an 8-stage, 64-bit superscalar multiprocessor supporting up to 4 cores, with dual-issue in-order pipeline, integrated DSP, single/double-precision FPU, and Linux-capable MMU.
- Upgraded AX45MP delivers up to 3× memory bandwidth improvement and over 20% higher floating-point performance (Whetstone benchmark) compared to its predecessor.
- NX27V supports RVV 1.0 (ratified) with configurable VLEN from 128 to 512 bits and DLEN (data path width) options of 128/256/512 bits, enabling flexible throughput trade-offs.
- NX27V adds Andes-proprietary BF16 and Int4 data type support for AI workloads, beyond the standard RVV 1.0 FP16–FP64 and Int8–Int64 types.
- NX27V contains an Out-of-Order VPU with a Streaming Port interface that connects directly to external hardware accelerator engines, decoupling data movement from compute scheduling.
- AndesAIRE NN SDK converts PyTorch, ONNX, and TensorFlow Lite models to binaries targeting the NX27V, providing a full software deployment stack.
- QiLai SoC integrates quad-core AX45MP plus NX27V in a single die; demonstrated on the Voyager micro-ATX development board (announced November 2024).

## Relationships

- [[risc_v_vector_extension]]: NX27V is a commercial silicon implementation of RVV 1.0 with proprietary AI data-type extensions.
- [[risc_v_p_extension]]: Andes Technology donated the original packed-SIMD (P-extension) specification to RISC-V International, and AX45MP cores include P-extension support.
- [[tvm_riscv_backend]]: AndesAIRE SDK competes with TVM as a model deployment path; TVM's RVV backend can also target NX27V-class hardware.

## Sources

- Andes press release: https://www.andestech.com/en/2021/12/02/andes-risc-v-superscalar-multicore-ax45mp-and-vector-processor-nx27v-upgrade-their-spec-and-performance/
- QiLai/Voyager: https://www.cnx-software.com/2024/11/06/andes-qilai-quad-core-ax45mp-risc-v-soc-with-nx27v-vector-processor-powers-micro-atx-voyager-development-platform/
- GlobeNewswire: https://www.globenewswire.com/en/news-release/2021/12/02/2345341/0/en/Andes-RISC-V-Superscalar-Multicore-A-X-45MP-and-Vector-Processor-NX27V-Upgrade-Their-Spec-and-Performance.html
