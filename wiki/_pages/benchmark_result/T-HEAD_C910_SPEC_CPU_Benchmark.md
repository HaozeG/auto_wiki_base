---
cold_start: true
created: '2023-12-31'
datatypes: []
evidence_strength: measured
hardware_targets:
- C910 (TH1520)
- Lichee Module 4A
hardware_versions:
- T-HEAD C910 in TH1520 SoC
- Lichee Module 4A
inbound_links: 17
measurement_method: SPEC CPU benchmark suite run on the board at 2GHz frequency with
  specified toolchains.
metrics:
- SPEC score (GEOMEAN)
- SPEC rate
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 1.0
  self_containedness: 1.0
software_versions:
- OpenSBI revyos/th1520-v1.3.1
- Kernel revyos/th1520-linux-kernel/th1520-master-wip
- SPEC CPU 2006 v1.2 RELEASE
- SPEC CPU 2017 v1.1.9
sources:
- https://blog.cyyself.name/t-head-c910-spec-cpu-performance/
tags:
- RISC-V
- C910
- SPEC
- benchmark
toolchains:
- gcc-13.2.1
- Xuantie-900-gcc-V2.8.0-20231018
type: benchmark_result
updated: '2026-06-28'
workloads:
- SPEC CPU 2006 INT
- SPEC CPU 2017 INT Rate
---

# T-HEAD C910 SPEC CPU Benchmark

The T-HEAD C910 SPEC CPU Benchmark documents the performance of the T-HEAD C910 core implemented in the TH1520 System-on-Chip running on a Lichee Module 4A development board at a clock frequency of 2 GHz. The benchmark suite includes SPEC CPU 2006 Integer and SPEC CPU 2017 Integer Rate tests. Measurements were obtained using two compiler toolchains: mainline gcc-13.2.1 and the vendor-supplied Xuantie-900-gcc-V2.8.0-20231018. The system runs OpenSBI firmware revyos/th1520-v1.3.1 and a kernel built from the revyos/th1520-linux-kernel repository. This resource, published by Yangyu Chen on December 31, 2023, provides score comparisons between 1.85 GHz and 2 GHz operation, and between the two compiler versions.

## Key Claims

- SPEC CPU 2006 INT GEOMEAN at 2 GHz with mainline GCC: 8.03.
- SPEC CPU 2006 INT GEOMEAN at 1.85 GHz with mainline GCC: 7.59 (approximately 5.8% improvement at 2 GHz).
- SPEC CPU 2006 INT GEOMEAN at 2 GHz with Xuantie GCC: 8.46.
- SPEC CPU 2017 INT Rate (copy=1) GEOMEAN at 2 GHz with mainline GCC: 1.000 (normalized).
- SPEC CPU 2017 INT Rate (copy=1) GEOMEAN at 2 GHz with Xuantie GCC: slightly higher in some sub-tests (e.g., deepsjeng_r: 1.285 vs 1.120).

## Measurement Context

- Hardware version: T-HEAD C910 in TH1520 SoC, Lichee Module 4A (2 GHz version).
- Software/toolchain version: OpenSBI revyos/th1520-v1.3.1; Kernel revyos/th1520-linux-kernel/th1520-master-wip; SPEC CPU 2006 v1.2 RELEASE; SPEC CPU 2017 v1.1.9; compilers: gcc-13.2.1 (mainline) and Xuantie-900-gcc-V2.8.0-20231018.
- Workload shape: SPEC CPU 2006 Integer (12 benchmarks) and SPEC CPU 2017 Integer Rate (copy=1) (10 benchmarks).
- Metric: SPEC score (ratio normalized to reference machine), GEOMEAN.
- Method: Benchmarks compiled with -O2 -fno-strict-aliasing (SPEC 2006) or -g -O3 (SPEC 2017) and run on the board at 2 GHz. Results recorded as ratios.
- Evidence strength: measured.

## Relationships

- [[Sipeed_MAIX_series]] – Another RISC-V development board platform for comparison.
- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel that could be benchmarked on this hardware.

## Sources

- [T-HEAD C910 SPEC CPU Benchmark blog post](https://blog.cyyself.name/t-head-c910-spec-cpu-performance/)
