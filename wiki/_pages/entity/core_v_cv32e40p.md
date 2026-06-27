---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.2
  claim_density: 0.95
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://docs.openhwgroup.org/projects/cv32e40p-user-manual/en/latest/intro.html
tags:
- risc-v
- open-hardware
- openhw-group
- pulp
type: entity
updated: '2026-06-27'
---

# CORE-V CV32E40P

The CV32E40P is a 4-stage in-order 32-bit RISC-V processor core developed and maintained by the OpenHW Group. It originated as a fork of the OR10N OpenRISC core and subsequently evolved from the RI5CY core, which was originally developed by ETH Zurich and the University of Bologna as part of the PULP platform. The core implements the RV32I base integer instruction set (version 2.1) along with standard extensions including C (compressed instructions), M (multiply/divide), Zicntr (performance counters), Zicsr (CSR instructions), Zifencei (instruction-fetch fence), and optionally F (single-precision floating-point) and Zfinx (floating-point in integer registers). Custom extensions include the CORE-V PULP ISA extensions (Xcv) and PULP Cluster extensions (Xcvelw). The core uses the Open Bus Interface (OBI) protocol for its instruction and data memory interfaces, improving timing and easing integration with AMBA AXI/AHB. The CV32E40P is fully compliant with RISC-V privileged specification version 1.11 and debug specification draft 0.13.2, with enhanced interrupt handling via a CLINT-compatible controller and 16 fast interrupt lines. The FPU is not instantiated inside the EX stage but as a separate module, and atomic extensions (RV32A), user mode, and PMP are not supported.

## Key Claims

- The core is a 4-stage, in-order, single-issue 32-bit RISC-V processor.
- It supports RV32I v2.1, C v2.0, M v2.0, Zicntr v2.0, Zicsr v2.0, Zifencei v2.0, F v2.2 (optional), Zfinx v1.0 (optional), Xcv v1.0 (optional), and Xcvelw v1.0 (optional).
- Instruction and data memory interfaces use the OBI protocol (v1.2), which eliminates combinatorial dependency of request on rvalid signal.
- The core does not implement the RV32A atomic extensions, user mode (U-mode), or physical memory protection (PMP).
- Interrupts are handled via a CLINT-compatible controller with 16 custom fast interrupt lines for a total of 19 interrupt sources.
- Hardware loop (HWLoop) supports two nested loops with a minimum of two instructions per loop; loops can be misaligned.
- Custom CSR address re-mapping moved PULP HWLoop CSRs from 0x7C* to the RISC-V user custom read-only range 0xCC0-0xCFF.
- The core evolved from OR10N (OpenRISC) to RI5CY (2016, PULP platform) and was contributed to OpenHW Group in February 2020, undergoing verification, bug fixes, and industrial quality documentation.
- FPU is instantiated as a separate module outside the EX stage, not via the APU interface visible at top-level I/Os.

## Relationships

No direct links to existing wiki pages; this page introduces the CORE-V CV32E40P as the first RISC-V processor core in the wiki. Future pages on RISC-V ISA, OpenHW Group, or PULP platform may link here.

## Sources

- OpenHW Group, "CORE-V CV32E40P User Manual v1.8.3", Introduction. URL: https://docs.openhwgroup.org/projects/cv32e40p-user-manual/en/latest/intro.html
