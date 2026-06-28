---
cold_start: false
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.spacemit.com/en/spacemit-x60-core/
- https://linuxgizmos.com/spacemit-x60-risc-v-processor-enables-ai-and-high-speed-storage-in-bit-brick-k1-embedded-board/
- https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
- https://www.tomshardware.com/pc-components/cpus/risc-v-cpu-comes-to-a-mini-itx-motherboard
tags:
- risc-v
- soc
- ai-acceleration
- edge-ai
- rva22
type: entity
updated: 2026-06-27
---

# SpacemiT K1 SoC

The SpacemiT K1 is a Chinese-designed octa-core RISC-V system-on-chip released in 2024, built around eight SpacemiT X60 processor cores and targeting edge AI, embedded computing, and single-board computer applications. The K1 implements the RVA22 profile — the first ratified RISC-V application profile standard — and delivers 2.0 TOPS of AI compute through 16 custom AI instructions that accelerate matrix multiplication and sliding window convolutions. These custom instructions are layered on top of the standard RISC-V 64GCV ISA (RV64GCV) and operate on 256-bit vector units. The chip is manufactured at a competitive process node and is notable for being among the first commercially available RISC-V SoCs to pass RVA22 compliance testing, offering a clear baseline for application software portability across RISC-V hardware. The K1 supports TensorFlow Lite, TensorFlow, and ONNX Runtime inference workloads without code changes, lowering the barrier for deploying neural networks on open-hardware platforms.

## Key Claims

- The SpacemiT K1 integrates eight X60 RISC-V cores in a dual-cluster design: Cluster 0 (four cores with AI extension, 32 KB L1, 512 KB L2, 512 KB TCM) and Cluster 1 (four cores, 32 KB L1, 512 KB L2), delivering 2.0 TOPS of AI performance.
- The X60 core implements 16 custom RISC-V AI instructions covering matrix multiplication and sliding window computation, built on top of 256-bit RVV vector extensions and the RVA22 profile.
- The K1 SoC includes an Imagination BXE-2-32 GPU clocked at 819 MHz with Vulkan 1.3 and OpenCL 3.0 support, plus a video engine supporting 4K H.265, H.264, VP9, and VP8 encode/decode.
- Security features include RISC-V PMP and ePMP extensions, secure boot, secure storage, and hardware acceleration for AES, SHA, RSA, SM2, SM3, and SM4 algorithms.
- The K1 has been adopted in commercially available boards including the Banana Pi BPI-F3, the Bit-Brick K1, and the Jupiter mini-ITX motherboard, demonstrating broad ecosystem traction for an early RISC-V AI SoC.

## Relationships

- [[risc_v_profiles_rva]] — The K1 implements the RVA22 profile, the ratified RISC-V application profile that the K1 was among the first commercial SoCs to satisfy.
- [[risc_v_vector_extension]] — The X60 core uses 256-bit RVV 1.0 vector units as the foundation for its AI instruction extensions.
- [[onnx_runtime_riscv]] — The K1 officially supports ONNX Runtime inference, enabling direct deployment of pre-trained models.
- [[spacemit_k3]] — The K3 is SpacemiT's successor SoC using the X100 core with 60 TOPS AI performance, replacing the K1's 2 TOPS.
- [[tinyml_riscv]] — The K1 targets similar edge-AI inference workloads as the TinyML-on-RISC-V ecosystem.

## Sources

- SpacemiT X60 Core product page: https://www.spacemit.com/en/spacemit-x60-core/
- LinuxGizmos review of K1 and Bit-Brick K1 board: https://linuxgizmos.com/spacemit-x60-risc-v-processor-enables-ai-and-high-speed-storage-in-bit-brick-k1-embedded-board/
- Banana Pi BPI-F3 technical docs: https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
- Tom's Hardware Jupiter mini-ITX coverage: https://www.tomshardware.com/pc-components/cpus/risc-v-cpu-comes-to-a-mini-itx-motherboard
