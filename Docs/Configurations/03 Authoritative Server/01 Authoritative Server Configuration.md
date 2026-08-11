# Configure Authoritative Server

First install Ubuntu Server 26.04 LTS 



## Install BIND9 on Authotitative server

```bash
sudo apt update
sudo apt install bind9 bind9utils bind9-doc dnsutils -y
```



## Configure server-02 as Authoritative

Edit:

```bash
sudo nano /etc/bind/named.conf.local
```

Add:

```bash
zone "dnspentest.lab" {    
    type master;    
    file "/etc/bind/db.dnspentest.lab";    
    allow-transfer { any; };        #this allows zone transfer
};
```

We'll intentionally enable AXFR later for the zone transfer exercise.



## Create the Zone File

Create data base for zone 

```bash
sudo nano /etc/bind/db.dnspentest.lab
```

Replace it with something like:

```
$TTL 86400

@       IN      SOA     ns1.dnspentest.lab. admin.dnspentest.lab. (
                        2026072501
                        3600
                        1800
                        604800
                        86400 )        

        IN      NS      ns1.dnspentest.lab.

ns1    IN      A       192.168.34.133

@      IN      A       192.168.34.134
www    IN      A       192.168.34.134
portal IN      A       192.168.34.134
admin  IN      A       192.168.34.134
mail   IN      A       192.168.34.134
ftp    IN      A       192.168.34.134
vpn    IN      A       192.168.34.134
api    IN      A       192.168.34.134

@      IN      MX 10   mail.dnspentest.lab.
```



## Validate

```bash
sudo named-checkzone dnspentest.lab /etc/bind/db.dnspentest.lab
```

Expected:

```
OK
```

Check configuration:

```bash
sudo named-checkconf
```



## Restart

```bash
sudo systemctl restart bind9
sudo systemctl status bind9
#OR
sudo rndc reload
```



## Test Authoritative Server

Check Authoritative Server itself can resolve the IP of given domain

```bash
dig @127.0.0.1 www.dnspentest.lab
```

Check from Kali whether authoritative server is reachable and can resolve domain IP:

```bash
dig @192.168.34.133 www.dnspentest.lab
```

Both command should return:

```
www.dnspentest.lab.   A   192.168.34.134
```



### NEXT

Configure [Interface on Authoritative server](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/03%20Authoritative%20Server/02%20IP%20Configuration.md)












