---
canonical_name: SpacemiT K3
aliases:
- K3
- SpacemiT K3 SoC
- Bianbu K3
- MilkV Jupiter 2
- Milk-V Jupiter 2
- llama.cpp inference on SpacemiT K3
- SpacemiT K3 LLM benchmark
- llama.cpp K3 benchmark
- Llama.cpp SpaceMIT K3 Gemma 4 QAT MTP Benchmarks
- llama-cpp-spacemit-k3
- SpaceMIT K3 Gemma 4 benchmarks
- Milk-V Jupiter 2 Gemma 4 benchmarks
subtype: null
tags:
- RISC-V
- SpacemiT
- AI CPU
- big.LITTLE
- RVV 1.0
hardware_targets:
- SpacemiT K3
- SpacemiT X100
- SpacemiT A100
toolchains:
- GCC 15.2.0
- cmake
- llama.cpp
constraints:
- 16 cores: 8 X100 (general-purpose) + 8 A100 (AI acceleration)
- X100: 2.4 GHz, vlen 256 bits, ISA rv64imafdcvh
- A100: 2.0 GHz, vlen 1024 bits, ISA rv64imafdcv (no hypervisor)
- shared extensions: zicbop, zicond, zfa, zawrs, vector crypto, zvfh
- 32 GB shared RAM
- Linux kernel 6.18.3
- GCC 15.2.0 compiler
- IME2 matrix instructions (vendor-only, not public)
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/c87de398f6c8a898.md
- https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
- raw/cache/673f92af34a7ba79.md
- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
- raw/cache/cc037e7fa5f7e3f8.md
- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
- raw/cache/6ed1f6b02116b03a.md
- https://www.cnx-software.com/2026/01/23/spacemit-k3-16-core-risc-v-soc-system-information-and-early-benchmarks/
source_url: https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
fetched_at: '2026-07-03T16:13:21.390248+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
outbound_links:
- target: spacemit-x60-hardware-target
  reason: The X100 general-purpose core in the K3 is the successor to the X60 core
    in the SpacemiT K1 SoC, sharing the same 256-bit vector width but operating at
    a 50% higher clock (2.4 GHz vs 1.6 GHz) and achieving 2.3x faster token generation
    throughput on TinyLlama 1.1B Q4_0
---

# SpacemiT K3

SpacemiT K3 is a 16-core RISC-V AI CPU/system-on-chip (SoC) designed by SpacemiT Technology, featuring a big.LITTLE architecture with two core types on the same die: eight X100 general-purpose cores (up to 2.4 GHz, 256-bit vector length) and eight A100 AI accelerator cores (up to 2.0 GHz, 1024-bit vector length). Both core types share the RV64IMAFDCV base ISA and common extensions including zicbop, zicond, zfa, zawrs, vector crypto, and half-precision float support (zvfh). The X100 cores additionally implement the hypervisor extension (rv64imafdcvh), while the A100 cores omit virtualization support. The SoC is RVA23-compliant, meeting the hardware requirements for Ubuntu 25.10 and later. The K3 runs Linux kernel 6.18.3 (also observed running Ubuntu 26.04 with Linux kernel 6.12) with 32 GB of shared RAM and uses GCC 15.2.0 as the default toolchain. The chip is accessible via SpacemiT's BianbuCloud platform for remote evaluation (also available as a remote-access server for benchmarking). The A100 cores include proprietary IME2 matrix instructions that are not yet supported by public compiler toolchains, requiring a vendor-specific build of llama.cpp to achieve optimal AI inference performance. The SoC features a shared 8 MB L2 cache (one source reports 10 MiB L2 cache), supports the RVA23 profile, and includes a 60 TOPS AI compute engine (IME2 matrix instructions). It also supports additional extensions: Zfh, Zvfh, Zfbfmin, Zvfbfmin, Zvfbfwma, and vector cryptography (Zvkng, Zvksg, Zvbc). The K3 powers the Milk-V Jupiter 2 single-board computer. The system includes a 128 GB NVMe solid-state drive and a 64 GB UFS 2.2 flash device, two Gigabit Ethernet ports (one active with dwmac_spacemit_ethqos driver), and an embedded DisplayPort (eDP) interface via the saturn-edp driver. No hardware GPU acceleration is available (softpipe renderer only). Temperature sensors are present but report erroneous high values (~413°C CPU); other thermal zones report plausible temperatures around 60–65°C.

## Key Claims

- The K3 has two core types: X100 (general-purpose, vlen 256) and A100 (AI acceleration, vlen 1024), identical ISA extensions except the hypervisor extension (X100 only).
- X100 cores run at up to 2.4 GHz (advertised 2.5 GHz), A100 cores at up to 2.0 GHz.
- Total system memory is 32 GB shared across both core types.
- Shared 8 MB L2 cache (one source reports 10 MiB L2 cache).
- RVA23 profile compliance.
- 60 TOPS peak AI compute (IME2 matrix instructions).
- Supports FP16/BF16 compute via Zvfh, Zfbfmin extensions.
- The A100 cores support proprietary IME2 matrix instructions for AI acceleration, which are not publicly compiled in standard toolchains.
- The K3 was accessed via the BianbuCloud platform, which uses Chinese-locale web terminals and requires ssh-rsa for access.
- Standard llama.cpp built with GGML_NATIVE=ON runs 2.3x faster on X100 cores than the K1's X60 cores, but 34x slower on A100 cores than X100 at single-thread prompt processing.
- SpacemiT's custom build using IME2 instructions achieves 111 t/s prompt processing on A100, making A100 the fastest core type.
- Powers the Milk-V Jupiter 2 SBC.
- Benchmark results using a custom llama.cpp fork with the SpaceMIT CPU backend (IME2-aware) and TurboQuant optimizations on the Milk-V Jupiter 2 (8 A100/IME2 cores, TCM block size 393216, f16 KV cache, memory backend HPAGE):
    - Gemma 4 E2B QAT (Q4_K_XL): cold prefill 93.14 tok/s, generation 12.93 tok/s, MTP acceptance 0.306, coherence pass.
    - Gemma 4 E4B QAT: cold prefill 55.37 tok/s, generation 8.52 tok/s, MTP acceptance 0.336.
    - Gemma 4 12B QAT: cold prefill 20.72 tok/s, generation 4.32 tok/s, MTP acceptance 0.429.
    - Gemma 4 26B A4B QAT: best generation 8.36 tok/s at context 16K with f16 KV cache; OOM at 64K.
    - llama-bench best results: E2B prefill 120.90 tok/s (threads=8, ubatch=256, f16), generation 13.36 tok/s (threads=8, ubatch=512, f16).
    - Thread count 8 performs best; using 12 threads causes TCM contention.
    - f16 KV cache consistently outperforms q8_0 by ~1.8 tok/s on generation.
- 128 GB NVMe SSD and 64 GB UFS 2.2 flash storage.
- Two Gigabit Ethernet ports (one active with dwmac_spacemit_ethqos driver).
- Embedded DisplayPort (eDP) interface via saturn-edp driver; no hardware GPU acceleration (softpipe renderer only).
- Temperature sensors report erroneous high values (~413°C CPU); other thermal zones report plausible temperatures around 60–65°C.

## Optimization-Relevant Details

- ISA/profile: X100: rv64imafdcvh; A100: rv64imafdcv; shared: zicbop, zicond, zfa, zawrs, vector crypto, zvfh; also RVA23 with Zfh, Zvfh, Zfbfmin, Zvfbfmin, Zvfbfwma, Zvkng, Zvksg, Zvbc
- Vector/matrix/accelerator support: X100: RVV 1.0, vlen 256 bits; A100: RVV 1.0, vlen 1024 bits, plus IME2 matrix instructions (vendor-only)
- Memory/cache/TLB/DMA: 32 GB shared RAM; shared L2 cache: 8 MB (one source reports 10 MiB); 128 GB NVMe SSD; 64 GB UFS 2.2 flash; eDP display; Gigabit Ethernet
- Compiler/toolchain support: GCC 15.2.0 (standard); vendor toolchain for IME2 not public; Linux kernel 6.18.3 / 6.12; Ubuntu 26.04; inxi 3.3.40
- Custom llama.cpp build flags: -DGGML_CPU_RISCV64_SPACEMIT=ON -DGGML_RV_ZBA=ON -DGGML_RV_ZFH=ON -DGGML_RV_ZVFH=ON
- Benchmark configuration: TCM block size 393216, memory backend HPAGE, f16 KV cache

## Relationships

- [[spacemit-x60-hardware-target]]: The X100 general-purpose core in the K3 is the successor to the X60 core in the SpacemiT K1 SoC, sharing the same 256-bit vector width but operating at a 50% higher clock (2.4 GHz vs 1.6 GHz) and achieving 2.3x faster token generation throughput on TinyLlama 1.1B Q4_0.
- [[llama.cpp-on-spacemit-k3-benchmark]]: Records benchmark results on this hardware for LLM inference workloads.
- [[spacemit-ime2-llama-cpp-optimization]]: Describes the vendor IME2 optimization recipe that unlocks A100 performance on this hardware.
- [[andes-ax45mpv-hardware-target]]: Both are high-performance RISC-V targets with vector processing capabilities; Andes AX45MPV is a licensable core IP available for SoC integration, while Spacemit K3 is a complete SoC that integrates custom X100 cores and provides a system for benchmarking.

## Sources

- https://dev.to/gounthar/benchmarking-llamacpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4-10mc
- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
- https://www.cnx-software.com/2026/01/23/spacemit-k3-16-core-risc-v-soc-system-information-and-early-benchmarks/
