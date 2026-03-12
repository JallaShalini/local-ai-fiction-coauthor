# Local AI Fiction Coauthor

A **Local AI-powered creative writing assistant** that helps authors write immersive stories while maintaining consistent lore using a **Retrieval-Augmented Generation (RAG)** pipeline.

This project runs entirely **locally**, combining:

- FastAPI
- Sentence Transformers
- ChromaDB (Vector Database)
- Ollama (Local LLM)
- Docker

The system stores story lore in a vector database and retrieves relevant context to assist the AI in generating coherent story continuations.

---

# Project Architecture

User Prompt  
↓  
FastAPI API  
↓  
Embedding Service (Sentence Transformers)  
↓  
ChromaDB Vector Store  
↓  
Context Retrieval  
↓  
Prompt Builder  
↓  
Ollama LLM  
↓  
Generated Story

---

# Features

- Local LLM-powered storytelling
- Persistent lorebook using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Docker-based deployment
- FastAPI REST API
- Parameter tuning (temperature, top_p)
- Automated API tests

---

# Project Structure

local-ai-fiction-coauthor/
│
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── .env.example
│
├── prompts/
│   └── persona.md
│
├── docs/
│   └── parameter_effects.md
│
├── scripts/
│   └── wait_for_services.sh
│
├── src/
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_generate.py
│   │   ├── routes_lore.py
│   │   └── routes_health.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── rag_service.py
│   │   ├── ollama_service.py
│   │   ├── embedding_service.py
│   │   └── chroma_service.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── chunking.py
│       └── prompt_builder.py
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_lore_endpoint.py
│   └── test_generate_endpoint.py
│
└── .gitignore
