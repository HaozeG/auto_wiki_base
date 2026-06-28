---
cold_start: true
created: '2025-10-10'
datatypes: []
evidence_strength: measured
hardware_targets:
- DC-ROMA AI PC RISC-V Mainboard II
- SiFive P550
hardware_versions:
- DC-ROMA AI PC RISC-V Mainboard II rev. 2025; 8-core SiFive P550 at 1.8 GHz
inbound_links: 0
measurement_method: 'Benchmarks were run on the board with 32GB RAM (16GB CPU) and
  512GB SSD. CPU: Geekbench 6; HPL from top500-benchmark repository. GPU: glmark2-es2-wayland.
  Disk: iozone. Network: iperf3 via WiFi 6. Power: measured at wall with power meter.'
metrics:
- Geekbench single score
- Geekbench multi score
- Gflops
- Power draw
- MB/s disk read/write
- Mbps network
- glmark2 score
scorecard:
  bridge_score: 0.7
  claim_density: 1.0
  hub_potential: 0.6
  novelty_delta: 1.0
  self_containedness: 1.0
software_versions:
- Ubuntu 24.04
- Kernel 6.6.92-eic7x-2025.07
- glmark2 2023.01
sources:
- https://github.com/geerlingguy/sbc-reviews/issues/82
tags:
- RISC-V
- SiFive P550
- DC-ROMA
- benchmark
- Geekbench
- HPL
- iozone
- iperf3
- glmark2
toolchains: []
type: benchmark_result
updated: '2026-06-28'
workloads:
- Geekbench 6
- TOP500 HPL
- iozone disk benchmark
- iperf3 network benchmark
- glmark2 GPU benchmark
---

# DC-ROMA AI PC Benchmarks

The DC-ROMA AI PC RISC-V Mainboard II was benchmarked by Jeff Geerling on October 10, 2025, using a standard Ubuntu 24.04 installation with kernel 6.6.92-eic7x-2025.07. The system features an 8-core 1.8 GHz SiFive P550 CPU, 32GB RAM (16GB allocated to CPU), and a 512GB ZHITAI TiPlus7100 SSD. The benchmark suite includes CPU performance via Geekbench 6 and TOP500 HPL, disk I/O via iozone, network throughput via iperf3 on WiFi 6, and GPU performance via glmark2. These measurements provide a comprehensive view of the board's capabilities for AI PC workloads, including compute, storage, network, and graphics performance.

## Key Claims

- Geekbench 6 single-core score: 174; multi-core score: 640.
- HPL benchmark: 17.759 Gflops at 32.5W, efficiency of 0.55 Gflops/W.
- Sleep power draw: 2.2W; idle: 25.1W; maximum load: 32.9W.
- Disk (iozone): 4K random read 60.31 MB/s, write 126.92 MB/s; 1M sequential read 1076.06 MB/s, write 1301.79 MB/s.
- Network (iperf3 WiFi 6): 637 Mbps down, 293 Mbps up, 510/141 Mbps bidirectional.
- GPU glmark2 score: 936.

## Measurement Context

- Hardware version: DC-ROMA AI PC RISC-V Mainboard II with 8-core SiFive P550 at 1.8 GHz, 32GB RAM (16GB CPU), 512GB ZHITAI TiPlus7100 SSD.
- Software/toolchain version: Ubuntu 24.04, Linux kernel 6.6.92-eic7x-2025.07, glmark2 2023.01.
- Workload shape: Geekbench 6 (multi- and single-threaded), TOP500 HPL (double-precision Linpack), iozone (4K and 1M random/sequential), iperf3 (TCP over WiFi 6), glmark2 (OpenGL ES 2.0 benchmark).
- Metric: Scores, Gflops, power in watts, MB/s, Mbps, FPS.
- Method: Benchmarks run with default settings. Power measured at wall outlet.
- Evidence strength: measured.

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Comparable RISC-V CPU benchmarks on a different core (C910 vs P550).
- [[Sipeed_MAIX_series]] – Both are RISC-V platforms, though the MAIX uses a lower-power K210 with NPU.

## Sources

- [geerlingguy/sbc-reviews Issue #82 - DC-ROMA AI PC - RISC-V Mainboard II](https://github.com/geerlingguy/sbc-reviews/issues/82)
