# ransomtest – Ransomware Simulator (Educational & Safe)

`ransomtest` is a **safe, educational ransomware simulator** written in Python.  
It does **not** implement real-world ransomware, and it **never touches files outside a sandbox directory**.

The goal is to demonstrate the **logic and workflow** of a ransomware-style incident from a **defender / DFIR perspective**, not to build malware.


## Safety & Ethical Disclaimer

- This project is **strictly for educational and defensive training purposes**.
- The simulator:
  - Only operates inside a local sandbox directory (by default: `lab_files/`).
  - Uses a **simple, reversible text transformation**, not industrial cryptography.
  - Does **not** delete, overwrite, or exfiltrate any files.
  - Does **not** contain any networking, propagation, or persistence mechanisms.
- You are responsible for using this project in a **legal and ethical** way, e.g. in your own lab environment.

## Project Goals

- Demonstrate the **typical lifecycle** of a ransomware-like event:
  - Target selection (sandbox folder)
  - “Encryption” of sample files using a reversible transformation
  - Creation of a simulated ransom note
  - Logging of all actions to support **DFIR / blue-team analysis**
  - Optional “restore” mode to reverse the transformation
- Provide a **safe lab tool** for:
  - Internal security awareness / training demos
  - DFIR practice (tracking what happened, when, and to which files)
  - Blue-team tabletop exercises
- Serve as a **portfolio project** showing understanding of:
  - Attack workflows (from a defender mindset)
  - Logging, traceability, and secure coding practices

## How It Works (High-Level)

1. **Scope Limitation – Sandbox Only**
   - The simulator only looks inside a user-controlled folder such as `lab_files/`.
   - You populate this folder with **test documents** (e.g. `.txt`, `.log`, dummy `.docx` etc.).
   - Nothing outside this folder is ever modified.

2. **Simulated “Encryption”**
   - In `encrypt` mode, the tool:
     - Iterates over files under `lab_files/` (or a custom target directory).
     - Reads their content.
     - Applies a **reversible transformation** (implemented in `crypto_sim/simple_transform.py`).
     - Writes the transformed content into `encrypted_files/` with a `.simenc` extension.
     - **Original files remain untouched.**

3. **Simulated Ransom Note**
   - A file like `lab_files/README_RECOVER.txt` is created with an **educational ransom-style message** clearly stating:
     - That this is a **lab-only simulator**.
     - That no real damage has been done.
     - That it is meant for training and demonstration purposes.

4. **Logging for DFIR / Blue Team**
   - All actions are logged to `reports/simulation_log.txt`, including:
     - Timestamps
     - Files processed
     - Mode used (`encrypt` / `restore`)
     - Transformation identifier (e.g. `"reverse"`, `"base64"`, etc.)
   - This log can later be used in exercises to:
     - Reconstruct the incident timeline
     - Correlate with other logs or tools (e.g. an IOC extractor)

5. **Simulated “Decryption” / Restore**
   - In `restore` mode, the tool:
     - Reads `.simenc` files from `encrypted_files/`.
     - Applies the inverse transformation.
     - Writes the restored content into `restored_files/`.
   - Again, original files in `lab_files/` remain unchanged.

## Project Structure

```text
ransomtest-ransomware-simulator/
├── simulator.py            # Main CLI entrypoint
├── crypto_sim/
│   ├── __init__.py
│   └── simple_transform.py # Simple, reversible text transformations
├── lab_files/              # Test files (created/maintained by the user)
│   ├── report_q4.txt
│   └── customer_list.txt
├── encrypted_files/        # Simulated “encrypted” outputs (.simenc)
├── restored_files/         # Restored outputs
├── reports/
│   └── simulation_log.txt  # Simulation log for DFIR exercises
└── README.md               # You are here

```

# CLI Usage

From the project root:

# Simulate a ransomware "encryption" run on the lab folder
python3 simulator.py --mode encrypt

# Restore from simulated encrypted files
python3 simulator.py --mode restore

# Optional: change directories
python3 simulator.py --mode encrypt --target-dir lab_files/ --encrypted-dir encrypted_files/ --reports-dir reports/

python3 simulator.py --mode restore --encrypted-dir encrypted_files/ --restored-dir restored_files/ --reports-dir reports/

For full options:

python3 simulator.py --help



## Command-Line Interface (Design)

The main script simulator.py exposes a simple CLI:
	•	--mode (required):
	•	encrypt – Simulate the “encryption” phase
	•	restore – Simulate the “decryption / recovery” phase
	•	--target-dir (optional, default: lab_files/)
	•	--encrypted-dir (optional, default: encrypted_files/)
	•	--restored-dir (optional, default: restored_files/)
	•	--reports-dir (optional, default: reports/)
	•	--transform (optional, default: e.g. reverse)
	•	Selects which simple transformation to use inside crypto_sim.simple_transform.
	•	--dry-run (optional flag)
	•	Show what would be done without writing any files.
	•	--verbose (optional flag)
	•	Print more detailed output during execution.

Example:

python3 simulator.py \
    --mode encrypt \
    --target-dir lab_files/ \
    --encrypted-dir encrypted_files/ \
    --reports-dir reports/ \
    --transform reverse \
    --verbose


# For Security Professionals & Recruiters

This project is designed as a blue-team / DFIR learning aid, not as a weaponized tool.

It can be used to:
	•	Walk through a simulated ransomware incident in a controlled lab.
	•	Demonstrate:
	•	Impact on files (within the sandbox).
	•	Ransom note artifacts.
	•	Logging and traceability of the “attack”.
	•	Anchor discussions about:
	•	Incident response workflows.
	•	Log analysis and IOC extraction.
	•	Backup and recovery strategies.

## Tech Stack
	•	Language: Python 3.x
	•	Environment: Designed to be run locally
	•	Dependencies: Standard library only for the core simulator (argparse, logging, pathlib, etc.)

## License

**Creative Commons Attribution-NonCommercial 4.0 International License**  
Copyright (c) 2025 - **Sebastián Fuentes**

**The author is not responsible for misuse; this project must only be used in controlled, legal, and ethical cybersecurity learning environments.**

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

You are free to:
- **Share**: copy and redistribute the material in any medium or format.
- **Adapt**: remix, transform, and build upon the material.

Under the following terms:
- **Attribution**: You must give appropriate credit.
- **NonCommercial**: You may not use the material or any derivatives for commercial purposes.

**No additional restrictions**:  
You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Full legal text:  
🔗 https://creativecommons.org/licenses/by-nc/4.0/legalcode