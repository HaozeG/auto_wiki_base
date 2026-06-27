---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://docs.openhwgroup.org/projects/cv32e40p-user-manual/en/latest/intro.html
tags:
- RISC-V
- CORE-V
- CV32E40P
- OpenHW Group
- PULP
- processor core
type: entity
updated: '2026-06-27'
---

# CV32E40P RISC-V Core

The CV32E40P is a 4-stage in-order 32-bit RISC-V processor core designed by the OpenHW Group, derived from the RI5CY core originally developed by ETH Zurich and the University of Bologna as part of the PULP platform. It implements the RV32I base integer instruction set version 2.1 along with standard extensions including C (compressed instructions), M (integer multiply/divide), Zicntr (performance counters), Zicsr (CSR instructions), Zifencei (instruction-fetch fence), and optionally F (single-precision floating-point) via an integrated FPU or Zfinx using X registers. Additionally, it supports custom CORE-V PULP ISA extensions (Xcv) and cluster extensions (Xcvelw) for hardware loops, post-increment load/store, SIMD, and other DSP-oriented operations. The core's instruction fetch and load/store interfaces are compliant with the Open Bus Interface (OBI) protocol, and it includes debug support compatible with RISC-V External Debug Specification v0.13.2. Designed for embedded and IoT applications, the CV32E40P balances performance and area efficiency with a small footprint and configurable features.

## Key Claims

- The CV32E40P uses a 4-stage in-order pipeline and is a 32-bit RISC-V core.
- It implements the RV32I base integer instruction set at version 2.1.
- Mandatory standard extensions (all version 2.0) include: C (compressed instructions), M (integer multiply/divide), Zicntr (performance counters), Zicsr (CSR instructions), Zifencei (instruction-fetch fence).
- Optional standard extensions: F (single-precision floating-point) version 2.2 (enabled via FPU parameter), Zfinx (single-precision floating-point using X registers) version 1.0 (requires FPU parameter).
- Custom extensions: Xcv (CORE-V PULP ISA) version 1.0, Xcvelw (CORE-V PULP Cluster ISA) version 1.0, both enabled by corresponding parameters.
- The core's bus interfaces (instruction fetch and data load/store) are compliant with the Open Bus Interface (OBI) protocol.
- Debug infrastructure follows RISC-V External Debug Specification draft version 0.13.2.
- Machine-level ISA version 1.11 is supported, including all CSRs, hardware performance counters (configurable via NUM_MHPMCOUNTERS), and trap handling (direct or vectored mode).
- The core is parameterizable; features such as the FPU, ZFINX, COREV_PULP, COREV_CLUSTER, and the number of performance counters are configurable via parameters.
- Licensed under the Solderpad Hardware License Version 0.51, copyright by OpenHW Group (2023) and ETH Zurich and University of Bologna (2018).
- The core originated as a fork of the OR10N core (OpenRISC ISA), was later adapted to RISC-V under the name RI5CY in 2016, and is maintained within the PULP platform ecosystem.

## Relationships

- This core is part of the OpenHW Group's CORE-V family and traces its lineage to the RI5CY core from the PULP platform. It is a concrete implementation of the RISC-V ISA and serves as a reference for embedded-class RISC-V cores.
- No direct existing wiki pages are currently linked, but the core relates to potential future pages on the RISC-V ISA, the PULP platform, and the OBI protocol.

## Sources

- https://docs.openhwgroup.org/projects/cv32e40p-user-manual/en/latest/intro.html
