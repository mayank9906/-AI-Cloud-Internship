CREATE TABLE document (
document_id SERIAL PRIMARY KEY,
filename VARCHAR(255),
filepath TEXT,
filetype VARCHAR(50),
upload_time TIMESTAMP
);

INSERT INTO document(filename,filepath,filetype,upload_time)
VALUES
('Contract.pdf','uploads/Contract.pdf','application/pdf',CURRENT_TIMESTAMP),
('Agreement.pdf','uploads/Agreement.pdf','application/pdf',CURRENT_TIMESTAMP),
('Invoice.pdf','uploads/Invoice.pdf','application/pdf',CURRENT_TIMESTAMP),
('LegalNotice.docx','uploads/LegalNotice.docx','application/docx',CURRENT_TIMESTAMP),
('CourtOrder.pdf','uploads/CourtOrder.pdf','application/pdf',CURRENT_TIMESTAMP);

EXPLAIN ANALYZE
SELECT *
FROM document
WHERE filename='Contract.pdf';
CREATE INDEX idx_filenames
ON document(filename);

