---
canonical_name: Intel Xeon Sapphire Rapids
aliases:
- Sapphire Rapids
- Eagle Stream
- Intel Sapphire Rapids
- Intel Sapphire Rapids-SP
- Sapphire Rapids-SP
- SPR
- Xeon 4th Gen Scalable
- Xeon Max
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.2
sources:
- raw/cache/56a2a062f1d5570c.md
- https://www.overclockers.ua/news/hardware/2022-02-22/131074/
- raw/cache/63b4ff550b0b197a.md
- https://www.techbyte.it/hardware/intel-sapphire-rapids-sp-3-volte-piu-potente-rispetto-a-ice-lake/
- raw/cache/8cbb8896ccf30234.md
- https://en.wikipedia.org/wiki/Sapphire_Rapids
source_url: https://www.overclockers.ua/news/hardware/2022-02-22/131074/
fetched_at: '2026-07-17T12:47:51.538153+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: vistara
  reason: Vistara is a CXL bridge chip from Meta that enables reuse of DDR4 memory
    in DDR5-only servers, providing a lower-cost memory capacity tier compared to
    the native DDR5 memory used in Sapphire Rapids-based systems
---

# Intel Xeon Sapphire Rapids

Intel Xeon Sapphire Rapids is a server processor microarchitecture released in 2022 as part of the fourth-generation Intel Xeon Scalable family. It is built on the Intel 7 process and uses a multi-chip module (MCM) design with up to four separate dies, each containing 15 Golden Cove cores, for a total of up to 60 cores. Each die includes 28.125 MB of shared L3 cache, a dual-channel DDR5 memory controller, 32 PCI Express 5.0 lanes, and EMIB (Embedded Multi-die Interconnect Bridge) connections for die-to-die communication. The platform, codenamed Eagle Stream, uses the LGA4677 socket and supports up to eight memory channels and 128 PCIe 5.0 lanes at the package level. Retail samples are expected to have up to 56 cores with reduced L3 cache and PCIe lane counts.

## Key Claims

- Sapphire Rapids uses a multi-chip module with up to four individual dies manufactured on Intel 7.
- Each die contains 15 Golden Cove cores, 28.125 MB of L3 cache, a dual-channel DDR5 controller, and 32 PCIe 5.0 lanes.
- Physical maximum configuration is 60 cores, 112.5 MB L3 cache, eight-channel DDR5, and 128 PCIe 5.0 lanes.
- Retail samples may be limited to 56 cores with reduced L3 cache and PCIe lane count.
- Die-to-die connectivity is achieved via EMIB interconnects.
- The processor uses the LGA4677 (Eagle Stream) platform socket.

## Relationships

- [[vistara]]: Vistara is a CXL bridge chip from Meta that enables reuse of DDR4 memory in DDR5-only servers, providing a lower-cost memory capacity tier compared to the native DDR5 memory used in Sapphire Rapids-based systems.

## Sources

- [Изучаем строение кристаллов серверных процессоров Intel...](raw/cache/56a2a062f1d5570c.md)
