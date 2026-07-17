---
canonical_name: AMD Machine-Readable GPU ISA Specifications
aliases:
- AMD ISA XML
- GPUOpen ISA
- amdgpu_isa
- IsaDecoder
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/ca001a0fd35c1ffb.md
- https://gpuopen.com/machine-readable-isa/
source_url: https://gpuopen.com/machine-readable-isa/
fetched_at: '2026-07-17T09:13:26.365628+00:00'
type: source_note
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMD Machine-Readable GPU ISA Specifications

AMD machine-readable GPU ISA specifications are a set of XML files published by AMD on GPUOpen that describe the instruction set architectures of AMD's GPU families, including CDNA and RDNA architectures from CDNA1 (MI100) through CDNA4 (MI350) and RDNA1 through RDNA4. The XML files encode instructions, encodings, operands, data formats, and human-readable description strings. In addition to the XML files, AMD provides the IsaDecoder API, a C++ library for parsing the specifications and decoding individual instructions or entire shaders. The specification is updated regularly; as of September 2025, CDNA4 support (amdgpu_isa_cdna4.xml) was added, and older MI* specification files were renamed to match the cdna* naming scheme. This resource thus serves as the primary authoritative machine-readable reference for AMD GPU programming and compiler development.

## Key Claims

- AMD publishes XML-based ISA specifications covering the CDNA 1–4 and RDNA 1–4 GPU architectures on GPUOpen.
- The XML files encode instructions, encoding bits, operands, data formats, and textual descriptions.
- An IsaDecoder API (C++) is provided for parsing the XML and decoding single instructions or complete shader kernels.
- In September 2025, support for CDNA4 was added (amdgpu_isa_cdna4.xml), and earlier MI* files were renamed to cdna* (e.g., amdgpu_isa_mi300.xml → amdgpu_isa_cdna3.xml).

## Relationships

- The [[amd_cdna_4]] architecture is documented by this specification; the machine-readable ISA files provide the authoritative instruction encoding for the matrix core and data-movement instructions that power CDNA4's AI workloads.

## Sources

- [AMD machine-readable GPU ISA documentation](raw/cache/ca001a0fd35c1ffb.md)
