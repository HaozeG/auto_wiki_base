---
canonical_name: XuanTie
aliases:
- T-Head XuanTie
- XuanTie processor
- XT
- XTheadVector
- XuanTie Vector Extension
- TH Vector
- xtheadvector
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/2219974cd9dd0df6.md
- https://www.xrvm.cn/
- raw/cache/bb714ae7abde63e5.md
- https://github.com/XUANTIE-RV/thead-extension-spec/blob/master/xtheadvector.adoc
source_url: https://www.xrvm.cn/
fetched_at: '2026-07-03T13:18:48.558457+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-ai-benchmark-suite
  reason: XuanTie is the brand that produces the XuanTie C907 and C908 cores targeted
    by the XuanTie AI Benchmark Suite, which provides precompiled model binaries for
    those specific cores
---

# XuanTie

XuanTie is a RISC-V processor IP brand under Alibaba's DAMO Academy (T-Head). The brand aims to become an international leader in the RISC-V ecosystem by developing RISC-V technology and launching a series of XuanTie processors covering high, medium, and low performance segments. XuanTie embraces open source and open innovation, building an ecosystem with partners across chips, development tools, operating systems, and application solutions to promote software-hardware integration. Leveraging Alibaba's strengths in cloud computing, artificial intelligence, and big data, XuanTie provides a new computing architecture based on RISC-V and secure processor IP cores for the digital age.

As part of its processor IP, T-Head (XuanTie) has developed XTheadVector, a non-standard RISC-V vector extension for their CPU cores. Version 1.0 of the extension is frozen and stable. XTheadVector is not compatible with the standard RISC-V V extension due to intentional encoding overlaps with V version 0.7.1, and it defines its own instruction prefixes (th.) and CSR prefixes (th.) to avoid conflict with the standard extension. The extension provides 32 vector registers and six unprivileged CSRs (th.vstart, th.vxsat, th.vxrm, th.vl, th.vtype, th.vlenb) that overlap with the corresponding V extension registers. Tools are required to report an error if both XTheadVector and V extensions are enabled simultaneously. The extension is available on XuanTie CPUs with vendor ID 0x5b7, misa bit 21 set, and implementation ID 0, which currently identifies the C906V, C920, and R920 processors.

## Key Claims

- XuanTie is a RISC-V processor IP brand under Alibaba's DAMO Academy (T-Head).
- The brand offers a series of XuanTie processors that cover high, medium, and low performance requirements.
- XuanTie embraces open source and has built an ecosystem with partners across chips, development tools, operating systems, and application solutions.
- The brand aims to become an international leader in the RISC-V ecosystem.
- XTheadVector v1.0 is a stable, non-standard RISC-V vector extension that uses an encoding space overlapping with the V extension v0.7.1, making the two extensions mutually exclusive in toolchains.
- The extension adds 32 vector registers and six CSRs prefixed with `th.` instead of the standard `v` prefix.
- All instructions are prefixed with `th.` to distinguish them from standard V instructions.
- Compared to V v0.7.1, XTheadVector adds VLENB CSR, renames CSRs with `th.` prefix, and promotes Zvlsseg to a mandatory part rather than a subextension.
- Compared to V v1.0, XTheadVector lacks vsetivli, whole register moves, fractional LMUL, vlm/vsm, and configurable vta/vma (fixed to TAMU). It also has different load/store instruction encodings and strict register overlap rules for narrowing and comparison operations.
- Availability is gated by vendor ID 0x5b7, misa.V set, and mimpid == 0 (implementation ID zero), identifying C906V, C920, and R920 cores.
- The extension defines pseudo instructions (`th.vmmv.m`, `th.vneg.v`, `th.vncvt.x.x.v`, `th.vfneg.v`, `th.vfabs.v`) to improve compatibility with RVV 1.0 source code.

## Relationships

- [[xuantie-ai-benchmark-suite]]: XuanTie is the brand that produces the XuanTie C907 and C908 cores targeted by the XuanTie AI Benchmark Suite, which provides precompiled model binaries for those specific cores.
- [[andes-ax45mpv-hardware-target]]: XTheadVector is a non-standard RISC-V vector extension that conflicts with the standard V extension used by the Andes AX45MPV core, as its encoding overlaps with V v0.7.1 and uses different CSR/instruction naming conventions, making the two incompatible in a single toolchain.

## Sources

- https://www.xrvm.cn/
- https://github.com/XUANTIE-RV/thead-extension-spec/blob/master/xtheadvector.adoc
