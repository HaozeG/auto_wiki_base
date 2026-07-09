---
canonical_name: Xuantie C910
aliases:
- C910
- T-HEAD C910
- Xuantie C910
- TH1520 C910
- XuanTie C910
- XT C910
subtype: null
tags: []
scorecard:
  novelty_delta: 0.82
  claim_density: 0.85
  self_containedness: 0.78
  bridge_score: 0.55
  hub_potential: 0.25
sources:
- raw/cache/2e598f9094e9c252.md
- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
- raw/cache/dd944bc005e8fc47.md
- https://arxiv.org/html/2505.24363v1
source_url: https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
fetched_at: '2026-07-09T07:55:50.027455+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara
  reason: 'Both the Xuantie C910 and the Ara vector unit implement the RISC-V Vector
    Extension, though C910 uses the draft 0.7.1 version while Ara uses the ratified
    1.0 specification. Ara is a coprocessor for the CVA6 scalar core, whereas C910
    is a full out-of-order core with integrated vector support. The two designs represent
    different approaches to RISC-V vector acceleration: a commercial integrated core
    versus an academic open-source coprocessor'
---

# Xuantie C910

The Xuantie C910 is a 3-wide out-of-order RISC-V processor core designed by T-HEAD, a wholly owned subsidiary of Alibaba. It is T-HEAD's first-generation out-of-order core and targets high-performance applications such as AI inference, edge servers, industrial control, and ADAS. The C910 implements the RISC-V Vector Extension version 0.7.1 (RVV 0.7.1), an early draft that includes masking and variable vector length support. The core is fabricated on TSMC's 12nm FinFET process, with a target frequency range of 2 to 2.5 GHz at 0.8–1.0 V, and occupies 0.8 mm² per core. On TSMC's 7nm process, T-HEAD achieved 2.8 GHz. Dynamic power is claimed at approximately 100 microwatts per MHz, yielding about 0.2 W at 2 GHz (excluding static and off-core power). The C910 is organized in clusters of up to four cores sharing a 1 MB L2 cache and is commercially available in the TH1520 SoC, used in the LicheePi single-board computer running at 1.85 GHz.

## Key Claims

- Xuantie C910 is a 3-wide out-of-order RISC-V core with a 12-stage pipeline.
- It supports the RISC-V Vector Extension version 0.7.1.
- Fabricated on TSMC's 12nm FinFET process; target frequency 2–2.5 GHz (2.8 GHz on 7nm).
- Core area: 0.8 mm² on 12nm.
- Dynamic power: ~100 μW/MHz, approximately 0.2 W at 2 GHz.
- L1i cache: 64 KB, 2-way set-associative with FIFO replacement, plus 83.7 KB of total raw bit storage including predecode data.
- Branch predictor: bi-mode predictor with 1024-entry selector, two 16384-entry history tables, 22-bit global history register, 12-entry return address stack, 256-entry indirect target buffer.
- L0 BTB: 16-entry fully associative; taken branches have effectively single-cycle latency.
- TH1520 SoC includes a quad-core C910 cluster at 1.85 GHz with 1 MB L2 cache and 8 GB LPDDR4X-3733.
- The RTL source code has been open-sourced by T-HEAD.

## Relationships

- [[ara]]: Both the Xuantie C910 and the Ara vector unit implement the RISC-V Vector Extension, though C910 uses the draft 0.7.1 version while Ara uses the ratified 1.0 specification. Ara is a coprocessor for the CVA6 scalar core, whereas C910 is a full out-of-order core with integrated vector support. The two designs represent different approaches to RISC-V vector acceleration: a commercial integrated core versus an academic open-source coprocessor.

## Sources

- [Alibaba/T-HEAD's Xuantie C910 - Chips and Cheese](raw/cache/2e598f9094e9c252.md)
