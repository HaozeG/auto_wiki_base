---
cold_start: true
created: 2026-06-27
inbound_links: 5
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.theregister.com/2026/03/25/alibaba_damo_xuantie_c950_chip/
- https://www.cnx-software.com/2026/03/25/alibaba-xuantie-c950-a-powerful-rva2364-bit-risc-v-core-for-edge-ai-computing/
- https://www.aibase.com/news/26500
- https://awesomeagents.ai/news/alibaba-xuantie-c950-risc-v-llm-inference/
tags:
- risc-v
- AI-acceleration
- processor
- LLM-inference
- alibaba
type: entity
updated: 2026-06-27
---

# Alibaba XuanTie C950

The Alibaba XuanTie C950, unveiled on March 24, 2026 at a RISC-V ecosystem conference in Shanghai, is a high-performance 64-bit out-of-order superscalar RISC-V server processor core developed by Alibaba's T-Head semiconductor division. Built on TSMC's 5nm process and clocked at 3.2 GHz, it is the first RISC-V CPU explicitly architected for large language model (LLM) native inference, supporting models including Qwen3-256B-A22B and DeepSeek V3-671B. The C950 is fully RVA23-profile compliant and extends the base ISA with Alibaba's proprietary Attached Matrix Extension (AME) and Tensor Processing Engine (TPE) integration, delivering 8 TOPS per TPE instance.

## Key Claims

- The C950 scores over 70 points on SPECint2006 single-core, a world record for RISC-V architecture at time of announcement, representing a 3× performance improvement over its predecessor, the C920.
- The chip is fabricated on TSMC 5nm with an 8-instruction decode width and a 16-stage pipeline, operating at 3.2 GHz; memory bandwidth increased 4× compared to the C920.
- The TPE acceleration engine supports data types from FP16 down to INT4 and FP8, plus micro-scaling formats MXFP8, MXFP4, and RVFP4 (Alibaba's custom format), delivering 8 TOPS per TPE unit.
- The C950 implements the proprietary XuanTie AME (Attached Matrix Extension) ISA for matrix-heavy AI workloads on top of standard RVV 1.0.
- In multi-processor mode the C950 uses the XL-300 interconnect to form clusters of up to 8 cores with a 4-cycle load-to-use L1 data cache latency.
- The chip supports Qwen3-256B-A22B and DeepSeek V3-671B inference natively, establishing RISC-V as a viable platform for frontier-scale LLM deployment outside x86/Arm ecosystems.

## Relationships

- [[risc_v_vector_extension]] — C950 implements RVA23 (mandatory RVV 1.0) plus the proprietary AME matrix extension
- [[alibaba_xuantie_c910_c920]] — C950 is the third generation, succeeding C910 (RVV 0.7.1) and C920 (RVV 1.0)

## Sources

- The Register announcement: https://www.theregister.com/2026/03/25/alibaba_damo_xuantie_c950_chip/
- CNX Software specs breakdown: https://www.cnx-software.com/2026/03/25/alibaba-xuantie-c950-a-powerful-rva2364-bit-risc-v-core-for-edge-ai-computing/
- SPECint record: https://www.aibase.com/news/26500
- LLM inference context: https://awesomeagents.ai/news/alibaba-xuantie-c950-risc-v-llm-inference/
