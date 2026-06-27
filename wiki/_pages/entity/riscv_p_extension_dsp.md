---
type: entity
tags:
  - risc-v
  - dsp
  - simd
  - embedded-ml
  - p-extension
  - andes
sources:
  - https://github.com/riscv/riscv-p-spec
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.7
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.55
  hub_potential: 0.4
---

# RISC-V P Extension (Packed SIMD DSP)

The RISC-V P extension (Packed SIMD) adds sub-word parallel data processing instructions to scalar RISC-V cores, enabling DSP and ML workloads on microcontrollers that lack a vector unit (the V extension). P-extension instructions operate on packed 8-bit and 16-bit data within standard 32-bit or 64-bit integer registers, allowing 4× INT8 or 2× INT16 parallel multiply-accumulate (MAC) operations per instruction on RV32 cores. The specification reached version 0.9.12 in late 2023 and was ratified in January 2024 as a RISC-V International standard. Unlike the V extension (which requires a separate wide vector register file), P-extension adds only ~80 new instructions to the base ISA—making implementation area negligible and suitable for cost- and power-constrained MCUs. Andes Technology and Nuclei System Technology ship commercial RISC-V cores with P-extension support; Andes has deployed P-ext cores in IoT and wearable SoCs where adding a full vector unit is impractical. The TVM deep learning compiler supports P-extension code generation for RISC-V MCU targets, enabling INT8 CNN inference on P-ext cores at latencies competitive with ARM Cortex-M55 Helium for equivalent model sizes.

## Key Claims

- P extension adds packed SIMD instructions operating on 8-bit and 16-bit elements packed within 32/64-bit registers: 4× INT8 or 2× INT16 parallel MACs per instruction on RV32.
- Specification v0.9.12 was frozen in late 2023 and formally ratified by RISC-V International in January 2024.
- Implementation overhead is approximately 80 additional instructions added to the base ISA, with negligible area cost compared to V extension (no wide vector register file required).
- Andes Technology and Nuclei System Technology ship production RISC-V MCU IP cores with P-extension support as of 2024.
- Apache TVM generates optimized P-extension kernels for RISC-V MCU targets, enabling INT8 CNN inference without a vector unit.
- P-extension targets sub-10 mW embedded AI workloads: keyword spotting, anomaly detection, and sensor fusion on MCU-class RISC-V cores without RVV.

## Relationships

- [[risc_v_vector_extension]] — P extension is the scalar SIMD complement to RVV; P targets MCUs without a vector unit, V targets application cores with full vector registers.
- [[tvm_hybrid_op_riscv_p_extension]] — TVM's P-extension backend for RISC-V is documented in this page, which covers the TVM compilation context.
- [[risc_v_architecture]] — P extension is a RISC-V International ratified standard extension of the base ISA.
- [[tinyml_mcu_inference]] — P extension is a key enabler for TinyML inference on low-cost RISC-V MCUs.
- [[andes_andescore_nx27v]] — Andes Technology, which implements the P extension in MCU cores, also offers the NX27V vector core for higher-performance AI.

## Sources

- RISC-V P specification GitHub: https://github.com/riscv/riscv-p-spec
- Andes Technology P-extension product notes
- TVM RISC-V P-extension backend: Apache TVM project
