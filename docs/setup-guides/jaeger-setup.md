# Jaeger Setup

## Purpose
Open source, end-to-end distributed tracing.

## Why chosen for this project
Tracks the lifecycle of an AI request across microservices to find bottlenecks.

## Install (in K8s)
```bash
kubectl apply -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/main/deploy/crds/jaegertracing.io_jaegers_crd.yaml
```

## Verify commands
```bash
kubectl get pods -l app=jaeger
```
