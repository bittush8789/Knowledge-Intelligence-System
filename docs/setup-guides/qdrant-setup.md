# Qdrant Setup

## Purpose
Vector Database for semantic similarity search.

## Why chosen for this project
High-performance, distributed vector search engine that supports complex filtering.

## Install (via Docker)
```bash
docker run -p 6333:6333 qdrant/qdrant
```

## Verify commands
```bash
curl http://localhost:6333/healthz
```
