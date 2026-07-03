---
canonical_name: XuanTie MME
aliases:
- XuanTie Matrix Multiply Extension
- MME
- XuanTie MME instruction set
subtype: null
tags: []
scorecard:
  novelty_delta: 1.0
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/245f22b2458bcdae.md
- https://riscv.org/blog/xuantie-matrix-multiply-extension-instructions/
source_url: https://riscv.org/blog/xuantie-matrix-multiply-extension-instructions/
fetched_at: '2026-07-03T13:32:39.651493+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# XuanTie MME

The XuanTie Matrix Multiply Extension (MME) is an independent instruction set extension proposed by T-Head for the RISC-V architecture to accelerate matrix multiplication operations required by AI workloads. Unlike Arm's Scalable Matrix Extension (SME), x86's Advanced Matrix Extensions (AMX), or Power's Matrix-Multiply Assist (MMA), XuanTie MME is designed as a completely separate extension decoupled from vector extensions, offering independent matrix register files and programming models. This design allows flexibility across different market segments including cloud, data center, consumer, and IoT devices. The extension introduces eight 2D matrix registers with configurable row length (MLEN) that scales computing power, and supports multiple integer and floating-point data types including int4, int8, fp16, bf16, and fp32. Two primary instruction types are defined: mmaqa for integer multiply-accumulate and fmmacc for floating-point multiply-accumulate operations. The independent programming model aims to simplify developer experience by eliminating the need to coordinate vector and matrix register reuse, while also simplifying hardware implementation and thermal design.

## Key Claims

- XuanTie MME is an independent matrix extension decoupled from vector extensions.
- The independent design provides flexibility across cloud, data center, consumer, and IoT markets.
- Developers need not master both vector and matrix extensions for network optimization, reducing development threshold.
- Hardware implementation benefits from simplified timing and layout optimization.
- Thermal design is eased by separating heat generation from vector and matrix operations.
- XuanTie MME adds eight 2D matrix registers with row length MLEN (power of 2, e.g., 128, 256 bits).
- Number of rows in a matrix register is MLEN/32; columns vary with element bit width (e.g., 4×4 32-bit entries for MLEN=128).
- Data types supported: int4, int8, int16, int32, fp16, bf16, fp32.
- Integer multiply-accumulate instruction: mmaqa.
- Floating-point multiply-accumulate instruction: fmmacc (with variants .h, .b for half-precision, .s for single-precision).
- Matrix registers are used for both source and destination; no separate accumulation registers.
- Data interaction between vector and matrix extensions is via memory operations only.
- Dirty Flags mechanism saves only used registers during thread switching to reduce performance loss.

## Relationships

No specific relationships to existing wiki pages are established by this source.

## Sources

- https://riscv.org/blog/xuantie-matrix-multiply-extension-instructions/
