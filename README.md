# Knowledge Intelligence System - Enterprise SaaS Edition

This branch (`cicd`) contains the modernized, enterprise-grade transformation of the Knowledge Intelligence System.

## 🚀 Key Features
- **Modern Microservices**: Next.js 14 Frontend + FastAPI Backend.
- **Advanced AI**: Multi-agent RAG workflows using **LangGraph**.
- **Production Infrastructure**: **AWS EKS** (Kubernetes) managed via **Terraform**.
- **Full CI/CD**: Automated security scanning (Trivy, Semgrep) and CI/CD (GitHub Actions).
- **High Observability**: Prometheus, Grafana, Loki, and OpenTelemetry integration.

## 📁 Project Structure
- `frontend/`: Next.js application.
- `backend/`: FastAPI core service.
- `infra/`: Terraform and KIND configurations.
- `k8s/`: Kubernetes base and environment manifests.
- `docs/setup-guides/`: Comprehensive step-by-step installation manuals for every tool.
- `scripts/`: Master auto-setup and verification scripts.

## 🛠️ Getting Started
1. Install core tools following the [Setup Order](docs/setup-order.md).
2. Run the master setup script: `bash scripts/setup-tools.sh`.
3. Verify the installation: `bash scripts/verify-tools.sh`.
4. Follow the [KIND Guide](docs/setup-guides/kind-full-setup.md) to launch the cluster locally.

## 🛡️ Security & Quality
This repository follows the **Shift Left** security principle. All code is scanned during pre-commit and CI stages to ensure production readiness.
