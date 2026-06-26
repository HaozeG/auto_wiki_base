---
type: entity
tags: [memory, hardware, packaging, ai-accelerator]
sources:
  - https://www.jedec.org/standards-documents/docs/jesd235
  - https://hc2023.hotchips.org/
  - https://ieeexplore.ieee.org/document/9365481
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

# HBM (High Bandwidth Memory)

High Bandwidth Memory (HBM) is a 3D-stacked DRAM standard developed jointly by AMD and SK Hynix, first ratified by JEDEC in 2013, that stacks multiple DRAM dies vertically using through-silicon vias (TSVs) and places the resulting stack directly alongside a compute die on a silicon interposer in a 2.5D package. The defining characteristic of HBM is its extremely wide memory bus — 1024 bits per stack in HBM2 — which allows very high aggregate bandwidth at lower clock frequencies and therefore lower power per bit compared to wide-bus alternatives such as GDDR6. HBM has become the dominant memory technology for AI training accelerators because the arithmetic intensity of large-matrix operations demands memory bandwidth that conventional DRAM interfaces cannot supply at acceptable power envelopes. The HBM standard has evolved through five generations: HBM1 (2013, up to 128 GB/s per stack), HBM2 (2016, up to 256 GB/s), HBM2E (2019, up to 460 GB/s), HBM3 (2022, up to 819 GB/s), and HBM3E (2024, up to ~1.2 TB/s per stack). Modern AI accelerators combine four to eight HBM stacks, reaching aggregate bandwidths exceeding 3 TB/s. Three manufacturers supply HBM at volume: SK Hynix (the original developer and dominant supplier), Samsung, and Micron Technology.

## Key Claims

- HBM1 offered 128 GB/s bandwidth per stack with a 1024-bit bus at 1 Gbps per pin; HBM2 doubled per-pin rate to 2 Gbps, reaching 256 GB/s per stack.
- HBM3E, sampling in 2024, delivers approximately 1.2 TB/s per stack; the NVIDIA H100 SXM5 uses six HBM3 stacks for 3.35 TB/s total memory bandwidth.
- HBM is mounted on a silicon interposer next to the GPU or AI chip in a 2.5D CoWoS (Chip on Wafer on Substrate) package, reducing interconnect length to millimetres and enabling the wide 1024-bit bus without prohibitive PCB routing.
- HBM3 achieves roughly 7–10 GB/s per watt of memory bandwidth, compared to approximately 3–4 GB/s per watt for GDDR6X at peak throughput, giving HBM a roughly 2–3× power efficiency advantage for bandwidth-bound workloads.
- The AMD MI300X uses 192 GB of HBM3 across eight stacks delivering 5.2 TB/s, the highest capacity and bandwidth of any AI accelerator announced as of 2024.
- SK Hynix held an estimated 50–60% market share for HBM supply in 2023–2024, followed by Samsung (~30%) and Micron (~10–15%), with supply constraints cited as a limiting factor for AI accelerator production.
- Each HBM stack connects to the interposer through thousands of micro-bumps and TSVs; HBM3 uses approximately 1000–2000 TSVs per DRAM die layer.

## Relationships

- [[nvidia_hopper_h100]] — Uses six HBM3 stacks achieving 3.35 TB/s; HBM is the primary memory subsystem enabling H100's memory bandwidth advantage over consumer GPUs.
- [[amd_mi300x]] — Integrates eight HBM3 stacks for 5.2 TB/s and 192 GB capacity; the MI300X chiplet architecture places HBM stacks alongside compute dies on a shared interposer.
- [[google_tpu]] — Google TPU v4 and v5 generations use HBM2E and HBM3 respectively; bandwidth is the primary bottleneck HBM addresses for TPU matrix units.
- [[cerebras_wse]] — Cerebras uses on-chip SRAM rather than HBM, representing the design alternative that avoids the bandwidth wall through an entirely different memory architecture.
- [[aws_trainium]] — AWS Trainium2 uses HBM3 stacks to achieve the bandwidth required by its NeuronCore matrix engines.
- [[nvlink_nvswitch]] — NVLink connects GPUs whose individual HBM stacks must collectively appear as a unified memory pool across the pod.

## Sources

- JEDEC JESD235 standard documents (HBM1 through HBM3E): https://www.jedec.org/standards-documents/docs/jesd235
- SK Hynix HBM3E product announcement (2024): https://news.skhynix.com/sk-hynix-mass-produces-the-worlds-first-hbm3e/
- NVIDIA H100 datasheet (80 GB SXM5 variant): https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet
- AMD MI300X product page and Hot Chips 2023 presentation
- IEEE Solid-State Circuits: "High Bandwidth Memory (HBM) DRAM Technology and Architecture" (2021), doi:10.1109/9365481
- Micron HBM3 product brief (2023): https://www.micron.com/products/memory/hbm
