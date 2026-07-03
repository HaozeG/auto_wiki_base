---
canonical_name: Sophon SG2044
aliases:
- SG2044
- SOPHGO SG2044
subtype: null
tags: []
hardware_targets:
- Sophon SG2044
toolchains:
- GCC
- LLVM
constraints:
- 64 cores
- RVV v1.0 (128-bit vector unit)
- T-Head XuanTie C920v2 cores
- Enhanced memory subsystem (improved over SG2042)
- Designed for high-throughput computing / workstation and server workloads
- Clock frequency not published
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/b94deb487cb62f82.md
- https://arxiv.org/html/2508.13840v1
source_url: https://arxiv.org/html/2508.13840v1
fetched_at: '2026-07-03T16:14:31.554803+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 5
outbound_links:
- target: xuantie-c906-hardware-target
  reason: Both the SG2044's C920v2 core and the XuanTie C906 are T-Head XuanTie cores;
    however, the C920v2 supports the ratified RVV v1.0 standard with a 128-bit vector
    unit, while the C906 uses a custom 128-bit SIMD unit and an in-order single-issue
    scalar pipeline
- target: andes-nx27v-hardware-target
  reason: Both the SG2044 (via C920v2) and the AndesCore NX27V implement the RISC-V
    Vector Extension version 1.0; the NX27V supports a larger 512-bit VLEN and out-of-order
    vector processing, whereas the SG2044's vector unit is 128-bit and integrated
    into an in-order core
---

# Sophon SG2044

The Sophon SG2044 is a 64-core high-performance RISC-V CPU designed by SOPHGO for workstation and server-grade workloads, building upon its predecessor the SG2042. The SG2044 is organized in clusters of four T-Head XuanTie C920v2 cores, each featuring a 128-bit vector unit that implements the ratified RISC-V Vector Extension version 1.0 (RVV v1.0), a significant upgrade from the C920v1's RVV v0.7.1. The memory subsystem has been substantially enhanced to address bottlenecks that limited the SG2042 in memory-bound workloads. The processor targets high-throughput computing and is evaluated for HPC readiness using the NAS Parallel Benchmark suite. SOPHGO has not published the clock frequency of the SG2044. Mainline compilers such as GCC and LLVM can target the vector unit directly, enabling standard vectorization without vendor-specific compiler forks.

## Key Claims

- The SG2044 is a 64-core RISC-V processor using T-Head XuanTie C920v2 cores with a 128-bit vector unit conforming to RVV v1.0.
- It addresses memory subsystem limitations present in the earlier SG2042, improving performance for workloads with complex memory access patterns.
- In a preliminary performance evaluation using the NAS Parallel Benchmark suite, the SG2044 delivered up to 4.91 times greater performance than the SG2042 on 64 cores (reported, pending full measurement context from the source paper).
- The switch to RVV v1.0 allows mainline GCC and LLVM to generate vectorized code without requiring a proprietary compiler fork.

## Optimization-Relevant Details

- ISA/profile: RISC-V with RVV v1.0 (128-bit VLEN)
- Vector/matrix/accelerator support: 128-bit vector unit per core, RVV v1.0
- Memory/cache/TLB/DMA: Enhanced memory subsystem (details not yet published; improved over SG2042 DDR stall behavior)
- Compiler/toolchain support: GCC, LLVM (mainline, no custom fork required)

## Relationships

- [[xuantie-c906-hardware-target]]: Both the SG2044's C920v2 core and the XuanTie C906 are T-Head XuanTie cores; however, the C920v2 supports the ratified RVV v1.0 standard with a 128-bit vector unit, while the C906 uses a custom 128-bit SIMD unit and an in-order single-issue scalar pipeline.
- [[andes-nx27v-hardware-target]]: Both the SG2044 (via C920v2) and the AndesCore NX27V implement the RISC-V Vector Extension version 1.0; the NX27V supports a larger 512-bit VLEN and out-of-order vector processing, whereas the SG2044's vector unit is 128-bit and integrated into an in-order core.

## Sources

- https://arxiv.org/html/2508.13840v1
