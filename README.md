# ransomtest – Ransomware Simulator (Educational & Safe)

`ransomtest` is a **safe, educational ransomware simulator** written in Python.  
It does **not** implement real-world ransomware, and it **never touches files outside the sandbox** (`lab_files/`).

The simulator helps DFIR students, blue-team analysts, and cybersecurity learners understand:

- How ransomware *logically* behaves  
- How files are “encrypted” and “restored” in a safe, controlled way  
- How to analyze DFIR logging (text or JSON)  
- How to simulate an incident and practice recovery workflows  

This project is intentionally **non-malicious**, **non-destructive**, and **fully reversible**.

---

# Safety & Ethical Disclaimer

- This tool is **strictly for educational and defensive training purposes**.
- It:
  - Operates only inside a designated sandbox folder (`lab_files/`)
  - Uses **simple reversible transformations** (Reverse, Base64, XOR)
  - Performs **no real cryptography**
  - Never deletes, corrupts, or exfiltrates data
  - Contains **no networking, persistence, or propagation**
- The author is **not responsible** for any misuse.
- Use only in **legal, ethical, controlled lab environments**.

---

# Project Goals

- Demonstrate how ransomware-like behavior works in a safe lab
- Simulate the phases of a ransomware incident:
  - Target selection
  - File transformation (“encryption”)
  - Ransom note creation
  - DFIR logging
  - File restoration  
- Provide a practical tool for:
  - DFIR practice  
  - Blue-team training  
  - Educational demonstrations  
  - Portfolio-building  
- Showcase understanding of:
  - File-handling
  - Reversible transformations
  - Logging & traceability  
  - Secure and ethical coding practices

---

# How It Works (High-Level)

## 1. Sandbox Scope
The simulator only interacts with files inside:

lab_files/

This folder must contain **only dummy test files** (`.txt`, `.log`, etc.).

## 2. Simulated “Encryption”
- Reads all text files inside `lab_files/`
- Applies a reversible transform:
  - `reverse`
  - `base64`
  - `xor` (requires key)
- Writes transformed output to:

encrypted_files/*.simenc

- Optionally: `--overwrite-original`
- Creates an educational ransom note:

lab_files/README_RECOVER.txt

## 3. Simulated “Decryption”
Reads from:

encrypted_files/*.simenc

Restores readable files into:

restored_files/

## 4. DFIR Logging
Every action is logged to:

reports/simulation_log.txt

Two formats supported:

- `--log-format text` (default)
- `--log-format json`

### JSON Example

```json
{
  "timestamp": "2025-11-18T10:33:41Z",
  "message": "ENCRYPT",
  "src": "lab_files/report_q4.txt",
  "dst": "encrypted_files/report_q4.txt.simenc",
  "transform": "base64",
  "orig_sha256": "…",
  "enc_sha256": "…",
  "dry_run": false
}
```

⸻

## CLI Usage Examples

Encrypt (safe mode)

python3 simulator.py --mode encrypt \
    --transform base64 \
    --verbose

Restore

python3 simulator.py --mode restore \
    --transform base64 \
    --verbose

XOR Mode

python3 simulator.py --mode encrypt \
    --transform xor \
    --key "test123" \
    --verbose

Restore:

python3 simulator.py --mode restore \
    --transform xor \
    --key "test123"

Overwrite originals (Lab realism)

python3 simulator.py --mode encrypt \
    --transform xor \
    --key "test123" \
    --overwrite-original

JSON Logging

python3 simulator.py --mode encrypt \
    --transform base64 \
    --log-format json

Dry Run (no files written)

python3 simulator.py --mode encrypt \
    --transform reverse \
    --dry-run


⸻

## Project Structure

```text
ransomtest-ransomware-simulator/
├── simulator.py            # Main CLI entrypoint
├── crypto_sim/
│   ├── __init__.py
│   └── simple_transform.py # reversible transforms (reverse, base64, xor)
├── lab_files/              # user test files (dummy data only)
├── encrypted_files/        # simulated encrypted outputs
├── restored_files/         # restored outputs
├── reports/
│   └── simulation_log.txt  # DFIR logs
├── HOW_TO_USE.txt          # beginner-friendly guide
└── README.md               # main documentation

```
⸻

## Tech Stack
	•	Language: Python 3
	•	Dependencies: Only standard library
	•	Focus Areas:
	•	DFIR
	•	Blue-team training
	•	Safe ransomware behavior emulation
	•	Traceability & forensic logging

⸻

## License

Creative Commons Attribution-NonCommercial 4.0 International License
Copyright
2025 — Sebastián Fuentes

You may share and adapt for non-commercial use with attribution.

Full license text:
https://creativecommons.org/licenses/by-nc/4.0/legalcode

