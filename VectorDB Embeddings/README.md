# VectorDB Embeddings

## Objective

Generate vector embeddings for text chunks and store them in a Vector Database using Qdrant.

---

## Dataset

Text file containing 20 document chunks.

---

## Technologies Used

- Python 3
- Sentence Transformers
- Qdrant
- Docker

---

## Files Included

- main.py
- chunks.txt
- requirements.txt
- README.md
- Explanation.pdf
- Output.png

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Qdrant using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## How to Run

```bash
py -3.14 main.py
```

---

## Expected Output

- 20 text chunks converted into embeddings.
- Embeddings stored successfully in Qdrant.
- Collection `legal_chunks` created.
- All vectors visible in the Qdrant Dashboard.

---

## Learning Outcomes

- Generate vector embeddings.
- Store embeddings in a Vector Database.
- Understand semantic search.
- Work with Qdrant and Sentence Transformers.

---

## Author

**Mayank Makhija**  
Step Ahead Internship