---
type: entity
tags: [risc-v, ultra-low-power, IoT, edge-AI, embedded, ETH-zurich, PULP, GreenWaves]
sources:
  - https://pulp-platform.org/projectinfo.html
  - https://arxiv.org/pdf/1908.11263
  - https://www.hackster.io/news/greenwaves-technologies-announces-gap9-iot-application-processor-with-major-improvements-over-gap8-399ba4acb602
  - https://arxiv.org/html/2407.13706v1
  - https://gf.com/gf-press-release/greenwaves-technologies-announces-next-generation-gap9-hearables-platform-using/
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# PULP Platform / GAP8 / GAP9

The Parallel Ultra-Low-Power (PULP) Platform is an open-source research initiative launched in 2013 as a joint project between the Integrated Systems Laboratory (IIS) at ETH Zürich and the Energy-Efficient Embedded Systems (EEES) group at the University of Bologna. Its goal is to develop highly energy-efficient multi-core computing architectures based on the RISC-V ISA targeting IoT, wearable, and edge-AI workloads within power envelopes of a few milliwatts. PULP designs employ a cluster of RISC-V cores sharing a tightly-coupled L1 scratchpad memory (TCDM), plus a lightweight fabric controller for peripheral management. The research prototypes (Mr. Wolf, GAP8) led to commercial products from GreenWaves Technologies. GAP8, fabricated in TSMC 55 nm, features 8 RI5CY DSP-optimized RISC-V cores in a compute cluster plus one fabric controller, targeting voice and image inference workloads. GAP9 — manufactured on GlobalFoundries 22 nm FDX — adds a 9th cluster core, an NE16 hardware neural engine for INT8/INT4 convolutions, transprecision floating-point, and achieves 150 GOPS at 0.33 mW/GOP peak efficiency, or 32.2 GMACs for ML and 15.6 GOPS for DSP. The PULP-NN library provides optimized quantized neural network kernels for PULP/GAP targets.

## Key Claims

- GAP8: 8 RI5CY RISC-V cluster cores + 1 fabric controller; built on TSMC 55 nm process.
- GAP9: 9-core RISC-V cluster on GF 22 nm FDX; 150 GOPS peak, 32.2 GMACs for ML, 15.6 GOPS DSP.
- GAP9 energy efficiency: 0.33 mW/GOP (330 µW/GOP) at peak performance; sleep power as low as 45 µW.
- GAP9 features NE16 hardware accelerator for INT8/INT4 convolutions and up to 370 MHz operation.
- GAP9 cluster L2 RAM: 1.6 MB; non-volatile in-package memory: 2 MB; peak cluster bandwidth: 41.6 GB/s.
- PULP-NN library provides INT2–INT8 quantized CNN kernels with software-managed DMA for PULP clusters.
- GAP9 ships in hearables/earbuds at ~50 mW total system power for always-on wake-word and ML inference.

## Relationships

- [[risc_v_vector_extension]]: PULP cluster uses RI5CY cores with RISC-V SIMD/DSP extensions (predecessor to P-extension).
- [[risc_v_p_extension]]: RI5CY cores implement a custom SIMD extension that influenced the RISC-V P-extension proposal.
- [[ara_vector_processor]]: Both are ETH Zürich RISC-V projects; Ara targets server/HPC vectors while PULP/GAP targets µW IoT.
- [[gemmini]]: Comparable open-source RISC-V accelerator ecosystem; Gemmini uses systolic arrays vs PULP's SIMD cluster approach.

## Sources

- https://pulp-platform.org/projectinfo.html
- https://arxiv.org/pdf/1908.11263
- https://www.hackster.io/news/greenwaves-technologies-announces-gap9-iot-application-processor-with-major-improvements-over-gap8-399ba4acb602
- https://arxiv.org/html/2407.13706v1
- https://gf.com/gf-press-release/greenwaves-technologies-announces-next-generation-gap9-hearables-platform-using/
