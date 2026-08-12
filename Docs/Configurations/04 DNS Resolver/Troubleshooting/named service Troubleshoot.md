# named service Troubleshoot

```bash
sudo systemctl start named
```

Error: 

```bash
Job for named.service failed because the control process exited with error code.
See "systemctl status named.service" and "journalctl -xeu named.service" for details.
```

</br>  



## Checking AppArmor Status

```bash
sudo aa-status | grep named
```

**Output:**

```
named
```

The Problem: AppArmor Blocks BIND

- AppArmor may prevent BIND from writing to custom log locations.

</br>  



## Solution

Solution 1: Put AppArmor in Complain Mode

```bash
sudo aa-complain /usr/sbin/named    #may throw error for comand not found
```



Solution 2: Temporarily stops AppArmor to allow BIND to start

```bash
sudo systemctl stop apparmor
```

this will pause apparmor entirely, which is not recommended for production environment.



Solution 3: Disable AppArmor for BIND only

```bash
sudo ln -s /etc/apparmor.d/usr.sbin.named \ /etc/apparmor.d/disable/
sudo systemctl reload apparmor
```

</br>  



## Verification & Testing

Start BIND9

```bash
sudo systemctl start named
```

Check Status

```bash
sudo systemctl status named
```

Expected Output:

```
named.service - BIND Domain Name Server
 Loaded: loaded (/usr/lib/systemd/system/named.service; enabled; preset: enabled)
 Active: active (running) since Wed 2026-07-22 19:24:55 UTC; 10s ago
 Main PID: 3147 (named)
 Status: "running"
 Tasks: 6 (limit: 1830)
 Memory: 4.9M (peak: 5.1M)
 CPU: 129ms
 CGroup: /system.slice/named.service
 └─3147 /usr/sbin/named -f -u bind
Jul 22 19:24:55 dnsresol named[3147]: automatic empty zone: HOME.ARPA
Jul 22 19:24:55 dnsresol named[3147]: automatic empty zone: RESOLVER.ARPA
Jul 22 19:24:55 dnsresol named[3147]: configuring command channel from '/etc/bind/rndc.key'
Jul 22 19:24:55 dnsresol named[3147]: command channel listening on 127.0.0.1#953
Jul 22 19:24:55 dnsresol named[3147]: configuring command channel from '/etc/bind/rndc.key'
Jul 22 19:24:55 dnsresol named[3147]: command channel listening on ::1#953
Jul 22 19:24:55 dnsresol named[3147]: all zones loaded
Jul 22 19:24:55 dnsresol named[3147]: FIPS mode is disabled
Jul 22 19:24:55 dnsresol systemd[1]: Started named.service - BIND Domain Name Server.
Jul 22 19:24:55 dnsresol named[3147]: running
```

**Status Interpretation:**

- `active (running)` = Successfully started

- `Main PID` = Process ID of BIND

- `running` = BIND is operational
