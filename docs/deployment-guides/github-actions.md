# GitHub Actions Guide

This project uses GitHub Actions for automated testing and deployment.

## Workflows:
1. **CI Pipeline (`ci.yml`)**: Runs on every push. It lints your code and runs tests.
2. **Security Scan (`security.yml`)**: Scans your Docker images for vulnerabilities using Trivy.
3. **EKS Deployment (`deploy-eks.yml`)**: Automatically deploys the app to AWS when code is pushed to the `main` branch.

## Setup:
1. Go to your GitHub Repository -> Settings -> Secrets and variables -> Actions.
2. Add your AWS and Docker Hub credentials.
