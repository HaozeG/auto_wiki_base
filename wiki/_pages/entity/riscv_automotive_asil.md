---
cold_start: false
created: 2026-06-27
inbound_links: 1
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.globenewswire.com/en/news-release/2022/02/15/2385494/0/en/Andes-Technology-Is-the-First-RISC-V-Vendor-to-Accomplish-ISO-26262-Functional-Safety-ASIL-D-Development-Process-Certification-with-SGS-TU%CC%88V-Saar.html
- https://www.andestech.com/en/2025/01/23/andes-technology-d45-se-processor-achieves-iso-26262-asil-d-certification-for-functional-safety/
- https://hightec-rt.com/news/blog/item/andes-hightec-risc-v
- https://www.edge-ai-vision.com/2025/09/andes-technology-announces-d23-se-a-functional-safety-risc-v-core-with-dcls-and-split-lock-for-asil-b-d-automotive-applications/
tags:
- risc-v
- automotive
- ISO-26262
- ASIL-D
- functional-safety
- andes
- certified
type: entity
updated: 2026-06-27
---

# RISC-V in Automotive AI (ASIL-D Certification)

RISC-V is entering automotive safety-critical applications through a growing family of ISO 26262 certified processor cores, with Andes Technology being the first RISC-V IP vendor to achieve both hardware (ISO 26262-5) and software (ISO 26262-6) ASIL-D process certification from SGS-TÜV Saar in 2022. ISO 26262 is the international standard for functional safety in road vehicles, with ASIL-D representing the highest safety integrity level required for systems such as autonomous driving, braking, and steering. RISC-V's open ISA is attractive for automotive because OEMs and Tier-1 suppliers can verify the complete instruction set specification, avoiding the opacity of proprietary ISAs. Andes' Safety Enhanced (SE) core series — including the D23-SE (streamlined, ASIL-D) and D45-SE (high-performance, ASIL-D) — implement hardware features such as Dual-Core Lockstep (DCLS) and Split-Lock mode to meet redundancy requirements mandated by ASIL-D.

## Key Claims

- Andes Technology was the first RISC-V processor IP vendor to receive ASIL-D certification for both hardware (ISO 26262-5) and software (ISO 26262-6) in February 2022, certified by SGS-TÜV Saar.
- Andes D45-SE processor achieved ISO 26262 ASIL-D product certification in January 2025, enabling direct deployment in automotive ASICs without additional safety arguments.
- Andes D23-SE features Dual-Core Lockstep (DCLS) and Split-Lock mode, the two primary hardware redundancy mechanisms required for ASIL-D automotive applications.
- Andes' Safety Enhanced (SE) series spans ASIL-B (N25F-SE, D25F-SE) and ASIL-D (D23-SE, D45-SE) processor variants for different automotive sub-systems.
- HighTec GmbH provides an ASIL-D-certified C/C++ compiler suite targeting Andes RISC-V cores, completing the certified toolchain required for ISO 26262 workflows.
- TASKING, Andes, and MachineWare collaborated on a toolchain ecosystem to accelerate RISC-V ASIL compliant automotive silicon development.
- The upcoming Andes 60-SE series targets Advanced Driver Assistance Systems (ADAS) and In-Vehicle Infotainment (IVI), extending ASIL certification to higher-performance RISC-V cores.

## Relationships

- [[andes_ax45mp_nx27v]]: The AX45MP and NX27V are general-purpose AI-edge Andes cores; the SE series are the automotive safety variants with ASIL certification.
- [[nuclei_ux900_n900]]: Nuclei also targets automotive with RISC-V cores, though as of 2024 Andes holds the first ASIL-D product certification in the RISC-V ecosystem.
- [[risc_v_profiles_rva]]: RVA profiles define software compatibility; automotive ASIL certification is an orthogonal hardware/process quality dimension.
- [[qualcomm_riscv_ai]]: Qualcomm's automotive Snapdragon chips incorporate RISC-V MCUs for sensor fusion and safety monitoring alongside the main application processor.

## Sources

- https://www.globenewswire.com/en/news-release/2022/02/15/2385494/0/en/Andes-Technology-Is-the-First-RISC-V-Vendor-to-Accomplish-ISO-26262-Functional-Safety-ASIL-D-Development-Process-Certification-with-SGS-TU%CC%88V-Saar.html
- https://www.andestech.com/en/2025/01/23/andes-technology-d45-se-processor-achieves-iso-26262-asil-d-certification-for-functional-safety/
- https://hightec-rt.com/news/blog/item/andes-hightec-risc-v
- https://www.edge-ai-vision.com/2025/09/andes-technology-announces-d23-se-a-functional-safety-risc-v-core-with-dcls-and-split-lock-for-asil-b-d-automotive-applications/
