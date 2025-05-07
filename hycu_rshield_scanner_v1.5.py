import json
import os
import signal
import subprocess
from datetime import datetime
import time
from dotenv import load_dotenv
import urllib3
import requests
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import threading
import pickle
import shutil

load_dotenv()

should_exit = threading.Event()

def signal_handler(sig, frame):
    """Handle termination signals (SIGINT, SIGTERM) by setting the exit flag"""
    print("\nShutdown signal received. Finishing current tasks and exiting...",flush=True)
    should_exit.set()
    
    # Attempt to cancel all thread pool futures
    print("Attempting to cancel running tasks...",flush=True)
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            print(f"Thread {thread.name} is still running",flush=True)
    
    # Try to shut down executor immediately (non-blocking)
    try:
        print("Initiating non-blocking executor shutdown...",flush=True)
        executor.shutdown(wait=False)
    except Exception as e:
        print(f"Error shutting down executor: {e}",flush=True)
    
    # Set a timer to forcibly exit if graceful shutdown takes too long
    def force_exit():
        print(f"Graceful shutdown taking over {force_timer_time} seconds, forcing exit...",flush=True)
        os._exit(1)  # Force immediate exit
    
    # Schedule force exit after 20 seconds if we're still running
    force_timer_time = 20.0
    force_timer = threading.Timer(force_timer_time, force_exit)
    force_timer.daemon = True
    force_timer.start()
    
# Register the signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# ----------------------------------------------------------------------------
# Configuration / Global Variables
# ----------------------------------------------------------------------------
key = os.getenv('API-KEY')   # from .env

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {key}"
}

scanned_images_file = "scanned_images.pkl"
git_repo_folder = "git_yara_folder"
yara_rules_path = "yara_rules.yar"
version_dir = "yara_rules_versions"
LOGS_DIR= "/r-shield/logs"
CONFIG_PATH = "/r-shield/r-shield-config"

os.makedirs(LOGS_DIR,exist_ok=True)

session = requests.Session()
session.headers.update(headers)

# For ignoring InsecureRequestWarning (self-signed, etc.)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Thread-safe set of scanned images
scanned_backups = {}
if os.path.exists(scanned_images_file):
    with open(scanned_images_file, "rb") as f:
        try:
            scanned_backups = pickle.load(f)
        except:
            # Fallback for compatibility with old format
            scanned_images = pickle.load(f)
            scanned_backups = {path: 0 for path in scanned_images}

scanned_images_lock = threading.Lock()

def send_teams_message(webhook_url,cluster_name, vm_name, scan_type, matches_found,total_matches=0,short_snippet=None,log_file_path=None,snapshot_uuid=None, error=None):
    """
    Send a notification to Microsoft Teams with scan results.

    Args:
        webhook_url: The Teams webhook URL
        vm_name: Name of the VM that was scanned
        scan_type: "Full" or "Incremental"
        matches_found: Boolean indicating if matches were found
        error: Optional error message if scan failed
    """
    # Format the status message based on results
    if error:
        status = "❌ Failed"
        color = "FF0000"  # Red
        result_text = f"Error: {error}"
    elif matches_found and total_matches > 0:
        status = f"⚠️ Warning: {total_matches} files with malware signatures found"
        color = "FFA500"  # Orange/Yellow
        snippet_str = ""
        if short_snippet:
            snippet_str = "<br>".join(short_snippet)
        if log_file_path:
            snippet_str += f"<br>...for full details see log file {log_file_path}"
        result_text = snippet_str if snippet_str else "YARA rules matched. See log file for details."
    else:
        status = "✅ Completed"
        color = "00FF00"  # Green
        result_text = "No matches found."

    # Create message card for Teams
    message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": color,
        "summary": f"R-Shield Scan Result for {vm_name}",
        "sections": [{
            "activityTitle": f"R-Shield Scan Results: {cluster_name}",
            "activitySubtitle": f"{scan_type} scan completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "facts": [
                {"name": "VM Name", "value": vm_name},
                {"name": "Scan Type", "value": scan_type},
                {"name": "Snapshot uuid", "value": snapshot_uuid},
                {"name": "Status", "value": status},
                {"name": "Result", "value": result_text}
            ],
            "markdown": True
        }]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(
            url=webhook_url,
            headers=headers,
            data=json.dumps(message)
        )
        response.raise_for_status()
        print(f"webhook notification sent successfully.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook message: {e}")
        return False

# ----------------------------------------------------------------------------
# Utility: Save scanned snapshots to avoid repeat scanning
# ----------------------------------------------------------------------------
def save_scanned_images():
    """Save the scanned backups dictionary to a file."""
    with open(scanned_images_file, "wb") as f:
        pickle.dump(scanned_backups, f)

# ----------------------------------------------------------------------------
# Subprocess helper
# ----------------------------------------------------------------------------
# def run_command(command, description):
#     """
#     Wrapper to run a shell command and capture output.
#     Returns stdout+stderr on success, or None on failure.
#     """
#     try:
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         return result.stdout + result.stderr
#     except subprocess.CalledProcessError as e:
#         print(f"Error during {description}: {e.stderr.strip() if e.stderr else str(e)}")
#         return None


def run_command(command, description):
    """
    Wrapper to run a shell command and capture output.
    Returns stdout+stderr even on failure.
    """
    if should_exit.is_set():
            return None
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout + result.stderr
    except subprocess.CalledProcessError as e:
        # Capture both stdout and stderr even if an error occurs
        output = (e.stdout or "") + (e.stderr or "")
        print(f"Error during {description}: {output.strip()}",flush=True)
        return output  # Return partial output instead of None
    
def cleanup_stale_mounts(mount_dirs):
    for mp in mount_dirs:
        try:
            if os.path.ismount(mp):
                print(f"[Startup] Cleaning stale mount: {mp}",flush=True)
                #do not forget to change to run_command after testing ps you most certanly will.
                subprocess.run(["sudo", "guestunmount", mp], check=False, timeout=5)
                subprocess.run(["sudo", "umount", "-lf", mp], check=False, timeout=5)
        except Exception as e:
            print(f"Error cleaning up {mp}: {e}",flush=True)


# ----------------------------------------------------------------------------
#  Update YARA rules if Git commit SHA changed
# ----------------------------------------------------------------------------
def update_rules_if_changed_sha(
    git_repo_folder,
    output_file,
    custom_yara_rules=False,
    old_version=None
):
    """
    - If custom_yara_rules=True => Aggregate custom folder ONCE if old_version is None.
      Otherwise, skip new aggregator and reuse old_version.
    - If custom_yara_rules=False => do normal Git-based aggregator using commit SHA check.

    Returns a string representing the (possibly new) version.
    """

    # -------------------------------------------------------------------------
    # 1) If user provided a custom folder (different from git_repo_folder)
    # -------------------------------------------------------------------------
    if custom_yara_rules:
        if old_version:
            # Already did the aggregator for custom rules once, or we have some version
            print(f"Custom folder: {git_repo_folder}. Reusing old_version: {old_version}",flush=True)
            return old_version
        else:
            # First time run => aggregator ONCE
            print(f" Custom folder. Aggregating rules for the first time: {git_repo_folder}",flush=True)
            return actually_aggregate_rules(git_repo_folder, output_file)

    # -------------------------------------------------------------------------
    # 2) Otherwise, do normal Git-based logic with commit SHA check
    # -------------------------------------------------------------------------
    git_repo_path = os.path.join(git_repo_folder, "reversinglabs-yara-rules")

    # 1) Get old commit SHA
    before_sha = run_command(["git", "-C", git_repo_path, "rev-parse", "HEAD"], "get before-sha")
    if before_sha:
        before_sha = before_sha.strip()
    else:
        before_sha = None

    # 2) Pull
    pull_output = run_command(["git", "-C", git_repo_path, "pull"], "git pull")
    if pull_output is None:
        # error or something
        print("error or empty output from 'git pull'.",flush=True)
        # fallback: if old_version exists, keep it, else do aggregator once
        return old_version or actually_aggregate_rules(git_repo_folder, output_file)

    # 3) Get new HEAD SHA
    after_sha = run_command(["git", "-C", git_repo_path, "rev-parse", "HEAD"], "get after-sha")
    if after_sha:
        after_sha = after_sha.strip()
    else:
        after_sha = None

    # 4) Compare
    if before_sha and after_sha and (before_sha == after_sha):
        print(f"No new commits in Git. Reusing old version: {old_version}",flush=True)
        if old_version:
            return old_version
        else:
            # First time run ever => aggregator once
            return actually_aggregate_rules(git_repo_folder, output_file)
    else:
        print("New commit detected; building new aggregator version.",flush=True)
        return actually_aggregate_rules(git_repo_folder, output_file)

def actually_aggregate_rules(git_repo_folder, output_file):
    """
    Aggregate all .yara (or .yar) files into 'output_file' (yara_rules.yar).
    Then copy the result to 'yara_rules_versions/yara_rules_<timestamp>.yar'.
    Return the new timestamp as the version.
    """
    # 1) Aggregate .yara and .yar into a single file
    try:
        with open(output_file, 'w') as outfile:
            for root, dirs, files in os.walk(git_repo_folder):
                for file in files:
                    # You can change this if you only want .yara or both
                    if file.endswith(".yara") or file.endswith(".yar"):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r') as infile:
                                outfile.write(infile.read() + "\n")
                        except IOError as e:
                            print(f"Error reading file '{file_path}': {e}",flush=True)
    except IOError as e:
        print(f"Error writing to output file '{output_file}': {e}",flush=True)

    # 2) Copy the newly created aggregator file into a versioned file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(version_dir, exist_ok=True)  # Ensure directory exists
    versioned_rules_file = os.path.join(version_dir, f"yara_rules_{timestamp}.yar")

    try:
        shutil.copy(output_file, versioned_rules_file)
        print(f"Created new YARA version: {versioned_rules_file}",flush=True)
    except IOError as e:
        print(f"Error copying {output_file} -> {versioned_rules_file}: {e}",flush=True)

    return timestamp

# ----------------------------------------------------------------------------
# 1) Get cluster IP mapping: { clusterExternalId : externalIpAddress }
# ----------------------------------------------------------------------------
def get_cluster_ips():
    """
    Queries the cluster endpoint to get all clusters and returns
    { externalId: externalIpAddress } for each cluster.
    """
    cluster_url = f"{HYCU_URL}/rest/v1.0/administration/clusters"
    cluster_info = {}

    try:
        params = {"pageSize": 100, "pageNumber": 1}
        while True:
            response = requests.get(cluster_url, params=params, headers=headers, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch cluster data: {response.status_code} - {response.text}",flush=True)
                break

            data = response.json()
            entities = data.get("entities", [])

            for entity in entities:
                external_id = entity.get("externalId")
                external_ip = entity.get("externalIpAddress")
                cluster_name = entity.get("name", "UnknownCluster")
                if external_id and external_ip:
                    cluster_info[external_id] = {
                        "ip":external_ip,
                        "name":cluster_name
                    }

            if len(entities) < params["pageSize"]:
                break
            params["pageNumber"] += 1

    except requests.exceptions.RequestException as e:
        print(f"Error processing GET request: {e}",flush=True)
    except ValueError as e:
        print(f"Error processing JSON: {e}",flush=True)
    except Exception as e:
        print(f"Unexpected exception occurred: {e}",flush=True)

    return cluster_info

# ----------------------------------------------------------------------------
# 2) Get the VMs. Return list of { vmName, externalHypervisorId }
# ----------------------------------------------------------------------------
def get_vms():
    base_url = f"{HYCU_URL}/rest/v1.0/vms"
    vms = []

    try:
        params = {"pageNumber": 1, "pageSize": 100}
        while True:
            response = session.get(base_url, params=params, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch VM data: {response.status_code} - {response.text}",flush=True)
                break

            data = response.json()
            entities = data.get("entities", [])

            for entity in entities:
                if entity.get("status") == "PROTECTED":
                    vms.append({
                        "vmName": entity["vmName"],
                        "externalHypervisorId": entity.get("externalHypervisorId", None)
                    })

            if len(entities) < params["pageSize"]:
                break

            params["pageNumber"] += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call for VMs: {e}",flush=True)
    except ValueError as e:
        print(f"An error occurred while parsing JSON for VMs: {e}",flush=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}",flush=True)

    return vms

# ----------------------------------------------------------------------------
# 3) Get latest backup for a VM name - OPTIMIZED to only get latest backup
# ----------------------------------------------------------------------------
def get_latest_backup(vm_name):
    """
    Get only the latest backup for a specific VM.
    Returns a tuple of (latest_backup, count, is_full_backup) where:
    - latest_backup is the backup details or None if none found
    - count is the total number of backups for this VM
    - is_full_backup is a boolean indicating if it's a full backup
    """
    base_url = f"{HYCU_URL}/rest/v1.0/vms/backups"
    params = {"pageNumber": 1, "pageSize": 100}

    # Will hold all backups for this VM
    vm_backups = []

    try:
        while True:
            response = session.get(base_url, params=params, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code} - {response.text}",flush=True)
                break

            data = response.json()
            entities = data.get("entities", [])

            # Filter backups for this specific VM and add to our list
            for entity in entities:
                if vm_name == entity.get("vmName"):
                    vm_backups.append(entity)

            if len(entities) < params["pageSize"]:
                break

            params["pageNumber"] += 1

        # Sort backups by restore point timestamp (newest first)
        if vm_backups:
            vm_backups.sort(key=lambda x: x["restorePointInMillis"], reverse=True)
            # Get the latest backup
            latest_backup = vm_backups[0]
            # Check if it's a full backup
            second_latest_backup = vm_backups[1] if len(vm_backups) > 1 else None
            is_full_backup = latest_backup.get("type") == "FULL_BACKUP"
            # Return the backup, count, and full backup status
            return latest_backup,second_latest_backup, len(vm_backups), is_full_backup

        return None,None, 0, False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call for vm:{vm_name} {e}",flush=True)
    except ValueError as e:
        print(f"An error occurred while parsing JSON for vm:{vm_name} {e}",flush=True)
    except Exception as e:
        print(f"An unexpected error occurred for vm:{vm_name} {e}",flush=True)

    return None, 0, False

# ----------------------------------------------------------------------------
# 4) Fetch NDFS paths for a given backup
# ----------------------------------------------------------------------------
def get_ndfs_paths(backup_uuid):
    base_url = f"{HYCU_URL}/rest/v1.0/vms/backup/{backup_uuid}/metadata"
    params = {"pageNumber": 1, "pageSize": 100}
    ndfs_paths = []

    try:
        while True:
            response = session.get(base_url, params=params, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code} - {response.text}",flush=True)
                break

            data = response.json()
            entities = data.get("entities", [])

            for entity in entities:
                vDiskList = entity.get("vDiskList", [])
                for vDisk in vDiskList:
                    ndfsPath = vDisk.get("ndfsPath")
                    if ndfsPath:
                        ndfs_paths.append({
                            "path": ndfsPath,
                            "virtualDiskId": vDisk.get("virtualDiskId"),
                            "vm_name": entity.get("vmName")
                        })

            if len(entities) < params["pageSize"]:
                break
            params["pageNumber"] += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call: {e}",flush=True)
    except ValueError as e:
        print(f"An error occurred while parsing JSON: {e}",flush=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}",flush=True)

    return ndfs_paths

# ----------------------------------------------------------------------------
# 5) Fetch snapshot paths
# ----------------------------------------------------------------------------
def get_snapshot_paths():
    base_url = f"{HYCU_URL}/rest/v1.0/vms/snapshots"
    params = {"pageNumber": 1, "pageSize": 100}
    snapshot_paths = []

    try:
        while True:
            response = session.get(base_url, params=params, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code} - {response.text}",flush=True)
                break

            data = response.json()
            entities = data.get("entities", [])

            for entity in entities:
                disks = entity.get("disks", [])
                for disk in disks:
                    snapshot_paths.append({
                        "path": disk.get("path"),
                        "externalId": disk.get("externalId")
                    })

            if len(entities) < params["pageSize"]:
                break
            params["pageNumber"] += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call: {e}",flush=True)
    except ValueError as e:
        print(f"An error occurred while parsing JSON: {e}",flush=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}",flush=True)

    return snapshot_paths


def return_paths(ndfs_paths, snapshot_paths, latest_backup):
    """
    Build a combined list of:
        {"ndfs_path": "...", "snapshot_path": "...", "vm_name": "..."}
    by matching vDisk's 'virtualDiskId' with snapshot's 'externalId'.
    Uses snapshot UUID from the latest backup to ensure we get the newest snapshots.
    """
    try:
        if not ndfs_paths or not snapshot_paths:
            raise ValueError("One or both input lists are empty")

        # Get the snapshot UUID from the latest backup
        backup_snapshot_uuid = None
        for snapshot in latest_backup.get("snapshots", []):
            backup_snapshot_uuid = snapshot.get("snapshot_uuid")
            if backup_snapshot_uuid:
                break

        if not backup_snapshot_uuid:
            print("Warning: Could not find snapshot UUID in latest backup.",flush=True)
        else:
            print(f"Found backup snapshot UUID: {backup_snapshot_uuid}",flush=True)

        # Group snapshots by externalId
        snapshot_dict = {}
        for snap in snapshot_paths:
            ext_id = snap["externalId"]
            path = snap["path"].lstrip("/")

            # Check if this snapshot path contains the backup's snapshot UUID
            if backup_snapshot_uuid and backup_snapshot_uuid in path:
                snapshot_dict[ext_id] = path
                print(f"Found exact match for backup snapshot UUID {backup_snapshot_uuid} in path {path}",flush=True)
            elif ext_id not in snapshot_dict:
                # Fallback: if no UUID match, just use the first one we find
                snapshot_dict[ext_id] = path

        matched_parts = []
        for ndfs in ndfs_paths:
            ext_id = ndfs["virtualDiskId"]
            if ext_id in snapshot_dict:
                matched_parts.append({
                    "ndfs_path": "/".join(ndfs["path"].split("/", 2)[:2]),
                    "snapshot_path": snapshot_dict[ext_id],
                    "vm_name": ndfs["vm_name"],
                    "snapshot_uuid": backup_snapshot_uuid
                })
        return matched_parts

    except KeyError as e:
        print(f"Key error while processing paths: {e}",flush=True)
    except Exception as e:
        print(f"Unexpected error occurred while comparing paths: {e}",flush=True)

    return []


# ----------------------------------------------------------------------------
# 7) Utilities for mounting & scanning
# ----------------------------------------------------------------------------
def get_root_partition(image_path):
    """
    Tries to detect the root partition using guestfish inspect-os first.
    If that fails, tries virt-filesystems.
    """
    os.environ['LIBGUESTFS_DEBUG'] = '1'
    os.environ['LIBGUESTFS_TRACE'] = '1'
    try:
        # Attempt with guestfish inspect-os
        output = subprocess.check_output(
            ["sudo", "guestfish", "--ro", "-a", image_path, "-i", "inspect-os"],
            universal_newlines=True,
            stderr=subprocess.STDOUT
        )
        partitions = [line.strip() for line in output.split("\n") if line.strip()]
        if partitions:
            return partitions[0]
    except subprocess.CalledProcessError as e:
        print(f"inspect-os failed: {e.output}",flush=True)
        print("Falling back to filesystem detection...",flush=True)

        try:
            output = subprocess.check_output(
                ["sudo", "virt-filesystems", "-a", image_path, "--long", "--all"],
                universal_newlines=True,
                stderr=subprocess.STDOUT
            )
            lines = output.splitlines()
            filesystems = {}
            for line in lines:
                line = line.strip()
                if (not line) or (line.lower().startswith("name")):
                    continue
                columns = line.split()
                if len(columns) < 2:
                    continue

                device_name = columns[0]
                device_type = columns[1].lower()
                if device_type in [
                    "partition","filesystem","lvm2","lvm1","lvm_thin","lvm_snapshot",
                    "lvm_cache","lvm_mirror","lvm_raid","dm_crypt"
                ]:
                    fs_type = columns[2] if len(columns) > 2 else "unknown"
                    filesystems[device_name] = fs_type

            if filesystems:
                return next(iter(filesystems.keys()))
            else:
                print("No valid partitions/filesystems found in virt-filesystems output.",flush=True)
                print(output)

        except subprocess.CalledProcessError as fallback_error:
            print(f"Error during filesystem detection with virt-filesystems: {fallback_error}",flush=True)

    return None

def yara_scan_incremental(
    yara_rules_path,
    mount_point,
    vm_name,
    cluster_name,
    previous_backup_time,
    snapshot_uuid=None,
    rules_version=None
):
    """
    Perform incremental YARA scanning using previous_backup_time as cutoff.
    Log scan details regardless of whether matches are found.
    """
    if should_exit.is_set():
        print(f"Skipping scan for {vm_name} due to shutdown request",flush=True)
        return
    webhook_url = WEBHOOK_URL
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(LOGS_DIR, f"scan_log_{vm_name}_{current_time}.log")

    error_message = None
    matches_found = False
    matched_files = []
    total_matches = 0

    def log_write(message, log=None):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} {message}\n"
        print(log_entry, end="",flush=True)
        if log:
            log.write(log_entry)

    try:
        with open(log_file_path, "a") as log:
            scan_start_time = datetime.now()
            start_time_str = scan_start_time.strftime("%Y-%m-%d %H:%M:%S")

            log_write("********** [ Incremental Scan Info ] **********", log)
            log_write(f"Incremental scan started for VM: {vm_name} at {start_time_str}", log)

            min_time = int(previous_backup_time / 1000)
            readable_time = datetime.fromtimestamp(min_time).strftime('%Y-%m-%d %H:%M:%S')
            log_write(f"Performing incremental scan for files newer than {readable_time}", log)

            if rules_version:
                log_write(f"YARA Ruleset Version: {rules_version}", log)

            # 1) Build a list of files changed after min_time using 'find'
            temp_file_list = f"/tmp/yara_scan_files_{vm_name}_{current_time}.txt"
            if should_exit.is_set():
                print(f"Skipping scan for {vm_name} due to shutdown request",flush=True)
                return
            find_cmd = [
                "sudo", "find", mount_point,
                "-type", "f",
                "-not", "-path", "*/\\.*",  # skip hidden .files if desired
                "-newermt", readable_time
            ]

            try:
                find_output = run_command(find_cmd, "Find command for incremental scan")
                if find_output:
                    # Check for "Input/output error" in the find output
                    if "Input/output error" in find_output:
                        error_io = (
                            "Error input/output message in most cases indicates that a snapshot being scanned "
                            "has been deleted from the cluster. This can happen if a new backup of the VM "
                            "was executed while the scan was still ongoing. Use fast restore option in the HYCU "
                            "policy to keep multiple snapshots on the cluster."
                        )
                        log_write(f"WARNING: {error_io}", log)
                        # Show the user the replaced text
                        modified_find_output = find_output.replace("Input/output error", error_io)
                        log_write(modified_find_output, log)

                    # Write all 'find' results to a temporary file
                    with open(temp_file_list, "w") as f:
                        f.write(find_output)
                else:
                    # If find_output is empty (no changed files), create empty file
                    with open(temp_file_list, "w") as f:
                        f.write("")

                # 2) If the file list isn't empty, run YARA with '--scan-list'
                if os.path.exists(temp_file_list) and os.path.getsize(temp_file_list) > 0:
                    yara_cmd = ["sudo", "yara", yara_rules_path, "--scan-list", temp_file_list]
                    if should_exit.is_set():
                        print(f"Skipping scan for {vm_name} due to shutdown request",flush=True)
                        return
                    output = run_command(yara_cmd, "Incremental YARA scan")

                    if output and output.strip():
                        lines = output.splitlines()
                        has_error = False

                        # Replace known errors with more descriptive text
                        if "error: 4" in output:
                            error_message_4 = (
                                "Error 4 indicates that a snapshot being scanned was deleted from the cluster. "
                                "A new backup might have been executed while the scan was ongoing. Use fast restore "
                                "option in the HYCU policy to keep multiple snapshots on the cluster."
                            )
                            log_write(f"ERROR: {error_message_4}", log)
                            output = output.replace("error: 4", error_message_4)
                            has_error = True
                            error_message = error_message_4

                        if "Input/output error" in output:
                            error_io = (
                                "Error input/output message typically indicates that a snapshot being scanned "
                                "has been deleted from the cluster. This can happen if a new backup was executed "
                                "while the scan was ongoing. "
                                "Use fast restore option in the HYCU policy to keep multiple snapshots on the cluster."
                            )
                            log_write(f"ERROR: {error_io}", log)
                            output = output.replace("Input/output error", error_io)
                            has_error = True
                            error_message = error_io

                        # Log the entire YARA output line-by-line
                        for line in lines:
                            log_write(line, log)

                        # If we didn't flag an error, parse lines for actual matches
                        if not has_error:
                            # For each line, check if there's a file path
                            # Example approach: if line has a slash or backslash, treat it as a match line
                            for line in lines:
                                line = line.strip()
                                if "/" in line or "\\" in line:
                                    matches_found = True
                                    matched_files.append(line)
                    else:
                        log_write("No matches found in the scan.", log)
                else:
                    log_write("No files found for scanning.", log)

            except Exception as e:
                error_message = str(e)
                log_write(f"Error during scanning process: {error_message}", log)
            finally:
                # Clean up temp file
                if os.path.exists(temp_file_list):
                    os.remove(temp_file_list)

                scan_end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_write(f"Scan completed at {scan_end_time}.", log)

                if error_message:
                    log_write("********** [ Scan Failed ] **********", log)
                else:
                    log_write("********** [ Scan Complete ] **********", log)

                print(f"Log saved to {log_file_path}",flush=True)

    except Exception as e:
        error_message = str(e)
        print(f"Error during incremental YARA scanning: {e}",flush=True)
        with open(log_file_path, "a") as log:
            log_write(f"ERROR: {error_message}", log)
            log_write("********** [ Scan Failed ] **********", log)

    finally:
        # Evaluate total matches & build short snippet
        total_matches = len(matched_files)
        short_snippet = matched_files[:3]

        # Send a Teams message if we have a webhook
        if webhook_url:
            send_teams_message(
                webhook_url=webhook_url,
                cluster_name=cluster_name,
                vm_name=vm_name,
                scan_type="Incremental",
                matches_found= matches_found,
                total_matches=total_matches,
                short_snippet=short_snippet,
                log_file_path=log_file_path,
                snapshot_uuid=snapshot_uuid,
                error=error_message
            )
        else:
            print("no webhook provided, scan results will not be sent",flush=True)

def yara_scan_full(yara_rules_path, mount_point, vm_name, cluster_name,snapshot_uuid = None, rules_version=None):
    """
    Perform a full YARA scan without incremental logic.
    Log scan details regardless of whether matches are found.
    """
    if should_exit.is_set():
        print(f"Skipping scan for {vm_name} due to shutdown request",flush=True)
        return
    webhook_url = WEBHOOK_URL
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(LOGS_DIR, f"scan_log_{vm_name}_{current_time}.log")
    error_message = None
    matches_found = False
    matched_files = []
    total_matches = 0

    # We'll define short_snippet here, so it exists even if we hit an exception
    short_snippet = []

    def log_write(message, log=None):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} {message}\n"
        print(log_entry, end="",flush=True)
        if log:
            log.write(log_entry)

    try:
        # Create log file at the start
        with open(log_file_path, "a") as log:
            # Log scan start time
            scan_start_time = datetime.now()
            start_time_str = scan_start_time.strftime("%Y-%m-%d %H:%M:%S")

            log_write("********** [ Full Scan Info ] **********", log)
            log_write(f"Full scan started for VM: {vm_name} at {start_time_str}", log)
            log_write("Performing full scan of all files", log)

            if rules_version:
                log_write(f"YARA Ruleset Version: {rules_version}", log)

            # Regular YARA scan of all files
            yara_cmd = ["sudo", "yara", "-r", yara_rules_path, mount_point]
            if should_exit.is_set():
                print(f"Skipping scan for {vm_name} due to shutdown request",flush=True)
                return
            output = run_command(yara_cmd, "Full YARA scan")

            if output and output.strip():
                lines = output.splitlines()
                # 1) If the output has "error: 4", we replace it with a more descriptive message
                if "error: 4" in output:
                    error_message = (
                        "Error 4 message in most cases indicates that a snapshot being scanned "
                        "has been deleted from the cluster. This can happen if a new backup of "
                        "the VM was executed while the scan was still ongoing. Use fast restore "
                        "option in HYCU policy to keep multiple snapshots on the cluster."
                    )
                    log_write(f"ERROR: {error_message}", log)

                    # Replace the literal 'error: 4' in the output before we write it to the log
                    modified_output = output.replace("error: 4", error_message)
                    log_write(modified_output, log)

                else:
                    # 2) No 'error: 4' found, so parse lines for matches
                    for line in lines:
                        # If a line has a slash or backslash, it might be a file path
                        if "/" in line or "\\" in line:
                            matches_found = True
                            matched_files.append(line.strip())

                    total_matches = len(matched_files)

                    # Write the original YARA output to the log (line by line)
                    # but make sure we don't do 'log_write(output, log)' repeatedly,
                    # or else it duplicates the entire output for each line.
                    for line in lines:
                        log_write(line, log)

            else:
                log_write("No matches found in the scan.", log)

            # Log scan end time
            scan_end_time = datetime.now()
            end_time_str = scan_end_time.strftime("%Y-%m-%d %H:%M:%S")
            log_write(f"Scan completed at {end_time_str}.", log)

            if error_message:
                log_write("********** [ Scan Failed ] **********", log)
            else:
                log_write("********** [ Scan Complete ] **********", log)

            print(f"Log saved to {log_file_path}",flush=True)

    except Exception as e:
        error_message = str(e)
        print(f"Error during full YARA scanning: {e}",flush=True)
        with open(log_file_path, "a") as log:
            log_write(f"ERROR: {error_message}", log)
            log_write("********** [ Scan Failed ] **********", log)

    finally:
        # Build a short snippet from the first few matched lines
        short_snippet = matched_files[:3]

        # Send Teams notification
        if webhook_url:
            send_teams_message(
                webhook_url=webhook_url,
                cluster_name=cluster_name,
                vm_name=vm_name,
                scan_type="Full",
                matches_found=matches_found,
                total_matches=total_matches,
                short_snippet=short_snippet,
                log_file_path=log_file_path,
                snapshot_uuid=snapshot_uuid,
                error=error_message,
            )
            
        else:
            print("no webhook provided, scan results will not be sent",flush=True)

# ----------------------------------------------------------------------------
# 8) Mount function with concurrency locks
# ----------------------------------------------------------------------------
mount_lock = threading.Lock()

def mount_shares(nfs_ip, nfs_path, image_file, yara_rules_path, vm_name, previous_backup_time, rules_version,snapshot_uuid=None, do_full_scan=False):
    """
    Mount NFS share and the disk image for scanning.
    Uses two separate mount points from the shared queues.
    """
    if should_exit.is_set():
        return
    with mount_lock:
        if nfs_mount_point_queue.empty() or image_mount_point_queue.empty():
            raise RuntimeError("No available mount points")
        nfs_mount_point = nfs_mount_point_queue.get()
        image_mount_point = image_mount_point_queue.get()

    try:
        # Unmount if image mount is busy
        if os.path.ismount(image_mount_point):
            print(f"Disk image is already mounted at {image_mount_point}. Attempting to unmount.",flush=True)
            run_command(["sudo", "guestunmount", image_mount_point], "unmounting guestmount")

        # Unmount if NFS mount is busy
        if os.path.ismount(nfs_mount_point):
            print(f"NFS share is already mounted at {nfs_mount_point}. Attempting to unmount.",flush=True)
            run_command(["sudo", "umount", "-lf", nfs_mount_point], "lazy unmounting NFS share")

        # Mount NFS share
        print(f"Mounting NFS share at {nfs_mount_point} with IP={nfs_ip}...",flush=True)
        run_command(["sudo", "mount", "-t", "nfs", f"{nfs_ip}:{nfs_path}", nfs_mount_point], "NFS mount")

        # Validate image file
        image_path = os.path.join(nfs_mount_point, image_file)
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        # Inspect + mount image
        print(f"Inspecting and mounting image at {image_mount_point}...",flush=True)
        root_partition = get_root_partition(image_path)
        if not root_partition:
            raise RuntimeError("Failed to determine the root partition.")

        run_command(
            ["sudo", "guestmount", "-a", image_path, "-m", root_partition, "--ro", image_mount_point],
            "Image mount"
        )

        # Just a quick listing
        print("Listing files in mounted dir",flush=True)
        files = os.listdir(image_mount_point)
        print("Files in root of the image: ", files,flush=True)

        # Choose the right scanning function based on whether we're doing full or incremental
        if do_full_scan:
            print(f"Running full YARA scan on VM={vm_name}...",flush=True)
            yara_scan_full(yara_rules_path, image_mount_point, vm_name,cluster_name, snapshot_uuid, rules_version)
        else:
            print(f"Running incremental YARA scan on VM={vm_name}...",flush=True)
            yara_scan_incremental(yara_rules_path, image_mount_point, vm_name,cluster_name, previous_backup_time,snapshot_uuid, rules_version,)
    except Exception as e:
            print(f"Error during NFS or image processing: {e}",flush=True)
    finally:
            # Cleanup
        if os.path.ismount(image_mount_point):
            run_command(["sudo", "guestunmount", image_mount_point], "unmounting image")
        if os.path.ismount(nfs_mount_point):
            run_command(["sudo", "umount", "-lf", nfs_mount_point], "unmounting NFS share")

        with mount_lock:
            nfs_mount_point_queue.put(nfs_mount_point)
            image_mount_point_queue.put(image_mount_point)


def parse_config_file(config_path: str):
    """
    Parses a config file of KEY=VALUE lines into a dictionary.
    Lines starting with '#' or empty lines are ignored.
    """
    config = {}
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found.")

    with open(config_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                # Skip lines without a key=value format
                continue
            key, value = line.split("=", 1)
            key = key.strip().upper()
            value = value.strip()
            config[key] = value
    return config


# Process task with the updated backup type information
def process_task(match, nfs_ip, yara_version,is_full_backup=False, backup_count=0, previous_backup_time=None, snapshot_uuid=None, force_full=False):
    """
    match = {
      "ndfs_path": "...",
      "snapshot_path": "...",
      "vm_name": "..."
    }
    nfs_ip is the cluster IP mapped to that VM's externalHypervisorId.
    yara_version is the timestamp or label of the current YARA rules.
    is_full_backup indicates if the latest backup is a full backup.
    backup_count is the total number of backups for this VM.
    previous_backup_time is the timestamp of the previous backup (if any).
    """
    if should_exit.is_set():
        return
    
    nfs_path = match["ndfs_path"]
    image_file = match["snapshot_path"]
    vm_name = match["vm_name"]

    # Determine scan type based on the new logic
    do_full_scan = force_full or backup_count <= 1 or is_full_backup

    try:
        print(f"Processing VM={vm_name} with NFS IP={nfs_ip}, path={nfs_path}, image_file={image_file}",flush=True)

        if do_full_scan:
            if force_full:
                print(f"VM '{vm_name}': Force full scan option enabled. Performing full scan.",flush=True)
            elif backup_count <= 1:
                print(f"VM '{vm_name}': First backup (count={backup_count}). Performing full scan.",flush=True)
            elif is_full_backup:
                print(f"VM '{vm_name}': Latest backup is a FULL_BACKUP. Performing full scan.",flush=True)
        else:
            print(f"VM '{vm_name}': Incremental backup detected. Performing incremental scan.",flush=True)
            print(f"Previous backup time: {datetime.fromtimestamp(previous_backup_time/1000).strftime('%Y-%m-%d %H:%M:%S')}",flush=True)

        mount_shares(nfs_ip, nfs_path, image_file, yara_rules_path, vm_name, previous_backup_time, yara_version,snapshot_uuid, do_full_scan)

        if should_exit.is_set():
            return

    except Exception as e:
        print(f"Error processing task for VM={vm_name}, NFS path={nfs_path}, image={image_file}: {e}",flush=True)


# ----------------------------------------------------------------------------
# 10) MAIN
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    
    config = parse_config_file(config_path=CONFIG_PATH)
    args = {}

    args["rules"] = config.get("RULES",git_repo_folder)
    args["vm_list"] = config.get("VM_LIST", None)
    args["force_full_scan"] = config.get("FORCE_FULL_SCAN", "False").strip().lower() == "true"
    args["buffer_minutes"] = int(config.get("BUFFER_MINUTES",0))

    #handle concurrency gracefully
    concurrency_str = config.get("CONCURRENCY", "")
    if not concurrency_str.strip():
        #default_concurrency
        concurrency = 4
    else:
        concurrency = int(concurrency_str)

    if concurrency < 1:
        raise ValueError(f"Concurrency must be a positive integer concurrency{concurrency}")
    args["concurrency"] = concurrency

    if "HYCU_URL" not in config:
        raise ValueError("Missing requiered parameter HYCU_URL in r-shield-config")
    args["hycu_url"] = config.get("HYCU_URL")
    args["webhook"] = config.get("WEBHOOK")

    # We'll use 'hycu_url' to match our functions that reference it
    HYCU_URL = args["hycu_url"]
    WEBHOOK_URL = args["webhook"]

    # We'll remember the current YARA ruleset version between loops
    current_rules_version = None

    # 1) Build dynamic mount points from concurrency
    NFS_MOUNT_POINTS = [f"/mnt/nfs{i}" for i in range(1, concurrency + 1)]
    IMAGE_MOUNT_POINTS = [f"/mnt/img{i}" for i in range(1, concurrency + 1)]

    # hopless fix for service if this does not run burn it with fire
    cleanup_stale_mounts(NFS_MOUNT_POINTS + IMAGE_MOUNT_POINTS)

    # Create them if they do not exist
    for mp in (NFS_MOUNT_POINTS + IMAGE_MOUNT_POINTS):
        if not os.path.isdir(mp):
            print(f"[Startup] {mp} optimizing directory structure",flush=True)
            try:
                subprocess.run(["sudo", "umount", "-lf", mp], check=False, timeout=3)
            except Exception as e:
                print(f"[Startup] Failed to unmount {mp}: {e}")
            try:
                os.makedirs(mp, exist_ok=True)
                print(f"[Startup] Successfully created mount point: {mp}",flush=True)
            except Exception as e:
                print(f"[Startup] Failed to create mount point {mp}: {e}",flush=True)
        else:
            # Directory exists and is fine
            os.makedirs(mp, exist_ok=True)

    # Queues for concurrency
    nfs_mount_point_queue = Queue()
    image_mount_point_queue = Queue()
    for nfs_mount in NFS_MOUNT_POINTS:
        nfs_mount_point_queue.put(nfs_mount)
    for img_mount in IMAGE_MOUNT_POINTS:
        image_mount_point_queue.put(img_mount)

    # Thread pool
    executor = ThreadPoolExecutor(max_workers=concurrency)

    # Gather cluster IPs once
    cluster_ips = get_cluster_ips()

    try:
        while not should_exit.is_set():
            print(f"Starting processing loop with concurrency={concurrency}...",flush=True)

            # A) Update or build YARA rules (only if commit SHA changed)
            custom_rules = (args["rules"] != git_repo_folder)
            current_rules_version = update_rules_if_changed_sha(
                args["rules"],
                yara_rules_path,
                custom_yara_rules=custom_rules,
                old_version=current_rules_version
            )

            # B) Fetch the VMs (status="PROTECTED")
            vm_list = get_vms()  # Each item = { "vmName": ..., "externalHypervisorId": ... }

            # B1) Optionally filter by --vm-list
            if args["vm_list"]:
                if os.path.exists(args["vm_list"]):
                    with open(args["vm_list"], "r") as f:
                        desired_vms = {line.strip() for line in f if line.strip()}
                    vm_list = [vm for vm in vm_list if vm["vmName"] in desired_vms]
                else:
                    print(f"Warning: VM list file '{args['vm_list']}' not found. No filtering applied.",flush=True)
            else:
                print("No VM list specified. Scanning all protected VMs.",flush=True)

            # C) Build a list of valid VMs that have a matching cluster IP
            valid_vms = []
            for vm_info in vm_list:
                vm_name = vm_info["vmName"]
                ext_hyp_id = vm_info["externalHypervisorId"]

                if not ext_hyp_id or ext_hyp_id not in cluster_ips:
                    print(f"No valid cluster IP for VM '{vm_name}' (extHypId={ext_hyp_id}). Skipping.",flush=True)
                    continue

                nfs_data = cluster_ips[ext_hyp_id]
                vm_info["nfs_ip"] = nfs_data["ip"]
                vm_info["cluster_name"] = nfs_data["name"]
                valid_vms.append(vm_info)

            # D) For each valid VM, fetch backups and figure out full vs incremental
            matched_parts = []
            for vm_info in valid_vms:
                vm_name = vm_info["vmName"]
                nfs_ip = vm_info["nfs_ip"]
                cluster_name = vm_info["cluster_name"]

                # Get the latest and second-latest backups
                latest_backup, second_latest_backup, backup_count, is_full_backup = get_latest_backup(vm_name)
                if not latest_backup:
                    print(f"No backups found for VM='{vm_name}'. Skipping.",flush=True)
                    continue
                # skip scan if backup in progress
                if latest_backup.get("status") != "OK":
                    print(f"Latest backup for VM='{vm_name}' is not OK "
                          f"(status={latest_backup.get('status')}). Skipping scan.",flush=True)
                    continue

                backup_uuid = latest_backup["uuid"]
                backup_timestamp = latest_backup.get("restorePointInMillis", 0)

                # Determine previous_backup_time for incremental
                if args["force_full_scan"] or backup_count <= 1 or is_full_backup:
                    # => Full scan
                    print(f"VM '{vm_name}': Doing FULL scan (force_full={args['force_full_scan']}, "
                          f"count={backup_count}, is_full={is_full_backup}).",flush=True)
                    previous_backup_time = None
                else:
                    # => Incremental scan using the second_latest_backup by default
                    if second_latest_backup is None:
                        # Fallback: if only 1 backup actually existed
                        print(f"VM '{vm_name}': Only 1 backup found, fallback to full scan.",flush=True)
                        previous_backup_time = None
                    else:
                        second_backup_timestamp = second_latest_backup["restorePointInMillis"]
                        latest_backup_timestamp = latest_backup["restorePointInMillis"]
                        if args["buffer_minutes"] > 0:
                            previous_backup_time = latest_backup_timestamp - (args["buffer_minutes"] * 60 * 1000)
                            print(
                                f"VM '{vm_name}': Overriding second-latest logic with LATEST backup time - buffer.\n"
                                f"Latest backup time: {datetime.fromtimestamp(latest_backup_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')}\n"
                                f"Buffer: {args['buffer_minutes']} minute(s)\n"
                                f"Incremental scanning files newer than: "
                                f"{datetime.fromtimestamp(previous_backup_time / 1000).strftime('%Y-%m-%d %H:%M:%S')}"
                            ,flush=True)
                        else:
                            previous_backup_time = second_backup_timestamp
                            print(
                                f"VM '{vm_name}': Using second-latest backup timestamp "
                                f"{datetime.fromtimestamp(previous_backup_time / 1000).strftime('%Y-%m-%d %H:%M:%S')} "
                                "for incremental scan."
                            ,flush=True)

                # D2) Build the NDFS & snapshot path matches (always from the *latest* backup’s UUID)
                ndfs_paths = get_ndfs_paths(backup_uuid)
                snapshot_paths = get_snapshot_paths()
                matches = return_paths(ndfs_paths, snapshot_paths, latest_backup)
                if not matches:
                    print(f"No NDFS-Snapshot matches for VM='{vm_name}'. Skipping.",flush=True)
                    continue

                # Append relevant info to each match
                for m in matches:
                    m["nfs_ip"] = nfs_ip
                    m["previous_backup_time"] = previous_backup_time
                    m["is_full_backup"] = is_full_backup
                    m["backup_count"] = backup_count
                    m["backup_timestamp"] = backup_timestamp
                    matched_parts.append(m)

            # E) Submit matched parts for scanning
            if matched_parts:
                for match in matched_parts:
                    snapshot_path = match["snapshot_path"]
                    vm_name = match["vm_name"]
                    nfs_ip = match["nfs_ip"]
                    prev_backup_time = match["previous_backup_time"]
                    is_full_backup = match["is_full_backup"]
                    backup_count = match["backup_count"]
                    backup_ts = match["backup_timestamp"]
                    snapshot_uuid = match["snapshot_uuid"]

                    # Avoid rescanning the same snapshot with the same or newer backup timestamp
                    with scanned_images_lock:
                        if snapshot_path in scanned_backups and scanned_backups[snapshot_path] >= backup_ts:
                            print(f"Skipping snapshot {snapshot_path}: already scanned",flush=True)
                            continue
                        scanned_backups[snapshot_path] = backup_ts
                        save_scanned_images()

                    # Submit to thread pool
                    executor.submit(
                        process_task,
                        match,
                        nfs_ip,
                        current_rules_version,
                        is_full_backup,
                        backup_count,
                        prev_backup_time,
                        snapshot_uuid,
                        args["force_full_scan"],
                    )
            else:
                print("No matched parts to process.",flush=True)

            print("Processing complete. Waiting 15 minutes for the next cycle...",flush=True)
            wait_start = time.time()
            while time.time() - wait_start < 900 and not should_exit.is_set():
                time.sleep(1)

    except KeyboardInterrupt:
        print("Processing stopped by user.",flush=True)
    except Exception as e:
        print("Unhandled exception occured:", e,flush=True)
    finally:
        print("Shutting down. Attempting to clean up resources...",flush=True)
        should_exit.set()
        
        # Force unmount all mount points with short timeouts
        for mp in (IMAGE_MOUNT_POINTS + NFS_MOUNT_POINTS):
            try:
                if os.path.ismount(mp):
                    print(f"Force unmounting {mp}...",flush=True)
                    if "img" in mp:
                        subprocess.run(["sudo", "guestunmount", mp], check=False, timeout=2)
                    else:
                        subprocess.run(["sudo", "umount", "-lf", mp], check=False, timeout=2)
            except Exception as e:
                print(f"Error unmounting {mp}: {e}",flush=True)
        
        # Shutdown executor with proper error handling
        print("Shutting down thread pool...",flush=True)
        try:
            executor.shutdown(wait=True, timeout=3)
        except TypeError:
            # Fallback if Python version doesn't support timeout
            executor.shutdown(wait=True)
        except Exception as e:
            print(f"Error during executor shutdown: {e}",flush=True)
        
        print("All cleanup completed. Exiting.",flush=True)