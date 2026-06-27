---
type: entity
tags: [risc-v, hardware, AI-acceleration, vector-processing, ISA]
sources:
  - https://semiwiki.com/ip/sifive/364948-risc-v-extensions-for-ai-enhancing-performance-in-machine-learning/
  - https://www.jonpeddie.com/news/the-risc-v-vector-extensions-for-ai/
  - https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
  - https://arxiv.org/pdf/2507.01457
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 6
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# RISC-V Vector Extension (RVV)

The RISC-V Vector Extension (RVV) is a standardized SIMD-style ISA extension for the open RISC-V architecture that enables data-parallel computation across configurable-width vector registers. Version 1.0 was ratified in 2021 and has since shipped in production silicon from multiple vendors, including Alibaba T-Head, SiFive, and Ventana. RVV's defining feature is a variable-length vector model: programs specify operations on "virtual" vectors of any length, and hardware executes them across the physical vector register width (VLEN), making the same binary portable across chips with 128-bit to 512-bit or wider register files without recompilation.

## Key Claims

- RVV 1.0 supports vector registers up to 4096 effective bits when using LMUL=8 grouping, enabling chips like the SiFive X280 (512-bit VLEN) to operate on 4096-bit logical vectors per instruction cycle.
- The RVA23 profile, ratified by RISC-V International, makes the Vector Extension mandatory for the first time; in RVA22 it was optional, creating fragmentation across implementations.
- NVIDIA shipped over 1 billion RISC-V cores in 2024 and announced plans to port its CUDA AI acceleration stack to RVA23-compliant cores, signaling mainstream datacenter adoption.
- Enabling RVV in OpenBLAS yields up to 1.3× inference speedup on general matrix workloads; specialized implementations such as SPEED achieve 287–738 GOPS at INT4–INT8 precision with over 1000 GOPS/W energy efficiency.
- TVM MetaSchedule auto-tuned RVV kernels achieve a mean 46% reduction in inference latency compared to GCC auto-vectorization and 35% faster execution compared to LLVM on commercial RVV 1.0 SoCs.
- AI model workloads (especially LLMs) have shifted demand from pure vector SIMD toward matrix operations, driving four competing matrix-extension proposals within RISC-V task groups targeting edge, cloud, and decode-heavy inference scenarios.

## Relationships

- [[alibaba_xuantie_c950]] — C950 implements RVA23 and extends RVV with the proprietary Attached Matrix Extension (AME)
- [[sifive_intelligence_x280]] — X280 implements 512-bit VLEN RVV 1.0; Gen 2 adds FP4/FP8 support
- [[ventana_veyron_v2]] — Veyron V2 adopted RVA23 (with RVV) as a key upgrade over V1
- [[tvm_riscv_backend]] — TVM MetaSchedule targets RVV intrinsics for auto-tuned neural network kernels
- [[tenstorrent_tt_ascalon]] — Ascalon carries dual 256-bit RVV 1.0 vector units

## Sources

- RVV AI extensions overview: https://semiwiki.com/ip/sifive/364948-risc-v-extensions-for-ai-enhancing-performance-in-machine-learning/
- RVA23 mandatory vector discussion: https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
- TVM MetaSchedule RVV results: https://arxiv.org/pdf/2507.01457
- SPEED processor GOPS/W: https://arxiv.org/pdf/2409.14017
