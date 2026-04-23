# GitHub Actions Setup

## Purpose
CI/CD platform integrated directly into GitHub.

## Why chosen for this project
Native integration with the repo for automated testing, building, and security scans.

## Configuration
- Go to Repository Settings -> Secrets and variables -> Actions.
- Add secrets:
    - `AWS_ACCESS_KEY_ID`: Your AWS access key.
    - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key.
    - `OPENAI_API_KEY`: Your OpenAI API key.
    - `DOCKERHUB_USERNAME`: Your Docker Hub username.
    - `DOCKERHUB_TOKEN`: Your Docker Hub personal access token.
    - `ARGOCD_SERVER`: Your ArgoCD server URL.
    - `ARGOCD_PASSWORD`: Your ArgoCD admin password.

## Verify commands
Check the "Actions" tab in your GitHub repository.

## Production recommendations
- Use environment protection rules.
- Use OIDC for AWS authentication instead of static keys.
