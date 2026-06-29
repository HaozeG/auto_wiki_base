---
cold_start: false
constraints:
- Requires kernel source access
- Requires device tree modification
created: '2023-12-31'
datatypes: []
evidence_strength: reported
hardware_targets:
- C910 (TH1520) on Lichee Module 4A
inbound_links: 0
metrics:
- SPEC score
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 1.0
  self_containedness: 1.0
sources:
- https://blog.cyyself.name/t-head-c910-spec-cpu-performance/
tags:
- C910
- Lichee Module 4A
- overclocking
- device tree
toolchains:
- gcc-13.2.1
- Xuantie-900-gcc-V2.8.0-20231018
type: optimization_recipe
updated: '2026-06-28'
workloads:
- SPEC CPU 2006 INT
- SPEC CPU 2017 INT Rate
---

# C910 2GHz Enablement

The C910 2GHz Enablement is a device tree patch that increases the maximum operating frequency of the T-HEAD C910 core on the Lichee Module 4A from 1.85 GHz to 2.0 GHz. The patch modifies the CPU operating points in the devicetree source file `arch/riscv/boot/dts/thead/th1520-lichee-module-4a.dtsi`. The expected effect is improved benchmark performance, as demonstrated by SPEC CPU 2006 and 2017 results. Failure modes are not documented in the source. The measurements show a geometric mean improvement of approximately 5.4% for SPEC CPU 2006 INT with mainline GCC.

## Key Claims

- Applying the patch increases the CPU frequency from 1.85 GHz to 2.0 GHz.
- SPEC CPU 2006 INT GEOMEAN improves from 7.59 (1.85 GHz, mainline GCC) to 8.03 (2 GHz, mainline GCC), a 5.8% gain.
- SPEC CPU 2006 INT GEOMEAN with Xuantie GCC improves from 8.46 (2 GHz) compared to 7.59 (1.85 GHz, mainline) — a mixed comparison but shows overall higher scores at 2 GHz.
- The patch is a simple one-line change to the `light,dvddm-operating-points` table.

## Transformation

- Prerequisites: Access to the kernel source tree for the TH1520-based Lichee Module 4A, ability to rebuild and flash the kernel.
- Steps: Apply the provided diff to `th1520-lichee-module-4a.dtsi`, which changes the highest operating point from 1848000 kHz to 2000000 kHz at 1000000 uV. Rebuild the kernel and boot.
- Expected effect: CPU clock frequency increases from 1.85 GHz to 2.0 GHz, resulting in higher benchmark scores as shown in the SPEC tables.
- Failure modes: Not documented; possible thermal or stability issues not discussed.
- Measurements: SPEC CPU 2006 INT GEOMEAN: 1.85 GHz = 7.59, 2 GHz = 8.03 (mainline GCC). Individual benchmark scores also show increases.

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – The benchmark results that validate this optimization.
- [[Sipeed_MAIX_series]] – A different RISC-V board for context.

## Sources

- [T-HEAD C910 SPEC CPU Benchmark blog post](https://blog.cyyself.name/t-head-c910-spec-cpu-performance/)
