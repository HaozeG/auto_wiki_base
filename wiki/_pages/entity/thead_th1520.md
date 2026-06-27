---
cold_start: true
created: 2026-06-27
inbound_links: 2
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://wiki.sipeed.com/hardware/en/lichee/th1520/lp4a.html
- https://www.cnx-software.com/2023/05/06/lichee-pi-4a-risc-v-sbc-raspberry-pi-4-th1520-processor/
- https://linuxgizmos.com/risc-v-embedded-board-features-th1520-soc-dual-gbe-and-4tops-ai/
- https://docs.u-boot.org/en/latest/board/thead/lpi4a.html
tags:
- risc-v
- SoC
- AI-acceleration
- NPU
- alibaba
- linux
- single-board-computer
type: entity
updated: 2026-06-27
---

# T-Head TH1520 SoC

The T-Head TH1520 is a production-grade, Linux-capable RISC-V system-on-chip designed by Alibaba's T-Head semiconductor division and manufactured at TSMC 12nm. It integrates four XuanTie C910 application-class RISC-V cores (RV64GCV, out-of-order, 3-issue superscalar) clocked at up to 2.0 GHz, alongside a dedicated 4 TOPS INT8 neural processing unit, an Imagination BXM-4-64 GPU delivering 50 GFLOPS, and a 1 GHz XuanTie C906 audio DSP. Each C910 core carries 64 KB L1 instruction and 64 KB L1 data cache; all four cores share an L2 cache. The SoC supports up to 16 GB of LPDDR4X RAM, hardware-accelerated H.264/H.265 encode at 4Kp40 and decode at 4Kp75, dual ISPs, and a full suite of standard peripherals. The TH1520 first gained broad developer attention as the processor inside Sipeed's Lichee Pi 4A single-board computer, launched in 2023 as a Raspberry Pi 4 competitor, and subsequently the BeagleV-Ahead board. Its NPU supports Tensorflow, ONNX, Caffe, and standard DNN/CNN/RNN graphs, enabling practical edge-AI workloads directly on a RISC-V platform without host-side acceleration.

## Key Claims

- Four XuanTie C910 RISC-V cores (RV64GCV) at up to 2.0 GHz; 3-issue out-of-order superscalar per core.
- Integrated 4 TOPS INT8 NPU at 1 GHz supporting Tensorflow, ONNX, Caffe, CNN, RNN, and DNN frameworks.
- Imagination BXM-4-64 GPU at 50 GFLOPS with OpenGLES 3.2, Vulkan 1.2, and OpenCL 2.0 support.
- H.265/H.264 hardware encode at 4Kp40 and decode at 4Kp75.
- Sipeed Lichee Pi 4A ships with up to 16 GB LPDDR4X RAM and 128 GB eMMC on the TH1520.
- Manufactured at TSMC 12nm; powers both Sipeed Lichee Pi 4A and BeagleBoard BeagleV-Ahead developer boards.

## Relationships

- [[alibaba_xuantie_c910_c920]]: TH1520 integrates four XuanTie C910 cores — the same open-sourced IP family.
- [[beaglev_ahead]]: BeagleV-Ahead is a developer SBC built around the TH1520 SoC.
- [[riscv_zve_sub_extensions]]: C910 implements RV64GCV (full V extension), predating Zve sub-profiles.

## Sources

- https://wiki.sipeed.com/hardware/en/lichee/th1520/lp4a.html (TH1520 and Lichee Pi 4A specs)
- https://www.cnx-software.com/2023/05/06/lichee-pi-4a-risc-v-sbc-raspberry-pi-4-th1520-processor/ (product launch coverage)
- https://linuxgizmos.com/risc-v-embedded-board-features-th1520-soc-dual-gbe-and-4tops-ai/ (NPU and peripherals)
- https://docs.u-boot.org/en/latest/board/thead/lpi4a.html (U-Boot upstream support)
