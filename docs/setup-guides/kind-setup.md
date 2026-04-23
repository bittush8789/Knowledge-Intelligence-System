# KIND Setup

## Purpose
Kubernetes in Docker - local development tool for running K8s clusters.

## Why chosen for this project
Lightweight, fast, and perfect for testing production manifests locally.

## Install
- **Windows**: `curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.22.0/kind-windows-amd64.exe`
- **Linux**: `[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64`
- **Mac**: `brew install kind`

## Start service commands
```bash
kind create cluster --name ai-platform
```

## Verify commands
```bash
kind get clusters
kubectl cluster-info
```

## Production recommendations
KIND is for development/CI only. Use EKS for production.
