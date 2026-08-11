# Interface and IP Setup for Kali Linux

This document is to configure Kali Linux (attacker) to use static IP address while using custom VMware's NAT Adapter (DHCP Enabled)

## Setup Interface

To make Kali Linux communicate locally, make sure to connect it with interface created during Virtual Network Configuration.

Follow given steps to configure Kali Linux to use custom interface

step 1: Edit Virtual Machine Settings

step 2: Click Network Adapter

step3: Select NAT

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Kali%20Linux/Custom-Interface.png" alt="Interface Setup" width="1484" height="552">



## Configure DNS nameserver for Kali Linux

Configure Kali to use Local DNS Resolver

First stop NetworkManager to prevent interruption

```bash
sudo sytemctl stop NetworkManager
```

edit resolv.conf file which help kali to resolve the domains

```bash
sudo nano /etc/resolv.conf
```

add:

```bash
#nameserver 192.169.34.2     #comment out old nameserver and add new
nameserver 192.168.34.131
```

if nameserver reverts back to default, check for resolv.conf Symlink to see which service is controlling resolv.conf

```bash
ls -l /etc/resolv.conf
```

Expected Ouput:

```bash
lrwxrwxrwx 1 root root /etc/resolv.conf -> ../run/system/resolve/stub-resolv.conf
```

Edit stub-resolve.conf

```bash
sudo nano /run/systemd/resolve/stub-resolv.conf
```

comment out old nameserver and add new one .

### NEXT
Configure [Authoritative Server](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/03%20Authoritative%20Server/01%20Authoritative%20Server%20Configuration.md)
