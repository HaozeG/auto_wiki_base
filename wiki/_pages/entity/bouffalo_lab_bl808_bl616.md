---
cold_start: false
created: 2026-06-27
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://files.pine64.org/doc/datasheet/ox64/BL808_DS_en_1.1(open).pdf
- https://www.cnx-software.com/2022/12/29/bouffalo-lab-bl616-bl618-risc-v-mcu-wifi-6-bluetooth-5-2-zigbee/
- https://www.elektormagazine.com/articles/bl808-and-cohorts-new-riscv-mcus
- https://www.cnx-software.com/2022/12/02/pine64-ox64-sbc-bl808-risc-v-multi-protocol-wisoc-64mb-ram/
tags:
- risc-v
- wireless
- IoT
- SoC
- embedded
- AI-edge
- bouffalo-lab
type: entity
updated: 2026-06-27
---

# Bouffalo Lab BL808 / BL616

Bouffalo Lab BL808 and BL616 are RISC-V wireless system-on-chip devices targeting IoT, wearables, and edge AI applications. The BL808 is the flagship: a heterogeneous multi-core design combining a 64-bit RV64IMAFCV core at 480 MHz (multimedia subsystem) with a 32-bit RV32IMAFCP core at 320 MHz (wireless subsystem), integrating WiFi 4 (802.11 b/g/n), Bluetooth 5.0, and 802.15.4 (Zigbee) radios alongside a neural network accelerator and 64 MB embedded PSRAM. The BL616 is a single-core compact variant (RV32IMAFCP at 320 MHz) with WiFi 6, Bluetooth 5.2, and Zigbee/Thread/Matter support, aimed at cost-sensitive smart home products. Both chips are notable for being fully RISC-V throughout, including their wireless protocol stacks, distinguishing them from hybrid RISC-V/ARM wireless SoCs.

## Key Claims

- BL808 uses a heterogeneous dual-core architecture: RV64IMAFCV at 480 MHz (multimedia/AI) and RV32IMAFCP at 320 MHz (wireless/RF).
- BL808 integrates 64 MB embedded PSRAM, WiFi 4, Bluetooth 5.0, and 802.15.4 (Zigbee) in a single package.
- BL808 includes a dedicated NPU for neural network inference supporting audio and vision AI applications.
- BL616 is a 32-bit RV32IMAFCP core at up to 320 MHz with 480 KB SRAM and 4 MB internal flash.
- BL616/BL618 supports WiFi 6 (802.11ax), Bluetooth 5.2 dual-mode, and 802.15.4 for Zigbee, Thread, and Matter protocols.
- BL616 includes a USB 2.0 High-Speed OTG port at 480 Mb/s, unusual for a sub-$3 MCU.
- Pine64 Ox64 ($6 SBC) is based on the BL808, demonstrating that a Linux-capable RISC-V board can cost under $10.

## Relationships

- [[risc_v_zve_sub_extensions]]: BL808's RV64IMAFCV core implements embedded vector extensions for AI acceleration kernels.
- [[risc_v_p_extension]]: BL616's IMAFCP designation includes the P (packed-SIMD) extension for DSP/audio processing.
- [[muriscv_nn]]: muRISCV-NN's optimized kernels can target BL808/BL616 for tinyML inference.
- [[allwinner_d1]]: Both are mass-market RISC-V SoCs targeting AIoT; D1 targets higher-end Linux workloads while BL808 focuses on wireless edge AI.

## Sources

- https://files.pine64.org/doc/datasheet/ox64/BL808_DS_en_1.1(open).pdf
- https://www.cnx-software.com/2022/12/29/bouffalo-lab-bl616-bl618-risc-v-mcu-wifi-6-bluetooth-5-2-zigbee/
- https://www.elektormagazine.com/articles/bl808-and-cohorts-new-riscv-mcus
- https://www.cnx-software.com/2022/12/02/pine64-ox64-sbc-bl808-risc-v-multi-protocol-wisoc-64mb-ram/
