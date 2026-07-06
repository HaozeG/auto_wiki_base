---
canonical_name: Zicond
aliases:
- zicond extension
- experimental-zicond
- Zicond (RISC-V extension)
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/23acb8eb8c3d2c4a.md
- https://reviews.llvm.org/D146946
source_url: https://reviews.llvm.org/D146946
fetched_at: '2026-07-06T02:34:59.745437+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c910v2-hardware-target
  reason: The XuanTie C910V2 core lists Zicond among its supported RISC-V standard
    Z extensions, making it a target for this conditional instruction extension
---

# Zicond

The Zicond extension is a RISC-V instruction-set extension providing conditional operations (such as conditional moves) that was added to LLVM as an experimental extension based on the 1.0-rc1 draft specification. The extension is gated by the `-menable-experimental-extensions` flag and the march string component `_zicond1p0`. When enabled, LLVM defines the preprocessor macro `__riscv_zicond` with value 1000000 (representing version 1.0.0). The MC layer support includes assembling and disassembling the Zicond instructions, defined in the new tablegen file `RISCVInstrInfoZicond.td` as part of the LLVM 17 development cycle. The extension is considered experimental until ratified, and version numbering is not incremented between release candidates, following LLVM policy for pre-ratification extensions.

## Key Claims

- Zicond adds conditional operation instructions to the RISC-V ISA.
- LLVM implements Zicond as an experimental extension based on the 1.0-rc1 draft specification.
- The extension is enabled by the `-march=rv32i_zicond1p0` or `rv64i_zicond1p0` string with `-menable-experimental-extensions`.
- When enabled, the preprocessor defines `__riscv_zicond` as 1000000.
- The MC layer (assembler/disassembler) support was added in LLVM commit rGd3291c692c0a.
- The extension is documented in LLVM's RISCVUsage.rst with the same spec reference.

## Relationships

- [[xuantie-c910v2-hardware-target]]: The XuanTie C910V2 core lists Zicond among its supported RISC-V standard Z extensions, making it a target for this conditional instruction extension.

## Sources

- https://reviews.llvm.org/D146946
