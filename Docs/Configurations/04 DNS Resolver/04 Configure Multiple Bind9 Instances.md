# Configure Open DNS Resolver for Amplification Attack

This document walks through configuring multiple Bind9 instance on server-01 (DNS Resolver) to mimic the DNS Amplification Attack under isolated network and limited space. 

> ![NOTE]
> 
> This configurations are only made to demonstrate DNS amplification attack and such configurations are never used on production servers.

## 

## Create Multiple Bind9 Instance

Stop old named service before modify or binding new service 

```bash
#stop & disble default BIND9 instance
sudo systemctl stop named
sudo systemctl disable named
```



### Create directories

Create directories for new bind9 instances 

```bash
sudo mkdir -p /etc/bind1 /var/cache/bind1/data /var/log/named1
sudo mkdir -p /etc/bind2 /var/cache/bind2/data /var/log/named2
sudo mkdir -p /etc/bind3 /var/cache/bind3/data /var/log/named3
```



### Copy Configuration

copy old configuration file of open DNS resolver to the new instance directory

```bash
sudo cp -r /etc/bind/* /etc/bind1/
sudo cp -r /etc/bind/* /etc/bind2/
sudo cp -r /etc/bind/* /etc/bind3/
```



### Configure instances

Configure new instances to act as open resolvers

For Bind1 instance 

```bash
sudo nano /etc/bind1/named.conf.options
```

Add :

    options {
     directory "/var/cache/bind1";
    recursion yes;
    allow-query { any; };
    allow-query-cache { any; };
    
    # Listen on port 5353
    listen-on port 5353 { any; };
    listen-on-v6 { none; }; 
    
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

For other instances change following value

| Instance | directory                   | port                         |
| -------- | --------------------------- | ---------------------------- |
| bind2    | directory /var/cache/bind2; | listen-on port 8053 {any; }; |
| bind3    | directory /var/cache/bind3; | listen-on port 9053 {any; }; |



## Check for error

verify if there is any error in named.conf.options configuration file

```bash
sudo named-checkconf -c /etc/bind1/named.conf.options /etc/bind1/named.conf
sudo named-checkconf -c /etc/bind2/named.conf.options /etc/bind2/named.conf
sudo named-checkconf -c /etc/bind3/named.conf.options /etc/bind3/named.conf
```

### Set permissions

set permissions for bind user and bind group 

```bash
sudo chown -R bind:bind /etc/bind1 /var/cache/bind1/data /var/log/named1
sudo chown -R bind:bind /etc/bind2 /var/cache/bind2/data /var/log/named2
sudo chown -R bind:bind /etc/bind3 /var/cache/bind3/data /var/log/named3
```

- **chown** : Short for "change owner." It updates the user and/or group assigned to a file or directory.

- -**R**: Recursive flag. It applies the ownership change not just to the specified folders, but to all files, subdirectories, and nested contents inside them.

- **bind:bind** : Sets the target User to bind (before the colon) and the target Group to bind (after the colon).



### Set Read Write and execute permission

```bash
sudo chmod 755 /var/cache/bind1/data /var/cache/bind2/data /var/cache/bind3/data
```

- chmod 755 command sets the read, write, and execute permissions for a file or directory on Linux/Unix systems



## Configure systemd (system daemon) file

Here replace (x) and (p) value according values given below

| Instance | x   | p    |
| -------- | --- | ---- |
| (named1) | 1   | 5353 |
| (named2) | 2   | 8053 |
| (named3) | 3   | 9053 |

```bash
sudo nano /etc/systemd/system/named(x).service
```

Add:

```
[Unit]
Description=BIND DNS Server (Instance (X) - Port (P))
After=network.target

[Service]
User=bind
Group=bind
Type=forking
ExecStart=/usr/sbin/named -c /etc/bind(X)/named.conf -u bind 
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Reset failed instance if cached any

```bash
sudo systemctl reset-failed named1 named2 named3
```

reload system daemon

```bash
sudo systemctl daemon-reload
```

start all the instances

```bash
sudo systemctl start named named1 named2 named3
```

check status of instance

```bash
sudo systemctl status named named1 named2 named3
```

--- 

## Unable to start new named services ??

check for syntax error

```bash
sudo named-checkconf -c /etc/bind(x)/named.conf
```

check if port are open for listening

```bash
sudo ss -tulpn | grep -E ":5353|:8053|:9053"
```

check whether instances are running

```bash
ps aux | grep named | grep -v grep
```

find error 

```bash
sudo /usr/sbin/named -g  -c /etc/bind(x)/named.conf -u bind
OR
journalctl -xeu named(x).service
```

```
if it shows permission denied, then check further to see who is blocking the access
```

check logs

```bash
sudo dmesg | grep DENIED
OR
journalctl -k | grep DENIED
```

```
if it shows apparmor='DENIED', then follow below steps to unblocl named(x) from apparmor
```

## 

## Unblock new instance

edit apparmor profile 

```bash
sudo nano /etc/apparmord/usr.sbin.named
```

Add: below (#include <local/usr.sbin.named>)

```bash
#named1 
/etc/bind1/** r,    #configuration
/var/cache/bind1/** rwk,     #cache
/var/cache/bind1/ rw,     #working directory
/var/log/named1/** rw,    #logs
/var/lib/bind1/** rw,    #if dynamic zones or journals used

#named2
/etc/bind2/** r, 
/var/cache/bind2/** rwk, 
/var/cache/bind2/ rw, 
/var/log/named2/** rw,
/var/lib/bind2/** rw, 

#named3
/etc/bind3/** r,
/var/cache/bind3/** rwk, 
/var/cache/bind3/ rw, 
/var/log/named3/** rw, 
/var/lib/bind3/** rw,
```

save -> exit and then reload pparmor

```bash
sudo systemctl reload apparmor
```

Now, try to start new instances

```bash
sudo systemctl start named1 named2 named3
```

if started successfully, set services to start on boot

```bash
sudo systemctl enable named1 named2 named3
```



### NEXT

Configure [Webserver](https://github.com/Incogn1mu5/DN53CLab/tree/main/Docs/Configurations/05%Webserver/01%20Webserver%20Configuration.md)

