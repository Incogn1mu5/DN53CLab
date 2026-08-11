# DNS Zone Transfer Attack

DNS Zone Transfer is the process where a secondary DNS server copies the entire zone file from the primary. If an administrator mistakenly leaves `allow-transfer` open to `any` (or to the attacker's IP), an attacker can dump **every single record** for the domain—including internal IPs, hidden subdomains, and server hostnames.

## Attack Guide

On Kali (192.168.34.129), run this single command:

```bash
dig @192.168.34.133 dnspentest.lab AXFR
```

Observe the Results**  

You will receive the complete zone file:

> Figure 

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Zone%20Transfer/Zone_Transfer-Proof.png" alt="DN53CLab_Banner" width="1484" height="552">

**Why this is dangerous:**

- The attacker discovers the real webserver (`192.168.34.134`), the DNS admin interface (`10.0.0.5`), and internal API servers that were never meant to be public.

- This reconnaissance directly enables further attacks.

- By exposing this structural blueprint without requiring complex brute-force techniques, the misconfiguration drastically reduces the effort needed for target reconnaissance and significantly accelerates the planning of subsequent network attacks.
