---
canonical_name: Xuantie C900 Bugs
aliases:
- C900-series bugs
- Xuantie C900 errata
- GhostWrite vulnerability
- C906 halt sequence
- revyos/xuantie-c900-bugs
subtype: null
tags:
- Xuantie
- C900
- bug
- security
- erratum
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/c40c2037eb708dd6.md
- https://github.com/revyos/xuantie-c900-bugs
source_url: https://github.com/revyos/xuantie-c900-bugs
fetched_at: '2026-07-02T06:20:18.955039+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Xuantie C900 Bugs

The Xuantie C900 Bugs document is a GitHub-hosted summary of security and functional errata affecting the Xuantie C900-series RISC-V processor cores developed by Alibaba T-Head. It documents three main issues: the GhostWrite vulnerability in XTheadVector unit-strided stores with reserved width that bypasses the MMU on C910 and C920 cores; a halt sequence triggered by specific load instructions in the XTheadMemIdx extension on C906 cores; and a potential hang condition on C910 when accessing physically-backed virtual address zero. For each bug, the document provides proof-of-concept code demonstrating the exploit or crash, lists the specific hardware variants that are affected, and describes available mitigations including detection in the mainline Linux kernel since commit `4bf97069239b` ("riscv: Add ghostwrite vulnerability") landed in version 6.14. The bugs span both the XTheadVector and XTheadMemIdx custom extensions as well as standard RISC-V behavior, and they affect SoCs such as the TH1520, SG2042, and CV1800B. The kernel mitigation for GhostWrite is controlled by the `CONFIG_ERRATA_THEAD_GHOSTWRITE` configuration option and can be disabled at runtime with `mitigations=off`.

## Key Claims

- GhostWrite (CVE-2025-?): Unit-strided vector stores with `mew=1` (reserved width) are incorrectly decoded and executed on C910 and C920 cores, allowing unprivileged writes to arbitrary physical memory by bypassing the MMU.
- GhostWrite scope: Affected variants include C910 (tested on TH1520 SoC) and C920v1 (tested on SG2042 SoC). C906 raises a Store/AMO access fault but does not perform arbitrary writes.
- C906 halt sequence: Fourteen load instructions from the XTheadMemIdx extension that modify the base register (e.g., `th.lbib`) can trigger a machine crash on C906 when the destination register matches the base and the instruction is followed by a CSR read targeting the same register and another register access.
- C910 hang: Reading from or writing to virtual address zero when mapped to a physical address can cause C910 to hang stably after repeated runs.
- Linux kernel mitigation for GhostWrite is present in upstream version 6.14 via the `CONFIG_ERRATA_THEAD_GHOSTWRITE` config option, which enables runtime detection and mitigation.
- The bugs are documented with assembler and C proof-of-concept code that can be reproduced on real hardware.

## Relationships

- [[sifive_performance_p570_gen3]] is another high-performance RISC-V core that may benefit from similar security hardening considerations.
- [[coral_npu_vector_execution_engine]] represents a different design point in the RISC-V vector space; the GhostWrite bug underscores the importance of MMU-aware vector instruction decoding. Insufficient context for additional cross-links.

## Sources

- https://github.com/revyos/xuantie-c900-bugs
