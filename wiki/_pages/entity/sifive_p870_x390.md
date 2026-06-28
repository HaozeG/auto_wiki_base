---
cold_start: false
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.cnx-software.com/2023/10/18/sifive-intelligence-x390-npu-performance-p870-risc-v-core/
- https://www.sifive.com/press/sifive-announces-differentiated-solutions-for-generative
- https://www.notebookcheck.net/SiFive-launches-Performance-P870-RISC-V-scalable-core-and-Intelligence-X390-NPU.759079.0.html
- https://www.sifive.com/cores/performance-p800
tags:
- risc-v
- processor
- AI-acceleration
- NPU
- SiFive
- out-of-order
- RVA23
type: entity
updated: 2026-06-27
---

# SiFive Performance P870 / Intelligence X390

The SiFive Performance P870 and Intelligence X390 NPU are a paired RISC-V CPU+NPU IP portfolio announced in October 2023, targeting high-performance edge AI and generative AI SoC designs. The P870 is a six-wide out-of-order RISC-V application core implementing the RVA23 profile, achieving 18 SPECint2000 points per MHz — approximately 50% higher single-thread performance than the prior SiFive Performance generation. It supports clustered configurations of up to 32 cores sharing a non-inclusive L3 cache, includes vector crypto and hypervisor extensions, and is qualified compatible with Google's Android on RISC-V platform requirements. Anticipated operating frequencies exceed 3 GHz. The paired X390 NPU is a vector coprocessor IP that quadruples sustained data bandwidth over the predecessor X280 by doubling the vector length to 1024-bit VLEN with 512-bit DLEN and adding dual vector ALUs; it connects to host CPUs via VCIX (Vector Coprocessor Interface eXtension) with 1024-bit inputs and 2048-bit outputs, enabling customers to attach additional custom acceleration hardware through the same interface. Combined P870+X390 system designs support up to 32 CPU cores plus 8 X390 accelerator cores alongside optional customer-defined VCIX accelerators, targeting generative AI inference at data-center edge.

## Key Claims

- P870: 6-wide out-of-order RISC-V core; RVA23 compliant; 18 SPECint2000/MHz; ~50% single-thread uplift over prior generation.
- P870 cluster: up to 32 cores with shared non-inclusive L3 cache; anticipated clock >3 GHz.
- P870 meets Google Android RISC-V platform requirements; includes hypervisor and vector crypto extensions.
- X390 NPU: 1024-bit VLEN, 512-bit DLEN, dual vector ALUs — 4× vector compute over predecessor X280.
- X390 connects via VCIX with 1024-bit input / 2048-bit output; supports custom customer-defined accelerator attachment.
- Combined SoC supports 32 P870 CPU cores + 8 X390 NPU cores + optional VCIX-custom accelerators.

## Relationships

- [[sifive_intelligence_x280]]: X390 is the direct successor to X280; doubles VLEN (512→1024-bit), adds dual ALU, quadruples bandwidth.
- [[risc_v_profiles_rva]]: P870 is RVA23-compliant, requiring full RVV 1.0 and hypervisor support as mandatory baseline.
- [[andes_ax45mp_nx27v]]: Andes NX27V and SiFive X390 are competing RISC-V vector NPU products compared in the andes_nx27v_sifive_p870_comparison page.
- [[ventana_veyron_v2]]: Both P870 and Veyron V2 target RVA23 server/edge deployments with large core counts.

## LLM Software Stack

SiFive has demonstrated end-to-end LLM inference on the X390 platform using a PyTorch-based workflow via SHARK-Turbine: `stateless_llm.py` compiles Hugging Face models into VMFB format, and `llm_runner.py` invokes the IREE runtime for inference. The full AI/ML software stack includes the SiFive LLVM compiler with micro-architecture-tuned codegen, the SiFive Kernel Library (SKL), SiFive System Software (FSFL and FSFM), and an IREE VCIX MLIR dialect that routes matrix-heavy operations to the X390's custom vector coprocessor interface. Performance profiling of TinyLlama on the X390 during the decode phase shows that matrix multiplication operations (GEMV pattern, M=1) account for over 95% of inference time. Alternative lightweight frameworks supported include customized TFLite with RVV optimizations, XNNPACK with RVV, ONNXRuntime, and llama.cpp with additional RVV patches.

## Sources

- https://www.cnx-software.com/2023/10/18/sifive-intelligence-x390-npu-performance-p870-risc-v-core/
- https://www.sifive.com/press/sifive-announces-differentiated-solutions-for-generative
- https://www.notebookcheck.net/SiFive-launches-Performance-P870-RISC-V-scalable-core-and-Intelligence-X390-NPU.759079.0.html
- https://www.sifive.com/cores/performance-p800
- https://www.sifive.com/blog/llm-optimization-and-deployment-on-sifive-intellig
