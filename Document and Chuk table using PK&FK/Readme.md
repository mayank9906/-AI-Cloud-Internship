# Database Design - Documents and Chunks Tables

## Objective

Design a relational database schema to store uploaded documents and their corresponding text chunks using Primary Key (PK) and Foreign Key (FK) relationships.

---

## Database Name

legalai

---

## Tables

### 1. documents

Stores metadata of uploaded documents.

Columns:

- document_id (Primary Key)
- filename
- filepath
- filetype
- upload_time

---

### 2. chunks

Stores extracted text chunks of each document.

Columns:

- chunk_id (Primary Key)
- document_id (Foreign Key)
- chunk_text
- chunk_number

---

## Relationship

One Document → Many Chunks (1:N)

The `document_id` in the `chunks` table references the `document_id` in the `documents` table.

---

## Files Included

- database.sql
- Design_Document.pdf
- ERD.png
- Output.png
- README.md

---

## How to Execute

1. Open pgAdmin 4.
2. Create or select the `legalai` database.
3. Open the Query Tool.
4. Execute the `database.sql` file.
5. Verify the tables using:

```sql
SELECT * FROM documents;
SELECT * FROM chunks;
```

---

## Expected Output

- `documents` table created successfully.
- `chunks` table created successfully.
- Primary Key and Foreign Key relationship established.
- One document can have multiple chunks.

---

## Technologies Used

- PostgreSQL
- pgAdmin 4
- SQL

---

## Author

Mayank Makhija
Step Ahead Internship