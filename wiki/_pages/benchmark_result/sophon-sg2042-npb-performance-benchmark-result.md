---
canonical_name: SG2042 NAS Parallel Benchmark Performance
aliases:
- SG2042 NPB results
- SG2042 HPC benchmarking
- NPB Performance of the Sophon SG2042
- NAS Parallel Benchmarks on SG2042
subtype: null
tags: []
hardware_targets:
- SOPHON SG2042
workloads:
- NAS Parallel Benchmark (NPB) suite
datatypes: []
metrics:
- Single-core performance improvement (2.6x-16.7x vs other RISC-V CPUs)
- Relative performance on compute-bound vs memory-bound algorithms
toolchains:
- XuanTie GCC 20210618 (GCC 8.4)
- GCC (optimization level 3)
hardware_versions:
- Sophon SG2042 (2 GHz, 64 cores)
- Milk-V Pioneer Box with 128 GB DDR4
software_versions:
- XuanTie GCC 20210618 (GCC 8.4) at -O3
- No operating system version given (Linux assumed)
measurement_method: Averaged over five runs, exclusive machine access per run; single-core
  and multi-core measurements taken; all codes compiled with optimization level 3.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/b8ccce9b3180873d.md
- https://arxiv.org/html/2406.12394v1
- raw/cache/5b1c2c5ef89a99ef.md
- https://arxiv.org/abs/2406.12394
source_url: https://arxiv.org/html/2406.12394v1
fetched_at: '2026-07-03T16:53:59.296103+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: sophon-sg2042-hardware-target
  reason: This benchmark evaluates the hardware target described on that page, providing
    measured performance context for the SG2042 CPU
- target: sophon-sg2044-hardware-target
  reason: The SG2044's key improvement over the SG2042 is an enhanced memory subsystem,
    which directly addresses the memory bottleneck identified in this benchmark result
---

# SG2042 NAS Parallel Benchmark Performance

This benchmark result reports the performance evaluation of the Sophon SG2042 RISC-V CPU on the NASA NAS Parallel Benchmark (NPB) suite, conducted by EPCC at the University of Edinburgh. The hardware configuration was a Milk-V Pioneer Box containing a 2 GHz SG2042 processor with 128 GB of DDR4 RAM. The software used was the XuanTie GCC compiler fork version 20210618 (GCC 8.4) at optimization level 3, which is the recommended version for best auto-vectorization on the C920 core's RVV v0.7.1 vector unit. All results were averaged over five runs with exclusive machine access. The study compared the SG2042 against other RISC-V CPUs as well as x86-64 and AArch64 CPUs commonly deployed in HPC systems.

## Key Claims

- At the single-core level on NPB benchmarks, the SG2042 delivers a performance improvement of 2.6x to 16.7x over other commodity RISC-V CPUs (measured).
- For computationally bound algorithms, the SG2042 performs comparatively well against x86-64 and AArch64 HPC CPUs (measured).
- The SG2042's relative performance decreases for algorithms that are memory bandwidth- or latency-bound, identifying the memory subsystem as the primary performance bottleneck (measured).

## Measurement Context

- Hardware version: Sophon SG2042, 2 GHz, 64 cores, Milk-V Pioneer Box with 128 GB DDR4 (four DDR4-3200 controllers).
- Software/toolchain version: XuanTie GCC 20210618 (GCC 8.4), optimization level 3. NPB suite version not specified.
- Workload shape: NAS Parallel Benchmark (NPB) suite, including kernels Integer Sort (IS), Multi Grid (MG), Embarrassingly Parallel (EP), Conjugate Gradient (CG), Fast Fourier Transform (FT), and pseudo-applications. Problem sizes not detailed in the available source excerpt.
- Metric: Performance improvement ratio (2.6x-16.7x for single-core vs other RISC-V); qualitative characterization for compute-bound vs memory-bound relative to x86-64/AArch64.
- Method: Average of five runs, exclusive machine access per run.
- Evidence strength: measured (the paper describes controlled benchmarking experiments on physical hardware).

## Relationships

- [[sophon-sg2042-hardware-target]]: This benchmark evaluates the hardware target described on that page, providing measured performance context for the SG2042 CPU.
- [[sophon-sg2044-hardware-target]]: The SG2044's key improvement over the SG2042 is an enhanced memory subsystem, which directly addresses the memory bottleneck identified in this benchmark result.

## Sources

- https://arxiv.org/html/2406.12394v1 (full HTML paper); also available at https://arxiv.org/abs/2406.12394
