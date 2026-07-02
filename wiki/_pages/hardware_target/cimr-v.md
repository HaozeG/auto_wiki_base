---
canonical_name: CIMR-V
aliases:
- CIMR-V Accelerator
- CIMR-V CIM Accelerator
subtype: null
tags: []
hardware_targets:
- CIMR-V
toolchains: []
constraints:
- PULPissimo platform
- ibex 32-bit 2-stage RISC-V architecture
- 512Kb SRAM-based CIM unit
- 256Kb feature map SRAM
- 512Kb weight SRAM
- CIM layer fusion support
- convolution/max pooling pipeline
scorecard:
  novelty_delta: 0.6
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/529d9c9da89f90a1.md
- https://www.semanticscholar.org/paper/CIMR-V:-An-End-to-End-SRAM-based-CIM-Accelerator-AI-Guo-Chang/9a55bcd747b501ceb54f82dc3349745d5e4062cc
source_url: https://www.semanticscholar.org/paper/CIMR-V:-An-End-to-End-SRAM-based-CIM-Accelerator-AI-Guo-Chang/9a55bcd747b501ceb54f82dc3349745d5e4062cc
fetched_at: '2026-07-02T12:35:44.663016+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# CIMR-V

CIMR-V is an end-to-end SRAM-based Computing-in-Memory (CIM) accelerator tightly coupled with a RISC-V core, designed for energy- and area-efficient AI inference at the edge. The accelerator is implemented on the PULPissimo platform, featuring the ibex 32-bit 2-stage RISC-V architecture. It integrates a 512Kb SRAM-based CIM unit for highly parallel computing with minimal data movement, a modified RISC-V core for control and high-precision computation, instruction memory, a 256Kb feature map SRAM for layer fusion, and a 512Kb weight SRAM for weight fusion. Three key architectural optimizations distinguish CIMR-V: CIM layer fusion, which reduces data movement between layers; a convolution/max pooling pipeline that overlaps operations; and weight fusion that combines weights to minimize memory accesses. These optimizations target latency and energy efficiency for AI workloads such as keyword spotting. The accelerator operates in two distinct modes (not further specified in the available source), and its CIM input buffer uses a 32-bit shift design to reduce routing complexity and power consumption.

## Key Claims

- CIMR-V integrates a 512Kb SRAM-based CIM unit with a RISC-V core on the PULPissimo platform, enabling end-to-end model inference.
- The accelerator incorporates CIM layer fusion, convolution/max pooling pipeline, and weight fusion to reduce data movement.
- CIMR-V achieves an 85.14% reduction in latency for a keyword spotting AI model compared to a baseline without these optimizations.
- The CIM input buffer uses a 32-bit shift design to reduce routing complexity and power consumption.

## Optimization-Relevant Details

- ISA/profile: RISC-V (ibex 32-bit 2-stage)
- Vector/matrix/accelerator support: SRAM-based CIM unit (non-vector)
- Memory/cache/TLB/DMA: 512Kb CIM unit, 256Kb feature map SRAM, 512Kb weight SRAM
- Compiler/toolchain support: Not specified (likely PULPissimo SDK)

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both are RISC-V AI accelerator optimizations; Gemmini uses systolic arrays while CIMR-V uses SRAM-based CIM.
- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets vector memory access in RISC-V, complementing CIMR-V's memory-centric architecture.
- Insufficient context for additional cross-links; no existing entity pages for CIM accelerators or PULPissimo are present in the wiki.

## Sources

- [CIMR-V: An End-to-End SRAM-based CIM Accelerator with RISC-V for AI Edge Device](https://www.semanticscholar.org/paper/CIMR-V:-An-End-to-End-SRAM-based-CIM-Accelerator-AI-Guo-Chang/9a55bcd747b501ceb54f82dc3349745d5e4062cc)
