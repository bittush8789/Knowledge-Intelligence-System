# LangSmith Setup

## Purpose
Platform for debugging, testing, evaluating, and monitoring LLM applications.

## Why chosen for this project
Essential for production-grade AI observability and tracing.

## Configure
- Create account at [smith.langchain.com](https://smith.langchain.com/).
- Set env vars:
```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls__...
```

## Verify commands
Run a LangChain request and check the LangSmith dashboard.
