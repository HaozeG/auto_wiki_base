---
canonical_name: NAS Parallel Benchmark characterization of Sophon SG2042
aliases:
- NPB on SG2042
- SG2042 NPB performance
subtype: null
tags: []
hardware_targets:
- Sophon SG2042
workloads:
- NAS Parallel Benchmark (NPB) suite
datatypes: []
metrics:
- Single-core performance improvement factor (2.6x to 16.7x)
- Relative performance on compute-bound vs memory-bound algorithms
toolchains:
- XuanTie GCC
hardware_versions:
- Milk-V Pioneer Box with 128GB DDR4
- SG2042 at 2GHz
software_versions:
- XuanTie GCC 20210618 (GCC 8.4)
- Optimization level 3
measurement_method: Averaged over five runs with exclusive machine usage.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.85
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/b8ccce9b3180873d.md
- https://arxiv.org/html/2406.12394v1
source_url: https://arxiv.org/html/2406.12394v1
fetched_at: '2026-07-03T18:04:35.239892+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: sophon-sg2042-hardware-target
  reason: This benchmark result characterizes the SG2042 hardware target, identifying
    its memory subsystem as the primary performance bottleneck
---

# NAS Parallel Benchmark characterization of Sophon SG2042

The NAS Parallel Benchmark (NPB) suite was used to characterize the performance of the Sophon SG2042 64-core RISC-V CPU in the Milk-V Pioneer Box with 128GB DDR4 RAM, running at 2GHz and compiled with XuanTie GCC 20210618 (GCC 8.4) at optimization level 3. The SG2042 was compared against other CPUs implementing RISC-V, x86-64, and AArch64 ISAs, including CPUs used in production supercomputers. Results were averaged over five runs with exclusive machine access. The study found that the SG2042 consistently outperformed all other RISC-V solutions, delivering between 2.6x and 16.7x performance improvement at the single-core level. When compared against x86-64 and AArch64 CPUs, the SG2042 performed comparatively well on computationally bound algorithms but its relative performance decreased on memory bandwidth- or latency-bound algorithms, highlighting the memory subsystem as the greatest bottleneck.

## Key Claims

- The SG2042 achieves 2.6x to 16.7x single-core performance improvement over other commodity RISC-V CPUs (measured).
- On compute-bound algorithms, the SG2042 performs competitively with x86-64 and AArch64 CPUs (measured).
- On memory bandwidth- or latency-bound algorithms, the SG2042 shows decreased relative performance (measured).
- The memory subsystem is identified as the primary performance bottleneck (analysis from measurements).

## Measurement Context

- Hardware version: Sophon SG2042 in Milk-V Pioneer Box, 128GB DDR4, 2GHz
- Software/toolchain version: XuanTie GCC 20210618 (GCC 8.4), -O3
- Workload shape: NAS Parallel Benchmark (NPB) suite (individual benchmark shapes not specified in source)
- Metric: Single-core performance improvement factor (2.6-16.7x); relative performance on compute-bound vs memory-bound algorithms
- Method: Five runs averaged, exclusive machine usage
- Evidence strength: measured

## Relationships

- [[sophon-sg2042-hardware-target]]: This benchmark result characterizes the SG2042 hardware target, identifying its memory subsystem as the primary performance bottleneck.

## Sources

- https://arxiv.org/html/2406.12394v1
