---
cold_start: true
created: '2026-06-28'
inbound_links: 3
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
- ai-accelerator
- ultra-low-power
- greenwaves
- pulp
type: entity
updated: '2026-06-28'
---

# GreenWaves GAP9

GreenWaves GAP9 is an ultra-low-power AI inference processor developed by GreenWaves Technologies, a fabless semiconductor company based in Grenoble, France. It combines a cluster of nine RISC-V cores with a dedicated NE16 hardware neural network engine, fabricated on GlobalFoundries 22nm FD-SOI process. The GAP9 delivers 50 GOPS at 50 mW power consumption with 41.6 GB/s peak cluster memory bandwidth, enabling AI inference on battery-powered devices such as tier 1 true wireless stereo (TWS) earbuds. Its architecture builds on the open-source PULP (Parallel Ultra-Low-Power) platform from ETH Zurich and the University of Bologna, and supports transprecision from 2-bit integers to 32-bit floating point. The processor has seen commercial adoption for neural noise cancellation and adaptive transparency in hearables, and has passed qualification cycles with multiple tier 1 customers.

## Key Claims

- Delivers 50 GOPS at 50 mW total power consumption, with 41.6 GB/s peak cluster memory bandwidth, a 20× improvement over the previous generation GAP8.
- Runs MobileNet V1 at 160×160 resolution with 0.25 channel scaling in 12 ms at 806 µW per frame.
- Hybrid architecture: RISC-V cores orchestrate data and manage layer transitions while the NE16 engine performs dedicated hardware matrix multiply operations for convolution, batch normalization, activation, and pooling without software intervention.
- Fabricated on GlobalFoundries 22nm FD-SOI process, providing dynamic voltage scaling advantages at sub-threshold operation for always-on IoT sensing.
- Security features include AES-128/256 hardware cryptography and a physically unclonable function (PUF) for per-device identification.
- Tier 1 hearables vendors use GAP9 for neural network-based noise filtering and adaptive transparency in production devices.
- Software stack includes GAP SDK, AutoTiler automatic code generator, and GAPFlow for converting TensorFlow models into deployable inference code.
- GreenWaves raised approximately $33.3 million across two rounds, including a €20M Series B in February 2023, with backing from Definvest Fund (managed by Bpifrance for the French Armed Forces Ministry).

## Relationships

- [[risc_v_vector_extension]] — The GAP9 RISC-V cores use the PULP ISA extensions, complementing general-purpose vector processing with a dedicated hardware neural engine for efficient AI inference.
- [[gemmini]] — Both Gemmini and GAP9 offer RISC-V-based AI acceleration; Gemmini uses a systolic array approach while GAP9 uses a hybrid RISC-V cluster with NE16 engine.
- [[tvm_riscv_backend]] — TVM targets RISC-V cores with RVV support; GAP9 uses a custom SDK (GAP SDK, AutoTiler, GAPFlow) for model deployment, representing an alternative compiler approach for RISC-V AI inference.

## Sources

- "GreenWaves GAP9 ships AI in earbuds at 50 mW" — Jon Peddie Research, June 15, 2026. https://www.jonpeddie.com/news/greenwaves-gap9-ships-ai-in-earbuds-at-50-mw/
