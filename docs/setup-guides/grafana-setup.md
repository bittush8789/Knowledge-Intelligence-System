# Grafana Setup

## Purpose
The open observability platform for visualizing metrics.

## Why chosen for this project
Used to create stunning dashboards for system health and AI performance.

## Install (via Helm)
```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm install grafana grafana/grafana
```

## Configure
- Access UI: `kubectl port-forward svc/grafana 3000:80`
- Get password: `kubectl get secret grafana -o jsonpath="{.data.admin-password}" | base64 --decode`

## Verify commands
Check `localhost:3000` in your browser.
