# Security Guide (DevSecOps)

We keep the application secure using these simple practices.

## 1. Container Scanning
We use **Trivy** to check our Docker images for security holes.
Command: `trivy image bittush8789/ai-backend:latest`

## 2. Code Scanning
We use **Semgrep** to find bugs in the Python code.
Command: `semgrep scan .`

## 3. Secret Management
Never push your `.env` file to GitHub! Use GitHub Secrets or AWS Secrets Manager.
