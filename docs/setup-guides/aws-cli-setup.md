# AWS CLI Setup

## Purpose
The unified tool to manage your AWS services from the terminal.

## Why chosen for this project
Required for authenticating with AWS and managing EKS, S3, and RDS.

## Install
- **Windows**: [Download MSI Installer](https://awscli.amazonaws.com/AWSCLIV2.msi).
- **Linux**: `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install`
- **Mac**: `brew install awscli`

## Configure commands
```bash
aws configure
```

## Verify commands
```bash
aws --version
```
