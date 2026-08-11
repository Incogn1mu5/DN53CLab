# VMware Virtual Network Configuration

This document describes the steps required to configure the virtual networking environment for the DN53C Lab in VMware.

The lab topology and IP addressing scheme are documented in [README.md](https://github.com/Incogn1mu5/DN53CLab/blob/323f0ec685af5427c21d880c2b6a27aa85098cd9/README.md).

## 1. Prerequisites

Before configuring the virtual network, make sure that:

- VMware Workstation/VMware Fusion is installed.
- All required lab virtual machines have been created.
- Each VM has the required network adapters.

## 2. Open VMware Virtual Network Editor

1. Open VMware.
2. Open **Virtual Network Editor**.
3. Select **Change Settings** / run with administrator privileges.

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Network_Config/Network_Config01.png" alt="Network_Config" width="1484" height="552">

4. Review the existing virtual networks`VMnet8` and follow step displayed below:

step 1: select VMnet8

step 2: select NAT 

step 3: Enter Subnet IP `192.168.34.0`

step 4: Set Subnet Mask `255.255.255.0`

step 5: click `OK` to apply

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Network_Config/Network_Config02.png" alt="Network_Config" width="1484" height="552">

### NEXT

Configure [Kali Linux](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/02%20Kali%20Linux/Interface%20and%20IP%20Setup%20for%20Kali%20Linux.md)


