---
cold_start: false
connected_entities:
- Tenstorrent
- TT_Metalium
- TT-Forge
- Tenstorrent_Software_Stack
- Tenstorrent_Ascalon
- Blackhole_Architecture
- Tenstorrent_Wormhole_n300
- Tenstorrent_Grayskull
- Wormhole_Tensix_Processor
- Blackhole_Tensix_Processor
- TT_Inference_Server_Benchmarking
- TT-QuietBox_2
- Operator_Fusion_for_LLM_Inference_on_Tensix
- FlashAttention_on_Tenstorrent_Wormhole_Optimization
created: 2026-06-29
inbound_links: 0
scorecard:
  bridge_score: 0.9
  contradiction_potential: 0.3
  cross_domain_connection: 0.85
sources:
- https://tenstorrent.com
- https://github.com/tenstorrent/tt-metal
- https://github.com/tenstorrent/tt-forge
- https://speakerdeck.com/tenstorrent_japan/blackhole-architecture
- https://arxiv.org/html/2509.19294v1
synthesis_status: active
type: synthesis
updated: 2026-06-29
---

# Tenstorrent RISC-V AI Ecosystem

## RAG Summary

Tenstorrent is building a vertically integrated RISC-V AI ecosystem spanning custom silicon, ISA-level CPU IP, and a fully open-source software stack. The hardware generation sequence—Grayskull (e75/e150), Wormhole (n150/n300), Blackhole (P150/P300)—each centers on the Tensix core, a tile containing five 32-bit RISC-V "baby cores," a matrix FPU, a wide SFPU, 1.5 MB SRAM, and a 2D torus Network-on-Chip (NoC). Wormhole ships 64–128 Tensix cores with GDDR6 memory and 200 Gbps Ethernet for multi-chip mesh scaling; Blackhole scales to 140 Tensix cores, adds PCIe Gen 5, 12×400G Ethernet, and GDDR6. The Ascalon RISC-V CPU core is separately licensable IP, targeted at SoC integrators who want a high-performance general-purpose host alongside the AI accelerator—LG and Hyundai are named IP licensees. The software stack layers TT-Metalium (bare-metal kernel runtime, analogous to CUDA) under TT-Forge, an MLIR-based compiler with PyTorch/JAX/ONNX frontends that defines TTIR, TTNN, and TTKernel dialects and tests 800+ model variants in CI. Key optimization results from the wiki include an SRAM-fused attention kernel on Grayskull and a FlashAttention implementation on Wormhole that avoids HBM round-trips by keeping K/V tiles in 1.5 MB per-core SRAM. A core architectural claim across generations is that the Tensix RISC-V baby cores handle DMA, synchronization, and data routing without a dedicated DMA engine, relying instead on the NoC and the programmable cores, which distinguishes this approach from both systolic-array accelerators and vector-ISA CPUs.

---

## Full Synthesis

### Hardware Generation Sequence

Tenstorrent has shipped three distinct silicon generations, all built around the Tensix tile abstraction:

| Generation | Cores | Memory | Key I/O | Status |
|-----------|-------|--------|---------|--------|
| Grayskull (e75/e150) | 80/120 Tensix | LPDDR4 | PCIe 4 | Discontinued, community boards available |
| Wormhole (n150/n300) | 64/128 Tensix | 12/24 GB GDDR6 | 2× QSFP-DD 200 Gbps, PCIe 4 | Current production |
| Blackhole (P150/P300) | 140 Tensix | GDDR6 | 12× 400G Ethernet, PCIe 5 | Available |

Blackhole introduces a more capable NoC (2D torus retained) and dramatically higher Ethernet bandwidth (12×400G vs Wormhole's 2×200G), enabling larger multi-chip Galaxy clusters without an external switch.

### The Tensix Core as RISC-V Compute Tile

Each Tensix core contains five 32-bit RISC-V "baby cores" that serve distinct roles: two BRISC cores handle data movement from NoC/DRAM to local SRAM, two TRISC cores orchestrate tensor operations on the FPU, and one NRISC core handles network routing. This RISC-V-programmable control plane is the key differentiator from fixed-dataflow accelerators like systolic arrays. The 1.5 MB of SRAM per Tensix core is the primary on-chip fast memory; Wormhole's 64 cores provide 96 MB total on-chip SRAM, which is leveraged by kernel optimizations that fuse attention to avoid HBM round-trips (see [[FlashAttention_on_Tenstorrent_Wormhole_Optimization]] and [[Grayskull_SRAM_Fused_Attention_Kernel]]).

### Software Stack Layers

```
TT-Forge (MLIR compiler: TTIR → TTNN → TTKernel dialects)
    ├── TT-XLA frontend (PyTorch via PJRT, JAX)
    ├── TT-Forge-ONNX frontend (TensorFlow, PaddlePaddle, ONNX)
    └── TT-Lang (Python DSL for custom kernels)
TT-NN (operator library)
TT-Metalium (low-level kernel runtime — RISC-V baby core programming)
TT-UMD (user-mode driver)
Hardware (Tensix NoC + RISC-V baby cores)
```

TT-Metalium is the CUDA/ROCm analogue: it exposes the RISC-V cores and NoC directly for custom kernel development in C++. TT-Forge sits above it as the compiler path for users bringing PyTorch/JAX models. The [[Tenstorrent_Software_Stack]] page provides the definitive layer map; the [[TT-Forge]] page covers compiler internals including the 800+ model CI test suite.

### Ascalon: RISC-V CPU IP as a Separate Product

Tenstorrent has made a strategic pivot to IP licensing. The Ascalon RISC-V CPU core is offered as licensable IP for SoC integrators. Imperas provides a simulation model of Ascalon within its RISC-V model library, enabling early software development and architectural exploration before tape-out. The licensing approach is already generating revenue (LG, Hyundai named as licensees) and positions Tenstorrent as a RISC-V IP vendor alongside the hardware business. The next-generation "Neo" core uses a cluster-shared-resource architecture, breaking from the current Tensix model.

### Key Open Questions

- **Compiler maturity gap:** TT-Forge is in public beta and tests 800+ models in CI, but production deployment reliability vs. established stacks (TensorRT, vLLM) is not yet benchmarked comparatively in this wiki.
- **Multi-chip scaling:** Galaxy clusters use Blackhole's 12×400G Ethernet for mesh interconnect, but published scaling efficiency numbers (MFU at scale) are absent from wiki pages.
- **RISC-V baby core vs. dedicated DMA:** Whether using programmable RISC-V cores for data routing is a performance advantage or bottleneck relative to fixed DMA engines (as in Gemmini or Ara) is an open architectural debate not resolved by current wiki sources.
- **Ascalon vs. main-core RISC-V:** Ascalon targets high-performance general-purpose hosts, but how it compares to XuanTie C910 or SiFive P870 on SPECcpu or per-core ML inference is uncovered.

## Open Questions

1. What is Tenstorrent Wormhole/Blackhole's achieved TFLOPS on LLM inference vs. published peak TFLOPS (utilization)?
2. Does TT-Forge match or exceed TT-Metalium hand-tuned kernels on standard transformer layers?
3. How does Galaxy multi-chip MFU compare to NVLink-connected GPU clusters at equivalent scale?
4. What is the Ascalon CPU's target frequency, core count, and cache configuration?

## Connected Pages

- [[Tenstorrent]] — company overview, IP licensing strategy, Neo roadmap
- [[TT_Metalium]] — low-level RISC-V kernel runtime
- [[TT-Forge]] — MLIR compiler stack with 800+ CI-tested models
- [[Tenstorrent_Software_Stack]] — full layer map from UMD to framework
- [[Tenstorrent_Ascalon]] — RISC-V CPU IP entity page
- [[Blackhole_Architecture]] — detailed Blackhole chip specs
- [[Tenstorrent_Wormhole_n300]] — Wormhole hardware specs
- [[Tenstorrent_Grayskull]] — first-generation hardware
- [[Wormhole_Tensix_Processor]] — Tensix core microarchitecture
- [[FlashAttention_on_Tenstorrent_Wormhole_Optimization]] — SRAM-tiling optimization recipe
- [[Operator_Fusion_for_LLM_Inference_on_Tensix]] — LLM operator fusion recipe
- [[TT_Inference_Server_Benchmarking]] — inference server benchmark framework
- [[TT-QuietBox_2]] — RISC-V AI workstation product
