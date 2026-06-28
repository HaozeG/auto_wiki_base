---
cold_start: false
connected_entities:
- muriscv_nn
- riscv_zve_sub_extensions
- canaan_kendryte_k510_k230
- pulp_platform
- onnx_runtime_riscv
- llm_inference_riscv
- milkv_pioneer_duo
- riscv_sparse_computation
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  contradiction_potential: null
  cross_domain_connection: null
sources:
- entity/muriscv_nn.md
- entity/riscv_zve_sub_extensions.md
- entity/canaan_kendryte_k510_k230.md
- entity/pulp_platform.md
- entity/onnx_runtime_riscv.md
- entity/llm_inference_riscv.md
- entity/milkv_pioneer_duo.md
- entity/riscv_sparse_computation.md
synthesis_status: draft
type: synthesis
updated: 2026-06-27
---

# RISC-V AI at the Edge: from muRISCV-NN to LLM Inference on Embedded and Server RISC-V

## RAG Summary
<!-- 150-250 words, self-contained, no dangling refs, names ≥2 entities, first sentence = core claim -->

The RISC-V AI software stack spans a continuous spectrum from microcontroller-class tinyML to server-class large language model inference, unified by the RISC-V Vector Extension (RVV) as the primary hardware abstraction. At the embedded end, muRISCV-NN provides CMSIS-NN-compatible INT8 and INT4 kernels optimized for RVV-capable cores, achieving a 3.85× ResNet speedup and 60% improvement over LLVM auto-vectorization for convolutional layers. The Zve32x and Zve64x sub-extension profiles (ratified as part of the RVV 1.0 family) allow MCU-class processors to implement partial vector support, enabling tinyML inference on chips like the Canaan Kendryte K230 (dual XuanTie C908, 6 TOPS KPU, 12nm) without full application-class cores. The PULP Platform pushes further, with the Darkside processor reaching 835 GOPS/W for sub-byte quantized inference on ultra-low-power RISC-V clusters using xPULP ISA extensions. ONNX Runtime provides a vendor-neutral deployment path through its RV64 CPU execution provider, bridging model export from training frameworks to any compliant RISC-V target. At the server end, the Milk-V Pioneer (SOPHGO SG2042, 64-core XuanTie C920) enables LLM inference via llama.cpp with RVV support: V-Seek (2025) achieves 4.32 token/s on DeepSeek R1 Distill Llama 8B. Sparse computation via RVV mask registers adds 25–33% structured-sparsity speedups. The unifying trend is that RISC-V's open extensibility allows each layer — ISA, kernel library, compiler runtime, model format — to be independently optimized, from milliwatt MCUs to 64-core workstations.

---

## Full Synthesis

### The Inference Spectrum

RISC-V AI inference splits naturally into three tiers by compute budget and model complexity:

**Tier 1 — Microcontroller / TinyML (<1W):** The RISC-V Zve sub-extensions (Zve32x, Zve64x) define minimal vector profiles for MCU-class cores. muRISCV-NN targets exactly this tier with hand-tuned RVV kernels for convolution, depthwise conv, and fully-connected layers at INT8/INT4 precision. The PULP Platform's xPULP extensions achieve sub-byte (2-bit, 4-bit) inference at 835 GOPS/W on specialized RISC-V clusters, the current efficiency frontier for MCU-class RISC-V AI.

**Tier 2 — Edge SoC (1–10W):** Canaan K230 (dual C908, 6 TOPS KPU, 12nm), StarFive JH7110 (NVDLA + NNE), and the T-Head TH1520 (4 TOPS NPU) represent production RISC-V SoCs shipping with dedicated AI acceleration. These chips run ONNX Runtime or vendor SDKs; ONNX Runtime's CPU execution provider with RVV microkernel support provides a portable path when proprietary NPU SDKs are absent.

**Tier 3 — Server / LLM (>100W):** The SOPHGO SG2042 (64-core C920, inside Milk-V Pioneer) is the first widely available many-core RISC-V workstation. V-Seek (arXiv 2503.17422) shows 2.9–3.0× speedup for LLM reasoning via custom memory layout and RVV-optimized attention kernels in llama.cpp, reaching 4.32 token/s on Llama 8B.

### Connecting Threads

**Quantization continuity:** muRISCV-NN's INT8/INT4 kernels, PULP-NN's sub-byte inference, and llama.cpp's GGUF quantization formats (Q4_K, Q8_0) all exploit RISC-V's vector mask register and integer arithmetic to reduce compute without custom silicon.

**Sparsity as a next frontier:** RVV mask operations naturally support unstructured sparse inference; structured sparsity shows 25–33% speedups on existing RVV hardware. Neither muRISCV-NN nor llama.cpp currently implements full sparse kernels, leaving a software gap.

**Compiler path divergence:** muRISCV-NN uses hand-written intrinsics; ONNX Runtime uses auto-vectorized microkernel dispatch; llama.cpp uses manual RVV assembly. There is no single compiler-generated kernel library serving all three tiers, which represents a fragmentation risk as RISC-V AI workloads scale.

## Open Questions

- Can muRISCV-NN's kernel library be extended upward to serve Tier 2 SoCs (K230, JH7110) as a unified portable layer?
- Will the RISC-V Matrix Extension (AME) supersede all current software-optimization approaches for LLM attention layers?
- Does the V-Seek LLM benchmark (4.32 token/s on Llama 8B) improve substantially with AME silicon, and by what factor?
- What is the power efficiency crossover point where a RISC-V cluster (PULP/Darkside-style) outperforms a dedicated NPU for INT8 inference?
- Does the sparse computation research (arXiv 2501.10189) translate to measurable gains in llama.cpp's attention or FFN layers on SG2042?

## Connected Pages

- [[muriscv_nn]] — CMSIS-NN-compatible INT8/INT4 kernels for RVV; 3.85× ResNet speedup
- [[riscv_zve_sub_extensions]] — Embedded RVV sub-profiles enabling Tier 1 tinyML on MCUs
- [[canaan_kendryte_k510_k230]] — K230 Tier 2 SoC with 6 TOPS KPU and dual C908 RVV 1.0 cores
- [[pulp_platform]] — Darkside 835 GOPS/W sub-byte inference frontier
- [[onnx_runtime_riscv]] — Portable model deployment via ONNX RT CPU EP with RVV
- [[llm_inference_riscv]] — llama.cpp + V-Seek LLM benchmarks on SG2042
- [[milkv_pioneer_duo]] — SG2042 hardware platform for Tier 3 LLM experiments
- [[riscv_sparse_computation]] — RVV mask-based sparsity, 25–33% structured-sparse speedup
