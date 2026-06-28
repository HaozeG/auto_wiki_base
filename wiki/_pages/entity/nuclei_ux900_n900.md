---
cold_start: true
created: 2026-06-27
inbound_links: 2
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.nucleisys.com/product/rvipes/ux900/
- https://www.nucleisys.com/product/rvipes/n900/
- https://www.riscvschool.com/2023/02/18/nuclei-risc-v-900-series-processors/
- https://riscv.org/blog/nuclei-system-technology-releases-ux1030h-with-full-support-for-rva23/
tags:
- risc-v
- commercial-ip
- china
- embedded
- aiot
- nuclei
type: entity
updated: 2026-06-27
---

# Nuclei UX900 / N900

The Nuclei 900 series (N900 and UX900) is a commercial RISC-V processor IP family from Nuclei System Technology, a Chinese IP vendor targeting AIoT edge computing, industrial control, and Linux-capable embedded SoCs. The 900 series sits at the high-performance end of Nuclei's catalog, positioned as replacements for ARM Cortex-A35/A53/A55 (UX900) and Cortex-M7/R7/R8 (N900). Nuclei reports nearly 1 billion cumulative RISC-V core shipments across its product line and counts over 300 customers, making it one of the highest-volume RISC-V IP vendors in China.

## Key Claims

- N900 is a 32-bit dual-issue, in-order 9-stage Harvard pipeline processor implementing RV32 IMACP + B/K/P/V extensions, targeting RTOS-class real-time embedded applications.
- UX900 is the 64-bit variant with MMU, implementing RV64 IMACFDPV + B/K/P extensions, enabling Linux deployment for AIoT edge gateways and data processing nodes.
- Both N900 and UX900 support configurable RVV (RISC-V Vector Extension) with VLEN options of 128, 256, or 512 bits and matching DLEN (data path width) configurations.
- Floating-point support covers double, single, and half-precision (FP64/FP32/FP16), with DSP extensions included for SIMD/packed arithmetic workloads.
- Security features include TEE (Trusted Execution Environment) and automotive safety compliance: ASIL-B and ASIL-D certifications, extending the 900 series into safety-critical markets.
- UX900 supports up to 4 cores in multiprocessor configurations; MMU enables standard Linux kernel and OS deployment.
- Nuclei's newer UX1030H (successor generation) achieved full RVA23 profile compliance, including mandatory Zvfhmin and Zihintntl extensions, signaling the 900 series' migration path to ratified RISC-V profiles.

## Relationships

- [[risc_v_vector_extension]]: UX900 and N900 implement RVV with configurable VLEN 128–512 bits; software uses standard RVV 1.0 intrinsics.
- [[risc_v_p_extension]]: Both cores include the RISC-V P (packed SIMD) extension for lightweight DSP workloads alongside the vector unit.
- [[alibaba_xuantie_c910_c920]]: Nuclei and Alibaba XuanTie represent the two dominant Chinese commercial RISC-V IP strategies — Nuclei focuses on IoT/embedded volume, XuanTie on high-performance application processors.

## Sources

- UX900 product page: https://www.nucleisys.com/product/rvipes/ux900/
- N900 product page: https://www.nucleisys.com/product/rvipes/n900/
- 900 series overview: https://www.riscvschool.com/2023/02/18/nuclei-risc-v-900-series-processors/
- UX1030H RVA23 blog: https://riscv.org/blog/nuclei-system-technology-releases-ux1030h-with-full-support-for-rva23/
