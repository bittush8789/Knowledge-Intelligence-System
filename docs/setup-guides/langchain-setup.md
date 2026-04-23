# LangChain Setup

## Purpose
Framework for developing applications powered by large language models.

## Why chosen for this project
Standard library for RAG, chains, and LLM integrations.

## Install
```bash
pip install langchain langchain-openai langchain-community
```

## Example usage
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
llm.invoke("Hello world")
```
