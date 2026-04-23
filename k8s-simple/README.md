# Simple Kubernetes Deployment

This folder contains the basic manifests needed to run the AI platform.

## How to use:
1. Create a KIND cluster: `kind create cluster --name ai-platform`
2. Run the deploy script: `bash deploy-all.sh`
3. Verify: `kubectl get pods -n ai-platform`

## Files:
- `backend-deployment.yaml`: Runs the AI API.
- `frontend-deployment.yaml`: Runs the Web UI.
- `postgres-deployment.yaml`: Database for metadata.
- `redis-deployment.yaml`: Cache and message broker.
- `ingress.yaml`: Routes traffic from your browser to the services.
