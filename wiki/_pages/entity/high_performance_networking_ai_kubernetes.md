---
cold_start: false
created: '2026-02-26'
inbound_links: 0
scorecard:
  bridge_score: 0.9
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://kubernetes.recipes/recipes/networking/infiniband-ethernet-ai-kubernetes/
tags:
- networking
- infiniband
- ethernet
- rdma
- roce
- kubernetes
- ai
- gpu
type: entity
updated: '2026-02-26'
---

# High-Performance Networking for AI on Kubernetes

High-performance networking for AI on Kubernetes is a critical infrastructure layer that enables GPU-intensive workloads to communicate efficiently across nodes. The choice between InfiniBand and Ethernet technologies, including RDMA (Remote Direct Memory Access) and RoCE (RDMA over Converged Ethernet), directly impacts training throughput, latency, and scalability of distributed AI models. InfiniBand offers dedicated high-bandwidth, low-latency interconnects traditionally used in HPC clusters, while Ethernet with RoCE provides a converged solution that leverages existing network infrastructure. Kubernetes orchestrates these networking options through specialized CNI plugins, device plugins, and NCCL (NVIDIA Collective Communications Library) configurations to achieve optimal performance for AI/ML workloads. This page synthesizes the trade-offs between InfiniBand and Ethernet for AI on Kubernetes based on practical deployment considerations.

## Key Claims

- InfiniBand provides lower latency (sub-1 microsecond) and higher throughput (up to 400 Gbps with NDR) compared to standard Ethernet, making it the preferred interconnect for large-scale distributed training.
- RoCE (RDMA over Converged Ethernet) enables RDMA capabilities on standard Ethernet networks, achieving latency in the range of 1-3 microseconds and throughput up to 200 Gbps with congestion control enabled.
- Kubernetes requires the RDMA CNI plugin (e.g., from Mellanox/NVIDIA) and device plugin for SR-IOV or VFIO to expose RDMA-capable network interfaces to pods.
- NCCL (NVIDIA Collective Communications Library) is optimized for both InfiniBand and RoCE, but performance tuning (e.g., NCCL_IB_HCA, NCCL_IB_DISABLE, NCCL_NET_GDR_LEVEL) differs between the two.
- Ethernet with RoCE is often chosen for its cost-effectiveness and compatibility with existing data center networking, though it may require additional configuration for lossless behavior (e.g., PFC, ECN).
- InfiniBand deployments on Kubernetes are more complex due to the need for dedicated hardware and often result in higher total cost of ownership but deliver deterministic performance for large training jobs.
- The choice between InfiniBand and Ethernet depends on factors including scale of training (number of GPUs), latency sensitivity, budget, and existing network infrastructure.

## Relationships

- [[ai_chip_export_controls]] — Export controls on advanced AI chips such as NVIDIA H100/H200 and AMD MI300X directly affect the availability and deployment of high-performance networking hardware (e.g., NVIDIA ConnectX-7/8 InfiniBand adapters and switches) in restricted markets, thereby influencing networking choices for AI on Kubernetes in those regions.

## Sources

- https://kubernetes.recipes/recipes/networking/infiniband-ethernet-ai-kubernetes/

