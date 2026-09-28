# Retrieval-Augmented Generation (RAG) Pipeline from Scratch

A beginner-friendly Retrieval-Augmented Generation (RAG) pipeline built from scratch in Python without using frameworks such as LangChain or LlamaIndex.

## Overview

This project demonstrates how a basic RAG system works internally, from loading documents to retrieving relevant information and generating an answer using a local Large Language Model (LLM).

### Pipeline

Documents → Cleaning → Chunking → Embeddings → Similarity Search → Retrieval → Prompt Construction → LLM Response

## How It Works

1. **Document Loading**  
   Loads Markdown and text documents from the `docs/` directory.

2. **Text Cleaning**  
   Cleans unnecessary whitespace and normalizes the document text.

3. **Chunking**  
   Splits documents into smaller paragraph-level chunks so relevant information can be retrieved more precisely.

4. **Embeddings**  
   Converts each text chunk into a numerical vector using the `all-MiniLM-L6-v2` Sentence Transformer model.

5. **Vector Store**  
   Stores the embeddings in memory using NumPy.

6. **Similarity Search**  
   Converts the user's question into an embedding and compares it with document embeddings using cosine similarity.

7. **Retrieval**  
   Selects the most relevant document chunks based on similarity scores.

8. **Prompt Construction**  
   Combines the user's question with the retrieved context.

9. **Generation**  
   Sends the context and question to a locally running Llama 3.2 model through Ollama to generate a grounded answer.

## Tech Stack

- Python
- Sentence Transformers
- NumPy
- Ollama
- Llama 3.2
- Embeddings
- Vector Similarity Search
- Retrieval-Augmented Generation (RAG)

## Project Structure

```text
diy-rag/
│
├── docs/
│   ├── python.md
│   ├── sql.md
│   ├── data_engineering.md
│   ├── machine_learning.md
│   ├── docker.md
│   └── rag.md
│
├── load_data.py
├── chunk_data.py
├── embed_data.py
├── vector_store.py
├── rag.py
├── .gitignore
└── README.md
