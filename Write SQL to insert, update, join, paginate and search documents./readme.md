# SQL Operations on Documents and Chunks Database

## Objective

Perform basic SQL operations on the **documents** and **chunks** tables using PostgreSQL.

---

## Database

**Database Name:** `legalai`

---

## Tables Used

### documents

Stores metadata of uploaded documents.

Columns:

- document_id (Primary Key)
- filename
- filepath
- filetype
- upload_time

### chunks

Stores text chunks extracted from documents.

Columns:

- chunk_id (Primary Key)
- document_id (Foreign Key)
- chunk_text
- chunk_number

---

## SQL Operations Performed

- Create Tables
- Insert Records
- Update Records
- INNER JOIN
- Pagination (LIMIT & OFFSET)
- Search using WHERE and LIKE

---

## Files Included

- queries.sql
- README.md
- Explanation.pdf
- Output.png

---

## How to Execute

1. Open pgAdmin 4.
2. Create or select the **legalai** database.
3. Open the Query Tool.
4. Execute the SQL statements in `queries.sql`.
5. Verify the output using SELECT queries.

---

## Technologies Used

- PostgreSQL
- pgAdmin 4
- SQL

---

## Learning Outcomes

- Creating relational database tables.
- Working with Primary Key and Foreign Key relationships.
- Inserting and updating records.
- Retrieving data using INNER JOIN.
- Implementing pagination with LIMIT and OFFSET.
- Searching records using WHERE and LIKE.

---

## Author

**Mayank Makhija**  
Step Ahead Internship