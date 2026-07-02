---
canonical_name: AX45MPV RVV Instruction Throughput
aliases:
- RVV instruction throughput AX45MPV
- AX45MPV instruction timings
subtype: null
tags: []
hardware_targets:
- AX45MPV
workloads:
- RVV instruction microbenchmarks
datatypes:
- int8 (e8)
- int16 (e16)
- int32 (e32)
- int64 (e64)
metrics:
- throughput (cycles per instruction)
toolchains:
- GCC (RISC-V toolchain)
hardware_versions:
- VLEN=512, DLEN=512
software_versions:
- AndeSim near-cycle-accurate simulator
measurement_method: Measured cycle averages when unrolling and looping over the instruction,
  with registers randomized to typical values (not NaN/Inf). Results obtained from
  AndeSim cycle-accurate simulator for AX45MPV with default configuration.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/cf4003729a4c4c3b.md
- https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html
source_url: https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html
fetched_at: '2026-07-02T11:47:40.122491+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# AX45MPV RVV Instruction Throughput

This benchmark result documents measured instruction throughput for the Andes AX45MPV RISC-V core running on the AndeSim near-cycle-accurate microarchitecture simulator with the default configuration of VLEN=DLEN=512. The measurements cover a range of RISC-V Vector Extension (RVV) instructions across various LMUL and SEW configurations, providing cycle counts per iteration under looped and unrolled execution. The results include integer operations (vadd, vsub, vmin, vmax, vand, etc.), control flow, and scalar operations. The instruction timings are presented as cycle averages when unrolling and looping over the given instruction, estimating instruction throughput. The source page provides a full table with 22 columns for different SEW/LMUL combinations.

## Key Claims

- For vadd.vv with LMUL=1 and SEW=e8 to e64, the throughput is consistently 1.0 cycles per iteration.
- For vadd.vv with LMUL=4, throughput scales to 4.0 cycles per iteration (1 cycle per 4 elements approximately).
- Scalar integer add (add t0,t1,t2) achieves between 0.57 and 0.69 cycles per instruction, with lower cycles at higher LMUL.
- Scalar integer mul achieves between 1.0 and 1.29 cycles.
- Instructions with masking (v0.t) do not significantly change throughput from unmasked versions.
- Most vector integer operations (vadd, vsub, vmin, vmax, vand) show similar throughput characteristics: 1.0 cycles for LMUL=1, 2.0 for LMUL=2, 4.0 for LMUL=4, and 8.0 for LMUL=8, indicating full vector unit utilization.

## Measurement Context

- Hardware version: AX45MPV with VLEN=512, DLEN=512
- Software/toolchain version: AndeSim simulator, GCC RISC-V toolchain (assumed)
- Workload shape: Instruction microbenchmarks, looped and unrolled
- Metric: Throughput in cycles per iteration (microarchitectural cycles)
- Method: Cycle averages from simulator, using rdcycle instructions, with warmup loops and register randomization
- Evidence strength: measured (on cycle-accurate simulator)

## Relationships

- [[andes-ax45mpv]]: The hardware target for which these instruction timings were obtained.
- [[earth-shifting-based-vector-memory-access]]: This optimization recipe for vector memory access could be applied to improve performance on memory-bound operations on the AX45MPV.

## Sources

- [RVV benchmark AX45MPV instruction timings](https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html)
