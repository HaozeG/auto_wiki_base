# Source: SiFive Intelligence X280 and 2nd Gen Family (cnx-software.com, sifive.com)
Fetched: 2026-06-26

## X280 (1st Gen) Architecture
- 64-bit RISC-V vector processor targeting AI/ML workloads
- 512-bit vector length RISC-V Vector extension
- 8-stage dual-issue in-order scalar pipeline
- Decoupled scalar and vector pipelines for parallel execution
- Multi-core, multi-cluster: up to 8 cores (original), up to 16-core cache-coherent complex (updated)
- Virtual memory support, up to 48-bit addressing
- VCIX (Vector Coprocessor Interface eXtension): allows integration with external custom AI accelerators

## X160/X180 Gen 2 (Entry-Level AIoT)
- X160 Gen 2: 32-bit RISC-V ISA (RV32I)
- X180 Gen 2: 64-bit RISC-V ISA (RV64I)
- Dual-issue in-order 8-stage superscalar pipeline
- 128-bit wide vector registers (vlen), 64-bit datapath (dlen)
- Int8 and BFloat16 support
- Integer throughput: 2× 32-bit / 4× 16-bit / 8× 8-bit per cycle
- Floating-point: 2× single precision, 4× half precision per cycle
- RVV1.0 compliant

## 2nd Gen Upgrades (X280, X390, XM Gen 2)
- RVA23 profile support
- Additional vector datatypes: FP4, FP8
- Expanded cache configurations
- Port modifications
- Available for licensing now; first silicon expected Q2 2026

## Real-World Implementation
- Sophgo SG2380: 16-core SiFive P670 processor at 2.5 GHz + 20 TOPS AI accelerator using SiFive Intelligence X280 + Sophgo TPU
- SiFive HiFive Premier P550: Red Hat Enterprise Linux 10 developer preview

## Extensions Supported
- SiFive Custom Instruction Extension (SCIE)
- Scalar Coprocessor Interface (SSCI)
- Vector Coprocessor Interface eXtension (VCIX)
- Up to 16 Physical Memory Protection regions
- Optional WorldGuard security (up to 4 worlds)
