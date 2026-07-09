---
canonical_name: Ara2
aliases:
- Ara2 vector processor
- Ara2 RVV 1.0 processor
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/6f93a3aa5b4558fd.md
- https://arxiv.org/html/2311.07493v2
- raw/cache/e96e952d676411c2.md
- https://bohrium.dp.tech/paper/arxiv/2311.07493
source_url: https://arxiv.org/html/2311.07493v2
fetched_at: '2026-07-09T02:20:40.118805+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 4
outbound_links:
- target: sifive-intelligence-x280
  reason: Both Ara2 and the SiFive Intelligence X280 implement the RISC-V Vector extension
    version 1.0. Ara2 is fully open-source, whereas X280 is a commercial processor
    with additional custom Intelligence Extensions for AI/ML workloads
---

# Ara2

Ara2 is the first fully open-source vector processor to implement the RISC-V Vector (RVV) extension version 1.0 frozen ISA. Developed by ETH Zurich and Huawei Zurich Research Center, Ara2 is designed for data-parallel workloads and achieves an average functional-unit utilization of 95% on computationally intensive kernels. It is implemented in a 22nm technology and reaches a clock frequency of 1.35 GHz with a state-of-the-art energy efficiency of 37.8 DP-GFLOPS/W at 0.8V. The processor is configurable with 2 to 16 lanes and supports both single-core and multi-core configurations. In multi-core setups, a cluster of eight 2-lane Ara2 cores (16 FPUs) outperforms a single 16-lane core by over 3× for a 32×32×32 matrix multiplication while improving energy efficiency by 1.5×. Ara2 is distinct from commercial RVV 1.0 implementations such as the SiFive Intelligence X280, offering a fully open-source alternative for research and prototyping.

## Key Claims

- First fully open-source vector processor to support the RISC-V V 1.0 frozen ISA.
- Achieves average functional-unit utilization of 95% on computationally intensive data-parallel kernels.
- Implemented in 22nm technology, reaching 1.35 GHz clock frequency with a critical path of approximately 40 FO4 gates.
- Energy efficiency of 37.8 DP-GFLOPS/W at 0.8V.
- Configurable vector unit with 2 to 16 lanes.
- Multi-core vector clusters address scalar core issue-rate bottlenecks for short-vector workloads: an 8-core 2-lane Ara2 cluster delivers over 3× performance improvement over a single 16-lane core on a 32×32×32 matrix multiplication, with 1.5× better energy efficiency.
- Open-source design enables detailed microarchitectural analysis and PPA characterization across configurations.

## Relationships

- [[sifive-intelligence-x280]]: Both Ara2 and the SiFive Intelligence X280 implement the RISC-V Vector extension version 1.0. Ara2 is fully open-source, whereas X280 is a commercial processor with additional custom Intelligence Extensions for AI/ML workloads.

## Sources

- [Ara2: Exploring Single- and Multi-Core Vector Processing with an Efficient RVV 1.0 Compliant Open-Source Processor](raw/cache/6f93a3aa5b4558fd.md)
