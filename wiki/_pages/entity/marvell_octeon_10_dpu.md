---
type: entity
tags:
  - risc-v
  - dpu
  - smartnic
  - network-ai
  - marvell
  - 5g
sources:
  - https://www.marvell.com/products/data-processing-units.html
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.7
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.5
  hub_potential: 0.4
---

# Marvell OCTEON 10 DPU

The Marvell OCTEON 10 is a data processing unit (DPU) family in the CN10K series that integrates RISC-V cores alongside ARM Cortex-A78 cores for programmable packet processing, 5G infrastructure, and cloud SmartNIC applications. The hybrid ISA architecture—ARM for control-plane tasks, RISC-V for flexible offload—distinguishes OCTEON 10 from purely ARM-based DPUs. The CN10K family scales to 36 cores at up to 2.0 GHz, supports 400 GbE line-rate processing, and integrates an on-chip ML inference accelerator targeting network anomaly detection, encrypted traffic classification, and real-time packet filtering without host CPU involvement. OCTEON 10 competes directly with NVIDIA BlueField-3 and Intel Infrastructure Processing Unit (IPU) in the SmartNIC/DPU market. Marvell positions OCTEON 10 as a converged DPU for hyperscale data centers, telco 5G RAN, and enterprise security appliances where line-rate ML-assisted network intelligence is critical.

## Key Claims

- OCTEON 10 CN10K series integrates RISC-V cores for programmable packet processing alongside ARM Cortex-A78 application cores, a hybrid ISA design unique among major DPU products.
- The CN10K family scales to 36 cores, clocked up to 2.0 GHz, with 400 GbE line-rate forwarding capability.
- An integrated ML inference accelerator enables anomaly detection and traffic classification at line rate without offloading to host CPU.
- OCTEON 10 targets three primary markets: hyperscale SmartNIC, 5G base station RAN acceleration, and enterprise network security appliances.
- Competes with NVIDIA BlueField-3 (Arm-based) and Intel Mount Evans IPU in the DPU market; differentiated by the RISC-V programmable offload engine.
- ML inference engine supports INT8 quantized models for network workloads, enabling throughput-efficient inference without full FP32 compute.

## Relationships

- [[risc_v_architecture]] — OCTEON 10 uses RISC-V cores for its programmable data-plane offload subsystem.
- [[infiniband_vs_ethernet_ai_clusters]] — OCTEON 10 targets Ethernet (400GbE) SmartNIC deployments relevant to AI cluster networking.
- [[high_performance_networking_ai_kubernetes]] — DPU-based network offload, including OCTEON 10, is used in AI cluster Kubernetes networking stacks.

## Sources

- Marvell OCTEON 10 product page: https://www.marvell.com/products/data-processing-units.html
- Marvell CN10K series product brief
- Hot Chips 2023 OCTEON 10 presentation
