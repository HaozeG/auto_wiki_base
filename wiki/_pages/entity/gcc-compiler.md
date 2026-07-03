---
canonical_name: GCC
aliases:
- GNU Compiler Collection
- gcc
- GCC compiler
subtype: null
tags: []
scorecard:
  novelty_delta: 0.3
  claim_density: 0.2
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/0922ffc2d217f269.md
- https://github.com/gcc-mirror/gcc
source_url: https://github.com/gcc-mirror/gcc
fetched_at: '2026-07-02T12:46:07.876294+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# GCC

The GNU Compiler Collection (GCC) is a free software compiler system that supports multiple programming languages including C, C++, Ada, D, Fortran, Go, and others, with source hosted at git://gcc.gnu.org/git/gcc.git and mirrored on GitHub under gcc-mirror/gcc. The repository includes runtime libraries such as libgcc, libstdc++-v3, libgfortran, libgo, libada, libobjc, and libatomic along with configuration, build, and install scripts, and the INSTALL directory contains copies of installation information as HTML and plain text derived from gcc/doc/install.texi. The project is licensed under GPL-2.0, with some components under LGPL-2.1 and other licenses, and the repository language breakdown shows C++ (30.0%), C (29.4%), Ada (13.9%), D (5.9%), Go (5.2%), HTML (3.6%), and other (12.0%). GCC serves as the primary compiler for many open-source operating systems and embedded platforms, and its source has accumulated over 230,000 commits.

## Key Claims

- GCC is free software under GPL-2.0 with additional LGPL-2.1 and other licenses for certain components.
- The GCC source repository on GitHub (gcc-mirror/gcc) has over 230,000 commits.
- The project is primarily written in C++ (30.0%) and C (29.4%), with significant portions in Ada, D, Go, and HTML.
- GCC includes runtime libraries: libgcc, libstdc++-v3, libgfortran, libgo, libada, libobjc, libatomic, libbacktrace, libcc1, libcody, libcpp, libdecnumber, libffi, libgomp, libgrust, libiberty, libitm, libphobos, libquadmath, libsanitizer, libssp, libvtv, and lto-plugin.
- Installation information is available in the INSTALL directory as HTML and plain text.
- Bug reports should be submitted via http://gcc.gnu.org/bugs/.

## Relationships

- [[vectrans]]: VecTrans is an LLM-assisted code vectorization framework that uses GCC as one of its target compilers to identify non-vectorized loops.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This optimization recipe compares LLVM and GCC performance on RISC-V, and GCC is a reference compiler for benchmarking.
- Insufficient context for additional cross-links to entity pages; only two optimization recipe pages are visible in the wiki context.

## Sources

- [GitHub - gcc-mirror/gcc](https://github.com/gcc-mirror/gcc)
- [GCC official site](http://gcc.gnu.org)
