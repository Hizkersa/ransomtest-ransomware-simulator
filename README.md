{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fswiss\fcharset0 Helvetica;
\f3\fnil\fcharset0 .SFNS-Regular;\f4\fnil\fcharset0 .SFNS-Semibold;\f5\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;
\f6\fnil\fcharset0 HelveticaNeue-Bold;}
{\colortbl;\red255\green255\blue255;\red135\green5\blue129;\red0\green0\blue0;\red181\green0\blue19;
\red20\green0\blue196;\red14\green14\blue14;\red13\green100\blue1;}
{\*\expandedcolortbl;;\cssrgb\c60784\c13725\c57647;\csgray\c0;\cssrgb\c76863\c10196\c8627;
\cssrgb\c10980\c0\c81176;\cssrgb\c6700\c6700\c6700;\cssrgb\c0\c45490\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf2 # ransomtest \'96 Ransomware Simulator (Educational & Safe)\cf3 \
\
\cf4 `ransomtest`\cf3  is a 
\f1\b **safe, educational ransomware simulator**
\f0\b0  written in Python.  \
It does 
\f1\b **not**
\f0\b0  implement real-world ransomware, and it 
\f1\b **never touches files outside a sandbox directory**
\f0\b0 .\
\
The goal is to demonstrate the 
\f1\b **logic and workflow**
\f0\b0  of a ransomware-style incident from a 
\f1\b **defender / DFIR perspective**
\f0\b0 , not to build malware.\
\
\
\cf2 ## Safety & Ethical Disclaimer\cf3 \
\
\cf5 -\cf3  This project is 
\f1\b **strictly for educational and defensive training purposes**
\f0\b0 .\
\cf5 -\cf3  The simulator:\
\cf5   -\cf3  Only operates inside a local sandbox directory (by default: \cf4 `lab_files/`\cf3 ).\
\cf5   -\cf3  Uses a 
\f1\b **simple, reversible text transformation**
\f0\b0 , not industrial cryptography.\
\cf5   -\cf3  Does 
\f1\b **not**
\f0\b0  delete, overwrite, or exfiltrate any files.\
\cf5   -\cf3  Does 
\f1\b **not**
\f0\b0  contain any networking, propagation, or persistence mechanisms.\
\cf5 -\cf3  You are responsible for using this project in a 
\f1\b **legal and ethical**
\f0\b0  way, e.g. in your own lab environment.\
\
\cf2 ## Project Goals\cf3 \
\
\cf5 -\cf3  Demonstrate the 
\f1\b **typical lifecycle**
\f0\b0  of a ransomware-like event:\
\cf5   -\cf3  Target selection (sandbox folder)\
\cf5   -\cf3  \'93Encryption\'94 of sample files using a reversible transformation\
\cf5   -\cf3  Creation of a simulated ransom note\
\cf5   -\cf3  Logging of all actions to support 
\f1\b **DFIR / blue-team analysis**
\f0\b0 \
\cf5   -\cf3  Optional \'93restore\'94 mode to reverse the transformation\
\cf5 -\cf3  Provide a 
\f1\b **safe lab tool**
\f0\b0  for:\
\cf5   -\cf3  Internal security awareness / training demos\
\cf5   -\cf3  DFIR practice (tracking what happened, when, and to which files)\
\cf5   -\cf3  Blue-team tabletop exercises\
\cf5 -\cf3  Serve as a 
\f1\b **portfolio project**
\f0\b0  showing understanding of:\
\cf5   -\cf3  Attack workflows (from a defender mindset)\
\cf5   -\cf3  Logging, traceability, and secure coding practices\
\
\cf2 ## How It Works (High-Level)\cf3 \
\
\cf5 1.\cf3  
\f1\b **Scope Limitation \'96 Sandbox Only**
\f0\b0 \
\cf5    -\cf3  The simulator only looks inside a user-controlled folder such as \cf4 `lab_files/`\cf3 .\
\cf5    -\cf3  You populate this folder with 
\f1\b **test documents**
\f0\b0  (e.g. \cf4 `.txt`\cf3 , \cf4 `.log`\cf3 , dummy \cf4 `.docx`\cf3  etc.).\
\cf5    -\cf3  Nothing outside this folder is ever modified.\
\
\cf5 2.\cf3  
\f1\b **Simulated \'93Encryption\'94**
\f0\b0 \
\cf5    -\cf3  In \cf4 `encrypt`\cf3  mode, the tool:\
\cf5      -\cf3  Iterates over files under \cf4 `lab_files/`\cf3  (or a custom target directory).\
\cf5      -\cf3  Reads their content.\
\cf5      -\cf3  Applies a 
\f1\b **reversible transformation**
\f0\b0  (implemented in \cf4 `crypto_sim/simple_transform.py`\cf3 ).\
\cf5      -\cf3  Writes the transformed content into \cf4 `encrypted_files/`\cf3  with a \cf4 `.simenc`\cf3  extension.\
\cf5      -\cf3  
\f1\b **Original files remain untouched.**
\f0\b0 \
\
\cf5 3.\cf3  
\f1\b **Simulated Ransom Note**
\f0\b0 \
\cf5    -\cf3  A file like \cf4 `lab_files/README_RECOVER.txt`\cf3  is created with an 
\f1\b **educational ransom-style message**
\f0\b0  clearly stating:\
\cf5      -\cf3  That this is a 
\f1\b **lab-only simulator**
\f0\b0 .\
\cf5      -\cf3  That no real damage has been done.\
\cf5      -\cf3  That it is meant for training and demonstration purposes.\
\
\cf5 4.\cf3  
\f1\b **Logging for DFIR / Blue Team**
\f0\b0 \
\cf5    -\cf3  All actions are logged to \cf4 `reports/simulation_log.txt`\cf3 , including:\
\cf5      -\cf3  Timestamps\
\cf5      -\cf3  Files processed\
\cf5      -\cf3  Mode used (\cf4 `encrypt`\cf3  / \cf4 `restore`\cf3 )\
\cf5      -\cf3  Transformation identifier (e.g. \cf4 `"reverse"`\cf3 , \cf4 `"base64"`\cf3 , etc.)\
\cf5    -\cf3  This log can later be used in exercises to:\
\cf5      -\cf3  Reconstruct the incident timeline\
\cf5      -\cf3  Correlate with other logs or tools (e.g. an IOC extractor)\
\
\cf5 5.\cf3  
\f1\b **Simulated \'93Decryption\'94 / Restore**
\f0\b0 \
\cf5    -\cf3  In \cf4 `restore`\cf3  mode, the tool:\
\cf5      -\cf3  Reads \cf4 `.simenc`\cf3  files from \cf4 `encrypted_files/`\cf3 .\
\cf5      -\cf3  Applies the inverse transformation.\
\cf5      -\cf3  Writes the restored content into \cf4 `restored_files/`\cf3 .\
\cf5    -\cf3  Again, original files in \cf4 `lab_files/`\cf3  remain unchanged.\
\
\cf2 ## Project Structure\cf3 \
\
\cf4 ```text\
ransomtest-ransomware-simulator/\
\uc0\u9500 \u9472 \u9472  simulator.py            # Main CLI entrypoint\
\uc0\u9500 \u9472 \u9472  crypto_sim/\
\uc0\u9474    \u9500 \u9472 \u9472  __init__.py\
\uc0\u9474    \u9492 \u9472 \u9472  simple_transform.py # Simple, reversible text transformations\
\uc0\u9500 \u9472 \u9472  lab_files/              # Test files (created/maintained by the user)\
\uc0\u9474    \u9500 \u9472 \u9472  report_q4.txt\
\uc0\u9474    \u9492 \u9472 \u9472  customer_list.txt\
\uc0\u9500 \u9472 \u9472  encrypted_files/        # Simulated \'93encrypted\'94 outputs (.simenc)\
\uc0\u9500 \u9472 \u9472  restored_files/         # Restored outputs\
\uc0\u9500 \u9472 \u9472  reports/\
\uc0\u9474    \u9492 \u9472 \u9472  simulation_log.txt  # Simulation log for DFIR exercises\
\uc0\u9492 \u9472 \u9472  README.md               # You are here
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf4 ```
\f2\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf6 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\b\fs34 \cf6 # CLI Usage
\f3\b0\fs28 \
\
From the project root:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf7 # Simulate a ransomware "encryption" run on the lab folder\cf3 \
python3 simulator.py --mode encrypt\
\
\cf7 # Restore from simulated encrypted files\cf3 \
python3 simulator.py --mode restore\
\
\cf7 # Optional: change directories\cf3 \
python3 simulator.py --mode encrypt --target-dir lab_files/ --encrypted-dir encrypted_files/ --reports-dir reports/\
\
python3 simulator.py --mode restore --encrypted-dir encrypted_files/ --restored-dir restored_files/ --reports-dir reports/
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf6 For full options:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py --help
\f2\fs24 \cf0 \
\
\
\
## 
\f4\b\fs34 \cf6 Command-Line Interface (Design)
\f3\b0\fs28 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0
\cf6 \
The main script 
\f5 simulator.py
\f3  exposes a simple CLI:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f5 --mode
\f3  (required):\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f5 encrypt
\f3  \'96 Simulate the \'93encryption\'94 phase\
	\'95	
\f5 restore
\f3  \'96 Simulate the \'93decryption / recovery\'94 phase\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f5 --target-dir
\f3  (optional, default: 
\f5 lab_files/
\f3 )\
	\'95	
\f5 --encrypted-dir
\f3  (optional, default: 
\f5 encrypted_files/
\f3 )\
	\'95	
\f5 --restored-dir
\f3  (optional, default: 
\f5 restored_files/
\f3 )\
	\'95	
\f5 --reports-dir
\f3  (optional, default: 
\f5 reports/
\f3 )\
	\'95	
\f5 --transform
\f3  (optional, default: e.g. 
\f5 reverse
\f3 )\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Selects which simple transformation to use inside 
\f5 crypto_sim.simple_transform
\f3 .\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f5 --dry-run
\f3  (optional flag)\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Show what would be done without writing any files.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f5 --verbose
\f3  (optional flag)\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Print more detailed output during execution.\
\
Example:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py \\\
    --mode encrypt \\\
    --target-dir lab_files/ \\\
    --encrypted-dir encrypted_files/ \\\
    --reports-dir reports/ \\\
    --transform reverse \\\
    --verbose
\f2\fs24 \cf0 \
\
\
# 
\f4\b\fs34 \cf6 For Security Professionals & Recruiters
\f3\b0\fs28 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0
\cf6 \
This project is designed as a 
\f6\b blue-team / DFIR learning aid
\f3\b0 , not as a weaponized tool.\
\
It can be used to:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Walk through a 
\f6\b simulated ransomware incident
\f3\b0  in a controlled lab.\
	\'95	Demonstrate:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Impact on files (within the sandbox).\
	\'95	Ransom note artifacts.\
	\'95	Logging and traceability of the \'93attack\'94.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Anchor discussions about:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	Incident response workflows.\
	\'95	Log analysis and IOC extraction.\
	\'95	Backup and recovery strategies.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0
\cf6 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\b\fs34 \cf6 ## Tech Stack
\f3\b0\fs28 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf6 	\'95	
\f6\b Language:
\f3\b0  Python 3.x\
	\'95	
\f6\b Environment:
\f3\b0  Designed to be run locally\
	\'95	
\f6\b Dependencies:
\f3\b0  Standard library only for the core simulator (argparse, logging, pathlib, etc.)\

\f2\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf0 ## License\
\
**Creative Commons Attribution-NonCommercial 4.0 International License**  \
Copyright (c) 2025 - **Sebasti\'e1n Fuentes**\
\
**The author is not responsible for misuse; this project must only be used in controlled, legal, and ethical cybersecurity learning environments.**\
\
This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.\
\
You are free to:\
- **Share**: copy and redistribute the material in any medium or format.\
- **Adapt**: remix, transform, and build upon the material.\
\
Under the following terms:\
- **Attribution**: You must give appropriate credit.\
- **NonCommercial**: You may not use the material or any derivatives for commercial purposes.\
\
**No additional restrictions**:  \
You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.\
\
Full legal text:  \
\uc0\u55357 \u56599  https://creativecommons.org/licenses/by-nc/4.0/legalcode}