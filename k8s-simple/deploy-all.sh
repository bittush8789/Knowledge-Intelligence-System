#!/bin/bash
# Script to deploy all manifests in order

echo "🚀 Starting deployment to Kubernetes..."

kubectl apply -f namespace.yaml
kubectl apply -f .

echo "✅ Deployment finished! Checking pods..."
kubectl get pods -n ai-platform
