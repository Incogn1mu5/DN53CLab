# 🌐 DNSecLab

### *Understanding DNS Internals & DNS Pentesting Through a Hands-On Lab*

<p align="center">
A practical cybersecurity lab designed to understand how DNS works, how attackers abuse it, and how defenders can detect and mitigate DNS-based attacks.
</p>

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu) ![Bind9](https://img.shields.io/badge/BIND9-DNS_Server-blue?style=for-the-badge) ![Nginx](https://img.shields.io/badge/Nginx-Web_Server-009639?style=for-the-badge&logo=nginx)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-DNS_Pentesting-red?style=for-the-badge) ![Status](https://img.shields.io/badge/Project-Active-success?style=for-the-badge) ![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)

---

# 📖 About

DNSecLab is a self-built cybersecurity laboratory focused on learning **DNS from both the administrator's and attacker's perspective**.

Unlike traditional DNS tutorials, this project demonstrates:

🔹 How DNS actually works
🔹 Recursive vs Authoritative DNS
🔹 Zone Files
🔹 DNS Record Types
🔹 DNS Resolution Process
🔹 DNS Security Concepts
🔹 Common DNS Misconfigurations
🔹 Real-world DNS Pentesting Techniques
🔹 Defensive Mitigations

The goal is to build a strong understanding of DNS while safely demonstrating common attack techniques inside an isolated lab environment.

> [!WARNING]
> This project is built **ONLY** for educational purposes inside an isolated virtual lab.
> 
> No techniques demonstrated here should ever be used against systems without explicit authorization.  
</br>

# 🎯 Objectives

- Learn DNS from scratch
- Understand how recursive resolution works
- Configure authoritative DNS servers
- Host a website using custom DNS
- Perform DNS enumeration
- Identify DNS misconfigurations
- Demonstrate common DNS attacks
- Learn practical mitigation techniques
</br>

# 🖥️ Lab Architecture

```
┌─────────────────────┐ ──────────────────────────────────────────┐
│NAT (192.168.34.0/24 │                                           │
└─────────────────────┘                                           │
│                                                                 │
│    H4CK3R [KALI LINUX]                     Victim [Windows 10]  │
│      (192.168.34.129)                        (192.168.34.130)   │
│            │                                         │          │
│            └───────────────────┬─────────────────────┘          │
│                                │                                │
│                                ▼                                │
│                          DNS Resolver                           │
│                   [Ubuntu Server 26.04 LTS]                     │
│                        (192.168.34.131)                         │
│                                │                                │
│                                │                                │
│                                ▼                                │
│                       Authoritative Server                      │
│                   [Ubuntu Server 26.04 LTS]                     │
│                        (192.168.34.133)                         │
│                                │                                │
│                                │                                │
│                                ▼                                │
│                            Webserver                            │
│                   [Ubuntu Server 26.04 minimized]               │
│                        (192.168.34.134)                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
</br>  

# 📚 Topics Covered

### DNS Fundamentals

- DNS Core Concepts
- DNS Record Types
- The Resolution Process
- Root Servers
- TLD Servers
- Recursive Resolver
- Authoritative DNS
- DNS Cache
- TTL
- Zone Files
- DNS Security Weaknesses
- DNS Attacks
</br>

# 🛠️ Technologies Used

| Component | Technology |
| --- | --- |
| DNS Server | BIND9 |
| Web Server | Nginx |
| Operating System | Ubuntu Server |
| Virtualization | VMware Workstation |
| Attacker Machine | Kali Linux |
| Packet Analysis | Wireshark |
| Enumeration | dig, nslookup, host |
| Pentesting | Nmap |
</br>  

# 🔥 DNS Pentesting Modules

### ✅ Information Gathering

- DNS Enumeration
- Subdomain Enumeration
- Reverse Lookup
- Record Enumeration
</br>

### ✅ Misconfiguration Testing

- Zone Transfer (AXFR)
- Open Recursive Resolver
- DNS Cache Inspection
- Weak DNS Configuration
</br>

### ✅ Attack Demonstrations

- DNS Enumeration & Reconnaissanc
- DNS Amplification (Controlled Demonstration)
- DNS Zone transfer
- Dynamic DNS Update
- DNS Hijacking Concepts
</br>

### 🛡️ Defensive Concepts

- Restrict Zone Transfers
- Disable Open Recursion
- Response Rate Limiting (RRL)
- DNSSEC Overview
- Logging & Monitoring
- Least Privilege Configuration
</br>

# 📂 Project Structure

```
DNSecLab/

├── Documentation/
│    ├── DNS Fundamentals
│    ├── DNS Attacks 
│    └── Configuration/
│        ├── Network Configuration
│        ├── DNS Resolver Configuration
│        │   ├── Multiple Bind9 Instance Configuration
│        │   └── Static IP Configuration
│        ├── Authoritative Server Configuration
│        │   └── Static IP Configuration
│        ├── Webserver Configuration
│        │   └── Static IP Configuration
│        ├── Victim Machine Configuration
│        │   └── Static IP Configuration
│        ├── Attacker Machine Configuration
│        │   └── Static IP Configuration
│        └── Malicious Server Configuration
│
├── Inventory/
│    ├── Diagrams
│    ├── Screenshots
│
├── Report/
│    ├── DNS Reconnaisance & Enumeration
│    ├── DNS Zone Transfer
│    ├── DNS Amplification Attack
│    ├── Dynamic DNS Update (DDNS)
│    
│    ├── DNS Hijacking
│    └── Mitigations
│
└── README.md
```

---

# 📖 Learning Outcomes

By completing this lab you will understand:

✅ How DNS works internally

✅ How recursive and authoritative servers interact

✅ How websites are resolved

✅ How attackers enumerate DNS

✅ How DNS misconfigurations occur

✅ How common DNS attacks work

✅ How organizations secure DNS infrastructure
</br>  

# 🚀 Future Improvements

- [ ] DNSSEC Implementation
- [ ] Split DNS
- [ ] Response Rate Limiting
- [ ] Passive DNS Monitoring
- [ ] DNS Logging Dashboard
- [ ] Additional Attack Scenarios
- [ ] Detection Engineering
- [ ] Blue Team Monitoring

</br>  

# 🤝 Contributing

Suggestions and improvements are always welcome.

Feel free to:

- Open an Issue
- Submit a Pull Request
- Share feedback

## Author

---

Incogn1mu5

## License

This project is licensed under the Apache License 2.0.

You are welcome to use, study, modify, and redistribute this project in accordance with the license terms. If you create derivative works, please retain the original copyright notice, include the Apache License 2.0, and clearly indicate any modifications.

See the [LICENSE](https://github.com/Incogn1mu5/PwnAD/blob/7091ec910e02949ee20d522bb7605f83cdeae6d0/LICENSE) file for full details.

</div>
