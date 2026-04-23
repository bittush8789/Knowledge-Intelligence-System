#!/bin/bash
# Tool Verification Script

echo "--- Verifying Installed Tools ---"

git --version || echo "Git not installed"
docker --version || echo "Docker not installed"
kubectl version --client || echo "Kubectl not installed"
kind version || echo "KIND not installed"
helm version || echo "Helm not installed"
terraform version || echo "Terraform not installed"
aws --version || echo "AWS CLI not installed"
eksctl version || echo "Eksctl not installed"
python3 --version || echo "Python not installed"
node --version || echo "Node.js not installed"

echo "--- Verification Complete ---"
