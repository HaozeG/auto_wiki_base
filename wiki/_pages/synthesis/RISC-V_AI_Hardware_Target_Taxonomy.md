---
cold_start: true
connected_entities:
- XuanTie_C908
- XuanTie_C910
- SpacemiT_KeyStone_K1
- MilkV_Pioneer
- SiFive_Intelligence_X390
- GAP8_PULP_Processor
- Kendryte_K210
- Gemmini_Architecture
- Sipeed_LicheePi_4A
- Kendryte_K230_SoC
- SiFive_Performance_P870
- Ara_simulator
created: 2026-06-29
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.9
  contradiction_potential: 0.5
  cross_domain_connection: 0.85
sources:
- wiki/_pages/hardware_target/XuanTie_C908.md
- wiki/_pages/hardware_target/XuanTie_C910.md
- wiki/_pages/hardware_target/SpacemiT_KeyStone_K1.md
- wiki/_pages/hardware_target/MilkV_Pioneer.md
- wiki/_pages/hardware_target/SiFive_Intelligence_X390.md
- wiki/_pages/hardware_target/GAP8_PULP_Processor.md
- wiki/_pages/hardware_target/Kendryte_K210.md
- wiki/_pages/hardware_target/Gemmini_Architecture.md
- wiki/_pages/entity/Sipeed_LicheePi_4A.md
- wiki/_pages/hardware_target/Kendryte_K230_SoC.md
- wiki/_pages/hardware_target/SiFive_Performance_P870.md
- wiki/_pages/hardware_target/Ara_simulator.md
synthesis_status: active
type: synthesis
updated: 2026-06-29
---

# RISC-V AI Hardware Target Taxonomy

## RAG Summary

RISC-V AI hardware targets as of mid-2026 span four distinct tiers differentiated by power envelope, vector ISA version, NPU integration, and target deployment context. The ultra-low-power IoT tier includes GAP8 (9 cores, no RVV, explicit DMA scratchpad, INT8 dot-product support, GreenWaves) and Kendryte K210 (dual RISC-V, KPU NPU, 28nm TSMC, 400 MHz, 8 MB SRAM). The edge AI SoC tier includes Kendryte K230 (KPU successor, enhanced NPU), SpacemiT KeyStone K1 (8 × SpacemiT X60, RVA22, 2.0 TOPS NPU, 1.6 GHz), and the TH1520 SoC powering Sipeed LicheePi 4A (XuanTie C910 × 4, RVV 0.7.1, 4 TOPS NPU). The high-performance application processor tier includes XuanTie C908 (9-stage in-order, RVV 1.0, 12nm TSMC, 52.8 mW/GHz) and XuanTie C910 (3-wide OOO, RVV 0.7.1, 2.0–2.5 GHz, open-sourced RTL). The research accelerator tier includes Gemmini (UC Berkeley, systolic/vector array DNN generator, 16nm and 22nm tapeouts, TVM integration) and SiFive Intelligence X390 (512-bit vectors, dual vector ALUs, VCIX custom extensions). A key unresolved contradiction: RVV 0.7.1 (C910, TH1520) and RVV 1.0 (C908, K1) are ABI-incompatible; binary distributions targeting one will not run on the other without recompilation.

---

## Full Synthesis

### Tier 1 — Ultra-Low-Power IoT

**[[GAP8_PULP_Processor]]** (GreenWaves, PULP project): 1 fabric controller + 8 compute cores, all RISC-V RV32IMC (no RVV). Uses a four-level scratchpad memory hierarchy with explicit DMA rather than hardware-managed caches. Provides INT8 dot-product instructions for neural network acceleration. Power target: IoT edge nodes. Key constraint: no hardware cache coherency; all data transfers between memory levels are software-managed via DMA.

**[[Kendryte_K210]]**: Dual 64-bit RISC-V (RV64GC), no RVV, 400 MHz, 28nm TSMC, 8 MB on-chip SRAM. Integrates a KPU (Knowledge Processing Unit) for CNN acceleration. Widely deployed in Sipeed MAIX-series edge AI boards. Key constraint: small SRAM limits model size; KPU supports only specific layer types.

### Tier 2 — Edge AI SoCs

**[[Kendryte_K230_SoC]]**: Successor to K210 with enhanced dual-core RISC-V and an improved NPU (KPU). Targets camera-based edge AI (computer vision at the edge).

**[[SpacemiT_KeyStone_K1]]**: 8 × SpacemiT X60 cores, RVA22 profile (RVV 1.0 compliant), 2.0 TOPS dedicated neural engine, 1.6 GHz. Used in Banana Pi BPI-F3 and BPI-CM6. Open-ecosystem focus with global RISC-V software infrastructure support.

**[[Sipeed_LicheePi_4A]]**: Single-board computer built on the TH1520 SoC (4 × XuanTie C910 + 4 TOPS NPU). RVV 0.7.1 ISA. Target for llama.cpp, ncnn, and MNN inference benchmarks; measured ~3–5 tokens/s for small LLMs.

### Tier 3 — High-Performance Application Processors

**[[XuanTie_C908]]** (T-Head/Alibaba): 9-stage dual-issue in-order, RVV 1.0, RVA22, TSMC 12nm, 52.8 mW/GHz/core, 24–64% improvement over C906 on synthetic benchmarks. Configurable 1–4 core clusters with hardware cache coherency.

**[[XuanTie_C910]]**: 3-wide out-of-order, RVV 0.7.1 (pre-ratification), TSMC 12nm (2.0–2.5 GHz) and 7nm (2.8 GHz), 0.8 mm²/core, ~0.2W at 2 GHz. Open-sourced RTL via T-Head Open Chip Community. The MilkV Pioneer's SG2042 uses 64 × C910-class cores and achieves server-class RISC-V compute.

**[[MilkV_Pioneer]]**: 64-core RISC-V workstation, 125 GB RAM, RVV (reported as RVV 0.7.1 on SG2042), no GPU. Supports llama.cpp LLM inference via GGML_CPU_AARCH64=ON build path. Largest memory footprint of any RISC-V AI inference board in this wiki.

**[[SiFive_Performance_P870]]**: High-performance application processor core with SiFive's vector ISA. Targets the performance tier above the X390.

### Tier 4 — Research and Academic Accelerators

**[[Gemmini_Architecture]]** (UC Berkeley): Open-source DNN accelerator generator producing ASIC or FPGA targets. Supports systolic and vector array configurations, output-stationary and weight-stationary dataflows, INT8 and FP datatypes. Fabricated in TSMC 16nm and Intel 22nm; measured 2670× speedup over high-performance CPUs on DNN benchmarks. Integrates with TVM and ONNX Runtime via onnxruntime-riscv.

**[[Ara_simulator]]**: Research vector processor simulator, used for evaluating RVV microarchitecture choices without silicon.

### Key Contradictions

- **RVV version fragmentation**: C910/TH1520/MilkV-Pioneer-SG2042 use RVV 0.7.1; C908/SpacemiT K1 use RVV 1.0. Software compiled for one is binary-incompatible with the other. No current page documents a unified binary distribution that handles both.
- **NPU integration diversity**: GAP8 and Gemmini use separate accelerator buses (DMA/RoCC); K210/K230 integrate a fixed KPU; SpacemiT K1 uses a separate neural engine. There is no standard RISC-V NPU programming interface — each accelerator requires its own driver/runtime.
- **Memory architecture gap**: GAP8's scratchpad-only hierarchy fundamentally differs from the hardware-coherent caches of C908/C910/SpacemiT K1. Algorithms optimized for scratchpad DMA transfer patterns will not benefit from the cache hierarchy of the higher tiers.

## Open Questions

- Does the SpacemiT K1 neural engine (2.0 TOPS) outperform the XuanTie C908's RVV path for INT8 CNN inference, and by how much?
- Is there a published cross-board benchmark using the same model and runtime (e.g., ncnn + MobileNetV2 INT8) across K1, LicheePi 4A, MilkV Pioneer, and GAP8?
- When will the SG2042 (MilkV Pioneer) formally confirm RVV 1.0 support, and does the current RVV 0.7.1 claim in the wiki need correction?
- Does the Gemmini systolic array outperform the SpacemiT K1 neural engine at comparable die area and power?

## Connected Pages

- [[XuanTie_C908]]
- [[XuanTie_C910]]
- [[SpacemiT_KeyStone_K1]]
- [[MilkV_Pioneer]]
- [[SiFive_Intelligence_X390]]
- [[GAP8_PULP_Processor]]
- [[Kendryte_K210]]
- [[Gemmini_Architecture]]
- [[Sipeed_LicheePi_4A]]
- [[Kendryte_K230_SoC]]
- [[SiFive_Performance_P870]]
- [[Ara_simulator]]
