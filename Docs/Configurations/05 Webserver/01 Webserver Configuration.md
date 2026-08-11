# Webserver Setup Guide

This webserver is configured to host the dnspentest.lab domain to demonstarte how DNS works.

## Install Unbuntu Server

OS: Ubuntu Server 26.04 LTS

Version: Miimized

IP:192.168.34.134 

#### Assign IP manually while installing

On Network Configuration Stage:

Step 1: click `ens33 eth0`

Step 2: edit IPv4

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Webserver/webserver-Manual-NetworkConf01.png" alt="Manual Network Config" width="1484" height="552">

step 3: IPv4 Method -> Manual

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Webserver/webserver-Manual-NetworkConf02" alt="Manual Network Config" width="1484" height="552">

Step 4: Configure Manually

- subnet: 192.168.34.0/24

- address: 192.168.34.134

- gateway: 192.168.34.2

- nameservers: 192.168.34.131, 8.8.8.8

<img title="" src="https://github.com/Incogn1mu5/DN53CLab/blob/main/Inventory/Screenshots/Webserver/webserver-Manual-NetworkConf03.png" alt="Manaul Network Config" width="1484" height="552">

## Install Nginx

update ubuntu server

```bash
sudo apt update
```

Install nginx 

```bash
sudo apt install ngnix -y
```

Check ngnix running status 

```bash
sudo systemctl status nginx
```

if running, then go ahead and check if ufw is installed.

Check if ubuntu firewall is installed?

```bash
sudo ufw status    #if returns ufw not found then install it

sudo apt install ufw -y     #install ufw
```

check ufw status

```bash
sudo ufw status    #if return [ status : inactive], enable ufw

sudo ufw enable    #enable ufw and check staus again
```

Open TCP ports and reload the firewall

```bash
sudo ufw allow 80/tcp
sudo ufw alloow 443/tcp


sudo ufw reload            #reload firewall 
```

Get IP address of current webserver

```bash
ip addr

#OR

hostname -I
```

it should return IP address [Ex. : 192.168.34.134]

Test nginx is accessible from browser

- Open browser

- past webserver's IP [Ex.: 192.168.34.134]

- should return message " Wellcome to Nginx!"

## Create and Deploy website

create directory for website

```bash
sudo mkdir -p /var/www/dnspentest.lab
# here -p checks if parent folder exists, if not then it will create parent directory and then the intended file.
```

change ownerhsip

```bash
sudo chown -R $USER:$USER /var/www/dnspentest.lab
```

**Option 1:** create homepage of website

```bash
nano /var/www/dnspentest.lab/index.html
```

```
<!DOCTYPE html>
<html>
<head>
    <title>DNS Pentesting Lab</title>
</head>

<body>

<h1>DNS Pentesting Lab</h1>

<p>This website is intentionally hosted for DNS security testing.</p>

<ul>
<li>DNS Zone Transfer</li>
<li>DNS Amplification</li>
<li>DNS Hijacking</li>
<li>DNS Enumeration</li>
</ul>

</body>
</html>
```

save it.

**Options 2:** attach usb to VM and copy html file 

step 1: attach USB to PC 

step 2 : connect to VM (webserver)

step 3 : create mount point on webserver

```bash
sudo mkdir /mnt/usb
```

step 4 : Find drive name

```bash
lsblk
#check original disk space of flash drive and letter 
#select drive with letter "sdbX" X = [1,2,3...]
```

step 5 : mount flash drive on mount point

```bash
sudo mount /dev/sdbX /mnt/usb        #sdbX = sdb1, sdb2
```

step 6 : copy html file from usb to webserver

```bash
sudo cp /mnt/usb/index.html /var/www/dnspentest.lab/index.html
```

step 7 : un-mount flash drive

```bash
sudo umount /dev/sdbX /mnt/usb
```

## create virtual host for dnspentest.lab

```bash
sudo nano /etc/nginx/sites-available/dnspentest.lab
```

Add:

```
server {

    listen 80;

    server_name
        dnspentest.lab
        www.dnspentest.lab;

    root /var/www/dnspentest.lab;

    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

}
```

Deploy the website

```bash
sudo ln -s /etc/nginx/sites-available/dnspentest.lab /etc/nginx/sites-enabled/

#remove default Nginx Wellcome page
sudo rm /etc/nginx/sites-enabled/default
#OR 
#move default file to another directory
sudo mv /etc/nginx/sites-enabled/default /home/dnsec/
```

validate configurations

```bash
sudo nginx -t

#Expected Output
    #syntax is ok
    #test is successful


#reload nginx
sudo systemctl reload nginx
```

#### Test if website is working

Open Browser 

Search webserver's IP

should load ur html page insead of Nginx welcome page.


### NEXT

Configure [Webserver](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/06%Windows10/Interface%20and%20IP%20Setup%20 for%20Windows.md)
