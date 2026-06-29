---
cold_start: false
constraints:
- 8-wide out-of-order decode
- 6 integer ALUs
- 2 branch execution units
- 3 load/store pipelines
- 2 FPU/SIMD pipelines (256-bit each)
- 128KB L1 data cache (8-way)
- TAGE branch predictor
- support for RV64ACDHFMV ISA
- support for vector extensions (RVV)
- no SMT
- 32 bytes per cycle instruction fetch
- deep reorder buffer (not disclosed)
created: '2025-03-25'
hardware_targets:
- Tenstorrent Ascalon
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.85
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.95
sources:
- https://www.hwcooling.net/en/jim-kellers-new-firm-prepares-risc-v-version-of-apples-powerful-cpus/
- https://www.tomshardware.com/
tags:
- RISC-V
- Tenstorrent
- Ascalon
- Jim Keller
- out-of-order
- wide core
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Ascalon

The Tenstorrent Ascalon is a high-performance RISC-V microarchitecture developed by Tenstorrent, led by Jim Keller, targeting server, HPC, and laptop segments. It implements an 8-wide out-of-order decode pipeline, significantly wider than most current RISC-V cores, with six integer ALUs, two branch execution units, and three load/store pipelines. The core supports the RV64ACDHFMV instruction set with vector extensions and features a TAGE-class branch predictor. The L1 data cache is 128KB with 8-way associativity. Ascalon continues the trend of wide RISC-V designs inspired by Apple's high-performance cores, aiming to compete with x86 and ARM in the highest performance tiers. The architecture is designed by Wei-Han Lien, who previously worked on AMD K6, PA-Semi, and Apple A6/A7/M1 chips. Raja Koduri has joined the board of Tenstorrent.

## Key Claims

- 8-wide instruction decode per cycle, matching Apple's current large cores.
- Six integer ALUs and two branch execution units for out-of-order execution.
- Three load/store pipelines (vs. Apple's four), supporting a combination of three reads or writes per clock.
- Two 256-bit FPU/SIMD pipelines, capable of processing RVV vector operations.
- 128KB L1 data cache, 8-way set-associative, similar to Apple core design.
- TAGE-type branch predictor, considered necessary for high-performance out-of-order cores.
- Support for RV64ACDHFMV ISA with virtualization and vector extensions.
- No SMT (Simultaneous Multithreading) capability reported.
- Deep reorder buffer expected to support high IPC, though exact size not disclosed.
- Instruction fetch width of 32 bytes per cycle.

## Optimization-Relevant Details

- ISA/profile: RV64ACDHFMV (includes vector and virtualization extensions).
- Vector/matrix/accelerator support: Two 256-bit SIMD units; supports RVV vector extensions.
- Memory/cache/TLB/DMA: 128KB L1 data cache (8-way), 32B per cycle instruction fetch; L1 instruction cache details not fully disclosed; deep load/store queues; cache parameters for higher levels not disclosed.
- Compiler/toolchain support: No specific toolchain versions provided in source; RISC-V GCC and LLVM are expected to support this core when available.

## Relationships

- [[SiFive_P550_and_T-HEAD_C910_Benchmark_Comparison]] – A comparison of earlier RISC-V performance cores, providing context for Ascalon's ambitious specifications.
- [[RVV_Autovectorization_Optimization_Insights]] – Relevant for understanding how compilers optimize for RISC-V vector extensions, which Ascalon supports.

## Sources

- HWCooling.net article summarizing Tom's Hardware reports: [Jim Keller's new firm plans RISC-V CPUs with Apple-like wide cores](https://www.hwcooling.net/en/jim-kellers-new-firm-prepares-risc-v-version-of-apples-powerful-cpus/)
- Tom's Hardware original coverage (referenced in the article).
