CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS pokemon (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type1 TEXT,
    type2 TEXT,
    base_experience INT,
    embeddings VECTOR(768)  -- Assuming 768-dimension embeddings for RAG
);
