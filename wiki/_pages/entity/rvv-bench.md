---
canonical_name: rvv-bench
aliases:
- RVV benchmark
- rvv-bench (GitHub Pages)
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.5
sources:
- raw/cache/98241072b9080554.md
- https://camel-cdr.github.io/rvv-bench-results/index.html
source_url: https://camel-cdr.github.io/rvv-bench-results/index.html
fetched_at: '2026-07-02T12:29:55.301590+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# rvv-bench

rvv-bench is a collection of RISC-V Vector (RVV) benchmarks hosted on GitHub Pages, intended to help developers write performance-portable RVV code. The project lists support for multiple processors with RVV 1.0, including SpacemiT X100 (K3), SpacemiT A100 (K3), SpacemiT X60 (Banana Pi BPI-F3, K1), XuanTie C908 (CanMV-K230), Tenstorrent Ascalon X and Ascalon S (hardware simulated), SiFive X280 (Tenstorrent Blackhole), Saturn Shuttle with VLEN=256 DLEN=128 (hardware simulated), and XiangShanV3 (hardware simulated). It also tracks processors with XTheadVector extension: XuanTie C920v1 (Milk-V Pioneer, SG2042), XuanTie C910 (Sipeed Lichee Pi 4A, TH1520), and XuanTie C906 (MangoPi MQ Pro, Allwinner D1), as well as performance models like the AX45MPV running on AndeSim. Additionally, the project features articles on RVV integer workloads, SWAR UTF-8 validation using xperm4, and vectorizing Unicode conversions for real RISC-V hardware. The repository aims to provide a reference for developers evaluating and optimizing RVV code across a range of RISC-V vector-capable hardware.

## Key Claims

- rvv-bench is a publicly hosted collection of RISC-V Vector (RVV) microbenchmarks aimed at developing performance-portable vector code.
- The project lists processors with RVV 1.0 support: SpacemiT X100 (K3), SpacemiT A100 (K3), SpacemiT X60 (Banana Pi BPI-F3, K1), XuanTie C908 (CanMV-K230, Kendryte K230), Tenstorrent Ascalon X and Ascalon S (hardware simulated), SiFive X280 (Tenstorrent Blackhole), Saturn Shuttle (VLEN=256, DLEN=128, simulated), XiangShanV3 (simulated), and others.
- Processors with XTheadVector extension include XuanTie C920v1 (Milk-V Pioneer, SG2042), XuanTie C910 (Sipeed Lichee Pi 4A, TH1520), and XuanTie C906 (MangoPi MQ Pro, Allwinner D1).
- A performance model for the AX45MPV on AndeSim is included, providing near-cycle-accurate simulation.
- The project also references articles on RVV integer workloads, SWAR UTF-8 validation, and Unicode conversion vectorization.

## Relationships

- [[andes-ax45mpv]]: AX45MPV is listed as a performance model in rvv-bench.
- [[ax45mpv-rvv-instruction-throughput]]: The instruction throughput benchmark results for AX45MPV were obtained from rvv-bench.
- (insufficient context for additional cross-links; no other relevant entity pages exist in the current wiki context)

## Sources

- https://camel-cdr.github.io/rvv-bench-results/index.html
