---
cold_start: false
created: '2025-07-10'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.85
  self_containedness: 0.8
sources:
- https://introl.com/blog/hbm-evolution-hbm3-hbm3e-hbm4-memory-ai-gpu-2025
tags:
- memory
- hbm
- ai-hardware
- market-shares
- sk-hynix
- micron
- samsung
type: entity
updated: '2025-07-10'
---

# High Bandwidth Memory (HBM)

High Bandwidth Memory (HBM) is a three-dimensional stacked DRAM architecture designed to provide extremely high data transfer rates while reducing power consumption and physical footprint compared to traditional GDDR memory. Developed through a joint effort by AMD, SK Hynix, Samsung, and Micron, HBM uses through-silicon vias (TSVs) to stack memory dies vertically and connect them to a logic die, enabling a wide memory bus (typically 1024 bits per stack) that achieves bandwidths unattainable by conventional memory interfaces. The technology has evolved through multiple JEDEC-standardized generations, with HBM3 introduced in 2022 offering per-pin data rates up to 6.4 Gbps and stack capacities up to 64 GB, HBM3e (enhanced) increasing rates to 9.2 Gbps, and HBM4 expected in 2026 targeting data rates above 10 Gbps and stack capacities beyond 64 GB. As of Q2 2025, SK Hynix leads the HBM market with a 62% share, followed by Micron at 21% and Samsung at 17%, driven by surging demand from AI GPU accelerators such as NVIDIA's H100, B200, and AMD's MI300X. The global HBM market is projected to grow from $38 billion in 2025 to $58 billion in 2026, reflecting the critical role of high-bandwidth memory in sustaining AI model training and inference workloads.

## Key Claims

- SK Hynix held a 62% market share in the HBM market during Q2 2025, compared to Micron's 21% and Samsung's 17%.
- The global HBM market is valued at approximately $38 billion in 2025 and is expected to reach $58 billion in 2026, representing a 53% year-over-year growth.
- HBM3e, an enhanced version of HBM3, offers per-pin data rates up to 9.2 Gbps, with stack capacities up to 64 GB, and is deployed in NVIDIA's H200 and B200 GPUs.
- HBM4, standardized by JEDEC, is slated for 2026 with data rates exceeding 10 Gbps and stack capacities beyond 64 GB, targeting next-generation AI accelerators.
- HBM3 was first introduced in 2022 with data rates of 6.4 Gbps per pin and stack capacities up to 64 GB, supporting NVIDIA's H100 GPU with a memory bandwidth of 3.35 TB/s.
- The HBM supply chain is heavily concentrated among three manufacturers (SK Hynix, Micron, Samsung), which collectively produce over 99% of all HBM devices globally as of 2025.
- JEDEC standardizes HBM specifications, including interfaces, pinouts, and testing methodologies, ensuring interoperability between memory and GPU manufacturers.

## Relationships

- [[ai_chip_export_controls]] — Export controls on advanced AI chips directly impact HBM demand, as restricted GPUs like NVIDIA's H100 and B200 rely on HBM3/HBM3e. U.S. regulations limiting chip exports to China inadvertently pressure HBM supply dynamics by restricting the end-use of HBM-equipped accelerators.

## Sources

- Introl Blog: "HBM evolution: from HBM3 to HBM4 and the AI memory war" (2025): https://introl.com/blog/hbm-evolution-hbm3-hbm3e-hbm4-memory-ai-gpu-2025
