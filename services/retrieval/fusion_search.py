from services.retrieval.tfidf_search import search_tfidf
from services.retrieval.bm25_search import search_bm25
from services.retrieval.vector_search import search_qdrant

def fusion_search(query: str, top_k: int = 20):

    tfidf_results = search_tfidf(query, top_k=20)

    bm25_results = search_bm25(query, top_k=20)

    vector_results = search_qdrant(query, top_k=20)

    scores = {}

    all_chunks = {}

    k = 60

    # TF-IDF
    for rank, item in enumerate(tfidf_results):

        chunk_id = item["chunk_id"]

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (k + rank + 1)
        )

        all_chunks[chunk_id] = item

    # BM25
    for rank, item in enumerate(bm25_results):

        chunk_id = item["chunk_id"]

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (k + rank + 1)
        )

        all_chunks[chunk_id] = item

    # Vector
    for rank, item in enumerate(vector_results):

        chunk_id = item["chunk_id"]

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (k + rank + 1)
        )

        all_chunks[chunk_id] = item

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for chunk_id, score in ranked[:top_k]:

        chunk = all_chunks[chunk_id]

        results.append({
            "score": float(score),
            "chunk_id": chunk["chunk_id"],
            "book_id": chunk["book_id"],
            "chapter_id": chunk["chapter_id"],
            "chapter_title": chunk["chapter_title"],
            "text": chunk["text"]
        })

    return results