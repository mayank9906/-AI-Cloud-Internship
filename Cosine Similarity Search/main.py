from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Connected to Qdrant successfully!")

# Read chunks from file
with open("chunks.txt", "r", encoding="utf-8") as file:
    chunks = [line.strip() for line in file if line.strip()]

print(f"Loaded {len(chunks)} chunks.")

# Generate embeddings
embeddings = model.encode(chunks)

print("Embeddings generated successfully!")

# Create Qdrant collection
collection_name = "legal_chunks"

client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

print("Collection created successfully!")

# Upload vectors to Qdrant
points = []

for i, embedding in enumerate(embeddings):
    points.append(
        PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding.tolist(),
            payload={
                "text": chunks[i]
            }
        )
    )

client.upsert(
    collection_name=collection_name,
    points=points
)

# Get search query from user
query = input("\nEnter your search query: ")

# Convert query into an embedding
query_vector = model.encode(query).tolist()

# Search for Top-5 similar chunks
results = client.query_points(
    collection_name=collection_name,
    query=query_vector,
    limit=5
).points

print("\nTop 5 Similar Chunks:\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. {result.payload['text']}")
    print(f"Similarity Score: {result.score:.4f}")
    print("-" * 60)
    

print(f"{len(points)} vectors uploaded successfully!")
