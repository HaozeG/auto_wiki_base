---
cold_start: false
created: '2026-06-26'
inbound_links: 3
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  gap_fill_score: 0.9
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- raw/snippets/tenstorrent_blackhole_snippets.md
tags:
- ai-accelerator
- risc-v
- tensix
- open-source-hardware
type: entity
updated: '2026-06-26'
---

# Tenstorrent Blackhole

Tenstorrent Blackhole is a RISC-V-based AI accelerator designed for standalone deep learning inference and training workloads, developed by Tenstorrent under the leadership of Jim Keller. The accelerator is built around the proprietary Tensix architecture, which integrates 120 Tensix cores comprising 768 RISC-V processors, 32GB of GDDR6 memory, and a high-bandwidth interconnect featuring ten 400GbE ports for scalable multi-card deployments. The Blackhole p150a PCIe card is priced at $1,399 and leverages a fully open-source software stack called Metalium, enabling developers to program the hardware without vendor lock-in. First disclosed at Hot Chips 2024, the Blackhole represents a shift from earlier prototype-stage RISC-V AI accelerators (e.g., FPGA-based custom extensions) to a production-grade chiplet-based system, with Tenstorrent's broader roadmap including both RISC-V CPU chiplets and advanced AI accelerator chiplets for heterogeneous machine learning solutions.

## Key Claims

- The Blackhole p150a incorporates 120 Tensix cores, each containing multiple RISC-V processors, for a total of 768 RISC-V cores.
- The accelerator is equipped with 32GB of GDDR6 memory and uses ten 400GbE links for chip-to-chip and system-level interconnect.
- The Blackhole is priced at $1,399 as a standalone PCIe card, targeting both cloud and edge AI workloads.
- The hardware is supported by the open-source Metalium software stack, providing full programmability and transparency.
- Tenstorrent's roadmap includes RISC-V-based CPU chiplets and next-generation AI accelerator chiplets, indicating a chiplet-based heterogeneous architecture.
- The Blackhole was detailed at Hot Chips 2024, demonstrating its readiness for deployment at scale with industry-leading benchmarks.

## Relationships

- [[tenstorrent]]: Parent company; the Blackhole is Tenstorrent's flagship commercial AI accelerator product built on the Tensix architecture.
- [[tensix_architecture]]: The Blackhole is the first production implementation of the Tensix architecture, which combines RISC-V processing elements and dedicated matrix engines.
- [[riscv_ai_ecosystem]]: As a commercial RISC-V AI accelerator, the Blackhole contributes to the growing ecosystem of RISC-V-based machine learning hardware, bridging the gap between FPGA prototypes and silicon products.
- [[fpga_riscv_isa_extension_nn_inference]]: While FPGA-based RISC-V accelerators (e.g., PYNQ-Z2, Arrow) target low-power edge inference, the Blackhole targets high-throughput data center and edge AI, representing a scale-up of the same RISC-V AI paradigm.
- [[metalium_software_stack]]: The open-source Metalium framework enables users to program the Blackhole directly, mirroring the transparency goals of RISC-V ISA.

## Sources

- raw/snippets/tenstorrent_blackhole_snippets.md: All search snippets (Hot Chips 2024, Tom's Hardware, Awesome Agents) used to extract specifications, pricing, and software details.
