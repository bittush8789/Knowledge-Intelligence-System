# Loki Setup

## Purpose
Horizontally-scalable, highly-available, multi-tenant log aggregation system.

## Why chosen for this project
"Prometheus for logs" - lightweight and integrated with Grafana.

## Install (via Helm)
```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm install loki grafana/loki-stack
```

## Verify commands
```bash
kubectl get pods -l "app.kubernetes.io/name=loki"
```
