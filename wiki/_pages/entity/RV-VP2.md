---
cold_start: true
created: '2025-01-28'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://link.springer.com/chapter/10.1007/978-3-031-78380-7_5
- https://github.com/riscv/riscv-p-spec
- https://github.com/TUD-ADS/RV-VP2
tags:
- RISC-V
- Packed-SIMD
- P-extension
- Virtual Prototype
- SystemC
- TLM
- simulation
type: entity
updated: '2026-06-29'
---

# RV-VP²

RV-VP² is an open-source extension of a SystemC Transaction-Level Modeling (TLM)-based RISC-V Virtual Prototype (VP) that adds support for the RISC-V Packed-SIMD (P) Extension Version 0.9.11-draft-20211209. It is the first publicly available open-source VP extension implementing this draft specification, enabling early software development, performance modeling, and design-space exploration for P-extension instructions on embedded processing workloads. The simulator supports evaluation of workloads such as matrix multiplication, convolution, max-pooling, and fully connected layers, and compares performance against the base RISC-V ISA to demonstrate the efficiency gains achievable through packed-SIMD operations.

## Key Claims

- First open-source RISC-V VP extension to support the P-extension (Version 0.9.11-draft-20211209).
- Built on SystemC TLM-based RISC-V VP framework.
- Demonstrated on four test cases: matrix multiplication, convolution, max-pooling, fully connected layer.
- Shows efficiency improvement of P-extension over base ISA for embedded processing.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – Both are RISC-V acceleration approaches; Gemmini is a hardware accelerator, while RV-VP² provides simulation infrastructure for packed-SIMD.
- [[FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe]] – An optimization recipe using custom ISA extensions on FPGA; RV-VP² simulates the standard P-extension for comparison.

## Sources

- [Springer Chapter: RV-VP²: Unlocking the Potential of RISC-V Packed-SIMD for Embedded Processing](https://link.springer.com/chapter/10.1007/978-3-031-78380-7_5)
- [RISC-V P-Spec GitHub Repository](https://github.com/riscv/riscv-p-spec)
- [RV-VP² GitHub Repository](https://github.com/TUD-ADS/RV-VP2)

