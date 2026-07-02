---
canonical_name: PULP Platform
aliases:
- Parallel Ultra-Low-Power Platform
- PULP
- PULP Project
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.8
sources:
- raw/cache/589a5c4a2ff7e749.md
- https://arxiv.org/html/2412.20391v1
source_url: https://arxiv.org/html/2412.20391v1
fetched_at: '2026-07-02T04:54:34.051340+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# PULP Platform

The PULP (Parallel Ultra-Low-Power) Platform is an open-source hardware ecosystem initiated by the University of Bologna and ETH Zürich in 2013, focused on the design of heterogeneous system-on-chips (SoCs) for energy-efficient AI acceleration. The platform provides a comprehensive portfolio of processor cores, network-on-chips, peripherals, SoC templates, and hardware accelerators, all released as open-source intellectual property. The core computing block, known as a PULP cluster, consists of a multi-banked Tightly-Coupled Data Memory (TCDM) typically ranging from 64 to 256 KiB, multiple 32-bit RISC-V processors with optional instruction set architecture extensions for digital signal processing and AI, and one or more Hardware Processing Engines (HWPEs) connected via a Heterogeneous Cluster Interconnect (HCI). The HCI comprises a logarithmic crossbar for fair core and DMA access to 32-bit memory banks and a wide router for HWPE memory accesses up to 512 bits. The architecture operates at low voltage and low frequency to maximize energy efficiency, compensating for lower clock speeds through parallelism and hardware acceleration.

## Key Claims

- The open-source model reduces non-recurrent engineering costs by leveraging shared IP for non-differentiating SoC components.
- The PULP cluster architecture combines a multi-banked TCDM, RISC-V processors with ISA extensions, and HWPEs via an HCI.
- HWPEs time-share a wide memory port (N×32-bit) to access multiple TCDM banks simultaneously.
- The HCI has two branches: a logarithmic crossbar for core and DMA access, and a wide router for HWPE memory accesses.
- The platform targets low-voltage, low-frequency operation, achieving energy efficiency through architectural parallelism and hardware acceleration.

## Relationships

- The K230 SoC ([[k230]]) integrates dual RISC-V cores and dedicated AI accelerators, representing a commercial implementation of a heterogeneous AI acceleration approach similar in spirit to PULP clusters.
- The XuanTie C908 core ([[xuantie_c908]]) exemplifies a RISC-V processor with vector extensions that could be integrated into a PULP cluster as a programmable element.
- The optimization recipe for MLIR+xDSL RVV code generation ([[mlir_xdsl_rvv_gemm_codegen_recipe]]) targets RISC-V platforms with vector support, relevant for programming PULP clusters equipped with such cores.
- Insufficient context for additional cross-links to entity pages within the current wiki context.

## Sources

- https://arxiv.org/html/2412.20391v1
