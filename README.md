# Simple Python Port Scanner

This is a beginner-friendly Python script that scans a set of common network ports on a target IP address or hostname. It checks whether each port is open or closed and prints the results to the console.

## How It Works

The script uses Python's built-in `socket` library to attempt TCP connections to each specified port on the target system. If the connection succeeds, the port is marked as **OPEN**; otherwise, it is **CLOSED**.

## Features

- Scans common ports: 20, 21, 22, 23, 25, 53, 80, 110, 443
- Clear output with status indicators
- Runs on macOS, Linux, or Windows (with Python 3 installed)

## How to Run

1. Clone this repository or download the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using Python 3:

4. Enter a target when prompted (e.g., `scanme.nmap.org`).

## Disclaimer

This tool is for educational and authorized testing purposes only. Do not scan networks or systems without explicit permission.

---

Created by SecureWithCam
