---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.75
  claim_density: 0.85
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/Nuclei-Software/nuclei-sdk
tags:
- risc-v
- sdk
- nuclei
- embedded
- rtos
type: entity
updated: '2026-06-27'
---

# Nuclei Software Development Kit (Nuclei SDK)

The Nuclei Software Development Kit (Nuclei SDK) is an open-source software development platform for building and evaluating applications on Nuclei RISC-V processor cores and evaluation System-on-Chips (SoCs). Developed by Nuclei System Technology, the SDK is built on top of the Nuclei Microcontroller Software Interface Standard (NMSIS) framework, providing a unified hardware abstraction layer and peripheral access APIs for on-board devices such as GPIO, UART, SPI, and I2C. It supports multiple toolchains including Nuclei RISC-V GCC/Clang, IAR Embedded Workbench, and Terapines ZCC, and integrates several real-time operating systems (RTOSes) – FreeRTOS, μC/OS-II, RT-Thread, and ThreadX – allowing developers to choose between baremetal and RTOS-based application development. The SDK targets Nuclei 200, 300, 600, 900, and 1000 series CPUs, and includes build system support for Linux and Windows environments, with preconfigured Makefiles and IDE integration via Nuclei Studio or PlatformIO. The SDK's structure includes directories for application code (baremetal and each RTOS), SoC-specific support packages, a build system under the `Build` directory, the NMSIS header library, and RTOS kernel source trees. Since version 0.5.0, Nuclei Studio 2023.10 or later and Nuclei RISC-V Toolchain/QEMU/OpenOCD 2023.10 or later are required. The SDK is distributed under an open-source license and is hosted on GitHub.

## Key Claims

- The Nuclei SDK is built on the NMSIS framework, providing a consistent hardware abstraction layer for Nuclei RISC-V processors.
- It supports three compiler toolchains: Nuclei RISC-V GCC/Clang, IAR Embedded Workbench, and Terapines ZCC.
- Four RTOSes are integrated: FreeRTOS, μC/OS-II, RT-Thread, and ThreadX.
- The SDK includes application examples for baremetal and each RTOS, located under the `application` directory.
- It provides APIs for on-board peripheral access: GPIO, UART, SPI, and I2C.
- The build system is based on GNU Make, with a set of modular Makefiles in the `Build` directory.
- For each supported SoC, the SDK requires a `nuclei_sdk_soc.h` header in the SoC include directory and a `nuclei_sdk_hal.h` header in the board include directory.
- The SDK is compatible with Nuclei 200, 300, 600, 900, and 1000 series CPUs.
- It can be used with PlatformIO via a provided `package.json` file.
- The SDK includes a `setup.sh` script for Linux environment setup and a `setup.bat` for Windows.
- Integration with RT-Thread package management is supported via a `SConscript` file.
- The NMSIS version used in the SDK is declared in a `NMSIS_VERSION` file and is periodically synced with the upstream NMSIS project.

## Relationships

No directly related wiki pages exist at this time. The SDK is complementary to pages on RISC-V architecture, NMSIS, and Nuclei processors, but those pages are not yet present in the wiki.

## Sources

- https://github.com/Nuclei-Software/nuclei-sdk
