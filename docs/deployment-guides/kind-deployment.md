# KIND Kubernetes Deployment Guide

This guide explains how to deploy the application to a local Kubernetes cluster using KIND.

## 1. Create a KIND Cluster
```bash
kind create cluster --name ai-platform
```

## 2. Deploy All Resources
Go to the `k8s-simple` folder and run the deploy script:
```bash
cd k8s-simple
bash deploy-all.sh
```

## 3. Verify the Deployment
Check if all pods are running:
```bash
kubectl get pods -n ai-platform
```

## 4. Access the App
Since we use Ingress, you might need to port-forward or use the internal cluster IP. For a simple check:
```bash
kubectl port-forward svc/frontend-service 3000:80 -n ai-platform
```
Open `http://localhost:3000` in your browser.

## 5. Delete the Cluster
```bash
kind delete cluster --name ai-platform
```
