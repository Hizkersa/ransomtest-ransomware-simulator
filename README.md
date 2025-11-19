# ransomtest – Educational Ransomware Simulator

`ransomtest` is a controlled, non-destructive ransomware simulation tool designed for DFIR training, blue-team practice, and cybersecurity education.  
The simulator operates strictly inside a sandbox directory and uses simple, reversible text transformations to emulate ransomware behavior.

---

## Overview

This project demonstrates the logical workflow of a ransomware incident without using real cryptography or destructive methods.  
It provides a safe environment for understanding:

- File targeting and traversal  
- Simulated “encryption” using reversible transforms  
- Ransom note generation  
- DFIR-oriented logging  
- Restoration of transformed data  

All actions are fully contained within controlled directories.

---

## Features

- Sandbox-only operation (`lab_files/`)
- Reversible transformations:
  - `reverse`
  - `base64`
  - `xor` (requires key)
- Safe simulation of encryption and decryption
- Optional overwrite mode for realistic laboratory scenarios
- DFIR logging in text or JSON format
- No networking, persistence, propagation, or deletion of system files

---

## Directory Structure
´´´text
ransomtest-ransomware-simulator/
├── simulator.py
├── crypto_sim/
│   ├── init.py
│   └── simple_transform.py
├── lab_files/
├── encrypted_files/
├── restored_files/
├── reports/
│   └── simulation_log.txt
├── HOW_TO_USE.txt
└── README.md
´´´
---

## Usage

### Encrypt files

´´´text
python3 simulator.py –mode encrypt –transform base64
´´´
### Restore files

´´´text
python3 simulator.py –mode restore –transform base64
´´´

### XOR mode (requires key)

´´´text
python3 simulator.py –mode encrypt –transform xor –key “yourkey”
python3 simulator.py –mode restore –transform xor –key “yourkey”
´´´

### Overwrite original files (lab-only realism)

´´´text
python3 simulator.py –mode encrypt –transform xor –key “yourkey” –overwrite-original
´´´

### JSON logging

´´´text
python3 simulator.py –mode encrypt –log-format json
´´´

### Dry run (no changes written)

´´´text
python3 simulator.py –mode encrypt –dry-run
´´´

---

## Logging Example (JSON)

´´´text
{
“timestamp”: “2025-11-18T10:33:41Z”,
“action”: “ENCRYPT”,
“src”: “lab_files/report_q4.txt”,
“dst”: “encrypted_files/report_q4.txt.simenc”,
“transform”: “base64”,
“orig_sha256”: “…”,
“enc_sha256”: “…”,
“dry_run”: false
}
 ´´´
---

## Supported Transforms

| Transform | Description | Reversible | Key Required |
|----------|-------------|------------|--------------|
| reverse  | String reversal | Yes | No |
| base64   | Base64 encode/decode | Yes | No |
| xor      | XOR with user-supplied key (hex output) | Yes | Yes |

---

## Requirements

 ´´´text
- Python 3.x  
- No external dependencies (standard library only)
´´´

---

## License

Licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**.  
© 2025 — Sebastián Fuentes.

See: https://creativecommons.org/licenses/by-nc/4.0/legalcode
