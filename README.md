# Darkly

## Project Description

**Darkly** is a web security project from **42 School** focused on discovering and exploiting common vulnerabilities found in modern web applications.

The objective is to analyze a deliberately vulnerable web platform and identify multiple security flaws. Each challenge simulates a real-world security misconfiguration or vulnerability that could appear in production systems.

This repository contains:

* Detailed walkthroughs for each discovered vulnerability
* Technical explanations of exploitation techniques
* Scripts or tools used during the analysis
* Flags obtained after successfully exploiting each breach

Each directory represents a **specific security breach** that must be identified and exploited.

## Setup Instructions

To begin the **Darkly challenge**, launch the provided **ISO image** in a virtual machine.

### Requirements

* A **virtualization platform** (VirtualBox, VMware, QEMU, etc.)
* The **Darkly ISO image** — a **32-bit (i386)** virtual machine, as specified in the project subject
* Attacker and target machines on the **same network**

Once the VM boots, it displays the target IP address at the login prompt. Access the web application through your browser:

```
http://<target-ip>
```

## Objectives

The mandatory part of this project requires identifying and exploiting **14 different breaches** present in the application.

For each breach:

* Identify the vulnerability
* Exploit it to retrieve the **flag**
* Document the **entire exploitation process**

Each write-up should include:

* The vulnerability description
* Step-by-step exploitation process
* Commands and tools used
* Screenshots or explanations when necessary
* The retrieved **flag**

> Each vulnerability represents a real-world security issue commonly found in poorly secured web applications.

## Repository Structure

Each directory corresponds to one **security breach** in the application.

```
.
├── <breach-name>
│   ├── flag
│   └── Resources
│       └── README.md
├── <breach-name>
│   ├── flag
│   └── Resources
│       └── README.md
├── <breach-name>
│   ├── flag
│   └── Resources
│       └── README.md
├── <breach-name>
│   ├── flag
│   └── Resources
│       └── README.md
└── ...
```

### Directory Contents

Each breach directory contains:

* **flag** — the flag obtained after successful exploitation
* **Resources/README.md** — detailed write-up explaining the vulnerability and exploitation process
* **Resources/** (optional) — custom scripts or tools used during the attack

No compiled binaries are included in any `Resources` folder.

## Completion Criteria

The Darkly project is considered **complete** when:

* All 14 mandatory vulnerabilities are successfully discovered
* Each breach has a **clear and reproducible write-up**
* The **flag is obtained for every vulnerability**
* The exploitation process is **technically explained**

The goal is not only to retrieve flags but to **understand the security flaw behind each breach**.

## ISO File

Need the **Darkly ISO**?

Contact via email:
**[mari.nazaryan7173@gmail.com](mailto:mari.nazaryan7173@gmail.com)**

Happy hacking.

> *Understand the vulnerability — don't just exploit it.* 🐚🔐
