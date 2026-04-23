# Terraform Setup

## Purpose
Infrastructure as Code (IaC) for provisioning cloud resources.

## Why chosen for this project
Automates AWS EKS, RDS, and VPC setup to ensure reproducible environments.

## Install
- **Windows**: `choco install terraform`
- **Linux**: Download from official HashiCorp site or use `apt`.
- **Mac**: `brew install terraform`

## Verify commands
```bash
terraform version
```

## Example usage
```bash
terraform init
terraform plan
terraform apply
```

## Best practices
- Always use a remote backend (S3/DynamoDB).
- Use modular structure.
- Never commit `terraform.tfstate` or secrets.
