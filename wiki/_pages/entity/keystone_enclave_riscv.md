---
type: entity
tags:
  - risc-v
  - security
  - tee
  - trusted-execution
  - open-source
  - ml-inference
sources:
  - https://keystone-enclave.org/
  - https://github.com/keystone-enclave/keystone
  - https://arxiv.org/abs/1907.10119
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.82
  claim_density: 0.77
  self_containedness: 0.86
  bridge_score: 0.68
  hub_potential: 0.60
---

# Keystone Enclave (RISC-V TEE Framework)

Keystone Enclave is an open-source Trusted Execution Environment (TEE) framework for RISC-V processors, developed primarily at UC Berkeley and MIT. Unlike proprietary TEE solutions (ARM TrustZone, Intel SGX), Keystone is fully open-source and leverages RISC-V's native physical memory protection (PMP) primitives to isolate enclaves from the untrusted OS and other software without requiring hardware modifications beyond a standard RISC-V M-mode and S-mode implementation. The Keystone design separates the security monitor (running in M-mode, the most privileged RISC-V mode) from the enclave runtime (running in S-mode within a PMP-isolated region) and the untrusted OS (also S-mode but in a different PMP region), with communication via a well-defined shared-memory API. Keystone supports confidential computing use cases including secure ML inference: model weights and activations can be loaded into an enclave region, preventing the host OS and hypervisor from observing them. The framework has been demonstrated on real RISC-V hardware (SiFive HiFive Unleashed, CVA6 FPGA SoC) and provides a programming model compatible with POSIX-like applications through its edge call (ECALL/OCALL) abstraction. Keystone is the standard open-source TEE reference for RISC-V security research and has influenced the RISC-V Security HC working group's TEE architecture proposals.

## Key Claims

- Keystone implements TEE isolation entirely using RISC-V PMP (Physical Memory Protection) registers, requiring no custom hardware extensions — any RISC-V chip with ≥16 PMP entries can run Keystone.
- The security monitor (SM) runs in M-mode and is the only software with unrestricted physical memory access; it is verified using a microarchitecture-independent formal verification approach (ProVerif in academic work).
- Enclave isolation is enforced at cache-line granularity by configuring PMP to cover enclave physical memory pages, with PMP checks performed in hardware on every memory access at machine speed.
- Keystone provides a remote attestation protocol using an ED25519 root key provisioned in the SM, allowing a remote client to verify that a specific enclave binary is running on a legitimate Keystone platform.
- Secure ML inference with Keystone has been demonstrated with TFLite Micro models running inside enclaves on the SiFive HiFive Unleashed, with less than 15% overhead vs. unsecured execution for models that fit in DRAM.
- The Keystone SDK provides POSIX-compatible edge calls (ECALL into enclave, OCALL from enclave to host), with a provided libc subset enabling standard C/C++ ML runtime code to run inside enclaves with minimal porting effort.
- Keystone's design has been adopted as a baseline by multiple academic TEE projects including TIMBER-V (IBM), HexFive MultiZone (HexFive Security), and SANCTUM (MIT), illustrating its role as an architectural reference.

## Relationships

- [[risc_v_pmp_security]] — Keystone's isolation mechanism is built entirely on RISC-V PMP; understanding PMP is prerequisite to understanding Keystone's security model.
- [[lowrisc_opentitan]] — OpenTitan provides a complementary security approach (hardware root of trust for boot) while Keystone provides runtime enclave isolation; the two can be combined.
- [[cva6_ariane_riscv]] — CVA6 on FPGA is used as a Keystone prototype platform in several research papers demonstrating TEE on open-source RISC-V.
- [[tinyml_mcu_inference]] — Keystone-protected TFLite Micro inference is a target use case for confidential edge AI.

## Sources

- Keystone Enclave website: https://keystone-enclave.org/
- Keystone GitHub: https://github.com/keystone-enclave/keystone
- Lee et al., "Keystone: An Open Framework for Architecting TEEs," EuroSys 2020: https://arxiv.org/abs/1907.10119
- Keystone SDK documentation: https://docs.keystone-enclave.org/
