# Configure DNS Resolver

DNS resolver helps computer to find domain IP by recursively quering to root server, .TLD server and Authoritative Server.

## Install Ubuntu Server

OS: Ubuntu Server 26.04 LTS

Install BIND9 on Authotitative server

```bash
sudo apt update && upgrade -y

sudo apt install bind9 bind9utils bind9-doc dnsutils -y
```

## Configure as Open Resolver

Configure BIND9 to be an Open Resolver:

```bash
sudo nano /etc/bind/named.conf.options
```

Add:

```
options {
    directory "/var/cache/bind";

    # Critical for open resolver status
    recursion yes;
    allow-query { any; };
    allow-query-cache { any; };

    # Listen on port 53 for all interfaces
    listen-on port 53{ any; };
    listen-on-v6 port 53{ any; };

    # Use forwarders for internet resolution
    forwarders {
        8.8.8.8;
        1.1.1.1;
        9.9.9.9;
    };

    dnssec-validation no;  # Disable DNSSEC for maximum amplification

    # Tweak for performance
    max-cache-size 100M;
    minimal-responses no;   # Return full responses

    # Enable EDNS for larger packets
    edns-udp-size 4096;
    max-udp-size 4096;
};
```

## Create the directory for log and data cache

BIND runs as user 'bind', needs ownership to write files

```bash
# For Log
sudo mkdir -p /var/log/named

#Set ownership to BIND user & group
sudo chown bind:bind /var/log/named

# For cache data
sudo mkdir -p /var/cache/bind/data

# Set ownership to BIND user & group
sudo chown bind:bind /var/cache/bind
sudo chown bind:bind /var/cache/bind/data
```

- `chown bind:bind` = Owner:bind, Group:bind

## Set directory permissions

```bash
sudo chmod 755 /var/log/named
sudo chmod 755 /var/cache/bind
sudo chmod 755 /var/cache/bind/data
```

- `755(rwxr-xr-x)` = User:rwx, Group:r-x, Others:r-x (owner can read/write/execute, others can read/execute)

## Enable query logging (for monitoring)

```bash
sudo nano /etc/bind/named.conf
```

```
logging {
    channel default_debug {
        file "/var/log/named/named.run" versions 3 size 10M;
        severity dynamic;
    };
};
```

---

## Check config for syntax errors

```bash
#Check for configuration error
sudo named-checkconf

#Restart BIND9
sudo systemctl restart bind9
sudo systemctl enable bind9


#Check status
sudo systemctl status bind9
```

Verify it's listening on port 53

```bash
sudo ss -tulpn | grep :53
```

start named.service

```bash
sudo systemctl start named
```

You may encounter error regarding port or named.service, to resolve the errors refer:

- [Port Conflict Troubleshoot]()

- [named service Troubleshoot]()

## 

## Verify Your Open Resolver Works

Test from the DNS server itself:

```bash
dig @127.0.0.1 google.com
dig @localhost google.com ANY
```

Test from another VM (Kali or Windows) on the same NAT network:

```bash
# From Kali VM (192.168.34.129)
dig @192.168.56.10 google.com
dig @192.168.56.10 google.com ANY


You should get full responses!
```

---

### NEXT

Configure DNS resolver to use static IP address 

[IP Configuration for DNS Resolver](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/05%20DNS%20Resolver/02%20IP%20Configuration.md) 
