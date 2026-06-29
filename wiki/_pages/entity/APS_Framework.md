---
cold_start: false
created: '2025-06-30'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.4
  hub_potential: 0.3
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://www.aspdac.com/aspdac2026/program/program-abstract.html
tags:
- RISC-V
- MLIR
- hardware-software co-design
- processor specialization
- EDA
type: entity
updated: '2026-06-28'
---

# APS Framework

APS (Agile Processor Specialization) is an MLIR-based hardware-software co-design framework for rapid development of RISC-V custom instruction extensions (ISAXs). It provides a unified set of open-source EDA tools that automate behavioral architecture description, hardware synthesis, processor-ISA adaptation, and compiler co-generation. APS leverages the Multi-Level Intermediate Representation (MLIR) to support these diverse tasks within a single infrastructure, enabling designers to navigate the complexities of RISC-V specialization with greater ease and efficiency. The framework addresses the challenge that existing RISC-V ecosystems often address manual customization without a fully automated and integrated solution, by offering a seamless flow from high-level specification to hardware implementation and compiler support.

## Key Claims

- APS provides a unified framework of powerful, open-source EDA tools for seamless hardware-software co-design of custom RISC-V instruction extensions.
- The framework is based on Multi-Level Intermediate Representation (MLIR), allowing it to support behavioral architecture description, hardware synthesis, processor-ISAX adaptation, and compiler co-generation in a unified infrastructure.
- APS aims to automate the processor specialization process, which traditionally involves complex interplay of multiple tasks and is often handled manually in existing RISC-V ecosystems.
- The platform is designed to empower designers with greater ease and efficiency in navigating the complexities of processor specialization for domain-specific applications.

## Relationships

- [[FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe]] – An alternative approach to RISC-V ISA extension using custom instructions for CNN acceleration, contrasting with the MLIR-based framework approach.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Another RISC-V optimization recipe on the GAP8 platform, representing a scratchpad-based parallelization method that could potentially benefit from the APS co-design flow.
- insufficient context for additional cross-links: Only two relevant specialized pages are available in the wiki context; additional entity pages would strengthen the relationship graph.

## Sources

- [ASP-DAC 2026 Program – Abstract for Tutorial 5 on APS](https://www.aspdac.com/aspdac2026/program/program-abstract.html)

