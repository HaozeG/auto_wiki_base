---
cold_start: false
connected_entities:
- NVIDIA_GPU_Secure_Boot
- NVIDIA_Confidential_Computing
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.4
  contradiction_potential: 0.1
  cross_domain_connection: null
synthesis_status: draft
type: synthesis
updated: '2026-06-27'
---

# Relationship Between FSP, SEC2, and FALCON in NVIDIA Confidential Computing

## RAG Summary

The relationship between FSP, SEC2, and FALCON in NVIDIA's confidential computing architecture is that FSP (Falcon Security Processor) functions as the hardware Root of Trust (RoT) for device attestation, while SEC2 and FALCON are additional micro-architecture modules that together establish a secure boot chain and isolated execution environment on NVIDIA GPUs. FSP is the first component to execute on GPU power-on, validating the integrity of subsequent firmware stages. SEC2 acts as a secondary security processor that handles the second-stage bootloader and enforces secure firmware loading policies. FALCON is a general-purpose microcontroller that coordinates control operations and may support cryptographic offload tasks within the secure enclave. These three modules collaborate to provide hardware-grounded trust for confidential computing workloads, ensuring that sensitive data processed on the GPU remains protected from the host operating system and other software. The architecture is designed to meet the requirements of multi-tenant environments where each tenant requires isolated and attested computation. The specific initialization sequence and trust transfer mechanisms between these components determine the overall security guarantees of the platform.

---

## Full Synthesis

The NVIDIA GPU confidential computing architecture relies on a multi-stage secure boot process orchestrated by three distinct micro-architecture modules: FSP, SEC2, and FALCON. The FSP (Falcon Security Processor) is the hardware Root of Trust (RoT) that begins execution immediately upon GPU power-on reset. It validates its own immutable boot ROM and then authenticates the next stage firmware image. The SEC2 (Security Engine 2) module assumes control after FSP, acting as a second-stage security processor that further validates and loads the FALCON microcontroller firmware. SEC2 enforces access control policies and manages cryptographic keys used during attestation. The FALCON microcontroller then handles higher-level control functions, including communication with the host driver, managing secure memory regions, and supporting remote attestation protocols. Together, these components create a chain of trust from the immutable hardware RoT to the runtime confidential computing environment. The design ensures that even if the host operating system is compromised, the GPU's secure enclave remains isolated and verifiable.

## Open Questions

The exact initialization order and trust transfer handshake between FSP, SEC2, and FALCON remains partially undocumented. It is unclear whether FALCON contributes directly to attestation or only serves as a control processor. The specific cryptographic primitives used by SEC2 for firmware verification are also not publicly confirmed.

## Connected Pages

- [[NVIDIA_GPU_Secure_Boot]] — describes the overall secure boot process for NVIDIA GPUs.
- [[NVIDIA_Confidential_Computing]] — architectural overview of confidential computing features on NVIDIA platforms.

## Sources

- NVIDIA Developer Forums thread "The relationship between FSP/SEC2 and FALCON?": https://forums.developer.nvidia.com/t/the-relationship-between-fsp-sec2-and-falcon/335926
