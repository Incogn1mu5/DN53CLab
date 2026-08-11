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

### 

## Dynamic DNS Update Configuration

To make changes in configurations, make sure to stop bind:

```bash
sudo systemctl stop named
```

Create directory for zone 

```bash
sudo mkdir -p /etc/bind/zones
```



**Misconfigure the Authoritative Server (Admin's mistake)** 
On your authoritative server (`192.168.34.133`), edit `named.conf` for the `dnspentest.lab` zone:

```bash
sudo nano /etc/bind/named.conf.local
```

Add:

```bash
zone "dnspentest.lab" {
    type master;
    file "/etc/bind/zones/dnspentest.lab.zone";  #separate zone folder and file
    allow-update { any; };   # MISTAKE: Allows anyone to update records
};
```



Copy Records from zone file to new Zone file (**Journal File [`.jnl`]**) to handle dynamic updates on BIND.

```bash
sudo cp /etc/bind/db.dnspentest.lab /var/lib/bind/zones/dnspentest.lab.zone
```

>  ![Note]
> 
> Dynamic updates require the zone file to be writable by the BIND user. Ensure the file permissions allow writes:



Give the 'bind' user full ownership of this directory and file

```bash
sudo chown -R bind:bind /var/lib/bind/zones
sudo chown bind:bind /etc/bind/zones/dnspentest.lab.zone
```

Make sure the file is writable

```bash
sudo chmod 644 /etc/bind/zones/dnspentest.lab.zone
```

Reload BIND:

```bash
sudo rndc reload dnspentest.lab
#OR
sudo rndc reload
```

Start BIND again

```bash
sudo systemctl start named
```



### Perform Dynamic DNS Update Injection Attack

[Dynamic DNS Update Attack](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Attacks%20Guide/03%20Dynamic%20DNS%20Update%20Attack.md)


### NEXT
Configure [DNS Resolver](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/04%20DNS%20Resolver/01%20Open%20DNS%20Resolver%20Configuration.md)
