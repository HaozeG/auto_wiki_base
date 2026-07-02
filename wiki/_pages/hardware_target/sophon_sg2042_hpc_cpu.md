---
canonical_name: Sophon SG2042
aliases:
- SG2042
- Sophon SG2042 CPU
- Milk-V Pioneer Box SG2042
subtype: null
tags:
- Sophon
- RISC-V
- HPC
- XuanTie C920
- Milk-V
hardware_targets:
- Sophon SG2042
toolchains:
- T-Head GCC 8.4 (20210618)
- GCC (upstream, limited)
constraints:
- RV64GCV
- RVV v0.7.1
- 128-bit VLEN
- 2 GHz
- 64 cores
- 4x DDR4-3200
- PCIe Gen4 32 lanes
- 64KB L1 I/D per core
- 1MB L2 per 4-core cluster
- 64MB L3 shared cache
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/f2a04d0bd66a1c7d.md
- https://arxiv.org/html/2309.00381
source_url: https://arxiv.org/html/2309.00381
fetched_at: '2026-07-02T07:24:53.549820+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Sophon SG2042

The Sophon SG2042 is the world's first publicly available 64-core RISC-V CPU designed for high-performance workloads, released in mid-2023. Each of its 64 cores is a T-Head XuanTie C920, a 64-bit out-of-order superscalar core with a 12-stage pipeline supporting the RV64GCV instruction set. The C920 cores implement version 0.7.1 of the RISC-V Vector Extension (RVV) with a 128-bit vector width and support for multiple data types including FP16, FP32, FP64, INT8, INT16, INT32, and INT64. The SG2042 organizes cores into clusters of four, each sharing 1MB of L2 cache, with a total of 64MB of L3 system cache shared across all cores. The CPU operates at 2GHz and includes four DDR4-3200 memory controllers and 32 lanes of PCI-E Gen4. The evaluation platform is the Milk-V Pioneer Box, which provides 32GB of RAM and a 1TB SSD. Compiler support for the non-standard RVV v0.7.1 requires T-Head's custom GCC fork, with the 20210618 release (GCC 8.4) offering the best auto-vectorization capability.

## Key Claims

- 64-core RISC-V CPU running at 2GHz with T-Head XuanTie C920 cores.
- C920 core: 12-stage out-of-order, multiple issue superscalar with RV64GCV.
- RVV v0.7.1 with 128-bit vector width, supporting vector lengths for FP16/FP32/FP64 and INT8/INT16/INT32/INT64.
- Memory hierarchy: 64KB L1 I/D per core, 1MB L2 per 4-core cluster, 64MB L3 shared cache.
- Four DDR4-3200 memory controllers, PCI-E Gen4 32 lanes.
- Best compiler support via T-Head GCC 8.4 (20210618) which generates vector-length-specific (VLS) 128-bit RVV assembly.
- Independent benchmarking shows 5-10x per-core performance improvement over other widely available RISC-V hardware.

## Optimization-Relevant Details

- ISA/profile: RV64GCV, with RVV v0.7.1 (not v1.0).
- Vector/matrix/accelerator support: 128-bit VLEN, VLS code generation.
- Memory/cache/TLB/DMA: 64KB L1 I-cache and D-cache per core; 1MB L2 per cluster; 64MB L3 shared cache; DDR4-3200 bandwidth; PCIe Gen4.
- Compiler/toolchain support: T-Head GCC 8.4 (20210618) with manual vectorization; upstream GCC lacks RVV v0.7.1 support; GNU rvv-next branch targets v1.0 (unmaintained).

## Relationships

- The XuanTie C920 core is also used in other T-Head processors; its architecture is comparable to the out-of-order [[sifive_performance_p570_gen3]] core, though SiFive's design supports RVA23 and RVV 1.0.
- The vector engine in the [[coral_npu_vector_execution_engine]] implements the more modern Zve32x subset of RVV 1.0, highlighting the gap between SG2042's v0.7.1 and current standards.
- Further benchmarking and optimization recipes for the SG2042 can be found in [[sophon_sg2042_rajaperf_hpc_benchmark]].

## Sources

- Nick Brown et al., "Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU", arXiv:2309.00381, 2023.
- T-Head GCC compiler fork (20210618 release).
