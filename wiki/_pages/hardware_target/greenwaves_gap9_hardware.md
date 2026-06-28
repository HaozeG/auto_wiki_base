---
cold_start: true
constraints:
- maximum_power_50mW
- 22nm_FD_SOI
- battery_powered_operation
created: '2026-06-28'
hardware_targets:
- greenwaves_gap9
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.jonpeddie.com/news/greenwaves-gap9-ships-ai-in-earbuds-at-50-mw/
tags:
- risc-v
- greenwaves
- pulp
- ne16
- ultra-low-power
toolchains:
- greenwaves_gap_sdk
- gaptiler_autotiler
- gapflow
type: hardware_target
updated: '2026-06-28'
---

# GreenWaves GAP9 Hardware Target

The GreenWaves GAP9 is an ultra-low-power AI inference processor designed for battery-powered edge devices. It combines a cluster of nine RISC-V cores based on the PULP (Parallel Ultra-Low-Power) open-source platform with a dedicated NE16 hardware neural network engine. Fabricated on GlobalFoundries 22nm FD-SOI, it delivers 50 GOPS at 50 mW with 41.6 GB/s peak cluster memory bandwidth. The architecture supports transprecision from INT2 through INT8 for the neural engine and from 2-bit integers to 32-bit floats on the general-purpose cores. Compiler support includes the GreenWaves GAP SDK, AutoTiler for automatic code generation, and GAPFlow for converting TensorFlow models into deployable inference code.

## Key Claims

- Hybrid architecture: fabric controller for orchestration, nine RISC-V parallel cluster cores for flexible workloads, and NE16 hardware engine for dedicated matrix multiply operations (convolution, normalization, activation, pooling).
- Transprecision support: NE16 operates at INT2, INT4, and INT8; RISC-V cores include transprecision floating-point units from 2-bit to 32-bit.
- 41.6 GB/s peak cluster memory bandwidth enables inference on neural networks 10× larger than GAP8 at equivalent power.
- Peripherals: bi-directional multi-channel digital audio, CSI-2 and parallel camera interfaces, multi-channel I²S for wearable audio.
- Security: AES-128/256 hardware cryptography and physically unclonable function (PUF).
- Software toolchain: GAP SDK, AutoTiler for automatic neural network graph code generation, GAPFlow for training framework model conversion.

## Optimization-Relevant Details

- ISA/profile: RISC-V custom PULP extensions; no standard RVV support — uses cluster-based parallel cores with dedicated NE16 engine.
- Vector/matrix/accelerator support: NE16 hardware neural engine for matrix multiplication; transprecision floating-point units on RISC-V cores for vectorized operations.
- Memory/cache/TLB/DMA: Shared cluster memory with banked architecture; peak 41.6 GB/s bandwidth; fabric controller for system orchestration.
- Compiler/toolchain support: GreenWaves proprietary SDK; AutoTiler for automated mapping of neural network graphs; GAPFlow for TensorFlow model deployment.

## Relationships

- [[greenwaves_gap9]] — Main entity page for the GAP9 processor.
- [[gemmini]] — Alternative RISC-V-based AI acceleration using systolic arrays, contrasting with GAP9's hybrid cluster+NE16 approach.
- [[risc_v_vector_extension]] — General-purpose vector extension; GAP9 uses a custom approach instead of standard RVV.

## Sources

- "GreenWaves GAP9 ships AI in earbuds at 50 mW" — Jon Peddie Research, June 15, 2026. https://www.jonpeddie.com/news/greenwaves-gap9-ships-ai-in-earbuds-at-50-mw/
