from services.retrieval.bm25_search import search_bm25
from services.retrieval.vector_search import search_qdrant


def hybrid_search(query: str, top_k: int = 5):

    # =========================================================
    # 1. Retrieve candidates (زيادة لتغطية أفضل)
    # =========================================================
    bm25_results = search_bm25(query, top_k=top_k * 5)
    vector_results = search_qdrant(query, top_k=top_k * 5)

    # =========================================================
    # 2. Build score dictionaries
    # =========================================================
    bm25_scores = {}
    vec_scores = {}

    # ---------------- BM25 ----------------
    for item in bm25_results:
        cid = item["chunk"]["doc_id"]
        bm25_scores[cid] = item["score"]

    # ---------------- Vector ----------------
    for item in vector_results:
        cid = item["chunk"]["doc_id"]
        vec_scores[cid] = item["score"]

    # =========================================================
    # 3. Normalize scores (VERY IMPORTANT)
    # =========================================================
    def normalize(scores_dict):
        if not scores_dict:
            return scores_dict

        max_score = max(scores_dict.values()) or 1.0
        return {k: v / max_score for k, v in scores_dict.items()}

    bm25_scores = normalize(bm25_scores)
    vec_scores = normalize(vec_scores)

    # =========================================================
    # 4. Weighted fusion (better than RRF)
    # =========================================================
    BM25_WEIGHT = 0.6
    VEC_WEIGHT = 0.4

    final_scores = {}

    all_ids = set(list(bm25_scores.keys()) + list(vec_scores.keys()))

    for cid in all_ids:
        final_scores[cid] = (
            BM25_WEIGHT * bm25_scores.get(cid, 0) +
            VEC_WEIGHT * vec_scores.get(cid, 0)
        )

    # =========================================================
    # 5. Merge metadata
    # =========================================================
    all_chunks = {}

    for item in bm25_results:
        chunk = item["chunk"]
        all_chunks[chunk["doc_id"]] = chunk

    for item in vector_results:
        chunk = item["chunk"]
        all_chunks[chunk["doc_id"]] = chunk

    # =========================================================
    # 6. Sort final results
    # =========================================================
    final_results = []

    for cid, score in sorted(final_scores.items(), key=lambda x: x[1], reverse=True):

        if cid in all_chunks:
            final_results.append({
                "chunk_id": cid,
                "score": float(score),
                "chunk": all_chunks[cid]
            })

    return final_results[:top_k]

# from services.retrieval.bm25_search import search_bm25
# from services.retrieval.vector_search import search_qdrant


# def hybrid_search(query: str, top_k: int = 5, k: int = 15):

#     bm25_results = search_bm25(query, top_k=top_k * 3)
#     vector_results = search_qdrant(query, top_k=top_k * 3)

#     scores = {}

#     # BM25
#     for rank, item in enumerate(bm25_results):
#         cid = item["chunk"]["doc_id"]
#         scores[cid] = scores.get(cid, 0) + 1 / (k + rank + 1)

#     # Embedding
#     for rank, item in enumerate(vector_results):
#         cid = item["chunk"]["doc_id"]
#         scores[cid] = scores.get(cid, 0) + 1 / (k + rank + 1)

#     # merge metadata
#     all_chunks = {}

#     for item in bm25_results:
#         chunk = item["chunk"]
#         all_chunks[chunk["doc_id"]] = chunk

#     for item in vector_results:
#         chunk = item["chunk"]
#         all_chunks[chunk["doc_id"]] = chunk

#     final_results = []

#     for cid, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
#         if cid in all_chunks:
#             final_results.append({
#                 "chunk_id": cid,
#                 "score": float(score),
#                 "chunk": all_chunks[cid]
#             })

#     return final_results[:top_k]