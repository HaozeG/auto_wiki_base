---
canonical_name: Allwinner V853
aliases:
- V853
- Allwinner V853S
- Allwinner R853
- Allwinner R853S
- Allwinner V851
- Allwinner V853 SoC
subtype: null
tags: []
hardware_targets:
- Allwinner V853
- Allwinner V853S
- Allwinner R853
- Allwinner R853S
- Allwinner V851
toolchains:
- TensorFlow
- Caffe
- TFLite
- PyTorch
- ONNX
constraints:
- 22nm process
- Arm Cortex-A7 @ 1 GHz
- Alibaba Xuantie E907 RISC-V core
- NPU up to 1 TOPS (V853) / 0.8 TOPS (V853S)
- NPU internal buffer 128 KB
- H.265/H.264 encoding up to 5M@30fps
- H.264 decoding up to 16 megapixels
- 16-bit DDR3/DDR3L memory interface
- SD 3.0/eMMC 5.1 storage
- MIPI DSI display output
- RGB display interface
- Parallel CSI and MIPI CSI camera inputs
- LFBGA 318 package
scorecard:
  novelty_delta: 0.85
  claim_density: 0.9
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/e48b8082875152c6.md
- https://www.cnx-software.com/2022/05/06/allwinner-v853-arm-cortex-a7-risc-v-soc-comes-with-1-tops-npu-for-ai-vision-applications/
source_url: https://www.cnx-software.com/2022/05/06/allwinner-v853-arm-cortex-a7-risc-v-soc-comes-with-1-tops-npu-for-ai-vision-applications/
fetched_at: '2026-07-01T06:52:01.077587+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 6
needs_summary_revision: false
---

# Allwinner V853

The Allwinner V853 is a system-on-chip (SoC) manufactured using a 22nm process, combining an Arm Cortex-A7 CPU core clocked at 1 GHz with an Alibaba Xuantie E907 RISC-V core for low-power control. The SoC integrates a neural processing unit (NPU) delivering up to 1 TOPS (0.8 TOPS for the V853S variant) with a 128 KB internal buffer, supporting AI frameworks including TensorFlow, Caffe, TFLite, PyTorch, and ONNX. Additionally, the chip includes an ISP image processor and a Smart video engine capable of H.265/H.264 encoding up to 5M@30fps and decoding up to 16 megapixels. Memory interfaces include 16-bit DDR3/DDR3L, SD 3.0, eMMC 5.1, and SPI flash. The SoC targets cost-sensitive AI vision applications such as smart door locks, access control, AI webcams, tachographs, and smart desk lamps. The V853 is part of a family that includes the V853S (reduced NPU performance), the R853 and R853S variants designed for robot motor control, and the V851 with built-in 64MB or 128MB memory.

## Key Claims

- Combines Arm Cortex-A7 @ 1 GHz (32 KB I-cache, 32 KB D-cache, 128 KB L2) with Xuantie E907 RISC-V core (16 KB I-cache, 16 KB D-cache).
- NPU provides up to 1 TOPS (V853) or 0.8 TOPS (V853S) with 128 KB internal buffer.
- Supports TensorFlow, Caffe, TFLite, PyTorch, ONNX for model deployment.
- Video engine encodes H.265/H.264 up to 5M@30fps and decodes H.264 up to 16 megapixels (4096x4096).
- ISP supports up to 5M@30fps with resolution up to 3072x3072.
- Memory interface: 16-bit DDR3/DDR3L, SD 3.0, eMMC 5.1, SPI NOR/NAND flash.
- Display outputs: 4-lane MIPI DSI up to 1920x1200@60fps, RGB interface up to 1920x1080@60fps.
- Camera inputs: parallel CSI and 4-lane MIPI CSI (or dual 2-lane) up to 5M@30fps.
- Audio: DAC with 8-192 kHz sample rate, dual ADC, PDM microphone support up to 8 channels.
- Peripherals: 5x I2C, 4x UART, 4x SPI, 8x GPIO, 12-ch PWM, 4x GPADC, USB 2.0 DRD.

## Optimization-Relevant Details

- ISA/profile: Arm Cortex-A7 (ARMv7-A) + Xuantie E907 (RISC-V RV32IMC or similar, used as MCU).
- Vector/matrix/accelerator support: NPU with up to 1 TOPS (INT8 inference), VPU for video encode/decode, ISP for image processing.
- Memory/cache/TLB/DMA: Cortex-A7 L1 cache 32 KB I + 32 KB D, L2 128 KB; E907 L1 cache 16 KB I + 16 KB D; NPU internal buffer 128 KB; external DDR3/DDR3L up to 16-bit bus.
- Compiler/toolchain support: Standard ARM toolchain for Cortex-A7; RISC-V toolchain for E907; NPU toolchain supports TensorFlow, Caffe, TFLite, PyTorch, ONNX (quantization likely required).

## Relationships

- The SoC's NPU performance and application domain overlap with the [[k230]] (Canaan Kendryte K230) which also targets AIoT with a RISC-V core and NPU, though K230 uses dual RISC-V C908 cores and a 6 TOPS NPU.
- The Xuantie E907 RISC-V core is also used in other Allwinner SoCs, but no dedicated page exists yet.  Insufficient context for additional cross-links.

## Sources

- https://www.cnx-software.com/2022/05/06/allwinner-v853-arm-cortex-a7-risc-v-soc-comes-with-1-tops-npu-for-ai-vision-applications/
