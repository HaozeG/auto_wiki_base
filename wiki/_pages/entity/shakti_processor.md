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
- https://shakti.org.in/tapeout.html
- https://www.open-electronics.org/shakti-risc-v-based-processor-the-first-open-source-indian-chip/
- https://abopen.com/news/an-overview-of-shakti-processor-program/
- https://journal.accsindia.org/show.article.php?id=64
- https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-isro-jointly-developed-and-successfully-booted
tags:
- risc-v
- open-source
- processor
- India
- IIT-Madras
- embedded
- BSV
type: entity
updated: 2026-06-27
---

# Shakti Processor Project

The Shakti Processor Project is an open-source RISC-V processor initiative launched in 2014 by the Reconfigurable Intelligent Systems Engineering (RISE) Group at IIT Madras, funded by the Indian Ministry of Electronics and Information Technology. It is India's first indigenous open-source processor ecosystem, aiming to deliver a complete family of six processor classes spanning IoT microcontrollers through server-grade multi-core designs. All IP is written in Bluespec SystemVerilog (BSV), a high-level hardware description language, and licensed under the 3-Clause BSD License. The C-class core — the most mature in the family — implements RV64IMAFD (ISA user spec 2.2, privilege spec 1.10, sv39 supervisor), is a 5-stage in-order pipeline, and was fabricated on Intel's 22 nm FinFET process in collaboration with Intel and HCL in 2017. A notable milestone came when IIT Madras and ISRO jointly developed and successfully booted a Shakti-based aerospace-quality semiconductor chip, demonstrating suitability for space and defense applications. The project has an educational and national-sovereignty mission: the first tapeout was designed by fewer than 15 students, and all components were fully open-sourced to build domestic chip design capability in India.

## Key Claims

- Six processor classes planned: E (IoT), C (embedded Linux), I (mobile/IoT), M (server), S (storage), H (HPC).
- C-class: RV64IMAFD, 5-stage in-order, sv39 virtual memory, fabricated in Intel 22 nm FinFET (2017).
- All source code written in Bluespec SystemVerilog (BSV); licensed under 3-Clause BSD.
- First tapeout designed by fewer than 15 students at IIT Madras.
- IIT Madras + ISRO joint Shakti chip for aerospace applications successfully booted.
- Funded by the Indian Ministry of Electronics and Information Technology.
- Project initiated in 2014; first C-class silicon in 2017.

## Relationships

- [[boom_riscv]]: BOOM (UC Berkeley) and Shakti (IIT Madras) are parallel national academic open-source RISC-V core projects.
- [[openhw_cva6]]: CVA6 (OpenHW/ETH Zürich) is a comparable open-source Linux-capable RISC-V application core.
- [[xiangshan_riscv]]: XiangShan (ICT-CAS China) and Shakti (IIT Madras India) represent national open-source RISC-V processor programs.

## Sources

- https://shakti.org.in/tapeout.html
- https://www.open-electronics.org/shakti-risc-v-based-processor-the-first-open-source-indian-chip/
- https://abopen.com/news/an-overview-of-shakti-processor-program/
- https://journal.accsindia.org/show.article.php?id=64
- https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-isro-jointly-developed-and-successfully-booted
