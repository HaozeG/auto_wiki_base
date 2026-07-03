---
canonical_name: StarFive JH-7110
aliases:
- JH7110
- JH-7110
subtype: null
tags: []
hardware_targets:
- StarFive JH-7110
toolchains: []
constraints:
- 5 cores (4 P-cores SiFive U74-MC + 1 E-core SiFive S76 + 1 RTC-core SiFive E24)
- 14 nm TSMC fabrication
- Base clock 1250 MHz, boost up to 1500 MHz
- 5 W TDP
- 2 MB shared L2 cache
- Single-channel DDR3/DDR4 up to 2800 MT/s
- PCI-Express Gen 2
- ImgTec BXE-4-32 GPU (400-600 MHz dynamic frequency)
- No SSE instruction set support
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 1.0
  bridge_score: 0.4
  hub_potential: 0.5
sources:
- raw/cache/8dee4d80847b71f6.md
- https://www.techpowerup.com/cpu-specs/jh-7110-soc.c4026
source_url: https://www.techpowerup.com/cpu-specs/jh-7110-soc.c4026
fetched_at: '2026-07-03T17:52:36.853786+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: andes-ax45mpv-hardware-target
  reason: Both the StarFive JH-7110 and the AndesCore AX45MPV are RISC-V based SoCs,
    but the JH-7110 is a specific mobile processor product using SiFive cores and
    targeting single-board computers, while the AX45MPV is a licensable CPU IP core
    from Andes Technology designed for data-intensive workloads such as AI and signal
    processing
---

# StarFive JH-7110

The StarFive JH-7110 SoC is a 64-bit RISC-V mobile processor launched in August 2022, fabricated on a 14 nm TSMC process. It features a heterogeneous core configuration with four SiFive U74-MC application cores and one SiFive S76 real-time core, plus a dedicated SiFive E24 RTC core. The processor operates at a base frequency of 1250 MHz with a boost up to 1500 MHz, and has a thermal design power of 5 W. It integrates 2 MB of shared L2 cache, supports single-channel DDR3/DDR4 memory up to 2800 MT/s, and includes an ImgTec BXE-4-32 GPU with a dynamic frequency range of 400-600 MHz. Connectivity includes PCI-Express Gen 2. The JH-7110 is one of the first widely available RISC-V SoCs targeting single-board computers and embedded systems, but it lacks SSE instruction set support, which limits its compatibility with x86-oriented software and games.

## Key Claims

- Heterogeneous 5-core configuration: 4× SiFive U74-MC (application), 1× SiFive S76 (real-time), 1× SiFive E24 (RTC).
- Base frequency 1250 MHz, turbo up to 1500 MHz.
- 5 W TDP.
- Fabricated on TSMC 14 nm process.
- 2 MB shared L2 cache (64 KB L1 per core).
- Single-channel memory controller supporting DDR3 and DDR4 up to 2800 MT/s.
- Integrated ImgTec BXE-4-32 GPU running at 400-600 MHz.
- PCI-Express Gen 2 interface.
- No SSE instruction set support.

## Optimization-Relevant Details

- ISA/profile: RV64GC (P-cores), RV32IMFC (E-core).
- Vector/matrix/accelerator support: None specified.
- Memory/cache/TLB/DMA: L1 64 KB per core, L2 2 MB shared.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[andes-ax45mpv-hardware-target]]: Both the StarFive JH-7110 and the AndesCore AX45MPV are RISC-V based SoCs, but the JH-7110 is a specific mobile processor product using SiFive cores and targeting single-board computers, while the AX45MPV is a licensable CPU IP core from Andes Technology designed for data-intensive workloads such as AI and signal processing.

## Sources

- TechPowerUp CPU Database: StarFive JH-7110 SoC Specs. https://www.techpowerup.com/cpu-specs/jh-7110-soc.c4026
