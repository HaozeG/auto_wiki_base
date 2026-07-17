---
canonical_name: NVIDIA DGX Spark
aliases:
- NVIDIA DGX Spark
- Project DIGITS
- DGX Spark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/219702dd7c33833d.md
- https://habr.com/ru/companies/x-com/articles/894152/
source_url: https://habr.com/ru/companies/x-com/articles/894152/
fetched_at: '2026-07-17T12:11:38.857017+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: nvidia_blackwell_ultra
  reason: The DGX Spark incorporates a Blackwell-architecture GPU with fifth-generation
    Tensor Cores and low-precision FP4 support, sharing the same architectural foundation
    as the NVIDIA Blackwell Ultra GPU, though implemented in a compact, low-power
    system-on-chip form factor for local AI inference
---

# NVIDIA DGX Spark

The NVIDIA DGX Spark, previously known as Project DIGITS, is a compact AI supercomputer designed and manufactured by NVIDIA for local execution of large artificial intelligence models. Weighing 1.2 kg and consuming up to 170 watts, it is built around the NVIDIA GB10 Grace Blackwell Superchip, which combines a Blackwell-architecture GPU with fifth-generation Tensor Cores supporting FP4 precision and a 20-core Arm CPU comprising ten Cortex-X925 performance cores and ten Cortex-A725 efficiency cores. The system integrates 128 GB of unified LPDDR5x memory with 273 GB/s bandwidth, up to 4 TB of NVMe SSD storage, and uses NVIDIA NVLink-C2C interconnect to achieve 900 GB/s chip-to-chip bandwidth with under 20 nanosecond latency. External connectivity includes four USB4 ports, HDMI 2.1a, a 10-gigabit Ethernet ConnectX-7 Smart NIC, Wi-Fi 7, and Bluetooth 5.3. The DGX Spark runs the NVIDIA DGX OS, a modified Ubuntu Linux distribution with the full CUDA-X AI stack, NIM microservices, and NVIDIA AI Enterprise platform. It can be clustered in pairs via the ConnectX-7 adapter for 200 Gb/s RDMA-attached scaling.

## Key Claims

- Delivers up to 1000 TOPS of AI inference performance.
- Uses the NVIDIA GB10 Grace Blackwell Superchip with a Blackwell GPU (fifth-generation Tensor Cores) and a 20-core Arm CPU (10x Cortex-X925 + 10x Cortex-A725).
- Supports FP4 (4-bit floating point) precision for reduced memory footprint and increased throughput.
- NVLink-C2C interconnect provides 900 GB/s chip-to-chip bandwidth with <20 ns latency.
- 128 GB unified LPDDR5x memory with 273 GB/s bandwidth.
- Up to 4 TB NVMe SSD storage.
- TDP of 170 W and weight of 1.2 kg.
- Includes four USB4, HDMI 2.1a, 10GbE ConnectX-7 Smart NIC, Wi-Fi 7, Bluetooth 5.3.
- Operates on NVIDIA DGX OS (Ubuntu-based) with CUDA-X AI, NIM, and NVIDIA AI Enterprise.
- Supports clustering two units over ConnectX-7 at 200 Gb/s with RDMA.

## Relationships

- [[nvidia_blackwell_ultra]]: The DGX Spark incorporates a Blackwell-architecture GPU with fifth-generation Tensor Cores and low-precision FP4 support, sharing the same architectural foundation as the NVIDIA Blackwell Ultra GPU, though implemented in a compact, low-power system-on-chip form factor for local AI inference.

## Sources

- [NVIDIA DGX Spark: карманный суперкомпьютер для ИИ... / Хабр](raw/cache/219702dd7c33833d.md)
