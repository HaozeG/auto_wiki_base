---
canonical_name: AMD Instinct MI200
aliases:
- MI200
- MI250X
- MI250
- Instinct MI200 series
- Aldebaran
- CDNA 2
- AMD Instinct MI200 Series
- AMD Instinct MI250X
- AMD Instinct MI250
- AMD Instinct MI210
subtype: null
tags:
- AMD
- Instinct
- CDNA2
- HPC
- GPU
- accelerator
scorecard:
  novelty_delta: 0.6
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.4
sources:
- raw/cache/1874a2c68d571790.md
- https://www.techpowerup.com/288776/amd-instinct-mi200-dual-gpu-chiplet-cdna2-architecture-128-gb-hbm2e
- raw/cache/71ec38cf8e1f8c44.md
- https://wccftech.com/amd-provides-first-look-at-aldebaran-cdna-2-instinct-mi200-series-mcm-gpu-block-diagram/
source_url: https://www.techpowerup.com/288776/amd-instinct-mi200-dual-gpu-chiplet-cdna2-architecture-128-gb-hbm2e
fetched_at: '2026-07-17T10:14:47.963625+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
outbound_links:
- target: amd_cdna
  reason: The AMD Instinct MI200 is the first product family to implement the CDNA2
    architecture, which is the second generation of the compute-oriented CDNA microarchitecture.
    The CDNA2 architecture introduced multi-chip module packaging via an elevated
    fanout bridge (EFB) to connect the two compute dies, and the MI200 series is the
    initial implementation of this design
---

# AMD Instinct MI200

The AMD Instinct MI200 is a dual-GPU chiplet accelerator for high-performance computing (HPC), based on the CDNA2 architecture. Announced in November 2021, it is manufactured on TSMC's 6 nm process. The MI200 family comprises the MI250X and MI250 models. The MI250X features 58 billion transistors across two compute dies, each with 110 Compute Units (CUs) for a total of 220 CUs, and 880 Matrix Cores (440 per die). It is paired with 128 GB of HBM2E memory providing 3.2 TB/s of bandwidth. The two dies are interconnected via AMD Infinity Fabric links, offering up to 100 GB/s bi-directional bandwidth per link and a total of 800 GB/s for on-the-fly communication. The MI250 is a lower-configuration variant with 104 CUs per die (208 total).

## Key Claims

- The AMD Instinct MI250X accelerator contains 58 billion transistors across two dies fabricated on TSMC 6 nm.
- It features 220 Compute Units (CUs) and 880 Matrix Cores based on the CDNA2 architecture.
- Memory subsystem: 128 GB of HBM2E memory with a bandwidth of 3.2 TB/s.
- Infinity Fabric interconnect: 25 Gbps links providing 100 GB/s bi-directional bandwidth per link, with a total of 800 GB/s available for chiplet communication.
- Performance claims compared to NVIDIA A100: 4.9× faster on FP64 vector compute, 2.5× faster on FP32 vector, 4.9× faster on FP64 matrix, 1.2× faster on FP16 and BF16 matrix, 1.6× more memory capacity, and 1.6× higher memory bandwidth.
- The MI250 model is binned to 104 CUs per die (208 total), approximately 5% slower than the MI250X.
- Packaged as an OAM (OCP Accelerator Module) form factor with eight Infinity Fabric links.

## Relationships

- [[amd_cdna]]: The AMD Instinct MI200 is the first product family to implement the CDNA2 architecture, which is the second generation of the compute-oriented CDNA microarchitecture. The CDNA2 architecture introduced multi-chip module packaging via an elevated fanout bridge (EFB) to connect the two compute dies, and the MI200 series is the initial implementation of this design.

## Sources

- [AMD Instinct MI200: Dual-GPU Chiplet; CDNA2 Architecture; 128 GB HBM2E | TechPowerUp](raw/cache/1874a2c68d571790.md)
