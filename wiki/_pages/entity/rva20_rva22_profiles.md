---
type: entity
tags:
  - risc-v
  - profiles
  - standards
  - linux
  - application-class
sources:
  - https://github.com/riscv/riscv-profiles
  - https://riscv.org/technical/specifications/
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.70
  claim_density: 0.76
  self_containedness: 0.85
  bridge_score: 0.60
  hub_potential: 0.55
---

# RISC-V RVA20 and RVA22 Application Profiles

The RISC-V Application profiles RVA20 and RVA22 are ratified RISC-V International specifications defining mandatory and recommended extension sets for 64-bit Linux-capable RISC-V processors. Profiles were introduced to solve a fragmentation problem: without a defined baseline, RISC-V software developers could not assume which extensions are present on a given chip, forcing per-platform feature detection for even common operations. RVA20U64 (User-mode, 64-bit) was the first ratified profile (2021), mandating RV64IMAFDC plus Zicsr, Zicntr, and Zifencei — the minimum needed to run a standard Linux ABI. RVA22U64 (ratified 2022) raised the mandatory baseline to include Zba/Zbb/Zbs (bit manipulation), Zfhmin (half-precision float minimum), and Zkt (data-independent execution latency), reflecting the extensions that Linux distributions and compilers had begun assuming. The profile system separates "mandatory" (must implement), "localization" (optional but RISC-V International recommended), and "development" (may be added in future ratification) tiers, giving SoC vendors a clear compliance target while retaining extensibility. RVA20 and RVA22 collectively established the first stable binary compatibility baseline for the RISC-V Linux ecosystem, enabling distributions such as Fedora, Ubuntu, and Alpine Linux to ship RISC-V packages targeting a defined ISA floor.

## Key Claims

- RVA20U64 mandates RV64IMAFDC + Zicsr + Zicntr + Zifencei as the minimum Linux-capable RISC-V 64-bit profile, ratified by RISC-V International in 2021.
- RVA22U64 adds mandatory Zba, Zbb, Zbs (bitmanip), Zfhmin (FP16 minimum), Zkt (constant-time execution), Sscofpmf (performance counter overflow), and Sstvecd (vectored trap) over RVA20.
- RVA22S64 (supervisor-mode variant) additionally mandates Sv39 virtual memory, Svpbmt (page-based memory types), and Svinval (cache invalidation fence), enabling full OS page-table management.
- Profile compliance is binary: a chip either implements all mandatory extensions for a profile or it does not claim compliance; optional extensions from the profile can be added without affecting the compliance claim.
- Linux distributions (Fedora 38+, Ubuntu 24.04+) adopted RVA22 as the minimum hardware target for general-purpose RISC-V packages, retiring RV64GC-only builds.
- The GNU toolchain (GCC 13+, Clang 17+) supports `-march=rv64gc_zba_zbb_zbs` and named profile targets, enabling profile-optimized code generation for RVA22 without per-extension flags.
- RVA22 is superseded by RVA23 (ratified 2024), which adds mandatory RVV 1.0 vector, Svnapot, and Zicbom among others, reflecting the growing importance of vector/AI workloads in the Linux RISC-V ecosystem.

## Relationships

- [[rva23_profile]] — RVA23 is the successor profile to RVA22, adding mandatory RVV 1.0 and additional system extensions.
- [[risc_v_international_foundation]] — Both RVA20 and RVA22 are ratified and maintained by RISC-V International through its profile working group.
- [[rvb23_embedded_profile]] — RVB23 is a parallel profile for embedded/RTOS targets, defined alongside the RVA application series.
- [[risc_v_vector_extension]] — RVA22 does not mandate RVV; adding mandatory RVV was a key motivation for the RVA23 revision.

## Sources

- RISC-V profiles repository: https://github.com/riscv/riscv-profiles
- RVA20 specification: https://github.com/riscv/riscv-profiles/blob/main/profiles.adoc
- Fedora RISC-V minimum ISA announcement (F38 release notes)
- GCC RISC-V profile support: GCC 13 release notes
