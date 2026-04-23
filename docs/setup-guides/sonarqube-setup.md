# SonarQube Setup

## Purpose
Automatic code review tool to detect bugs, vulnerabilities, and code smells.

## Why chosen for this project
Provides a high-level dashboard of code quality and security health.

## Install (via Docker)
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
```

## Verify commands
Check `localhost:9000`.
