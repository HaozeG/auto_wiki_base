---
cold_start: true
created: 2026-06-26
inbound_links: 3
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- raw/sources/riscv_ai_native_platform.md
- raw/sources/sifive_intelligence_x280_2ndgen.md
tags:
- risc-v
- isa-profile
- standardization
- ai-acceleration
type: entity
updated: 2026-06-26
------

# RVA23 Profile

The RVA23 profile is a RISC-V International standardization artifact that bundles a mandatory set of RISC-V extensions into a single, guaranteed feature level, enabling software vendors to compile and distribute binaries that target all compliant hardware without per-chip tuning. Ratified in late 2024, RVA23 mandates the RISC-V Vector Extension v1.0 (RVV 1.0) alongside a defined set of scalar, memory, and privilege-mode extensions. Its significance for AI workloads is that it establishes a universal ABI for vectorized computation, allowing frameworks like PyTorch, TensorFlow Lite, and llama.cpp to ship optimized code paths that run on any RVA23 hardware. NVIDIA, Canonical (Ubuntu), and Red Hat have all publicly committed to RVA23 support, marking a major ecosystem alignment event in the RISC-V AI space.

## Key Claims

- RVA23 mandates RVV 1.0, making 512-bit-minimum vector capability a guaranteed feature rather than an optional extension on compliant implementations.
- NVIDIA announced a port of its CUDA AI acceleration stack to RVA23, the first major GPU-software-stack vendor to commit to a RISC-V profile.
- Canonical Ubuntu 25.10 and 26.04 are targeting RVA23 as a baseline; Red Hat Enterprise Linux 10 ships in developer preview on an RVA23-capable board (SiFive HiFive Premier P550).
- Hardware deployments meeting RVA23 are expected in 2026; RVA23-compatible developer boards are planned for 2026.
- SiFive's 2nd Gen Intelligence family (X280 Gen 2, X390 Gen 2, XM Gen 2) adds RVA23 compliance and FP4/FP8 datatypes; first silicon Q2 2026.
- The profile system enforces "zero-day bring-up": Linux kernel, compilers, and runtime libraries support new AI features immediately at silicon delivery because the feature set is standardized in advance.

## Relationships

- [[risc_v_vector_extension]]: RVV 1.0 is the most AI-relevant mandatory component of RVA23.
- [[sifive_intelligence_x280]]: SiFive's 2nd Gen family is an early implementer of RVA23 compliance.
- [[riscv_ai_ecosystem]]: RVA23 is the primary mechanism driving software ecosystem convergence for RISC-V AI.
- [[risc_v_matrix_extensions]]: Matrix extensions (IME, VME, AME) are candidates for future profile versions beyond RVA23.

## Sources

- riscv_ai_native_platform.md: RVA23 ratification date, NVIDIA CUDA commitment, Canonical/Red Hat support, zero-day bring-up concept, 2026 hardware timeline.
- sifive_intelligence_x280_2ndgen.md: SiFive 2nd Gen RVA23 compliance details, Q2 2026 silicon date.
