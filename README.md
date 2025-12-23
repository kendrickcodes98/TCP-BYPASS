<div align="center">

# TCP-BYPASS ENGINE

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scapy](https://img.shields.io/badge/scapy-v2.4+-green.svg)](https://scapy.net/)

*An advanced Python-based network analysis toolkit for TCP bypass and penetration testing.*

</div>

---

## ⚠️ **Disclaimer**

**This tool is intended for educational and authorized security testing purposes ONLY.** The author of this software ("Kendrick") is not responsible for any misuse or illegal activity conducted with this script. Users are solely responsible for their actions and must comply with all applicable local, state, and federal laws. Unauthorized access to computer networks is a criminal offense. By using this software, you agree to these terms and assume full legal and ethical responsibility for your actions.

---

## 🎯 Features

Kendricks-Fork is a powerful and versatile script that leverages the `scapy` library to perform low-level network operations. It is designed with both functionality and aesthetics in mind.

- **SYN Flood Attack**: Overwhelms a target's ports with SYN packets to test firewall resilience and perform stress tests.
- **ICMP Tunneling**: Create a covert communication channel by embedding data within ICMP packets.
- **Stealthy Port Scanning**: Identify open ports on a target system using SYN scan techniques to avoid detection.
- **IP Spoofing**: Enhance anonymity by spoofing the source IP address of outgoing packets.
- **Multithreaded Operations**: Utilize multiple threads for high-performance packet flooding.
- **Aesthetic CLI Interface**: Features a clean, colored, and informative command-line interface.

## 📦 Installation

### Prerequisites

- **Python 3.8 or higher**
- **Root/Administrator privileges** (required for raw socket access)
- **Linux** (Recommended, though may work on other OS with adjustments)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Kendricks-Handle/Kendricks-Fork.git
   cd Kendricks-Fork
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

The script requires root privileges to run. Use `sudo` on Linux-based systems.

### Basic Syntax

```bash
sudo python3 tcp_bypass.py -t <TARGET_IP> [OPTIONS]
```

### Options

| Option | Description | Required |
|--------|-------------|----------|
| `-t`, `--target` | Target IP address | Yes |
| `-p`, `--port` | Target port for SYN flood | No (for `--syn-flood`) |
| `-s`, `--spoof` | Spoof source IP address | No |
| `--syn-flood` | Perform a SYN flood attack | No |
| `--icmp-tunnel` | Create an ICMP tunnel | No |
| `--port-scan` | Scan for common open ports (1-1024) | No |

### Examples

1. **Perform a SYN Flood on port 80:**
   ```bash
   sudo python3 tcp_bypass.py -t 192.168.1.10 -p 80 --syn-flood
   ```

2. **Perform a SYN Flood with a spoofed IP:**
   ```bash
   sudo python3 tcp_bypass.py -t 192.168.1.10 -p 22 --syn-flood -s 8.8.8.8
   ```

3. **Start an ICMP tunnel:**
   ```bash
   sudo python3 tcp_bypass.py -t 192.168.1.10 --icmp-tunnel
   ```

4. **Scan a target for open ports:**
   ```bash
   sudo python3 tcp_bypass.py -t 192.168.1.10 --port-scan
   ```

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a patch, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created and maintained by **Kendrick**.

---
