---
canonical_name: VCIX Scheduling Model
aliases:
- RISC-V VCIX instructions scheduling
- SiFive Vector Coprocessor Interface scheduling
- LLVM VCIX scheduler
- XSfvcp scheduling
- SiFive VCIX scheduling information
subtype: null
tags:
- VCIX
- LLVM
- scheduling
- RISC-V
- SiFive
- compiler
- vector coprocessor
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/dc7adc993adc4155.md
- https://llvm.org/docs/RISCV/RISCVVCIX.html
source_url: https://llvm.org/docs/RISCV/RISCVVCIX.html
fetched_at: '2026-07-02T05:56:47.225639+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# VCIX Scheduling Model

The VCIX Scheduling Model is the mechanism within the LLVM compiler infrastructure for describing the processor latency and resource usage of instructions belonging to RISC-V's XSfvcp extension, the SiFive Vector Coprocessor Interface (VCIX). Since the same processor definition (e.g., `-mcpu=sifive-x280`) may be paired with different coprocessors that exhibit drastically different latencies and resource consumption for VCIX instructions, LLVM provides a default scheduling implementation that can be customized by integrators. The default scheduling is defined in `llvm/lib/Target/RISCV/RISCVSchedSiFive7.td` and is shared across the SiFive 7 family of scheduling models, including `SiFive7VLEN512Model` and `SiFive7VLEN1024X300Model`. These models are used by the `-mtune=sifive7-series` tuning and by `-mcpu=sifive-x390`, `-mcpu=sifive-x280`, `-mcpu=sifive-e76`, `-mcpu=sifive-s76`, and `-mcpu=sifive-u74`. The model assigns every VCIX pseudo-instruction a `SchedWrite` that references processor resources (vector command queue VCQ and vector arithmetic sequencer VA1) and specifies acquisition/release cycles and latency. Customization is achieved by writing new TableGen functions that return per-mx (LMUL) cycle counts, then overriding `Latency`, `AcquireAtCycles`, and `ReleaseAtCycles` in `LMULWriteResMX` declarations. Additional processor resources can be introduced and bound to specific VCIX instructions. Advanced customization allows changing scheduling information based on the immediate operand of a pseudo-instruction.

## Key Claims

- VCIX instructions in LLVM are represented as pseudo-instructions defined in `RISCVInstrInfoXSf.td`, each with an attached `SchedWrite` that points to a scheduler model description.
- The default implementation in `RISCVSchedSiFive7.td` assigns the same `Latency`, `AcquireAtCycles`, and `ReleaseAtCycles` to all VCIX instructions, using the `SiFive7GetCyclesDefault` function to compute cycle counts per LMUL.
- VCIX scheduling is supported across all SiFive 7 family models and applies to the listed `-mtune` and `-mcpu` targets.
- Customization involves writing a new `SiFive7GetCustomCycles` function to override latency and resource occupancy, then targeting specific `SchedWrite` names (e.g., `WriteVC_V_I`) via a new `defm` block with modified `Latency` and `ReleaseAtCycles`.
- Integrators can add new `ProcResource` definitions to model additional coprocessor resources, then include them in `LMULWriteResMX` with corresponding `AcquireAtCycles` and `ReleaseAtCycles` entries.
- The scheduling model can be further refined to distinguish VCIX behavior based on the immediate operand of the pseudo-instruction, as the immediate is considered part of the opcode.

## Relationships

- The VCIX scheduling model is part of the [[llvm_riscv_target]] backend for RISC-V, which provides ISA support and code generation for SiFive cores.
- The scheduling model is used by SiFive cores such as the [[sifive_performance_p570_gen3]] and others in the SiFive 7 family, which are hardware targets for which VCIX scheduling customization is relevant.
- The model is documented alongside other LLVM scheduling documentation for the RISC-V target.

## Sources

- https://llvm.org/docs/RISCV/RISCVVCIX.html
