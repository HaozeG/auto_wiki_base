---
canonical_name: PULP Platform
aliases:
- PULP
- Parallel Ultra-Low-Power
- Parallel Ultra Low Power
- PULP project
- PULP platform
- Parallel Ultra-Low Power Platform
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/fe63c3e8312ec174.md
- https://pulp-platform.org/
- raw/cache/9e7ec2d830fe2c54.md
- https://www.pulp-platform.org/
- raw/cache/cbbed81bf44e4778.md
- https://github.com/pulp-platform/pulp
- raw/cache/589a5c4a2ff7e749.md
- https://arxiv.org/html/2412.20391v1
source_url: https://pulp-platform.org/
fetched_at: '2026-07-02T10:48:56.293306+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# PULP Platform

PULP (Parallel Ultra-Low-Power) is an open-source multi-core computing platform developed through a collaboration between ETH Zurich and the University of Bologna, initiated in 2013. It targets IoT end-node applications that require flexible processing of data streams from multiple sensors, such as accelerometers, low-resolution cameras, microphone arrays, and vital signs monitors. The PULP platform offers efficient implementations of RISC-V cores, complete systems, and peripherals for IoT applications. Its architecture includes either the RI5CY core or the zero-riscy core as the main processor, an autonomous Input/Output subsystem (uDMA), and a new memory subsystem. The platform also includes a tightly-coupled cluster of processors to which compute-intensive kernels can be offloaded from the main processor. PULP represents a significant advancement over PULPino in terms of completeness and complexity, with support for autonomous I/O, advanced data pre-processing, external interrupts, and multiple processor cores.

## Key Claims

- PULP is an open-source multi-core RISC-V platform targeting IoT end-node applications.
- It uses either the RI5CY or zero-riscy core as the main processor.
- The platform includes an autonomous I/O subsystem (uDMA) for efficient data handling.
- Compute-intensive kernels can be offloaded to a tightly-coupled cluster of processors.
- PULP supports flexible processing of sensor data streams (accelerometers, cameras, microphones, vital signs monitors).
- The platform is a collaboration between ETH Zurich and University of Bologna, started in 2013.
- PULP includes a memory subsystem and peripheral support for IoT.
- The project provides a full simulation platform with JTAG emulation, support for SPI, I2C, I2S peripheral models, and a RISC-V GNU toolchain.

## Relationships

- [[voyager-development-platform]]: related via shared platform.

- [[cpa-factored-gemmini-systolic-array]]: Both are open-source RISC-V-based projects; Gemmini is a systolic array generator for machine learning, while PULP is a general-purpose IoT platform.
- [[earth-shifting-based-vector-memory-access]]: This optimization targets the Saturn RISC-V vector unit, another open-source RISC-V hardware project; PULP and Saturn are both part of the open RISC-V ecosystem.

## Sources

- [PULP Platform Official Website](https://pulp-platform.org/)
- [PULP GitHub Organization](https://github.com/pulp-platform)
- [PULP Project Repository](https://github.com/pulp-platform/pulp)
