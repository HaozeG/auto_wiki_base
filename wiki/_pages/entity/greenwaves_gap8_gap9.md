---
cold_start: true
created: 2026-06-27
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.cnx-software.com/2019/12/13/greenwaves-gap9-iot-application-processor-enables-ai-on-coin-cell-powered-devices/
- https://arxiv.org/html/2407.13706v1
- https://fuse.wikichip.org/news/990/the-risc-v-momentum-continues-with-the-gap8-a-new-iot-ai-application-processor/
- https://www.hackster.io/news/greenwaves-technologies-announces-gap9-iot-application-processor-with-major-improvements-over-gap8-399ba4acb602
tags:
- risc-v
- ultra-low-power
- edge-AI
- IoT
- tinyML
- audio
- vision
- greenwaves
type: entity
updated: 2026-06-27
---

# GreenWaves GAP8 / GAP9

GreenWaves Technologies' GAP8 and GAP9 are ultra-low-power RISC-V application processors designed for battery-operated IoT devices requiring on-device AI inference for audio, keyword spotting, and computer vision. GAP8 was the first commercial RISC-V chip for edge AI, featuring a fabric controller RISC-V core plus an 8-core parallel compute cluster, all sharing a software-managed L1 scratchpad memory optimized for CNN inference. GAP9 is the successor generation, delivering five times lower power consumption than GAP8 while enabling inference on neural networks ten times larger, achieving 330 μW per GOP energy efficiency. GAP9 integrates a 9-core RISC-V compute cluster with a hardware NE16 neural engine, transprecision floating-point (FP32, FP16, bfloat16), a CSI-2 camera interface, and Serial Audio Interfaces, targeting hearables, nano-drones, biosignal monitors, and industrial IoT.

## Key Claims

- GAP8 integrates one RISC-V fabric controller + 8-core parallel compute cluster sharing L1 scratchpad memory; targets CNN inference at under 1 mW average.
- GAP9 achieves 330 μW/GOP energy efficiency and delivers 15.6 GOPs for DSP and 32.2 GMACs for ML inference.
- GAP9 delivers 5× lower power consumption than GAP8 while supporting 10× larger neural network models.
- GAP9 includes the NE16 neural engine accelerator for structured 8-bit and mixed-precision inference.
- GAP9 supports transprecision floating-point: IEEE FP32, FP16, and bfloat16.
- GAP9Shield module achieves 150 GOPS on a nano-drone platform for real-time vision and ranging.
- A QVGA (320×240) image CNN classification can run every three minutes for 10 years on a 3.6 Wh battery using GAP8, demonstrating extreme energy efficiency.

## Relationships

- [[pulp_platform]]: GAP8 is a commercial derivative of the PULP (Parallel Ultra-Low-Power) research platform from ETH Zurich and University of Bologna.
- [[risc_v_zve_sub_extensions]]: GAP8/GAP9 use RISC-V cores with embedded extensions including DSP/packed-SIMD for efficient compute cluster kernels.
- [[muriscv_nn]]: muRISCV-NN neural network library targets the same sub-watt RISC-V inference use case as GAP8/GAP9.
- [[tvm_riscv_backend]]: TVM's RISC-V backend can target GAP8/GAP9 for automated kernel generation for ML inference.

## Sources

- https://www.cnx-software.com/2019/12/13/greenwaves-gap9-iot-application-processor-enables-ai-on-coin-cell-powered-devices/
- https://arxiv.org/html/2407.13706v1
- https://fuse.wikichip.org/news/990/the-risc-v-momentum-continues-with-the-gap8-a-new-iot-ai-application-processor/
- https://www.hackster.io/news/greenwaves-technologies-announces-gap9-iot-application-processor-with-major-improvements-over-gap8-399ba4acb602
