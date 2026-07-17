---
canonical_name: AMD CDNA 4
aliases:
- CDNA 4
- gfx950
- MI350X architecture
- MI355X architecture
- AMD CDNA4
subtype: null
tags:
- gpu-architecture
- amd
- ai-accelerator
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.95
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/45a88d7548d628ee.md
- https://zhaifeiyue.github.io/papers/amd-cdna4-whitepaper/detail.html
source_url: https://zhaifeiyue.github.io/papers/amd-cdna4-whitepaper/detail.html
fetched_at: '2026-07-17T09:10:53.797272+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 2
---

# AMD CDNA 4

AMD CDNA 4 is a GPU compute architecture designed by AMD for datacenter AI and high-performance computing workloads, introduced in 2025 as the successor to CDNA 3. It powers the AMD Instinct MI350X and MI355X accelerators. CDNA 4 is fabricated using a heterogeneous chiplet approach: eight compute chiplets (XCD) on TSMC's N3P (3 nm) process are stacked vertically on two I/O dies (IOD) on TSMC N6 (6 nm) via advanced 3D packaging, surrounded by eight HBM3E memory stacks providing 288 GB of memory at 8.0 TB/s bandwidth. The architecture reduced the number of compute units to 256 (down from 304 in CDNA 3) but doubled per-CU matrix throughput for 16-bit and lower precisions through an expanded Matrix Core execution width. Core innovations include the addition of MXFP microscaling formats based on the OCP MX standard: MXFP8, MXFP6 (a unique AMD mid-precision format), and MXFP4, which deliver peak throughput of 5.0 PFLOPS in FP8 and 10 PFLOPS in both MXFP4 and MXFP6. The local data share (LDS) per CU was increased to 160 KB (2.5× larger) with read bandwidth doubled to 256 bytes per cycle. In a notable shift toward AI-first design, CDNA 4 removes dedicated TF32 hardware (emulated via BF16) and halves FP64 matrix performance to 78.6 TFLOPS, prioritizing matrix resources for AI workloads.

## Key Claims

- CDNA 4 consists of 8 XCD (TSMC N3P) + 2 IOD (TSMC N6), packaging 185 billion transistors.
- Total compute units: 256 (32 per XCD), down from 304 in MI300X (CDNA 3).
- Peak FP8 throughput: 5.0 PFLOPS (10 PFLOPS with 2:4 sparsity).
- Peak MXFP4/MXFP6 throughput: 10 PFLOPS (no sparsity benefit for 4-bit).
- MXFP6 is an AMD-unique 6-bit microscaling format (E3M2/E2M3) providing a precision level between FP8 and FP4 at the same throughput as MXFP4.
- LDS per CU increased from 64 KB to 160 KB (2.5×), read bandwidth from 128 B/cycle to 256 B/cycle.
- Memory: 288 GB HBM3E at 8.0 TB/s.
- TF32 hardware removed; FP64 matrix performance halved to 78.6 TFLOPS.
- MI350X (air-cooled) TDP 1000 W; MI355X (liquid-cooled) TDP 1400 W.
- Infinity Fabric interconnect bandwidth: 1,075 GB/s (vs. NVIDIA NVLink5 at 1,800 GB/s).

## Relationships

- AMD CDNA 4 succeeds the CDNA 3 architecture used in the AMD Instinct MI300X and MI325X, part of the [[amd_instinct]] product line, and adopts a more aggressive AI-first focus by removing TF32 hardware and reducing FP64 matrix resources in favor of expanded matrix throughput and microscaling support.

## Sources

- [AMD CDNA 4 Architecture White Paper — Feiyue KB](raw/cache/45a88d7548d628ee.md)
