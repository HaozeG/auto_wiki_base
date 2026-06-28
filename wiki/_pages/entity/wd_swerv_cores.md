---
cold_start: false
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://riscv.org/blog/what-is-swerv-core-eh2/
- https://blog.westerndigital.com/risc-v-data-centric-architectures-swerv-cores/
- https://antmicro.com/blog/2020/07/swerv-cores-tools-ecosystem
- https://github.com/westerndigitalcorporation/swerv_eh1
tags:
- risc-v
- open-source
- processor
- embedded
- storage
- chips-alliance
type: entity
updated: 2026-06-27
---

# Western Digital SweRV Cores (EH1 / EH2 / EL2)

Western Digital's SweRV (Storage-Wear-Leveling-RISC-V) core family comprises three open-source 32-bit RISC-V processors designed originally for use in Western Digital's own NVMe SSDs and flash storage controllers, then released to the CHIPS Alliance as open-source IP under the Apache 2.0 license in 2019–2020. The EH1 is a 2-way superscalar, 9-stage pipeline RV32IMC core optimized for high single-thread throughput in storage firmware. The EH2 extends EH1 with simultaneous dual-thread support, achieving up to 6.3 CoreMark/MHz in TSMC 16nm at a footprint of 0.067 mm², making it the first dual-threaded commercial RISC-V core at time of release (2020). The EL2 is a lower-area, 4-stage single-issue RV32IMC pipeline targeting 3.6 CoreMark/MHz for medium-performance embedded tasks. Western Digital's broader roadmap also included a 64-bit multi-core EHX3 for data-center storage, though the EHX3 was not open-sourced. The SweRV family demonstrated that a hyperscale storage vendor could drive RISC-V adoption from within its own supply chain and validate the ISA at volume before broader commercial silicon.

## Key Claims

- SweRV EH1 is a 32-bit, 2-way superscalar, 9-stage pipeline RV32IMC core open-sourced via CHIPS Alliance in 2019.
- SweRV EH2 adds dual-thread support and achieves 6.3 CoreMark/MHz in 16nm TSMC with a 0.067 mm² footprint.
- SweRV EH2 was described as the first dual-threaded commercial RISC-V core at its 2020 release.
- SweRV EL2 uses a 4-stage single-issue pipeline and targets 3.6 CoreMark/MHz for medium-power embedded use.
- All three 32-bit cores are available on the CHIPS Alliance GitHub under the Apache 2.0 license.
- Western Digital announced a goal of shipping 1 billion RISC-V cores across its product portfolio.

## Relationships

- [[chips_alliance_governance]]: SweRV EH1/EH2/EL2 are hosted and stewarded by CHIPS Alliance under Linux Foundation.
- [[risc_v_profiles_rva]]: SweRV targets RV32IMC, predating the RVA profile series which focuses on 64-bit application-class profiles.
- [[boom_riscv]]: Both SweRV and BOOM are open-source RISC-V cores; BOOM targets OoO server workloads while SweRV targets embedded storage.

## Sources

- https://riscv.org/blog/what-is-swerv-core-eh2/ (EH2 architecture details, CoreMark/MHz, footprint)
- https://blog.westerndigital.com/risc-v-data-centric-architectures-swerv-cores/ (WD RISC-V strategy, 1B core goal)
- https://antmicro.com/blog/2020/07/swerv-cores-tools-ecosystem (open-source tooling for SweRV)
- https://github.com/westerndigitalcorporation/swerv_eh1 (EH1 source code)
