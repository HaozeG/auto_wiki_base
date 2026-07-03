---
canonical_name: Monte Cimone
aliases:
- Monte Cimone v2
- MCv2
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.6
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/d3a1a170bafe75d0.md
- https://arxiv.org/html/2503.18543v4
source_url: https://arxiv.org/html/2503.18543v4
fetched_at: '2026-07-03T17:01:15.088455+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Monte Cimone

Monte Cimone is a multi-node RISC-V computing cluster developed by the University of Bologna and ETH Zürich, designed as a validation platform for high-performance computing (HPC) workloads using RISC-V hardware. The first iteration, Monte Cimone v1 (MCv1), consisted of SiFive HiFive Unmatched boards powered by the Freedom U740 SoC, achieving 4.0 Gflop/s peak theoretical performance per node. The second iteration, Monte Cimone v2 (MCv2), upgrades the cluster with Sophgo Sophon SG2042 processors based on the Xuantie C920 architecture, which includes 64 cores per socket with 128-bit vector units supporting RVV 0.7.1. MCv2 adds four nodes: three Milk-V Pioneer Box single-socket systems with 128 GB of DDR4 ECC memory each, and one dual-socket Sophgo SR1-2208A0 system with 128 cores and 256 GB of system memory. The cluster software stack is built with Spack, runs Ubuntu 21.04, and uses SLURM for job scheduling and ExaMon for monitoring. The upgrade achieves a 127x improvement in HPL double-precision FLOP/s and a 69x improvement in STREAM memory bandwidth compared to MCv1, demonstrating the increasing viability of RISC-V systems for HPC.

## Key Claims

- Monte Cimone v1 used SiFive Freedom U740 SoC with a peak of 4.0 Gflop/s per node.
- Monte Cimone v2 integrates Sophgo SG2042 (64-core Xuantie C920 with RVV 0.7.1, 128-bit vector unit).
- MCv2 nodes include three single-socket Milk-V Pioneer Box (128 GB memory) and one dual-socket SR1-2208A0 (256 GB memory).
- The software stack employs Spack with Ubuntu 21.04, SLURM, and ExaMon.
- The upgrade delivers a 127x improvement in HPL DP FLOP/s and a 69x improvement in STREAM memory bandwidth relative to MCv1.
- Network interconnect uses 1Gb/s Ethernet.

## Relationships

No specific relationship to other context pages could be identified from the source material.

## Sources

- https://arxiv.org/html/2503.18543v4
