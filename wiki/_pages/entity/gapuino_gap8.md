---
cold_start: false
created: '2025-01-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.5
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://docs.platformio.org/en/stable/boards/riscv_gap/gapuino.html
tags:
- risc-v
- greenwaves
- iot
- microcontroller
- development-board
type: entity
updated: '2026-06-28'
---

# GAPuino GAP8

The GAPuino is a development board produced by GreenWaves Technologies featuring the GAP8 IoT application processor, a RISC-V based microcontroller designed for intelligent sensing devices that capture and analyze data from sources such as images, sounds, or vibrations. The board operates at a frequency of 250 MHz and provides 64 MB of Flash memory and 8 MB of RAM, making it suitable for edge AI applications requiring moderate on-board processing and storage. It is fully supported by the PlatformIO development ecosystem, offering a straightforward configuration using the board identifier `gapuino` within the `riscv_gap` platform. The GAPuino includes an on-board FTDI debug probe, enabling one-click debugging without the need for an external debug tool. Software development can leverage either the Arm Mbed OS or the PULP OS SDK, the latter being purpose-built for GreenWaves' GAP processors.

## Key Claims

- The GAPuino board uses the GreenWaves GAP8 microcontroller, a RISC-V IoT application processor.
- CPU frequency: 250 MHz.
- On-board memory: 64 MB Flash and 8 MB RAM.
- Vendor: GreenWaves Technologies.
- Integrated on-board debug probe (FTDI) for zero-configuration debugging.
- Supported frameworks: Mbed OS and PULP OS.
- PlatformIO board ID: `gapuino`; configuration via `[env:gapuino]` with `platform = riscv_gap`, `board = gapuino`.

## Relationships

- [[risc_v_vector_extension]]: GAP8 is a RISC-V based processor; the Vector Extension standard is part of the broader RISC-V ISA ecosystem, though GAP8 uses custom PULP extensions rather than the ratified RVV.
- [[alibaba_xuantie_c910_c920]]: Represent high-performance RISC-V core implementations targeting server and edge AI, contrasting with the ultra-low-power GAP8 IoT application processor.

## Sources

- https://docs.platformio.org/en/stable/boards/riscv_gap/gapuino.html
