# Eksctl Setup

## Purpose
The official CLI tool for Amazon EKS.

## Why chosen for this project
Simplifies EKS cluster creation and IAM management.

## Install
- **Windows**: `choco install eksctl`
- **Linux**: `curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp && sudo mv /tmp/eksctl /usr/local/bin`
- **Mac**: `brew install eksctl`

## Verify commands
```bash
eksctl version
```

## Example usage
```bash
eksctl create cluster --name my-eks --region us-east-1
```
