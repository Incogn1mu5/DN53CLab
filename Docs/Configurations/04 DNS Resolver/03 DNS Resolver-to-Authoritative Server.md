# Configure DNS Resolver to use Authoritative Server

Server-01 (DNS Resolver) is supposed to recursively query Server-02 (Authoritative-Server) when it needs answers for `dnspentest.lab`.

Because `.lab` isn't a public TLD, we need to tell Server-01 where to find that zone.

On Server-01, edit:

```bash
sudo nano /etc/bind/named.conf.local
```

Add:

```
zone "dnspentest.lab" {    
    type forward;    
    forward only;    
    forwarders {        
        192.168.34.133;    
    };
};
```

This tells Server-01:

> "Whenever someone asks for anything in `dnspentest.lab`, forward the query to 192.168.34.133 which our Server-02 (Authoritative Server) IP"

Restart BIND:

```bash
sudo systemctl restart bind9
```

---

## Test the Resolver

On Resolver itself:

```bash
dig @localhost www.dnspentest.lab
dig @127.0.0.1 dnspentest.lab
dig @192.168.34.133 www.dnspentest.lab
dig @192.168.34.133 dnspentest.lab
```

From Kali:

```bash
dig @192.168.34.131 www.dnspentest.lab
dig www.dnspentest.lab
dig dnspentest.lab
```

If any command fails to resolve A record for dnspentest.lab, then execute below commands and try again.

flush the cache:

```bash
sudo rndc flush
sudo rndc flushname dnspentest.lab
```

Restart BIND:

```bash
sudo systemctl restart bind9
```

The flow should be:

```
Kali
↓
Server-01
↓
Server-02
↓
Server-01 caches response
↓
Kali receives answer : www.dnspentest.lab A 192.168.34.134
```



### NEXT

Configure [DNS Resolver to Perform DNS Amplification Attack](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/04%20DNS%20Resolver/04 %20Configure%20Multiple%20Bind9%20Instances.md)


