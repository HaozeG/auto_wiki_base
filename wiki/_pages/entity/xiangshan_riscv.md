---
cold_start: false
created: 2026-06-27
inbound_links: 6
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://github.com/OpenXiangShan/XiangShan
- https://www.cnx-software.com/2021/07/05/xiangshan-open-source-64-bit-risc-v-processor-rival-arm-cortex-a76/
- https://english.cas.cn/newsroom/cas-in-media/202603/t20260330_1154281.shtml
- https://hackaday.com/2025/01/03/high-performance-risc-v/
tags:
- risc-v
- open-source
- high-performance
- out-of-order
- china
- cas
type: entity
updated: 2026-06-27
---

# XiangShan (香山)

XiangShan is an open-source, high-performance out-of-order 64-bit RISC-V processor developed by the Institute of Computing Technology, Chinese Academy of Sciences (ICT-CAS) and Peng Cheng Laboratory. Written in the Chisel hardware description language and released under the Mulan PSL v2 license, XiangShan is designed to push the performance frontier of open-source RISC-V to commercial-grade levels, targeting applications in AI inference, cloud computing, and industrial control. It is the highest-performance open-source RISC-V processor publicly benchmarked as of 2025, achieving 16.5 SPEC CPU2006 points per GHz on a 28nm first-generation implementation.

## Key Claims

- Achieves 16.5 SPEC CPU2006 points/GHz, placing it competitively with ARM Cortex-A76 class cores in single-threaded workload throughput.
- First-generation Yanqihu implementation features an 11-stage pipeline, 6-wide issue, and 4 memory access units, fabricated at 28 nm with a clock frequency of up to 1.3 GHz.
- Planned 14 nm iteration targets 2 GHz, with potential for A76-equivalent multi-GHz performance after process scaling.
- Implements the RV64GC ISA with vector extensions; the Nanhu generation adds matrix instruction extensions (vector dot product) for LLM acceleration experiments.
- L2 cache is 2 MB; supports up to 32 GB DDR4 memory and includes PCIe connectivity.
- Active development branches include Yanqihu (first generation), Nanhu (second generation, process-improved), and Kunminghu (third generation, in development as of 2025).
- The repository on GitHub (OpenXiangShan/XiangShan) is among the most-starred open-source processor projects; the project is part of China's push for domestic RISC-V ecosystem independence.

## Relationships

- [[boom_riscv]]: Both are open-source out-of-order RISC-V processors written in Chisel; XiangShan targets higher absolute performance while BOOM prioritizes parameterizability and academic research.
- [[risc_v_vector_extension]]: XiangShan Nanhu integrates RVV and experimental matrix extensions for AI workloads.
- [[alibaba_xuantie_c910_c920]]: XiangShan and XuanTie C910/C920 represent competing Chinese high-performance RISC-V strategies — open-source academic vs. commercial IP.

## Sources

- GitHub: https://github.com/OpenXiangShan/XiangShan
- CNX Software overview: https://www.cnx-software.com/2021/07/05/xiangshan-open-source-64-bit-risc-v-processor-rival-arm-cortex-a76/
- CAS announcement 2026: https://english.cas.cn/newsroom/cas-in-media/202603/t20260330_1154281.shtml
- Hackaday 2025 overview: https://hackaday.com/2025/01/03/high-performance-risc-v/
