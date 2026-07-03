---
canonical_name: SpacemiT X60
aliases:
- X60
- SpacemiT X60 core
- spacemit-x60
subtype: null
tags:
- RISC-V
- GCC tuning
- SpacemiT
- in-order
- RVV 1.0
hardware_targets:
- SpacemiT X60
toolchains:
- GCC
constraints:
- RVA22 Profile
- 8-stage dual-issue in-order scalar pipeline
- RVV 1.0 with VLEN 256/128-bit
- 32KB L1 instruction cache per core
- 32KB L1 data cache per core
- 1MB L2 cache (cluster shared)
- extension string: rv64imafdcv_zba_zbb_zbc_zbs_zicboz_zicond_zbkc_zfh_zvfh_zvkt_zvl256b_sscofpmf_xsmtvdot
- ALU0/ALU1 integer ALU units (dual-issue)
- LSU0/LSU1 load/store units
- FPALU and FDIVSQRT floating-point units
- ALU0 shared by integer division and branches (bottleneck)
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/8b6f2fcad88939f5.md
- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
source_url: https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
fetched_at: '2026-07-03T14:14:12.383377+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: gcc-tuning-c908-canmv-k230
  reason: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model
    in-order scalar pipelines to improve instruction scheduling; however, the X60
    tuning additionally models a vector unit (RVV 1.0) and dual-issue capability,
    while the C908 tuning is purely scalar and targets a different microarchitecture
---

# SpacemiT X60

The SpacemiT X60 is a 64-bit RISC-V core implementing the RVA22 profile, designed by SpacemiT Technology for the K1 SoC used in development boards and consumer devices such as the Banana Pi BPI-F3, Milk-V Jupiter, and DeepComputing DC-ROMA Laptop II. It features an 8-stage dual-issue in-order scalar pipeline, a 256-bit vector unit supporting RVV 1.0, 32KB L1 instruction and data caches per core, and a 1MB L2 cache shared across the cluster. The core targets a balance of performance and power efficiency, and its microarchitecture is explicitly modeled in the GCC RISC-V backend to enable instruction scheduling that avoids pipeline stalls. The GCC tuning model defines execution resources such as two integer ALU units (ALU0 and ALU1) for dual-issue, two load/store units (LSU0 and LSU1), a vector unit (VXU0), and floating-point units (FPALU and FDIVSQRT). Instruction latencies are specified (e.g., 5-cycle loads, 3-cycle stores, 1-cycle ALU operations, 20-cycle 64-bit integer division) and asymmetric bottlenecks such as the shared ALU0 for division and branches are explicitly modeled. This compiler-level description is essential because the in-order hardware does not reorder instructions; scheduling decisions made by GCC directly affect throughput and pipeline utilization.

## Key Claims

- The SpacemiT X60 is an 8-stage dual-issue in-order RISC-V core with RVV 1.0 vector support (256/128-bit VLEN) and dual-issue scalar pipeline.
- It powers the SpacemiT K1 SoC, used in boards and devices including Banana Pi BPI-F3, Milk-V Jupiter, Sipeed Lichee Pi 3A, DeepComputing DC-ROMA Laptop II, DC-ROMA Pad II, and SpacemiT MUSE Book.
- GCC tuning for the X60 defines a custom automaton and CPU units (ALU0/ALU1, LSU0/LSU1, FPALU, FDIVSQRT, VXU0) to model structural hazards and instruction reservations.
- The tuning specifies latencies: 5 cycles for loads, 3 for stores, 1 for integer ALU and jump, 4 for floating-point arithmetic, 20 for 64-bit integer division (idivsi).
- Integer division and branches share ALU0, creating an asymmetric bottleneck; the scheduler must avoid issuing a branch while a division occupies ALU0.
- Without specific tuning, GCC defaults to a generic cost model that fails to utilize dual-issue capabilities and full vector width.
- The tuning does not currently define bypass mechanisms (forwarding), which could further reduce effective latencies for Read-After-Write hazards.

## Optimization-Relevant Details

- ISA/profile: RVA22
- Vector/matrix/accelerator support: RVV 1.0, VLEN 256/128-bit, x2 execution width
- Memory/cache/TLB/DMA: 32KB L1 I-cache, 32KB L1 D-cache per core; 1MB L2 cache cluster shared
- Compiler/toolchain support: GCC (tune "spacemit_x60" in riscv-cores.def and machine description file spacemit-x60.md)

## Relationships

- [[gcc-tuning-c908-canmv-k230]]: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model in-order scalar pipelines to improve instruction scheduling; however, the X60 tuning additionally models a vector unit (RVV 1.0) and dual-issue capability, while the C908 tuning is purely scalar and targets a different microarchitecture.

## Sources

- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
