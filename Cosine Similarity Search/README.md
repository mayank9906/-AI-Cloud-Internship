# Cosine Similarity Search using Qdrant

## Objective

Implement semantic search using cosine similarity with a Vector Database (Qdrant). The application converts text into embeddings, stores them in Qdrant, accepts a user query, and retrieves the Top-5 most similar text chunks.

---

## Technologies Used

- Python 3.14
- Sentence Transformers
- Qdrant Vector Database
- Docker
- qdrant-client

---

## Project Structure

```
Cosine Similarity Search/
│
├── main.py
├── chunks.txt
├── requirements.txt
├── README.md
├── Explanation.pdf
└── Output.png
```

---

## Workflow

1. Read text chunks from `chunks.txt`
2. Generate embeddings using SentenceTransformer
3. Create a Qdrant collection
4. Upload embeddings into Qdrant
5. Accept user search query
6. Convert query into an embedding
7. Perform cosine similarity search
8. Retrieve and display Top-5 most similar chunks

---

## Features

- Semantic Search
- Cosine Similarity
- Vector Embeddings
- Top-5 Result Retrieval
- Fast Vector Search using Qdrant

---

## Learning Outcomes

- Understanding Embeddings
- Working with Vector Databases
- Semantic Search
- Cosine Similarity
- Retrieval stage of RAG systems