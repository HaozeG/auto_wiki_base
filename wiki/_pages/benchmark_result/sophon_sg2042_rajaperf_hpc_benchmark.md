---
canonical_name: Sophon SG2042 RAJAPerf HPC Benchmark
aliases:
- SG2042 RAJAPerf
- Sophon SG2042 RAJAPerf performance
subtype: null
tags:
- benchmark
- RAJAPerf
- HPC
- Sophon SG2042
hardware_targets:
- Sophon SG2042
workloads:
- RAJAPerf HPC loop-based kernels
datatypes:
- FP32
- FP64
- INT32
- INT64
metrics:
- per-core performance ratio (5-10x vs other RISC-V)
- multi-threaded performance ratio (4-8x slower vs x86 HPC)
toolchains:
- T-Head GCC 8.4 (20210618)
hardware_versions:
- Sophon SG2042 @2GHz, Milk-V Pioneer Box, 32GB RAM, 1TB SSD
software_versions:
- RAJAPerf (version unspecified)
- T-Head GCC 8.4 (20210618)
measurement_method: Average of five runs, exclusive machine use, command-line execution
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/f2a04d0bd66a1c7d.md
- https://arxiv.org/html/2309.00381
source_url: https://arxiv.org/html/2309.00381
fetched_at: '2026-07-02T07:24:53.549820+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Sophon SG2042 RAJAPerf HPC Benchmark

This benchmark evaluates the performance of the Sophon SG2042 64-core RISC-V CPU using the RAJAPerf HPC benchmarking suite, comparing it against existing RISC-V hardware and high-performance x86 CPUs. On average, the SG2042 delivers per-core performance between five and ten times that of the nearest widely available RISC-V hardware, while x86 high-performance CPUs outperform the SG2042 by four to eight times for multi-threaded workloads. The benchmark was conducted on a Milk-V Pioneer Box with 32GB of RAM and a 1TB SSD, using the T-Head GCC 8.4 compiler from the 20210618 release at optimization level -O3. Results are averaged over five runs, with each benchmark making exclusive use of the machine. The RAJAPerf suite provides a set of loop-based computational kernels common in HPC applications, though the specific subset used is not detailed in the source.

## Key Claims

- Per-core performance: 5-10x improvement over nearest widely available RISC-V hardware (e.g., embedded SBCs).
- Multi-threaded performance: 4-8x slower than x86 HPC CPUs used in modern supercomputers.
- Some individual kernels execute faster on the SG2042 than on x86, though overall averages favor x86.

## Measurement Context

- Hardware version: Sophon SG2042 @2GHz, Milk-V Pioneer Box with 32GB RAM and 1TB SSD.
- Software/toolchain version: T-Head GCC 8.4 (20210618), RAJAPerf suite (version unspecified), Linux command-line execution.
- Workload shape: Loop-based HPC kernels from RAJAPerf (unspecified specific kernels).
- Metric: Relative performance ratios (per-core and multi-threaded).
- Method: Independent benchmarking, five-run average, exclusive machine access, compiled with -O3.
- Evidence strength: measured

## Relationships

- The hardware platform used is the [[sophon_sg2042_hpc_cpu]], which provides detailed architecture and compiler context.
- The RVV v0.7.1 vector engine in this chip differs from the RVV 1.0 implementation found in the [[coral_npu_vector_execution_engine]], affecting compiler support and performance.
- This benchmark provides a performance data point that can be compared against other RISC-V HPC benchmarks on [[sifive_performance_p570_gen3]].

## Sources

- Nick Brown et al., "Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU", arXiv:2309.00381, 2023.
