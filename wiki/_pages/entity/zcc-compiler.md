---
canonical_name: ZCC
aliases:
- Terapines ZCC
- ZCC 4.x
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/8933264019d5d3b7.md
- https://www.terapines.com/en/docs/zcc/
source_url: https://www.terapines.com/en/docs/zcc/
fetched_at: '2026-07-03T14:05:40.203797+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: ZCC supports XuanTie vendor extensions, providing compiler compatibility
    for the XuanTie C908 processor targeted in the SHL Winograd and GEMM optimization
    recipe
---

# ZCC

ZCC is a high-performance C/C++ compiler for RISC-V architectures, developed by Terapines and based on the LLVM framework. It supports modern C and C++ language standards including C17, C11, C99, C++17, C++14, and C++11, and provides RVV auto-vectorization along with other compiler optimizations. ZCC supports a wide range of RISC-V ISA extensions, including standard extensions and vendor-specific extensions from XuanTie, Nuclei, and Andes. The toolchain is available for Windows (10 and above) and multiple Linux distributions such as Ubuntu, CentOS, Fedora, and openSUSE Leap. ZCC also includes optional libraries: LibDSP for digital signal processing and LibNN for neural network inference.

## Key Claims

- ZCC is an LLVM-based C/C++ compiler for RISC-V, supporting vendor extensions from XuanTie, Nuclei, and Andes.
- It supports RVV auto-vectorization and other compiler optimizations.
- The toolchain is available on Windows 10+ and Linux distributions including Ubuntu (18-24.04), CentOS (6-8), Fedora 42, and openSUSE Leap 15.5.
- Optional libraries include LibDSP (digital signal processing) and LibNN (neural network inference).
- Supports C and C++ language standards up to C17/C18 and C++17.

## Relationships

- [[c908-wino-gemm-optimization]]: ZCC supports XuanTie vendor extensions, providing compiler compatibility for the XuanTie C908 processor targeted in the SHL Winograd and GEMM optimization recipe.

## Sources

- https://www.terapines.com/en/docs/zcc/
