CREATE TABLE document (

document_id SERIAL PRIMARY KEY,

filename VARCHAR(255) NOT NULL,

filepath TEXT NOT NULL,

filetype VARCHAR(50) NOT NULL,

upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE chunks (

chunk_id SERIAL PRIMARY KEY,

document_id INT NOT NULL,

chunk_text TEXT NOT NULL,

chunk_number INT NOT NULL,

FOREIGN KEY(document_id)

REFERENCES document(document_id)

ON DELETE CASCADE

);

INSERT INTO document (filename, filepath, filetype)
VALUES (
    'Contract.pdf',
    'uploads/Contract.pdf',
    'application/pdf'
);

INSERT INTO chunks (document_id, chunk_text, chunk_number)
VALUES
(1, 'This is chunk 1.', 1),
(1, 'This is chunk 2.', 2),
(1, 'This is chunk 3.', 3);
INSERT INTO chunks (document_id, chunk_text, chunk_number)
VALUES (1, 'Invalid Chunk', 1);

SELECT * FROM document;

SELECT * FROM chunks;
