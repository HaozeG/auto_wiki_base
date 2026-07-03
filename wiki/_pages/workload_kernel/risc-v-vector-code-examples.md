---
canonical_name: RISC-V Vector Code Examples
aliases:
- RVV code examples
- RISC-V vector example kernels
- Vector Assembly Code Examples
- RISC-V vector-vector add example
- SAXPY RISC-V vector example
- SGEMM RISC-V vector example
subtype: null
tags:
- RISC-V
- RVV
- vector
- assembly
workloads:
- vector-vector add (VVADD)
- mixed-width mask and compute
- memcpy
- conditional selection
- SAXPY
- SGEMM
datatypes:
- int8
- int16
- int32
- float32
constraints:
- RVV 1.0 (ratified specification)
- LMUL settings: m1, m2, m4, m8
- SEW settings: e8, e16, e32
- Use of vsetvli for length setting
- VLMAX-dependent vector length
scorecard:
  novelty_delta: 0.5
  claim_density: 0.2
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.6
sources:
- raw/cache/3bb806a6221961bd.md
- https://docs.riscv.org/reference/isa/v20240411/unpriv/vector-examples.html
source_url: https://docs.riscv.org/reference/isa/v20240411/unpriv/vector-examples.html
fetched_at: '2026-07-02T09:56:04.558517+00:00'
type: workload_kernel
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# RISC-V Vector Code Examples

This page documents vector assembly code examples extracted from the non-normative text of the RISC-V ratified specifications library. These examples illustrate how to implement common data-parallel kernels using the RISC-V Vector Extension (RVV 1.0) instruction set. The kernels include a vector-vector add of 32-bit integers (VVADD), a mixed-width pattern that uses 8-bit elements for predicate computation and 32-bit elements for the masked operation, a byte-wise memcpy, a conditional selection that promotes 8-bit conditions to 16-bit results, a SAXPY (single-precision AXPY) kernel, and a partial SGEMM (single-precision general matrix multiply) kernel that processes a 16 x VLMAX block of the C matrix. Each example demonstrates idiomatic use of vsetvli to set vector length, vector load/store instructions (vle8.v, vle16.v, vle32.v, vse32.v), mask manipulation (vmslt.vi, vmnot.m), fused multiply-accumulate (vfmacc.vf), and pointer arithmetic for strided memory access. The examples are provided as non-normative reference material to aid developers in writing performant vector code for RISC-V platforms.

## Key Claims

- The VVADD kernel performs element-wise addition of two int32 vectors using vsetvli, vle32.v, vadd.vv, and vse32.v in a loop.
- The mixed-width kernel uses e8/m1 for predicate computation and e32/m4 for the masked compute, demonstrating SEW/LMUL change.
- The memcpy kernel copies bytes using e8/m8 vectors.
- The conditional selection kernel uses a mask to select between two vectors based on a comparison.
- The SAXPY kernel computes y[i] = a * x[i] + y[i] in single precision using vfmacc.vf.
- The SGEMM kernel implements a 16-row block of C matrix multiplication using software-pipelined loads and vfmacc.vf instructions, assuming a 4-cycle vfmacc occupancy.
- All examples are non-normative and target the ratified RISC-V Vector Extension 1.0.

## Kernel Shape

### VVADD
- Operation: z[i] = x[i] + y[i] for 32-bit integers
- Shapes: n elements, n determined at runtime; vector length set via vsetvli
- Datatypes: int32
- Layout: contiguous arrays
- Sparsity: dense
- Baseline implementation: scalar loop (not shown)

### Mixed-width Mask and Compute
- Operation: b[i] = (a[i] < 5) ? c[i] : 1, where a is int8, b and c are int32
- Shapes: n elements
- Datatypes: int8 (predicate), int32 (data)
- Layout: contiguous
- Sparsity: dense
- Baseline implementation: scalar branch (not shown)

### Memcpy
- Operation: dest[i] = src[i] for bytes
- Shapes: n bytes
- Datatypes: int8
- Layout: contiguous
- Sparsity: dense
- Baseline implementation: scalar byte copy (not shown)

### Conditional Selection
- Operation: z[i] = (x[i] < 5) ? a[i] : b[i], where x is int8, a, b, z are int16
- Shapes: n elements
- Datatypes: int8 (condition), int16 (data)
- Layout: contiguous
- Sparsity: dense
- Baseline implementation: scalar branch (not shown)

### SAXPY
- Operation: y[i] = a * x[i] + y[i] for single-precision floats
- Shapes: n elements
- Datatypes: float32
- Layout: contiguous
- Sparsity: dense
- Baseline implementation: scalar fused multiply-add (not shown)

### SGEMM
- Operation: c += a * b (alpha=1, no transpose), matrices in row-major order
- Shapes: m rows, n columns, k inner dimension; code processes 16 rows at a time
- Datatypes: float32
- Layout: row-major
- Sparsity: dense
- Baseline implementation: not provided; the code uses a 16*VLMAX block of C held in vector registers

## Relationships

- [[xuantie-c920v1-rvv-instruction-timings]]: related via shared float32, int16, int32, int8, rvv.

- [[riscv-vector-tests]]: related via shared risc-v, rvv, vector.

- [[sifive-intelligence-x160-gen-2]]: This hardware target supports RVV 1.0 and can execute these vector code examples.
- [[gemmini]]: The SGEMM kernel represents a software-vectorized alternative to the systolic matrix multiplication approach implemented in Gemmini accelerators.

## Sources

- [Vector Assembly Code Examples :: RISC-V Ratified Specifications Library](https://docs.riscv.org/reference/isa/v20240411/unpriv/vector-examples.html)
