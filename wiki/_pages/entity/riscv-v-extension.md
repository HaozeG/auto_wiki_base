---
canonical_name: RISC-V V Extension
aliases:
- RVV
- RISC-V Vector Extension
- V extension
- CORE-V
- CORE-V Family
- OpenHW CORE-V
- CORE-V cores
- RVV Bench
- camel-cdr/rvv-bench
- rvv-bench
- RISC-V Vector benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.4
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.8
sources:
- raw/cache/0f909339888951bc.md
- https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
- raw/cache/a71b0e3b12c36de7.md
- https://github.com/openhwgroup/core-v-cores
- raw/cache/282a556eaea822f1.md
- https://github.com/camel-cdr/rvv-bench
source_url: https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
fetched_at: '2026-07-03T15:51:28.357627+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# RISC-V V Extension

The RISC-V Vector Extension (RVV) is the standard instruction set extension for vector processing in the RISC-V ISA, providing data-level parallelism for compute-intensive workloads. Version 1.0 of the specification has been frozen by RISC-V International and is undergoing public review, marking a stable baseline for hardware and software implementations. The extension defines 32 vector registers (v0–v31) with a configurable vector length (VLEN), along with instructions for arithmetic, memory access (unit-stride, strided, and indexed), reductions, and masking. The specification evolves through the riscv-v-spec GitHub repository, which hosts working drafts and release candidates such as v1.0-rc1 and v1.0-rc2. RVV is designed to support a wide range of microarchitectures, from tiny embedded cores to high-performance out-of-order implementations, and forms the foundation for further vector and matrix extensions like Zve (embedded) and Zvfh (half-precision floating-point).

## Key Claims

- The RISC-V Vector Extension (RVV) version 1.0 has been frozen and is undergoing public review as part of the RISC-V International ratification process.
- The specification defines 32 vector registers (v0–v31) with a configurable vector length (VLEN).
- RVV includes instructions for arithmetic, memory access (unit-stride, strided, indexed), reductions, and masking.
- The specification is developed in the open-source riscv-v-spec GitHub repository, with release candidates v1.0-rc1 and v1.0-rc2 preceding the v1.0 frozen release.

## Relationships

No specific relationships to visible context pages are evident from the source content.

## Sources

- https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
- https://github.com/riscvarchive/riscv-v-spec
