This document outlines the standardized process for preparing a **generalized disk image** for Nutanix VMs, including container mounting, disk identification, image cleanup, conversion, sysprep, and upload.

***

# 1. VM Disk Identification
### 1.1 Locate VM Disks Using Nutanix CLI | Identify Primary Disk
Identify all disks attached to the golden image VM.
```bash
acli vm.get "R-Shield-Golden" include_vmdisk_paths=true | grep -w vmdisk_nfs_path && \
acli vm.disk_get "R-Shield-Golden" disk_addr="scsi.0" | grep -w vmdisk_uuid
```
Output:
```bash
admin@NTNX-CZJ837108G-A-CVM:10.169.28.155:~$ acli vm.get "R-Shield-Golden" include_vmdisk_paths=true | grep -w vmdisk_nfs_path && acli vm.disk_get "R-Shield-Golden" disk_addr="scsi.0" | grep -w vmdisk_uuid
      vmdisk_nfs_path: "/default-container-45667019721350/.acropolis/vmdisk/00e5a3fe-0b78-4759-ae15-adc8786851b7"
  vmdisk_uuid: "00e5a3fe-0b78-4759-ae15-adc8786851b7"
```
> Now, we can move to the next steps and we will mount this Nutanix container and copy this disk image in the later steps. 

***

# 3. Inside the R_Shield Golden Image
Run these interactively inside the guest (recommended) before shutdown.

### 3.1 Clean logs, caches, and orphaned packages inside the VM
Removes old logs and package caches (deletes files only; preserves directories).
This ensures the `/swapfile` remains available but contains no residual memory data from the build process.

```bash
sudo journalctl --vacuum-time=1s && \
sudo rm -rf /var/log/* && \
sudo apt-get autoremove -y && \
sudo apt-get clean && \
sudo fstrim -av
```

### 3.2 Zero-out the swapfile but keep it present and enabled (Optional)
Preferred: wipes old memory contents but keeps `/swapfile` for future boots.
```bash
# --- 1️⃣ Disable swap ---
sudo swapoff -a

# --- 2️⃣ Remove any old swap entries ---
sudo sed -i '/swapfile/d' /etc/fstab
sudo rm -f /swapfile

# --- 3️⃣ Recreate a clean, minimal swapfile (1 GB recommended) ---
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile

# --- 4️⃣ Add swap entry back to /etc/fstab ---
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# --- 5️⃣ Enable swap again ---
sudo swapon /swapfile

```
Expected verification output (example):
```bash
NAME      TYPE  SIZE  USED  PRIO
/swapfile file  2G    0B    -2
```
>Note: If your system uses a swap partition (not a file), follow the offline or partition-specific steps; do not dd-over a live swap partition.

### 3.5 Trim and zero-fill free space (to optimize compression)
`fstrim` reclaims unused blocks; `dd` writes zeros so sparsifiers/compressors do better.
```bash
# Trim then zero-fill free space for best compression
sudo dd if=/dev/zero of=/zero.fill bs=1M status=progress || true && \
sudo rm -f /zero.fill && sync
```
### 3.6 Shutdown the VM cleanly
```bash
# Shut down the VM
sudo shutdown -h now
```
(After all in-guest cleanup is done.)
***
# 3. Mount the Nutanix Container

### 3.1 Verify NFS Export Availability
Verify that the desired container export is available and accessible from your image build host.
```bash
showmount -e 10.169.28.147 | grep default-container-45667019721350
showmount -e 10.169.28.147 | egrep -v 10.169.32.182
```
Expected Output:
```bash
/default-container-45667019721350 [accessible]
```
>Note: `10.169.28.147` is the Nutanix Cluster IP and `default-container-45667019721350` is the container where the R-shield VM is hosted. 

### 3.2 Mount the Container
Mount the NFS export to your local filesystem.
```bash
sudo mount -t nfs 10.169.28.147:/default-container-45667019721350 /mnt/nutanix
```
Verify Mount:
```bash
df -h /mnt/nutanix
```
Expected Output:
```bash
hycu@hycu-AHV:/mnt/image$ df -h /mnt/nutanix
Filesystem                                       Size  Used Avail Use% Mounted on
10.169.28.147:/default-container-45667019721350   13T  2,9T   10T  23% /mnt/nutanix
```
***
# 4. Copy Image
```bash
sudo rsync -avh --progress /mnt/nutanix/.acropolis/vmdisk/00e5a3fe-0b78-4759-ae15-adc8786851b7 /mnt/image/
```
***
# 5. Base Golden Image

### 5.1 Base Golden Image (clean + sysprepped)

#### Step 1: Build the reusable `base image`:
```bash
sudo qemu-img convert -p -f raw -O qcow2 -c \
  -o compat=1.1,cluster_size=1M,lazy_refcounts=on \
  /mnt/image/00e5a3fe-0b78-4759-ae15-adc8786851b7 \
  /mnt/image/hycu-r-shield-image_v1.qcow2
```
####  Step 2: Apply system cleanup and first-boot configuration
```bash
sudo virt-sysprep -a /mnt/image/hycu-r-shield-image_v1.qcow2 \
  --operations defaults,bash-history,logfiles,tmp-files,machine-id,user-account \
  --keep-user-accounts hycu \
  --firstboot-command '
    systemctl enable --now NetworkManager || true
    for iface in $(nmcli -t -f DEVICE,TYPE device status | grep -E "ethernet|enp|ens" | cut -d: -f1); do
      nmcli connection add type ethernet ifname "$iface" \
        con-name "Auto-$iface" \
        connection.autoconnect yes \
        ipv4.method auto \
        ipv6.method auto 2>/dev/null || true
    done
    echo "Network ready at $(date)" > /var/log/network-firstboot.log
    nmcli device show >> /var/log/network-firstboot.log 2>&1
    if [ ! -f /etc/ssh/ssh_host_ecdsa_key ]; then
      dpkg-reconfigure openssh-server
    fi
    systemctl enable --now ssh
    if command -v ufw >/dev/null; then
      ufw allow ssh
    fi
  '
```

```bash
# The image is ready
hycu@hycu-AHV:/mnt/image$ ls -ltrh
total 28G
-rwxrwxrwx 1 root root  25G nov  3 11:44 00e5a3fe-0b78-4759-ae15-adc8786851b7
-rw-r--r-- 1 root root 2,8G nov  3 12:05 hycu-r-shield-image_v1.qcow2

```
#### Step 3: Verify Image Integrity (Post-Conversion, Pre-Sysprep)
```bash
sudo virt-ls -a /mnt/image/hycu-r-shield-image_v1.qcow2 /etc/ && \
sudo qemu-img check /mnt/image/hycu-r-shield-image_v1.qcow2 && \
sudo virt-cat -a /mnt/image/hycu-r-shield-image_v1.qcow2 /etc/fstab | grep swap

```
### 5.2 Versioned Image Releases
```bash
sudo qemu-img convert -p -O qcow2 -c -o compat=1.1 \
  /mnt/image/hycu-r-shield-image_v1.qcow2 \
  /mnt/image/hycu-r-shield-5.2.0-1103.qcow2
```
### 5.3 Generate checksums automatically:
```bash
sudo sha256sum /mnt/image/hycu-r-shield-5.2.0-1103.qcow2 > /mnt/image/hycu-r-shield-5.2.0-1103.qcow2.sha256
```

# 6.Generate VMware or export formats from the same base

### 6.1 Create VMware-Compatible VMDK
For OVA/OVF packaging, use the streamOptimized subformat.
```bash
sudo virt-sparsify --compress \
  /mnt/image/hycu-r-shield-image_v1.qcow2 \
  /mnt/image/hycu-r-shield-5.2.0-1103.qcow2
```
###6.2 Verify and Checksum
Validate image metadata and record hashes for consistency.
```bash
sudo sha256sum /mnt/image/hycu-r-shield-5.2.0-1103.vmdk> /mnt/image/hycu-r-shield-5.2.0-1103.vmdk.sha256
```
### 6.3 (Optional) Convert to Thin-Provisioned VMDK on ESXi
If uploading directly to an ESXi datastore:
```bash
vmkfstools -i hycu-r-shield-5.2.0-1103.vmdk -d thin hycu-r-shield-5.2.0-1103-thin.vmdk
```
***
# 7 Upload Image to Nutanix

### 7.1 Copy Image to Nutanix Container
```bash
sudo rsync -avh --progress /mnt/image/ hycu-r-shield-5.2.0-1103.qcow2 /mnt/nutanix/
```

### 7.2 Register Image via acli
```bash
acli image.create  hycu-r-shield-test \
  image_type=kDiskImage \
  source_url=nfs://10.169.28.147/default-container-45667019721350/hycu-r-shield-5.2.0-1103.qcow2 \
  container=default-container-45667019721350
```


