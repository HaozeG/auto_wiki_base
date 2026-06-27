---
type: entity
tags:
  - risc-v
  - soc
  - npu
  - rvv
  - spacemit
  - edge-ai
  - banana-pi
sources:
  - https://www.spacemit.com/key-stone/
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.75
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.55
  hub_potential: 0.45
---

# SpacemiT K1 AI SoC

The SpacemiT K1 (also designated X60) is an 8-core RISC-V application-processor SoC designed by SpacemiT (Beijing Jingjia Microelectronics) for edge AI and single-board computer (SBC) applications. It is one of the first commercially available RISC-V SoCs to integrate an on-chip 2 TOPS neural processing unit (NPU) alongside RVV 1.0 (vector extension) with Zvfh (FP16) support, enabling transformer-class model inference without off-chip accelerators. The K1 implements eight RISC-V RV64GCVB cores based on the X60 microarchitecture, clocked at up to 1.6 GHz in a cluster configuration. It is the SoC in the Banana Pi BPI-F3 SBC, which ships running Bianbu Linux (an Ubuntu derivative) and ArchLinux RISC-V community ports. The K1's inclusion of Zvfh makes it a notable platform for evaluating FP16 ML inference on RISC-V without a discrete NPU, positioning it alongside StarFive JH7110 and SiFive HiFive Premier P550 as commercially available RISC-V SoCs with real ML workload capability.

## Key Claims

- SpacemiT K1 integrates 8 RV64GCVB cores (X60 microarchitecture) at up to 1.6 GHz with an on-chip 2 TOPS INT8 NPU in a single SoC.
- Implements RVV 1.0 with the Zvfh (FP16 half-precision) extension, enabling native FP16 vector ML inference without software emulation.
- The Banana Pi BPI-F3 SBC, powered by K1, ships with 4–16 GB LPDDR4X and eMMC storage; retail price starts at approximately $49 for the 4 GB variant.
- K1 NPU supports INT8 and FP16 precision for standard CNN and transformer inference, targeting object detection (YOLO-class) and lightweight LLM inference at the edge.
- Bianbu Linux (Ubuntu-based), ArchLinux RISC-V, and Fedora RISC-V community ports run on the Banana Pi BPI-F3 as of mid-2024.
- SpacemiT K1 is among the first production RISC-V SoCs to combine RVV 1.0, Zvfh, and an integrated NPU—a combination previously only available in ARM-based SoCs.

## Relationships

- [[spacemit_k1_archlinux]] — Covers the ArchLinux RISC-V porting effort for the Banana Pi BPI-F3 board using the K1 SoC.
- [[risc_v_vector_extension]] — K1 fully implements RVV 1.0 as the vector foundation of its ML compute capability.
- [[riscv_zvfh_extension]] — K1 is one of the first production implementations of Zvfh FP16 in a commercial RISC-V SoC.
- [[starfive_visionfive2_jh7110]] — Competing RISC-V SoC SBC platform with different NPU/GPU approach.
- [[tinyml_mcu_inference]] — K1's NPU and RVV support push edge inference capability well above MCU-class TinyML.

## Sources

- SpacemiT K1 product page: https://www.spacemit.com/key-stone/
- Banana Pi BPI-F3 hardware specifications
- RISC-V software ecosystem reports, 2024
