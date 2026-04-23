# Docker Setup

## Purpose
Containerization platform for packaging application and dependencies.

## Why chosen for this project
Ensures "it works on my machine" consistency across development and production.

## Install
- **Windows**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Linux**: Use the convenience script: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
- **Mac**: Install Docker Desktop.

## Start service commands
- **Linux**: `sudo systemctl start docker`
- **Win/Mac**: Open Docker Desktop.

## Verify commands
```bash
docker --version
docker run hello-world
```

## Best practices
- Use multi-stage builds.
- Use non-root users in Dockerfiles.
- Keep images small using alpine/distroless bases.
