# 🛡️ Python Network Honeypot (Blue Team)

**Author:** S.A. Nikam  
**Domain:** Cybersecurity / Threat Intelligence  
**Language:** Python 3.x

## 📖 Overview
This project is a **Low-Interaction Honeypot** designed to detect and log unauthorized intrusion attempts on an internal network. It simulates a vulnerable SSH service to lure attackers, captures their credentials, and generates forensic logs for threat analysis.

## 🚀 How It Works
1.  **The Trap:** The script listens on a TCP port (e.g., 2222).
2.  **The Lure:** It sends a fake server banner (e.g., `SSH-2.0-OpenSSH_8.2p1 Ubuntu`) to trick scanners like Nmap.
3.  **The Capture:** When an intruder attempts to login, the script records their IP address and the payload (username/password) to a log file.

## 🛠️ Usage
1.  Run the script: `python honeypot.py`
2.  The system will start listening on `0.0.0.0:2222`.
3.  Any connection attempts will be logged to `honeypot_attacks.log`.

## ⚠️ Disclaimer
This tool is for **Educational and Defensive purposes only**. It is designed to run on own infrastructure to detect intruders.