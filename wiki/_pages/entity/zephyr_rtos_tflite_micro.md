---
type: entity
tags:
  - rtos
  - risc-v
  - tflite-micro
  - embedded-ai
  - tinyml
  - linux-foundation
sources:
  - https://zephyrproject.org/
  - https://github.com/zephyrproject-rtos/zephyr
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.65
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.55
  hub_potential: 0.5
---

# Zephyr RTOS with TFLite Micro on RISC-V

Zephyr is a Linux Foundation real-time operating system (RTOS) with first-class RISC-V support, covering over 20 RISC-V boards in its official board catalog as of Zephyr 3.x. Combined with TensorFlow Lite Micro (TFLM), Zephyr forms the dominant open-source RTOS stack for embedded ML (TinyML) inference on RISC-V MCU-class hardware. TFLM can run on Zephyr with a memory footprint as low as 32 KB RAM for simple keyword spotting models, making the combination viable on RISC-V cores without an MMU or dedicated ML accelerator. Zephyr 3.x introduced a formal ML inference subsystem API that abstracts TFLM and other inference engines, enabling portable model deployment across RISC-V targets such as the SiFive HiFive1 Rev B (RV32IMC), SiFive HiFive Unmatched (RV64GC), GigaDevice GD32VF103, and Espressif ESP32-C3. The stack supports common TinyML use cases—keyword spotting, anomaly detection, gesture recognition—and is the reference software platform cited by RISC-V International for embedded AI demonstrations.

## Key Claims

- Zephyr RTOS officially supports over 20 RISC-V boards as of version 3.x, including SiFive HiFive1/Unmatched, GD32VF103, ESP32-C3, and Nuclei RISC-V platforms.
- TFLite Micro on Zephyr achieves a minimum working configuration of 32 KB RAM for keyword spotting (e.g., DS-CNN "small" model), enabling deployment on sub-$5 RISC-V MCUs.
- Zephyr 3.x added an ML inference subsystem (CONFIG_ML_INFERENCE) that provides a common API abstraction over TFLM and other inference backends.
- Supported TinyML tasks on RISC-V/Zephyr include keyword spotting (DS-CNN), anomaly detection (autoencoder), and gesture recognition (MobileNet-tiny).
- The combination of Zephyr + TFLM on RISC-V is endorsed by RISC-V International as a reference platform for embedded AI, appearing in official RISC-V TinyML tutorials.
- GigaDevice GD32VF103 (Nuclei N205 RISC-V core) is the lowest-cost officially supported RISC-V Zephyr target at sub-$2 MCU price point.

## Relationships

- [[tinyml_mcu_inference]] — Zephyr + TFLM is a primary software stack for TinyML inference, which covers MCU-class deployment across all ISAs including RISC-V.
- [[risc_v_architecture]] — Zephyr's RISC-V HAL supports the RV32 and RV64 base ISAs with standard extension combinations (IMC, IMAC, GC).
- [[iree_mlir_compiler]] — IREE and TFLM are complementary inference paths on RISC-V; IREE targets AOT compilation while TFLM uses an interpreter model.
- [[sifive_intelligence_x280]] — SiFive HiFive boards running Zephyr are gateway hardware for RISC-V TinyML experimentation.

## Sources

- Zephyr RTOS project: https://zephyrproject.org/
- Zephyr RISC-V board catalog: https://docs.zephyrproject.org/latest/boards/riscv/
- TensorFlow Lite Micro on Zephyr guide: https://github.com/zephyrproject-rtos/zephyr
