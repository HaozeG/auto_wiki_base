---
type: entity
tags: [amd, gpu, ai-accelerator, data-center, hbm4, cdna]
sources:
  - https://videocardz.com/newz/amd-launches-instinct-mi350-series-confirms-mi400-in-2026-with-432gb-hbm4-memory
  - https://www.tweaktown.com/news/105758/amds-next-gen-instinct-mi400-gpu-confirmed-rocks-432gb-of-hbm4-at-19-6tb-sec-ready-for-2026/index.html
  - https://www.guru3d.com/story/amd-instinct-mi400-launches-in-2026-with-cdna-5-architecture/
  - https://ir.amd.com/news-events/press-releases/detail/1201/amd-accelerates-pace-of-data-center-ai-innovation-and-leadership-with-expanded-amd-instinct-gpu-roadmap
  - https://tech-insider.org/amd-mi400-series-ai-gpu-data-center-2026/
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AMD Instinct MI400 (CDNA 5)

The AMD Instinct MI400 series is AMD's 2026 data-center AI accelerator family, built on the CDNA 5 architecture and TSMC's 2nm process node. The MI400 follows the MI350 (which used CDNA 4 on 3nm) and represents AMD's most aggressive chiplet redesign to date: the flagship MI455X combines 12 compute chiplets on TSMC N2 with 3 additional chiplets on a 3nm interposer, reaching 320 billion total transistors. Memory capacity jumps to 432 GB of HBM4 per GPU — 50% more than the MI350's 288 GB of HBM3e — while memory bandwidth reaches 19.6 TB/s, a 145% increase over the MI350's 8 TB/s. Peak compute performance targets 40 PFLOPS FP4 and 20 PFLOPS FP8, roughly doubling MI350 throughput. AMD markets the platform under the codename Helios as a rack-scale solution designed for large-scale AI training and distributed inference, with scale-out bandwidth of 300 GB/s per GPU. Two variants were confirmed at launch: the MI455X for cloud and large-scale training, and the MI430X targeting HPC and government AI workloads. The MI400 series was officially unveiled at CES 2026, with AMD positioning it against NVIDIA's Blackwell and Vera Rubin generations.

## Key Claims

- The MI455X integrates 320 billion transistors across 12 TSMC N2 compute chiplets plus 3 additional chiplets at 3nm, AMD's largest chiplet count in a single GPU package.
- HBM4 memory capacity reaches 432 GB per GPU at 19.6 TB/s bandwidth, versus 288 GB HBM3e at 8 TB/s on the MI350 — a 145% bandwidth improvement.
- FP4 peak throughput is 40 PFLOPS and FP8 is 20 PFLOPS, approximately doubling MI350 (CDNA 4) performance at both precisions.
- Scale-out bandwidth per GPU is 300 GB/s, enabling the Helios rack-scale platform for distributed training.
- The MI400 uses CDNA 5 architecture on TSMC 2nm, one full node generation ahead of MI350's CDNA 4 on 3nm.
- AMD confirmed the MI500 series (successor) is in advanced design targeting a 2027 launch, indicating annual cadence continuation.

## Relationships

- [[amd_cdna_architecture]] — MI400 implements CDNA 5, the fifth generation of AMD's Compute DNA data-center GPU architecture; MI350 used CDNA 4.
- [[amd_mi300x]] — Two generations prior; MI300X introduced AMD's 3D chiplet stacking with unified CPU+GPU+HBM die; MI400 abandons CPU dies and scales compute chiplets instead.
- [[hbm_high_bandwidth_memory]] — MI400 adopts HBM4 at 432 GB, the largest HBM4 capacity announced among 2026 AI accelerators.
- [[chiplet_architecture_advanced_packaging]] — MI455X's 15-chiplet design (12+3) represents the most complex chiplet integration in the Instinct product line.
- [[nvidia_vera_rubin]] — Primary competitor; R100 offers 288 GB HBM4 at 22 TB/s versus MI455X's 432 GB at 19.6 TB/s; MI400 leads on capacity, R100 leads on per-GB bandwidth.

## Sources

- VideoCardz — MI400 confirmation with 432 GB HBM4 at 19.6 TB/s: https://videocardz.com/newz/amd-launches-instinct-mi350-series-confirms-mi400-in-2026-with-432gb-hbm4-memory
- Tweaktown — MI400 GPU specs confirmed: https://www.tweaktown.com/news/105758/amds-next-gen-instinct-mi400-gpu-confirmed-rocks-432gb-of-hbm4-at-19-6tb-sec-ready-for-2026/index.html
- Guru3D — MI400 CDNA 5 architecture launch: https://www.guru3d.com/story/amd-instinct-mi400-launches-in-2026-with-cdna-5-architecture/
- AMD IR press release — expanded Instinct roadmap: https://ir.amd.com/news-events/press-releases/detail/1201/amd-accelerates-pace-of-data-center-ai-innovation-and-leadership-with-expanded-amd-instinct-gpu-roadmap
- Tech Insider — MI400 series analysis: https://tech-insider.org/amd-mi400-series-ai-gpu-data-center-2026/
