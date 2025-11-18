{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fswiss\fcharset0 Helvetica;
\f3\fnil\fcharset0 .SFNS-Regular;\f4\fnil\fcharset0 HelveticaNeue-Bold;\f5\fnil\fcharset0 .SFNS-Semibold;
\f6\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;}
{\colortbl;\red255\green255\blue255;\red135\green5\blue129;\red0\green0\blue0;\red181\green0\blue19;
\red14\green14\blue14;}
{\*\expandedcolortbl;;\cssrgb\c60784\c13725\c57647;\csgray\c0;\cssrgb\c76863\c10196\c8627;
\cssrgb\c6700\c6700\c6700;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf2 # How to Use `ransomtest` (Step by Step)\cf3 \
\
This is a 
\f1\b **safe, educational ransomware simulator**
\f0\b0 .  \
It only works inside the \cf4 `lab_files/`\cf3  folder and uses simple, reversible transforms (NOT real crypto).\
\
---\
\
\cf2 ## 1. Setup the project\cf3 \
\
Make sure your folder looks like this:\
\
\cf4 ```text\
ransomtest-ransomware-simulator/\
\uc0\u9500 \u9472 \u9472  simulator.py\
\uc0\u9500 \u9472 \u9472  crypto_sim/\
\uc0\u9474    \u9500 \u9472 \u9472  __init__.py\
\uc0\u9474    \u9492 \u9472 \u9472  simple_transform.py\
\uc0\u9500 \u9472 \u9472  lab_files/\
\uc0\u9500 \u9472 \u9472  encrypted_files/\
\uc0\u9500 \u9472 \u9472  restored_files/\
\uc0\u9500 \u9472 \u9472  reports/\
\uc0\u9492 \u9472 \u9472  README.md
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 You run all commands from the 
\f4\b project root
\f3\b0 :
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 cd ransomtest-ransomware-simulator
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\b\fs34 \cf5 ## 2. Add test files to the lab
\f3\b0\fs28 \
\
Put 
\f4\b dummy files
\f3\b0  in 
\f6 lab_files/
\f3 .\
Example:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 lab_files/report_q4.txt\
\
Q4 Financial Report - DUMMY DATA\
Customer: Alice\
Customer: Bob
\f2\fs24 \cf0 \
\
\pard\tx860\tx1420\tx1980\tx2540\tx3100\tx3660\tx4220\tx4780\tx5340\tx5900\tx6460\tx7020\li300\sl324\slmult1\partightenfactor0

\f3\fs28 \cf5 Only files inside 
\f6 lab_files/
\f3  will be processed.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\b\fs34 \cf5 ## 3. Simulate \'93encryption\'94 (safe mode)
\f3\b0\fs28 \
\
This mode does 
\f4\b NOT
\f3\b0  change the original files.
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py --mode encrypt --transform base64 --verbose
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 What happens:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Original file stays the same:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 lab_files/report_q4.txt
\f3 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Simulated encrypted copy is created:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 encrypted_files/report_q4.txt.simenc
\f3 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	An educational ransom note is created:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 lab_files/README_RECOVER.txt
\f3 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	All actions are logged:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 reports/simulation_log.txt
\f3 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\b\fs34 \cf5 ## 4. Simulate \'93decryption\'94 / restore
\f3\b0\fs28 \
\
This reverses the transformation from the encrypted copies.
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py --mode restore --transform base64 --verbose
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 What happens:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Restored file is created:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 restored_files/report_q4.txt
\f3 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	The content should be 
\f4\b identical
\f3\b0  to the original in 
\f6 lab_files/
\f3 .\
\
Your original test file in 
\f6 lab_files/
\f3  is still unchanged.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\b\fs34 \cf5 ## 5. Optional: overwrite originals (more realistic)
\f3\b0\fs28 \
\
\pard\tx860\tx1420\tx1980\tx2540\tx3100\tx3660\tx4220\tx4780\tx5340\tx5900\tx6460\tx7020\li300\sl324\slmult1\partightenfactor0
\cf5 \uc0\u9888  Use only with dummy data, in a lab environment.\
\
If you want the 
\f4\b original files in lab_files/ to look \'93encrypted\'94
\f3\b0 , use:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py --mode encrypt --transform base64 --overwrite-original --verbose
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 Now:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 lab_files/report_q4.txt
\f3  \uc0\u8594  contains the transformed (Base64) content\
	\'95	
\f6 encrypted_files/report_q4.txt.simenc
\f3  \uc0\u8594  encrypted copy\
	\'95	You can still restore from 
\f6 encrypted_files/
\f3  into 
\f6 restored_files/
\f3  with:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf3 python3 simulator.py --mode restore --transform base64 --verbose
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\b\fs34 \cf5 # Quick reference
\f3\b0\fs28 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Modes:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 --mode encrypt
\f3  \uc0\u8594  simulate encryption\
	\'95	
\f6 --mode restore
\f3  \uc0\u8594  simulate decryption\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Transforms:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 --transform reverse
\f3 \
	\'95	
\f6 --transform base64
\f3 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	Safety:\
\pard\tqr\tx500\tx660\li660\fi-660\sl324\slmult1\sb240\partightenfactor0
\cf5 	\'95	
\f6 --dry-run
\f3  \uc0\u8594  show what would happen, no files written\
	\'95	
\f6 --overwrite-original
\f3  \uc0\u8594  overwrite files in 
\f6 lab_files/
\f3  (lab use only)\
	\'95	
\f6 --verbose
\f3  \uc0\u8594  print detailed output}