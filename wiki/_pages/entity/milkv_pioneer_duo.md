---
type: entity
tags: [risc-v, developer-board, SBC, SG2042, CV1800B, milk-v, sophgo]
sources:
  - https://milkv.io/pioneer
  - https://milkv.io/docs/pioneer/getting-started/processor
  - https://www.circuitstate.com/tutorials/getting-started-with-milk-v-duo-risc-v-linux-development-board/
  - https://www.hackster.io/news/milk-v-unveils-its-third-risc-v-board-in-a-month-the-9-dual-core-linux-capable-milk-v-duo-3fb5d9f978d1
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

# Milk-V Pioneer and Milk-V Duo

Milk-V is a brand of RISC-V developer boards from Shenzhen-based SOPHGO (formerly Cvitek), offering hardware from a $9 microcontroller board (Duo) up to a workstation-class server (Pioneer), collectively demonstrating the range of RISC-V silicon available for native software development. The Milk-V Pioneer is a micro-ATX workstation mainboard powered by SOPHGO's SG2042, a 64-core RISC-V processor built with 16 clusters of 4 XuanTie C920 cores each, running at up to 2 GHz with a 64 MB L3 system cache and 4 DIMM slots supporting up to 128 GB DDR4-3200 ECC RAM. Pioneer provides 32 PCIe Gen4 lanes, five SATA 3.0 ports, two 2.5GbE NICs, and M.2 NVMe storage, making it the first workstation-class many-core RISC-V platform available for open purchase. The Milk-V Duo targets the opposite end of the spectrum: a compact $9 board featuring a Cvitek CV1800B dual-core SoC with one 1 GHz and one 700 MHz XuanTie C906 RISC-V core, 64 MB DDR2, a 0.5 TOPS INT8 NPU, and USB 2.0/Ethernet connectivity. The Duo runs a Linux environment and is aimed at IoT, embedded vision, and AIoT prototyping at minimal cost. Together these boards provide a vertical range of RISC-V platforms enabling native compilation, AI inference, and OS porting without cross-compilation.

## Key Claims

- Milk-V Pioneer uses the SOPHGO SG2042: 64 XuanTie C920 cores across 16 clusters, up to 2 GHz, 64 MB L3 cache.
- Pioneer supports up to 128 GB DDR4-3200 ECC RAM via 4 DIMM slots in a micro-ATX form factor.
- Pioneer offers 32 PCIe Gen4 lanes, five SATA 3.0 ports, and two 2.5GbE ports for datacenter-like I/O.
- Milk-V Duo uses the CV1800B: dual-core C906 (1 GHz + 700 MHz), 64 MB DDR2, 0.5 TOPS INT8 NPU, retailing at approximately $9.
- Duo includes an 8051 microcontroller core plus two RISC-V cores for a three-core heterogeneous design.
- SG2042 is the first commercially available many-core RISC-V CPU explored for LLM inference (V-Seek, arXiv 2503.17422).

## Relationships

- [[alibaba_xuantie_c910_c920]]: Pioneer's SG2042 uses 64 XuanTie C920 cores; Duo uses C906 from the same XuanTie lineage.
- [[canaan_kendryte_k510_k230]]: Both Canaan and SOPHGO are Chinese RISC-V AI SoC vendors targeting edge vision.
- [[llm_inference_riscv]]: V-Seek paper benchmarks LLM inference on Pioneer's SG2042, achieving 4.32 token/s on Llama 8B.

## Sources

- https://milkv.io/pioneer (Pioneer product page with SG2042 specs)
- https://milkv.io/docs/pioneer/getting-started/processor (SG2042 core/cache/memory specs)
- https://www.circuitstate.com/tutorials/getting-started-with-milk-v-duo-risc-v-linux-development-board/ (Duo specs and use cases)
- https://www.hackster.io/news/milk-v-unveils-its-third-risc-v-board-in-a-month-the-9-dual-core-linux-capable-milk-v-duo-3fb5d9f978d1 (Duo launch and pricing)
