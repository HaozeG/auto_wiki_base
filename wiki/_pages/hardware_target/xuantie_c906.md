---
canonical_name: XuanTie C906
aliases:
- C906
- T-Head XuanTie C906
- T-HEAD XuanTie C906
- XuanTie C906 processor
- Xuantie C906
- Alibaba XuanTie C906
subtype: null
tags: []
hardware_targets:
- XuanTie C906
toolchains:
- GNU toolchain
- OpenBLAS (with RVV v0.7.1 optimizations)
constraints:
- RV64GCV instruction set
- RISC-V Vector Extension (v0.7.1 configurable)
- Vector register width 128 bits
- Element sizes 8/16/32/64 bits
- Half-precision floating-point support
- Integrated MMU
scorecard:
  novelty_delta: 0.85
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.7
sources:
- raw/cache/89756ce7e9d9be7f.md
- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c906-risc-v/
- raw/cache/4846536b770902d6.md
- raw/cache/7d46c580f16bec4d.md
- https://riscv.org/blog/2022/06/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
source_url: https://www.riscvschool.com/2023/03/09/t-head-xuantie-c906-risc-v/
fetched_at: '2026-07-01T04:19:54.493265+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
needs_summary_revision: false
---

# XuanTie C906

The XuanTie C906 is a RISC-V processor core developed by T-Head Semiconductor, a subsidiary of the Alibaba Group, designed for high energy efficiency and low cost. It is based on the RV64GCV instruction set and includes customized extensions for arithmetic enhancement, bit manipulation, load store enhancement, and TLB/Cache operations. The core supports the RISC-V Vector extension (configurable, version v0.7.1) with a vector register width of 128 bits and element sizes of 8/16/32/64 bits, including half-precision floating-point. It integrates a floating-point unit, a vector unit, and a memory management unit (MMU). The C906 is used in the Allwinner single-core RISC-V processor powering the Sipeed SBC board at a price of $12.5, making it one of the most affordable RISC-V development platforms. OpenBLAS has been optimized for the RVV v0.7.1 vector extension specifically targeting the C906 and C910 cores, enabling accelerated numerical computing.

## Key Claims

- Based on RV64GCV with customized arithmetic, bit manipulation, load store, and TLB/Cache enhancement extensions.
- RISC-V Vector extension (v0.7.1) configurable with 128-bit vector registers and element sizes from 8 to 64 bits.
- Integrated FPU, Vector Unit, and MMU.
- Used in a $12.5 Sipeed single-board computer, providing an accessible RISC-V platform.
- OpenBLAS includes optimizations for RVV v0.7.1 for C906 and C910 cores.

## Optimization-Relevant Details

- ISA/profile: RV64GCV with custom extensions (arithmetic enhancement, bit manipulation, load store enhancement, TLB/Cache operations enhancement).
- Vector/matrix/accelerator support: RISC-V Vector extension (v0.7.1), vector register width 128 bits, element sizes 8/16/32/64, half-precision FP.
- Memory/cache/TLB/DMA: Integrated MMU; TLB/Cache operations enhancement extension.
- Compiler/toolchain support: GNU toolchain (available from T-Head), OpenBLAS with RVV v0.7.1 optimizations.

## Relationships

- [[xuantie_c908]]: The newer generation core in the same XuanTie family with enhanced vector capabilities and higher performance.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: The code generation recipe for RISC-V Vector GEMM micro-kernels that can be applied to the C906 as a target platform.
- [[sgemm_optimization_allwinner_nezha_d1]]: a hand-tuned SGEMM optimization case study run directly on the Allwinner Nezha D1 board, which uses this C906 core with RVV support.

## Sources

- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c906-risc-v/
