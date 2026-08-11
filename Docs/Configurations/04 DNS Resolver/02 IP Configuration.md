# IP Configuration for DNS Resolver

This document shows to configure DNS Resolver to use static IP address while using VMware's NAT Adapter (DHCP Enabled)

## Setup Interface

To make DNS Resolver work locally, make sure to connect it with interface created during Virtual Network Configuration.

Follow given steps to configure DNS Resolver to use custom interface

step 1: Edit Virtual Machine Settings 

step 2: Click Network Adapter 

step3: Select NAT 

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/DNS_Resolver/Interface-Setup.png" alt="Interface Setup" width="1484" height="552">

## Configure IP

DNS-Resolver is supposed to used static IP, becuase if it has dynamic IP user's computer won't be able to contact DNS-Resolver if IP gets changed

Change netplan config to make the IP address static for Open DNS Resolver

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Add:

```
#This is the network config written by 'subiquity'
network:
    ethernets:
        ens33: 
         dhcp4: false             #disable dynamic IPv4 allocation
         dhcp6: false             #disable dynamic IPv6 allocation
         addresses:
             - 192.168.34.131/24     # YOUR static IP
         routes: 
             - to: default
               via: 192.168.34.2
         nameservers:
            addresses:
                - 127.0.0.1         # only add after updating server
         match:
            macaddress: 00:50:56:22:46:62     #make sure to verify the MAC address look in to vmware -> machine -> edit settings -> network adapter -> mac address
         set-name: ens33
version: 2
```

## Check for error

```bash
sudo netplan try
```

`if no error fond, it will ask you to press enter to apply settings before XXX seconds or it will revert to default settings `

## Apply netplan settings

```bash
sudo netplan apply
```

### NEXT

Configure DNS Resolver to query Authoritative Server in case of missing Cache

[DNS Resolver to Authoritative Server](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/04%20DNS%20Resolver/03%20DNS%20Resolver-to-Authoritative%20Server.md)