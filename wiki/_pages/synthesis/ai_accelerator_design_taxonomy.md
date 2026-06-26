---
type: synthesis
connected_entities: [google_tpu, intel_amx, apple_neural_engine, arm_sme, gemmini, tenstorrent_blackhole, fpga_riscv_isa_extension_nn_inference, apple_amx]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# AI Accelerator Design Taxonomy: ISA Extensions vs. Fixed-Function vs. Systolic Arrays

## RAG Summary

Three dominant architectural philosophies govern AI accelerator design, each making a distinct set of trade-offs across flexibility, power efficiency, and ecosystem integration. The first philosophy — ISA extensions — keeps matrix compute inside the CPU pipeline: Intel AMX adds eight 1 KB tile registers and a TMUL unit to x86, delivering 1,024 BF16 MACs per cycle per core (a 16× gain over AVX-512 VNNI), while ARM SME introduces a 2D ZA tile register with outer-product throughput that scales as SVL², and RISC-V custom extensions on FPGA platforms achieve 2.14× average speedup at 49.1% energy reduction on edge networks. The second philosophy — fixed-function dedicated blocks decoupled from the CPU — trades programmability for peak efficiency: the Apple Neural Engine grew from 0.6 TOPS (A11, 2017) to 38 TOPS (M4, 2024) at roughly 3.8 TOPS/Watt, operating exclusively through Core ML with no public ISA, while the Google TPU v1 systolic array delivered 15–30× higher performance than contemporary CPUs and GPUs on inference at roughly 40 W. The third philosophy — programmable systolic and dataflow arrays with custom ISAs — targets a middle ground: Gemmini provides an open-source configurable RoCC systolic array for RISC-V research, and the Tenstorrent Blackhole integrates 120 Tensix cores backed by 768 RISC-V processors with a fully open-source Metalium software stack, priced at $1,399. No single approach dominates: ISA extensions minimize deployment friction, fixed-function blocks maximize efficiency at scale, and programmable arrays maximize long-term adaptability.

---

## Full Synthesis

### Taxonomy Overview

AI accelerator designs in the current landscape cluster into three recognizable families, differentiated by where the matrix-multiply engine sits relative to the host CPU pipeline, and by how much general-purpose programmability the system retains.

**Family 1: ISA Extensions (in-pipeline)** — Intel AMX, ARM SME, RISC-V custom extensions. These keep compute architecturally inside the CPU. AMX introduces a 2D tile register file (8 × 1 KB tmm registers) and a TMUL unit, operating on BF16 and INT8 with 1,024 operations per cycle per core. ARM SME uses a square ZA tile with outer-product FMOPA instructions; because ZA storage and throughput both scale as SVL², implementations at SVL=512 bits yield 4× the storage and 4× the MACs of SVL=256 bit implementations — a deliberate design incentive for wider silicon. FPGA-based RISC-V extensions on the PYNQ-Z2 (Zynq-7020) demonstrate the same principle at the research level: four custom opcodes (VCONV, GEMM, RELU, CUSTOM) achieve 2.14× average speedup, with convolution acceleration alone reaching 7.20× for operations dominating per-inference latency. The unifying property is transparency: operating system context switching handles tile state (XSAVE/XRSTOR in AMX, PSTATE.SM/PSTATE.ZA in SME), existing compilers emit the new instructions automatically through library backends (oneDNN for AMX), and no additional driver or runtime is required.

**Family 2: Fixed-Function Dedicated Blocks** — Apple Neural Engine, Google TPU v1, Apple AMX (partially). These architectures decouple the accelerator die from the CPU pipeline entirely. The Apple ANE is the purest example: it has no public ISA, exposes no direct programming interface, and is reachable only through Core ML's MIL compiler. This opacity enables Apple to change the microarchitecture every generation — from 2-core at 0.6 TOPS (A11) to 16-core at 38 TOPS (M4) — without breaking software compatibility. The cost is ecosystem lock-in and limited debugging surface. Google TPU v1 is similarly fixed-function for inference: a 256×256 systolic array of 8-bit MACs delivering 92 TOPS, with no caches, no speculative execution, and no general-purpose ISA on the matrix path. This deliberate narrowness achieves 15–30× higher performance and 30–80× higher performance-per-watt than contemporary Haswell CPUs and K80 GPUs on production workloads. From TPU v2 onward, Google added BF16 support (with FP32 accumulation) and a 3D torus ICI for pod-scale training, but the fundamental design — a fixed datapath optimized for dense GEMM — remains intact through v5p (95 GB HBM2e, 2,765 GB/s bandwidth, 8,960-chip pods delivering 2.8× v4 training throughput). The Apple AMX coprocessor occupies a middle position: more programmable than ANE (it is accessible via undocumented arm64 instructions), but still a proprietary coprocessor with no official documentation, separate from the CPU pipeline and specialized for outer-product GEMM. The M4 Pro's two AMX units deliver approximately 1.9 TFLOPS FP32, with energy efficiency scaling from ~56 GFLOPs/Watt (M1) to over 700 GFLOPs/Watt (M4 Pro) on batched workloads.

**Family 3: Programmable Systolic/Dataflow Arrays with Custom ISAs** — Gemmini, Tenstorrent Blackhole. These architectures are neither purely in-pipeline nor entirely opaque: they expose a custom instruction set or low-level software stack, but the compute is physically decoupled from the CPU into a reconfigurable accelerator tile. Gemmini is the academic anchor of this family: a parameterized systolic array generator implemented as a RoCC coprocessor, tightly coupled to a RISC-V host via TileLink. Its value is research agility — architects can vary array dimensions, dataflow strategy (weight-stationary vs. output-stationary), memory hierarchy, and precision without silicon respin. Tenstorrent Blackhole is the commercial realization of similar ideas at scale: 120 Tensix cores, each containing multiple RISC-V processors (768 total across the chip), 32 GB GDDR6, and ten 400 GbE links for multi-card networking. The open-source Metalium stack provides full hardware transparency — in explicit contrast to Apple ANE and Google TPU, whose software stacks are closed. At $1,399 for a PCIe card, Blackhole is positioned between consumer GPUs and datacenter TPU instances.

### Cross-Cutting Trade-offs

**Ecosystem integration vs. peak efficiency.** ISA extensions (AMX, SME) win on integration: they require no new driver, no separate runtime, and no model recompilation beyond targeting the right ISA level. Fixed-function blocks (ANE, TPU) win on efficiency at their target workload — 3.8 TOPS/Watt for ANE at the edge, extraordinary performance-per-watt for TPU at datacenter scale — but fail outside their design envelope (ANE delegates sequential attention operations back to the CPU). Programmable arrays (Gemmini, Blackhole) offer the most workload coverage but require explicit programming effort.

**Scaling strategy.** TPU scales through physical pod topology (3D torus ICI, up to 8,960 chips in v5p). Tenstorrent Blackhole scales through ten 400 GbE ports per card, enabling multi-card clusters without proprietary interconnect IP. ISA extensions scale only with the CPU core count and socket count — there is no equivalent of a TPU pod for AMX or SME.

**Numerical format choices reveal priorities.** AMX (BF16/INT8), SME (BF16/FP32/INT32/FP64), and TPU (BF16 with FP32 accumulation) all converge on BF16 as the primary training format, confirming BF16's dominance. Apple ANE dequantizes INT8 to FP16 before compute, making its nominal "INT8" TOPS figure equivalent to its FP16 figure — a discrepancy that matters for systems designers comparing INT8 throughput claims across vendors.

**Openness spectrum.** RISC-V FPGA extensions and Gemmini are fully open-source. Metalium/Blackhole is open-source at the software layer with closed silicon. Intel AMX and ARM SME are architecturally documented but closed silicon. Apple AMX is closed both at the silicon and ISA level (reverse-engineered only). Apple ANE and Google TPU are closed at every layer, exposing only high-level framework APIs.

## Open Questions

1. **Convergence or divergence?** ARM SME adopts outer-product instructions that structurally resemble the compute model of Apple AMX (also outer-product based) and Gemmini (systolic = iterated outer products). Will future generations of ISA extensions (SME2, RISC-V AME) converge sufficiently with fixed-function blocks to eliminate the distinct "ISA extension" vs. "dedicated accelerator" categories?

2. **BF16 vs. FP8 transition.** TPU v5p, AMX, and SME all standardize on BF16 with FP32 accumulation as the primary format. FP8 (E4M3/E5M2) is emerging in GPU (H100) and inference contexts. Which family — ISA extensions, fixed-function blocks, or programmable arrays — will absorb FP8 first, and will format divergence fragment the training ecosystem?

3. **Open-source programmability premium.** Gemmini and Blackhole/Metalium claim that openness reduces deployment friction. Apple ANE achieves comparable or higher efficiency while remaining completely closed. Is the efficiency gap between open and closed accelerators closing as open toolchains (MLIR, Triton, Metalium) mature, or does closed co-design (Apple's vertical integration across silicon, compiler, and framework) permanently dominate at the highest TOPS/Watt point?

4. **Edge vs. datacenter boundary.** FPGA-RISC-V extensions and Apple ANE target edge/client inference (sub-10 W); Google TPU and Tenstorrent Blackhole target cloud/server (hundreds of watts per card). Intel AMX sits awkwardly in the middle — Sapphire Rapids server processors use it for datacenter inference, but Meteor Lake brings AMX to thin laptops. Will the three-family taxonomy remain stable, or will laptop-class accelerators with ISA-extension-level integration eventually match fixed-function blocks in efficiency?

## Connected Pages

- [[google_tpu]]
- [[intel_amx]]
- [[apple_amx]]
- [[apple_neural_engine]]
- [[arm_sme]]
- [[gemmini]]
- [[tenstorrent_blackhole]]
- [[fpga_riscv_isa_extension_nn_inference]]
