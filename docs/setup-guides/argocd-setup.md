# ArgoCD Setup

## Purpose
Declarative, GitOps continuous delivery tool for Kubernetes.

## Why chosen for this project
Automates deployments by syncing the K8s state with the GitHub repo.

## Install (in K8s)
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Verify commands
```bash
kubectl get pods -n argocd
```

## Best practices
- Use the "App of Apps" pattern.
- Enable auto-sync with pruning.
