# Troubleshooting

## Common Issues

### 1. Docker context error
**Problem**: Docker daemon not running.
**Fix**: Start Docker Desktop or run `sudo systemctl start docker`.

### 2. Kubectl connection refused
**Problem**: Kubeconfig not set or cluster down.
**Fix**: Run `kind create cluster` or `aws eks update-kubeconfig`.

### 3. S3 Access Denied
**Problem**: Invalid IAM credentials.
**Fix**: Check `aws configure` and S3 bucket policies.

### 4. OpenAI API Timeout
**Problem**: Network issues or rate limits.
**Fix**: Check internet connection and API usage dashboard.
