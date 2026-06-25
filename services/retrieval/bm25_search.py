# services/retrieval/bm25_search.py

import pickle
import json
from pathlib import Path
from services.retrieval.query_bm25 import build_query_bm25

BASE_DIR = Path(__file__).resolve().parents[2]

# تحميل model
with open(BASE_DIR / "output" / "bm25" / "bm25_model.pkl", "rb") as f:
    bm25 = pickle.load(f)

# تحميل metadata
with open(BASE_DIR / "output" / "bm25" / "bm25_metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)


def search_bm25(query: str, top_k=5):

    query_tokens = build_query_bm25(query)

    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = []

    for idx in ranked_indices[:top_k]:
        score = float(scores[idx])

        chunk_meta = metadata[idx]

        results.append({
            "score": score,
            "chunk_id": chunk_meta["doc_id"],
            "book_id": chunk_meta["book_id"],
            "chapter_id": chunk_meta["chapter_id"],
            "chapter_title": chunk_meta["chapter_title"],
            "text": chunk_meta["chunk_text"]
        })

        if len(results) == top_k:
            break
            
    return results