# AWS R-shield Image Preparation guide
***
# Step 1: Log in to the Data Mover VM

Log in to the Data Mover VM as the **root user** on port `42222`, using your SSH private key.

> **Note:** Ensure you are connected to a **full VPN tunnel**, otherwise SSH access may fail.

```powershell
ssh -i "C:\Users\PiyushRai\Downloads\hycu-ssh.pem" root@13.53.245.120 -p 42222
```

# Step 2: Prepare the Machine for SSH Password Login

#### **2.1 Set the System Hostname**

```bash
sudo hostnamectl set-hostname r-shield-aws
```

#### **2.2 Create a New User**

Create a user with a home directory and Bash shell, set a password, and add the user to the `wheel` group (for sudo access):

```bash
sudo useradd -m -s /bin/bash hycu && \
echo 'hycu:hycu/4u' | sudo chpasswd && \
sudo usermod -aG wheel hycu

# Verify group membership
groups hycu

#Expected Ouput 
hycu : hycu wheel
```

#### **2.3 Configure Firewall to Allow SSH**

Check firewall status and allow SSH:

```bash
# Check firewall status
sudo firewall-cmd --state

# Allow SSH service
sudo firewall-cmd --permanent --add-service=ssh

# Reload firewall rules
sudo firewall-cmd --reload

# Verify allowed services
sudo firewall-cmd --list-services
```

#### **2.4 Configure SSH for Password Authentication**

Edit the SSH daemon configuration: 

```bash
sudo vi /etc/ssh/sshd_config
```

Ensure the following parameters are present and **not commented out.** 

> **⚠️ Note:** Port `42222` may still be active. Keeping both ports allows fallback access.

```bash
Port 22
PasswordAuthentication yes
PubkeyAuthentication yes
PermitRootLogin prohibit-password
```

#### **2.5 Restart and Verify SSH Configuration**

Restart the SSH service:

```bash
sudo systemctl restart sshd
```

Verify the effective configuration:

```bash
sudo sshd -T | grep -Ei 'port|passwordauthentication|pubkeyauthentication|permitrootlogin'
```

Expected output (example):

```bash
port 42222
port 22
permitrootlogin prohibit-password
pubkeyauthentication yes
passwordauthentication yes
```

#### **2.6 Configure SSH Login Banner**

Edit the SSH banner file:

```bash
sudo vi /etc/ssh/sshd-banner
```

Add the following content: 

```bash
***************************************************************
                HYCU R-Shield Scanner
***************************************************************
```

Verify

```bash
sudo sshd -T | grep banner

# Expected Ouput 
banner /etc/ssh/sshd-banner
```

#### **2.7 Disable Unwanted Login Scripts**

Disable the script which is appearing automatically during SSH login due to `/etc/profile.d/`

```bash
sudo sed -i '/Active root partition is/d' /etc/profile.d/ab-partition-info.sh
```

---

# Step 3: Handling R-shield dependencies

#### 3.1 Install Development Tools and Dependencies

```bash
sudo dnf groupinstall -y "Development Tools"

sudo dnf install -y \
  git automake libtool \
  openssl-devel libcurl-devel \
  bison flex
```

#### 3.2 Remove Any Existing YARA Installation

```bash
sudo rm -f /usr/local/bin/yara /usr/local/bin/yara64
```

#### 3.3 Clone and Build YARA from Source

```bash
git clone https://github.com/VirusTotal/yara.git
cd yara

./bootstrap.sh
./configure
make
```

Run test suite:

```bash
make check
```

> ⚠️**Known Issue (RHEL/Rocky 9):** OpenSSL disables SHA-1 by default, which may cause
> `test-pe` failures.

If tests fail, rerun:

```bash
OPENSSL_ENABLE_SHA1_SIGNATURES=yes make check
```

#### 3.4 Install YARA

```bash
sudo make install
# Update shared library cache (recommended):
sudo ldconfig

# Verify Installation
yara --version
```

#### 3.5 Install Python and AWS SDK Dependencies

Install Python and pip

```bash
sudo dnf install -y python3 python3-pip
```

Install Required Python Packages

```bash
pip3 install --upgrade pip

pip3 install requests boto3
```

> 
> 
> 
> ✔ `boto3` is required for interacting with AWS services such as **Secrets Manager**
> 
> ✔ `requests` is used for HTTP/API interactions
> 

Install AWS CLI v2

```bash
# Install Prerequisites
sudo dnf install -y unzip curl

# Download and Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

```bash
# Verify Installation
aws --version

# Expected output (example):
aws-cli/2.x.x Python/3.x Linux/x86_64
```

---

# Step 4: Download `r-shield` binaries

#### 4.1 Create Target Directory

Create the `/r-shield` directory if it does not already exist:

```bash
sudo mkdir -p /r-shield
```

#### 4.2 Download the Source Files

We will download these into your home directory build folder instead of `/tmp` to avoid accidental deletion during the build process.

```bash
# Download the r_shield_aws_mount.py in the /tmp/ directory
sudo wget -P /tmp/ --content-disposition https://files.hycu.com/seafhttp/f/c83648d00a25439583d6/?op=view

# Download the r-shield-hycu_aws.py in the /tmp/ directory
sudo wget -P /tmp/ --content-disposition https://files.hycu.com/seafhttp/f/799dbdcfa6a84c24a8b0/?op=view

# Download the r-shield-config file in the /tmp/ directory
sudo wget -P /tmp/ --content-disposition "https://files.hycu.com/seafhttp/f/3cf9ec8016f240ffabbe/?op=view" 

# Sample files 

[hycu@r-shield-aws tmp]$ ls -lh
total 192K
-rw-r--r--. 1 root root  43K Mar 19 07:14 r_shield_aws_mount.py
-rw-r--r--. 1 root root 6.8K Mar 19 07:14 r-shield-config-03-19-2026
-rw-r--r--. 1 root root 138K Mar 19 07:14 r-shield-hycu_aws.py
```

> ✔ Replace `<file_path>` with the actual artifact URLs.
✔ `--content-disposition` ensures correct filenames are preserved.
> 

> ✔ `-P /tmp/`  ensures that the files are downloaded in the /tmp directory.
> 

#### 4.3 Build the Binary

Install the pyinstaller

```bash
pip install pyinstaller
```

This command bundles the script into a single executable named with the specific date version in the `/tmp/dist` directory. 

```bash
cd /tmp
pyinstaller --onefile --name r-shield-aws-03-11-2026 r-shield-hycu_aws.py
```

#### 4.3 Move Files to Target Directory

Move the downloaded files into `/r-shield` directory. 

```bash
sudo mv /tmp/dist/r-shield-aws-03-11-2026 /r-shield/r-shield
sudo mv /tmp/r-shield-config-03-19-2026 /r-shield/r-shield-config

# clean the /tmp directory 
sudo rm -rf /tmp/* 

# Uninstall the pyinstaller 
sudo pip uninstall pyinstaller -y
```

Set appropriate ownership and permissions:

```bash
sudo chown root:root /r-shield/r-shield /r-shield/r-shield-config
sudo chmod +x /r-shield/r-shield
sudo chmod 750 /r-shield/r-shield
sudo chmod 640 /r-shield/r-shield-config
```

# Step 5: Configure and Validate `r-shield` executable (SELinux)

#### 5.1 Verify Current SELinux Context

```bash
ls -Z /r-shield/r-shield
```

Example (before fix):

```bash
unconfined_u:object_r:default_t:s0 /r-shield/r-shield
```

#### 5.2 Assign Correct SELinux Context

Add a persistent SELinux rule to label the binary as executable:

```bash
sudo semanage fcontext -a -t bin_t "/r-shield/r-shield"
```

Apply the context:

```bash
sudo restorecon -v /r-shield/r-shield
```

#### 5.3 Verify Updated Context

```bash
ls -Z /r-shield/r-shield
```

Expected output:

```bash
unconfined_u:object_r:bin_t:s0 /r-shield/r-shield
```

#### 5.4 Troubleshooting SELinux Issues

If the context does not apply correctly:

```bash
# Remove existing rule
sudo semanage fcontext -d "/r-shield/r-shield"
```

Re-add and reapply

```bash
sudo semanage fcontext -a -t bin_t "/r-shield/r-shield"
sudo restorecon -v /r-shield/r-shield
```

# Step 6: Configure `r-shield` as a Systemd Service

#### 6.1 Create the Service Unit File

```bash
sudo vi /etc/systemd/system/r-shield.service
```

Add the following configuration:

```bash
[Unit]
Description=R-Shield Scanner Service
After=network.target

[Service]
Type=simple

# Set the working directory (where logs, etc. will live)
WorkingDirectory=/r-shield/

# Force Python to run in unbuffered mode so print() goes straight to the journal
Environment=PYTHONUNBUFFERED=1

# Your PyInstaller-compiled executable
ExecStart=/r-shield/r-shield

# Explicitly capture all stdout/stderr in the journal
StandardOutput=journal
StandardError=journal

# These signals/timeouts ensure your script can catch SIGINT/SIGTERM for graceful cleanup
KillSignal=SIGINT
KillMode=mixed
TimeoutStopSec=20

[Install]
WantedBy=multi-user.target

```

#### 6.2 Enable the service at boot

```bash
sudo systemctl enable r-shield.service
```

# Step 7: Download YARA Rules

#### 7.1 Create Rules Directory

```bash
sudo mkdir -p /r-shield/git_yara_folder
```

#### 7.2 Clone YARA Rules Repository

```bash
cd git_yara_folder
sudo git clone https://github.com/reversinglabs/reversinglabs-yara-rules.git
```

# Step 8: Validate Service Operation

#### 8.1 Check Service Status

```bash
sudo systemctl status r-shield.service
```

#### 8.2 Start the Service

```bash
sudo systemctl start r-shield.service && sudo journalctl -u r-shield.service -f
```

#### 8.3 Verify Scanner Version Output

```bash
sudo journalctl -u r-shield.service | egrep "Scanner version" | tail -n 1
# Sample Ouput 
Mar 19 06:54:25 r-shield-aws r-shield[51313]: Scanner version: aws-03-11-2026
```

---
