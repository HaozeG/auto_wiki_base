---
type: entity
tags: [ai-accelerator, asic, microsoft, azure, inference, hbm, liquid-cooling]
sources:
  - https://techcommunity.microsoft.com/blog/azureinfrastructureblog/inside-maia-100-revolutionizing-ai-workloads-with-microsofts-custom-ai-accelerat/4229118
  - https://azure.microsoft.com/en-us/blog/azure-maia-for-the-era-of-ai-from-silicon-to-software-to-systems/
  - https://hc2024.hotchips.org/assets/program/conference/day2/81_HC2024.Microsoft.Xu.Ramakrishnan.final.v2.pdf
  - https://www.servethehome.com/microsoft-maia-100-ai-accelerator-for-azure/
  - https://newsletter.semianalysis.com/p/microsoft-infrastructure-ai-and-cpu
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

# Microsoft Azure Maia 100

The Microsoft Azure Maia 100 is a custom AI accelerator ASIC designed by Microsoft and manufactured by TSMC on their N5 (5 nm) process, announced in November 2023 and deployed in Azure datacenters from 2024 onward. With 105 billion transistors packed onto an 820 mm² reticle-limited die — the maximum area a single photolithography exposure can cover — Maia 100 is one of the largest monolithic AI chips produced at 5 nm. It is paired with four HBM2E stacks via TSMC's CoWoS-S 2.5D interposer packaging, delivering 64 GB of capacity and 1.8 TB/s of memory bandwidth. Peak dense BF16 tensor throughput is approximately 0.8 petaFLOPS (800 TFLOPS). The chip's vector processor implements a custom ISA supporting FP32, BF16, and INT8 data types. Maia 100 targets large-scale generative AI inference workloads on Azure, including Microsoft Copilot, Azure OpenAI Service, GitHub Copilot, and Bing, and was validated against GPT-3.5-Turbo workloads before deployment.

## Key Claims

- **105 billion transistors** on an 820 mm² die manufactured at TSMC N5 (5 nm), using CoWoS-S 2.5D interposer packaging to integrate four HBM2E die.
- **Memory subsystem**: 64 GB HBM2E capacity at 1.8 TB/s aggregate bandwidth; dense BF16 peak throughput is ~0.8 PFLOPS (800 TFLOPS).
- **Power envelope**: designed for up to 700 W TDP but rack-provisioned at 500 W in production deployments.
- **Custom vector ISA**: the on-chip vector processor uses a proprietary instruction set architecture supporting FP32, BF16, and INT8 data types, distinct from standard GPU or TPU compute models.
- **Closed-loop liquid cooling ("Sidekick")**: because no existing rack standard could accommodate Maia 100's thermal and power cabling requirements, Microsoft designed wider custom racks and a rack-adjacent "Sidekick" unit that circulates cold liquid to cold plates on each chip and returns warm liquid for dissipation — enabling deployment in datacenters without facility-level liquid cooling infrastructure.
- **Deployment scope**: as of 2024 Maia 100 runs Azure OpenAI Service inference, Copilot, GitHub Copilot, and Bing; Microsoft confirmed GPT-3.5-Turbo validation runs were conducted on behalf of OpenAI prior to GA deployment.

## Relationships

- [[nvidia_hopper_h100]] — primary incumbent AI accelerator in Azure; Maia 100 is Microsoft's in-house alternative targeting cost-optimized inference at scale for the same AI workloads.
- [[google_tpu]] — Google's analogous in-house AI ASIC lineage (TPU v1–Trillium); both companies use 2.5D HBM packaging and custom compiler stacks for inference cost reduction.
- [[microsoft_cobalt_100]] — Microsoft's companion custom CPU (Arm Neoverse N2, 128 cores) that acts as the host processor for Maia 100 accelerator nodes in Azure.
- [[aws_inferentia]] — AWS Inferentia/Trainium represent the same hyperscaler-owned inference ASIC strategy; both use HBM and target transformer inference cost reduction.

## Sources

- Microsoft Tech Community blog "Inside Maia 100" (2024): transistor count, die area, process, HBM2E specs, BF16 throughput, power envelope, custom ISA.
- Microsoft Azure Blog "Azure Maia for the era of AI" (2023): system-level design, Sidekick cooling, rack co-design, deployment workloads.
- Hot Chips 2024 presentation (Xu & Ramakrishnan): architectural details, CoWoS-S packaging, ISA design.
- ServeTheHome hardware coverage: physical measurements and rack design.
- SemiAnalysis newsletter "Microsoft Infrastructure — AI & CPU Custom Silicon Maia 100, Athena, Cobalt 100": deployment context and competitive positioning.
