---
cold_start: true
created: 2026-06-27
inbound_links: 2
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://fires.im/
- https://github.com/firesim/firesim
- https://bar.eecs.berkeley.edu/projects/firesim.html
- https://aws.amazon.com/blogs/compute/bringing-datacenter-scale-hardware-software-co-design-to-the-cloud-with-firesim-and-amazon-ec2-f1-instances/
tags:
- risc-v
- simulation
- FPGA
- UC-Berkeley
- cloud
- cycle-accurate
- EDA
type: entity
updated: 2026-06-27
---

# FireSim FPGA-Accelerated Simulation

FireSim is an open-source, cycle-accurate, FPGA-accelerated hardware simulation platform developed at UC Berkeley that runs on Amazon EC2 F1 FPGA cloud instances as well as on-premises Xilinx Alveo boards. It automatically transforms open-source target RTL — primarily RISC-V designs such as Rocket Chip, BOOM, and Chipyard SoCs — into deterministic, fast FPGA-based simulators using the MIDAS (Model-Integrated Design Automation for Simulation) transformation framework, which instruments RTL for cycle-accurate timing and adds golden-gate bridges for host-target decoupling. FireSim enables simulation of complete multi-node datacenter-scale clusters: from a single RISC-V core to thousands of multi-core nodes with simulated network interconnects. A representative workload is running all of SPECInt2017 with reference inputs on a Rocket core in approximately one day across ten AWS cloud FPGAs in parallel, a task infeasible with software simulation. FireSim eliminates the capital expenditure of on-premises FPGA farms by running on AWS EC2 F1 instances (Xilinx VU9P FPGAs), which are available per-hour without upfront cost. The platform supports workload orchestration via FireMarshal (Linux image and bare-metal workload manager) and integrates with the Chipyard SoC framework for end-to-end design and evaluation. FireSim has been used in research on RISC-V memory systems, network-on-chip design, coherence protocols, and AI accelerator integration.

## Key Claims

- FireSim provides cycle-accurate FPGA-based simulation of RISC-V SoCs using MIDAS RTL transformation, running on AWS EC2 F1 and Xilinx Alveo boards.
- Supports scale from a single core to thousands of simulated multi-core nodes with network simulation.
- All of SPECInt2017 with reference inputs can run on a Rocket core in approximately one day across ten AWS F1 FPGAs in parallel.
- Uses AWS EC2 F1 (Xilinx VU9P FPGAs), removing the capital cost of on-premises FPGA farms.
- MIDAS framework instruments open-source RTL (Rocket, BOOM, Chipyard) into deterministic, host-decoupled FPGA simulators.
- Released under the BSD-3-Clause license at github.com/firesim/firesim with active UC Berkeley maintenance.

## Relationships

- [[chipyard_soc_framework]]: FireSim is the FPGA simulation flow within Chipyard; both share the MIDAS and FireMarshal infrastructure.
- [[boom_riscv]]: BOOM and Rocket Chip are the primary target RTL designs validated and published through FireSim.
- [[gemmini]]: Gemmini accelerator integration in Chipyard is evaluated using FireSim for cycle-accurate workload profiling.

## Sources

- https://fires.im/ (official FireSim project page)
- https://github.com/firesim/firesim (source repository and documentation)
- https://bar.eecs.berkeley.edu/projects/firesim.html (UC Berkeley BAR project description)
- https://aws.amazon.com/blogs/compute/bringing-datacenter-scale-hardware-software-co-design-to-the-cloud-with-firesim-and-amazon-ec2-f1-instances/ (AWS F1 integration blog)
