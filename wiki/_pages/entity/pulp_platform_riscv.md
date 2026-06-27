---
type: entity
tags:
  - risc-v
  - open-source
  - cpu
  - edge-ai
  - ultra-low-power
  - parallel-computing
  - eth-zurich
sources:
  - https://pulp-platform.org/
  - https://github.com/pulp-platform
  - https://arxiv.org/abs/1705.04590
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.85
  claim_density: 0.80
  self_containedness: 0.90
  bridge_score: 0.70
  hub_potential: 0.65
---

# PULP Platform (Parallel Ultra-Low-Power)

The PULP Platform is an open-source research initiative jointly led by ETH Zurich's Integrated Systems Laboratory (IIS) and the University of Bologna, producing a family of ultra-low-power RISC-V processor clusters, SoC designs, and peripheral IP targeting edge AI and IoT applications. The project's defining architectural decision is a shared-memory cluster of 2–16 RISC-V cores connected to a tightly coupled data memory (TCDM) through a low-latency logarithmic interconnect, enabling near-linear parallel speedup for data-parallel workloads such as convolutional neural network (CNN) inference. PULP's flagship production chip, Mr. Wolf (GAP8), was commercialized by GreenWaves Technologies in 2018 and integrates 8 RISC-V cores (based on the RI5CY/CV32E40P core) plus a Fabric Controller in 55 nm TSMC, achieving 10–50 GOPS/W for 8-bit integer CNN inference — competitive with dedicated neural accelerators at the time. The platform has grown into a comprehensive open-source ecosystem covering the CV32E40P (RI5CY) 32-bit core, CVA6 (Ariane) 64-bit application-class core, PULP-NN inference library, PULP-SDK, and numerous SoC variants (Vega, Kraken, Occamy), with all RTL released under permissive open-source licenses. PULP has become a standard academic baseline for benchmarking energy-efficient RISC-V AI inference.

## Key Claims

- Mr. Wolf (GAP8) integrates 8 RI5CY (CV32E40P) RISC-V cores plus 1 Fabric Controller in TSMC 55 nm, achieving 50 GOPS at 1 mW for 8-bit CNN inference at sub-100 MHz clock frequencies.
- The PULP cluster uses a logarithmic interconnect (log-N crossbar) between N cores and the TCDM, delivering one-cycle latency for bank-conflict-free access patterns and enabling near-N× speedup from N cores.
- CV32E40P (formerly RI5CY) is a 4-stage, 32-bit RISC-V core implementing RV32IMFCXpulp, where Xpulp adds hardware loops, SIMD, and post-increment load/store for DSP/ML workloads.
- GreenWaves Technologies GAP8 and GAP9 are commercial derivatives of PULP designs; GAP9 (22 nm) targets always-on audio/vision at under 1 mW idle with burst inference up to 200 GOPS.
- The Occamy chip (2022) scales the PULP cluster concept to a 216-core RISC-V manycore in 12 nm with 4 TB/s on-chip bandwidth, targeting HPC workloads.
- PULP-NN is an open-source library of hand-optimized RISC-V intrinsic kernels for 8-bit and mixed-precision CNN inference on PULP clusters, outperforming scalar CMSIS-NN by 5–13× on the same workloads.
- The project has published over 100 peer-reviewed papers and is the source of both the CV32E40P core (in OpenHW Group) and CVA6/Ariane (used in FPGA-based Linux SoCs).

## Relationships

- [[cva6_ariane_riscv]] — CVA6 (Ariane) 64-bit application-class core originated from the PULP Platform and serves as the main processor in PULP heterogeneous SoCs.
- [[risc_v_vector_extension]] — Newer PULP cores (Snitch, Spatz) implement RVV 1.0 for vectorized ML inference.
- [[gemmini]] — Gemmini (Berkeley) and PULP represent parallel approaches to open-source RISC-V AI accelerators; PULP emphasizes clustered scalar cores while Gemmini adds a systolic array.
- [[tinyml_mcu_inference]] — PULP-NN and GAP8/GAP9 are reference platforms for TinyML deployment benchmarks.
- [[zephyr_rtos_tflite_micro]] — TFLite Micro has been ported to PULP/GAP8 as a higher-level inference runtime above PULP-NN.

## Sources

- PULP Platform website: https://pulp-platform.org/
- PULP GitHub organization: https://github.com/pulp-platform
- Gautschi et al., "Near-Threshold RISC-V Core With DSP Extensions for Scalable IoT Endpoint Devices," IEEE JSSC 2017: https://arxiv.org/abs/1705.04590
- Conti et al., "PULP-NN: Accelerating Quantized Neural Networks on Parallel Ultra-Low-Power RISC-V Processors," Phil. Trans. Royal Society A, 2020
- GreenWaves Technologies GAP8 datasheet: https://greenwaves-technologies.com/gap8_gap9/
