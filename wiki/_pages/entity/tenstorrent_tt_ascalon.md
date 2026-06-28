---
cold_start: true
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
- https://tenstorrent.com/en/newsroom/tenstorrent-announces-availability-of-tt-ascalon
- https://www.eetimes.com/tenstorrent-productizes-risc-v-cpu-and-ai-ip/
- https://pbxscience.com/tenstorrent-unveils-tt-ascalon-a-high-performance-risc-v-cpu-challenging-the-market/
tags:
- risc-v
- processor
- AI-acceleration
- out-of-order
- server
type: entity
updated: 2026-06-27
---

# Tenstorrent TT-Ascalon

The Tenstorrent TT-Ascalon is a high-performance RISC-V CPU core IP developed by Tenstorrent, the AI chip company led by Jim Keller, and made available as licensable silicon IP. The Ascalon-X is an 8-wide decode out-of-order superscalar design built by a team with backgrounds from Apple's M-series and AMD's Zen microprocessor projects, targeting server and AI workloads. It is fully compliant with the RVA23 RISC-V architecture profile and implements dual 256-bit RVV 1.0 vector units, making it one of the highest-performance general-purpose RISC-V cores available as commercial IP. Tenstorrent positions Ascalon as a CPU component within its broader Wormhole and Blackhole AI accelerator SoC ecosystem, enabling chiplet-based hybrid designs that combine RISC-V CPUs with dedicated matrix accelerators.

## Key Claims

- Ascalon achieves over 22 SPECint2006/GHz, over 2.3 SPECint2017/GHz, and over 3.6 SPECfp2017/GHz, placing it in direct competition with high-performance Arm Cortex-X series cores on per-clock throughput.
- The core operates at over 2.5 GHz on Samsung SF4X (4nm-class) process, with implementations spanning 10–20 SPECint2006/GHz depending on configuration.
- Ascalon-X features dual 256-bit vector data paths implementing RVV 1.0, enabling 512 bits of effective SIMD throughput per cycle and full RVA23 compliance.
- Tenstorrent's successor core, Babylon, is in advanced development with an 18-month release cadence, targeting a significant IPC improvement over Ascalon.
- At CES 2026, Tenstorrent demonstrated mixed CPU/accelerator/chiplet configurations using TT-Ascalon as the control CPU, illustrating its role in heterogeneous AI system-on-chip designs.

## Relationships

- [[risc_v_vector_extension]] — Ascalon implements RVA23 with dual 256-bit RVV 1.0 vector units
- [[ventana_veyron_v2]] — direct competitor as high-performance RISC-V server CPU IP

## Sources

- Tenstorrent availability announcement: https://tenstorrent.com/en/newsroom/tenstorrent-announces-availability-of-tt-ascalon
- EE Times productization coverage: https://www.eetimes.com/tenstorrent-productizes-risc-v-cpu-and-ai-ip/
- Performance benchmarks: https://pbxscience.com/tenstorrent-unveils-tt-ascalon-a-high-performance-risc-v-cpu-challenging-the-market/
