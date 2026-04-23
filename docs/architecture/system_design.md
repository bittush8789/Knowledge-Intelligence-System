# Phase 2: Target Enterprise Architecture

## 1. Overview
The new architecture transforms the monolithic Flask app into a distributed microservices system designed for high availability, security, and scalability on AWS EKS.

## 2. Component Breakdown

### 🎨 Frontend (Modern UI)
- **Framework**: Next.js 14 (React)
- **Styling**: Tailwind CSS + Shadcn UI
- **State Management**: React Query (Server state) + Zustand (Client state)
- **Features**: Real-time streaming AI responses, drag-and-drop uploads, interactive citations.

### ⚙️ Backend (API Gateway & Core)
- **Framework**: FastAPI (Asynchronous)
- **Validation**: Pydantic v2
- **Auth**: Clerk or Auth0 (OIDC)
- **Task Queue**: Celery with Redis for heavy document processing.

### 🧠 AI & LLMOps Layer
- **Orchestration**: LangGraph (Stateful multi-agent workflows)
- **RAG Pipeline**: Hybrid search (Dense + Sparse) with Re-ranking.
- **Evaluation**: Ragas + LangSmith for hallucination detection.
- **Tracing**: LangSmith for full prompt/latency visibility.

### 💾 Data Persistence
- **Relational**: PostgreSQL (via AWS RDS) for user data and file metadata.
- **Vector**: Qdrant (Distributed) for semantic embeddings.
- **Cache**: Redis (via AWS ElastiCache).
- **Blob**: AWS S3 for original document storage.

### 🚢 Infrastructure & DevOps
- **Containerization**: Docker (Distroless for security).
- **Orchestration**: AWS EKS (Kubernetes).
- **IaC**: Terraform (Modular design).
- **CI/CD**: GitHub Actions for automated building and deployment.
- **Security**: Trivy, Semgrep, Vault (Secrets).

## 3. High-Level Flow
1. **User** uploads a PDF via **Next.js**.
2. **FastAPI** saves metadata to **PostgreSQL** and triggers an async **Celery** task.
3. **Worker** extracts text, generates embeddings, and stores them in **Qdrant**.
4. **User** asks a question.
5. **AI Orchestrator (LangGraph)** retrieves context from **Qdrant**, calls **OpenAI/Claude**, and streams the response back.
6. **Prometheus/Loki** monitor performance and logs throughout the cycle.
