from qdrant_client import QdrantClient
from .query_embedding import build_query_embedding

# الاتصال بـ Qdrant المحلي
client = QdrantClient(path="output/qdrant")

COLLECTION_NAME = "rag_chunks"


def search_qdrant(query: str, top_k: int = 5):

    query_vector = build_query_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,
        score_threshold=0.2,
        search_params={"hnsw_ef": 128}
    )

    output = []

    for r in results.points:
        payload = r.payload

        output.append({
            "score": float(r.score),
            "chunk_id": payload.get("doc_id"),
            # "chunk_id": payload.get("chunk_id"),
            "book_id": payload.get("book_id"),
            "chapter_id": payload.get("chapter_id"),
            "chapter_title": payload.get("chapter_title"),
            "text": payload.get("chunk_text")
        })

    return output