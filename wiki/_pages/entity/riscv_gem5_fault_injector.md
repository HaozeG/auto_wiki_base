---
canonical_name: riscv-gem5-fault-injector
aliases:
- RISC-V gem5 Fault Injector
- gem5 fault injector
- riscv-gem5-fi
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/dbc260f6f6ddf440.md
- https://github.com/imndllnuri/riscv-gem5-fault-injector
source_url: https://github.com/imndllnuri/riscv-gem5-fault-injector
fetched_at: '2026-07-02T05:41:45.789932+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# riscv-gem5-fault-injector

The RISC-V gem5 Fault Injector is a fork of the gem5 computer architecture simulator that adds a deterministic, single-bit register fault injector for the RISC-V AtomicSimpleCPU and TimingSimpleCPU models. It is designed for soft-error and resiliency research, allowing researchers to flip a single bit in a chosen integer register at a precise simulated cycle and observe the workload reaction, such as crashes, silent data corruption, or no visible effect. The injector is implemented as a gem5 SimObject with parameters for enable, register index, bit position, and injection cycle, supporting both polling (AtomicSimpleCPU) and event-driven (TimingSimpleCPU) injection mechanisms. The tool also includes a campaign runner for automated parameter sweeps and parallel execution, enabling efficient fault injection studies across multiple registers, cycle windows, and repetitions. Demo microbenchmarks (towers and mat_mul) are bundled to avoid dependency on licensed benchmark suites. The tool outputs per-run stats, console output, and a metadata file summarizing the injected fault and its outcome.

## Key Claims

- Deterministic, single-bit register fault injector for RISC-V AtomicSimpleCPU and TimingSimpleCPU models in gem5.
- Configurable via four parameters: enabled, reg_index (x0-x31), bit_pos (0-63), and inject_cycle.
- AtomicSimpleCPU: injects by polling every tick; TimingSimpleCPU: injects using a one-shot FaultInjectionEvent.
- Supports golden run comparison by omitting the --fault-inject flag.
- Bundled campaign runner (run_campaign.py) automates golden run plus randomized parameter sweep with resumable progress tracking.
- Includes demo microbenchmarks: towers and mat_mul, with source code.
- Debug flag FaultTrace enables before/after register value logging.

## Relationships

- The fault injector can be used to simulate fault injection on RISC-V cores such as [[xuantie_c908]] and [[k230]] when modeled in gem5.
- This tool extends gem5, the widely used computer architecture simulator; the original gem5 repository is at https://www.gem5.org.

## Sources

- https://github.com/imndllnuri/riscv-gem5-fault-injector
