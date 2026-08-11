# DNS Reconnaissance & Enumeration

Here is standard methodology used in penetration testing (with authorization) and security research. 

> [!CAUTION]
> 
> Only run active enumeration against domains you own or have explicit written permission to test — DNS recon against third parties without authorization can violate computer misuse laws even though the queries themselves are "public." 

## 1. Passive Reconnaissance

no direct interaction with target's DNS

##### WHOIS lookups

```bash
whois example.com
```

Reveals registrar, registration dates, name servers, sometimes registrant contact info (often redacted by privacy services now).

##### 

##### Certificate Transparency logs

Find subdomains without touching the target at all — CT logs are public records of issued TLS certs.

```bash
# crt.sh via curl
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sort -u
```

Web UI alternative: [https://crt.sh](https://crt.sh)

#### 

##### Search-engine / OSINT subdomain discovery

`theHarvester` — pulls from search engines, PGP key servers, CT logs, etc.

```bash
theHarvester -d example.com -b all
```

` Shodan / Censys` — search for hosts and certs tied to the domain

```bash
shodan search hostname:example.com
```

### 

## 2. Active DNS Enumeration

##### Basic record queries with DIG

**DIG** (Domain Information Groper) is a flexible, open-source **command-line tool** used for querying **Domain Name System (DNS)** servers to troubleshoot network issues and retrieve domain records.

```bash
dig example.com ANY          # some modern resolvers ignore ANY
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
dig example.com SOA
dig example.com CNAME
```

##### quick alternative)`nslookup`

**Nslookup** (Name Server Lookup) is a **command-line utility** available on Windows, Linux, and macOS used to **query DNS servers** for domain name-to-IP address mappings and other DNS records.

```bash
nslookup -type=MX example.com
nslookup -type=NS example.com
```

##### host `command`

The **host** command is a lightweight, command-line utility used to query **DNS** servers, primarily on **Linux** and **Unix** systems, to resolve domain names to IP addresses (A/AAAA records) and vice versa (reverse lookups).

```bash
host -t txt example.com
host -a example.com   # equivalent to ANY  
```

##### Zone transfer attempt (AXFR) — misconfiguration check

```bash
dig axfr example.com @ns1.example.com
```

If this succeeds, the server is misconfigured and dumps the entire zone. Almost always disabled on properly configured servers, but worth checking.

## 

## 3. Automated Enumeration Tools

##### dnsrecon

Combines many of the above techniques automatically.

```bash
dnsrecon -d example.com -a          # AXFR check
dnsrecon -d example.com -t brt      # brute force subdomains
dnsrecon -d example.com -t std      # standard enum (NS, SOA, MX, TXT, etc.)
```

##### dnsenum

```bash
dnsenum example.com
dnsenum --dnsserver ns1.example.com example.com
```

##### fierce

Good for quick subdomain discovery + adjacent IP scanning.

```bash
fierce --domain example.com
```

##### amass (OWASP) — the modern go-to

Combines passive sources (CT logs, APIs, scraping) and active brute forcing/permutation.

```bash
amass enum -passive -d example.com
amass enum -active -d example.com -brute -w /usr/share/wordlists/subdomains.txt
amass intel -d example.com     # org/ASN discovery
```

##### subfinder ([ProjectDiscovery](https://github.com/projectdiscovery/subfinder))

Fast passive subdomain enumeration from many APIs.

```bash
subfinder -d example.com -all -o subs.txt
```

##### gobuster

Subdomain brute forcing tool

```bash
gobuster dns -d example.com -w /usr/share/wordlists/subdomains-top1million.txt -t 50
```

##### massdns

high-speed resolver, pairs with wordlists

```bash
massdns -r resolvers.txt -t A -o S -w results.txt subdomains.txt
```

## 

## 4. Reverse DNS & Network Range Mapping

```bash
dig -x 93.184.216.34                 # reverse lookup single IP
whois 93.184.216.34                  # find ASN / netblock owner
```

For a whole range, tools like `dnsrecon -r <CIDR>` or `nmap -sL <CIDR>` can do bulk reverse lookups.

## 

## 5. DNSSEC Checks

```bash
dig +dnssec example.com
dig DNSKEY example.com
```

Useful to see if the zone is signed, and can reveal misconfigurations.

### 

## 6. Wildcard Detection (avoid false positives in brute forcing)

Before brute-forcing subdomains, check if the domain uses a wildcard DNS record — it'll make every guess "resolve," creating false positives.

```bash
dig random-nonexistent-subdomain12345.example.com
```

If it returns an IP, wildcard DNS is active — tools like `amass` and `gobuster dns` have built-in wildcard filtering.

## 
