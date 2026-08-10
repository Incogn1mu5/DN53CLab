# 🗝️ DNS Fundamentals

### What is DNS?  

The Domain Name System (DNS) also considered as "The Phonebook of the Internet" is the hierarchical and decentralized naming system used to identify computers, services, and other resources reachable through the Internet or other Internet Protocol (IP) networks. 
Think of it as the **phonebook of the Internet**—it translates human-readable domain names (like `www.dnseclab.com`) into machine-readable IP addresses (like `192.0.2.1`) that computers use to communicate with each other.  
</br>  

### The Problem DNS Solves
- **Without DNS:** Users would need to memorize numerical IP addresses for every website they visit—impossible given that there are billions of websites.

- **With DNS:** Users type memorable domain names, and DNS handles the translation automatically.
</br>  

### DNS Core Concepts
> Key Terminology

| Term | Definition |
| --- | --- |
| **Domain Name** | A human-readable identifier for a resource on the Internet (e.g., `www.google.com`) |
| **IP Address** | A numerical label assigned to each device connected to a network (e.g., `142.250.190.46`) |
| **Resolver** | A DNS server that receives queries from clients and resolves them by querying other servers |
| **Authoritative Server** | A DNS server that holds the actual DNS records for a specific domain |
| **Root Server** | The top-level DNS servers that provide the starting point for DNS resolution |
| **TLD Server** | Top-Level Domain server that handles specific extensions (.com, .org, .edu, etc.) |

### DNS Record Types

| Record Type | Purpose | Example |
| --- | --- | --- |
| **A** | Maps a domain name to an IPv4 address | `www.dnseclab.com → 192.0.2.1` |
| **AAAA** | Maps a domain name to an IPv6 address | `www.dnseclab.com → 2001:db8::1` |
| **MX** | Specifies mail servers for the domain | `dnseclab.com → mail.dnseclab.com` |
| **NS** | Delegates a DNS zone to an authoritative server | `dnseclab.com → dnseclab.com` |
| **CNAME** | Aliases one domain name to another | `www.dnseclab.com → dnseclab.com` |
| **TXT** | Holds text information (SPF, DKIM, etc.) | `v=spf1 mx include:...` |
| **SOA** | Start of Authority—contains administrative information | Zone configuration metadata |
| **PTR** | Reverse DNS lookup (IP to domain) | `1.0.0.127.in-addr.arpa → localhost` |
</br>  

---

## How DNS Works: The Resolution Process
> The Complete Query Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌───────────────┐
│   Client    │     │  Resolver   │     │   Root      │     │   TLD       │     │ Authoritative │
│  (Browser)  │     │ (Recursive) │     │   Server    │     │   Server    │     │     Server    │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘     └──────┬──────┘     └──────┬────────┘
       │                   │                   │                   │                   │
       │   1. Query        │                   │                   │                   │
       │ "www.dnseclab.com │                   │                   │                   │
       │   A?"             │                   │                   │                   │
       │──────────────────>│                   │                   │                   │
       │                   │                   │                   │                   │
       │                   │   2. Query Root   │                   │                   │
       │                   │   ".com TLD?"     │                   │                   │
       │                   │──────────────────>│                   │                   │
       │                   │                   │                   │                   │
       │                   │   3. Referral     │                   │                   │
       │                   │   "Ask .com TLD   │                   │                   │
       │                   │    at a.gtld.net" │                   │                   │
       │                   │<──────────────────│                   │                   │
       │                   │                   │                   │                   │
       │                   │   4. Query TLD    │                   │                   │
       │                   │  "dnseclab.com?"  │                   │                   │
       │                   │──────────────────────────────────────>│                   │
       │                   │                   │                   │                   │
       │                   │   5. Referral     │                   │                   │
       │                   │  "Ask ns1.dnseclab│                   │                   │
       │                   │    .com at 192.0. │                   │                   │
       │                   │    2.1"           │                   │                   │
       │                   │<──────────────────────────────────────│                   │
       │                   │                   │                   │                   │
       │                   │   6. Query Auth   │                   │                   │
       │                   │  "www.dnseclab.com│                   │                   │
       │                   │    A?"            │                   │                   │
       │                   │───────────────────────────────────────────────────────>   │
       │                   │                   │                   │                   │
       │                   │   7. Response     │                   │                   │
       │                   │   "192.0.2.1"     │                   │                   │
       │                   │<───────────────────────────────────────────────────────   │
       │                   │                   │                   │                   │
       │   8. Response     │                   │                   │                   │
       │   "192.0.2.1"     │                   │                   │                   │
       │<──────────────────│                   │                   │                   │
```

### Step-by-Step Breakdown

> Step 1: Client Query

- A user types `www.dnseclab.com` into their browser.
- The client's operating system sends a DNS query to its configured recursive resolver (usually provided by the ISP or a public resolver like Google's 8.8.8.8).

> Step 2: Root Server Query

- The resolver checks its cache. If it does not have the answer, it sends a query to one of the 13 root servers (managed by ICANN).
- The resolver asks: *"Where can I find the authoritative server for .com?"*

> Step 3: Root Server Referral

- The root server does not know the IP of `www.dnseclab.com`, but it knows the TLD servers for `.com`.
- It responds with a referral: *"Ask the .com TLD server at a.gtld.net."*

> Step 4: TLD Server Query

- The resolver queries the .com TLD server: *"Where can I find the authoritative server for dnseclab.com?"*

> Step 5: TLD Server Referral

- The .com TLD server responds: *"Ask ns1.dnseclab.com (the authoritative server) at 192.0.2.1."*

> Step 6: Authoritative Server Query

- The resolver queries the authoritative server: *"What is the A record for www.dnseclab.com?"*

> Step 7: Authoritative Server Response

- The authoritative server responds with the IP address: *"www.dnseclab.com A 192.0.2.1"*

> Step 8: Client Response

- The resolver caches the response and returns the IP address to the client's browser.
- The browser can now connect to `192.0.2.1` to load the webpage.
</br>

## Recursive vs. Authoritative DNS Servers

### Recursive Resolver

A recursive resolver accepts queries from clients and **does all the work** of finding the answer by traversing the DNS hierarchy.

```
┌─────────────────────────────────────────────────────────┐
│              Recursive Resolver                         │
│                                                         │
│  Client asks: "www.dnseclab.com A?"                     │
│                                                         │
│  1. Check cache ▸ [No result]                           │
│  2. Ask Root ▸ "Where is .com?"                         │
│  3. Ask .com TLD ▸ "Where is dnseclab.com?"             │
│  4. Ask ns1.dnseclab.com ▸ "www.dnseclab.com IP?"       │
│  5. Return to client: "192.0.2.1"                       │
│                                                         │
│  "I will do all the work for you."                      │
└─────────────────────────────────────────────────────────┘
```

### Authoritative Server

An authoritative server **only responds to queries about domains it knows**. It does not query other servers.

```
┌─────────────────────────────────────────────────────────┐
│           Authoritative Server (ns1.dnseclab.com)       │
│                                                         │
│  Resolver asks: "www.dnseclab.com A?"                   │
│                                                         │
│  1. Check zone file ▸ "www.dnseclab.com A 192.0.2.1"    │
│  2. Return response directly                            │
│                                                         │
│  "I only know about domains I am authoritative for."    │
└─────────────────────────────────────────────────────────┘
```
</br>  

## DNS Caching: Performance at the Cost of Staleness

Caching is what makes DNS fast but also enables attacks like cache poisoning.

### How Caching Works

```
 ┌─────────────┐     ┌─────────────┐   ┌───────────┐      ┌───────────────┐
 │   Client    │     │   Resolver  ├──►│Root Server│      │ Authoritative │
 │             │     │   (Cache)   │   └─────┬─────┘      │    Server     │
 └──────┬──────┘     └──────┬──────┘    ┌────▼─────┐      └─▲────┬────────┘
        │                   │           │TLD server├────────┘    │         
        │   1. Query        │           └──────────┘             │         
        │  "dnseclab.com A" │                                    │         
        │──────────────────>│                                    │         
        │                   │ 2. Missing Cache, Fetch from       │         
        │                   │    Authoritative Server            │         
        │                   ├──────────────────────────────────► │         
        │                   │                                    │         
        │                   │ 3. Response "192.0.2.1"            │         
        │                   │    TTL: 300s                       │         
        │                   │◄───────<────────<─────────<────────┤         
        │                   │                                    │         
        │              4. Store in                               │         
        │              Cache (300s)                              │         
        │                   │                                    │         
        │    5. Response    │                                    │         
        │    "192.0.2.1"    │                                    │         
        │◄──<────<─────<────│                                    │         
        │                   │                                    │         
        │  6. Same Query    │                                    │         
        │ "dnseclab.com A"  │                                    │         
        │──────────────────►│                                    │         
        │                   │                                    │         
        │              7. Cache Hit                              │         
        │              Return stored                             │         
        │              "192.0.2.1"                               │         
        │                   │                                    │         
        │   8. Response     │                                    │         
        │   "192.0.2.1"     │                                    │         
        │◄──────<─────<─────│                                    │         
```

### TTL (Time To Live)

- The TTL value (in seconds) tells resolvers **how long to cache** a DNS record.
- Short TTL (e.g., 5 seconds): Frequent updates, but more query overhead.
- Long TTL (e.g., 86400 seconds / 24 hours): Efficient caching, but slow to propagate changes.
</br>

## DNS Security: The Weaknesses

### The Core Vulnerability

DNS was designed in the 1980s when the Internet was a small, trusted network. Security was not a primary concern. This has led to several inherent weaknesses:

| Weakness | Why It's a Problem |
| --- | --- |
| **UDP Transport** | Easy to spoof source IP addresses |
| **No Authentication** | Resolvers accept responses from ANY IP |
| **Transaction IDs** | Only 16 bits (65,535 possible values) → Brute-forceable |
| **Source Port** | Predictable or fixed → Reduces entropy |
| **Cache Manipulation** | Poisoned cache affects ALL users of the resolver |
</br>  

## DNS Attack Surface

### Diagram: How an Attacker Can Intercept DNS

```
                    ┌─────────────────────────────────────┐
                    │         Attacker (Kali)             │
                    │         192.168.34.129              │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┴───────────────────┐
                    │                                     │
                    ▼                                     ▼
┌─────────────────────────┐                  ┌─────────────────────────┐
│  Attack Vector 1        │                  │  Attack Vector 2        │
│  ARP Spoofing           │                  │  Cache Poisoning        │
│  (Local Network)        │                  │  (DNS Level)            │
└─────────────────────────┘                  └─────────────────────────┘
                    │                                     │
                    ▼                                     ▼
┌─────────────────────────┐                  ┌─────────────────────────┐
│  Intercept DNS Queries  │                  │  Inject Spoofed         │
│  to Resolver            │                  │  Responses              │
└─────────────────────────┘                  └─────────────────────────┘
                    │                                     │
                    └─────────────────┬───────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │       DNS Resolver (Target)         │
                    │        192.168.34.132               │
                    └─────────────────────────────────────┘
                                      │
                                      │ Queries forwarded
                                      ▼
                    ┌─────────────────────────────────────┐
                    │     Authoritative Server (Trusted)  │
                    │        192.168.34.133               │
                    └─────────────────────────────────────┘
```
</br>  

## DNS Attack Classification

> Cache Poisoning (The Kaminsky Attack)

An attacker injects a fake DNS response into a resolver's cache, redirecting legitimate users to malicious websites.

> DNS Amplification (DDoS)

Attackers use open resolvers to amplify their bandwidth, overwhelming a victim with massive traffic.

> Zone Transfer (Information Disclosure)

Misconfigured authoritative servers allow attackers to download the entire zone file.

> Dynamic Update Injection (Record Hijacking)

Attackers directly modify DNS records on the authoritative server.

> DNS Tunneling (Data Exfiltration)

Attackers encode data inside DNS queries to bypass firewalls and extract sensitive information.

> DNS Rebinding (Same-Origin Policy Bypass)

Attackers exploit short TTLs to trick browsers into connecting to malicious IPs.  

</br>  

## DNS in DN53CLab: Architecture Overview

DN53CLab replicates a realistic enterprise DNS infrastructure to demonstrate these vulnerabilities in a controlled environment.

> Figure

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              DNSecLab Architecture  (NAT Adapter 192.168.34.0/24)       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────┐                                                        │
│  │  Victim Client (Windows 10) │                                                        │
│  │     (192.168.34.130)        │                                                        │
│  └───────────────────┬─────────┘                                                        │
│                 ▲    │                                                                  │
│ dnspentest.lab  │   Sends Query: "www.dnspentest.lab"                                   │
│     is at       │    │                                                                  │
│  192.168.34.134 │    ▼                                                                  │
│  ┌──────────────┴──────────────┐    Forwarding Zone    ┌───────────────────────────┐    │
│  │   DNS Resolver (Target)     │ ── dnspentest.lab ──> │ Authoritative Server      │    │
│  │   (Ubuntu Server 26.04 LTS) │                       │ (Ubuntu Server 26.04 LTS) │    │
│  │   192.168.34.131            │                       │ 192.168.34.133            │    │
│  │                             │                       │                           │    │
│  │ Vulnerabilities:            │                       │ Vulnerabilities:          │    │
│  │  • Open Recursive           │    Response with IP   │  • Zone Transfer (AXFR)   │    │
│  │  • No DNSSEC                │ ◄─────────────────────┤  • Dynamic Updates        │    │
│  │  • No Rate Limiting         │                ┌────► │                           │    │
│  └─────────────────────────────┘                │      └───────────────┬───────────┘    │
│                 ▲                               │                      │                │
│                 │                               │         ┌────────────┴────────────┐   │
│                 │                               │         │Zone for dnspentest.lab  │   │
│        Malicious Query                          └─────────┤pointing (192.168.34.134)│   │
│                 │                                         └───────────────────┬─────┘   │
│  ┌──────────────┴──────────────┐                                              │         │
│  │   Attacker (Kali Linux)     │                                              │         │
│  │   192.168.34.129            │                                              │         │
│  │                             │                                              │         │
│  │ Attacks:                    │                      ┌────────────────┐      │         │
│  │  • DNS Amplification        │                      │Real Web Server │      │         │
│  │  • Zone Transfer            │                      │ dnspentest.lab │ ◄────┘         │
│  │  • DDNS Injection           │                      │192.168.34.134  │                │
│  │                             │                      └────────────────┘                │
│  └─────────────────────────────┘                                                        │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

## Why DNS is Hard to Secure

1. **Backward Compatibility**: Many features (like `ANY` queries, no authentication) are baked into the protocol.
2. **Performance vs. Security**: Encryption (DNS-over-HTTPS, DNS-over-TLS) adds latency.
3. **Distributed Trust**: No single authority controls all of DNS.
4. **Ubiquitous Dependency**: Breaking DNS breaks everything on the Internet.

## Best Practices for Securing DNS (Mitigations)

| Security Measure | Prevents |
| --- | --- |
| **DNSSEC** | Cache poisoning (validates responses) |
| **Rate Limiting** | Amplification attacks |
| **Restrict Recursion** | Open resolver abuse |
| **Source Port Randomization** | Makes cache poisoning harder |
| **ACLs for Zone Transfers** | Information disclosure |
| **TSIG/DNS over TLS** | Zone transfer security, privacy |
| **Regular Patching** | Exploits against known CVEs |
| **Monitoring & Logging** | Early detection of attacks |

## Summary

DNS is the **critical infrastructure** that makes the Internet usable by translating human-readable names into machine-readable IP addresses. However, its original design from the 1980s lacks security considerations, making it a prime target for attackers.

DNSecLab demonstrates six major attack vectors against DNS infrastructure using a **realistic BIND 9.16.0 , BIND 9.20.18 deployment**, highlighting the importance of proper configuration, regular patching, and proactive security monitoring.
