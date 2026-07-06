--Create
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    filepath TEXT NOT NULL,
    filetype VARCHAR(100) NOT NULL,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chunks (
    chunk_id SERIAL PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_text TEXT NOT NULL,
    chunk_number INT NOT NULL,

    CONSTRAINT fk_document
    FOREIGN KEY (document_id)
    REFERENCES documents(document_id)
    ON DELETE CASCADE
);

--Insert
INSERT INTO documents (filename, filepath, filetype)
VALUES
('Contract.pdf', 'uploads/Contract.pdf', 'application/pdf'),
('Agreement.docx', 'uploads/Agreement.docx', 'application/docx'),
('Notice.pdf', 'uploads/Notice.pdf', 'application/pdf'),
('Invoice.pdf', 'uploads/Invoice.pdf', 'application/pdf'),
('LegalNotice.docx', 'uploads/LegalNotice.docx', 'application/docx'),
('Policy.pdf', 'uploads/Policy.pdf', 'application/pdf'),
('Terms.docx', 'uploads/Terms.docx', 'application/docx'),
('Evidence.pdf', 'uploads/Evidence.pdf', 'application/pdf'),
('CourtOrder.pdf', 'uploads/CourtOrder.pdf', 'application/pdf'),
('Affidavit.docx', 'uploads/Affidavit.docx', 'application/docx');

INSERT INTO chunks (document_id, chunk_text, chunk_number)
VALUES
(1, 'Contract Introduction', 1),
(1, 'Contract Terms', 2),
(2, 'Agreement Clause 1', 1),
(2, 'Agreement Clause 2', 2),
(3, 'Notice Information', 1),
(4, 'Invoice Details', 1),
(5, 'Legal Notice Body', 1),
(6, 'Policy Section', 1),
(7, 'Terms and Conditions', 1),
(8, 'Evidence Summary', 1),
(9, 'Court Order Details', 1),
(10, 'Affidavit Declaration', 1);

--Update
UPDATE documents
SET filename = 'Updated_Contract.pdf'
WHERE document_id = 1;

--Join
SELECT
    d.document_id,
    d.filename,
    d.filetype,
    c.chunk_id,
    c.chunk_number,
    c.chunk_text
FROM documents d
INNER JOIN chunks c
ON d.document_id = c.document_id;

--Pagination
SELECT *
FROM documents
LIMIT 5 OFFSET 0;

SELECT *
FROM documents
LIMIT 5 OFFSET 5;

--Search

--BY FILE
SELECT *
FROM documents
WHERE filename LIKE '%Contract%';

--BY Pdf
SELECT *
FROM documents
WHERE filetype = 'application/pdf';

--By Docs
SELECT *
FROM documents
WHERE filetype = 'application/docx';

