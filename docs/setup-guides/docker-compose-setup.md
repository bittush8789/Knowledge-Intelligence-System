# Docker Compose Setup

## Purpose
Orchestrating multi-container Docker applications.

## Why chosen for this project
Simplifies local development by running DBs, AI services, and frontend with one command.

## Install
- **Windows/Mac**: Included with Docker Desktop.
- **Linux**: `sudo apt install docker-compose-plugin`

## Verify commands
```bash
docker compose version
```

## Example usage
```bash
docker compose up -d
docker compose down
```

## Production recommendations
Do not use Docker Compose for production scaling; use Kubernetes instead.
