---
canonical_name: GCC Tuning Benchmark on XuanTie C908
aliases:
- C908 GCC tuning benchmark
- CoreMark C908 0.8%
- XuanTie C908 GCC Tuning
- C908 GCC scheduler model
- xt-c908 tuning
- xt-c908 GCC tuning
- C908 scheduler model
- RISC-V XuanTie C908 tuning
- GCC Tuning for XuanTie C908
- XuanTie C908 scheduler model
- C908 GCC tuning
subtype: null
tags: []
hardware_targets:
- XuanTie C908
workloads:
- CoreMark
- instruction throughput loops (add, fadd etc.)
datatypes: []
metrics:
- CoreMark score improvement
- cycle-count improvement
toolchains:
- GCC
hardware_versions:
- CanMV-K230-V1.1 board
- XuanTie C908 R1S0
software_versions:
- GCC patch (2026-06-03)
measurement_method: 20 warm-up runs, 200 measured runs, aligned memory access
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/84a65460eb9d8421.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- raw/cache/1369a5b7d9302dfe.md
- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406284.html
- raw/cache/a02cf74402ee2d7e.md
- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
source_url: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
fetched_at: '2026-07-03T13:30:30.422521+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 7
outbound_links:
- target: xuantie-c908-gcc-tuning
  reason: This benchmark result is the direct performance validation of the GCC scheduler
    model documented on that hardware target page
- target: c908-wino-gemm-optimization
  reason: Contrasts a software library (SHL) optimization benchmark with the GCC compiler
    tuning benchmark; the SHL optimization assumes vector support, while this GCC
    benchmark confirms scalar-only measurement
---

# GCC Tuning Benchmark on XuanTie C908

The XuanTie C908 GCC tuning patch, submitted in June 2026 by Milan Tripkovic, defines a scheduler model for the XuanTie C908 RISC-V core within the GCC compiler backend. The model describes scalar integer, load/store, multiply, divide, and floating-point pipeline resources based on the XuanTie C908 R1S0 User Manual. It is the first GCC tuning specifically for the C908 core and targets in-order scalar scheduling only, leaving vector scheduling for future work (xt-c908v). The tuning was tested on a CanMV-K230-V1.1 board and resulted in a 0.8% CoreMark improvement and 5-17% cycle-count improvements on instruction throughput loops. The patch also introduced clamping of long-latency reservations to 7 cycles, following the existing RISC-V scheduler modelling approach. During review, Jeffrey Law noted that all instruction types must have reservations in the GCC RISC-V backend and recommended adding dummy reservations for unused types, similar to the SpacemiT X60 tuning, to avoid compilation failures (ICE). The benchmark methodology consisted of 20 warm-up runs followed by 200 measured executions with aligned memory access. No vector instructions were used as the C908 lacks a vector extension.

## Key Claims

- CoreMark improvement: 0.8% on a CanMV-K230-V1.1 board.
- Cycle-count improvements on instruction throughput loops: 5% to 17%.
- Measurement methodology: 20 warm-up runs, then 200 measured runs with aligned memory access.
- The benchmark validates the scalar scheduler model for the C908 GCC tuning.
- The GCC scheduler model for XuanTie C908 models scalar integer, load/store, multiply, divide, and FP pipeline resources based on the XuanTie C908 R1S0 User Manual.
- Scalar-only scheduling implementation; vector scheduling is deferred to a future xt-c908v model.
- Long-latency reservations are clamped to 7 cycles, following the existing RISC-V scheduler modelling approach introduced by commit 8265192.
- Reviewer identified that missing instruction type reservations cause an ICE during scheduling; the fix requires covering all insn types, including dummy reservations for types not relevant to the C908 microarchitecture.

## Measurement Context

- Hardware version: XuanTie C908 on CanMV-K230-V1.1 board
- Software/toolchain version: GCC patch submitted 2026-06-03 (pre-trunk)
- Workload shape: CoreMark; unrolled loops with independent register groups (add, fadd, etc.)
- Metric: CoreMark score improvement (%), cycle-count improvement (%)
- Method: 20 warm-up runs, 200 measured runs, aligned memory access
- Evidence strength: measured
- Scheduler model reference: XuanTie C908 R1S0 User Manual
- Clamping of long-latency reservations to 7 cycles (commit 8265192)
- Reviewer (Jeffrey Law) required dummy reservations for all insn types to prevent ICE

## Transformation

- Prerequisites: GCC source tree, XuanTie C908 User Manual for pipeline details.
- Steps: Add cpu tuning entry in riscv-cores.def, microarchitecture type in riscv-opts.h, tune structure in riscv.cc, and include the xt-c908.md file in riscv.md. The xt-c908.md file defines the scheduler automaton and instruction reservations.
- Expected effect: Reduced pipeline stalls for scalar code, leading to better instruction throughput on XuanTie C908 cores. The patch reports 0.8% CoreMark improvement and 5-17% improvement on instruction throughput loops.
- Failure modes: If the scheduler model does not accurately reflect hardware, it may cause suboptimal scheduling. However, it is based on the user manual and validated with measurements. The model does not cover vector instructions; compiling vector code without future tuning may not benefit.
- Measurements: CoreMark: 0.8% improvement. Instruction throughput loops (add, fadd): 5-17% cycle-count improvement. Method: 20 warm-up runs, 200 measured runs, aligned memory.

## Relationships

- [[xuantie-c908-gcc-tuning]]: This benchmark result is the direct performance validation of the GCC scheduler model documented on that hardware target page.
- [[c908-wino-gemm-optimization]]: Contrasts a software library (SHL) optimization benchmark with the GCC compiler tuning benchmark; the SHL optimization assumes vector support, while this GCC benchmark confirms scalar-only measurement.
- [[gcc-tuning-c908-canmv-k230]]: This optimization recipe describes the GCC tuning patch that produced the benchmark results reported in that page; the benchmark result provides the performance validation for the scheduler model defined here.
- [[xuantie-c906-hardware-target]]: Both the XuanTie C906 and C908 are T-Head in-order single-issue RISC-V cores with GCC tuning; however, the C906 includes a 128-bit SIMD vector unit while the C908 is entirely scalar and lacks any vector extension, making their scheduler models fundamentally different.
- [[spacemit-x60-hardware-target]]: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model in-order scalar pipelines using the same RISC-V backend infrastructure and both required dummy reservations for unsupported instruction types; however, the X60 tuning additionally models dual-issue capabilities and an RVV 1.0 vector unit.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406284.html
- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
