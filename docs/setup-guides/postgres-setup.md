# PostgreSQL Setup

## Purpose
The world's most advanced open source relational database.

## Why chosen for this project
Stores user data, document metadata, and application state with ACID compliance.

## Install (via Docker)
```bash
docker run --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

## Verify commands
```bash
docker exec -it postgres psql -U postgres -c "SELECT 1;"
```
