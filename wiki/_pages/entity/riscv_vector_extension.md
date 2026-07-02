---
canonical_name: RISC-V Vector Extension (RVV)
aliases:
- RISC-V V extension
- RVV
- vector extension
- v-spec
- RISC-V Vector Extension
- RISC-V V vector extension
- RISC-V
- RISC-V ISA
- risk-five
- RISC V
- RISC-V International
subtype: null
tags:
- riscv
- vector
- specification
scorecard:
  novelty_delta: 0.8
  claim_density: 0.25
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.8
sources:
- raw/cache/5012a631903f97a6.md
- https://github.com/riscvarchive/riscv-v-spec
- raw/cache/876948b910a3f287.md
- raw/cache/ac89c67a6b8baf3d.md
- https://en.wikipedia.org/wiki/RISC-V
source_url: https://github.com/riscvarchive/riscv-v-spec
fetched_at: '2026-07-01T03:52:21.482224+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# RISC-V Vector Extension (RVV)

The RISC-V Vector Extension (RVV) is a standard extension to the RISC-V Instruction Set Architecture (ISA) that adds vector processing capabilities. The specification defines a vector register file, vector instructions including arithmetic, memory, and configuration operations, and supports variable-length vectors through the vsetvl model. Version 1.0 of the specification has been frozen and is currently undergoing public review, while earlier stable releases (v0.8 and v0.7.1) are available for reference. The specification is hosted in the riscvarchive/riscv-v-spec GitHub repository as an AsciiDoc document (v-spec.adoc), and tools such as Spike with the RISC-V Proxy Kernel and riscvOVPsim provide simulation support for various versions. RVV is implemented in several commercial and open-source RISC-V cores, including the XuanTie C908 with VLEN 128/256 configurations.

## Key Claims

- Version 1.0 of the RISC-V Vector Extension is frozen and undergoing public review.
- Prior stable releases include v0.8 and v0.7.1, with source available in the riscvarchive/riscv-v-spec repository.
- The specification is written in AsciiDoc (v-spec.adoc) and can be rendered with asciidoctor.
- Spike and the RISC‑V Proxy Kernel support v1.0 binaries; riscvOVPsim supports v0.9, v0.8, and v0.7.1.
- Hardware cores such as XuanTie C908 implement the extension, configurable with VLEN 128 or 256.

## Relationships

- [[xuantie_c908]] – implements RVV 1.0 with configurable VLEN.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]] – uses RVV intrinsics for GEMM code generation.
- [[rvv-lite]] – a reduced, area-optimized subset of this specification proposed for resource-constrained IoT devices.
- [[rvv_intrinsic_spec]] – the companion C intrinsic API specification that exposes this ISA to software.

## Sources

- https://github.com/riscvarchive/riscv-v-spec
