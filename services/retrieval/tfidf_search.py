import pickle
import json
import numpy as np

from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
from services.retrieval.query_tfidf import build_query_tfidf

BASE_DIR = Path(__file__).resolve().parents[2]

# Load TF-IDF model
with open(BASE_DIR / "output" / "tfidf" / "tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

# Load metadata
with open(
    BASE_DIR / "output" / "tfidf" / "tfidf_metadata.json",
    "r",
    encoding="utf-8"
) as f:
    metadata = json.load(f)


def search_tfidf(query: str, top_k: int = 5, min_score: float = 0.0):

    query_vector = build_query_tfidf(query)

    similarities = cosine_similarity(query_vector, tfidf_matrix)[0]

    similarities = np.array(similarities)

    ranked_indices = np.argsort(-similarities)

    results = []

    for idx in ranked_indices:

        score = float(similarities[idx])

        if score < min_score:
            continue

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