---
cold_start: true
created: 2026-06-27
inbound_links: 2
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.theregister.com/special-features/2025/12/10/qualcomm-takes-risc-on-arm-alternative-with-ventana-buy/2292187
- https://www.theregister.com/2025/01/02/riscv_journey_to_mainstream
- https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/
tags: []
type: entity
updated: 2026-06-27
---

# Qualcomm RISC-V AI

Qualcomm has emerged as a stealth major in the RISC-V ecosystem, having shipped approximately 650 million RISC-V cores to date as microcontroller units embedded within Snapdragon SoCs — a practice dating back to the Snapdragon 865 in 2019. These are not application-class cores but deeply embedded MCUs handling power management, sensor fusion, and peripheral control. Qualcomm's RISC-V strategy escalated dramatically in December 2025 with the acquisition of Ventana Micro Systems, a startup specializing in high-performance RISC-V CPU chiplets. Ventana's Veyron V2 design features up to 32 RVA23-compatible cores at 3.85 GHz with 512-bit vector units and a custom matrix math accelerator delivering 0.5 TOPS INT8/GHz/core, while the next-generation Veyron V3 targets 4.2 GHz with FP8 support. Qualcomm has stated it will develop Arm (Oryon) and RISC-V CPU cores in parallel, positioning RISC-V as both a strategic hedge against Arm legal disputes and a genuine architectural alternative. In wearables, Qualcomm and Google announced in 2023 a co-developed open-source RISC-V Snapdragon Wear platform, with a new SoC confirmed for 2025 targeting week-long battery life and on-device LLM inference (1–3B parameter models). The on-device AI push spans Snapdragon 8 Elite (mobile), Snapdragon X Series (PCs with Copilot+ NPU), automotive Digital Chassis, and industrial IoT edge appliances.

## Key Claims

- Qualcomm has shipped approximately 650 million RISC-V cores as embedded MCUs inside Snapdragon SoCs, making it one of the largest RISC-V shippers by volume despite minimal public RISC-V branding.
- Ventana's Veyron V2 chiplet achieves 3.85 GHz across 32 RVA23-compatible RISC-V cores with 512-bit RVV 1.0 vector units and a custom matrix accelerator rated at 0.5 TOPS INT8/GHz per core, with 128 MB shared L3 cache.
- Qualcomm confirmed in 2025 that a new RISC-V-based Snapdragon Wear SoC is under development with Google, targeting week-long battery life and local inference of 1–3B parameter LLMs on smartwatches.
- The Qualcomm AI Engine combines custom NPU, CPU, and GPU blocks — on the Snapdragon 8 Elite (2024) this runs multimodal generative AI locally, and DeepSeek R1-distilled models were ported within days of release.
- Qualcomm's parallel Arm (Oryon) and RISC-V development strategy was publicly confirmed after the Ventana acquisition, with RISC-V positioned for both datacenter and edge inference roles starting from 2026.
- Google removed RISC-V support from the Android Generic Kernel Image (GKI) in mid-2024 but states continued commitment to RISC-V long-term, creating uncertainty for the Snapdragon Wear RISC-V platform's software ecosystem.

## Relationships

- [[ventana_veyron_v2]]: Ventana's Veyron V2 is now a Qualcomm asset post-acquisition, and its chiplet architecture directly informs Qualcomm's RISC-V datacenter strategy.
- [[sifive_intelligence_x280]]: Qualcomm's embedded RISC-V MCU usage parallels SiFive's lower-end core deployments, while the Ventana acquisition pushes Qualcomm into the high-performance segment where SiFive P870 competes.
- [[tenstorrent_tt_ascalon]]: Both Tenstorrent and Qualcomm (via Ventana) are pursuing RISC-V-based AI accelerator strategies, representing competing visions for how RISC-V integrates into AI silicon.
- [[risc_v_vector_extension]]: The RVA23 profile ratification in October 2024 mandates RVV 1.0 and provides the software compatibility baseline that Ventana's Veyron V2 (and Qualcomm's subsequent designs) target.

## Sources

- https://www.theregister.com/special-features/2025/12/10/qualcomm-takes-risc-on-arm-alternative-with-ventana-buy/2292187
- https://www.theregister.com/2025/01/02/riscv_journey_to_mainstream
- https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/
