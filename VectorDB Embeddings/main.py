from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

# Create collection
client.recreate_collection(
    collection_name="legal_chunks",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

# Read text chunks
with open("chunks.txt", "r", encoding="utf-8") as file:
    chunks = [line.strip() for line in file.readlines() if line.strip()]

# Generate embeddings
embeddings = model.encode(chunks)

# Store vectors in Qdrant
points = []

for i, embedding in enumerate(embeddings):
    points.append(
        PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={
                "text": chunks[i]
            }
        )
    )

client.upsert(
    collection_name="legal_chunks",
    points=points
)

print(f"{len(points)} embeddings stored successfully in Qdrant!")
