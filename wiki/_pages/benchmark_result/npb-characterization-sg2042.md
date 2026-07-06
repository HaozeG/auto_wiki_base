---
canonical_name: NAS Parallel Benchmark characterization of Sophon SG2042
aliases:
- NPB on SG2042
- SG2042 NPB performance
- SG2042 NPB Benchmark Characterization
- SG2042 performance characterisation
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
- raw/cache/f4ce8d173e27b53c.md
- https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
source_url: https://arxiv.org/html/2406.12394v1
fetched_at: '2026-07-03T18:04:35.239892+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: sophon-sg2042-hardware-target
  reason: This benchmark result characterizes the SG2042 hardware target, identifying
    its memory subsystem as the primary performance bottleneck
---

# NAS Parallel Benchmark characterization of Sophon SG2042

The NAS Parallel Benchmark (NPB) suite was used to characterize the performance of the Sophon SG2042 64-core RISC-V CPU in the Milk-V Pioneer Box with 128GB DDR4 RAM, running at 2GHz and compiled with XuanTie GCC 20210618 (GCC 8.4) at optimization level 3. The SG2042 uses T-Head XuanTie C920 cores. The study, by Brown and Jamieson (EPCC, University of Edinburgh, June 2024), compares the SG2042 against other CPUs implementing RISC-V, x86-64 (Xeon Platinum 8170), and AArch64 ISAs. Results were averaged over five runs with exclusive machine access. Single-core results show that the SG2042 outperforms all other RISC-V solutions by a factor of 2.6 to 16.7. Multi-core NPB tests with OpenMP and MPI parallelization reveal that the SG2042 performs competitively on compute-bound algorithms but shows decreased relative performance on memory-bandwidth- or latency-bound workloads, with the memory subsystem identified as the primary bottleneck. The study uses NPB pseudo-applications including the MG (Multi-Grid) benchmark.

## Key Claims

- The SG2042 achieves 2.6x to 16.7x single-core performance improvement over other commodity RISC-V CPUs (measured).
- On compute-bound algorithms, the SG2042 performs competitively with x86-64 and AArch64 CPUs (measured).
- On memory bandwidth- or latency-bound algorithms, the SG2042 shows decreased relative performance (measured).
- The memory subsystem is identified as the primary performance bottleneck (analysis from measurements).

## Measurement Context

- Hardware version: Sophon SG2042 in Milk-V Pioneer Box, 64-core T-Head XuanTie C920, 128GB DDR4, 2GHz
- Software/toolchain version: XuanTie GCC 20210618 (GCC 8.4), -O3; NAS Parallel Benchmark suite with OpenMP and MPI
- Workload shape: NPB pseudo-applications (including MG - Multi-Grid; other benchmark shapes not fully specified)
- Metric: Single-core performance improvement factor (2.6-16.7x); relative performance on compute-bound vs memory-bound algorithms
- Method: Five runs averaged, exclusive machine usage; single-core and multi-core runs; comparison against other RISC-V, Xeon Platinum 8170 (x86-64), and an AArch64 CPU
- Evidence strength: measured (preprint with experimental results)

## Relationships

- [[sophon-sg2042-hardware-target]]: This benchmark result characterizes the SG2042 hardware target, identifying its memory subsystem as the primary performance bottleneck.

## Sources

- arXiv:2406.12394 ("Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC", Brown and Jamieson, June 2024) — also available at https://arxiv.org/html/2406.12394v1
