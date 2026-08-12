# Port Conflict Troubleshoot



## Error

` Job for named.service failed because the control process exited with error code.`

What does it mean? It simply wanted to say **Port 53 Already in Use**

</br>  



## Diagnostic Command:

```bash
sudo ss -tulpn | grep :53
```

**Output:**

```bash
udp UNCONN 0 0 127.0.0.54:53 0.0.0.0:* users:(("systemd-resolve",pid=985,fd=18))
udp UNCONN 0 0 127.0.0.53:53 0.0.0.0:* users:(("systemd-resolve",pid=985,fd=16))
tcp LISTEN 0 4096 127.0.0.54:53 0.0.0.0:* users:(("systemd-resolve",pid=985,fd=19))
tcp LISTEN 0 4096 127.0.0.53:53 0.0.0.0:* users:(("systemd-resolve",pid=985,fd=17))
```

**What this shows:**

- `systemd-resolved` is listening on ports 53 (both TCP and UDP)

- PID 985 is the process ID

- This prevents BIND9 from binding to port 53

**Why this happens:**

Ubuntu uses `systemd-resolved` as the default DNS resolver. It starts automatically and occupies port 53.

</br>  



## Solution:

Stop and Disable systemd-resolved



##### Stop the service

Immediately stops the service to free port 53

```bash
sudo systemctl stop systemd-resolved
```

# 

##### Disable the service

Prevents service from starting at boot

```bash
sudo systemctl disable systemd-resolved
```

##### Mask the service

Creates a symlink to /dev/null, preventing any other service from starting it

```bash
sudo systemctl mask systemd-resolved
```

##### Remove the old resolv.conf

Removes the symlink pointing to systemd-resolved

```bash
sudo rm /etc/resolv.conf
```

##### Create new resolv.conf

Sets manual DNS servers for system resolution

```bash
sudo tee /etc/resolv.conf << 'EOF'
nameserver 8.8.8.8
nameserver 1.1.1.1
EOF
```

##### Make it immutable

Prevents system from overwriting resolv.conf

```bash
sudo chattr +i /etc/resolv.conf
```

**chattr +i Explanation:**

- `chattr` = Change file attributes

- `+i` = Make file immutable (Even sudo cannot modify, rename, or delete it)

- Prevents systemd-resolved from recreating the symlink

- If you want to make changes on immutable file simply use (-i) flag instead of (+i)

##### Verification

```bash
sudo ss -tulpn | grep :53
```

 Should show nothing - port 53 is free!
