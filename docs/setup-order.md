# Setup Order Guide

To setup the **Knowledge Intelligence System** enterprise platform, follow this exact order:

## 📊 Phase 1: Core Tools
1. **Git**: Clone the repository.
2. **Docker**: Required for everything else.
3. **Python**: Backend and AI logic.
4. **Node.js**: Frontend development.

## ☸️ Phase 2: Orchestration
5. **kubectl**: Manage Kubernetes.
6. **kind**: Local Kubernetes cluster.
7. **Helm**: Install K8s applications.

## ☁️ Phase 3: Cloud & IaC
8. **Terraform**: Provision AWS infrastructure.
9. **AWS CLI**: Authenticate with AWS.
10. **eksctl**: Manage EKS clusters.

---

### 🚀 Quick Start (Linux)
```bash
chmod +x scripts/setup-tools.sh
./scripts/setup-tools.sh
./scripts/verify-tools.sh
```
