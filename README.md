RAG-Based Document Question Answering System using Langchain

Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline that enables intelligent, context-aware question answering over a collection of PDF documents. It combines local knowledge retrieval with LLM-based reasoning to deliver precise, grounded answers instead of generic or hallucinated responses.

The system uses LangChain as its orchestration layer, FAISS and ChromaDB as vector stores, Sentence Transformers for embeddings, and Llama (via Groq API) for generation — providing a complete end-to-end RAG workflow.

Key Features:-

LLM Generation via Groq API (Llama Model):
Utilises the Llama model hosted on Groq’s low-latency inference API for fast and efficient response generation.

Semantic Embeddings with Sentence Transformers:
Uses all-MiniLM-L6-v2 to generate high-quality dense embeddings representing the semantic meaning of text.

Efficient Vector Search with FAISS & ChromaDB:
Implements a hybrid vector storage setup where FAISS powers fast similarity search, while ChromaDB handles metadata and persistence.

LangChain Framework for RAG Orchestration:
Integrates loaders, splitters, retrievers, and LLMs into a unified RAG pipeline.

PDF Knowledge Base:
Ingests multiple PDFs, cleans, chunks, and stores their textual content for efficient retrieval and contextual question answering.

System Workflow

Data Ingestion:
PDF files are parsed using LangChain’s document loaders. Text is split into smaller chunks for embedding.

Embedding Generation:
Each chunk is vectorised using Sentence Transformer all-MiniLM-L6-v2.

Vector Storage:
Embeddings are indexed using FAISS for similarity search and stored in ChromaDB for persistence.

Query Processing:
User queries are embedded and compared with stored vectors to retrieve top relevant chunks.

Response Generation:
Retrieved context is passed to the Llama model (via Groq API), which generates a coherent and context-aware response.

Tech Stack
Language Model (LLM)	Llama (served via Groq API)
Embedding Model	Sentence Transformers – all-MiniLM-L6-v2
Vector Stores	FAISS + ChromaDB
Framework	- LangChain
Knowledge Base	PDF Documents
Language	Python 3.13

Example Use Cases

Q&A over research papers, healthcare reports, or technical documentation

Enterprise knowledge assistants for internal policies and manuals

Customer support chatbots grounded in company documents

Educational assistants that answer from textbook PDFs

