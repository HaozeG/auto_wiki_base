---
cold_start: true
created: '2026-07-09'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://www.cnx-software.com/2023/10/21/sophgo-sg2380-16-core-sifive-p670-risc-v-processor-20-tops-ai-accelerator/
tags:
- risc-v
- sophgo
- ai-accelerator
- china-semiconductor
type: entity
updated: '2026-06-27'
---

# Sophgo SG2380

The Sophgo SG2380 is a 16-core RISC-V microprocessor based on SiFive's P670 cores, operating at a clock speed of 2.5 GHz, with an integrated neural processing unit capable of 20 TOPS (trillion operations per second) for AI inference workloads. Unveiled in October 2023, it represents one of the highest-performance RISC-V chips announced at the time, targeting server, edge computing, and AI acceleration applications. The SG2380 is designed by Sophgo, a Chinese fabless semiconductor company, and highlights the growing capability of the open-standard RISC-V architecture to compete with established ARM and x86 processors in high-performance segments, particularly for AI-accelerated computing in environments subject to export control restrictions.

## Key Claims

- The SG2380 integrates 16 SiFive P670 RISC-V cores, each clocked at up to 2.5 GHz, providing general-purpose compute for server and edge workloads.
- It includes a dedicated AI accelerator achieving 20 TOPS at integer precision, enabling on-chip inference without a separate GPU or NPU.
- The chip is fabricated on an unspecified advanced process node (likely 7 nm or similar), as inferred from its performance and power targets.
- Sophgo positioned the SG2380 as a direct competitor to ARM-based server SoCs like the Ampere Altra and to RISC-V chips such as the StarFive JH7110, but with higher core count and AI capabilities.
- The announcement in late 2023 signals the maturation of RISC-V for high-performance, AI-focused applications, especially in markets seeking alternatives to controlled x86/ARM exports.

## Relationships

- [[ai_chip_export_controls]] — The SG2380 is a Chinese-designed chip that could serve as a domestic alternative to restricted foreign AI accelerators, potentially influencing export control dynamics.
- [[risc_v_vector_extensions]] (proposed page) — The chip likely supports the RISC-V vector extension (RVV) for parallel compute, though not explicitly confirmed.

## Sources

- https://www.cnx-software.com/2023/10/21/sophgo-sg2380-16-core-sifive-p670-risc-v-processor-20-tops-ai-accelerator/
