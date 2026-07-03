---
canonical_name: SpacemiT X60 GCC Tuning
aliases:
- spacemit-x60 gcc tuning
- GCC tuning for SpacemiT X60
- GCC tuning for SpacemiT X60 RISC-V Core
- GCC Vector Scheduling for SpacemiT X60
- SpacemiT X60 GCC vector tuning
- X60 LMUL cost scaling
- Dynamic LMUL scaling for SpacemiT X60
subtype: null
tags:
- RISC-V
- GCC
- SpacemiT
- pipeline
- in-order
hardware_targets:
- SpacemiT X60
workloads: []
datatypes: []
metrics: []
toolchains:
- GCC
constraints:
- 8-stage dual-issue in-order scalar pipeline
- RVV 1.0 with VLEN 256/128-bit
- ALU0 shared by integer division and branches
- custom automaton defined in GCC RISC-V backend
evidence_strength: reported
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/8b6f2fcad88939f5.md
- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
- raw/cache/110413a720fff850.md
- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-ii/
source_url: https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
fetched_at: '2026-07-03T18:08:22.289988+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-x60-hardware-target
  reason: This tuning recipe implements the GCC scheduling model for the SpacemiT
    X60 core, whose microarchitecture details (8-stage dual-issue pipeline, RVV 1.0
    vector unit, cache hierarchy) are documented in that page
---

# SpacemiT X60 GCC Tuning

The SpacemiT X60 GCC Tuning is an optimization recipe implemented in the GCC RISC-V backend that provides an explicit instruction scheduling model for the SpacemiT X60 core. The tuning defines a custom automaton and CPU units (ALU0, ALU1, LSU0, LSU1, FPALU, FDIVSQRT, VXU0) to model the 8-stage dual-issue in-order scalar pipeline and the 256-bit RVV 1.0 vector unit. It specifies instruction latencies and resource reservations to enable the compiler to make cycle-aware scheduling decisions that avoid pipeline stalls, which is critical because the in-order hardware does not reorder instructions. The tuning does not currently define bypass mechanisms (forwarding), which could further improve scheduling quality. The expected effect is better utilization of the dual-issue pipeline and vector unit compared to the generic GCC cost model. The recipe is described in a blog post series by rt-rk.com documenting the GCC patches for the RISC-V backend.

## Key Claims

- The GCC tuning for the SpacemiT X60 defines a custom automaton (`spacemit_x60`) and CPU units: ALU0, ALU1, LSU0, LSU1, FPALU, FDIVSQRT, and VXU0.
- Instruction latencies are specified: 5 cycles for loads, 3 for stores, 1 for integer ALU and jumps, 4 for floating-point arithmetic, 20 for 64-bit integer division.
- Integer division and branches share ALU0, creating an asymmetric bottleneck that the scheduler must handle.
- Without this tuning, GCC defaults to a generic cost model that fails to utilize dual-issue capabilities or the full vector width.
- The tuning is part of the GCC RISC-V backend and is defined in `riscv-cores.def` and `spacemit-x60.md`.

## Transformation

### Prerequisites
- GCC source tree with RISC-V backend support.
- Familiarity with GCC machine description files (`*.md`) and the structure of `riscv-cores.def`.

### Steps
1. Define the core in `riscv-cores.def` with the extension string:
   ```
   RISCV_CORE("spacemit-x60", "rv64imafdcv_zba_zbb_zbc_zbs_zicboz_zicond_zbkc_zfh_zvfh_zvkt_zvl256b_sscofpmf_xsmtvdot", "spacemit-x60")
   ```
2. Define the tune and pipeline model in `riscv-cores.def`:
   ```
   RISCV_TUNE(spacemit_x60, spacemit_x60_tune_info)
   ```
3. Create or update the machine description file `spacemit-x60.md` with:
   - `define_automaton "spacemit_x60"`
   - CPU units: `define_cpu_unit "spacemit_x60_alu0, spacemit_x60_alu1"`, `define_cpu_unit "spacemit_x60_lsu0, spacemit_x60_lsu1"`, `define_cpu_unit "spacemit_x60_vxu0"`, `define_cpu_unit "spacemit_x60_fpalu"`, `define_cpu_unit "spacemit_x60_fdivsqrt"`
   - Instruction reservations and latencies for each instruction class (e.g., 5-cycle loads, 3-cycle stores, 20-cycle integer division).
4. Rebuild GCC and verify the scheduling via cycle-level simulation or performance benchmarks.

### Expected Effect
Improved instruction scheduling that reduces pipeline stalls and increases dual-issue utilization, leading to better performance on scalar and vector workloads compared to using the generic GCC cost model.

### Failure Modes
- Incorrect latency assignments may cause over-scheduling or under-utilization.
- Missing bypass modeling may leave Read-After-Write (RAW) hazards unresolved, reducing the benefit of the tuning.
- Over-constraining resources may prevent dual-issue dispatch, negating the hardware's capability.

### Measurements
The blog post series describes the tuning implementation but does not provide specific performance measurements. The evidence for the claimed improvement is reported rather than measured.

## Relationships

- [[spacemit-x60-hardware-target]]: This tuning recipe implements the GCC scheduling model for the SpacemiT X60 core, whose microarchitecture details (8-stage dual-issue pipeline, RVV 1.0 vector unit, cache hierarchy) are documented in that page.

## Sources

- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
