---
cold_start: false
created: 2026-06-26
inbound_links: 6
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- raw/sources/sifive_intelligence_x280_2ndgen.md
- raw/sources/riscv_ai_native_platform.md
tags:
- risc-v
- ai-accelerator
- sifive
- vector-processor
- ip-core
type: entity
updated: 2026-06-26
------

# SiFive Intelligence X280

The SiFive Intelligence X280 is a licensable 64-bit RISC-V vector processor IP core designed for AI and ML workloads, developed by SiFive. It implements a 512-bit wide RISC-V Vector extension with an 8-stage dual-issue in-order scalar pipeline and decoupled scalar/vector execution, enabling simultaneous scalar and vector computation. The X280 is notable for its Vector Coprocessor Interface eXtension (VCIX), which allows SoC designers to attach custom external accelerators that share the vector register file and instruction stream, turning the X280 into an extensible AI processing fabric. Sophgo used the X280 in the SG2380 chip paired with a Sophgo TPU to reach 20 TOPS. The 2nd Gen Intelligence family, announced September 2025 with first silicon targeted Q2 2026, adds RVA23 profile compliance and FP4/FP8 datatype support.

## Key Claims

- X280 implements 512-bit RISC-V vector registers with an 8-stage dual-issue in-order pipeline; supports multi-core clusters of up to 16 cache-coherent cores.
- VCIX (Vector Coprocessor Interface eXtension) enables seamless integration of external custom AI accelerators sharing the X280 vector unit's register file and instruction decode.
- Sophgo SG2380 combines 16 SiFive P670 cores at 2.5 GHz with the X280-based Intelligence unit and a Sophgo TPU to achieve 20 TOPS.
- X160/X180 Gen 2 (entry-level, 32/64-bit respectively) deliver 8× Int8, 4× Int16, 2× Int32 throughput per cycle from 128-bit vector registers (vlen) with 64-bit datapath (dlen).
- The 2nd Gen family (X280 Gen 2, X390 Gen 2, XM Gen 2) adds FP4 and FP8 datatypes to the vector pipeline, enabling INT4/FP8 quantized LLM inference.
- First 2nd Gen silicon expected Q2 2026; IPs are available for licensing as of late 2025.
- SiFive HiFive Premier P550 runs Red Hat Enterprise Linux 10 in developer preview, demonstrating production-OS readiness of the platform.

## Relationships

- [[risc_v_vector_extension]]: X280 is a primary commercial implementation of wide-vector RVV for AI; VCIX extends this with custom accelerator hooks.
- [[rva23_profile]]: 2nd Gen X280 adds RVA23 compliance, enabling Ubuntu and NVIDIA CUDA to target it.
- [[tenstorrent_blackhole]]: Contrasting AI-RISC-V strategy — X280 uses wide RVV; Blackhole uses Baby RISC-V as dataflow controllers.
- [[riscv_ai_ecosystem]]: SiFive is one of the leading IP vendors in the RISC-V AI ecosystem.

## Sources

- sifive_intelligence_x280_2ndgen.md: All X280 and Gen 2 specifications, VCIX description, Sophgo SG2380 use case, Linux support.
- riscv_ai_native_platform.md: Ecosystem context, RVA23 timeline, SiFive's market position.
