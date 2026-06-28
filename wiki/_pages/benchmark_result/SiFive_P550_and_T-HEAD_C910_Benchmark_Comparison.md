---
cold_start: true
created: YYYY-MM-DD
datatypes: []
evidence_strength: measured
hardware_targets:
- SiFive P550 (EIC7700X)
- T-HEAD C910
hardware_versions:
- EIC7700X with P550 at 1.4 GHz
- C910 at 1.85 GHz
inbound_links: 2
measurement_method: 'Benchmarks run on stock boards with GCC 14.2.0. SPEC CPU2017
  built with march flags specified. 7-Zip: compressing 2.67 GB file with 4 threads.
  SHA256: sha256sum on 2.67 GB file. x264: software video encode using libx264.'
metrics:
- SPEC score
- IPC
- throughput
- time
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 1.0
software_versions: []
sources:
- https://chipsandcheese.com/p/a-risc-v-progress-check-benchmarking
tags:
- RISC-V
- P550
- C910
- SPEC
- benchmark
toolchains:
- GCC 14.2.0
type: benchmark_result
updated: '2026-06-28'
workloads:
- SPEC CPU2017
- 7-Zip
- SHA256
- x264
---------

# SiFive P550 and T-HEAD C910 Benchmark Comparison

This page documents benchmark results for SiFive's Performance P550 core (implemented in the EIC7700X SoC at 1.4 GHz) and T-HEAD's Xuantie C910 core (at 1.85 GHz), as measured by Chester Lam and published on Chips and Cheese on January 30, 2025. The benchmarks include SPEC CPU2017, 7-Zip file compression, SHA256 checksum calculation, and x264 software video encoding. The results are compared against Arm Cortex A73, Intel Goldmont Plus, and Arm Cortex A55 cores. The article highlights that both RISC-V cores suffer from low clock speeds and relatively small out-of-order execution engines, with the P550 demonstrating better IPC and balanced design compared to the C910, but both falling short of comparable Arm and x86 cores in most workloads. The x264 benchmark particularly shows the software ecosystem gap for RISC-V vector extensions, as both cores lack optimized assembly kernels, resulting in very poor performance despite high IPC.

## Key Claims

- SPEC CPU2017 Integer: P550 at 1.4 GHz and C910 at 1.85 GHz both trail Cortex A73 and Goldmont Plus significantly, with clock speed differences playing a large role.
- SPEC CPU2017 Floating Point: C910 wins some tests but fails to take overall lead; P550 shows good IPC but low clock speed limits performance.
- 7-Zip (4-thread compression on 2.67 GB file): P550 and C910 similar performance, both slightly behind in-order Cortex A55 in higher-clocked implementation.
- SHA256 checksum: Cortex A55 takes large lead; P550 and C910 sustain >2 IPC for P550 and near 2 IPC for C910; both execute more instructions than x86 and aarch64.
- x264: Performance disaster for RISC-V cores; they top IPC chart but instruction counts are much higher, making IPC meaningless; libx264 has no assembly optimized for RISC-V vector extensions.
- P550 has a well-balanced out-of-order execution engine, sustaining higher IPC than C910; C910 struggles to utilize its 3-wide width.

## Measurement Context

- Hardware version: SiFive P550 in EIC7700X SoC, clocked at 1.4 GHz (datasheet supports up to 1.8 GHz). T-HEAD C910 in unspecified board, clocked at 1.85 GHz.
- Software/toolchain version: SPEC CPU2017 built with GCC 14.2.0; march flags: P550: -march=rv64imafdc_zicsr_zifencei_zba_zbb -mtune=sifive-p400-series; C910: -march=rv64imafdc_xtheadvector -mtune=generic-ooo. 7-Zip, sha256sum, libx264 from Linux distribution.
- Workload shape: SPEC CPU2017 (full suite). 7-Zip: 2.67 GB file, 4 threads. SHA256: same file. x264: unspecified input.
- Metric: SPEC score (ratios), IPC from performance counters, throughput for application benchmarks.
- Method: Benchmarks run on stock hardware, performance counter data collected via perf.
- Evidence strength: measured

## Relationships

- [[Sipeed_MAIX_series]] - A RISC-V development board platform, though targeting edge AI rather than high-performance computing.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] - A prior benchmark result for the C910 core at 2 GHz, providing additional data points.
(Insufficient context for additional entity cross-links.)

## Sources

- [Chips and Cheese: A RISC-V Progress Check: Benchmarking P550 and C910](https://chipsandcheese.com/p/a-risc-v-progress-check-benchmarking)
