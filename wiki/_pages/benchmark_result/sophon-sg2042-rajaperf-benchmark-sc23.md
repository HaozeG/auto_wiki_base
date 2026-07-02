---
canonical_name: Sophon SG2042 RAJAPerf Benchmark (SC'23)
aliases:
- SG2042 RAJAPerf results
- Brown et al. 2023 SG2042 benchmark
subtype: null
tags:
- RISC-V
- HPC
- RAJAPerf
- SG2042
hardware_targets:
- Sophon SG2042
workloads:
- HPC kernels (RAJAPerf suite)
datatypes: []
metrics:
- per-core performance ratio
- multi-threaded performance ratio
toolchains:
- RAJAPerf
hardware_versions:
- Sophon SG2042 (64-core XuanTie C920, 2 GHz presumed)
software_versions: []
measurement_method: Comparative benchmarking using the RAJAPerf suite, measuring execution
  time ratios between the SG2042, nearest RISC-V hardware, and x86 CPUs.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/f027de9f838085f3.md
- https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/
source_url: https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/
fetched_at: '2026-07-02T12:42:20.656164+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Sophon SG2042 RAJAPerf Benchmark (SC'23)

A benchmark evaluation of the Sophon SG2042 64-core RISC-V CPU was published in the SC'23 Workshops proceedings by researchers at the University of Edinburgh. Using the RAJAPerf benchmarking suite, the study measured per-core and multithreaded performance relative to the nearest comparable RISC-V hardware and modern x86 high-performance CPUs. The results are reported as performance ratios without absolute throughput numbers. The SG2042 delivered 5x to 10x per-core performance compared to other RISC-V hardware but was 4x to 8x slower than x86 CPUs in multithreaded workloads. Some individual kernels within the RAJAPerf suite achieved faster performance on the SG2042 compared to x86, highlighting cases where the RISC-V design excels. The measurement context includes the Sophon SG2042 (XuanTie C920 cores, 64 cores) and unspecified x86 CPUs representative of modern supercomputers. The evidence strength is reported, as the study is a peer-reviewed conference paper.

## Key Claims

- Per-core performance of the SG2042 is 5x to 10x higher than the nearest widely available RISC-V hardware (RAJAPerf suite).
- Multi-threaded performance of the SG2042 is 4x to 8x lower than high-performance x86 CPUs on the same suite.
- Some individual RAJAPerf kernels run faster on the SG2042 than on x86, indicating workload-specific advantages.
- The benchmarking methodology uses RAJAPerf, an established HPC benchmark suite.

## Measurement Context

- Hardware version: Sophon SG2042 (64-core, XuanTie C920 cores, 2 GHz typical).
- Software/toolchain version: Not specified; RAJAPerf suite used as the benchmark.
- Workload shape: General HPC kernels from the RAJAPerf suite; individual kernel names not disclosed in the available abstract.
- Metric: Performance ratio (relative speedup/slowdown).
- Method: Comparative execution time measurements; SG2042 versus nearest RISC-V hardware and x86 CPUs.
- Evidence strength: reported (peer-reviewed conference paper).

## Relationships

- [[sophon-sg2042]]: The hardware target that was benchmarked.
- Insufficient context for additional cross-links to entity pages within the wiki.

## Sources

- [Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU](https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/)
