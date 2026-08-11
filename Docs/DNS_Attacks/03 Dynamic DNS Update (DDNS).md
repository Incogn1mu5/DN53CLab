# Dynamic DNS Update Injection Attack (DDNS)

Dynamic DNS (DDNS) is a feature that lets clients or servers automatically update DNS records via **RFC 2136 DNS UPDATE** messages — instead of an admin manually editing zone files, a host can say "hey authoritative server, update my A record to this new IP" (common in DHCP environments, VPNs, IoT devices). A DDNS attack exploits weak or missing authentication on that update mechanism to inject or alter records the attacker shouldn't control.

## How it works

**Normal DDNS flow**: A client sends a signed `UPDATE` message to the authoritative server (e.g., "update `host.dnseclab.com` A record to 10.0.0.5"). The server verifies a shared secret (TSIG key) before accepting it.

> Figure

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DDNS/Legit_Update.png" alt="Legitimate Update" width="1484" height="552">



**The vulnerability**: If the zone allows updates from **any source** (`allow-update { any; }`) or uses a **weak/no TSIG key**, anyone who can reach the server on port 53 can send their own forged `UPDATE` message.

**The attack**: An attacker crafts a DNS UPDATE packet claiming authority to modify a record — e.g., pointing `mail.company.com` or `vpn.company.com` to an attacker-controlled IP. If the server accepts it, that malicious mapping propagates to every client that resolves the name.

> Figure

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DDNS/Malicious_Update.png" alt="Malicious Update" width="1484" height="552">



### Impact

1. Traffic redirection (phishing/MITM), record injection (adding a rogue NS or A record), or record deletion (denial of service on that hostname) — all without touching the resolver's cache logic (unlike cache poisoning, this attacks the *authoritative* data directly).

2. If a system administrator only checks the static zone file to audit for changes (thinking it contains all records), they will be **completely blind** to an active DDNS attack. The `.jnl` file is binary and unreadable to humans, so they won't see the rogue record unless they run `rndc sync` or query the live server.

The key difference from cache poisoning: cache poisoning forges a *response* to trick a resolver into caching bad data temporarily. A DDNS attack modifies the *authoritative source record* itself, persistently, by abusing weak update authentication — it's essentially unauthorized zone-write access.








