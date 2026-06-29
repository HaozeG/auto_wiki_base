---
cold_start: false
constraints:
- tight power and memory constraints
- edge computing
created: YYYY-MM-DD
hardware_targets:
- Vector RISC-V core with tightly coupled DIMC tile
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.5
sources:
- https://semiiphub.com/pulse/technical-articles/in-pipeline-integration-of-digital-in-memory-computing-into-risc-v-vector-architecture-to-accelerate-deep-learning
tags:
- RISC-V
- DIMC
- Vector
- AI
- accelerator
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# Vector RISC-V DIMC Architecture

The Vector RISC-V DIMC Architecture is a novel hardware extension that integrates a Digital In-Memory Computing (DIMC) unit directly into the execution stage of a RISC-V vector processor pipeline for accelerating deep learning inference at the edge. Proposed by researchers from Politecnico di Milano and STMicroelectronics, this architecture extends the RISC-V Vector ISA with four custom instructions for data loading, computation, and write-back, enabling flexible control over DIMC tile operations. The design targets energy-constrained edge devices by reducing data movement between memory and compute units. Experimental results on ResNet-50 inference show high DIMC tile utilization and a sustained throughput of 137 GOP/s, achieving a 217× speedup over a baseline RISC-V core and a 50× area-normalized speedup even under near-resource-limit conditions.

## Key Claims

- The architecture integrates a DIMC tile into the execution stage of a RISC-V vector pipeline.
- Four custom instructions are added to the RISC-V Vector ISA: data loading, computation, and write-back.
- The design achieves 137 GOP/s peak throughput on ResNet-50 inference.
- Speedup of 217× over a baseline RISC-V core, and 50× area-normalized speedup.
- Targeting edge applications with tight power and memory constraints.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector (V) extension with custom DIMC instructions.
- Vector/matrix/accelerator support: DIMC tile tightly coupled in execution pipeline.
- Memory/cache/TLB/DMA: Not specified in available source; requires additional reference.
- Compiler/toolchain support: Not specified; custom instructions require toolchain support.

## Relationships

- [[Sipeed_MAIX_series]] – A development board series for edge AI using RISC-V; the DIMC architecture could be relevant for future accelerator integration.
- (Insufficient context for additional cross-links.)

## Sources

- [In-Pipeline Integration of Digital In-Memory-Computing into RISC-V Vector Architecture to Accelerate Deep Learning](https://semiiphub.com/pulse/technical-articles/in-pipeline-integration-of-digital-in-memory-computing-into-risc-v-vector-architecture-to-accelerate-deep-learning)
