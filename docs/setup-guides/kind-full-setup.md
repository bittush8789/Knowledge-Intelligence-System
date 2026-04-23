# KIND Local Kubernetes Setup

## Why use KIND?
- **Cost**: $0 (Runs on your machine).
- **Speed**: Clusters start in < 2 minutes.
- **Reliability**: Perfect for testing K8s manifests before cloud deployment.
- **CI/CD**: Used in GitHub Actions for validation.

## 🚀 Step-by-Step Guide

### 1. Create the cluster
```bash
kind create cluster --name ai-platform --config infra/kind/kind-config.yaml
```

### 2. Build and load images
Build your local Docker image:
```bash
docker build -t backend:latest ./backend
```
Load it into KIND:
```bash
kind load docker-image backend:latest --name ai-platform
```

### 3. Install Ingress Nginx
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

### 4. Deploy Manifests
```bash
kubectl apply -f k8s/base/
```

### 5. Verify Pods
```bash
kubectl get pods -A
```

### 6. Access Locally
Open `http://localhost` in your browser.

### 7. Cleanup
```bash
kind delete cluster --name ai-platform
```
