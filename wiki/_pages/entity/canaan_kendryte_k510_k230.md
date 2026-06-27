---
type: entity
tags: []
sources:
  - https://www.kendryte.com/k230/en/v2.0/K230_brief_datasheet.html
  - https://riscv.org/blog/canaan-announces-kendryte-k510-edge-ai-chip-as-a-triple-core-risc-v-part-with-3-tops-npu-gareth-halfacree-hackster-io/
  - https://www.eet-china.com/news/202211307275.html
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 2
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Canaan Kendryte K510 / K230

The Canaan Kendryte series represents the world's first commercially deployed RISC-V AI processor family, spanning three generations from the pioneering K210 (2018) through the K510 (2021) to the K230 (2023). The K230, fabricated in TSMC 12nm, is particularly notable as the first commercial chip to implement the ratified RISC-V Vector Extension 1.0, featuring a dual-core XuanTie C908 configuration: a big core at 1.6 GHz with 128-bit RVV 1.0 running RT-Thread for real-time AI inference, and a small core at 800 MHz without VPU running Linux for application control. Its third-generation Knowledge Process Unit (KPU) neural accelerator achieves approximately 6 TOPS (INT8), delivering ResNet-50 at ≥85 fps, MobileNetV2 at ≥670 fps, and YoloV5S at ≥38 fps — all at a typical power envelope of roughly 2 watts. The chip also integrates a dedicated 3D structured-light depth processing unit (DPU) capable of 1080p, a 2.5D GPU with tessellation, a video encoder/decoder supporting H.264/H.265 up to 8 MP, and an ISP handling 8 MP at 30 fps with multi-frame noise reduction. The K230 is targeted at smart door locks with 3D face recognition, smart security cameras, AI dictionary pens, payment terminals, drones, and battery-powered AI cameras. A compact variant, the K230D, integrates 128 MB LPDDR4 in-package and achieves approximately 1 TOPS at roughly 300 mW for ultra-low-power applications. The K510 (2021) preceded it with a triple-core RISC-V configuration and roughly 2–3 TOPS KPU v2, establishing the dual-OS architecture (Linux + RTOS) that the K230 refines. Over 2 million K210 units shipped globally, demonstrating commercial viability of RISC-V AI silicon well before the broader ecosystem matured.

## Key Claims

- The K230 is the first commercial chip to implement the ratified RISC-V Vector Extension 1.0 (RVV 1.0), enabling inference libraries like muRISCV-NN to achieve up to 6.68× speedup on fully connected layers versus scalar RISC-V execution.
- The K230's third-generation KPU delivers approximately 6 TOPS (INT8) at roughly 2 watts, with measured ResNet-50 throughput of ≥85 fps and MobileNetV2 at ≥670 fps, with typical network MAC utilization exceeding 70%.
- The K230 employs a heterogeneous dual-OS architecture: the big XuanTie C908 core (1.6 GHz, RVV 1.0) runs RT-Thread for real-time AI inference, while the small XuanTie C908 (800 MHz, no VPU) runs Linux for application logic and connectivity.
- The dedicated 3D structured-light DPU in the K230 processes depth data at 1080p resolution, enabling secure facial recognition for smart locks and payment terminals — a specialized feature absent from general-purpose RISC-V SoCs.
- The K230D variant achieves roughly 300 mW active power for 1 TOPS AI throughput with in-package LPDDR4, targeting battery-powered always-on AI cameras with a deep sleep current of ≤20 μW.
- Over 2 million first-generation K210 units shipped across 20+ countries, establishing the Kendryte family as the highest-volume RISC-V AI chip line at its 2018 launch and validating the market for RISC-V edge AI silicon.

## Relationships

- [[alibaba_xuantie_c910_c920]]: The K230 integrates Alibaba/T-Head's XuanTie C908 cores, directly connecting Canaan's AI SoC to the XuanTie processor IP ecosystem and its toolchain support.
- [[starfive_jh7110_visionfive2]]: The JH7110 VisionFive 2 competes in the RISC-V edge AI SBC space but takes a different architectural approach (NVDLA + external Hailo-8L) versus the K230's integrated KPU.
- [[risc_v_vector_extension]]: The K230 is the first silicon proof-point for RVV 1.0 in a commercial product, providing empirical validation of the vector specification's suitability for edge AI workloads.
- [[riscv_zve_sub_extensions]]: While the K230 uses full RVV 1.0, the Zve* embedded vector sub-extensions target a similar low-power inference domain with reduced hardware cost — the K230 sits at the boundary between these embedded vector profiles and full application-class vectors.

## Sources

- https://www.kendryte.com/k230/en/v2.0/K230_brief_datasheet.html
- https://riscv.org/blog/canaan-announces-kendryte-k510-edge-ai-chip-as-a-triple-core-risc-v-part-with-3-tops-npu-gareth-halfacree-hackster-io/
- https://www.eet-china.com/news/202211307275.html
