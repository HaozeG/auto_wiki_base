---
canonical_name: nexus-am
aliases:
- Nexus Abstract Machine
- AM (XiangShan fork)
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/081e54846e46688e.md
- https://github.com/OpenXiangShan/nexus-am
source_url: https://github.com/OpenXiangShan/nexus-am
fetched_at: '2026-07-09T03:07:27.895458+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
---

# nexus-am

Nexus-am is a fork of the Abstract Machine (AM) bare-metal test framework adapted for the OpenXiangShan processor development, hosted on GitHub at OpenXiangShan/nexus-am. It provides a build system for creating memory images (binary files at base address 0x80000000) that can be loaded into RTL simulations of the XiangShan processor, using the DiffTest RTL-simulation framework. The repository includes workloads such as CoreMark (located in apps/coremark) that can be built by setting the ARCH to riscv64-xs. It also supports building bootrom flash images at base address 0x10000000 for designs with a read-only bootrom, using a separate architecture target riscv64-xs-flash. The project includes shared libraries (klib) and test programs, and is maintained under the OpenXiangShan organization alongside the XiangShan processor design. The environment variable AM_HOME must be set to the repository root for the build system to function.

## Key Claims

- Fork of the Abstract Machine (AM) framework tailored for OpenXiangShan, as indicated by the repository name and README.
- Provides Makefiles and build infrastructure for producing memory images for RTL simulation at base address 0x80000000.
- Supports building bootrom flash images at base address 0x10000000 using the riscv64-xs-flash target.
- Uses the riscv64-xs architecture target for simulation workloads.
- Includes a CoreMark benchmark build example under apps/coremark.
- Designed to work with the DiffTest RTL-simulation framework and NEMU, as mentioned in the README.
- Requires the environment variable AM_HOME to point to the repository root.

## Relationships

None at this time.

## Sources

- [OpenXiangShan/nexus-am - GitHub](raw/cache/081e54846e46688e.md)
