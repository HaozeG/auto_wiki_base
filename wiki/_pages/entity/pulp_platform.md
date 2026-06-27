---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://github.com/pulp-platform/pulp
tags:
- risc-v
- ultra-low-power
- iot
- open-source
- parallel-computing
type: entity
updated: '2026-06-27'
---

# PULP Platform

PULP (Parallel Ultra-Low-Power) is an open-source multi-core computing platform developed collaboratively by ETH Zurich and the University of Bologna since 2013. It targets IoT end-node applications that require flexible processing of data streams from multiple sensors, such as accelerometers, low-resolution cameras, microphone arrays, and vital signs monitors. The architecture includes a tightly-coupled cluster of processors, an autonomous I/O subsystem (uDMA), support for hardware processing engines (HWPEs), and multiple RISC-V cores including the RI5CY and zero-riscy cores. PULP significantly advances beyond the earlier PULPino design by providing advanced features like autonomous I/O, external interrupt handling, and a system DMA. The platform uses the RISC-V instruction set architecture with extensions such as hardware loops, post-incrementing loads/stores, bit-manipulation, and packed-SIMD to improve energy efficiency in signal processing applications. PULP supports integration of hardware accelerators that share memory with the main core and are programmed via the memory map, enabling customized data processing pipelines for edge computing workloads.

## Key Claims

- PULP is an open-source multi-core computing platform for IoT edge processing, developed by ETH Zurich and University of Bologna (started 2013).
- The RI5CY core is an in-order, single-issue core with 4 pipeline stages and IPC close to 1; it supports RV32I, RV32C, RV32M, optional RV32F, and custom ISA extensions including hardware loops, post-incrementing load/store, bit-manipulation, MAC, fixed-point operations, packed-SIMD, and dot product. It implements a subset of the RISC-V privileged specification 1.9.
- The zero-riscy core is an in-order, single-issue core with 2 pipeline stages; it supports RV32I, RV32C, optional RV32M and RV32E, and is designed for ultra-low-power and ultra-low-area constraints.
- PULP includes an autonomous I/O subsystem via a micro-DMA (uDMA) that communicates with peripherals autonomously; the core only programs the uDMA and waits for the transfer to complete.
- Supported I/O interfaces include SPI (master), I2S, Camera Interface (CPI), I2C, UART, and JTAG.
- Hardware Processing Engines (HWPEs) can be integrated as accelerators sharing memory with the RI5CY core; an example multiply-accumulate engine is provided in the `hwpe-mac-engine` repository.
- The platform includes a new memory subsystem, simple interrupt controller, event unit, and SDK.
- The PULP toolchain is based on the RISC-V GNU toolchain; building the RTL simulation platform uses the bender dependency manager.
- The Mr.Wolf SoC, based on PULP, was published in IEEE Journal of Solid-State Circuits in 2019 (DOI: 10.1109/JSSC.2019.2912307).

## Relationships

- [[RISC-V]] — PULP implements RISC-V cores (RI5CY, zero-riscy) and extends the ISA with custom instructions for energy efficiency.
- [[PULPino]] — PULP is a more advanced architecture building upon PULPino, adding autonomous I/O, cluster computing, and advanced preprocessing.
- [[RI5CY core]] — The main processing core in PULP, supporting multiple ISA extensions.
- [[zero-riscy core]] — The ultra-low-power core option in PULP.
- [[Hardware Processing Engine]] — PULP supports integration of HWPEs for custom accelerators.
- [[uDMA]] — The autonomous I/O subsystem used in PULP.

## Sources

- GitHub repository: https://github.com/pulp-platform/pulp
- Mr.Wolf paper: Pullini et al., IEEE JSSC 2019, DOI: 10.1109/JSSC.2019.2912307
