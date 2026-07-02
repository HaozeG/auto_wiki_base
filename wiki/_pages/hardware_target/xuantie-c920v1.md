---
canonical_name: XuanTie C920v1
aliases:
- C920v1
- XuanTie C920 (original marketing)
- C920v1 with XTheadVector
subtype: null
tags: []
hardware_targets:
- XuanTie C920v1
toolchains: []
constraints:
- RV64GC instruction set
- XTheadVector extension (based on RVV 0.7.1)
- VLEN = 128 bits
- SEW support: e8, e16, e32, e64
- Single, half, double precision floating point
- Frequency: 2 GHz
- SOPHON SG2042 SoC (64 cores)
- Milk-V Pioneer platform
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/700944b8c7e0c9ef.md
- https://camel-cdr.github.io/rvv-bench-results/milkv_pioneer/index.html
source_url: https://camel-cdr.github.io/rvv-bench-results/milkv_pioneer/index.html
fetched_at: '2026-07-02T10:25:51.448358+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# XuanTie C920v1

The XuanTie C920v1 is a RISC-V CPU core developed by T-Head (Alibaba Group) that implements the rv64gc instruction set with the XTheadVector extension, a proprietary vector extension based on the 0.7.1 draft of the RISC-V Vector Extension (RVV). It features a vector length (VLEN) of 128 bits and supports element sizes of 8, 16, 32, and 64 bits, along with single, half, and double precision floating point operations. The core runs at 2 GHz and is integrated into the SOPHON SG2042 system-on-chip, which contains 64 C920v1 cores and is used in the Milk-V Pioneer single-board computer. The core was originally marketed as C920, but XuanTie retroactively applied the C920v1 designation to distinguish XTheadVector-equipped cores from future RVV 1.0-based C920 chips.

## Key Claims

- The XuanTie C920v1 implements rv64gc and the XTheadVector extension, which is based on the 0.7.1 version of the RISC-V vector extension draft.
- It has a vector length (VLEN) of 128 bits and supports SEW = 8, 16, 32, 64.
- It supports single-precision, half-precision, and double-precision floating point vector instructions.
- The core runs at 2 GHz and is part of the SOPHON SG2042 SoC with 64 cores.
- The core was originally marketed as C920; the C920v1 revision specifically denotes the XTheadVector variant, while a future C920 is expected to support RVV 1.0.

## Optimization-Relevant Details

- ISA/profile: rv64gc + XTheadVector (RVV 0.7.1)
- Vector/matrix/accelerator support: XTheadVector, VLEN = 128, no matrix accelerator
- Memory/cache/TLB/DMA: Not detailed in source
- Compiler/toolchain support: Tested with rvv-bench suite (gcc-based toolchain)

## Relationships

- [[xuantie-c920v1-rvv-instruction-timings]]: Detailed instruction cycle counts derived from microbenchmarks on this core.
- [[xuantie-c920v1-rvv-performance-observations]]: Optimization strategies for vector code on this core.
- Note: insufficient context for additional cross-links to entity pages; only one relevant page was available in the wiki context.

## Sources

- [RVV benchmark XuanTie C920v1 - GitHub Pages](https://camel-cdr.github.io/rvv-bench-results/milkv_pioneer/index.html)
