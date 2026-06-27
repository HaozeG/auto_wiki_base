---
cold_start: true
created: 2026-06-27
inbound_links: 6
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://pulp-platform.org/projectinfo.html
- https://www.eetimes.com/open-source-processor-core-ready-for-iot/
- https://www.techpowerup.com/308389/432-core-risc-v-processor-with-chiplets-aims-to-provide-ultra-efficient-floating-point-computation
tags: []
type: entity
updated: 2026-06-27
---

# PULP Platform

The PULP (Parallel Ultra-Low-Power) Platform is an open-source RISC-V computing ecosystem launched in 2013 as a joint effort between the Integrated Systems Laboratory (IIS) of ETH Zurich and the Energy-efficient Embedded Systems (EEES) group of the University of Bologna, under the direction of Prof. Luca Benini. Over its first decade, the platform produced more than 50 fabricated silicon chips and has become one of the most influential open-source hardware initiatives worldwide. The core architectural concept is a cluster of RISC-V cores sharing tightly coupled data memory, optimized for near-threshold computing and extreme energy efficiency across a power range from milliwatt-scale IoT to multi-watt HPC systems. The platform has produced a family of open-source RISC-V cores — Ibex (RV32, Cortex-M0+ class), CV32E40P/RI5CY (RV32 with DSP extensions), Snitch (streaming-optimized), and CVA6/Ariane (RV64, Linux-capable) — all released under the permissive Solderpad Hardware License. Custom xPULP ISA extensions (hardware loops, post-increment load/store, packed-SIMD) deliver up to 10× speedup on 8-bit convolution compared to baseline RISC-V, and up to 75× overall gain when combined with parallel cluster scaling. Notable silicon implementations include Mr. Wolf (multi-core IoT processor), Kraken (8-core IoT in GF 22nm FDSOI with ternary CNN and spiking neural network accelerators), Darkside (TinyML processor achieving 835 GOPS/W peak efficiency), and Occamy (432-core chiplet design in GF 12nm with HBM2e memory targeting up to 6.144 TFLOPS FP8). The platform has spawned industrial adoption through Greenwaves Technologies (GAP8 IoT processor), Google's OpenTitan root-of-trust project, and contributions to the OpenHW Group's CORE-V family. The team now numbers approximately 100 researchers across Zurich and Bologna, with research spanning IoT, edge AI, high-performance computing, and space-grade RISC-V SoCs.

## Key Claims

- PULP's custom xPULP ISA extensions deliver up to 10× speedup on 8-bit convolution versus baseline RISC-V ISA, and up to 75× combined speedup when parallel cluster scaling (8 cores) is factored in — directly relevant to TinyML inference workloads.
- The Darkside TinyML processor achieves a peak energy efficiency of 835 GOPS/W, representing one of the highest published efficiency figures for an open-source RISC-V AI accelerator in the sub-watt power envelope.
- The Occamy chiplet design integrates 432 RISC-V cores in GF 12nm with HBM2e memory, targeting up to 6.144 TFLOPS (FP8) for high-performance floating-point computation — demonstrating PULP's scalability from microwatt IoT to teraflop-scale computing.
- Over 50 chips have been fabricated by the PULP team since 2013, with designs spanning IoT (Mr. Wolf, Kraken), TinyML (Darkside), HPC (Occamy), and heterogeneous FPGA platforms (HERO), providing an unmatched empirical foundation for open-source RISC-V silicon design.
- The CV32E40P (RI5CY) and CVA6 (Ariane) cores originated within PULP and are now industrially maintained by the OpenHW Group under Eclipse Foundation governance, while Google's OpenTitan — the most popular SystemVerilog project on GitHub — was built on Ibex, a PULP-derived core.
- Greenwaves Technologies' GAP8 commercial IoT processor is a direct industrialization of PULP technology, with the GAP9 successor targeting edge AI inference, proving the PULP platform's viability for commercial silicon products.

## Relationships

- [[openhw_cva6]]: CVA6 originated as the Ariane core within PULP and is now maintained by OpenHW Group, representing the most prominent example of PULP→industrial transition.
- [[riscv_zve_sub_extensions]]: PULP's CV32E40P and Ibex cores are natural targets for Zve* embedded vector extensions, enabling vector-accelerated TinyML on PULP-derived MCU-class designs.
- [[gemmini]]: Gemmini is a systolic array generator from UC Berkeley; PULP's Darkside and Kraken chips integrate domain-specific CNN accelerators that represent a parallel approach to open-source AI acceleration hardware.
- [[risc_v_vector_extension]]: PULP's Snitch core includes streaming vector support and the platform has contributed to RVV 1.0 validation; Occamy's 432 cores use vector units for the 6.144 TFLOPS FP8 target.

## Sources

- https://pulp-platform.org/projectinfo.html
- https://www.eetimes.com/open-source-processor-core-ready-for-iot/
- https://www.techpowerup.com/308389/432-core-risc-v-processor-with-chiplets-aims-to-provide-ultra-efficient-floating-point-computation
