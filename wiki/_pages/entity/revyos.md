---
cold_start: false
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.65
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.85
  self_containedness: 0.9
sources:
- https://docs.revyos.dev/en/docs/intro/
tags:
- risc-v
- distribution
- debian
- xuantie
- alibaba
- plct-lab
- ruyisdk
type: entity
updated: '2026-06-28'
---

# RevyOS

RevyOS is a Debian-based customised Linux distribution developed and maintained by the RevyOS squad of the RuyiSDK team for the XuanTie chip ecosystem. It is part of the RuyiSDK open-source project initiated by PLCT Lab, which aims to provide a convenient and comprehensive development environment for RISC-V developers. RevyOS delivers up-to-date hardware information and software support, including details on supported devices, software components such as system images, toolchains, and package managers. The distribution offers comprehensive adaptation and optimisation for XuanTie C906, C910, C920, C908 and other processors, shipping with a GCC toolchain that supports the XuanTie extension instruction set and RVV 1.0 by default, together with Glibc and the kernel tuned for RVV 1.0. At present, RevyOS already satisfies day-to-day needs in office work, web browsing, and video playback.

## Key Claims

- RevyOS is a Debian-based distribution specifically customised for the XuanTie chip ecosystem, developed by the RuyiSDK team at PLCT Lab.
- It provides comprehensive adaptation and optimisation for XuanTie C906, C910, C920, C908 and other RISC-V processors.
- The distribution ships with a GCC toolchain that supports the XuanTie extension instruction set and the ratified RVV 1.0 vector extension, along with tuned Glibc and kernel for RVV 1.0.
- RevyOS meets basic daily computing requirements including office work, web browsing, and video playback on supported hardware.
- User-edition images are updated regularly and hosted on the ISCAS mirror, with support for multiple development boards such as Lichee Pi 4A, Milk-V Meles, Lichee Cluster 4A, Lichee Console 4A, Lichee Book 4A, Milk-V Pioneer, and Sophgo EVB.
- The distribution includes a dedicated user group (Telegram) and extensive documentation for building, porting, and system usage.

## Relationships

- [[alibaba_xuantie_c910_c920]] – RevyOS is optimised for XuanTie C910 and C920 processors, which are the hardware foundation for many supported boards like Lichee Pi 4A and Milk-V Meles.
- [[risc_v_vector_extension]] – RevyOS ships with a toolchain that supports RVV 1.0 and includes tuned Glibc and kernel for the ratified vector extension, aligning with the RISC-V Vector Extension standard.

## Sources

- RevyOS official documentation: https://docs.revyos.dev/en/docs/intro/
