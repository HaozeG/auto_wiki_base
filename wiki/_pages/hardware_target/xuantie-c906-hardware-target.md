---
canonical_name: XuanTie C906
aliases:
- T-Head C906
- C906
- OpenC906
- Xuantie C906
- 玄铁C906
subtype: null
tags: []
hardware_targets:
- XuanTie C906
toolchains:
- GCC
- LLVM
constraints:
- 5-stage in-order single-issue pipeline
- 128-bit vector SIMD unit (FP16/FP32/INT8/INT16/INT32)
- L1 cache 8KB-64KB configurable
- no L2 cache
- RV64IMA[FD]C[V] base architecture
- 130 custom instruction extensions
- memory model extensions (cacheable, strong order)
- two-level TLB: uTLB (10 entries each for I and D) and jTLB (128/256/512 entries)
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/42c87081c0c1c296.md
- https://blog.csdn.net/tugouxp/article/details/122068912
source_url: https://blog.csdn.net/tugouxp/article/details/122068912
fetched_at: '2026-07-03T14:51:12.335228+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 14
outbound_links:
- target: gcc-tuning-c908-canmv-k230
  reason: Both the XuanTie C906 and C908 are in-order single-issue RISC-V cores from
    T-Head; the C906 includes a 128-bit SIMD vector unit while the C908 lacks a vector
    extension and relies on scalar performance
- target: spacemit-x60-hardware-target
  reason: Both are 64-bit RISC-V cores targeting embedded applications; however, the
    C906 uses a custom SIMD vector unit rather than RVV 1.0, and is single-issue compared
    to the X60's dual-issue scalar pipeline
---

# XuanTie C906

XuanTie C906 is a low-cost 64-bit RISC-V processor core developed by Alibaba's T-Head Semiconductor Co., Ltd. Based on the RV64IMA[FD]C[V] architecture, it features 130 instruction-set enhancements in memory access, arithmetic, bit operations, and cache operations, along with memory model extensions supporting cacheable and strong-order page attributes. The core implements a 5-stage in-order single-issue pipeline with a 128-bit vector compute unit capable of FP16, FP32, INT8, INT16, and INT32 SIMD operations. It supports a configurable L1 cache (8KB–64KB) with VIPT 4-way set-associative data cache and no L2 cache. The C906 is used in systems such as the Allwinner D1 processor and was open-sourced by T-Head in October 2021 as part of the OpenXuantie series, providing RTL code for simulation and FPGA implementation.

## Key Claims

- The C906 is a 64-bit RISC-V core with a 5-stage in-order single-issue pipeline and a 128-bit SIMD vector unit.
- It includes 130 custom instruction extensions beyond the RISC-V base, covering memory access, arithmetic, bit operations, and cache operations, supported by GCC and LLVM.
- The memory model is extended with page attributes such as Cacheable and Strong Order, with Linux kernel support.
- The L1 cache is configurable from 8KB to 64KB; no L2 cache is supported.
- The MMU uses a two-level TLB: first-level micro-TLB (10 entries each for instruction and data) and second-level joint TLB (configurable 128/256/512 entries, 2-way set-associative).
- The core has been open-sourced (RTL) on GitHub and can be simulated with Icarus Verilog and synthesized for FPGAs.
- Practical simulation setup requires manual creation of a `work` directory, removal of copyright notices from setup scripts, and fixes for tool compatibility (e.g., `static integer` → `integer` in Verilog).

## Optimization-Relevant Details

- ISA/profile: RV64IMA[FD]C[V] with T-Head custom extensions
- Vector/matrix/accelerator support: 128-bit SIMD vector unit supporting FP16, FP32, INT8, INT16, INT32
- Memory/cache/TLB/DMA: 8KB–64KB L1 I/D cache (VIPT 4-way), no L2; two-level TLB (10-entry uTLB per type, jTLB up to 512 entries)
- Compiler/toolchain support: GCC, LLVM (custom extensions compilable except cache operations)

## Relationships

- [[gcc-tuning-c908-canmv-k230]]: Both the XuanTie C906 and C908 are in-order single-issue RISC-V cores from T-Head; the C906 includes a 128-bit SIMD vector unit while the C908 lacks a vector extension and relies on scalar performance.
- [[spacemit-x60-hardware-target]]: Both are 64-bit RISC-V cores targeting embedded applications; however, the C906 uses a custom SIMD vector unit rather than RVV 1.0, and is single-issue compared to the X60's dual-issue scalar pipeline.

## Sources

- https://blog.csdn.net/tugouxp/article/details/122068912
- https://github.com/T-head-Semi/openc906
