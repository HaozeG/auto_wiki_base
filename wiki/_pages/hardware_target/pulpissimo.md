---
canonical_name: PULPissimo
aliases:
- PULPissimo SoC
- PULPissimo microcontroller
subtype: null
tags:
- PULP
- RISC-V
- microcontroller
- ultra-low-power
hardware_targets:
- PULPissimo
toolchains:
- PULP SDK
- RISC-V GNU Toolchain
constraints:
- RV32I, RV32C, RV32M, optional RV32F
- RISC-V Privileged Specification 1.10 subset
- RISC-V External Debug Support 0.13
- Optional Physical Memory Protection (PMP)
- Optional User Mode
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.4
  hub_potential: 0.5
sources:
- raw/cache/b8a59cb8e81fc9a5.md
- https://github.com/pulp-platform/pulpissimo
source_url: https://github.com/pulp-platform/pulpissimo
fetched_at: '2026-07-02T04:57:37.562631+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: k230
  reason: Both are RISC-V-based SoCs; K230 integrates C908 cores while PULPissimo
    uses RI5CY/Ibex and serves as controller for larger PULP systems
- target: xuantie_c908
  reason: The RI5CY core in PULPissimo is another RISC-V in-order core, offering a
    contrast to the C908's vector-enabled design; PULPissimo targets ultra-low-power
    MCU applications rather than AI acceleration. Insufficient context for additional
    cross-links – closely related PULP platform pages (e.g., pulpino, pulp) are not
    yet present in the wiki
---

# PULPissimo

PULPissimo is a single-core microcontroller architecture developed as part of the PULP (Parallel Ultra-Low-Power) platform collaboration between ETH Zurich and the University of Bologna, started in 2013. It serves as the main System-on-Chip (SoC) controller for recent multi-core PULP chips, handling autonomous I/O, advanced data pre-processing, and external interrupts. The architecture supports either the RI5CY core or the Ibex core as the main processor, and includes an Autonomous Input/Output subsystem (uDMA), a new memory subsystem, support for Hardware Processing Engines (HWPEs), a simple interrupt controller, new peripherals, and a new SDK. RI5CY is an in-order, single-issue core with 4 pipeline stages, supporting RV32I, RV32C, RV32M, and optionally RV32F, along with ISA extensions for hardware loops, post-incrementing loads/stores, bit-manipulation, MAC, fixed-point, packed-SIMD, and dot product. Ibex is a 2-stage in-order core supporting RV32I, RV32C, optionally RV32M and RV32E, and is maintained by lowRISC. The uDMA subsystem enables autonomous peripheral communication, offloading the core. Peripherals include SPI, I2S, Camera Interface (CPI), I2C, UART, Hyperbus, and JTAG. Hardware accelerators can be integrated as HWPEs that share memory with the core.

## Key Claims

- Single-core platform used as the SoC controller for multi-core PULP chips, managing autonomous I/O, data pre-processing, and interrupts.
- Supports two processor options: RI5CY (4-stage, in-order, single-issue) or Ibex (2-stage, in-order).
- RI5CY implements RV32I, RV32C, RV32M, optional RV32F, and additional ISA extensions including hardware loops, post-incrementing load/store, bit-manipulation, MAC, fixed-point, packed-SIMD, and dot product.
- Ibex implements RV32I, RV32C, optional RV32M and RV32E, with Machine ISA version 1.11 and RISC-V External Debug Support 0.13.2.
- Includes an autonomous I/O subsystem (uDMA) for peripheral communication without core intervention.
- Supports integration of Hardware Processing Engines (HWPEs) as memory-mapped accelerators.
- Peripherals: SPI (master), I2S, CPI, I2C, UART, Hyperbus, JTAG.
- An example MAC accelerator provided in `ips/hwpe-mac-engine`.
- Presented at WOSH 2019; datasheet and slides available.

## Optimization-Relevant Details

- ISA/profile: RV32I, RV32C, RV32M, optional RV32F; RISC-V Privileged Specification 1.10 subset; PMP optional; Debug 0.13.
- Vector/matrix/accelerator support: No vector unit; HWPEs provide custom accelerator integration via shared memory.
- Memory/cache/TLB/DMA: uDMA subsystem for autonomous data transfers; new memory subsystem (specific hierarchy not detailed in this source).
- Compiler/toolchain support: PULP SDK, RISC-V GNU toolchain.

## Relationships

- [[k230]]: Both are RISC-V-based SoCs; K230 integrates C908 cores while PULPissimo uses RI5CY/Ibex and serves as controller for larger PULP systems.
- [[xuantie_c908]]: The RI5CY core in PULPissimo is another RISC-V in-order core, offering a contrast to the C908's vector-enabled design; PULPissimo targets ultra-low-power MCU applications rather than AI acceleration. Insufficient context for additional cross-links – closely related PULP platform pages (e.g., pulpino, pulp) are not yet present in the wiki.

## Sources

- https://github.com/pulp-platform/pulpissimo
- Schiavone et al., "Quentin: an Ultra-Low-Power PULPissimo SoC in 22nm FDX," IEEE S3S 2018, doi:10.1109/S3S.2018.8640145.
