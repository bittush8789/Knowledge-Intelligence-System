# Prometheus Setup

## Purpose
Open-source monitoring and alerting toolkit.

## Why chosen for this project
Standard for collecting metrics from Kubernetes nodes and pods.

## Install (via Helm)
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus
```

## Verify commands
```bash
kubectl get pods -l "app.kubernetes.io/name=prometheus"
```
