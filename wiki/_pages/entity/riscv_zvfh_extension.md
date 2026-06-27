---
type: entity
tags:
  - risc-v
  - fp16
  - vector
  - ml-inference
  - zvfh
  - rvv
sources:
  - https://github.com/riscv/riscv-v-spec
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.75
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.55
  hub_potential: 0.45
---

# RISC-V Zvfh Extension (FP16 Vector Half-Precision)

The RISC-V Zvfh extension adds IEEE 754 half-precision (FP16) floating-point operations to the RISC-V Vector Extension (RVV), enabling native vector FP16 compute on RISC-V cores without software emulation or round-trip conversion to FP32. Without Zvfh, FP16 values on RISC-V must be promoted to FP32 before arithmetic, doubling memory bandwidth and compute cost. Zvfh is ratified as part of the RISC-V ISA specification and is mandatory for ML inference workloads—particularly transformer-based models—where FP16 activations and weights are standard. The extension adds widening, narrowing, and accumulation instructions for FP16 elements within the V register file, enabling fused multiply-add (FMA) operations on up to VLEN/16 elements per instruction. The SpacemiT K1 and SiFive X280 are among the first commercial RISC-V processors to implement Zvfh in silicon, making them capable of running FP16 transformer inference competitive with ARM SVE FP16 on equivalent silicon area. Zvfh is distinct from Zfh (scalar half-precision float), which adds a single FP16 register without vector capability.

## Key Claims

- Zvfh adds IEEE 754 FP16 operations to the RVV vector register file, enabling up to VLEN/16 FP16 FMA operations per instruction (e.g., 32 FP16 FMAs per instruction at VLEN=512).
- Without Zvfh, RISC-V RVV cores must promote FP16 to FP32 before arithmetic, incurring 2× bandwidth cost on weight loading for inference.
- Zvfh is ratified in the RISC-V ISA specification as a sub-extension of RVV; implementations must also support RVV 1.0 base as a prerequisite.
- SpacemiT K1 (X60 microarchitecture) and SiFive Intelligence X280 are the first commercially available RISC-V cores with Zvfh implemented in silicon (as of 2024).
- Transformer inference on RISC-V with Zvfh achieves FP16 throughput competitive with ARM SVE FP16 on comparable core area, per early benchmark reports.
- Zvfh is distinct from Zfh (scalar FP16 in standard scalar registers); combining both extensions gives full scalar and vector FP16 capability.

## Relationships

- [[risc_v_vector_extension]] — Zvfh is a sub-extension of RVV 1.0; requires the full V extension as a base.
- [[spacemit_k1_soc]] — SpacemiT K1 is one of the first production implementations of Zvfh, a primary differentiator of its AI capability.
- [[sifive_intelligence_x280]] — SiFive X280 also implements Zvfh, relevant to its ML inference positioning.
- [[iree_mlir_compiler]] — IREE's RISC-V FP16 codegen path targets Zvfh to generate native FP16 vector kernels.
- [[int8_fp8_quantization_llm_inference]] — Zvfh FP16 complements INT8 quantization for RISC-V LLM inference.

## Sources

- RISC-V Vector Extension specification (includes Zvfh): https://github.com/riscv/riscv-v-spec
- SpacemiT K1 SoC datasheet (Zvfh implementation note)
- SiFive X280 product brief
