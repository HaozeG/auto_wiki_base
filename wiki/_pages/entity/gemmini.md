---
canonical_name: Gemmini
aliases:
- Berkeley's Spatial Array Generator
- ucb-bar/gemmini
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.6
  bridge_score: 0.8
  hub_potential: 0.9
sources:
- raw/cache/8ed8b85210255169.md
- https://scispace.com/papers/gemmini-an-agile-systolic-array-generator-enabling-18gqvurz6k
source_url: https://scispace.com/papers/gemmini-an-agile-systolic-array-generator-enabling-18gqvurz6k
fetched_at: '2026-07-02T09:30:11.932583+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Gemmini

Gemmini is an open-source, agile systolic array generator that enables systematic evaluation of deep-learning architectures. It generates custom ASIC accelerators for matrix multiplication based on a systolic array architecture, complete with additional functions for neural network inference. The generator is parameterizable, allowing designers to explore trade-offs in performance, energy, and area across a multi-dimensional design space. Gemmini is integrated within the Rocket Chip ecosystem, a RISC-V-based open-source platform, and has been used in the fabrication of two test system-on-chips in different process technologies, demonstrating flexibility and utility. By providing a generator-based methodology, Gemmini accelerates the design space exploration for deep neural network hardware accelerators, achieving up to two to three orders of magnitude speedup in inference compared to baseline host processor execution.

## Key Claims

- Gemmini is an open-source and agile systolic array generator for custom ASIC accelerators targeting matrix multiplication and neural network inference.
- The accelerator architecture features a 2-D systolic array fed by a banked scratchpad memory made of SRAMs, with data movement instructions (mvin, mvout) and an output-stationary compute instruction.
- The generator is parameterizable, enabling exploration of different design points in performance, energy, and area.
- Integration with the Rocket Chip open-source platform allows seamless integration with RISC-V cores and other accelerators.
- Gemmini has been used in tape-outs of two test SoCs within a month of each other in different process technologies.
- The generated accelerators achieve two to three orders of magnitude speedup in deep neural network inference compared to baseline host processor execution.

## Relationships

- [[Rocket Chip]]: Gemmini is integrated within the Rocket Chip RISC-V platform.
- [[RISC-V]]: The generated accelerators interface with RISC-V cores.

(Insufficient context for additional cross-links; no existing entity pages in wiki.)

## Sources

- [Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architectures](https://scispace.com/papers/gemmini-an-agile-systolic-array-generator-enabling-18gqvurz6k)
