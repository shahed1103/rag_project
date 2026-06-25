import json
import numpy as np
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

COLLECTION_NAME = "rag_chunks"

client = QdrantClient(path="output/qdrant")


with open(
    "output/embeddings/embeddings_metadata.json",
    "r",
    encoding="utf-8"
) as f:
    metadata = json.load(f)

embeddings = np.load(
    "output/embeddings/embeddings.npy"
)

model = SentenceTransformer(MODEL_NAME)

embedding_size = model.get_sentence_embedding_dimension()

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
    size=embedding_size,
    distance=Distance.COSINE
    )
)

points = []

for idx, vector in enumerate(embeddings):

    payload = metadata[idx]

    points.append(
        PointStruct(
            id=idx,
            vector=vector.tolist(),
            payload=payload
        )
    )

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print("QDRANT INDEX BUILD DONE")
print(f"Indexed {len(points)} chunks")