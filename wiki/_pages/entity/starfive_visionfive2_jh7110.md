---
type: entity
tags:
  - risc-v
  - sbc
  - soc
  - npu
  - gpu
  - starfive
  - linux
sources:
  - https://www.starfivetech.com/en/site/boards
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.75
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.5
  hub_potential: 0.45
---

# StarFive VisionFive 2 and JH7110 SoC

The StarFive VisionFive 2 is a single-board computer (SBC) launched in 2023, powered by the StarFive JH7110 SoC—a quad-core SiFive U74 RISC-V application processor running at up to 1.5 GHz. It is the first mass-market RISC-V SBC to integrate a GPU (Imagination Technologies BXE-4-32) capable of OpenGL ES and Vulkan rendering, enabling graphics-accelerated workloads beyond CPU-only RISC-V boards. The JH7110 also incorporates a 1 TOPS INT8 neural processing unit (NPU) for basic computer vision inference tasks such as object detection and image classification. The VisionFive 2 ships in 2 GB, 4 GB, and 8 GB LPDDR4 configurations; the 4 GB variant retails for approximately $55–79. Linux kernel mainline support for the JH7110 was merged in kernel 6.6 (late 2023), including the GPU driver, making it the first RISC-V SoC SBC with upstream GPU support in the mainline kernel. VisionFive 2 supports HDMI 2.0 output, PCIe 2.0 (×1), dual MIPI CSI camera interfaces, MIPI DSI display, and a 40-pin GPIO header, positioning it as a developer platform for RISC-V embedded Linux and edge AI experiments.

## Key Claims

- JH7110 integrates four SiFive U74 RISC-V cores (RV64GC) at up to 1.5 GHz, with a 1 TOPS INT8 NPU for edge ML inference.
- VisionFive 2 is the first mass-market RISC-V SBC to ship with a GPU (Imagination BXE-4-32) supporting OpenGL ES and Vulkan—enabling graphics-accelerated ML frameworks.
- Mainline Linux kernel 6.6 merged JH7110 SoC support including the GPU driver, giving VisionFive 2 the first upstream GPU support of any RISC-V SBC.
- Available in 2 GB, 4 GB, and 8 GB LPDDR4 variants; 4 GB model priced at $55–79, making it the most affordable RISC-V SBC with GPU acceleration.
- Connectivity includes PCIe 2.0 ×1 (M.2 Key M slot), HDMI 2.0, dual MIPI CSI, MIPI DSI, dual Gigabit Ethernet, and USB 3.0.
- Multiple Linux distros support VisionFive 2: Fedora RISC-V, Ubuntu RISC-V, Debian RISC-V, and vendor Bianbu Linux as of mid-2024.

## Relationships

- [[spacemit_k1_soc]] — Competing RISC-V SoC SBC; K1 offers more CPU cores and higher NPU throughput (2 TOPS vs. 1 TOPS) but no discrete GPU.
- [[risc_v_architecture]] — JH7110 uses SiFive U74 cores implementing the RV64GC base ISA without the V (vector) extension.
- [[sifive_intelligence_x280]] — SiFive U74 in JH7110 is a different (non-vector) SiFive core family; X280 is SiFive's vector AI-focused product.
- [[tinyml_mcu_inference]] — VisionFive 2 NPU enables edge inference above MCU class but below discrete GPU/NPU performance.

## Sources

- StarFive VisionFive 2 product page: https://www.starfivetech.com/en/site/boards
- JH7110 SoC datasheet (StarFive)
- Linux kernel 6.6 merge commit for JH7110
- VisionFive 2 pricing and availability (various retailers, 2023–2024)
