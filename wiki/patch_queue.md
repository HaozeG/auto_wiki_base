# Wiki Patch Queue

## [2026-07-02] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908 MLPerf tiny inference vs C906
source: https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
status: pending_review
<!-- merge_draft_body
# XuanTie C908 MLPerf tiny inference vs C906

The XuanTie C908 achieves up to 3.5 times the inference performance of the XuanTie C906 on the MLPerf Tiny v0.7 benchmark, as reported by T-Head Semiconductor. The C908 runs at up to 2 GHz on TSMC 12nm and includes an optional Vector Processing Unit with INT4 data type support and vector dot product extensions. The C906 is a lower-cost single-issue in-order core. This benchmark result demonstrates the ML acceleration improvements of the C908 pipeline, instruction fusion, and data prefetching technologies, along with the HHB and SHL software libraries.

## Key Claims

- XuanTie C908 outperforms XuanTie C906 by up to 3.5× on MLPerf Tiny v0.7 inference tasks.
- The gain is attributed to architectural innovations (9-stage dual-issue pipeline, instruction fusion, data prefetching, vector unit with INT4).
- The comparison is at same frequency and process (TSMC 12nm).
- Source: T-Head Semiconductor official blog post, evidence strength: reported.

## Measurement Context

- Hardware version: XuanTie C908 (9-stage dual-issue in-order, 2 GHz, TSMC 12nm) vs XuanTie C906 (single-issue in-order).
- Software/toolchain version: MLPerf Tiny v0.7; HHB inference deployment tool; SHL computing library; Linux kernel 5.19+.
- Workload shape: MLPerf Tiny v0.7 inference (exact model/layer details not provided).
- Metric: Ratio of inference performance (e.g., throughput or latency improvement); up to 3.5×.
- Method: Reported from vendor blog post; no independent verification or detailed methodology disclosed.
- Evidence strength: reported

## Relationships

- [[xuantie-c908]]: The hardware target whose benchmark result is reported.
- [[cpa-factored-gemmini-systolic-array]]: Another optimization for RISC-V AI accelerators; no direct connection but contextually relevant to the AI acceleration theme.

## Sources

- [XuanTie C908 blog post on RISC-V International](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
merge_draft_body -->
