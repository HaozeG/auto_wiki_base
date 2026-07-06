---
canonical_name: XuanTie C910V2
aliases:
- C910V2
- xt-c910v2
subtype: null
tags: []
hardware_targets:
- XuanTie C910V2
toolchains:
- LLVM
- Clang
constraints:
- 64-bit superscalar out-of-order RISC-V core
- RV64IMAFDCB plus Zicbom, Zicbop, Zicboz, Zicntr, Zicond, Zicsr, Zifencei, Zihintntl,
  Zihintpause, Zihpm, Zmmul, Zaamo, Zalrsc, Zawrs, Zfa, Zfbfmin, Zfh, Zfhmin, Zca,
  Zcb, Zcd, Zba, Zbb, Zbc, Zbs, Sscofpmf, Sstc, Svinval, Svnapot, Svpbmt
- T-Head custom extensions: XTHeadBa, XTHeadBb, XTHeadBs, XTHeadCmo, XTHeadCondMov,
    XTHeadFMemIdx, XTHeadMac, XTHeadMemIdx, XTHeadMemPair, XTHeadSync
- Does not include RISC-V Vector Extension (V)
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/adbcbaf870422ef4.md
- http://www.mail-archive.com/cfe-commits@lists.llvm.org/msg642200.html
source_url: http://www.mail-archive.com/cfe-commits@lists.llvm.org/msg642200.html
fetched_at: '2026-07-06T02:08:14.064012+00:00'
type: hardware_target
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
outbound_links:
- target: xuantie-c906-hardware-target
  reason: Both are T-Head XuanTie cores, but the C910V2 is a superscalar out-of-order
    design while the C906 is in-order single-issue
- target: xuantie-c920v2-hardware-target
  reason: The C910V2 and C920V2 share the same T-Head custom extensions and base ISA,
    but the C920V2 adds the RISC-V Vector Extension version 1.0
---

# XuanTie C910V2

XuanTie C910V2 is a 64-bit superscalar out-of-order RISC-V CPU core developed by T-Head Semiconductor Co., Ltd. It implements the RISC-V base ISA with extensions including I, M, A, F, D, C, B, and a comprehensive set of standard Z extensions such as Zicbom, Zicbop, Zicboz, Zfa, Zfbfmin, Zfh, Zca, Zcb, Zcd, and T-Head custom extensions including XTHeadBa, XTHeadBb, XTHeadBs, XTHeadCmo, XTHeadCondMov, XTHeadFMemIdx, XTHeadMac, XTHeadMemIdx, XTHeadMemPair, and XTHeadSync. The C910V2 does not include the RISC-V Vector Extension, distinguishing it from the C920V2. This processor definition was added to LLVM in pull request #174056, enabling the -mcpu=xt-c910v2 target flag. The core is designed for high-performance computing with superscalar out-of-order execution and supports the full set of T-Head custom instructions for cache management, synchronization, and bit manipulation. The LLVM scheduling model for the C910V2 is planned for a future follow-up PR.

## Key Claims

- XuanTie C910V2 is a 64-bit superscalar out-of-order RISC-V CPU core.
- The core supports a broad set of standard RISC-V extensions including Zfa, Zfh, Zfbfmin, and the B extension (zba, zbb, zbc, zbs).
- It features T-Head custom extensions for cache management, synchronization, memory operations, and bit manipulation.
- The C910V2 does not include the RISC-V Vector Extension (V).
- LLVM processor definition was added in PR #174056, allowing use of -mcpu=xt-c910v2. A scheduling model is expected in a future PR.

## Optimization-Relevant Details

- ISA/profile: RV64IMAFDCB plus standard Z extensions (list above) and T-Head custom extensions.
- Vector/matrix/accelerator support: None (no vector extension).
- Memory/cache/TLB/DMA: Details not provided in this source.
- Compiler/toolchain support: LLVM/Clang (via PR #174056), GCC compatibility expected.

## Relationships

- [[xuantie-c906-hardware-target]]: Both are T-Head XuanTie cores, but the C910V2 is a superscalar out-of-order design while the C906 is in-order single-issue.
- [[xuantie-c920v2-hardware-target]]: The C910V2 and C920V2 share the same T-Head custom extensions and base ISA, but the C920V2 adds the RISC-V Vector Extension version 1.0.

## Sources

- https://github.com/llvm/llvm-project/pull/174056
- http://www.mail-archive.com/cfe-commits@lists.llvm.org/msg642200.html
