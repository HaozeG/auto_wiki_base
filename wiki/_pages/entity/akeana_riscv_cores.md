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
- https://www.prnewswire.com/news-releases/akeana-exits-stealth-mode-with-comprehensive-risc-v-processor-portfolio-challenging-the-semiconductor-industry-status-quo-302220144.html
- https://www.cnx-software.com/2024/08/15/akeana-unveils-10-risc-v-cores-suitable-for-microcontrollers-up-to-data-center-chips/
- https://www.theregister.com/2024/08/13/akeana_riscv_cpus/
- https://www.akeana.com/leveraging-risc-v-as-a-unified-heterogeneous-platform-for-next-gen-ai-chips/
tags:
- risc-v
- processor-ip
- ai-acceleration
- data-center
- startup
type: entity
updated: 2026-06-27
---

# Akeana RISC-V Processor IP

Akeana is a U.S. semiconductor IP company that emerged from stealth in August 2024 with a comprehensive portfolio of ten RISC-V processor cores spanning IoT microcontrollers to data-center-class compute, backed by $100 million in funding. The company positions its IP as a vertically integrated, heterogeneous alternative to Arm's Cortex and Neoverse families, targeting SoC designers who want a single RISC-V ISA spanning all tiers of a product line without cross-ISA software complexity. Akeana ships three core series — the 100 Series (32-bit MCU), 1000 Series (64-bit Linux-capable), and 5000 Series (64-bit high performance) — each software-compatible at the RISC-V ISA level and each pairable with Akeana's AI Matrix computation engine for matrix-multiply offload. A key differentiator is the accompanying System IP portfolio (coherent cluster cache, I/O MMU, interrupt controller, coherence hub, and scalable mesh interconnect), which reduces the integration burden for SoC teams adopting the cores commercially. Akeana's approach treats RISC-V as a unified heterogeneous platform, allowing a single SoC to combine an MCU-class safety island with Linux application cores and data-center-scale cores on the same ISA, an architecture pattern increasingly demanded in automotive, networking, and cloud AI inference chips.

## Key Claims

- Akeana emerged from stealth in August 2024 with $100 million raised and a portfolio of ten RISC-V processor cores ranging from 32-bit microcontrollers to 64-bit data-center cores, making it one of the best-funded RISC-V processor IP startups.
- The Akeana 100 Series (32-bit) achieves 4–9.5 CoreMarks/MHz at up to 2 GHz; the 1000 Series (64-bit, in-order or out-of-order) reaches 5–18 SPECint2006/GHz; the 5000 Series (64-bit high-performance) delivers 20–25 SPECint2006/GHz at up to 3 GHz.
- All three series pair with an AI Matrix computation engine that offloads matrix-multiply operations, enabling systolic-array-style acceleration without requiring a separate ISA or separate tool chain.
- The 1000 Series supports optional multithreading, vector acceleration (RVV), virtualization hypervisor extensions, and AI computation extensions in a configurable in-order or out-of-order pipeline.
- Akeana provides companion System IP blocks — Coherent Cluster Cache, I/O MMU, Interrupt Controller, Scalable Mesh interconnect, and Coherence Hub — allowing SoC designers to build complete multi-core clusters without sourcing additional third-party interconnect IP.

## Relationships

- [[risc_v_vector_extension]] — The 1000 Series optionally integrates RVV vector acceleration, which underpins AI matrix computation in the Akeana ecosystem.
- [[riscv_matrix_extension]] — Akeana's AI Matrix computation engine targets the same matrix-multiply bottleneck that the RISC-V Matrix Extension proposal aims to standardize.
- [[chips_alliance_governance]] — Akeana's IP competes in the RISC-V commercial IP space governed by RISC-V International and complemented by CHIPS Alliance open hardware efforts.
- [[gemmini]] — Gemmini is an open-source systolic-array accelerator for RISC-V; Akeana's AI Matrix engine occupies a similar role but as proprietary licensable IP.
- [[tenstorrent_tt_ascalon]] — Tenstorrent's Ascalon is another RISC-V AI core targeting data-center inference; Akeana competes in the processor IP licensing tier rather than complete SoC design.

## Sources

- Akeana press release (exits stealth, August 2024): https://www.prnewswire.com/news-releases/akeana-exits-stealth-mode-with-comprehensive-risc-v-processor-portfolio-challenging-the-semiconductor-industry-status-quo-302220144.html
- CNX Software technical overview of ten cores: https://www.cnx-software.com/2024/08/15/akeana-unveils-10-risc-v-cores-suitable-for-microcontrollers-up-to-data-center-chips/
- The Register on $100M funding and IP strategy: https://www.theregister.com/2024/08/13/akeana_riscv_cpus/
- Akeana blog on heterogeneous RISC-V AI platform: https://www.akeana.com/leveraging-risc-v-as-a-unified-heterogeneous-platform-for-next-gen-ai-chips/
