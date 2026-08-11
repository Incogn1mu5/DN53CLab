# IP Configuration for Authoritative Server

This document shows to configure Authoritative Server to use custom Interface and static IP address while using VMware's NAT Adapter (DHCP Enabled)

## Setup Interface

To make Authoritative Server function locally, make sure to connect it with interface created during Virtual Network Configuration.

Follow given steps to configure Authoritative Server to use custom interface

step 1: Edit Virtual Machine Settings

step 2: Click Network Adapter

step3: Select NAT

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Authoritative_Server/Auth_Server01.png" alt="Interface Setup" width="1484" height="552">

## Configure IP

For Authoritative Server its not mandatory to use static IP, but if you use preconfigured vm images you may needd to configure IP manually.

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
             - 192.168.34.133/24     # YOUR static IP
         routes: 
             - to: default
               via: 192.168.34.2
         nameservers:
            addresses:
                - 127.0.0.1         # only add after updating server
         match:
            macaddress: 00:XX:XX:XX:XX:XX     #make sure to verify the MAC address look in to vmware -> machine -> edit settings -> network adapter -> mac address
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

Configure Authoritative Server for [Zone Transfer Vulnerability](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/03%20Authoritative%20Server/03%20Zone%20Transfer%20Configuraion.md)


