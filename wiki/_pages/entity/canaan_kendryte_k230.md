---
type: entity
tags: [risc-v, AI-accelerator, edge-AI, SoC, vision, embedded, canaan]
sources:
  - https://www.kendryte.com/k230/en/main/K230_brief_datasheet.html
  - https://www.cnx-software.com/2023/10/24/canmv-k230-ai-development-board-features-kendryte-k230-dual-core-64-bit-risc-v-processor/
  - https://linuxgizmos.com/canmv-k230-features-dual-risc-v-processors-and-kpu/
  - https://www.electronics-lab.com/canmv-k230-ai-development-board-with-kendryte-k230-risc-v-processor-and-6-tops-npu/
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

# Canaan Kendryte K230

The Canaan Kendryte K230 is a dual-core 64-bit RISC-V SoC designed for edge AI and computer vision applications, produced by Canaan Inc. (known for its Bitcoin mining ASICs). Released in 2023, the K230 integrates two RISC-V C908 cores and a built-in KPU (Knowledge Process Unit) delivering up to 6 TOPS of AI compute. The primary core runs at 1.6 GHz with full RISC-V Vector Extension 1.0 (RVV 1.0) and floating-point support, while the secondary core operates at 800 MHz with a base RV64GCB configuration for real-time tasks. The K230 represents a significant generational leap over its predecessor, the K510 (3 TOPS, triple-core, 800 MHz), with 2× more NPU throughput and 2.5× better MAC utilization — achieving 341 FPS/TOPS on YoloV5S versus 133 FPS/TOPS on the K510. Target use cases span smart door locks, surveillance cameras, dictionary pens, drones, interactive robots, and industrial inspection. The chip ships in development kits (CanMV-K230) with 512 MB LPDDR4 and supports up to three 4K camera inputs via MIPI CSI, making it one of the most capable sub-$50 RISC-V AI inference platforms available.

## Key Claims

- Dual RISC-V C908 cores: CPU1 at 1.6 GHz with RVV 1.0, CPU0 at 800 MHz with RV64GCB.
- KPU delivers 6 TOPS with INT8 and INT16 precision support.
- Achieves 341 FPS/TOPS on YoloV5S (vs. 133 FPS/TOPS on K510, 86 FPS/TOPS on K210).
- Typical network benchmarks: ResNet-50 ≥ 85 fps @INT8, MobileNet_v2 ≥ 670 fps @INT8, YoloV5S ≥ 38 fps @INT8.
- Supports up to three 4K camera inputs via MIPI CSI, plus 2.5D GPU and 3D depth engine.
- Predecessor K510 featured triple-core RISC-V with 3 TOPS NPU at 800 MHz (released 2021).

## Relationships

- [[risc_v_vector_extension]]: K230's primary CPU core implements RVV 1.0 for SIMD-accelerated inference.
- [[tvm_riscv_backend]]: Apache TVM supports K230-class RVV 1.0 targets for compiled model deployment.

## Sources

- https://www.kendryte.com/k230/en/main/K230_brief_datasheet.html
- https://www.cnx-software.com/2023/10/24/canmv-k230-ai-development-board-features-kendryte-k230-dual-core-64-bit-risc-v-processor/
- https://linuxgizmos.com/canmv-k230-features-dual-risc-v-processors-and-kpu/
- https://www.electronics-lab.com/canmv-k230-ai-development-board-with-kendryte-k230-risc-v-processor-and-6-tops-npu/
