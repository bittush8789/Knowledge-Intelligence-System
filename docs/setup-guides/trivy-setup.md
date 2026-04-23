# Trivy Setup

## Purpose
A comprehensive security scanner for containers and other artifacts.

## Why chosen for this project
Fast and accurate vulnerability scanning for Docker images.

## Install
- **Linux**: `wget -qO - https://aquasecurity.github.io/trivy-repo/dabest/public.key | sudo apt-key add - && echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list && sudo apt-get update && sudo apt-get install trivy`
- **Mac**: `brew install trivy`

## Verify commands
```bash
trivy --version
```

## Example usage
```bash
trivy image backend:latest
```
