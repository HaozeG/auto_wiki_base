---
canonical_name: K230
aliases:
- Kendryte K230
- K230 SoC
- CanMV-K230
- CanMV K230
- K230 CanMV
- Kendryte K230 CanMV
- CanMV K230 development board
- CanMV K230 v1.1
subtype: hardware_target
type: hardware_target
tags: []
sources:
- raw/cache/ad5bac76fff61d4e.md
- https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
- raw/cache/8dc1b8fc652db78e.md
- https://deepwiki.com/kendryte/k230_canmv_docs
- raw/cache/e6bdd614ff99edbc.md
- https://owhinata.github.io/canmv-k230/en/
- raw/cache/f9558347e39a510f.md
- https://www.kendryte.com/en/proDetail/230
hardware_targets:
- K230
toolchains:
- K230_SDK
- nncase
- AI Cube
- KTS (k230_training_scripts)
- CanCollectorPlus
constraints:
- multi-precision AI computing
- utilization >70% for some typical networks
- low latency
- low power consumption
- quick startup
- high security
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.2
  hub_potential: 0.3
source_url: https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
fetched_at: '2026-07-03T13:35:08.582836+00:00'
---

# K230

The K230 is a system-on-chip (SoC) from Canaan Technology's Kendryte series, designed for AIoT applications. It features a multi-heterogeneous unit accelerated computing architecture that integrates two Xuantie C908 RISC-V 64-bit cores in a heterogeneous configuration: a big core (CPU1) operating at 1.6 GHz running the RT-Smart real-time OS, and a little core (CPU0) operating at 800 MHz running Linux 5.10.4 for system control, networking, and user interaction. The big core includes RISC-V Vector 1.0 support with a 128-bit vector length. The SoC also includes 512 MB LPDDR3 memory and a new generation KPU (Knowledge Process Unit) intelligent computing unit that supports multi-precision AI computing (INT8/INT16 quantized inference) and achieves utilization rates exceeding 70% for some typical networks. Models are compiled from ONNX and TFLite formats to kmodel format using the nncase compiler. The two cores communicate through a shared filesystem at /sharefs. Additionally, the chip includes specialized hardware acceleration units for scalar, vector, and graphic computations, such as 2D and 2.5D units, enabling full-process acceleration of image, video, audio, and AI tasks. Documentation and development tools provided include the K230_SDK, nncase model converter, AI Cube, and KTS training scripts. The SoC powers the CanMV K230 development board, which adds 2.4 GHz WiFi (via Broadcom bcmdhd) and USB serial connectivity.

## Key Claims

- Multi-heterogeneous unit architecture with two RISC-V cores and KPU.
- Dual-core heterogeneous architecture: big core at 1.6 GHz (RT-Smart) and little core at 800 MHz (Linux 5.10.4).
- Big core implements RISC-V Vector 1.0 with 128-bit vector registers.
- Multi-precision AI computing with >70% utilization for some typical networks; KPU supports INT8/INT16 quantized model inference.
- Hardware acceleration for 2D/2.5D graphics.
- Low latency, high performance, low power, quick startup, high security.
- AI development flow: data preparation, model training, model conversion (ONNX/TFLite to kmodel via nncase), KModel generation, image burning, board operation.
- Supports general AI computing frameworks.
- Tools: K230_SDK, nncase, AI Cube, KTS, CanCollectorPlus, online cloud training platform.
- Over 50 AI demo examples for different scenarios.
- CanMV K230: a MicroPython-based development environment for the K230, providing hardware abstraction, media processing pipelines, computer vision, and AI inference capabilities. Its PipeLine class implements a dual-stream architecture: a direct display stream for low latency and a second stream with ai2d preprocessing and KPU inference with overlay, optimized for edge computing applications.
- Two cores communicate via a shared filesystem (/sharefs).
- Board includes 512 MB LPDDR3 RAM and 2.4 GHz WiFi (Broadcom bcmdhd).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, RVV 1.0 (128-bit) on big core.
- Vector/matrix/accelerator support: KPU for AI, RVV for operators not supported by KPU (e.g., softmax), 2D/2.5D units for graphics.
- Memory/cache/TLB/DMA: 512 MB LPDDR3; further details not specified in available sources.
- Compiler/toolchain support: Linux 5.10.4, RT-Smart, nncase, CanMV MicroPython, K230_SDK, AI Cube, KTS, CanCollectorPlus.

## Relationships

- [[c908-wino-gemm-optimization]]: The K230's big core is a XuanTie C908 processor; the optimization recipe for SHL-based im2col/GEMM and Winograd convolution targets the same core and applies directly to K230 deployments.

## Sources

- https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
- kendryte/k230_canmv_docs on DeepWiki (https://deepwiki.com/kendryte/k230_canmv_docs)
- https://owhinata.github.io/canmv-k230/en/
