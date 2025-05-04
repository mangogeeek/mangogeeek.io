# GCP Cost Audit and Security Policy Cleanup Guide

This guide walks you through identifying cost-incurring networking resources and managing Cloud Armor policies using `gcloud` CLI.  The following commands are used via PowerShell.

* * *

## 🔍 1. Identify Networking Resources (Potential Cost Contributors)

### List VPC Networks

```bash
gcloud compute networks list
```

### List Compute Engine Instances

```bash
gcloud compute instances list
```

### List Global Load Balancers

```bash
gcloud compute load-balancers list --global
```

### List Regional Forwarding Rules

```bash
gcloud compute forwarding-rules list --regions=[REGION1],[REGION2],...
```

### List Firewall Rules

```bash
gcloud compute firewall-rules list
```

### List VPN Tunnels

```bash
gcloud compute vpn-tunnels list
```

### List VPN Gateways

```bash
gcloud compute vpn-gateways list
```

### List Interconnects

```bash
gcloud compute interconnects list
```

### List Interconnect Attachments

```bash
gcloud compute interconnect-attachments list
```

* * *

## 🔐 2. Authentication and Account Management

### Login to Google Cloud

```bash
gcloud auth login
```

### Login Without Browser (Headless)

```bash
gcloud auth login --no-launch-browser
```

### Activate Service Account with Key File

```bash
gcloud auth activate-service-account SERVICE_ACCOUNT_EMAIL --key-file=PATH_TO_KEY_FILE
```

### List Authenticated Accounts

```bash
gcloud auth list
```

### Logout All Accounts

```bash
gcloud auth revoke --all
```

* * *

## 👥 3. IAM Permissions Management

### Grant IAM Role to a User

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member="user:your_email@example.com" --role="ROLE_NAME"
```

### Grant IAM Role to a Service Account

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:YOUR_SERVICE_ACCOUNT_EMAIL" --role="ROLE_NAME"
```

### Get IAM Policy and Filter by Principal (with jq)

```bash
gcloud projects get-iam-policy PROJECT_ID --format="json" | jq '.bindings[] | select(.members[] | contains("PRINCIPAL_IDENTIFIER"))'
```

### Extract Roles for a Principal (with jq)

```bash
gcloud projects get-iam-policy PROJECT_ID --format="json" | jq '.bindings[] | select(.members[] | contains("PRINCIPAL_IDENTIFIER")) | .role'
```

### Get Service Account IAM Policy

```bash
gcloud iam service-accounts get-iam-policy SERVICE_ACCOUNT_EMAIL --format="json" | jq ".bindings[].role"
```

* * *

## ⚙️ 4. Project Configuration and Permissions Checks

### Check Active Project

```bash
gcloud config get project
```

### Set Active Project

```bash
gcloud config set project mangogeek
```

### IAM Policy Lookup

```bash
gcloud projects get-iam-policy hycu-learning --format="json" | jq ".bindings[] | select(.members[] | contains(\"serviceAccount:mangogeekdefault@mangogeek.iam.gserviceaccount.com\"))"
```

### Activate Service Account

```bash
gcloud auth activate-service-account mangogeekdefault@mangogeek.iam.gserviceaccount.com --key-file="G:\My Drive\keys\GCP_Private_Key\mangogeeek_personal\mangogeek-14ffa7df3bbe.json"
```

* * *

## 🛡️ 5. Managing Cloud Armor Security Policies

### List Security Policies

```bash
gcloud compute security-policies list --format="table(name,description)"
```

### Describe Security Policy Rules

```bash
gcloud compute security-policies describe custom-security-policy-for-backend-service-web-backend-service --format="table(rules.priority, rules.action, rules.match.versionedExpr, rules.description)"
gcloud compute security-policies describe default-security-policy-for-backend-service-web-backend-service --format="table(rules.priority, rules.action, rules.match.versionedExpr, rules.description)"
```

### Delete Unused Security Policies

```bash
gcloud compute security-policies delete custom-security-policy-for-backend-service-web-backend-service --project=mangogeek
gcloud compute security-policies delete default-security-policy-for-backend-service-web-backend-service --project=mangogeek
```

* * *

## ✅ Final Checklist

- [x] Validated active GCP project and service account
- [x] Listed and reviewed cost-heavy networking resources
- [x] Inspected and cleaned up unused Cloud Armor security policies
- [x] Verified IAM roles for service account access
