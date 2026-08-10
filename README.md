<img width="1484" height="552" alt="DN53CLab_Banner" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DN53CLab_Banner.png" />

[![Kali Linux](https://img.shields.io/badge/Kali%20Linux-557C94?logo=kalilinux&logoColor=black)](https://www.kali.org/get-kali/#kali-virtual-machines) [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/download/server) [![nginx](https://img.shields.io/badge/nginx-009639?logo=nginx&logoColor=fff)](https://nginx.org/en/download.html) 
<a href="https://www.isc.org/bind/"><img src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/bind9logo.png" height="20" alt="Bind9"></a>
![Pentesting](https://img.shields.io/badge/Focus%20Pentesting-black?logo=owasp&logoColor=red)
![Pentesting](https://img.shields.io/badge/Red%20Team-black?logo=hackthebox&logoColor=red)
![Project Status](https://img.shields.io/badge/Project-Active-brightgreen?logo=statuspage&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?logo=apache&logoColor=white)


<!-- ![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu) ![Bind9](https://img.shields.io/badge/BIND9-DNS_Server-blue?style=for-the-badge) ![Nginx](https://img.shields.io/badge/Nginx-Web_Server-009639?style=for-the-badge&logo=nginx)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-DNS_Pentesting-red?style=for-the-badge) ![Status](https://img.shields.io/badge/Project-Active-success?style=for-the-badge) ![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)
![Project Status](https://img.shields.io/badge/Project-Active-black)
![License](https://img.shields.io/badge/License-Apache%202.0-black)
-->
---
# 🌐 DN53CLab
A vulnerable DNS environment designed to understand how DNS works, how attackers abuse it and how defenders can detect & mitigate DNS-based attacks. Yes, that's a "53" in there — DN**53**CLab, pronounced "DNSecLab", because Port 53 is where all the fun happens.

DN53CLab is a self-built cybersecurity laboratory focused on learning **DNS from both the administrator's and attacker's perspective**.

Unlike traditional DNS tutorials, this project demonstrates:

🔹 How DNS actually works </br>🔹 Recursive vs Authoritative DNS </br>🔹 Zone Files </br>🔹 DNS Record Types </br>🔹 DNS Resolution Process </br>🔹 DNS Security Concepts </br>🔹 How DNS is Configured </br>🔹 Common DNS Misconfigurations </br>🔹 Real-world DNS Pentesting Techniques </br>🔹 Defensive Mitigations. 

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

| Component | Technology 
| --- | --- 
| DNS Server | BIND9 
| Web Server | Nginx 
| Operating System | Ubuntu Server 
| Virtualization | VMware Workstation 
| Attacker Machine | Kali Linux 
| Victim Machine | Windows 10
</br>  

# 🔥 DNS Pentesting Modules

### ✅ Information Gathering

- DNS Enumeration
- Subdomain Enumeration
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
DN53CLab/

├── Documentation/
│    ├── DNS Fundamentals
│    ├── DNS Attacks 
│    └── Configuration/
│        ├── Network Configuration
│        ├── DNS Resolver/
│        │   ├── Open DNS Resolver Configuration
│        │   └── Multiple Bind9 Instance Configuration
│        ├── Authoritative Server/
│        │   └── Authoritative Server Configuration
│        ├── Webserver/
│        │   └── Webserver Configuration
│        ├── Victim_Machine/
│        │   └── Windows 10 Configuration
│        ├── Attacker_Machine/
│        │   └── Kali Linux Configuration
│        └── Malicious Server Configuration
│
├── Inventory/
│    ├── Diagrams
│    └── Screenshots
│
├── Report/
│    ├── DNS Reconnaisance & Enumeration
│    ├── DNS Zone Transfer
│    ├── DNS Amplification Attack
│    ├── Dynamic DNS Update (DDNS)
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
</br>  

## License

This project is licensed under the Apache License 2.0.

You are welcome to use, study, modify, and redistribute this project in accordance with the license terms. If you create derivative works, please retain the original copyright notice, include the Apache License 2.0, and clearly indicate any modifications.

See the [LICENSE](https://github.com/Incogn1mu5/DN53CLab/blob/main/LICENSE) file for full details.  
</br>  

## Author

Incogn1mu5
