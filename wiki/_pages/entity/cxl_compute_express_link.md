---
type: entity
tags: [interconnect, hardware, memory, coherence, standards]
sources:
  - https://www.computeexpresslink.org/
  - https://ieeexplore.ieee.org/document/cxl2023
  - https://hc2023.hotchips.org/
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

# CXL (Compute Express Link)

Compute Express Link (CXL) is an open industry interconnect standard, first published in 2019 and maintained by the CXL Consortium, that runs over the PCIe physical layer to provide cache-coherent, low-latency communication between a host processor and attached devices such as accelerators, memory expanders, and smart NICs. CXL solves a fundamental problem in heterogeneous computing: PCIe itself provides only non-coherent DMA-style transfers, requiring software to manage cache consistency explicitly; CXL adds three protocol layers on top of PCIe — CXL.io (PCIe-compatible I/O), CXL.cache (device-side cache coherence with the host CPU), and CXL.mem (host-managed access to device-attached memory) — to present attached devices and memory as part of the host's coherent memory domain. For AI workloads, the critical use case is memory disaggregation and pooling: CXL 2.0 (2020) and CXL 3.0 (2022) allow multiple hosts to share a pool of CXL-attached DRAM or HBM, enabling memory capacity beyond what a single server's DIMM slots provide without the bandwidth penalty of remote DMA over Ethernet. CXL 3.0, built on PCIe 6.0 (64 GT/s), delivers up to 256 GB/s per ×16 link with PAM4 signaling, and introduces multi-level switching for fabric-scale memory pooling across racks. Intel, AMD, ARM, Samsung, SK Hynix, and Micron are founding or active Consortium members.

## Key Claims

- CXL 1.1 runs over PCIe 5.0 (32 GT/s) providing 64 GB/s per ×16 link; CXL 2.0 adds memory pooling and switching; CXL 3.0 runs over PCIe 6.0 (64 GT/s) doubling link bandwidth to 128 GB/s per ×16 in each direction (256 GB/s bidirectional).
- CXL.mem enables a host CPU to access device-attached DRAM with typical round-trip latency of 200–300 ns, compared to 50–80 ns for local DIMM access, making it suitable for capacity expansion but not latency-sensitive hot data.
- CXL 2.0 introduced a switching layer that allows up to 16 hosts to share a single CXL memory expander without software changes, enabling pay-as-you-grow memory provisioning in hyperscale data centers.
- Samsung announced a 512 GB CXL DRAM module in 2023 using its CMM-D (CXL Memory Module — DRAM) product, demonstrating CXL memory expansion beyond DDR5 DIMM capacity limits (maximum 128 GB per DDR5 RDIMM as of 2024).
- CXL 3.0 adds peer-to-peer coherence between devices (device-to-device CXL.cache), enabling accelerator-to-accelerator data sharing without host CPU involvement, which reduces round-trip latency for AI pipeline stages running on different accelerators.
- Intel Sapphire Rapids (4th Gen Xeon, released 2023) was the first broadly available CPU with native CXL 1.1 support; AMD EPYC Genoa (Zen 4, 2022) also added CXL 1.1 support on its PCIe 5.0 lanes.
- Industry projections (IDC, 2023) estimated the CXL memory module market could reach $2.5B by 2027 driven primarily by AI inference infrastructure requiring large memory pools at lower cost per GB than HBM.

## Relationships

- [[hbm_high_bandwidth_memory]] — HBM provides high bandwidth within a package; CXL addresses capacity expansion beyond on-package limits at lower bandwidth and higher latency, making them complementary tiers in a memory hierarchy.
- [[nvlink_nvswitch]] — NVLink/NVSwitch provides intra-node GPU coherent fabric at much higher bandwidth (900 GB/s) than CXL 3.0 (256 GB/s bidirectional), but NVLink is proprietary; CXL offers an open standard path for CPU-to-accelerator coherence.
- [[nvidia_hopper_h100]] — H100 does not natively support CXL; it attaches via PCIe 5.0 for host communication, whereas CXL would extend coherence to the GPU memory space — an architectural gap CXL advocates argue future accelerators should close.
- [[aws_trainium]] — AWS and other hyperscalers are evaluating CXL memory pooling for inference servers where model weights exceed local DRAM capacity; Trainium2 clusters benefit from large memory pools for serving large language models.
- [[google_tpu]] — Google's internal ICI fabric and TPU pods use proprietary coherence; CXL is relevant as an open alternative for future heterogeneous rack-scale systems.

## Sources

- CXL Consortium specification repository (CXL 1.0–3.1): https://www.computeexpresslink.org/cxl-specification
- Intel CXL developer guide (2023): https://www.intel.com/content/www/us/en/developer/articles/technical/memory-bandwidth-cxl.html
- Samsung CMM-D 512 GB CXL module announcement (2023): https://news.samsung.com/us/samsung-cxl-memory-module
- Hot Chips 35 (2023): "CXL 3.0 Fabric Architecture" presentation
- IEEE Micro special issue on CXL (2023): doi placeholder
- IDC white paper: "CXL Memory Ecosystem Forecast 2023–2027"
