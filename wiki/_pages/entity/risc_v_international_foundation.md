---
type: entity
tags:
  - risc-v
  - governance
  - standards
  - open-source
  - isa
sources:
  - https://riscv.org/
  - https://riscv.org/technical/specifications/
  - https://riscv.org/membership/
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.72
  claim_density: 0.74
  self_containedness: 0.88
  bridge_score: 0.75
  hub_potential: 0.80
---

# RISC-V International Foundation

RISC-V International is the non-profit membership organization that owns, governs, and standardizes the RISC-V instruction set architecture (ISA). Founded in 2015 as the RISC-V Foundation and reincorporated as RISC-V International in Switzerland in 2020 (to prevent potential US export control restrictions on ISA participation), the organization manages the specification ratification process, working groups, and the open-source license under which RISC-V is distributed. As of 2024, RISC-V International has over 4,000 member organizations across 70+ countries, including founding members UC Berkeley, SiFive, Google, Nvidia, Qualcomm, Western Digital, and Alibaba. The organization operates a layered membership structure (Community, Silver, Gold, Premier, Strategic) where higher tiers gain voting rights on specifications and seats on the Technical Steering Committee (TSC). RISC-V specs are ratified through a multi-stage process: draft → public review → freeze → ratification, with the TSC approving each transition. The open ISA model means any company can implement RISC-V without royalties or license fees, which has made it the primary open alternative to ARM in embedded, automotive, HPC, and AI accelerator markets.

## Key Claims

- RISC-V International reincorporated in Switzerland in 2020 specifically to remove US-entity governance control and ensure global membership access, responding to US-China technology tensions.
- The organization has over 4,000 member organizations as of 2024, making it the largest open ISA standards body in the world by membership count.
- RISC-V specifications are released under a Creative Commons Attribution 4.0 International license, with implementations unrestricted by royalties or per-unit fees.
- The Technical Steering Committee (TSC) consists of representatives from Premier and Strategic members and approves new extension ratifications; working groups (e.g., Vector, Security, Hypervisor) develop drafts.
- Ratified profiles (RVA20, RVA22, RVA23, RVB23) allow software vendors to target a defined extension baseline rather than individual extension combinations, reducing fragmentation.
- RISC-V International hosts the RISC-V Software Ecosystem (RISE) project, a Linux Foundation initiative founded in 2023 with AMD, Google, Intel, Nvidia, Qualcomm, Red Hat, and Samsung to fund open-source RISC-V software development.
- The ISA spec separates "unprivileged" (user-mode) and "privileged" (supervisor/machine-mode) specifications; both are formally ratified and maintained under version control at github.com/riscv/riscv-isa-manual.

## Relationships

- [[rva23_profile]] — RVA23 is the latest ratified RISC-V Application profile, standardized by RISC-V International and targeting Linux-class 64-bit software stacks.
- [[rva20_rva22_profiles]] — Earlier ratified profiles from RISC-V International that established the Linux-capable RISC-V baseline before RVA23.
- [[rvb23_embedded_profile]] — RVB23 is RISC-V International's embedded/real-time profile for MCU and RTOS workloads.
- [[risc_v_vector_extension]] — The V extension was ratified by RISC-V International in 2021 (v1.0) after years of working group development.
- [[lowrisc_opentitan]] — OpenTitan implements the RISC-V privileged spec (machine mode only, with PMP) as specified by RISC-V International.

## Sources

- RISC-V International website: https://riscv.org/
- RISC-V membership page: https://riscv.org/membership/
- RISC-V technical specifications: https://riscv.org/technical/specifications/
- RISE project announcement (2023): https://riseproject.dev/
- RISC-V ISA manual repository: https://github.com/riscv/riscv-isa-manual
