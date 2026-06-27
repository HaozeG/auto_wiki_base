---
type: synthesis
connected_entities:
  - spacemit_k1_soc
  - starfive_visionfive2_jh7110
  - andes_andescore_nx27v
  - western_digital_swerv_core
  - riscv_p_extension_dsp
  - riscv_zvfh_extension
  - iree_mlir_compiler
  - zephyr_rtos_tflite_micro
  - risc_v_vector_extension
  - tinyml_mcu_inference
synthesis_status: active
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  bridge_score: 0.7
  contradiction_potential: 0.4
  cross_domain_connection: 0.65
---

# RISC-V AI at the Edge: From MCU to SoC

## RAG Summary

RISC-V has emerged as the dominant open ISA for edge AI deployment, spanning from microcontroller-class devices running TFLite Micro on Zephyr RTOS to application-processor SoCs with integrated NPUs. The SpacemiT K1 SoC (8-core RISC-V, 2 TOPS NPU, RVV 1.0 with Zvfh FP16 support) and StarFive JH7110 (quad-core SiFive U74, 1 TOPS NPU, mainline Linux 6.6 GPU support) represent the SoC end of this spectrum, while RISC-V MCU-class cores from Andes Technology (AndesCore NX27V, RVV 1.0 up to 512-bit VLEN) and Western Digital (SweRV EH1, 4.9 CoreMark/MHz in 28 nm) anchor the embedded end. The RISC-V P extension (packed SIMD, ratified January 2024) enables 4× INT8 MAC per cycle on scalar cores without a vector register file, targeting sub-10 mW microcontrollers. The Zvfh extension adds IEEE 754 FP16 vector operations on top of RVV 1.0, enabling transformer-class inference on RISC-V without a dedicated NPU. The software stack has converged around two primary paths: IREE (Google's MLIR-based AOT compiler) targeting RVV for ahead-of-time vectorized kernel generation, and TFLite Micro on Zephyr RTOS for MCU-class deployment with 32 KB RAM minimum footprint. Key open questions include whether the fragmented extension landscape (P, V, Zvfh, Zve32x) will consolidate into a unified RISC-V embedded AI profile, and whether RISC-V SoC NPU performance can close the gap with ARM Cortex-A plus dedicated ML hardware at comparable silicon area and cost.

---

## Full Synthesis

### The RISC-V Edge AI Stack

The RISC-V ISA's modular extension model has produced a layered edge AI ecosystem where hardware capability and software stack are tightly coupled to the chosen extension set. At the bottom, scalar RISC-V MCU cores without vector extensions can still run ML workloads via the P extension (packed SIMD, ratified 2024): the P extension adds ~80 instructions enabling 4× INT8 or 2× INT16 SIMD MAC operations within standard 32-bit registers, with Andes Technology and Nuclei System Technology shipping production P-ext cores. Above this layer, cores implementing RVV 1.0 (e.g., AndesCore NX27V with up to 512-bit VLEN, SiFive X280 with 512-bit VLEN) enable full SIMD vectorization of ML kernels, achieving order-of-magnitude throughput improvements over scalar. The Zvfh sub-extension adds FP16 native support to RVV, critical for transformer inference—SpacemiT K1 and SiFive X280 are the first commercial implementations.

### SoC-Class Platforms

The SpacemiT K1 and StarFive JH7110 represent the application-processor tier. K1's 2 TOPS NPU with Zvfh support makes it suitable for lightweight LLM inference and object detection (YOLO-class). JH7110 differentiates on GPU integration (Imagination BXE-4-32, mainline Linux 6.6) enabling Vulkan-accelerated ML frameworks. Both platforms are priced under $80 as SBCs, dramatically lowering the barrier for RISC-V edge AI experimentation relative to custom ASIC silicon.

### Software Convergence

IREE's AOT compilation pipeline generates RVV-optimized kernels ahead of deployment, avoiding interpreter overhead on constrained hardware. TFLite Micro on Zephyr handles the MCU tier (32 KB RAM minimum). Zephyr's support for 20+ RISC-V boards and its formal ML inference subsystem API (Zephyr 3.x) make it the de facto RTOS for RISC-V TinyML. The two paths are complementary: IREE targets RVV-capable cores where AOT binary size is acceptable, TFLM targets ultra-low-power MCUs where code size and RAM are the binding constraints.

### Fragmentation Risks

The RISC-V extension landscape presents integration challenges. A single SoC may expose different subsets: RV64GC (JH7110), RV64GCVB (K1 with RVV+Zvfh+B), RV32IMC (SweRV EL2), or RV32IMACPZfh (P+Zfh MCU). Toolchain and runtime must detect and dispatch to the correct kernel variant. The RVA23 profile (ratified 2023) mandates RVV 1.0 for application processors, helping standardize the vector baseline, but P-extension is not included in RVA23, leaving the MCU tier fragmented.

## Open Questions

- Will RISC-V International publish a formal "Embedded AI Profile" that mandates P-extension for MCU-class cores, analogous to RVA23 for application processors?
- Can SpacemiT K1's 2 TOPS NPU performance compete with ARM Cortex-A78AE + Ethos-N78 NPU combinations in automotive edge AI use cases?
- How will the software stack (IREE, TFLM, TVM) converge on a common RISC-V capability detection API to handle P/V/Zvfh extension heterogeneity?
- Will affordable RISC-V SoC SBCs (VisionFive 2, BPI-F3) attract ML framework ports (PyTorch, ONNX Runtime native) comparable to Raspberry Pi ARM ecosystem?

## Connected Pages

- [[spacemit_k1_soc]] — SpacemiT K1 SoC with 2 TOPS NPU and Zvfh FP16 support
- [[starfive_visionfive2_jh7110]] — StarFive JH7110 SoC with GPU and 1 TOPS NPU in VisionFive 2 SBC
- [[andes_andescore_nx27v]] — AndesCore NX27V vector IP core for AI SoC integration
- [[western_digital_swerv_core]] — WD SweRV EH1/EH2/EL2 open-source RISC-V cores
- [[riscv_p_extension_dsp]] — RISC-V P extension packed SIMD for MCU ML
- [[riscv_zvfh_extension]] — Zvfh FP16 extension enabling transformer inference on RVV cores
- [[iree_mlir_compiler]] — IREE AOT compiler with RISC-V RVV backend
- [[zephyr_rtos_tflite_micro]] — Zephyr RTOS + TFLite Micro stack for RISC-V MCUs
- [[risc_v_vector_extension]] — RVV 1.0 specification underlying NX27V and K1 vector compute
- [[tinyml_mcu_inference]] — TinyML inference landscape covering MCU-class RISC-V deployments
