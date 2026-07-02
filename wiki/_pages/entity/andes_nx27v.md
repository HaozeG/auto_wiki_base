---
canonical_name: Andes NX27V
aliases:
- AndesCore NX27V
- NX27V
- Andes RISC-V Vector Processor NX27V
- Andes Technology NX27V
- RISC-V NX27V
subtype: hardware_target
tags:
- RISC-V
- vector processor
- Andes
scorecard:
  novelty_delta: 0.8
  claim_density: 0.4
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/a23be859f5aa7b68.md
- https://www.globenewswire.com/news-release/2020/12/02/2138618/0/en/andes-risc-v-vector-processor-nx27v-is-upgraded-to-rvv-1-0.html
- raw/cache/88af220095d3e0cf.md
- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
source_url: https://www.globenewswire.com/news-release/2020/12/02/2138618/0/en/andes-risc-v-vector-processor-nx27v-is-upgraded-to-rvv-1-0.html
fetched_at: '2026-07-02T04:49:56.624212+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Andes NX27V

The Andes NX27V (AndesCore NX27V) is a RISC-V vector processor IP core developed by Andes Technology Corporation, announced as the first commercial RISC-V vector processor to support the RISC-V Vector Extension (RVV) version 1.0. The NX27V is part of the 27-series in Andes' comprehensive RISC-V CPU family, which ranges from the entry-level N22 to the high-performance 45-series. The vector processor supports full data types up to 64 bits (FP64 and Int64) and includes new RVV 1.0 instructions such as vector floating-point reciprocal and reciprocal square-root estimate. Additionally, LMUL (vector length multiplier) was extended with fractional options to allow more flexible use of register bits. Andes Technology, a Founding Premier member of RISC-V International, adopted RISC-V as the base of its fifth-generation AndeStar V5 architecture. The NX27V has been adopted by server-bound customers as of 2020.

## Key Claims

- First commercial RISC-V vector processor IP upgraded to support RVV 1.0.
- Supports full data types up to 64-bit (FP64 and Int64).
- RVV 1.0 includes vector floating-point reciprocal and reciprocal square-root estimate instructions.
- LMUL fractional options enable more flexible register usage.
- Part of Andes' 27-series RISC-V CPU family; Andes CPUs exceeded 1 billion SoC shipments annually since 2018.

## Relationships

- [[xuantie_c908]]: Another RISC-V processor core with RVV 1.0 support, targeting AIoT applications, from T-Head.
- [[k230]]: SoC integrating RISC-V C908 cores with RVV 1.0, representing an end-product using RVV-enabled cores.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: Compilation pipeline targeting RVV hardware for GEMM micro-kernels, relevant to NX27V as a potential target.

## Sources

- https://www.globenewswire.com/news-release/2020/12/02/2138618/0/en/andes-risc-v-vector-processor-nx27v-is-upgraded-to-rvv-1-0.html
