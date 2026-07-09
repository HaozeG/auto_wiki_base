---
canonical_name: Blackhole QuietBox
aliases:
- TT-QuietBox
- QuietBox
- Blackhole QuietBox workstation
subtype: hardware_target
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/a8d0220dbddf9e79.md
- https://www.theregister.com/on-prem/2025/11/27/blackhole-quietbox-tenstorrents-ai-workstation-reviewed/2113269
source_url: https://www.theregister.com/on-prem/2025/11/27/blackhole-quietbox-tenstorrents-ai-workstation-reviewed/2113269
fetched_at: '2026-07-09T11:35:10.933640+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: tt-quietbox-2
  reason: TT-QuietBox 2 is the successor workstation to the Blackhole QuietBox, using
    a different host platform (Ryzen 9700X vs EPYC Siena) and lower launch price ($9,999
    vs $11,999) while sharing the same liquid-cooled four-Blackhole-chip design.
---

# Blackhole QuietBox

The Blackhole QuietBox (also known as TT-QuietBox or QuietBox) is a liquid-cooled AI workstation developed by Tenstorrent, designed as a development platform for the company's third-generation Blackhole accelerator architecture. Priced at $11,999, the system contains four Blackhole P150 accelerators, each liquid-cooled, providing a combined compute capacity of up to 2,656 TFLOPS FP8 (post-firmware revision). The workstation is built around an ASRock Rack EPYC server board powered by an AMD EPYC Siena 8124P CPU with 16 Zen4C cores clocked at up to 3 GHz, and 512 GB of DDR5-4800 memory across eight 64 GB RDIMMs, delivering approximately 200 GB/s of memory bandwidth. The massive cooling system uses two 400 mm radiators and four Noctua 200 mm fans in a chimney layout to dissipate over 1,300 watts of heat while keeping noise levels low enough for desktop use. The QuietBox serves as a cut-down version of the upcoming Galaxy Blackhole rack servers, sharing the same chips, memory, and interconnects to allow seamless scaling of code and models from a single workstation to a 32-chip cluster. Tenstorrent positions this machine as a low-cost entry point for developers targeting production deployment of the Blackhole ecosystem.

## Key Claims

- The Blackhole QuietBox costs $11,999 and includes four liquid-cooled Blackhole P150 accelerators.
- The system uses a custom chimney-style cooling case with two 400 mm radiators and four Noctua 200 mm fans.
- The workstation is based on an ASRock Rack EPYC server board with an AMD EPYC Siena 8124P CPU (16 Zen4C cores, 3 GHz boost).
- Memory configuration: 512 GB DDR5-4800 across eight 64 GB RDIMMs, providing over 200 GB/s bandwidth.
- The QuietBox is designed as a development platform for the Tenstorrent Blackhole architecture; software stack is described as immature for local AI enthusiasts.
- The system shares the same chips, memory, and interconnects as the Galaxy Blackhole rack servers, enabling code scaling.

## Relationships

- [[blackhole]] shares the Blackhole P150 accelerators as its compute resources; each QuietBox integrates four of the same chips used in the larger Galaxy rack system.

- [[tt-quietbox-2]]: TT-QuietBox 2 is the successor workstation to the Blackhole QuietBox, using a different host platform (Ryzen 9700X vs EPYC Siena) and lower launch price ($9,999 vs $11,999) while sharing the same liquid-cooled four-Blackhole-chip design.

## Sources

- https://www.theregister.com/on-prem/2025/11/27/blackhole-quietbox-tenstorrents-ai-workstation-reviewed/2113269
