
# Ransomtest — Educational Ransomware Simulator

Ransomtest is a controlled, non-destructive ransomware simulator built for DFIR training, blue-team workflows, and cybersecurity education.
The tool mimics the logical behavior of ransomware inside a sandbox, using simple reversible transforms instead of real cryptography.

This project is fully safe, reversible, and intended for educational environments only.

## Overview

ransomtest simulates the core phases of a ransomware incident:
	•	File targeting inside a sandbox (lab_files/)
	•	Reversible pseudo-encryption (reverse, base64, xor)
	•	Ransom note generation
	•	DFIR logging (text or JSON)
	•	File restoration into a clean directory

It provides a practical, hands-on way to understand how ransomware acts, without implementing harmful behavior.


## Features

	•	Sandbox-only execution
No file outside lab_files/ is ever touched.
	•	Reversible transformations
	•	reverse
	•	base64
	•	xor (requires --key)
	•	DFIR logging
	•	Text logs
	•	JSON logs (SOC/forensics-friendly)
	•	Safe simulation
No exfiltration, no deletion, no persistence, no networking.
	•	Recovery mode
Full restoration of .simenc files into restored_files/.
	•	Dry-run support
Test actions without writing any files.

## Project Structure

```bash
ransomtest-ransomware-simulator/
├── simulator.py
├── crypto_sim/
│   ├── __init__.py
│   └── simple_transform.py
├── lab_files/
├── encrypted_files/
├── restored_files/
├── reports/
├── HOW_TO_USE.txt
└── README.md
```

## CLI Usage

 - Encrypt
```bash
python3 simulator.py --mode encrypt --transform base64
```
Restore
```bash
python3 simulator.py --mode restore --transform base64
```
XOR Transform
```bash
python3 simulator.py --mode encrypt --transform xor --key "yourkey"
python3 simulator.py --mode restore --transform xor --key "yourkey"
```
Overwrite originals (optional)
```bash
python3 simulator.py --mode encrypt --overwrite-original
```
JSON logging
```bash
python3 simulator.py --mode encrypt --log-format json
```
Dry-run
```bash
python3 simulator.py --mode encrypt --dry-run
```


Example JSON Log

```bash
{
  "timestamp": "2025-11-18T10:33:41Z",
  "action": "ENCRYPT",
  "src": "lab_files/report_q4.txt",
  "dst": "encrypted_files/report_q4.txt.simenc",
  "transform": "base64",
  "orig_sha256": "...",
  "enc_sha256": "...",
  "dry_run": false
}
```

## Supported Transforms

Transform	Description	Reversible	Key
reverse	Reverse string	Yes	No
base64	Base64 encode/decode	Yes	No
xor	XOR (hex output)	Yes	Yes


## Requirements
	•	Python 3.x
	•	No external dependencies (standard library only)

⸻

## License

Licensed under CC BY-NC 4.0.
© 2025 — Sebastián Fuentes.
This project is intended for non-commercial educational use only.

Full license:
https://creativecommons.org/licenses/by-nc/4.0/legalcode
