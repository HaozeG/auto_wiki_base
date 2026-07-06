---
canonical_name: XuanTie C920V2
aliases:
- C920V2
- xt-c920v2
subtype: null
tags: []
hardware_targets:
- XuanTie C920V2
toolchains:
- LLVM
- Clang
constraints:
- 64-bit superscalar out-of-order RISC-V core
- RISC-V Vector Extension version 1.0 (V), with Zve32f and Zve32x subsets
- RV64IMAFDCB plus standard Z extensions (similar to C910V2: Zicbom, Zicbop, Zicboz,
    Zfa, Zfbfmin, Zfh, Zca, Zcb, Zcd, etc.)
- T-Head custom extensions: XTHeadBa, XTHeadBb, XTHeadBs, XTHeadCmo, XTHeadCondMov,
    XTHeadFMemIdx, XTHeadMac, XTHeadMemIdx, XTHeadMemPair, XTHeadSync
- Used in the Sophon SG2044 SoC
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
inbound_links: 2
outbound_links:
- target: sophon-sg2044-hardware-target
  reason: The Sophon SG2044 SoC uses the XuanTie C920v2 core; this page documents
    the processor definition for that core as added to LLVM
- target: xuantie-c910v2-hardware-target
  reason: The C920V2 is the vector-capable counterpart of the C910V2, sharing T-Head
    custom extensions and base ISA but adding RVV 1.0
---

# XuanTie C920V2

XuanTie C920V2 is a 64-bit superscalar out-of-order RISC-V CPU core developed by T-Head Semiconductor Co., Ltd. It includes the ratified RISC-V Vector Extension version 1.0 (V) along with the Zve32f and Zve32x subsets, supporting 128-bit vector lanes. The core inherits the same T-Head custom extensions as the C910V2, including XTHeadBa, XTHeadBb, XTHeadBs, XTHeadCmo, XTHeadCondMov, XTHeadFMemIdx, XTHeadMac, XTHeadMemIdx, XTHeadMemPair, and XTHeadSync, which accelerate cache management, synchronization, and bit manipulation. The C920V2 is the vector-capable variant of the C910V2 and is used in the Sophon SG2044 high-performance RISC-V SoC. This processor definition was added to LLVM in pull request #174056, enabling the -mcpu=xt-c920v2 target flag. The LLVM scheduling model for the C920V2 is planned for a future PR.

## Key Claims

- XuanTie C920V2 is a 64-bit superscalar out-of-order RISC-V CPU core.
- It implements the RISC-V Vector Extension version 1.0, including Zve32f and Zve32x.
- It shares the same set of T-Head custom extensions with the C910V2.
- The core is used in the Sophon SG2044 SoC.
- LLVM processor definition added in PR #174056, with -mcpu=xt-c920v2; scheduling model to follow.

## Optimization-Relevant Details

- ISA/profile: RV64IMAFDCB_V plus standard Z extensions (including B, Zfa, Zfh, Zfbfmin, etc.) and T-Head custom extensions.
- Vector/matrix/accelerator support: RVV 1.0 with Zve32f and Zve32x; 128-bit vector lanes (implied by Zve32x).
- Memory/cache/TLB/DMA: Details not provided in this source.
- Compiler/toolchain support: LLVM/Clang (via PR #174056), GCC expected to support via similar definitions.

## Relationships

- [[sophon-sg2044-hardware-target]]: The Sophon SG2044 SoC uses the XuanTie C920v2 core; this page documents the processor definition for that core as added to LLVM.
- [[xuantie-c910v2-hardware-target]]: The C920V2 is the vector-capable counterpart of the C910V2, sharing T-Head custom extensions and base ISA but adding RVV 1.0.

## Sources

- https://github.com/llvm/llvm-project/pull/174056
- http://www.mail-archive.com/cfe-commits@lists.llvm.org/msg642200.html
