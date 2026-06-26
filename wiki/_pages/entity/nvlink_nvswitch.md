---
type: entity
tags: [interconnect, hardware, nvidia, multi-gpu, networking]
sources:
  - https://www.nvidia.com/en-us/data-center/nvlink/
  - https://hc2022.hotchips.org/
  - https://ieeexplore.ieee.org/document/nvswitch2022
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# NVLink / NVSwitch

NVLink is NVIDIA's proprietary high-bandwidth, low-latency GPU-to-GPU interconnect introduced in 2016 as a direct response to the bandwidth bottleneck imposed by PCIe for multi-GPU training workloads. Unlike PCIe — which routes all inter-GPU traffic through the CPU's root complex — NVLink creates point-to-point electrical links between GPU dies, or between a GPU and a compatible CPU (in the case of IBM POWER9 and later Grace), enabling cache-coherent memory access across devices. NVSwitch is a companion switching chip that extends NVLink into a non-blocking all-to-all fabric, allowing every GPU in a server node to communicate with every other GPU at full bandwidth simultaneously. NVLink has evolved through four generations: NVLink 1.0 (2016, 160 GB/s bidirectional per GPU), NVLink 2.0 (2018, 300 GB/s), NVLink 3.0 (2020, 600 GB/s), and NVLink 4.0 (2022, 900 GB/s bidirectional per GPU). For comparison, PCIe 5.0 ×16 provides only 128 GB/s bidirectional, making NVLink 4.0 approximately 7× faster for inter-GPU traffic. NVSwitch enables the DGX H100 eight-GPU node to expose a 640 GB unified memory pool at 900 GB/s per GPU, which is essential for fitting models that exceed single-GPU HBM capacity, including large language models with hundreds of billions of parameters.

## Key Claims

- NVLink 4.0 delivers 900 GB/s bidirectional bandwidth per GPU, compared to 128 GB/s for PCIe Gen5 ×16, a 7× bandwidth advantage for GPU-to-GPU traffic.
- The DGX H100 system uses four third-generation NVSwitch chips to create a fully non-blocking all-to-all fabric connecting eight H100 GPUs; aggregate switch bisection bandwidth is 3.6 TB/s.
- NVLink supports unified virtual addressing across connected GPUs, allowing a CUDA kernel on one GPU to directly read or write memory on a peer GPU without explicit data copies.
- NVLink 3.0 (Ampere generation) introduced NVLink Sharp, an in-network collective operations unit capable of performing reductions (AllReduce, AllGather) inside the switch fabric rather than in GPU cores, reducing training communication overhead.
- Each NVLink 4.0 link consists of two sub-links of 25 lanes each at 50 Gbps per lane (PAM4 signaling), and each H100 GPU exposes 18 NVLink 4.0 links (900 GB/s aggregate).
- NVSwitch 3.0, paired with H100, reduced all-to-all latency to approximately 1 µs for small messages, enabling fine-grained pipeline parallelism strategies that were impractical with Ethernet-based clusters.
- NVIDIA's NVLink-C2C variant (used in the Grace Hopper Superchip) connects a Grace CPU to an H100 GPU at 900 GB/s with full cache coherence, allowing the CPU and GPU to share a unified 480 GB+ memory pool spanning LPDDR5X and HBM3.

## Relationships

- [[nvidia_hopper_h100]] — H100 is the primary GPU deploying NVLink 4.0 and NVSwitch 3.0; all DGX H100 and HGX H100 configurations depend on NVSwitch for the unified memory fabric.
- [[hbm_high_bandwidth_memory]] — NVLink enables the aggregation of per-GPU HBM pools across a node; NVSwitch fabric bandwidth must be provisioned relative to aggregate HBM bandwidth to avoid becoming the bottleneck.
- [[google_tpu]] — Google TPU pods use a proprietary ICI (Inter-Chip Interconnect) fabric that serves the same architectural function as NVLink/NVSwitch but is custom-built for TPUs.
- [[amd_mi300x]] — AMD's competing solution uses Infinity Fabric for inter-die communication within MI300X but relies on PCIe or AMD's XGMIi/Infinity Fabric links at node level rather than NVLink.
- [[cxl_compute_express_link]] — CXL addresses CPU-to-accelerator memory coherence and memory pooling across the PCIe fabric, complementing rather than replacing NVLink within a node.

## Sources

- NVIDIA NVLink and NVSwitch product page: https://www.nvidia.com/en-us/data-center/nvlink/
- NVIDIA DGX H100 datasheet (2023): https://resources.nvidia.com/en-us-dgx-systems/ai-enterprise-dgx
- Hot Chips 34 (2022): NVIDIA Hopper H100 GPU — NVLink 4.0 and NVSwitch 3.0 architecture
- NVIDIA technical blog: "NVLink-C2C: A Chip-to-Chip Interconnect for NVIDIA Grace Hopper Superchip" (2022)
- IEEE Micro: "NVSwitch: The Nerve Center of NVIDIA DGX-2" (2019)
