# Interface and IP Setup for Windows

This document is to configure Windows 10 (Vicitm) to use static IP address while using custom VMware's NAT Adapter (DHCP Enabled)

## Setup Interface

To make Windows 10 communicate locally, make sure to connect it with interface created during Virtual Network Configuration.

Follow given steps to configure Windows 10 to use custom interface

step 1: Edit Virtual Machine Settings 

step 2: Click Network Adapter 

step3: Select NAT 

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Windows10/Custom-Interface-Setup.png" alt="Interface Setup" width="1484" height="552">

## Configure IP

Step 1: Open Control Panel 

Step 2: Open Network and Internet

Step 3: Open Network and Sharing Center

Step 4: Click (Connections : Ethernet1)
<img width="1484" height="552" alt="control panel" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Windows10/control-panel.png" />

Step 5: Ethernet1 > Properties

Step 6: Internet Protocol Version IPv4 Protocol > Properties

Step 7:  use the following (IP address & DNS server address)

- IP address: 192.168.34.130

- Subnet mask: 255.255.255.0

- Default gateway: 192.168.34.2

- preferred DNS server: 192.168.34.131

<img width="1484" height="552" alt="control panel" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Windows10/IP-Conf_victim.png" />

#### Verify whether windows using local DNS Resolver

```powershell
ipconfig /all
```

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Windows10/Verification01.png" alt="verify01" width="1484" height="552">

#### Try to access webpage hosted on webserver over nginx

open browser and search `http://dnspentest.lab`
<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Windows10/Verification02.png" alt="verify02" width="1484" height="552">
