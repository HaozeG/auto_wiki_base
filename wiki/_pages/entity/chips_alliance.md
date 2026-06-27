---
type: entity
tags: [risc-v, open-source, governance, ecosystem, Linux-Foundation, EDA, hardware]
sources:
  - https://www.chipsalliance.org/workgroups/
  - https://www.chipsalliance.org/about/governance/
  - https://www.chipsalliance.org/news/risc-v-international-omnixtend-working-group/
  - https://www.chipsalliance.org/news/2026-vision/
  - https://www.chipsalliance.org/news/chips-alliance-welcomes-the-caliptra-open-source-root-of-trust-project/
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# CHIPS Alliance

The CHIPS Alliance is an open-source hardware consortium organized as a directed fund of The Linux Foundation (a 501(c)(6) non-profit). Its mission is to develop and maintain high-quality open-source hardware IP and chip design tooling, with a strong emphasis on RISC-V cores, SoC infrastructure, and EDA tools. Governance is divided between a Governing Board (policy, membership agreements) and a Technical Advisory Council (TAC) that oversees Technical Projects; similar projects are grouped into Workgroups. Key workgroups include: Chisel (hardware design language; FPGA/ASIC rapid prototyping for ML and video), Interconnect (open networking protocols for cache-coherent messaging between RISC-V cores, accelerators, and memory controllers), Rocket Chip (pipelined RISC-V SoC generator using Chisel and Diplomacy meta-repository), and SystemVerilog Tools (open-source simulation, synthesis, linting). A notable security project is Caliptra — an open-source silicon Root of Trust (RoT) macro that embeds the VeeR RISC-V core (Apache 2.0 license) and reached version 2.1 RTL with OCP LOCK integration and post-quantum cryptographic capabilities. CHIPS Alliance and RISC-V International co-manage an OmniXtend working group targeting an open cache-coherent unified memory standard for multi-core RISC-V architectures. As of the 2026 vision statement, CHIPS Alliance priorities include AI acceleration infrastructure and post-quantum security standards.

## Key Claims

- CHIPS Alliance is a directed fund of The Linux Foundation; Platinum Members each hold a TAC seat.
- Caliptra open-source Root of Trust (v2.1) embeds VeeR RISC-V core (Apache 2.0); includes post-quantum crypto.
- OmniXtend WG (joint with RISC-V International): open cache-coherent unified memory standard for RISC-V multi-core.
- Chisel Workgroup maintains the hardware design language used by BOOM, Rocket Chip, and Gemmini at UC Berkeley.
- Rocket Chip Workgroup provides the meta-repository for Chisel-based RISC-V SoC generation (Diplomacy framework).
- VeeR RISC-V core family is embedded in Caliptra and fully open-sourced under Apache 2.0.
- 2026 priorities include AI acceleration infrastructure and post-quantum security standardization.

## Relationships

- [[boom_riscv]]: BOOM uses Chisel (CHIPS Alliance Chisel WG) and Rocket Chip infrastructure for its SoC generator.
- [[gemmini]]: Gemmini uses Chisel and attaches via RoCC within the Rocket Chip/CHIPS Alliance ecosystem.
- [[ara_vector_processor]]: Ara uses Chisel for RTL design, connecting to the broader CHIPS Alliance open hardware community.
- [[xiangshan_riscv]]: XiangShan also uses Chisel; represents a parallel open-source community (ICT-CAS) outside CHIPS Alliance.

## Sources

- https://www.chipsalliance.org/workgroups/
- https://www.chipsalliance.org/about/governance/
- https://www.chipsalliance.org/news/risc-v-international-omnixtend-working-group/
- https://www.chipsalliance.org/news/2026-vision/
- https://www.chipsalliance.org/news/chips-alliance-welcomes-the-caliptra-open-source-root-of-trust-project/
