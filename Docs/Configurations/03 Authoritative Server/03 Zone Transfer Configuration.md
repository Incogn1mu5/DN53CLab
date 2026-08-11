# DNS Zone Transfer (AXFR) - Information Disclosure

A DNS Zone Transfer vulnerability occurs when a Domain Name System (DNS) server is misconfigured to allow unauthorized users to request a complete copy of its zone database using the AXFR protocol. Designed strictly to synchronize DNS records between primary and secondary servers, an unrestricted zone transfer grants attackers direct access to a comprehensive inventory of an organization's network assets—including hidden subdomains, internal IP addresses, mail servers, and staging environments. 



This only happens when admin did not restrict zone transfers to legitimate secondary servers. This Attack usually targets Authoritative Servers where actual records are stored.



## Zone Transfer Configuration

**Misconfigure the Authoritative Server (Admin's mistake)**  

On authoritative server (`192.168.34.133`), edit `named.conf` for the `dnspentest.lab` zone:

```bash
sudo nano /etc/bind/named.conf.local
```

Add:

```
zone "dnspentest.lab" {
 type master;
 file "/etc/bind/zones/dnspentest.lab.zone";
 allow-transfer { any; }; # MISTAKE: Allows ANYONE to transfer the zone
};
```



**Reload BIND**

```bash
sudo rndc reload dnspentest.lab
```



### Perform DNS Zone Transfer Attack

[DNS Zone Transfer Attack](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Attacks%20Guide/02%20DNS%20Zone%20Transfer%20Attack.md)



### NEXT

Configure Authoritative Server for [Dynamic DNS Update Vulnerability](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/03%20Authoritative%20Server/04%20Dynamic%20DNS%20Update%20Configuration.md)


