# Helm Setup

## Purpose
The package manager for Kubernetes (The "App Store" of K8s).

## Why chosen for this project
Standardizes the deployment of third-party tools like Prometheus, Grafana, and ArgoCD.

## Install
- **Windows**: `choco install kubernetes-helm`
- **Linux**: `curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`
- **Mac**: `brew install helm`

## Verify commands
```bash
helm version
```

## Example usage
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install my-release prometheus-community/prometheus
```
