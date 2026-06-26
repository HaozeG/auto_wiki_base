---
type: entity
tags: [geopolitics, export-controls, nvidia, amd, huawei, china, semiconductor-policy]
sources:
  - https://www.bis.doc.gov/index.php/documents/about-bis/newsroom/press-releases/3081-2022-10-07-bis-press-release-advanced-computing-and-semiconductor-manufacturing-controls-final/file
  - https://www.federalregister.gov/documents/2023/10/25/2023-23052/export-controls-on-advanced-computing-items-supercomputer-and-semiconductor-end-use-end-user-and
  - https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion
  - https://www.reuters.com/technology/nvidia-expects-2-billion-quarterly-revenue-loss-new-us-export-curbs-2023-10-17/
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AI Chip Export Controls

AI chip export controls are a set of United States government regulations administered by the Bureau of Industry and Security (BIS) within the Department of Commerce that restrict the sale and transfer of high-performance computing semiconductors and related manufacturing equipment to designated countries, primarily the People's Republic of China. The policy framework uses a performance threshold model: chips whose total processing performance (TPP) and interconnect bandwidth density together exceed specified values require export licenses that are presumed to be denied for Chinese end-users. The first major rule took effect in October 2022, immediately restricting NVIDIA A100 and H100 GPUs and AMD MI250X from export to China without a license. In October 2023, BIS expanded the controls to close loopholes exploited by NVIDIA's A800 and H800 — downclocked China-market variants designed to sit just below the original performance thresholds — by adding an interconnect bandwidth density parameter to the threshold calculation. In January 2025, BIS published the "Diffusion Rule," a tiered global framework dividing countries into three tiers with differentiated licensing requirements, closing country-of-destination arbitrage that allowed chips to reach China via third-country intermediaries. The cumulative effect of these rules has restructured the global AI semiconductor market: NVIDIA estimated it would lose approximately $5.5 billion in revenue from the October 2023 update alone, with total China revenue impact across 2023–2024 estimated at roughly $17 billion, while China has accelerated domestic alternatives including Huawei's Ascend 910B accelerator and investment in SMIC's N+2 (7 nm-class) process.

## Key Claims

- The **October 2022 BIS rule** imposed export restrictions on chips with total processing performance (TPP) exceeding 4,800 TOPS at FP16 or with performance-to-bandwidth density ratios above a defined threshold, immediately covering the NVIDIA A100 (312 TFLOPS at FP16) and H100 (989 TFLOPS at FP16) and the AMD MI250X.
- NVIDIA designed the **A800 and H800** as restricted-market variants by capping NVLink interconnect bandwidth from 600 GB/s (H100) to 400 GB/s, placing them just below the October 2022 bandwidth-density threshold; the **October 2023 update** explicitly added a total chip-to-chip transfer rate parameter that covered these variants within days of publication.
- The **October 2023 rule** also introduced a performance density metric combining TOPS with interconnect bandwidth density (measured in Gbps/mm²) to prevent future threshold-straddling designs; NVIDIA's H20, a further-downclocked China variant, was permitted under these rules until April 2025, when BIS added H20 to the control list.
- NVIDIA disclosed in its October 2023 quarterly filing that the new rules would result in approximately **$5.5 billion in revenue charges** from export-controlled A800/H800 inventory; independent analyst estimates place total forgone China datacenter revenue across 2023–2024 at approximately **$15–17 billion**.
- AMD faced similar restrictions on its **MI300X** (5.2 TB/s HBM3 bandwidth, ~1,300 TFLOPS at FP16), which was added to the control list in the October 2023 update alongside a broader set of datacentre accelerators.
- China's domestic response centres on **Huawei Ascend 910B**, which delivers approximately 256–320 TFLOPS at FP16 using Huawei's 910B die fabricated at SMIC's **N+2 node** (an approximately 7 nm-class process without EUV lithography); production yields at SMIC N+2 were estimated at 20–30% in 2023–2024 compared to ~80%+ for TSMC N5, constraining Ascend supply.
- The **January 2025 Diffusion Rule** (Framework for AI Diffusion) divides all countries into Tier 1 (18 close allies, unrestricted), Tier 2 (most of world, quantity caps without individual licenses), and Tier 3 (embargoed countries including China, Russia, Iran), closing arbitrage routes through Malaysia, the UAE, Singapore, and other third-country transshipment hubs previously used to supply Chinese end-users.
- BIS separately imposed **Foreign Direct Product Rule (FDPR)** extensions in October 2022 restricting SMIC from receiving semiconductor manufacturing equipment produced anywhere in the world using US technology if the equipment would produce chips for military end-uses or certain advanced logic — effectively blocking SMIC's path to EUV tools and constraining its N+2 node scaling.

## Relationships

- [[nvidia_hopper_h100]] — H100 was the primary target of the October 2022 rule; NVIDIA subsequently designed H800 as a compliant variant, which was then captured by the October 2023 update; H100 remains the de facto reference chip against which export thresholds are calibrated.
- [[nvidia_blackwell_b200]] — B200 (20 PFLOPS FP4, 8 TB/s HBM3e) substantially exceeds all current performance thresholds; no Blackwell variant is licensed for export to China as of 2026.
- [[amd_mi300x]] — Covered by October 2023 controls; AMD's MI300X China business was effectively eliminated by the rule update; AMD disclosed similar revenue exposure to NVIDIA in China datacenter markets.
- [[tsmc_n3_n2_process_node]] — TSMC is prohibited from manufacturing chips for Chinese customers at nodes below approximately 16 nm for advanced applications under the FDPR, reinforcing SMIC's role as China's only domestic advanced-node foundry.

## Sources

- BIS October 7, 2022 Final Rule — "Advanced Computing and Semiconductor Manufacturing Controls": https://www.bis.doc.gov/index.php/documents/about-bis/newsroom/press-releases/3081-2022-10-07-bis-press-release-advanced-computing-and-semiconductor-manufacturing-controls-final/file
- Federal Register October 25, 2023 — Updated Export Controls on Advanced Computing: https://www.federalregister.gov/documents/2023/10/25/2023-23052/export-controls-on-advanced-computing-items-supercomputer-and-semiconductor-end-use-end-user-and
- Federal Register January 15, 2025 — Framework for Artificial Intelligence Diffusion (Diffusion Rule): https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion
- Reuters: "Nvidia expects $2 billion quarterly revenue loss from new US export curbs" (October 2023): https://www.reuters.com/technology/nvidia-expects-2-billion-quarterly-revenue-loss-new-us-export-curbs-2023-10-17/
- SemiAnalysis: "Huawei Ascend 910B and SMIC N+2 yield analysis" (2024)
- CSET (Georgetown): "Export Controls on Semiconductors: Huawei's Response and China's Path Forward" (2023)
