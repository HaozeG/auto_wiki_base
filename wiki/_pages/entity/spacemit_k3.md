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
- https://linuxgizmos.com/spacemit-k3-integrates-8-core-risc-v-cpu-cluster-and-60-tops-ai-engine/
- https://cdn-resource.spacemit.com/file/chip/K3/K3_brief_en.pdf
- https://www.cnx-software.com/2026/05/11/rva23-pico-itx-sbc-spacemit-k3-octa-core-risc-v-ai-soc-up-to-32gb-ram-256gb-ufs/
- https://forum.spacemit.com/uploads/short-url/60aJ8cYNmrFWqHn4ddwwSzMLjlY.pdf
tags:
- risc-v
- soc
- ai-acceleration
- rva23
- llm-inference
type: entity
updated: 2026-06-27
---

# SpacemiT K3

The SpacemiT K3 is a Chinese heterogeneous RISC-V AI SoC announced in 2025 and available on development boards from mid-2026, designed to close the gap between ARM-based edge AI platforms and open-ISA hardware. The K3 combines eight high-performance X100 CPU cores with eight dedicated A100 AI cores and delivers 60 TOPS of AI performance at INT4 precision, making it the highest-TOPS RISC-V AI SoC commercially available as of mid-2026. The CPU cluster follows the RVA23 profile — the 2024-ratified RISC-V application profile — and each A100 AI core implements 1024-bit RVV 1.0 vector units optimized for matrix operations. The K3 supports the BF16, FP16, FP8, INT8, and INT4 data types and is capable of running 30B-parameter language models locally, positioning it as the first broadly available RISC-V platform suitable for on-device LLM inference. Competing directly with boards based on the Rockchip RK3588, the K3 is benchmarked as delivering equivalent general-purpose compute with an open ISA advantage for research and customization.

## Key Claims

- The SpacemiT K3 delivers 60 TOPS of AI performance at INT4 precision, using eight dedicated A100 AI RISC-V cores with 1024-bit RVV 1.0 vector units, alongside eight X100 CPU cores clocked up to 2.4 GHz.
- The X100 CPU cluster is RVA23-compliant and achieves 130 KDMIPS of general-purpose compute, enabling K3 to run mainline Linux and standard application software without modification.
- The K3 supports five precision formats — BF16, FP16, FP8, INT8, INT4 — and has been demonstrated running 30B-parameter LLMs locally, making it the first production RISC-V SoC to reach this capability tier.
- Development boards shipping in 2026 (K3 Pico-ITX, K3-CoM260) support up to 32 GB DDR5 RAM and 256 GB UFS storage, with connectivity including 10GbE SFP+, WiFi 6, Bluetooth 5.2, and M.2 Key-B for 5G.
- Benchmarks place K3 performance in the RK3588 class for general compute while providing an open-ISA platform with full mainline Linux kernel support.

## Relationships

- [[spacemit_k1_soc]] — The K1 is SpacemiT's prior SoC (2 TOPS, RVA22), which the K3 succeeds with a 30x improvement in AI throughput and RVA23 compliance.
- [[risc_v_profiles_rva]] — The K3 X100 cluster implements the RVA23 profile, the 2024-ratified RISC-V application profile requiring mandatory vector, cryptography, and hypervisor extensions.
- [[risc_v_vector_extension]] — The A100 AI cores use 1024-bit wide RVV 1.0 vector units as the primary compute engine for AI workloads.
- [[llm_inference_riscv]] — The K3 is the first production RISC-V SoC demonstrated running 30B-parameter LLMs locally.
- [[sophgo_sg2042]] — The SG2042 is another high-core-count RISC-V SoC targeting performance computing; K3 targets edge AI inference instead.

## Sources

- LinuxGizmos K3 announcement: https://linuxgizmos.com/spacemit-k3-integrates-8-core-risc-v-cpu-cluster-and-60-tops-ai-engine/
- SpacemiT K3 brief (official): https://cdn-resource.spacemit.com/file/chip/K3/K3_brief_en.pdf
- CNX Software K3 Pico-ITX coverage: https://www.cnx-software.com/2026/05/11/rva23-pico-itx-sbc-spacemit-k3-octa-core-risc-v-ai-soc-up-to-32gb-ram-256gb-ufs/
- SpacemiT K3 forum technical overview: https://forum.spacemit.com/uploads/short-url/60aJ8cYNmrFWqHn4ddwwSzMLjlY.pdf
