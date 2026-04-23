# Redis Setup

## Purpose
In-memory data structure store, used as a database, cache, and message broker.

## Why chosen for this project
Caches LLM responses and acts as the broker for Celery async tasks.

## Install (via Docker)
```bash
docker run --name redis -p 6379:6379 -d redis
```

## Verify commands
```bash
docker exec -it redis redis-cli ping
```
