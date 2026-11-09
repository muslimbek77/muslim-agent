# Muslim Agent RAG Implementation Report

## Overview
This document records the refactor and RAG update performed for the Muslim Agent project. The purpose was to split the single-file script into a clearer modular structure, add file-operation utilities, and integrate a lightweight vector-based retrieval layer backed by the provided knowledge base markdown file.

## Architecture changes
The project was split into the following files:

- `config.py` — environment and model configuration.
- `file_tools.py` — project file reading, writing, listing, and context generation.
- `rag_store.py` — Markdown chunk parsing and vector-based retrieval logic.
- `agent.py` — conversational agent and command loop.
- `main.py` — application entry point.

This separation makes the code easier to understand, test, and extend.

## RAG flow
The workflow now works as follows:

1. The system loads `muslim_agent_rag_knowledge_base.md`.
2. The markdown is split into `## CHUNK` sections.
3. Each chunk is normalized and converted into a simple vector representation using a lightweight bag-of-words embedding via NumPy.
4. A user query is also converted into the same vector space.
5. Cosine similarity is used to rank the most relevant chunks.
6. The best matching chunks are appended to the prompt before sending the request to Anthropic Claude.

This gives the agent a retrieval step that can answer questions using stored project context rather than relying only on the current chat history.

## Comments and maintainability
Each new module includes short docstrings and targeted comments to explain the purpose of the logic. The file commands are isolated in `file_tools.py`, the retrieval logic in `rag_store.py`, and the runtime loop in `agent.py`.

## Validation
The project was validated by importing the new modules and running a lightweight smoke test that:
- loaded the knowledge base
- retrieved relevant chunks from a sample prompt
- executed the agent loop with a stubbed API response

The result confirmed that the modularized code loads and responds correctly.

## Final note
This is a lightweight, dependency-friendly implementation of RAG designed to work in a local development environment without requiring a large external vector database service. It is easy to evolve into ChromaDB or FAISS later if the project grows.
