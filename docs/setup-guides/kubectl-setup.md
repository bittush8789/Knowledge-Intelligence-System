# Kubectl Setup

## Purpose
The Kubernetes command-line tool for controlling K8s clusters.

## Why chosen for this project
Standard tool for managing KIND clusters locally and EKS clusters in AWS.

## Install
- **Windows**: `curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"`
- **Linux**: `curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"`
- **Mac**: `brew install kubectl`

## Verify commands
```bash
kubectl version --client
```

## Example usage
```bash
kubectl get pods
kubectl apply -f deployment.yaml
```
