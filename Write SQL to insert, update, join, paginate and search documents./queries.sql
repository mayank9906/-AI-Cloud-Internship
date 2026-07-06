CREATE TABLE documents (

document_id SERIAL PRIMARY KEY,

filename VARCHAR(255) NOT NULL,

filepath TEXT NOT NULL,

filetype VARCHAR(50) NOT NULL,

upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

INSERT INTO documents (filename, filepath, filetype)
VALUES
('Contract.pdf','uploads/Contract.pdf','application/pdf'),
('Agreement.docx','uploads/Agreement.docx','application/docx'),
('Notice.pdf','uploads/Notice.pdf','application/pdf');

UPDATE documents
SET filename='Updated_Contract.pdf'
WHERE document_id=1;

SELECT
d.document_id,
d.filename,
c.chunk_number,
c.chunk_text

FROM documents d

INNER JOIN chunks c

ON d.document_id = c.document_id;

SELECT *
FROM documents
LIMIT 5
OFFSET 0;
SELECT *
FROM documents
LIMIT 5
OFFSET 5;

--Search File
SELECT *
FROM documents
WHERE filename LIKE '%Contract%';
--Search Pdf
SELECT *
FROM documents
WHERE filetype='application/pdf';   
