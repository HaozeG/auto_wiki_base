---
cold_start: true
created: 2026-06-27
inbound_links: 4
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://chipsalliance.org
- https://fosdem.org/2025/events/attachments/fosdem-2025-5921-how-to-quickly-build-an-ai-startup-on-open-source-risc-v-cores/slides/238061/2025_02_O_ZrCbM4S.pdf
- https://riscv.or.jp/wp-content/uploads/CHIPS_Alliance_Keynote_RISC-V_Tokyo_compressed.pdf
tags: []
type: entity
updated: 2026-06-27
---

# Chips Alliance and RISC-V Ecosystem Governance

The CHIPS Alliance (Common Hardware for Interfaces, Processors and Systems) is an open-source hardware consortium hosted under The Linux Foundation, with founding members including Google, Western Digital, Esperanto, and SiFive. It operates alongside but independently of two other key governance bodies in the RISC-V ecosystem: RISC-V International (which governs the ISA specification itself) and the OpenHW Group (now under the Eclipse Foundation, which provides industrial-grade verified RISC-V core implementations). This three-tier governance architecture — specification (RISC-V International), open-source IP and tooling (CHIPS Alliance), and verified industrial cores (OpenHW) — forms the institutional backbone of the RISC-V ecosystem. The CHIPS Alliance hosts a portfolio spanning RISC-V core families (Western Digital's SweRV EH1/EH2/EL2, VeeR), verification tools (Verilator, riscv-dv, cocotb), chiplet interconnect standards (AIB for die-to-die physical interface, OmniXtend for cache coherence over Ethernet), open-source EDA flows (OpenROAD/OpenLANE, OpenFASoC), and hardware construction languages (Chisel/FIRRTL). Its governance structure includes a Governing Board (business decisions, budgets, trademarks), Technical Steering Committee (project coordination), and Outreach Committee (evangelism and events), with membership tiers from Platinum to Individual. For AI toolchains specifically, CHIPS Alliance projects provide critical infrastructure — Verilator enables open-source simulation of AI accelerators, Chisel/FIRRTL is used by Google's TPU design flow and SiFive's core generation, and the AIB standard is adopted in chiplet-based AI processors. The ecosystem is further supported by the FOSSI Foundation (Free and Open Source Silicon), lowRISC (OpenTitan root of trust), and EU-funded initiatives like the TRISTAN project (46 participants over 36 months) which develops open-source RISC-V building blocks for European SMEs.

## Key Claims

- The RISC-V ecosystem operates under a three-tier governance model: RISC-V International sets the ISA specification, CHIPS Alliance hosts open-source IP and EDA tools, and OpenHW Group (Eclipse Foundation) delivers industrially verified core implementations — each with distinct membership, licensing, and governance structures.
- The CHIPS Alliance hosts Verilator, the most widely used open-source RTL simulator, which is capable of simulating RISC-V AI accelerator designs at speeds sufficient for software development and architectural exploration without commercial EDA licenses.
- Western Digital's SweRV core family (EH1, EH2, EL2) is hosted within CHIPS Alliance and was used in over 1 billion shipped storage controllers, making it one of the most commercially deployed open-source RISC-V core designs.
- The AIB (Advanced Interface Bus) standard for die-to-die physical interconnect, developed by Intel and contributed to CHIPS Alliance, enables chiplet-based AI processors where RISC-V host dies connect to accelerator chiplets via an open, royalty-free interface.
- Antmicro and Google collaborated on a CHIPS Alliance verification methodology combining Verible (SystemVerilog linting/formatting), riscv-dv (random instruction generation), and cocotb/pyuvm (Python-based co-simulation) — this flow uncovered real silicon bugs in the VeeR EL2 core used in the Caliptra Root of Trust project driven by Google, AMD, NVIDIA, and Microsoft.
- The EU TRISTAN project (2023–2026, 46 participants) specifically targets open-source RISC-V building blocks for AI and embedded applications, with deliverables flowing through CHIPS Alliance and OpenHW governance structures to ensure European industrial adoption.

## Relationships

- [[openhw_cva6]]: OpenHW's CVA6 core is verified using CHIPS Alliance tools (Verilator, riscv-dv) and the two organizations coordinate on open-source hardware quality standards through complementary governance roles.
- [[pulp_platform]]: PULP Platform cores (Ibex, CV32E40P, CVA6) flow through OpenHW for industrial verification, with CHIPS Alliance providing the EDA infrastructure — the three organizations form a pipeline from academic research to industrial deployment.
- [[tenstorrent_tt_ascalon]]: Tenstorrent's chiplet-based AI processors using RISC-V cores represent a commercial implementation of the chiplet vision that CHIPS Alliance's AIB and OmniXtend standards aim to standardize.
- [[riscv_matrix_extension]]: The AME specification, once ratified by RISC-V International, would flow through CHIPS Alliance for open-source reference implementations and through OpenHW for inclusion in verified core products.

## Sources

- https://chipsalliance.org
- https://fosdem.org/2025/events/attachments/fosdem-2025-5921-how-to-quickly-build-an-ai-startup-on-open-source-risc-v-cores/slides/238061/2025_02_O_ZrCbM4S.pdf
- https://riscv.or.jp/wp-content/uploads/CHIPS_Alliance_Keynote_RISC-V_Tokyo_compressed.pdf
