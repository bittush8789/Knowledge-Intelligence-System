# Complete Deployment Flow (Step-by-Step)

Follow this guide to take your app from code to production.

---

## Stage 1: Local Run (Developer Mode)
1. **Clone**: `git clone <repo-url>`
2. **Install**: `pip install -r requirements.txt`
3. **Run**: `python app/main.py`
   - Access at `http://localhost:8080`

---

## Stage 2: Docker (Container Mode)
1. **Build**: `docker build -t ai-backend -f docker/backend.Dockerfile .`
2. **Run Compose**: `docker compose -f docker/docker-compose.yml up -d`
   - Access backend at `http://localhost:8000`

---

## Stage 3: KIND (Local Kubernetes)
1. **Create Cluster**: `kind create cluster --name ai-platform`
2. **Deploy**: 
   ```bash
   cd k8s-simple
   bash deploy-all.sh
   ```
3. **Verify**: `kubectl get pods -n ai-platform`

---

## Stage 4: AWS EKS (Cloud Production)
1. **Configure**: `aws configure`
2. **Create Cluster**: 
   ```bash
   eksctl create cluster --name ai-platform --region ap-south-1 --nodes 2
   ```
3. **Deploy**: `kubectl apply -f k8s-simple/`
4. **Verify**: `kubectl get nodes`

---

## Stage 5: CI/CD (Automation)
1. **Push**: `git add .`, `git commit -m "feat: deploy"`, `git push origin main`
2. **Monitor**: Go to GitHub "Actions" tab to see the auto-deploy process.
