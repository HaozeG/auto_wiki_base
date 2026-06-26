---
type: entity
tags: [npu, edge-ai, arm, inference, mobile, mcu]
sources:
  - https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55
  - https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65
  - https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85
  - https://armkeil.blob.core.windows.net/developer/Files/pdf/ML%20on%20Arm/arm-ethos-n78-product-brief.pdf
  - https://www.jonpeddie.com/news/arm-ethos-n78-scales-npu-ip-to-10-tops/
  - https://developer.arm.com/documentation/109267/0103/Arm-Ethos-U-NPU/Ethos-U-hardware-architecture
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Arm Ethos NPU

The Arm Ethos family is a line of dedicated neural processing unit (NPU) IP cores designed for on-device AI inference across two distinct market segments: the Ethos-U microNPU series targets Cortex-M microcontrollers in IoT and embedded systems, while the Ethos-N series targets mobile application processors requiring multi-TOPS throughput. Both product lines are licensable silicon IP, meaning SoC vendors integrate Ethos cores alongside Arm CPU IP rather than purchasing finished chips. Ethos NPUs implement fixed-function dataflow engines optimized for MAC-intensive convolution and matrix operations, offloading the host CPU entirely for supported operator graphs. The U-series in particular was designed to fit within the severe area and power budgets of MCU SoCs, operating on tightly coupled SRAM without requiring DRAM. This design philosophy allows battery-constrained and energy-harvesting IoT nodes to run quantized neural networks for tasks such as keyword spotting, anomaly detection, and image classification at milliwatt or sub-milliwatt active power. The N-series is positioned above the U-series, targeting premium and mid-range Android SoCs where peak throughput and DRAM bandwidth efficiency are primary constraints. Arm provides the Vela compiler and Android NNAPI driver to translate TensorFlow Lite and ONNX models to Ethos hardware, covering both product lines.

## Key Claims

- **Ethos-U55 configurability**: The Ethos-U55 microNPU is available in four MAC configurations — 32, 64, 128, or 256 MACs per cycle — delivering 64 to 512 GOPS at 1 GHz; when paired with the Cortex-M55 CPU, Arm claims a 480× ML performance uplift over prior Cortex-M designs without an NPU.
- **Ethos-U65 memory interfaces**: The Ethos-U65 scales to 256 and 512 MACs per cycle and connects to both on-chip SRAM and DRAM via 128-bit AXI interfaces, enabling it to handle larger models than the SRAM-only U55.
- **Ethos-U85 peak throughput**: The Ethos-U85 scales from 128 to 2048 MACs per cycle, covering 256 GOPS to 4 TOPS at 1 GHz, with up to six 128-bit AXI5 interfaces and 29–267 KB of internal SRAM; it also adds transformer and sparse model acceleration not present in earlier U-series designs.
- **Ethos-N78 mobile-tier performance**: The Ethos-N78 reaches 10 TOPS at its maximum configuration across 90-plus configurable variants, and reduces DRAM bandwidth by 40% compared to its predecessor (Ethos-N77), making it practical for integration in area-constrained mobile SoC floorplans.
- **Commercial deployments**: The Ethos-N78 shipped in the Samsung Exynos 2200 (powering the Galaxy S22 series in 2022) and the MediaTek Dimensity 9000 series, establishing it as one of the highest-volume NPU IP cores in Android devices.
- **Framework support**: Ethos-U NPUs are supported by TensorFlow Lite Micro and the Arm Vela compiler toolchain; Ethos-N NPUs integrate with the Android NNAPI driver stack, enabling framework-agnostic deployment pipelines.

## Relationships

- [[apple_neural_engine]] — A competing dedicated inference accelerator; Apple ANE is a proprietary monolithic design tightly integrated with Apple Silicon, whereas Ethos is licensable IP deployed across multiple third-party SoCs.
- [[qualcomm_ai_engine]] — Qualcomm's AI Engine (Hexagon NPU) occupies a similar mobile-tier niche to Ethos-N78; both ship in high-volume Android SoCs but differ in ISA philosophy and compiler stack.
- [[fpga_riscv_isa_extension_nn_inference]] — An alternative deployment path for edge inference using reconfigurable logic or ISA extensions rather than fixed-function NPU IP; relevant for comparing area-efficiency trade-offs.
- [[int8_fp8_quantization_llm_inference]] — INT8 quantization is mandatory for Ethos-U deployment, as the U-series operates exclusively on 8-bit integer operands; quantization methodology directly determines whether a model fits within Ethos-U memory and MAC budgets.
- [[arm_sme]] — Arm's Scalable Matrix Extension targets server and laptop-class Cortex-A/X cores for larger matrix workloads; Ethos NPUs serve the complementary MCU and mobile market segments where SME is not present.

## Sources

- Arm Ethos-U55 product page: https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55
- Arm Ethos-U65 product page: https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65
- Arm Ethos-U85 product page and blog: https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85 ; https://newsroom.arm.com/blog/ethos-u85
- Arm Ethos-N78 product brief: https://armkeil.blob.core.windows.net/developer/Files/pdf/ML%20on%20Arm/arm-ethos-n78-product-brief.pdf
- Jon Peddie Research on Ethos-N78: https://www.jonpeddie.com/news/arm-ethos-n78-scales-npu-ip-to-10-tops/
- Arm ML Developer Guide (Ethos-U hardware architecture): https://developer.arm.com/documentation/109267/0103/Arm-Ethos-U-NPU/Ethos-U-hardware-architecture
- NAND Research note on Ethos-U65: https://nand-research.com/wp-content/uploads/2024/04/2024-04-10-RN-Arm-U65-NPU.pdf
