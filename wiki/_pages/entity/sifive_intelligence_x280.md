---
cold_start: true
created: 2026-06-27
inbound_links: 5
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.sifive.com/blog/introduction-to-the-sifive-intelligence-x280
- https://www.cnx-software.com/2021/04/27/sifive-intelligence-x280-64-bit-risc-v-processor-integrates-ai-extensions/
- https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
- https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
tags:
- risc-v
- processor
- vector-processing
- AI-acceleration
- embedded
type: entity
updated: 2026-06-27
---

# SiFive Intelligence X280

The SiFive Intelligence X280 is a 64-bit RISC-V application processor IP core from SiFive designed for AI, ML, and high-performance embedded workloads. It is an 8-stage dual-issue in-order superscalar core with a 512-bit vector register length (VLEN) and 256-bit data path width (DLEN), implementing RVV 1.0 with 32 physical vector registers and support for logical vector widths up to 4096 bits via LMUL=8 grouping. SiFive markets the X280 as the centerpiece of its Intelligence processor family, which targets autonomous vehicles, edge AI servers, and HPC DSPs. A second-generation X280 Gen 2 was introduced in September 2025, adding support for FP4 and FP8 datatypes alongside a wider range of cache options to address emerging LLM and diffusion model workloads.

## Key Claims

- The X280 features a 512-bit VLEN with 32 vector registers, supporting logical LMUL=8 operations equivalent to 4096-bit vector widths, enabling high-throughput SIMD on compute-dense AI kernels.
- SiFive Intelligence Extensions for ML support BF16, FP16, FP32, FP64, and INT8–INT64 fixed-point datatypes, delivering 12× faster inference compared to RISC-V cores without Intelligence Extensions on the same benchmark suite.
- Multi-core X280 complexes scale to 16 cache-coherent cores, supporting shared L2 configurations suitable for embedded AI inference clusters.
- The X280 introduced the Vector Coprocessor Interface Extension (VCIX), allowing SoC designers to attach custom accelerator datapaths to the X280 pipeline and access them through standard RISC-V vector instruction slots without additional bus transactions.
- The second-generation X280 Gen 2 (announced September 2025) adds FP4 and FP8 datatype support, targeting the precision requirements of quantized large language model inference on edge devices.

## Relationships

- [[risc_v_vector_extension]] — X280 implements RVV 1.0 with 512-bit VLEN and VCIX custom extension interface
- [[tvm_riscv_backend]] — SiFive X280 is a target platform for TVM-based RVV kernel auto-tuning

## Sources

- SiFive X280 introduction: https://www.sifive.com/blog/introduction-to-the-sifive-intelligence-x280
- VCIX extension announcement: https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
- Gen 2 announcement: https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
