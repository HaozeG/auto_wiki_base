---
cold_start: false
created: 2026-06-26
inbound_links: 12
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- raw/sources/riscv_ai_native_platform.md
- raw/sources/sifive_intelligence_x280_2ndgen.md
- raw/sources/arrow_riscv_vector_ml_inference.md
- raw/sources/fpga_riscv_isa_extensions_nn.md
tags:
- risc-v
- isa
- vector-processing
- ai-acceleration
type: entity
updated: 2026-06-26
------------------

# RISC-V Vector Extension (RVV)

The RISC-V Vector Extension (RVV) is a standardized, scalable SIMD instruction set extension for RISC-V processors that enables efficient parallel computation over variable-length vectors. Unlike fixed-width SIMD (such as ARM NEON's 128-bit or AVX-512's 512-bit), RVV uses a vector-length-agnostic programming model where software specifies operations over abstract vector lengths and hardware executes them at its physical vector register width. This architectural flexibility makes RVV particularly valuable for AI/ML inference workloads, where matrix multiplications, dot products, and activation functions map naturally to vectorized data paths. The RVV 1.0 specification was ratified in 2021 and is part of the RVA23 mandatory profile ratified in late 2024.

## Key Claims

- RVV 1.0 is mandated by the RVA23 profile, making vector capability a guaranteed feature for all RVA23-compliant RISC-V processors; hardware deployments are expected in 2026.
- SiFive Intelligence X280 implements 512-bit vector registers with a dual-issue, in-order 8-stage pipeline, supporting vector lengths up to 512 bits with decoupled scalar/vector execution.
- SiFive X160/X180 Gen 2 use 128-bit wide vector registers (vlen) with a 64-bit datapath (dlen), achieving throughput of 8× Int8 / 4× Int16 / 2× Int32 per cycle.
- The Arrow accelerator, implementing a subset of RISC-V v0.9 vector ISA on a Xilinx XC7A200T FPGA, achieves 2–78× speedup and 20–99% energy reduction versus scalar RISC processors on ML inference benchmarks.
- A custom FPGA.VCONV RVV-inspired extension achieves 7.20× speedup with 60–75% latency savings per inference pass, the highest single-extension contribution among four tested ISA extensions.
- llama.cpp fully leverages 128-bit RISC-V Vector extensions, demonstrating production-grade LLM inference on RISC-V hardware.
- The 2nd Gen SiFive Intelligence family adds FP4 and FP8 datatypes to the vector pipeline to support quantized LLM inference; first silicon expected Q2 2026.

## Relationships

- [[risc_v_matrix_extensions]]: RVV is the foundation; matrix extensions (IME, VME, AME) layer higher-dimensional tensor operations on top of RVV's vector infrastructure.
- [[sifive_intelligence_x280]]: SiFive's X280 and its Gen 2 variants are the primary commercial implementations of wide-vector RISC-V for AI workloads.
- [[tenstorrent_blackhole]]: Tenstorrent's Tensix cores use Baby RISC-V processors rather than RVV, representing an alternative approach where RISC-V controls dataflow rather than executing vector arithmetic directly.
- [[fpga_riscv_isa_extension_nn_inference]]: Demonstrates the prototyping pathway: custom ISA extensions on FPGA-hosted RISC-V cores before ASIC tapeout.
- [[rva23_profile]]: The profile that mandates RVV 1.0 and enables vendor-independent software targeting.

## Sources

- riscv_ai_native_platform.md: RVA23 profile details, llama.cpp usage, matrix extension names, 2026 deployment timeline.
- sifive_intelligence_x280_2ndgen.md: X280 512-bit vector specs, X160/X180 Gen 2 throughput numbers, FP4/FP8 addition, Q2 2026 silicon date.
- arrow_riscv_vector_ml_inference.md: Arrow FPGA performance (2–78× speedup, 20–99% energy reduction).
- fpga_riscv_isa_extensions_nn.md: FPGA.VCONV 7.20× speedup data.
