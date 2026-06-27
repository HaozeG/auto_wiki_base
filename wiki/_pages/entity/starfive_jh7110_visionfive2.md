---
type: entity
tags: []
sources:
  - https://forum.rvspace.org/t/visionfive-2-ai-kit-user-guide-update/5173
  - https://semiiphub.com/news/risc-v-powered-ai-computing
  - https://github.com/open-riscv-initiative/website/blob/master/content/en/docs/boards/starfive_visionfive_2/_index.md
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# StarFive JH7110 / VisionFive 2

The StarFive JH7110 is a production-grade 64-bit RISC-V quad-core application SoC fabricated in TSMC 28nm, and the VisionFive 2 is the single-board computer (SBC) built around it — representing the most widely available RISC-V SBC with native AI acceleration capabilities. The JH7110 integrates four SiFive U74 application cores running at up to 1.5 GHz, an Imagination BXE-4-32 MC1 GPU (supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.2 at up to 600 MHz), and critically for AI workloads, an NVIDIA Deep Learning Accelerator (NVDLA) engine plus a Neural Network Engine (NNE) and a Vision DSP on-die. The VisionFive 2 SBC ships with up to 8 GB LPDDR4 RAM, dual Gigabit Ethernet, M.2 M-key slot, and official Linux distributions including Debian and Fedora. In October 2024, StarFive and Hailo jointly launched the VisionFive 2 AI Kit, bundling the SBC with a Hailo-8L M.2 AI acceleration module delivering up to 13 TOPS (INT8) with support for YOLOv5, YOLOv8, MobileNet SSD, and the full Hailo Model Zoo. The native on-die NVDLA and NNE provide modest inference throughput suitable for lightweight always-on tasks, while the Hailo-8L handles production-grade computer vision at the edge. The board has been benchmarked with NCNN and other inference frameworks, making it a practical RISC-V AI development and deployment platform for smart home, industrial vision, and educational use cases.

## Key Claims

- The JH7110 SoC includes an NVDLA (NVIDIA Deep Learning Accelerator) engine and a Neural Network Engine on-die, providing native AI inference without requiring external accelerator hardware — though throughput is modest compared to dedicated NPUs.
- The VisionFive 2 AI Kit with Hailo-8L M.2 module delivers up to 13 TOPS (INT8) and supports pre-trained models from the Hailo Model Zoo including YOLOv5, YOLOv8, and MobileNet SSD for object detection and image segmentation.
- The VisionFive 2 is one of the first production RISC-V SBCs to offer an M.2 M-key slot, enabling direct plug-in of PCIe-based AI accelerators — a critical hardware feature for edge AI workloads absent from earlier RISC-V boards.
- The JH7110's IMG BXE-4-32 GPU supports Vulkan 1.2 and OpenCL 3.0 at up to 600 MHz, enabling GPU-accelerated ML inference via frameworks that target these APIs on RISC-V.
- Official Linux distributions (Debian, Fedora, openEuler) provide first-class support for the VisionFive 2, making it one of the few RISC-V boards with production-quality OS images and package repositories.
- The board has been adopted by the Open RISC-V Initiative as a reference platform, and the JH7110's RISC-V vector-capable U74 cores provide a baseline for software ecosystem development even though the U74 does not implement the full RVV 1.0 specification.

## Relationships

- [[risc_v_vector_extension]]: The JH7110's U74 cores predate RVV 1.0 ratification and lack hardware vector units, making the Hailo-8L and NVDLA the primary AI compute paths rather than RVV-based inference.
- [[canaan_kendryte_k510_k230]]: The Canaan K230 represents a competing RISC-V edge AI SoC approach with integrated KPU, contrasting with the JH7110's strategy of on-die NVDLA plus external AI accelerator via M.2.
- [[sifive_intelligence_x280]]: The U74 cores in the JH7110 are SiFive-designed, establishing the foundation that SiFive later built upon with the X280 and X390 NPU designs for dedicated AI acceleration.

## Sources

- https://forum.rvspace.org/t/visionfive-2-ai-kit-user-guide-update/5173
- https://semiiphub.com/news/risc-v-powered-ai-computing
- https://github.com/open-riscv-initiative/website/blob/master/content/en/docs/boards/starfive_visionfive_2/_index.md
