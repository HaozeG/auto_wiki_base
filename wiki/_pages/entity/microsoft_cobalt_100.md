---
type: entity
tags: [cpu, arm, neoverse, microsoft, azure, cloud, server]
sources:
  - https://www.servethehome.com/microsoft-azure-cobalt-100-128-core-arm-neoverse-n2-cpu-launched/
  - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview
  - https://newsroom.arm.com/blog/arm-powered-microsoft-azure-cobalt-100-vms
  - https://newsletter.semianalysis.com/p/microsoft-infrastructure-ai-and-cpu
  - https://www.theregister.com/2024/10/21/microsoft_arm_cobalt_100_cpu/
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

# Microsoft Cobalt 100

The Microsoft Azure Cobalt 100 is a custom 128-core server CPU designed by Microsoft and manufactured by TSMC on a 5 nm process, generally available in Azure from October 2024. It is Microsoft's first fully in-house 64-bit Arm-based processor, implemented using Arm's Neoverse N2 compute cores on the Armv9 architecture. The die is constructed as two 64-core tiles joined together and operates at 3.4 GHz. Memory connectivity consists of 12 channels of DDR5. The processor targets general-purpose cloud-native and scale-out Linux workloads — including web servers, data analytics, caches, and open-source databases — and also serves as the host CPU in Azure server nodes paired with the Maia 100 AI accelerator. Azure VMs based on Cobalt 100 provide one physical core per vCPU, avoiding the noisy-neighbor effects of SMT hyperthreading typical in hyperscaler deployments.

## Key Claims

- **128 Arm Neoverse N2 cores** (Armv9 ISA) across two 64-core tiles, manufactured on TSMC 5 nm; clocked at 3.4 GHz per core.
- **12-channel DDR5** memory interface, providing substantially higher memory bandwidth than the 8-channel DDR4/DDR5 configurations common in competing x86 cloud CPUs.
- **40% higher IPC** versus Arm Neoverse N1 (the core used in Ampere Altra), and 1.4× overall performance improvement compared to prior-generation Azure Arm-based VMs on general compute workloads.
- **Workload-specific gains**: Microsoft reports Cobalt 100 VMs deliver up to 1.5× faster Java throughput, 2× faster web server and .NET application performance, and 4× local storage IOPS (via NVMe) versus the previous generation Azure Arm VM fleet.
- **One physical core per vCPU**: Cobalt 100 Azure VMs disable simultaneous multithreading, guaranteeing dedicated core access — a differentiated feature relative to Intel Xeon and AMD EPYC deployments on Azure.
- **Host CPU for Maia 100**: Cobalt 100 is paired with the Maia 100 AI accelerator in Microsoft's AI server nodes, handling orchestration and data movement for large-scale inference workloads.

## Relationships

- [[microsoft_azure_maia_100]] — companion AI accelerator sharing the same Azure server node; Cobalt 100 acts as host CPU for Maia 100 AI inference workloads.
- [[arm_sve2]] — Neoverse N2 implements SVE2 (Scalable Vector Extension 2), enabling SIMD vector operations on floating-point and integer data types relevant to AI inference on CPU.
- [[google_tpu]] — Google similarly pairs custom CPUs (via Titanium offload) with its TPU accelerators; the Cobalt/Maia pairing mirrors this hyperscaler co-design pattern.
- [[nvidia_hopper_h100]] — Cobalt 100 represents Microsoft's push to replace x86 Xeon host CPUs in non-GPU AI infrastructure with lower-power Arm designs, part of broader hyperscaler Arm adoption.

## Sources

- ServeTheHome "Microsoft Azure Cobalt 100 128 Core Arm Neoverse N2 CPU Launched" (2024): core count, tile structure, clock speed, DDR5 channels.
- Microsoft Learn Azure Cobalt VM documentation: per-vCPU core mapping, VM series specs.
- Arm Newsroom "Arm-powered Microsoft Azure Cobalt 100 VMs" (2024): Neoverse N2 architecture context, performance claims.
- The Register "Microsoft's Arm-based Cobalt 100 CPU VMs go live in Azure" (Oct 2024): GA announcement, benchmark comparisons.
- SemiAnalysis newsletter "Microsoft Infrastructure — AI & CPU Custom Silicon": system integration with Maia 100.
