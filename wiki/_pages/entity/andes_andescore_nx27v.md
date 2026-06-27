---
type: entity
tags:
  - risc-v
  - ip-core
  - vector
  - ai-soc
  - embedded-ai
  - andes-technology
sources:
  - https://www.andestech.com/en/risc-v-andescorex/
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.7
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.5
  hub_potential: 0.4
---

# Andes Technology AndesCore NX27V

The AndesCore NX27V is a high-performance RISC-V vector processor IP core developed by Andes Technology (Taiwan), designed for integration into AI SoCs, DSP subsystems, and automotive edge-compute designs. It implements the RISC-V Vector Extension (RVV) 1.0 specification with configurable VLEN (vector register length) up to 512 bits, enabling SIMD-style parallel computation across integer and floating-point data types. Andes Technology, a founding member of RISC-V International, licenses its core portfolio to over 200 semiconductor companies worldwide. The NX27V belongs to the NX (vector-capable) series within the AndesCore family, which also includes scalar N/D series cores; the distinction makes NX27V suitable for workloads requiring vectorized neural network inference, image processing, or multi-channel DSP at power envelopes competitive with ARM Cortex-M55 and Cortex-R82. The core targets embedded AI use cases where a dedicated NPU is too costly or inflexible, bridging the gap between pure scalar RISC-V cores and full NPU solutions.

## Key Claims

- NX27V implements RVV 1.0 with configurable VLEN from 128 to 512 bits, supporting INT8, INT16, FP16, and FP32 element types for ML kernels.
- Andes Technology holds RISC-V International founding membership and has licensed AndesCore IP to more than 200 chip companies as of 2024.
- The AndesCore family separates scalar (N/D series) from vector (NX series) products; NX27V is the primary vector core targeting AI/DSP SoC integration.
- NX27V is used in automotive SoC designs where functional safety and power efficiency are required alongside ML inference capability.
- Competing directly with ARM Cortex-M55 (Helium/MVE vector) and Cortex-R82 for edge AI workloads that need vectorized inference without a discrete NPU.
- The core supports both 32-bit and 64-bit base ISA variants, allowing flexible integration in RV32 or RV64 SoC subsystems.

## Relationships

- [[risc_v_vector_extension]] — NX27V fully implements RVV 1.0, the standard RISC-V vector ISA this core is built upon.
- [[risc_v_architecture]] — Part of the broader RISC-V ecosystem; licensed ISA from RISC-V International.
- [[sifive_intelligence_x280]] — Competing RISC-V vector IP core from SiFive targeting similar AI/edge SoC markets.
- [[fpga_riscv_isa_extension_nn_inference]] — Provides context for RISC-V ISA extension approaches to NN inference including vector cores.
- [[tinyml_mcu_inference]] — AndesCore NX27V is a hardware substrate for TinyML inference pipelines.

## Sources

- Andes Technology AndesCore NX product page: https://www.andestech.com/en/risc-v-andescorex/
- RISC-V International member directory (founding members list)
- AndesCore NX27V datasheet and product brief
