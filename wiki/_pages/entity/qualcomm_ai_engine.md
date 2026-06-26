---
type: entity
tags: [npu, ai-inference, mobile, datacenter, qualcomm, snapdragon]
sources:
  - https://www.qualcomm.com/processors/ai-engine
  - https://www.qualcomm.com/processors/hexagon
  - https://fuse.wikichip.org/news/6311/a-look-at-qualcomms-data-center-inference-accelerator/
  - https://quic.github.io/cloud-ai-sdk-pages/latest/Getting-Started/Architecture/
  - https://www.qualcomm.com/artificial-intelligence/data-center/cloud-ai-100-ultra
  - https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips
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

# Qualcomm AI Engine and Cloud AI 100

Qualcomm's AI acceleration strategy spans two distinct product lines: the on-device AI Engine embedded in every Snapdragon SoC, and the Cloud AI 100 family of standalone PCIe inference accelerators for datacenter deployment. The on-device AI Engine uses heterogeneous computing—combining Hexagon NPU cores (Neural Signal Processors, or NSPs), Adreno GPU shader cores, Kryo CPU cores, and a low-power Sensing Hub—to route neural network operators to the most efficient execution unit based on operator type and precision. The Hexagon NPU is the primary AI compute element, built on the Hexagon DSP architecture extended with the Hexagon Tensor Accelerator (HTA) and vector extensions. The Cloud AI 100, first shipped in September 2020, is a purpose-built deep learning inference card based on 16 seventh-generation Hexagon-derived AI cores. It targets INT8 and FP16 inference in data center servers with a dramatically higher peak throughput than any Snapdragon SoC but in the same architectural family, making the same quantized model formats portable between edge and cloud deployments. Qualcomm's announced intent to acquire Tenstorrent in 2025 further extends this two-tier strategy into high-throughput training and edge AI hardware.

## Key Claims

- The on-device AI Engine in Snapdragon 865 (2019) delivered 15 TOPS via the Hexagon 698 NPU; successive generations escalated to approximately 26 TOPS in Snapdragon 8 Gen 1, 33 TOPS in Snapdragon 8 Gen 2, 45 TOPS in Snapdragon 8 Gen 3, and 45–75 TOPS in the Snapdragon X Elite PC platform.
- The Snapdragon 8 Gen 3 Hexagon NPU achieved 98% faster inference throughput and 40% better performance-per-watt compared to Snapdragon 8 Gen 2, according to Qualcomm's published benchmarks.
- The Qualcomm Cloud AI 100 SoC integrates 16 seventh-generation AI cores delivering over 400 INT8 TOPS and over 200 FP16 TOPS, with 144 MB of on-chip SRAM and an LPDDR4X memory subsystem providing 136 GB/s of bandwidth and up to 32 GB of capacity.
- Cloud AI 100 is available in three form factors: a full-height PCIe card at up to 75 W TDP, a dual M.2 module at 15–25 W, and a passive M.2e module for embedded deployment—the same model binary targets all three via a shared software stack.
- Cloud AI 100 supports INT8, INT16, FP16, and FP32 precision natively, and shares model compilation tooling with the on-device Qualcomm AI stack through the Qualcomm AI Hub platform.
- Qualcomm announced the acquisition of Tenstorrent in 2025, a move interpreted as accelerating Qualcomm's datacenter AI portfolio beyond inference-only cards toward training-capable accelerators.

## Relationships

- [[qualcomm_hexagon_dsp]] — The Hexagon DSP is the silicon foundation of both the on-device AI Engine NSP cores and the Cloud AI 100 AI cores; the two product lines share the same ISA and programming model.
- [[tenstorrent]] — Qualcomm's 2025 acquisition of Tenstorrent is intended to augment the Cloud AI 100 inference-focused product line with Tenstorrent's training-capable RISC-V + Tensix architecture.
- [[apple_neural_engine]] — Apple ANE and the Qualcomm AI Engine are the two dominant on-device NPU architectures in mobile SoCs; ANE is a fixed-function matrix engine while Qualcomm uses a programmable heterogeneous stack.
- [[google_tpu]] — Google TPU v1 pioneered the datacenter inference accelerator category that Cloud AI 100 targets; both use systolic-array-like matrix engines but Cloud AI 100 adds a tiered on-chip/off-chip memory hierarchy distinct from TPU's design.
- [[intel_amx]] — Intel AMX addresses the same enterprise AI inference problem on CPUs; Cloud AI 100 competes as a dedicated PCIe card that removes the CPU bottleneck at the cost of additional hardware.

## Sources

- Qualcomm AI Engine product page: heterogeneous compute architecture, NSP description
- Qualcomm Hexagon NPU page: TOPS progression per Snapdragon generation
- WikiChip analysis of Cloud AI 100: 16-core SoC, 400 TOPS, 144 MB SRAM, memory specs
- Qualcomm Cloud AI SDK documentation: software stack and precision support
- Qualcomm Cloud AI 100 Ultra product page: form factor and TDP details
- Wikipedia Snapdragon SoC list: per-generation TOPS figures
- The Next Platform (2025): Qualcomm datacenter AI strategy and Tenstorrent context
