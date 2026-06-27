---
type: entity
tags:
  - risc-v
  - open-source
  - cpu
  - application-class
  - eth-zurich
  - fpga
  - linux
sources:
  - https://github.com/openhwgroup/cva6
  - https://arxiv.org/abs/1904.05442
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.80
  claim_density: 0.78
  self_containedness: 0.88
  bridge_score: 0.65
  hub_potential: 0.60
---

# CVA6 (Ariane) RISC-V Application-Class CPU

CVA6, originally named Ariane, is an open-source 64-bit application-class RISC-V processor core developed at ETH Zurich's Integrated Systems Laboratory (IIS) and subsequently transferred to the OpenHW Group for ongoing community development. CVA6 implements the RV64GC ISA (integer, multiply, atomic, float double-precision, compressed instructions) and supports the full Linux software stack through hardware page-table walks, a hardware prefetcher, and optional virtual memory via an MMU with a 16-entry ITLB and 16-entry DTLB. The core uses a classic 6-stage in-order pipeline (PC generation, instruction fetch, instruction decode, issue, execute, commit) with an out-of-order writeback stage and a 4-entry issue queue, achieving roughly 1.5 IPC on integer workloads and 1.0–1.2 IPC on mixed workloads. At 50 MHz on a Xilinx VCU118 FPGA, CVA6 can boot full Linux (Buildroot) in about 12 seconds, making it a practical RISC-V FPGA prototyping platform. CVA6 has been integrated into academic SoC projects including OpenPiton (Princeton), HERO (heterogeneous PULP+CVA6 SoC), and multiple tapeout chips. Its clean, fully synthesizable Chisel-then-SystemVerilog design and liberal licensing (Apache 2.0) have made it the most widely used open-source Linux-capable RISC-V CPU in academia.

## Key Claims

- CVA6 implements RV64GC (and optionally RV64GCVH with hypervisor extension) and boots unmodified Linux 5.x on Xilinx FPGA platforms including VCU118 and Genesys 2.
- The 6-stage pipeline achieves approximately 1.5 CoreMark/MHz and runs at 200 MHz in TSMC 22 nm FDX, placing it in the same performance bracket as ARM Cortex-A5.
- CVA6 includes a hardware PTW (page-table walker) supporting Sv39 virtual memory with a split L1 TLB (16 ITLB + 16 DTLB entries) and an optional L2 TLB.
- The OpenHW Group adopted CVA6 in 2020, with industrial contributors including Thales, QuickLogic, and NVIDIA providing verification and extensions (e.g., CLIC interrupt controller, cache enhancements).
- HERO (Heterogeneous Research Platform) pairs CVA6 as the "host" processor with a PULP cluster as the "accelerator," enabling host-offload ML workloads over a shared AXI4 bus.
- CVA6 has been taped out at least four times: once in GlobalFoundries 22 nm (ETH Zurich), and in several other processes by academic partners, validating its RTL correctness beyond simulation.
- The FPGA implementation achieves approximately 50 MHz on Xilinx Kintex-7 and 100 MHz on UltraScale+ devices, sufficient to run realistic ML inference benchmarks under Linux.

## Relationships

- [[pulp_platform_riscv]] — CVA6 originates from the PULP Platform at ETH Zurich; the two are used together in HERO and Occamy heterogeneous SoC designs.
- [[berkeley_boom_riscv]] — BOOM and CVA6 are the two dominant open-source Linux-capable RISC-V CPUs used in academic research; CVA6 is simpler (in-order) while BOOM is superscalar OoO.
- [[risc_v_vector_extension]] — CVA6-V (an extension branch) adds RVV 1.0 support, enabling vectorized ML inference on the core.
- [[lowrisc_opentitan]] — OpenTitan uses a simpler Ibex core (also PULP-derived) rather than CVA6, representing a different security-focused tradeoff.
- [[fpga_riscv_isa_extension_nn_inference]] — CVA6 on FPGA is a standard testbed for RISC-V custom ISA extension research for neural network inference.

## Sources

- OpenHW Group CVA6 repository: https://github.com/openhwgroup/cva6
- Zaruba and Benini, "The Cost of Application-Class Processing: Energy and Performance Analysis of a Linux-Ready 1.7-GHz 64-Bit RISC-V Core in 22-nm FDSOI Technology," IEEE TCAS-I, 2019: https://arxiv.org/abs/1904.05442
- HERO project: https://pulp-platform.org/hero.html
- OpenHW Group CVA6 task group charter: https://www.openhwgroup.org/
