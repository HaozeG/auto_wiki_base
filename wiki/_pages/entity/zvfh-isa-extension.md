---
canonical_name: ZVFH
aliases:
- Zvfh
- RISC-V ZVFH
- Vector FP16 extension
subtype: null
tags:
- RISC-V
- ISA extension
- FP16
- vector
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.3
sources:
- raw/cache/11f47272348acbe8.md
- https://gcc.gnu.org/pipermail/gcc-patches/2023-May/620174.html
source_url: https://gcc.gnu.org/pipermail/gcc-patches/2023-May/620174.html
fetched_at: '2026-07-06T02:02:48.082208+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-x60-hardware-target
  reason: ZVFH is a required extension in the SpacemiT X60's RVA22 extension string
    (rv64imafdcv_zba_...zfh_zvfh...), enabling FP16 vector operations on that core
---

# ZVFH

ZVFH is a RISC-V vector extension for half-precision floating-point (FP16) operations, ratified as part of the RISC-V Vector Extension specification. It enables 16-bit floating-point arithmetic and data movement within the vector unit, complementing the scalar half-precision extension Zfhmin and the single-precision vector extension Zve32f. In GCC, ZVFH was added as a sub-extension to the -march= option in May 2023 by a patch from Intel, defining the MASK_ZVFH flag and TARGET_ZVFH macro, along with implied dependencies on Zve32f and Zfhmin. The underlying FP16 RVV intrinsic API depends on TARGET_ZVFH. The extension is specified in the RISC-V vector specification document.

## Key Claims

- ZVFH is a RISC-V vector extension for half-precision floating-point (FP16).
- It depends on the Zve32f and Zfhmin extensions.
- GCC support for ZVFH was added in May 2023 via a patch from Intel (Pan Li).
- The GCC patch defined MASK_ZVFH and TARGET_ZVFH and added implicit dependency rules in riscv_implied_info.
- FP16 RVV intrinsics require TARGET_ZVFH to be enabled.
- The extension is documented in the RISC-V vector specification (section 18.5: ZVFH).

## Relationships

- [[spacemit-x60-hardware-target]]: ZVFH is a required extension in the SpacemiT X60's RVA22 extension string (rv64imafdcv_zba_...zfh_zvfh...), enabling FP16 vector operations on that core.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2023-May/620174.html
- https://github.com/riscv/riscv-v-spec/blob/master/v-spec.adoc#185-zvfh-vector-extension-for-half-precision-floating-point
