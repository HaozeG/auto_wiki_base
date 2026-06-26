---
type: entity
tags: [ai-hardware, inference, rdu, dataflow, mixture-of-experts, hbm]
sources:
  - https://arxiv.org/abs/2405.07518
  - https://sambanova.ai/blog/sn40l-chip-best-inference-solution
  - https://ieeexplore.ieee.org/document/10904578/
  - https://hc2024.hotchips.org/assets/program/conference/day1/48_HC2024.Sambanova.Prabhakar.final-withoutvideo.pdf
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

# SambaNova SN40L

The SambaNova SN40L is a dataflow AI accelerator built around the Reconfigurable Dataflow Unit (RDU) architecture, designed to serve very large and mixture-of-experts (MoE) models at enterprise inference scale. Unlike GPU-centric designs that rely on a single HBM memory tier, the SN40L employs a three-tier memory hierarchy: ~520 MB of on-chip SRAM for active layer activations, 64 GB of HBM3 per RDU at ~2 TB/s bandwidth for weights of layers currently executing, and up to 1.5 TB of DDR5 per socket (up to 12 TB in an 8-RDU node) for cold expert weights not currently being routed. This tiered design directly targets the memory wall problem for trillion-parameter sparse models, where at any inference step only a small fraction of weights are needed but total model footprint is enormous. The chip is fabricated on TSMC's 5 nm process and packaged as a dual-die socket using Chip-on-Wafer-on-Substrate (CoWoS) 2.5D packaging, integrating 102 billion transistors per socket and delivering 640 BF16 TFLOPS. The RDU compute fabric consists of Pattern Compute Units (PCUs), Pattern Memory Units (PMUs), and Address Generation and Coalescing Units (AGCUs) interconnected by a 2D mesh called the Reconfigurable Dataflow Network (RDN), enabling operators to be fused and streamed across tiles without off-chip round-trips.

## Key Claims

- The SN40L integrates a three-tier memory hierarchy: 520 MB on-chip SRAM, 64 GB HBM3 at ~2 TB/s, and 1.5 TB DDR5 at >200 GB/s per RDU socket, enabling trillion-parameter model weight residency.
- Each SN40L socket contains 102 billion transistors and delivers 640 BF16 TFLOPS, fabricated in TSMC 5 nm with CoWoS 2.5D packaging.
- SambaNova's Composition of Experts (CoE) system deploys 150 independent 7B-parameter expert models totaling ~1 trillion parameters, using DDR for cold experts, HBM for the router, and SRAM for active execution.
- An 8-socket RDU node running CoE inference achieves 3.7x speedup over a DGX H100 and 6.6x over a DGX A100 for equivalent workloads, with 15–31x faster model switching.
- The chip reduces machine footprint by up to 19x versus DGX-class servers for CoE-style trillion-parameter deployments due to DDR capacity integration on-accelerator.
- The RDU supports both inference and fine-tuning on the same hardware without reconfiguration, a capability not available on inference-only ASICs.

## Relationships

- [[nvidia_hopper_h100]] — primary benchmark comparison target; SN40L achieves 3.7x CoE throughput advantage by using three-tier memory versus H100's single HBM tier.
- [[groq_lpu]] — contrasting SRAM-only design philosophy; LPU maximizes bandwidth with no DDR/HBM, while SN40L sacrifices peak bandwidth for much larger weight capacity.
- [[aws_inferentia]] — both target cloud inference ASICs; Inferentia is inference-only and uses HBM, while SN40L integrates DDR for cold-weight capacity and supports training.
- [[google_tpu]] — both use custom interconnects and compiler-directed dataflow; TPU targets dense transformer training while RDU targets sparse MoE inference at large weight capacity.
- [[tenstorrent_blackhole]] — both support reconfigurable compute fabrics; Tenstorrent uses RISC-V cores and NoC, SN40L uses PCU/PMU tiles and RDN mesh.

## Sources

- "SambaNova SN40L: Scaling the AI Memory Wall with Dataflow and Composition of Experts" (arXiv 2405.07518): https://arxiv.org/abs/2405.07518
- SambaNova blog, "Why SN40L Is the Best for Inference": https://sambanova.ai/blog/sn40l-chip-best-inference-solution
- IEEE ISSCC 2025 paper (16.4): https://ieeexplore.ieee.org/document/10904578/
- Hot Chips 2024 presentation: https://hc2024.hotchips.org/assets/program/conference/day1/48_HC2024.Sambanova.Prabhakar.final-withoutvideo.pdf
- SambaRack SN40L-16 datasheet: https://sambanova.ai/hubfs/SambaRack%20data%20sheet%20template%2007%2009%2025.pdf
