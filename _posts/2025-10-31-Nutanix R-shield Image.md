This document outlines the standardized process for preparing a **generalized disk image** for Nutanix VMs, including container mounting, disk identification, image cleanup, conversion, sysprep, and upload.

------------
[2. Mount the Nutanix Container](#2-mount-the-nutanix-container)

# 1. VM Disk Identification
### 1.1 Locate VM Disks Using Nutanix CLI
Identify all disks attached to the golden image VM.
```bash
acli vm.get r-shield_Golden include_vmdisk_paths=true | grep -w vmdisk_nfs_path
```
Output:
```bash
vmdisk_nfs_path: "/default-container-45667019721350/.acropolis/vmdisk/39d4acd8-c22b-4f7d-9826-08121f706ed5"
```
### 1.2 Identify Primary Disk
Determine which vDisk corresponds to the OS/root volume.
```bash
acli vm.disk_get r-shield_Golden disk_addr="scsi.0" | grep -w vmdisk_uuid
```
Output:
```bash
vmdisk_uuid: "39d4acd8-c22b-4f7d-9826-08121f706ed5"
```
------------
# 2. Mount the Nutanix Container
### 2.1 Verify NFS Export Availability
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

### 2.2 Mount the Container
Mount the NFS export to your local filesystem.
```bash
sudo mount -t nfs 10.169.28.147:/default-container-45667019721350 /mnt/test
```
Verify Mount:
```bash
df -h /mnt/test
```
Expected Output:
```bash
Filesystem                                       Size  Used  Avail  Use%  Mounted on
10.169.28.147:/default-container-45667019721350  4.6T  2.8T  1.8T   61%  /mnt/test
```

------------

# 3. Inside Guest VM — Cleanup and Preparation (full content)
Run these interactively inside the guest (recommended) before shutdown.
### 3.1 Clean system logs and apt caches
Removes old logs and package caches (deletes files only; preserves directories).
This ensures the `/swapfile` remains available but contains no residual memory data from the build process.
```bash
# Clean logs and apt caches
sudo journalctl --vacuum-time=1s && \
sudo find /var/log -type f -delete && \
sudo apt-get clean && \
sudo apt-get autoremove -y
```
### 3.2 Reset machine ID
Ensures each clone gets a unique machine-id on first boot.
```bash
# Reset systemd machine-id and recreate dbus symlink
sudo truncate -s 0 /etc/machine-id && \
sudo rm -f /var/lib/dbus/machine-id && \
sudo ln -s /etc/machine-id /var/lib/dbus/machine-id
```
###3.3 Remove SSH host keys & clear shell histories
Removes lingering host keys and clears shell histories for privacy.
```bash
# Remove SSH host keys and clear bash histories for root and hycu
sudo rm -f /etc/ssh/ssh_host_* && \
history -c || true && \
history -w || true && \
sudo rm -f /root/.bash_history /home/hycu/.bash_history || true
```
### 3.4 Zero-out the swapfile but keep it present and enabled
Preferred: wipes old memory contents but keeps `/swapfile` for future boots.
```bash
# Zero the swapfile while preserving its presence in /etc/fstab
sudo swapoff /swapfile && \
sudo dd if=/dev/zero of=/swapfile bs=1M status=progress && \
sudo mkswap /swapfile && \
sudo swapon /swapfile && \
swapon --show
```
Expected verification output (example):
```bash
NAME      TYPE  SIZE  USED  PRIO
/swapfile file  2G    0B    -2
```
>Note: If your system uses a swap partition (not a file), follow the offline or partition-specific steps; do not dd-over a live swap partition.

###3.5 Trim and zero-fill free space (to optimize compression)
`fstrim` reclaims unused blocks; `dd` writes zeros so sparsifiers/compressors do better.
```bash
# Trim then zero-fill free space for best compression
sudo fstrim -av || true && \
sudo dd if=/dev/zero of=/zero.fill bs=1M status=progress || true && \
sudo rm -f /zero.fill && \
sync
```
### 3.6 Shutdown the VM cleanly
```bash
# Shut down the VM
sudo shutdown -h now
```
(After all in-guest cleanup is done.)
***
# 4. Image Generalization (virt-sysprep)
Run `virt-sysprep` on the QCOW2 image to reset identifiers, clear histories, and configure first-boot networking and SSH. Resets logs, tmp files, machine ID, and SSH keys. It also enables networking and SSH on first boot.
```bash
sudo virt-sysprep \
  -a /mnt/image/hycu-r-shield-image_v1.qcow2 \
  --operations bash-history,logfiles,tmp-files,machine-id,ssh-userdir,package-manager-cache,crash-data,backups \
  --keep-user-accounts hycu \
  --firstboot-command '
    set -eux
    echo "[Firstboot] Starting post-sysprep configuration..." | tee /var/log/firstboot.log

    # --- Network Configuration ---
    if systemctl list-unit-files | grep -q "^NetworkManager.service"; then
      echo "[Firstboot] Enabling NetworkManager..." | tee -a /var/log/firstboot.log
      systemctl enable --now NetworkManager || true

      echo "[Firstboot] Setting up Ethernet connections..." | tee -a /var/log/firstboot.log
      for iface in $(nmcli -t -f DEVICE,TYPE device status | awk -F: "$2==\"ethernet\"{print $1}"); do
        nmcli -t -f NAME c show | grep -q "^Auto-$iface$" || \
          nmcli connection add type ethernet ifname "$iface" con-name "Auto-$iface" \
          connection.autoconnect yes ipv4.method auto ipv6.method auto || true
      done

      echo "[Firstboot] Ethernet configuration complete." | tee -a /var/log/firstboot.log
    else
      echo "[Firstboot] NetworkManager not found, skipping network setup." | tee -a /var/log/firstboot.log
    fi

    # --- SSH Configuration ---
    echo "[Firstboot] Regenerating SSH host keys..." | tee -a /var/log/firstboot.log
    rm -f /etc/ssh/ssh_host_* || true
    dpkg-reconfigure openssh-server || true

    echo "[Firstboot] Enabling SSH service..." | tee -a /var/log/firstboot.log
    systemctl enable --now ssh || systemctl enable --now sshd || true

    # --- UFW (Firewall) Configuration ---
    if command -v ufw >/dev/null; then
      echo "[Firstboot] Allowing SSH in UFW..." | tee -a /var/log/firstboot.log
      ufw allow ssh || true
    else
      echo "[Firstboot] UFW not installed, skipping firewall configuration." | tee -a /var/log/firstboot.log
    fi

    # --- Verification & Completion ---
    nmcli device show >> /var/log/firstboot.log 2>&1 || true
    echo "[Firstboot] Completed successfully at $(date)" | tee -a /var/log/firstboot.log
  '
```
> This process will: **re-enable NetworkManager**, automatically **connect Ethernet interfaces**,** regenerate SSH host keys** on first boot, **enable the SSH service**, and **allow SSH access via UFW** (if present).

------------

#5. Image Optimization and Conversion
###5.1 (Optional) Sparsify Image
Reclaim unused zeroed blocks to reduce disk size.
```bash
sudo virt-sparsify --in-place /mnt/image/hycu-r-shield-image_v1.qcow2
```
###5.2 Create AHV-Compatible QCOW2
Convert and compress the cleaned image.
```bash
qemu-img convert -p -O qcow2 -c -o compat=1.1 \
/mnt/image/hycu-r-shield-image_v1.qcow2 \
/mnt/image/hycu-r-shield-5.2.0-805.qcow2
```
### 5.3 Create VMware-Compatible VMDK
For OVA/OVF packaging, use the streamOptimized subformat.
```bash
qemu-img convert -p -f qcow2 -O vmdk -o subformat=streamOptimized \
/mnt/image/hycu-r-shield-image_v1.qcow2 \
/mnt/image/vmware/hycu-r-shield-5.2.0-805.vmdk
```
###5.4 Verify and Checksum
Validate image metadata and record hashes for consistency.
```bash
qemu-img info /mnt/image/hycu-r-shield-5.2.0-805.qcow2 && \
qemu-img info /mnt/image/vmware/hycu-r-shield-5.2.0-805.vmdk && \
sha256sum /mnt/image/hycu-r-shield-5.2.0-805.qcow2 && \
sha256sum /mnt/image/vmware/hycu-r-shield-5.2.0-805.vmdk
```
### 5.5 (Optional) Convert to Thin-Provisioned VMDK on ESXi
If uploading directly to an ESXi datastore:
```bash
vmkfstools -i hycu-r-shield-5.2.0-805.vmdk -d thin hycu-r-shield-5.2.0-805-thin.vmdk
```

------------


[2. mount the nutanix container]: 2. mount the nutanix container "# 2. Mount the Nutanix Container"
[26]: 2-mount-the-nutanix-container
