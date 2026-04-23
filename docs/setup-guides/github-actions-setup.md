# GitHub Actions Setup

## Purpose
CI/CD platform integrated directly into GitHub.

## Why chosen for this project
Native integration with the repo for automated testing, building, and security scans.

## Configuration
- Go to Repository Settings -> Secrets and variables -> Actions.
- Add secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `OPENAI_API_KEY`, `DOCKER_PASSWORD`.

## Verify commands
Check the "Actions" tab in your GitHub repository.

## Production recommendations
- Use environment protection rules.
- Use OIDC for AWS authentication instead of static keys.
