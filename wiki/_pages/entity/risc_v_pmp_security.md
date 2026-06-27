---
type: entity
tags:
  - risc-v
  - security
  - hardware
  - memory-protection
  - isolation
  - privileged-spec
sources:
  - https://github.com/riscv/riscv-isa-manual
  - https://riscv.org/technical/specifications/
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.75
  claim_density: 0.80
  self_containedness: 0.90
  bridge_score: 0.65
  hub_potential: 0.55
---

# RISC-V Physical Memory Protection (PMP)

RISC-V Physical Memory Protection (PMP) is a hardware memory isolation mechanism defined in the RISC-V Privileged Architecture Specification that allows the machine-mode (M-mode) software — typically a security monitor or hypervisor — to restrict which physical memory regions are accessible by lower-privilege software running in supervisor-mode (S-mode) or user-mode (U-mode). PMP operates by checking every memory access against a set of configuration registers: up to 64 PMP entries (pmpcfg/pmpaddr register pairs), where each entry defines a physical address range and an access permission mask (Read, Write, Execute). When a PMP entry matches an access and denies permission, the processor raises a synchronous exception (access-fault), preventing the access. Unlike virtual memory (which requires an MMU and page tables), PMP is purely physical and operates without address translation, making it available even on cores without an MMU — critical for bare-metal security on embedded RISC-V MCUs. PMP is the foundation of RISC-V TEE implementations including Keystone Enclave, HexFive MultiZone, and RISC-V Trusted Firmware-M (TF-M), and is also used to implement isolation between RTOS tasks in safety-critical real-time systems without virtualization overhead.

## Key Claims

- RISC-V PMP supports up to 64 entries (16 mandatory minimum for non-trivial deployments; the base spec allows 0, 16, or 64), each covering a physical address range defined by an address register and one of three modes: TOR (Top-Of-Range), NA4 (Naturally Aligned 4-byte), or NAPOT (Naturally Aligned Power-Of-Two).
- PMP checks are performed in hardware on every memory access in S-mode and U-mode, with M-mode bypassing PMP by default unless the L (Lock) bit is set in the pmpcfg entry, which also makes the entry immutable until reset.
- PMP granularity is configurable per-implementation: the minimum grain size is 4 bytes (NA4 mode), but most implementations enforce a minimum of 4 KB (platform page size) due to hardware cost; the grain size is discoverable via the G field in mstatus.
- Lock bit (L) in PMP entries serves a dual purpose: it prevents M-mode software from modifying the entry (protecting security monitor isolation) and optionally applies PMP restrictions to M-mode accesses to the covered range.
- Zmpat (RISC-V Memory Attribute Table) extension proposal extends PMP with memory-type attributes (WB cacheable, IO, non-cacheable), addressing the limitation that base PMP only controls access permissions, not memory type.
- Trusted Firmware-M (TF-M) uses PMP to isolate Secure Partitions from each other and from the Non-Secure world on RISC-V M-profile chips (e.g., SiFive E series), providing PSA Certified Level 1/2 root of trust.
- The RISC-V PMP model is intentionally simpler than ARM's MPU but more flexible than ARM TrustZone's fixed two-world model, allowing up to 64 independently configurable isolation zones.

## Relationships

- [[keystone_enclave_riscv]] — Keystone TEE uses PMP as its primary isolation primitive; the security monitor configures PMP entries to protect enclave regions.
- [[risc_v_international_foundation]] — PMP is defined in the RISC-V Privileged Specification maintained by RISC-V International.
- [[lowrisc_opentitan]] — OpenTitan uses PMP on its Ibex RISC-V core to enforce isolation between firmware layers during secure boot.
- [[zephyr_rtos_tflite_micro]] — Zephyr RTOS uses RISC-V PMP for memory domain isolation between tasks in its kernel's memory protection subsystem.
- [[rvb23_embedded_profile]] — RVB23 mandates PMP support (minimum 16 entries) as part of the embedded security baseline.

## Sources

- RISC-V Privileged Architecture Specification (Volume II), Chapter 3 (PMP): https://github.com/riscv/riscv-isa-manual
- Keystone Enclave PMP usage: https://keystone-enclave.org/
- Trusted Firmware-M RISC-V platform port: https://tf-m-user-guide.trustedfirmware.org/
- RISC-V PMP analysis: "Security Analysis of RISC-V Physical Memory Protection," ISCA 2021 workshop
