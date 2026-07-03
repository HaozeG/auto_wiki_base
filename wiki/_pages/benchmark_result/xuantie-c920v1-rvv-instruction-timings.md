---
canonical_name: XuanTie C920v1 RVV Instruction Timings
aliases:
- C920v1 instruction timings
- C920v1 cycle counts
subtype: null
tags: []
hardware_targets:
- XuanTie C920v1
workloads:
- RVV instruction microbenchmarks (vadd, vmul, vsub, vmin, vmax, etc.)
datatypes:
- int8
- int16
- int32
- int64
- float16
- float32
- float64
metrics:
- cycle count (20/80 percentile average)
toolchains:
- rvv-bench (gcc-based)
hardware_versions:
- XuanTie C920v1 rev1 (SOPHON SG2042, Milk-V Pioneer)
software_versions:
- rvv-bench commit referenced in source
measurement_method: Unrolled loop over each instruction, 20/80 percentile cycle averages,
  excluding vsetvl and load/store instructions. Registers randomized to usual values
  (non-NaN/Inf). Does not isolate latency v. throughput; includes destination dependency.
evidence_strength: measured
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
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# XuanTie C920v1 RVV Instruction Timings

This page presents measured instruction timings for the XuanTie C920v1 core (with XTheadVector extension, VLEN = 128) running on a Milk-V Pioneer (SOPHON SG2042) at 2 GHz. The timings were collected using the rvv-bench suite, which unrolls and loops over each instruction while randomizing register values. The reported values are 20/80 percentile cycle averages, excluding vsetvl and load/store latencies. The methodology does not distinguish between latency and throughput and includes a dependency on the destination register, so figures should be interpreted as operational cycle counts rather than pure latency or throughput. The full table in the source covers 32 instruction variants across LMUL settings from 1 to 8 and SEW from 8 to 64.

## Key Claims

- Vector arithmetic operations such as vadd.vv, vsub.vv, vminu.vv, vmin.vv, vmaxu.vv, vmax.vv achieve 0.5 cycles per iteration at LMUL = 1 and scale linearly to 4.0 cycles at LMUL = 8, for all SEW widths.
- Vector multiply (vmul) achieves 1.0 cycles per iteration across all LMUL and SEW combinations.
- Masked versions of these operations (e.g., vadd.vv with .v0.t) show a fixed overhead of about 2.5–3 cycles, resulting in 3.0 cycles at LMUL = 1 and 4.0 cycles at LMUL = 8.
- Vector-scalar operations (vadd.vx, vsub.vx, vminu.vx, etc.) cost 2.4 cycles at LMUL = 1, 2.4 at LMUL = 2, 3.0 at LMUL = 4, and 5.0 at LMUL = 8, indicating a higher base cost than vector-vector operations.
- Vector-immediate operations (vadd.vi, vrsub.vi) mirror the vector-vector behavior with 0.5–4.0 cycles per LMUL.
- The measurement methodology includes a dependency on the destination register, so the numbers may not represent pure throughput. A newer measurement framework without this dependency has not yet been run on this processor.

## Measurement Context

- Hardware version: XuanTie C920v1 rev1 (SOPHON SG2042, 64 cores, 2 GHz)
- Software/toolchain version: rvv-bench (commit referenced in source)
- Workload shape: Single instruction loops with varying LMUL (1, 2, 4, 8) and SEW (8, 16, 32, 64)
- Metric: Cycle count (20/80 percentile average across iterations)
- Method: Unrolled loop over the instruction, randomized register values, excluding vsetvl and load/store instructions
- Evidence strength: measured (run on actual hardware)

## Relationships

- [[rvv-matrix-multiplication-example-double]]: related via shared float64, rvv.

- [[risc-v-vector-code-examples]]: related via shared float32, int16, int32, int8, rvv.

- [[xuantie-c920v1]]: Hardware target providing the core specifications.
- [[xuantie-c920v1-rvv-performance-observations]]: Optimization strategies derived from these instruction timings.
- Note: insufficient context for additional cross-links to entity pages.

## Sources

- [RVV benchmark XuanTie C920v1 - GitHub Pages](https://camel-cdr.github.io/rvv-bench-results/milkv_pioneer/index.html)
