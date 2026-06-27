---
type: entity
tags: [risc-v, SoC, single-board-computer, StarFive, VisionFive, production]
sources:
  - https://www.cnx-software.com/2022/08/29/starfive-jh7110-risc-v-processor-specifications/
  - https://www.design-reuse.com/news/52544/starfive-risc-v-jh7110-soc-visionfive-2-sbc.html
  - https://riscv.org/blog/starfive-announced-2-high-performance-risc-v-products-jh7110-soc-and-visionfive-2-sbc-starfive/
  - https://www.phoronix.com/review/visionfive2-riscv-benchmarks
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# StarFive JH7110

The StarFive JH7110 is a production 64-bit RISC-V SoC manufactured on TSMC's 28 nm process, designed to power affordable single-board computers (SBCs). It is the basis of the VisionFive 2 board — described at launch as the world's first mass-production RISC-V SBC with an integrated 3D GPU. The JH7110 features six RISC-V cores in total: four high-performance 64-bit cores running the main OS at up to 1.5 GHz with 2 MB shared L2 cache, plus one 64-bit monitoring core and one 32-bit real-time core. Its CoreMark score reaches 5.09 CoreMarks/MHz. For multimedia, the SoC integrates an Imagination Technologies IMG BXE-4-32 MC1 GPU supporting OpenCL 3.0 and Vulkan 1.2, H.264/H.265 video codecs, and an ISP. Importantly, the JH7110 does not include a dedicated NPU or neural network accelerator — a regression from the earlier JH7100 which had an NVDLA and neural network engine. AI workloads on JH7110 run on the CPU cores (leveraging standard RISC-V scalar instructions) or via GPU compute. The VisionFive 2 board is priced around $55–100 USD (4 GB and 8 GB LPDDR4 variants) and represents one of the first widely available, Linux-ready RISC-V SBC platforms, making it a common target for RISC-V software ecosystem development and porting.

## Key Claims

- Quad-core 64-bit RISC-V CPU at up to 1.5 GHz; plus one 64-bit monitoring core and one 32-bit RT core (6 cores total).
- Fabricated on TSMC 28 nm process; 2 MB shared L2 cache.
- CoreMark score: 5.09 CoreMarks/MHz.
- Integrated Imagination IMG BXE-4-32 MC1 GPU with OpenCL 3.0 and Vulkan 1.2 support.
- No dedicated NPU — AI inference relies on CPU scalar execution or GPU compute.
- VisionFive 2 SBC based on JH7110 launched at ~$55 USD (4 GB) to ~$100 USD (8 GB LPDDR4).
- First mass-production RISC-V SBC with integrated 3D GPU, enabling practical RISC-V Linux desktop use.

## Relationships

- [[canaan_kendryte_k230]]: K230 is a competing RISC-V SoC with dedicated NPU (6 TOPS) targeting AI-first edge applications vs. JH7110's multimedia focus.
- [[risc_v_vector_extension]]: JH7110 CPU cores do not implement RVV 1.0; AI speedup from vector extensions is absent.
- [[tvm_riscv_backend]]: TVM can compile models for JH7110's scalar RISC-V cores but without RVV optimization.

## Sources

- https://www.cnx-software.com/2022/08/29/starfive-jh7110-risc-v-processor-specifications/
- https://www.design-reuse.com/news/52544/starfive-risc-v-jh7110-soc-visionfive-2-sbc.html
- https://riscv.org/blog/starfive-announced-2-high-performance-risc-v-products-jh7110-soc-and-visionfive-2-sbc-starfive/
- https://www.phoronix.com/review/visionfive2-riscv-benchmarks
