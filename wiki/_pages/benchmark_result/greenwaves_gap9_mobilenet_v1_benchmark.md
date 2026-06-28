---
cold_start: false
created: '2026-06-28'
datatypes:
- INT8
- INT4
- INT2
evidence_strength: reported
hardware_targets:
- greenwaves_gap9
hardware_versions:
- GreenWaves GAP9 22nm FD-SOI
inbound_links: 0
measurement_method: Reported by GreenWaves; independent verification not stated.
metrics:
- power (mW)
- latency (ms)
- GOPS
- GOPS/W
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions: []
sources:
- https://www.jonpeddie.com/news/greenwaves-gap9-ships-ai-in-earbuds-at-50-mw/
tags:
- greenwaves
- gap9
- mobilenet-v1
- ultra-low-power
- benchmark
toolchains:
- gapflow
type: benchmark_result
updated: '2026-06-28'
workloads:
- MobileNet V1
---

# GreenWaves GAP9 MobileNet V1 Benchmark

The GreenWaves GAP9 processor, fabricated on GlobalFoundries 22nm FD-SOI, runs MobileNet V1 at 160×160 resolution with 0.25 channel scaling in 12 ms at 806 µW per frame. This benchmark demonstrates the processor's capability for always-on computer vision in battery-powered devices. The measurement context is reported by GreenWaves Technologies and cited by Jon Peddie Research. The GAP9 delivers 50 GOPS at 50 mW total power consumption, with a peak cluster memory bandwidth of 41.6 GB/s. These figures indicate strong energy efficiency for AI inference at the extreme edge.

## Key Claims

- MobileNet V1 at 160×160 resolution with 0.25× channel scaling: 12 ms inference latency at 806 µW per frame.
- Overall processor performance: 50 GOPS at 50 mW power consumption.
- Peak cluster memory bandwidth: 41.6 GB/s.
- Supports INT2, INT4, and INT8 precisions on the NE16 hardware engine.

## Measurement Context

- Hardware version: GreenWaves GAP9 on GlobalFoundries 22nm FD-SOI.
- Software/toolchain version: GAPFlow (model conversion) and AutoTiler (code generation); specific versions not cited.
- Workload shape: MobileNet V1, resolution 160×160, channel scaling 0.25.
- Metric: Latency (12 ms), power (806 µW per frame), total power at peak (50 mW at 50 GOPS).
- Method: Reported by GreenWaves; no independent third-party verification confirmed.
- Evidence strength: reported.

## Relationships

- [[greenwaves_gap9]] — Main entity page for the GAP9 processor.
- [[greenwaves_gap9_hardware]] — Detailed hardware target description.
- [[risc_v_vector_extension]] — Alternative vector-based approach for inference; GAP9 uses dedicated HW engine for these benchmarks.

## Sources

- "GreenWaves GAP9 ships AI in earbuds at 50 mW" — Jon Peddie Research, June 15, 2026. https://www.jonpeddie.com/news/greenwaves-gap9-ships-ai-in-earbuds-at-50-mw/
