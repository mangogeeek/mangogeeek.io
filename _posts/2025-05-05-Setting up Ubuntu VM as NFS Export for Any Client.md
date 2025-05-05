# Configuring NFS Export
To make a directory on your Ubuntu VM available as an NFS export to any client, follow these steps:  
**1\. Install the NFS kernel server:**

```bash
sudo apt update
sudo apt install nfs-kernel-server
```

**2\. Create the export directory:**  
Create the directory you want to share. For example, to share /mnt/nfs_share, run:

```bash
sudo mkdir -p /mnt/nfs_share  
sudo chown -R nobody:nogroup /mnt/nfs_share
```

**3\. Configure the exports file for any client:**  
Edit the /etc/exports file to allow access from any client by using 0.0.0.0/0 or \*(...).  
To allow any client to access the share, add this line:

```
/mnt/nfs_share 0.0.0.0/0(rw,sync,no_subtree_check)
```

OR

```
/mnt/nfs_share *(rw,sync,no_subtree_check)
```

- /mnt/nfs_share: The directory to export.
- 0.0.0.0/0 or \*: This allows access from any client.
- (rw,sync,no_subtree_check): Export options:
    - rw: Read/write access.
    - sync: Ensure data is written to disk before the server replies.
    - no_subtree_check: Disables subtree checking, which can improve performance in some cases.

**Permissions:** Ensure the `/mnt/nfs_share` directory on the NFS server has the correct permissions. A common setting is to give write access to **"others"**:

```
sudo chmod 777 /mnt/nfs_share
```

**4\. Export the share:**  
Apply the changes made to /etc/exports by running:

```
sudo exportfs -a
```

**5\. Open the firewall:**  
If the UFW firewall is enabled, allow NFS traffic from any source:

```
sudo ufw allow from 0.0.0.0/0 to any port 2049  
sudo ufw enable
```

OR

```
sudo ufw allow proto tcp to any port 2049  
sudo ufw allow proto udp to any port 2049  
sudo ufw enable
```

**6\. Restart the NFS server:**  
Restart the NFS server to ensure the changes take effect:

```
sudo systemctl restart nfs-kernel-server
```

**7\. Verify the export:**
Run the command below to show the active nfs exports

```
showmount -e
```

# Client Configuration (on the client machine):
**1\. Install the NFS client:**

```
sudo apt update  
sudo apt install nfs-common
```

**2\. Create a mount point:**  
Create a directory where you'll mount the NFS share:

```
sudo mkdir /mnt/nfs_share
```

**3\. Mount the share:**  
Mount the NFS share from the server:

```
sudo mount <server_ip>:/mnt/nfs_share /mnt/nfs_share
```

Replace &lt;server_ip&gt; with the actual IP address of your Ubuntu VM.  
**4\. Verify the mount:**  
Check that the share is mounted:

```
df -h
```

or

```
mount | grep /mnt/nfs_share
```

**Make the mount persistent (optional):**  
To automatically mount the share at boot, add an entry to /etc/fstab:

```
<server_ip>:/mnt/nfs_share /mnt/nfs_share nfs defaults 0 0
```
