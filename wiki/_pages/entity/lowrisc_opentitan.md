---
type: entity
tags:
  - risc-v
  - security
  - root-of-trust
  - open-hardware
  - lowrisc
  - google
sources:
  - https://opentitan.org/
  - https://github.com/lowRISC/opentitan
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.75
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.5
  hub_potential: 0.45
---

# LowRISC OpenTitan

OpenTitan is an open-source silicon root of trust (RoT) project led by lowRISC CIC, producing the first open-source hardware security chip to reach production silicon tape-out. It uses the RISC-V Ibex core—a 32-bit, 2-stage in-order pipeline developed at ETH Zurich—as its main processor, running cryptographic key management, secure boot verification, and attestation firmware. OpenTitan achieved its first silicon tape-out on TSMC 40 nm in 2023, making it the first transparently auditable RoT to move from RTL to fabricated silicon with a fully open design. The project is a consortium effort with partners including Google (primary sponsor and integrator), Western Digital, Nuvoton Technology, Microsoft, ETH Zurich, Seagate, and G+D Mobile Security. Google deploys OpenTitan-derived silicon in its data center server hardware as a replacement for closed-source Titan security chips. Unlike traditional RoT solutions (e.g., TPM 2.0, Google Titan), OpenTitan publishes its complete RTL, firmware, and verification suite under Apache 2.0, enabling third parties to audit and extend the security design—a critical property for supply-chain trust in AI infrastructure.

## Key Claims

- OpenTitan achieved first silicon tape-out at TSMC 40 nm in 2023, becoming the first open-source silicon root of trust to transition from RTL to fabricated silicon.
- The chip uses the RISC-V Ibex core (RV32IMC, 2-stage pipeline), originally developed at ETH Zurich and contributed to the open-source community.
- Consortium partners include Google, Western Digital, Nuvoton, Microsoft, ETH Zurich, Seagate, and G+D Mobile Security; Google is the primary integrator in production data center hardware.
- Complete RTL, firmware, and verification suite are published under Apache 2.0, enabling public security audits—unlike proprietary RoT chips (Infineon SLB, Microchip ATECC).
- OpenTitan provides secure boot, cryptographic key management, runtime integrity measurement, and remote attestation functions for server-class hardware.
- Distinct from the lowrisc_riscv_llvm project (LLVM toolchain work); OpenTitan is a complete SoC product including hardware, firmware, and cryptographic library stack.

## Relationships

- [[lowrisc_riscv_llvm]] — Separate lowRISC project focusing on RISC-V LLVM toolchain; OpenTitan uses this toolchain for Ibex firmware compilation.
- [[risc_v_architecture]] — OpenTitan's Ibex core implements RV32IMC; part of the RISC-V security use-case ecosystem.
- [[western_digital_swerv_core]] — Western Digital is an OpenTitan consortium partner, connecting open RISC-V CPU and open RISC-V security silicon efforts.

## Sources

- OpenTitan project website: https://opentitan.org/
- OpenTitan GitHub repository: https://github.com/lowRISC/opentitan
- lowRISC CIC blog: OpenTitan silicon tape-out announcement (2023)
- Google Open Source Blog: OpenTitan production deployment notes
