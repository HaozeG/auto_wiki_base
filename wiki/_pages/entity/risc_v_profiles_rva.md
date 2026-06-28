---
cold_start: false
created: 2026-06-27
inbound_links: 7
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/
- https://github.com/riscv/riscv-profiles/blob/main/src/rva23-profile.adoc
- https://fprox.substack.com/p/risc-v-profiles
- https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
- https://www.cnx-software.com/2025/07/08/ubuntu-25-10-release-to-mandate-rva23-profile-obsoleting-most-risc-v-hardware/
tags:
- risc-v
- ISA
- standardization
- profiles
- RVA23
- software-portability
type: entity
updated: 2026-06-27
---

# RISC-V Application Profiles (RVA20 / RVA22 / RVA23)

RISC-V Application Profiles (RVA series) are standardized extension bundles ratified by RISC-V International that define the mandatory and optional ISA features a 64-bit RISC-V processor must implement to be binary-compatible with mainstream OS distributions and application software. Unlike ad hoc extension combinations, profiles allow software vendors to assume a stable, versioned feature floor. Three application profiles have been ratified: RVA20 and RVA22 (both ratified March 2023, version 1.0) and RVA23 (ratified October 2024, version 1.0); RVB23 (a base subset) was co-ratified with RVA23. The critical progression from RVA22 to RVA23 is that the RISC-V Vector (V) extension moved from optional to mandatory: RVA23U64 requires full RVV 1.0, making hardware vector acceleration a baseline expectation for any RVA23-compliant application processor. RVA23 also mandates hypervisor extensions (H), addressing enterprise virtualization. Ubuntu 25.10 announced it would mandate the RVA23 profile, effectively obsoleting most existing RISC-V hardware that lacks RVV. The profiles are essential for AI/ML software portability: code compiled for RVA23 can rely on RVV for vectorized inference kernels without runtime feature detection, enabling standard binary distributions to ship optimized AI libraries.

## Key Claims

- RVA20 and RVA22 ratified March 2023 (v1.0); RVA23 and RVB23 ratified October 2024 (v1.0).
- RVA23U64 makes V (RVV 1.0) mandatory — it was optional in RVA22U64; this is the key AI/ML inflection.
- RVA23 also mandates Hypervisor (H) extensions for enterprise virtualization support.
- Ubuntu 25.10 will require RVA23 profile compliance, obsoleting pre-RVV RISC-V hardware.
- Profiles exist only in 64-bit RV form; each version adds mandatory extensions and carries optional ones forward.
- Mandatory extensions can be assumed at compile time; optional extensions require runtime probing.

## Relationships

- [[risc_v_vector_extension]]: RVV 1.0 became mandatory in RVA23, elevating vector from optional to required across the RISC-V application ecosystem.
- [[risc_v_matrix_extension]]: Matrix extension is explicitly listed as a future target for RVA profiles but is not yet ratified into any profile.
- [[tenstorrent_tt_ascalon]]: TT-Ascalon is RVA23-compliant, meaning it includes mandatory RVV 1.0 and hypervisor support.
- [[ventana_veyron_v2]]: Veyron V2 is RVA23-compliant, targeting data-center deployments where software assumes RVA23.
- [[alibaba_xuantie_c950]]: C950 targets RVA23 plus proprietary matrix extensions beyond the profile.

## Sources

- https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/
- https://github.com/riscv/riscv-profiles/blob/main/src/rva23-profile.adoc
- https://fprox.substack.com/p/risc-v-profiles
- https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
- https://www.cnx-software.com/2025/07/08/ubuntu-25-10-release-to-mandate-rva23-profile-obsoleting-most-risc-v-hardware/
