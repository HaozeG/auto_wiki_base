---
type: entity
tags: []
sources:
  - https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
  - https://www.cnx-software.com/2023/10/18/sifive-intelligence-x390-npu-performance-p870-risc-v-core/
  - https://www.sifive.com/cores/performance-p800
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AndesCore NX27V vs SiFive Intelligence P870

The AndesCore NX27V and SiFive Intelligence P870 represent two fundamentally different architectural approaches to RISC-V AI acceleration, making a direct "apples-to-apples" comparison misleading. The NX27V is a dedicated vector processor built around the RISC-V Vector Extension (RVV 1.0, VLEN up to 512 bits) with a 5-stage in-order pipeline optimized for data-parallel throughput — it is primarily a compute engine rather than a general-purpose Linux-capable application core. The SiFive P870, by contrast, is a full 6-wide out-of-order 64-bit application processor targeting RVA23 profile compliance with a 128-bit VLEN vector unit, designed to run rich OS stacks (Linux, Android) in datacenter, automotive, and consumer SoCs. For AI workloads specifically, the P870 is designed to be paired with the separate SiFive Intelligence X390 NPU (1024-bit VLEN, dual vector ALUs), while the NX27V handles vector acceleration on-die without a separate NPU. The NX27V has achieved silicon validation in the QiLai SoC and targets edge AI, ADAS sensor processing, and IoT gateways. The P870 excels in throughput-oriented general compute and serves as a Linux-capable host that offloads heavy AI to dedicated accelerators. This comparison illuminates a broader RISC-V ecosystem pattern: dedicated vector processors vs. general-purpose cores with accelerator interfaces.

## Key Claims

- The AndesCore NX27V implements RVV 1.0 with a configurable VLEN up to 512 bits and a 5-stage in-order dual-issue pipeline, while the SiFive P870 is a 6-wide out-of-order core with a fixed 128-bit VLEN vector unit.
- The NX27V achieved silicon validation in the Andes QiLai SoC (2024) which integrates the NX27V vector core alongside AX45MP application cores, whereas the P870 was announced in October 2023 with RVA23 compliance and is targeting customer tape-outs.
- SiFive designed the P870 to pair with the separate X390 NPU (1024-bit VLEN, 4× vector computation improvement over the prior X280) for generative AI workloads, while the NX27V handles vector acceleration natively without an external NPU dependency.
- The NX27V achieves up to 6.4 GFLOPS/W (FP32) in its 512-bit VLEN configuration on TSMC 12nm, whereas SiFive does not publish standalone TOPS or GFLOPS metrics for the P870 core itself — AI throughput depends on the companion X390 NPU.
- Both cores support the ratified RVV 1.0 specification, but the NX27V can be configured with wider vector datapath (512-bit vs. 128-bit), giving it higher single-core vector throughput for HPC-style vector workloads.
- The P870 supports up to 32-core clusters with shared L3 cache and can scale to 256 cores via CHI interconnect, while the NX27V is typically deployed as one or two vector cores alongside scalar application cores in heterogeneous SoCs.

## Relationships

- [[risc_v_vector_extension]]: Both cores implement RVV 1.0 but with different VLEN configurations — this contrast illustrates how the same ISA specification maps to divergent microarchitectural choices.
- [[andes_ax45mp_nx27v]]: The NX27V is detailed further in the Andes portfolio page; the QiLai SoC pairs it with AX45MP cores.
- [[sifive_intelligence_x280]]: The X280 is the predecessor NPU to the X390 that pairs with the P870, establishing the SiFive AI product family lineage.
- [[riscv_matrix_extension]]: Both companies participate in the AME Task Group; SiFive's February 2025 AME proposal directly informs future iterations of both product lines.

## Sources

- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
- https://www.cnx-software.com/2023/10/18/sifive-intelligence-x390-npu-performance-p870-risc-v-core/
- https://www.sifive.com/cores/performance-p800
